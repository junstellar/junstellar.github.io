#!/bin/bash
# Render one language's video from the seq_LL_sN frame sequences, then mux the
# preserved v4 audio track (audio_LL_v4.aac extracted from the existing mp4).
# Usage: render_v5.sh ko|en OUT.mp4
set -e
LANG=$1
OUT=$2
cd "$(dirname "$0")"

if [ "$LANG" = "ko" ]; then
  OFF=(9.66667 18.1 32.1 47.86667 57.26667)
  DUR=65.66667
else
  OFF=(7.53333 14.6 23.56667 33.73333 39.06667)
  DUR=44.86667
fi

echo "== per-scene encode =="
for n in 1 2 3 4 5 6; do
  ffmpeg -y -v error -framerate 30 -i seq_${LANG}_s${n}/%05d.png \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30 \
    scene_${LANG}_s${n}.mp4
done

echo "== xfade chain =="
# chain 6 scenes with 0.5s xfade at the given offsets
ffmpeg -y -v error \
  -i scene_${LANG}_s1.mp4 -i scene_${LANG}_s2.mp4 -i scene_${LANG}_s3.mp4 \
  -i scene_${LANG}_s4.mp4 -i scene_${LANG}_s5.mp4 -i scene_${LANG}_s6.mp4 \
  -filter_complex "\
[0][1]xfade=transition=fade:duration=0.5:offset=${OFF[0]}[a]; \
[a][2]xfade=transition=fade:duration=0.5:offset=${OFF[1]}[b]; \
[b][3]xfade=transition=fade:duration=0.5:offset=${OFF[2]}[c]; \
[c][4]xfade=transition=fade:duration=0.5:offset=${OFF[3]}[d]; \
[d][5]xfade=transition=fade:duration=0.5:offset=${OFF[4]}[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30 \
  video_${LANG}_v5.mp4

echo "== mux preserved v4 audio (trim to $DUR) =="
ffmpeg -y -v error -i video_${LANG}_v5.mp4 -i audio_${LANG}_v4.aac \
  -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 128k \
  -t $DUR -movflags +faststart "$OUT"

echo "== done: $OUT =="
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1 "$OUT"
