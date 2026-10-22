#!/usr/bin/env python3
"""Synthesise the music and sound effects for the Alopex DB videos.

Nothing here is sampled or downloaded: every sound is generated from oscillators and noise, so
there is no licence to track and every effect lands on the exact frame the picture changes.

    python3 audio_synth.py commercial          # -> out/audio/alopex-commercial.wav (+ -music.wav)
    python3 audio_synth.py all

The picture and the sound share one timetable. TIMELINE below is the audio side of the timings in
render_video.py; if a caption or a cut moves there, move it here too.

Palette: a calm arctic bed (slow pads, glassy bells, a soft pulse) that resolves from D minor to D major
at the end card. The three words of the project, Silent, Adaptive and Unbreakable, set the mix: quiet
bed, effects that are felt rather than shouted, and one clear lift at the close.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from render_video import INSTALL, SQL  # noqa: E402  (typed text, so keystrokes match the picture)

SR = 44100
OUT = HERE / "out" / "audio"


def hz(m: float) -> float:
    return 440.0 * 2 ** ((m - 69) / 12)


CHORDS = {   # (bass notes, pad notes) as MIDI numbers
    "Dm9":    ([38, 45], [50, 53, 57, 60, 64]),
    "Bbmaj7": ([46, 53], [58, 62, 65, 69]),
    "Fmaj7":  ([41, 48], [53, 57, 60, 64]),
    "Gm9":    ([43, 50], [55, 58, 62, 65, 69]),
    "D":      ([38, 45], [50, 54, 57, 62, 66]),   # the lift: D major
}

# Each video: chord changes, where the bells start, the pulse window, and every effect with its time.
TIMELINE = {
    "commercial": dict(
        dur=30.0, end=28.4, bells=5.0, pulse=(15.0, 27.4),
        chords=[(0, "Dm9"), (5, "Bbmaj7"), (10, "Fmaj7"), (15, "Gm9"), (20, "Bbmaj7"), (25, "Dm9"), (27.6, "D")],
        cuts=[(4.0, "soft"), (9.0, "soft"), (10.6, "gust"), (12.2, "gust"), (13.8, "calm"),
              (15.0, "soft"), (21.0, "soft"), (23.0, "soft"), (25.0, "soft"), (27.6, "soft")],
        captions=[0.5, 4.6, 9.2, 11.9, 16.0, 21.5], panels=[15.4, 25.4],
        typing=[(16.0, 4.2, SQL, ""), (25.7, 1.8, INSTALL, "$ ")], chimes=[20.4, 27.6 - 0.1],
        wind=[(0.0, 4.4, 1.0), (10.6, 12.2, 0.45), (12.2, 14.0, 1.0)], shimmer=[(13.8, 15.4)],
    ),
    "s1": dict(
        dur=15.0, end=12.4, bells=4.2, pulse=(8.4, 12.2),
        chords=[(0, "Dm9"), (4.2, "Bbmaj7"), (8.4, "Fmaj7"), (12.4, "D")],
        cuts=[(4.2, "calm"), (8.4, "soft")], captions=[0.2, 8.9], panels=[],
        typing=[], chimes=[], wind=[(0.0, 4.6, 1.0)], shimmer=[(4.2, 8.6)],
    ),
    "s2": dict(
        dur=18.0, end=15.0, bells=6.0, pulse=(6.0, 14.8),
        chords=[(0, "Dm9"), (6, "Bbmaj7"), (11, "Gm9"), (15, "D")],
        cuts=[], captions=[0.2, 11.4], panels=[2.0],
        typing=[(2.6, 8.0, SQL, "")], chimes=[10.8], wind=[], shimmer=[],
    ),
    "s3": dict(
        dur=12.0, end=9.2, bells=4.6, pulse=(4.6, 9.0),
        chords=[(0, "Dm9"), (4.6, "Bbmaj7"), (9.2, "D")],
        cuts=[], captions=[0.2, 6.0], panels=[1.8],
        typing=[(2.2, 3.4, INSTALL, "$ ")], chimes=[5.7], wind=[], shimmer=[],
    ),
}


# ----------------------------------------------------------------------------- building blocks
def env_ar(n: int, attack: float, release: float) -> np.ndarray:
    a, r = max(1, int(attack * SR)), max(1, int(release * SR))
    e = np.ones(n)
    e[:a] = np.linspace(0, 1, min(a, n)) ** 2
    if r < n:
        e[-r:] *= np.linspace(1, 0, r) ** 2
    return e


def lowpass(x: np.ndarray, fc: float, order: int = 2) -> np.ndarray:
    return signal.sosfilt(signal.butter(order, fc, "low", fs=SR, output="sos"), x)


def highpass(x: np.ndarray, fc: float, order: int = 2) -> np.ndarray:
    return signal.sosfilt(signal.butter(order, fc, "high", fs=SR, output="sos"), x)


def bandpass(x: np.ndarray, lo: float, hi: float, order: int = 2) -> np.ndarray:
    return signal.sosfilt(signal.butter(order, [lo, hi], "band", fs=SR, output="sos"), x)


def put(buf: np.ndarray, sig: np.ndarray, t: float, gain: float = 1.0, pan: float = 0.0) -> None:
    """Mix `sig` (mono) into the stereo buffer at time `t`, constant-power panned (-1 left .. +1 right)."""
    i = int(t * SR)
    if i >= buf.shape[0] or i + len(sig) <= 0:
        return
    s = sig[max(0, -i):]
    i = max(i, 0)
    n = min(len(s), buf.shape[0] - i)
    ang = (pan + 1) * np.pi / 4
    buf[i:i + n, 0] += s[:n] * gain * np.cos(ang)
    buf[i:i + n, 1] += s[:n] * gain * np.sin(ang)


def saw_voice(f: float, dur: float, detune_cents: float, phase: float) -> np.ndarray:
    t = np.arange(int(dur * SR)) / SR
    f2 = f * 2 ** (detune_cents / 1200)
    return signal.sawtooth(2 * np.pi * f2 * t + phase)


def pad(freqs: list[float], dur: float, bright: float = 1500.0) -> tuple[np.ndarray, np.ndarray]:
    """A warm slow pad: three detuned saws per note, low-passed; returns (left, right)."""
    n = int(dur * SR)
    l, r = np.zeros(n), np.zeros(n)
    for k, f in enumerate(freqs):
        for cents, side in ((-7, 0), (0, 2), (+7, 1)):
            v = saw_voice(f, dur, cents, 0.9 * k + side)
            (l if side != 1 else r)[:] += v / len(freqs)
            (r if side == 2 else l)[:] += 0.5 * v / len(freqs)
    env = env_ar(n, 1.3, 1.8)
    return lowpass(l, bright) * env, lowpass(r, bright) * env


def bell(f: float, dur: float = 2.4, bright: float = 2.2, tau: float = 0.9) -> np.ndarray:
    """A glassy FM bell: inharmonic modulator, index decaying with the amplitude."""
    t = np.arange(int(dur * SR)) / SR
    amp = np.exp(-t / tau)
    idx = bright * np.exp(-t / (tau * 0.6))
    s = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * 3.5 * t))
    s += 0.25 * np.sin(2 * np.pi * f * 2.0 * t) * np.exp(-t / (tau * 0.5))
    a = int(0.004 * SR)
    amp[:a] *= np.linspace(0, 1, a)
    return s * amp


def noise(n: int, rng: np.random.Generator) -> np.ndarray:
    return rng.standard_normal(n)


def wind(dur: float, level: float, rng: np.random.Generator) -> np.ndarray:
    """Wind: band-limited noise with slow, uneven gusts and a high whistle riding on top."""
    n = int(dur * SR)
    base = bandpass(noise(n, rng), 140, 1100)
    gust = lowpass(noise(n, rng), 0.7)                       # slow random gusts
    gust = 0.55 + 0.45 * np.tanh(gust / (np.std(gust) + 1e-9))
    whistle = bandpass(noise(n, rng), 1800, 3200) * (0.25 * gust ** 3)
    x = (base * gust + whistle)
    x /= np.max(np.abs(x)) + 1e-9
    return x * env_ar(n, 0.9, 1.1) * level


def whoosh(kind: str, rng: np.random.Generator) -> np.ndarray:
    dur = {"soft": 0.5, "gust": 0.8, "calm": 1.1}[kind]
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    x = noise(n, rng)
    bands = [bandpass(x, 180, 700), bandpass(x, 600, 2200), bandpass(x, 2000, 6000)]
    centre = np.array([0.15, 0.5, 0.85]) if kind != "gust" else np.array([0.1, 0.35, 0.6])
    out = sum(b * np.exp(-((t - c) ** 2) / (2 * 0.17 ** 2)) for b, c in zip(bands, centre))
    out /= np.max(np.abs(out)) + 1e-9
    e = np.sin(np.pi * t) ** (1.6 if kind == "soft" else 1.1)
    gain = {"soft": 0.45, "gust": 0.8, "calm": 0.4}[kind]
    if kind == "calm":                                       # the aurora cut: a bell under the air
        out = out * 0.6 + 0.0
    return out * e * gain


def key_click(rng: np.random.Generator, space: bool = False) -> np.ndarray:
    n = int(0.045 * SR)
    t = np.arange(n) / SR
    click = highpass(noise(n, rng), 2200) * np.exp(-t / 0.004)
    thump = np.sin(2 * np.pi * (110 if not space else 80) * t) * np.exp(-t / 0.012) * 0.7
    x = click * 0.9 + thump
    return x / (np.max(np.abs(x)) + 1e-9) * (0.55 if space else 1.0) * rng.uniform(0.55, 1.0)


def caption_tick(freq: float) -> np.ndarray:
    return bell(freq, 0.7, bright=1.2, tau=0.18) * 0.55


def panel_in() -> np.ndarray:
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * (320 + 700 * t) * t) * np.exp(-t / 0.09)
    return s * 0.35


def chime(rng: np.random.Generator) -> np.ndarray:
    out = np.zeros(int(2.6 * SR))
    for k, (m, d) in enumerate(((81, 0.0), (88, 0.11), (93, 0.24))):      # A5, E6, A6-ish rising
        b = bell(hz(m - 12 + 0), 2.2, tau=0.7) * (0.55 - 0.12 * k)
        i = int(d * SR)
        out[i:i + len(b)] += b[: len(out) - i]
    return out


def shimmer(dur: float) -> np.ndarray:
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * hz(m) * t + k) * (0.6 + 0.4 * np.sin(2 * np.pi * (0.3 + 0.11 * k) * t))
            for k, m in enumerate((86, 90, 93, 98)))
    return x / 4 * env_ar(n, dur * 0.4, dur * 0.45)


def sting(rng: np.random.Generator) -> np.ndarray:
    """The close: a bell chord in D major over a rising air swell."""
    n = int(4.5 * SR)
    out = np.zeros(n)
    for k, m in enumerate((74, 78, 81, 86)):            # D5 F#5 A5 D6
        b = bell(hz(m), 4.0, tau=1.6) * (0.5 - 0.06 * k)
        i = int(0.06 * k * SR)
        out[i:i + len(b)] += b[: n - i]
    air = lowpass(highpass(noise(n, rng), 2500), 8000) * env_ar(n, 0.9, 2.5) * 0.10
    return out + air


def sub(freq: float, dur: float) -> np.ndarray:
    n = int(dur * SR)
    t = np.arange(n) / SR
    return np.sin(2 * np.pi * freq * t) * env_ar(n, 1.0, 1.5)


def thump() -> np.ndarray:
    n = int(0.22 * SR)
    t = np.arange(n) / SR
    f = 58 + 40 * np.exp(-t / 0.03)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.07)


def reverb_ir(rng: np.random.Generator, seconds: float = 2.8) -> np.ndarray:
    n = int(seconds * SR)
    t = np.arange(n) / SR
    ir = np.stack([lowpass(noise(n, rng), 5500) * np.exp(-t / 0.75) for _ in range(2)], axis=1)
    ir[: int(0.012 * SR)] *= np.linspace(0, 1, int(0.012 * SR))[:, None]
    return ir / np.sqrt(np.sum(ir ** 2, axis=0, keepdims=True))


def wet(x: np.ndarray, ir: np.ndarray, length: int) -> np.ndarray:
    out = np.zeros((length, 2))
    for c in range(2):
        y = signal.fftconvolve(x[:, c], ir[:, c])
        out[:, c] = y[:length]
    return out


# ----------------------------------------------------------------------------- the mix
def build(name: str):
    tl = TIMELINE[name]
    rng = np.random.default_rng({"commercial": 11, "s1": 21, "s2": 31, "s3": 41}[name])
    n = int((tl["dur"] + 3.0) * SR)                      # a tail for the reverb; trimmed at the end
    music, sfx = np.zeros((n, 2)), np.zeros((n, 2))

    # ---- music: pad + sub, one voicing per chord, overlapping at the changes
    ch = tl["chords"]
    for i, (t0, cname) in enumerate(ch):
        t1 = ch[i + 1][0] if i + 1 < len(ch) else tl["dur"] + 2.0
        bass, upper = CHORDS[cname]
        dur = (t1 - t0) + 1.6
        l, r = pad([hz(m) for m in upper], dur)
        put(music, l, t0, 0.16, -0.35)
        put(music, r, t0, 0.16, 0.35)
        put(music, sub(hz(bass[0]), dur), t0, 0.10, 0.0)
        put(music, sub(hz(bass[1]), dur) * 0.6, t0, 0.12, 0.0)

    # ---- music: sparse glassy bells from the chord tones, thickening towards the end card
    grid = 0.3125
    k, t = 0, tl["bells"]
    stop = tl["end"] - 0.4
    while t < stop:
        cname = [c for s, c in ch if s <= t][-1]
        tones = [m + 12 for m in CHORDS[cname][1][1:]]
        p = 0.22 + 0.34 * (t - tl["bells"]) / max(stop - tl["bells"], 1)
        if rng.random() < p:
            put(music, bell(hz(int(rng.choice(tones))), 2.2) * 0.7, t, 0.12, float(rng.uniform(-0.6, 0.6)))
        t += grid
        k += 1
    # the lift: a D-major bell chord as the end card arrives
    for j, m in enumerate((74, 78, 81)):
        put(music, bell(hz(m), 3.5, tau=1.4), tl["end"] - 0.8 + 0.07 * j, 0.14, -0.3 + 0.3 * j)

    # ---- music: a soft pulse once the video starts to build
    p0, p1 = tl["pulse"]
    tt = p0
    while tt < p1:
        put(music, thump(), tt, 0.10, 0.0)
        tt += 1.25

    # ---- effects
    for (t0, t1, lvl) in tl["wind"]:
        put(sfx, wind(t1 - t0, lvl, rng), t0, 0.34, 0.0)
        put(sfx, wind(t1 - t0, lvl, rng), t0, 0.20, 0.0)       # a second, decorrelated layer for width
    for (t0, t1) in tl["shimmer"]:
        put(sfx, shimmer(t1 - t0), t0, 0.12, 0.0)
    for t0, kind in tl["cuts"]:
        put(sfx, whoosh(kind, rng), t0 - 0.12, 0.7, float(rng.uniform(-0.3, 0.3)))
    notes = [81, 84, 86, 88, 93]
    for i, t0 in enumerate(tl["captions"]):
        put(sfx, caption_tick(hz(notes[i % len(notes)])), t0 + 0.05, 0.62, float(rng.uniform(-0.4, 0.4)))
    for t0 in tl["panels"]:
        put(sfx, panel_in(), t0, 0.9, 0.0)
    for (t0, dur, lines, prompt) in tl["typing"]:
        total = sum(len(prompt + s) for s in lines)
        text = "".join(prompt + s for s in lines)
        for k2, chx in enumerate(text):
            put(sfx, key_click(rng, chx == " "), t0 + (k2 + 1) * dur / total, 0.62, float(rng.uniform(-0.15, 0.15)))
    for t0 in tl["chimes"]:
        put(sfx, chime(rng), t0, 0.5, 0.0)
    put(sfx, sting(rng), tl["end"], 0.55, 0.0)

    # ---- sidechain: the bed gives way a little whenever an effect speaks, so the effects need no extra level
    env = lowpass(np.abs(sfx).mean(axis=1), 9.0, 1)
    env = np.clip(env / (np.percentile(env, 97) + 1e-9), 0.0, 1.0)
    music *= (1.0 - 0.50 * env)[:, None]

    # ---- space: a shared hall, more on the bed than on the effects
    ir = reverb_ir(rng)
    music_mix = music + 0.32 * wet(music, ir, n)
    sfx_mix = sfx + 0.14 * wet(sfx, ir, n)
    return music_mix, sfx_mix, int(tl["dur"] * SR)


def finish(x: np.ndarray, length: int, tail: float = 1.6) -> np.ndarray:
    x = x[:length]
    f = int(tail * SR)
    x[-f:] *= np.linspace(1, 0, f)[:, None] ** 1.5
    x = highpass(x.T, 38).T
    x = np.tanh(x * 0.9) / np.tanh(0.9)                    # gentle saturation instead of hard clipping
    peak = np.max(np.abs(x)) + 1e-9
    return x / peak * 0.89                                  # about -1 dBFS


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("format", choices=[*TIMELINE, "all"])
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for name in (TIMELINE if args.format == "all" else [args.format]):
        music, sfx, length = build(name)
        full = finish(music * 0.85 + sfx, length)
        only = finish(music, length)
        sf.write(OUT / f"alopex-{name}.wav", full.astype(np.float32), SR, subtype="PCM_16")
        sf.write(OUT / f"alopex-{name}-music.wav", only.astype(np.float32), SR, subtype="PCM_16")
        print(f"{name}: {length / SR:.1f}s -> {OUT / f'alopex-{name}.wav'}", file=sys.stderr)


if __name__ == "__main__":
    main()
