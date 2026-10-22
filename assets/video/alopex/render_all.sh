#!/bin/sh
# Render every video, in both languages, at full quality. Stills are saved at a few moments per video for review.
cd "$(dirname "$0")" || exit 1
for fmt in ${*:-commercial s1 s2 s3}; do
  case $fmt in
    commercial) ST="2.0,6.5,10.0,12.8,14.4,18.0,22.0,24.0,26.5,29.3";;
    s1) ST="1.5,6.0,10.5,13.5";;
    s2) ST="1.2,6.0,13.0,16.5";;
    s3) ST="1.0,5.0,7.5,11.0";;
  esac
  for lang in en ja; do
    python3 render_video.py "$fmt" --lang "$lang" --stills "$ST" 2>&1 | tr '\r' '\n' | tail -1
  done
done
# music and effects, then added to the picture without re-encoding it
python3 audio_synth.py all
python3 mux_audio.py
echo ALL_DONE
