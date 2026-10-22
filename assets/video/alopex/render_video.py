#!/usr/bin/env python3
"""Assemble the Alopex DB commercial and short videos from generated keyframes.

The keyframes are pictures only (no text). Everything that says something — captions, the
code panel, the install lines, the lockup — is composed here, so the words stay real, editable
and translatable, and the artwork never has to be regenerated to change a sentence.

    python3 render_video.py commercial --lang en
    python3 render_video.py s1 --lang ja --draft          # half resolution, 15 fps: for checking
    python3 render_video.py commercial --lang en --audio music.wav

Formats: commercial (30 s, 1920x1080), s1 / s2 / s3 (shorts, 1080x1920). Output: out/<name>.mp4
Needs: ffmpeg on PATH, Pillow, numpy.
"""
from __future__ import annotations

import argparse
import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
NIGHT, DEEP = (11, 25, 41), (30, 58, 95)
SNOW, FROST, ICE, AURORA = (248, 250, 252), (184, 212, 227), (95, 180, 201), (126, 200, 227)

FONT_LATIN = "/System/Library/Fonts/Supplemental/Futura.ttc"            # index 0 = Medium, as in the lockups
FONT_JA = "/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"


# ----------------------------------------------------------------------------- copy
# Every sentence on screen. Claims are limited to what Alopex DB v0.8.16 ships today.
COPY = {
    "en": {
        "storm": ["Every scene", "has its storm."],
        "engine": ["One database engine."],
        "from": ["From an embedded file"],
        "to": ["to a distributed cluster."],
        "triad": ["SQL. Vector search.", "Columnar. One engine."],
        "family": ["Skulk: time series.", "Chirps: messaging."],
        "tag": ["Silent. Adaptive.", "Unbreakable."],
        "s1_hook": ["Survives", "in every scene."],
        "s1_end": ["Embedded file.", "Distributed cluster."],
        "s2_hook": ["One query.", "SQL and vectors."],
        "s2_end": ["Filter with SQL.", "Rank by similarity."],
        "s3_hook": ["Two lines."],
        "s3_end": ["Rust. Python.", "Embedded."],
        "url": "alopex-db.github.io",
        "sponsor": "github.com/sponsors/asopitech",
    },
    "ja": {
        "storm": ["どんな現場にも、", "嵐はある。"],
        "engine": ["ひとつの", "データベースエンジン。"],
        "from": ["組み込みの1ファイルから"],
        "to": ["分散クラスタまで。"],
        "triad": ["SQL。ベクトル検索。", "列指向。ひとつのエンジンで。"],
        "family": ["Skulk：時系列。", "Chirps：メッセージング。"],
        "tag": ["Silent. Adaptive.", "Unbreakable."],
        "s1_hook": ["あらゆるシーンで、", "生き残る。"],
        "s1_end": ["組み込みから、", "分散クラスタまで。"],
        "s2_hook": ["ひとつのクエリで。", "SQLとベクトル検索。"],
        "s2_end": ["SQLで絞り込み、", "類似度で並べる。"],
        "s3_hook": ["たった2行。"],
        "s3_end": ["Rust。Python。", "組み込み。"],
        "url": "alopex-db.github.io",
        "sponsor": "github.com/sponsors/asopitech",
    },
}

# The hybrid-search example from the README ("Hello, hybrid search"), abridged to the category filter.
SQL = [
    "SELECT content,",
    "       vector_similarity(embedding, ?)",
    "         AS score",
    "FROM knowledge_chunks",
    "WHERE category = 'research'",
    "ORDER BY score DESC",
    "LIMIT 5;",
]
INSTALL = ["cargo add alopex-embedded alopex-sql", "pip install alopex"]


# ----------------------------------------------------------------------------- fonts
_font_cache: dict = {}


def font(kind: str, size: int):
    key = (kind, size)
    if key not in _font_cache:
        path = {"latin": FONT_LATIN, "ja": FONT_JA, "mono": FONT_MONO}[kind]
        _font_cache[key] = ImageFont.truetype(path, size, index=0)
    return _font_cache[key]


