# Alopex DB videos

A 30-second commercial and three shorts, each in English and Japanese. Pictures come from
generated keyframes (`keyframes/`, no text in any of them); everything that says something is
composed by `render_video.py`, so a sentence can be changed without regenerating artwork.

```bash
./render_all.sh                    # picture, music, effects, mux: all eight videos -> out/
./render_all.sh commercial         # one format, both languages (sound is regenerated for all)
python3 render_video.py s2 --lang ja --draft     # half size, 15 fps, for checking layout
python3 audio_synth.py commercial  # just the sound -> out/audio/
python3 mux_audio.py               # add out/audio/*.wav to the rendered videos (the silent render is replaced)
```

Needs `ffmpeg`, Python 3, Pillow, numpy, scipy and soundfile. Fonts: Futura (Latin), Hiragino Maru Gothic (Japanese),
Menlo (code) — all system fonts on macOS.

| File | What |
|:--|:--|
| `STORYBOARD.md` | beats, captions in both languages, the claims policy, the keyframe list |
| `keyframes/` | 13 generated frames and `README.md` recording each prompt and its review |
| `render_video.py` | the compositor: push-ins, dissolves, captions, typed code, end card |
| `audio_synth.py` | music and effects, synthesised; one timetable shared with the picture |
| `mux_audio.py` | adds the sound (two-pass loudness to -16 LUFS), picture stream copied untouched, the silent render replaced |
| `brand/lockup-horizontal-dark.png` | the end-card lockup, copied from the brand kit |

## Where the videos live

On the owner's YouTube channel. They are **not** kept in git: the files are build output (4 to 17 MB
each), they regenerate in minutes with `./render_all.sh`, and a binary cannot be removed from a
repository's history later.

The generated keyframes are not in git either (`keyframes/*.png` is ignored). They exist only on the
owner's disk, and a generated picture cannot be reproduced exactly, so **they are the one thing that
cannot be rebuilt from this repository**. `keyframes/README.md` records the prompt and the review of
every frame, which is enough to generate a replacement set but not an identical one.

## Claims

Only what Alopex DB v0.8.16 ships. The SQL is the README's hybrid-search example; the install
lines are the published ones. Re-read the README before reusing this for a later version.

## Sound

Everything is synthesised, so there is nothing to license and every effect lands on the frame it belongs to.

- **Music**: a slow pad and glassy FM bells on a D minor progression that lifts to D major as the end card
  arrives; a soft pulse once the video starts to build; a quiet sub. Silent, Adaptive, Unbreakable set the
  mix: a bed you barely notice, effects felt rather than shouted, one clear lift at the close.
- **Effects**: wind that rises with the storm, a soft whoosh on each cut, a tick as each caption arrives,
  a keystroke for every character typed into the code panel (same count and timing as the picture), a
  chime when a query or command finishes, and a bell chord on the logo. The bed ducks under the effects.
- **Mix**: -16 LUFS integrated, true peak -1.5 dBTP, a normal level for web video.
- `out/audio/alopex-<format>-music.wav` is the music alone, to reuse elsewhere.
- No silent cut is kept: the videos are published with their music. `--audio your-track.wav` on `render_video.py` swaps in any track.

The levels, balance and timing are measured (loudness, spectrum, effect-to-bed ratio, keystroke
alignment within 2 ms). How the music *feels* has not been judged by ear: that is the owner's call.
