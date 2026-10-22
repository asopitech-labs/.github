#!/usr/bin/env python3
"""Add the synthesised sound to the rendered videos without re-encoding any picture.

    python3 audio_synth.py all          # makes out/audio/alopex-<format>.wav
    python3 mux_audio.py                # replaces each silent video in out/ with the version that has sound

Loudness is normalised to -16 LUFS integrated with a -1.5 dBTP ceiling, in two passes so the
correction is a single clean gain rather than a compressor working on the music. The picture
stream is copied bit for bit.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
TARGET = dict(I=-16.0, TP=-1.5, LRA=11.0)


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def has_audio(path: Path) -> bool:
    r = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(path)])
    return "audio" in r.stdout


def measure(wav: Path) -> dict:
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(wav), "-af",
             f"loudnorm=I={TARGET['I']}:TP={TARGET['TP']}:LRA={TARGET['LRA']}:print_format=json", "-f", "null", "-"])
    blob = r.stderr[r.stderr.rindex("{"):]
    return json.loads(blob[: blob.index("}") + 1])


def main() -> None:
    videos = sorted(p for p in OUT.glob("alopex-*.mp4") if not p.name.endswith(".part.mp4"))
    if not videos:
        sys.exit("no videos in out/ — run render_all.sh first")
    for video in videos:
        fmt = re.match(r"alopex-([a-z0-9]+)-(?:en|ja)\.mp4$", video.name)
        if not fmt:
            continue
        wav = OUT / "audio" / f"alopex-{fmt.group(1)}.wav"
        if not wav.exists():
            print(f"skip {video.name}: {wav.name} missing (run audio_synth.py)", file=sys.stderr)
            continue
        if has_audio(video):
            print(f"skip {video.name}: already has sound", file=sys.stderr)
            continue
        m = measure(wav)
        af = (f"afade=t=in:d=0.3,loudnorm=I={TARGET['I']}:TP={TARGET['TP']}:LRA={TARGET['LRA']}"
              f":measured_I={m['input_i']}:measured_LRA={m['input_lra']}:measured_TP={m['input_tp']}"
              f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
        part = video.with_name(video.stem + ".mux.part.mp4")
        r = run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
                 "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest",
                 "-movflags", "+faststart", str(part)])
        if r.returncode != 0 or not part.exists():
            part.unlink(missing_ok=True)
            sys.exit(f"ffmpeg failed on {video.name}:\n{r.stderr}")
        part.replace(video)                              # the silent render is replaced, not kept
        print(f"{video.name}: sound added (input {m['input_i']} LUFS -> {TARGET['I']})", file=sys.stderr)


if __name__ == "__main__":
    main()