def ease(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def window(t: float, t0: float, t1: float, fade: float = 0.45) -> float:
    """1 inside [t0, t1], with eased fades at both ends; 0 outside."""
    if t < t0 or t > t1:
        return 0.0
    return min(ease((t - t0) / fade), ease((t1 - t) / fade))


# ----------------------------------------------------------------------------- format
class Spec:
    def __init__(self, name: str, w: int, h: int, fps: int, dur: float):
        self.name, self.w, self.h, self.fps, self.dur = name, w, h, fps, dur
        self.tall = h > w


FORMATS = {
    "commercial": Spec("commercial", 1920, 1080, 30, 30.0),
    "s1": Spec("s1", 1080, 1920, 30, 15.0),
    "s2": Spec("s2", 1080, 1920, 30, 18.0),
    "s3": Spec("s3", 1080, 1920, 30, 12.0),
}


# ----------------------------------------------------------------------------- picture
class Scene:
    """One keyframe with a slow push-in; `start` is when it begins fading in over the previous."""

    def __init__(self, image: str, start: float, zoom=(1.0, 1.08), focus=(0.5, 0.5), xf: float = 0.55):
        self.image, self.start, self.zoom, self.focus, self.xf = image, start, zoom, focus, xf
        self._img: Image.Image | None = None

    def load(self, kf_dir: Path) -> Image.Image:
        if self._img is None:
            self._img = Image.open(kf_dir / self.image).convert("RGB")
        return self._img

    def frame(self, kf_dir: Path, spec: Spec, t_local: float, span: float) -> Image.Image:
        img = self.load(kf_dir)
        k = ease(t_local / max(span, 0.01))
        zoom = self.zoom[0] + (self.zoom[1] - self.zoom[0]) * k
        iw, ih = img.size
        # cover-crop to the output aspect, then zoom into the focus point
        target = spec.w / spec.h
        if iw / ih > target:
            cw, ch = ih * target, ih
        else:
            cw, ch = iw, iw / target
        cw, ch = cw / zoom, ch / zoom
        cx = min(max(self.focus[0] * iw, cw / 2), iw - cw / 2)
        cy = min(max(self.focus[1] * ih, ch / 2), ih - ch / 2)
        box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
        return img.resize((spec.w, spec.h), Image.BICUBIC, box=box)


def picture(scenes: list[Scene], kf_dir: Path, spec: Spec, t: float) -> Image.Image:
    ends = [s.start for s in scenes[1:]] + [spec.dur]
    idx = max(i for i, s in enumerate(scenes) if s.start <= t) if t >= scenes[0].start else 0
    cur = scenes[idx]
    xf = cur.xf
    cur_img = cur.frame(kf_dir, spec, t - cur.start, ends[idx] - cur.start + xf)
    if idx > 0 and t - cur.start < xf:
        prev = scenes[idx - 1]
        prev_img = prev.frame(kf_dir, spec, t - prev.start, ends[idx - 1] - prev.start + xf)
        return Image.blend(prev_img, cur_img, ease((t - cur.start) / xf))
    return cur_img


# ----------------------------------------------------------------------------- overlays
def _text_size(draw: ImageDraw.ImageDraw, text: str, fnt) -> tuple[int, int]:
    l, t, r, b = draw.textbbox((0, 0), text, font=fnt)
    return r - l, b - t


def caption(base: Image.Image, lines: list[str], lang: str, a: float, *, x: float, y: float,
            size: int, anchor: str = "left") -> None:
    """A caption on a night-navy plate, so it reads on bright snow as well as on dark sky."""
    if a <= 0:
        return
    fnt = font("ja" if lang == "ja" else "latin", size)
    probe = ImageDraw.Draw(base)
    sizes = [_text_size(probe, ln, fnt) for ln in lines]
    lh = int(size * 1.32)
    tw = max(w for w, _ in sizes)
    th = lh * len(lines)
    pad_x, pad_y = int(size * 0.62), int(size * 0.42)
    pw, ph = tw + pad_x * 2, th + pad_y * 2 - int(size * 0.18)
    px = int(x - pw / 2) if anchor == "center" else int(x)
    py = int(y + (1 - a) * 18)
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((px, py, px + pw, py + ph), radius=int(size * 0.5), fill=NIGHT + (int(205 * a),))
    # a short ice-blue rule at the left edge of the plate, the one accent
    d.rounded_rectangle((px + int(size * 0.22), py + pad_y, px + int(size * 0.22) + 5, py + ph - pad_y),
                        radius=3, fill=ICE + (int(255 * a),))
    for i, ln in enumerate(lines):
        d.text((px + pad_x + int(size * 0.18), py + pad_y - int(size * 0.12) + i * lh), ln,
               font=fnt, fill=SNOW + (int(255 * a),))
    base.paste(Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB"))


_TOKEN = re.compile(r"(SELECT|FROM|WHERE|ORDER BY|LIMIT|AS|DESC|AND)\b|(vector_similarity)|('[^']*')|(\d+)")


def _colour_runs(line: str):
    runs, pos = [], 0
    for m in _TOKEN.finditer(line):
        if m.start() > pos:
            runs.append((line[pos:m.start()], SNOW))
        col = ICE if m.group(1) else AURORA if m.group(2) else FROST if m.group(3) else (224, 181, 74)
        runs.append((m.group(0), col))
        pos = m.end()
    if pos < len(line):
        runs.append((line[pos:], SNOW))
    return runs


def code_panel(base: Image.Image, lines: list[str], shown: int, a: float, *, box, size: int,
               title: str, prompt: str = "") -> None:
    """A terminal-style panel; `shown` characters of the code are revealed, with a blinking cursor."""
    if a <= 0:
        return
    x0, y0, x1, _ = box
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # shrink the type until the longest line fits the panel, and size the panel to its lines
    longest = max((prompt + ln for ln in lines), key=len)
    avail = (x1 - x0) - 76
    width = d.textlength(longest, font=font("mono", size))
    if width > avail:
        size = max(10, int(size * avail / width))
    y1 = y0 + 78 + int(size * 1.55) * len(lines) + 38
    d.rounded_rectangle((x0, y0, x1, y1), radius=26, fill=(8, 18, 32, int(232 * a)), outline=DEEP + (int(255 * a),), width=2)
    for i, c in enumerate((ICE, FROST, DEEP)):                       # window dots
        d.ellipse((x0 + 26 + i * 26, y0 + 24, x0 + 40 + i * 26, y0 + 38), fill=c + (int(255 * a),))
    d.text((x0 + 120, y0 + 18), title, font=font("mono", int(size * 0.62)), fill=FROST + (int(190 * a),))
    fnt = font("mono", size)
    lh = int(size * 1.55)
    ty = y0 + 78
    remaining = shown
    for li, line in enumerate(lines):
        text = (prompt + line) if prompt else line
        if remaining <= 0:
            break
        vis = text[: remaining] if remaining < len(text) else text
        cx = x0 + 34
        offset = 0
        for run, col in _colour_runs(text):
            part = run[: max(0, len(vis) - offset)]
            if part:
                d.text((cx, ty), part, font=fnt, fill=col + (int(255 * a),))
                cx += d.textlength(part, font=fnt)
            offset += len(run)
        remaining -= len(text)
        if remaining < 0 or li == len(lines) - 1 and remaining == 0:
            pass
        ty += lh
    base.paste(Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB"))


def cursor(base: Image.Image, t: float, x: int, y: int, size: int, a: float) -> None:
    if a <= 0 or int(t * 2.2) % 2:
        return
    d = ImageDraw.Draw(base)
    d.rectangle((x, y + 4, x + int(size * 0.58), y + int(size * 1.15)), fill=ICE)


def veil(base: Image.Image, a: float) -> None:
    if a > 0:
        base.paste(Image.blend(base, Image.new("RGB", base.size, NIGHT), a))


def end_card(base: Image.Image, spec: Spec, copy: dict, lang: str, a: float, lockup: Image.Image,
             center: float = 0.5, dim: float = 1.0) -> None:
    """Lockup, the tagline, the URL, and one small line pointing at GitHub Sponsors."""
    if a <= 0:
        return
    veil(base, dim * a)
    lw = int(spec.w * ((0.40 if center != 0.5 else 0.46) if not spec.tall else 0.78))
    lk = lockup.resize((lw, int(lockup.height * lw / lockup.width)), Image.LANCZOS)
    lay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    lay.paste(lk, (int(spec.w * center - lw / 2), int(spec.h * (0.30 if not spec.tall else 0.36))), lk)
    alpha = lay.getchannel("A").point(lambda v: int(v * a))
    lay.putalpha(alpha)
    base.paste(Image.alpha_composite(base.convert("RGBA"), lay).convert("RGB"))
    s1 = int(spec.w * (0.034 if not spec.tall else 0.052))
    caption(base, copy["tag"], "en", a, x=spec.w * center, y=spec.h * (0.52 if not spec.tall else 0.50), size=s1, anchor="center")
    d = ImageDraw.Draw(base)
    fu = font("latin", int(s1 * 0.78))
    fs = font("latin", int(s1 * 0.52))
    ya = int(spec.h * (0.72 if not spec.tall else 0.66))
    for txt, fnt, col in ((copy["url"], fu, ICE), (copy["sponsor"], fs, FROST)):
        w, h = _text_size(d, txt, fnt)
        d.text((spec.w * center - w / 2, ya), txt, font=fnt, fill=tuple(int(NIGHT[i] + (col[i] - NIGHT[i]) * a) for i in range(3)))
        ya += int(h * 2.0)


# ----------------------------------------------------------------------------- timelines
def build(spec: Spec, lang: str, kf_dir: Path, lockup: Image.Image):
    """Return (scenes, draw) for a format. `draw(frame, t)` lays the overlays on a picture."""
    c = COPY[lang]
    W, H = spec.w, spec.h

    if spec.name == "commercial":
        scenes = [
            Scene("k1-blizzard.png", 0.0, (1.00, 1.10), (0.62, 0.55)),
            Scene("k5-slabs.png", 4.0, (1.00, 1.08), (0.32, 0.55)),
            Scene("k2-calm.png", 9.0, (1.00, 1.07), xf=0.30),
            Scene("k3-wind.png", 10.6, (1.00, 1.07), xf=0.16),
            Scene("k1-blizzard.png", 12.2, (1.06, 1.14), (0.60, 0.55), xf=0.16),
            Scene("k4-aurora.png", 13.8, (1.00, 1.08), xf=0.16),
            Scene("k5-slabs.png", 15.0, (1.12, 1.00), (0.32, 0.55)),
            Scene("k6-skulk.png", 21.0, (1.00, 1.08)),
            Scene("k7-chirps.png", 23.0, (1.00, 1.08)),
            Scene("k8-walking.png", 25.0, (1.00, 1.07)),
            Scene("k9-portrait.png", 27.6, (1.00, 1.04)),
        ]
        cs, cx = int(W * 0.030), int(W * 0.045)

        def draw(f: Image.Image, t: float):
            caption(f, c["storm"], lang, window(t, 0.5, 3.8), x=cx, y=H * 0.62, size=cs)
            caption(f, c["engine"], lang, window(t, 4.6, 8.7), x=W * 0.55, y=H * 0.30, size=cs)
            caption(f, c["from"], lang, window(t, 9.2, 11.8), x=W / 2, y=H * 0.06, size=cs, anchor="center")
            caption(f, c["to"], lang, window(t, 11.9, 15.0), x=W / 2, y=H * 0.06, size=cs, anchor="center")
            a = window(t, 15.4, 20.8)
            if a > 0:
                n = int(max(0.0, t - 16.0) / 4.2 * sum(len(s) for s in SQL))
                code_panel(f, SQL, n, a, box=(int(W * 0.52), int(H * 0.12), int(W * 0.97), int(H * 0.70)),
                           size=int(W * 0.0185), title="hybrid-search.sql")
            caption(f, c["triad"], lang, window(t, 16.0, 20.8), x=int(W * 0.60), y=H * 0.76, size=int(cs * 0.82))
            caption(f, c["family"], lang, window(t, 21.5, 24.8), x=W * 0.50, y=H * 0.07, size=int(cs * 0.9))
            a = window(t, 25.4, 27.4, 0.35)
            if a > 0:
                n = int(max(0.0, t - 25.7) / 1.8 * sum(len(s) + 2 for s in INSTALL))
                code_panel(f, INSTALL, n, a, box=(int(W * 0.06), int(H * 0.14), int(W * 0.60), int(H * 0.40)),
                           size=int(W * 0.0178), title="terminal", prompt="$ ")
            end_card(f, spec, c, lang, ease((t - 28.4) / 0.8), lockup)

    elif spec.name == "s1":
        scenes = [
            Scene("v1-blizzard.png", 0.0, (1.00, 1.10), (0.5, 0.6)),
            Scene("v2-aurora.png", 4.2, (1.00, 1.08)),
            Scene("v3-slabs.png", 8.4, (1.00, 1.08), (0.5, 0.7)),
        ]
        cs = int(W * 0.074)

        def draw(f: Image.Image, t: float):
            caption(f, c["s1_hook"], lang, window(t, 0.2, 3.9), x=W / 2, y=H * 0.14, size=cs, anchor="center")
            caption(f, c["s1_end"], lang, window(t, 8.9, 12.0), x=W / 2, y=H * 0.14, size=int(cs * 0.86), anchor="center")
            end_card(f, spec, c, lang, ease((t - 12.4) / 0.8), lockup)

    elif spec.name == "s2":
        scenes = [Scene("v3-slabs.png", 0.0, (1.00, 1.07), (0.5, 0.72))]
        cs = int(W * 0.072)

        def draw(f: Image.Image, t: float):
            caption(f, c["s2_hook"], lang, window(t, 0.2, 2.6), x=W / 2, y=H * 0.07, size=cs, anchor="center")
            a = window(t, 2.0, 14.4)
            if a > 0:
                n = int(max(0.0, t - 2.6) / 8.0 * sum(len(s) for s in SQL))
                code_panel(f, SQL, n, a, box=(int(W * 0.04), int(H * 0.16), int(W * 0.96), int(H * 0.46)),
                           size=int(W * 0.040), title="hybrid-search.sql")
            caption(f, c["s2_end"], lang, window(t, 11.4, 14.6), x=W / 2, y=H * 0.035, size=int(cs * 0.80), anchor="center")
            end_card(f, spec, c, lang, ease((t - 15.0) / 0.8), lockup)

    else:  # s3
        scenes = [Scene("v4-walking.png", 0.0, (1.00, 1.08), (0.5, 0.72))]
        cs = int(W * 0.088)

        def draw(f: Image.Image, t: float):
            caption(f, c["s3_hook"], lang, window(t, 0.2, 2.2), x=W / 2, y=H * 0.05, size=cs, anchor="center")
            a = window(t, 1.8, 8.6, 0.35)
            if a > 0:
                n = int(max(0.0, t - 2.2) / 3.4 * sum(len(s) + 2 for s in INSTALL))
                code_panel(f, INSTALL, n, a, box=(int(W * 0.04), int(H * 0.165), int(W * 0.96), int(H * 0.32)),
                           size=int(W * 0.0430), title="terminal", prompt="$ ")
            caption(f, c["s3_end"], lang, window(t, 6.0, 8.8), x=W / 2, y=H * 0.035, size=int(cs * 0.80), anchor="center")
            end_card(f, spec, c, lang, ease((t - 9.2) / 0.8), lockup)

    return scenes, draw


# ----------------------------------------------------------------------------- render
def render(args) -> Path:
    spec = FORMATS[args.format]
    if args.draft:
        spec = Spec(spec.name, spec.w // 2, spec.h // 2, 15, spec.dur)
    kf_dir = Path(args.kf_dir)
    lockup = Image.open(HERE / "brand" / "lockup-horizontal-dark.png").convert("RGBA")
    scenes, draw = build(spec, args.lang, kf_dir, lockup)
    out_dir = HERE / "out"
    out_dir.mkdir(exist_ok=True)
    suffix = ("-draft" if args.draft else "")
    out = out_dir / f"alopex-{args.format}-{args.lang}{suffix}.mp4"
    part = out.with_name(out.stem + f".{__import__('os').getpid()}.part.mp4")   # never write the real name directly

    total = int(round(spec.dur * spec.fps))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{spec.w}x{spec.h}", "-r", str(spec.fps), "-i", "-"]
    if args.audio:
        fade = f"afade=t=in:d=1.2,afade=t=out:st={spec.dur - 2.0}:d=2.0"
        cmd += ["-i", args.audio, "-af", fade, "-c:a", "aac", "-b:a", "192k", "-shortest"]
    cmd += ["-c:v", "libx264", "-preset", "slow" if not args.draft else "veryfast", "-crf", "17" if not args.draft else "26",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(part)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    stills = {float(s) for s in (args.stills or "").split(",") if s}
    still_dir = out_dir / "stills"
    if stills:
        still_dir.mkdir(exist_ok=True)
    pending = sorted(stills)
    try:
        for i in range(total):
            t = i / spec.fps
            frame = picture(scenes, kf_dir, spec, t)
            draw(frame, t)
            if pending and t >= pending[0]:
                frame.save(still_dir / f"{args.format}-{args.lang}-{pending[0]:05.2f}.png")
                pending.pop(0)
            proc.stdin.write(np.asarray(frame, dtype=np.uint8).tobytes())
            if i % spec.fps == 0:
                print(f"\r{args.format}/{args.lang}  {t:5.1f}s / {spec.dur:.0f}s", end="", file=sys.stderr)
    finally:
        proc.stdin.close()
        rc = proc.wait()
    if rc != 0 or not part.exists():
        part.unlink(missing_ok=True)
        raise SystemExit(f"ffmpeg failed (exit {rc}); {out.name} was not written")
    part.replace(out)
    print(f"\r{args.format}/{args.lang}  done -> {out}", file=sys.stderr)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("format", choices=sorted(FORMATS))
    ap.add_argument("--lang", choices=sorted(COPY), default="en")
    ap.add_argument("--draft", action="store_true", help="half resolution, 15 fps, fast encode")
    ap.add_argument("--audio", help="optional music track; faded in and out, trimmed to the video")
    ap.add_argument("--kf-dir", default=str(HERE / "keyframes"))
    ap.add_argument("--stills", help="comma-separated seconds at which to also save a PNG still")
    render(ap.parse_args())


if __name__ == "__main__":
    main()
