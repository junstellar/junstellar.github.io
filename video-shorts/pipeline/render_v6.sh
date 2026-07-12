#!/bin/bash
# v6 render: S5 re-authored (see-description CTA) + shortened S5 narration, so the
# audio is FULLY re-mixed from tts_LL_v6 (narration adelay + BGM), NOT stream-copied
# from the old v4 track. S1-S4/S6 frames/timeline unchanged; only S5 shrinks and
# every offset/adelay after S5 shifts earlier.
# Usage: render_v6.sh ko|en OUT.mp4
set -e
LANG=$1
OUT=$2
cd "$(dirname "$0")"

if [ "$LANG" = "ko" ]; then
  OFF=(9.66667 18.1 32.1 47.86667 55.46667)
  ADEL=(300 9967 18400 32400 48167 55767)
  DUR=63.86667
  DFO=61.33667          # DUR - 2.53 (bgm fade-out start)
else
  OFF=(7.53333 14.6 23.56667 33.73333 38.6)
  ADEL=(300 7833 14900 23867 34033 38900)
  DUR=44.4
  DFO=41.87
fi

echo "== per-scene encode =="
for n in 1 2 3 4 5 6; do
  ffmpeg -y -v error -framerate 30 -i seq_${LANG}_s${n}/%05d.png \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30 \
    scene_${LANG}_s${n}.mp4
done

echo "== xfade chain =="
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
  video_${LANG}_v6.mp4

echo "== re-mix narration (tts_${LANG}_v6) + BGM, mux =="
ffmpeg -y -v error \
  -i video_${LANG}_v6.mp4 \
  -i tts_${LANG}_v6/scene1.mp3 -i tts_${LANG}_v6/scene2.mp3 \
  -i tts_${LANG}_v6/scene3.mp3 -i tts_${LANG}_v6/scene4.mp3 \
  -i tts_${LANG}_v6/scene5.mp3 -i tts_${LANG}_v6/scene6.mp3 \
  -stream_loop -1 -i bgm_pad.wav \
  -filter_complex "\
[1:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[0]}:all=1[a1]; \
[2:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[1]}:all=1[a2]; \
[3:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[2]}:all=1[a3]; \
[4:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[3]}:all=1[a4]; \
[5:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[4]}:all=1[a5]; \
[6:a]aresample=44100,aformat=channel_layouts=stereo,adelay=${ADEL[5]}:all=1[a6]; \
[a1][a2][a3][a4][a5][a6]amix=inputs=6:normalize=0[nm]; \
[nm]apad=whole_dur=${DUR}[narr]; \
[7:a]aformat=channel_layouts=stereo,volume=0.15,afade=t=in:d=1.5,atrim=0:${DUR},afade=t=out:st=${DFO}:d=2.5[bg]; \
[narr][bg]amix=inputs=2:normalize=0:duration=first[mix]" \
  -map 0:v:0 -map "[mix]" -c:v copy -c:a aac -b:a 128k \
  -movflags +faststart "$OUT"

echo "== done: $OUT =="
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate,nb_frames -of default=noprint_wrappers=1 "$OUT"
