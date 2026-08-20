#!/bin/bash
# Face-mosaic short render (clone of render_comfyui.sh). Per-scene encode ->
# xfade chain (0.5s x5) -> narration adelay+amix + looped BGM (volume 0.15,
# fadein 1.5, fadeout st=DUR-2.53 d=2.5, amix normalize=0), mux AAC.
# Timeline params come from render_params_${LANG}.sh (written by the generator).
# Frames: seq_facemosaic_${LANG}_s*, narration: tts_facemosaic_${LANG}/scene*.mp3.
# Usage: render_facemosaic.sh ko|en OUT.mp4
set -e
LANG=$1
OUT=$2
cd "$(dirname "$0")"
source "render_params_${LANG}.sh"

echo "== per-scene encode =="
for n in 1 2 3 4 5 6; do
  ffmpeg -y -v error -framerate 30 -i seq_facemosaic_${LANG}_s${n}/%05d.png \
    -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30 \
    scene_facemosaic_${LANG}_s${n}.mp4
done

echo "== xfade chain =="
ffmpeg -y -v error \
  -i scene_facemosaic_${LANG}_s1.mp4 -i scene_facemosaic_${LANG}_s2.mp4 -i scene_facemosaic_${LANG}_s3.mp4 \
  -i scene_facemosaic_${LANG}_s4.mp4 -i scene_facemosaic_${LANG}_s5.mp4 -i scene_facemosaic_${LANG}_s6.mp4 \
  -filter_complex "\
[0][1]xfade=transition=fade:duration=0.5:offset=${OFF[0]}[a]; \
[a][2]xfade=transition=fade:duration=0.5:offset=${OFF[1]}[b]; \
[b][3]xfade=transition=fade:duration=0.5:offset=${OFF[2]}[c]; \
[c][4]xfade=transition=fade:duration=0.5:offset=${OFF[3]}[d]; \
[d][5]xfade=transition=fade:duration=0.5:offset=${OFF[4]}[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -r 30 \
  video_facemosaic_${LANG}.mp4

echo "== narration + BGM mix, mux =="
ffmpeg -y -v error \
  -i video_facemosaic_${LANG}.mp4 \
  -i tts_facemosaic_${LANG}/scene1.mp3 -i tts_facemosaic_${LANG}/scene2.mp3 \
  -i tts_facemosaic_${LANG}/scene3.mp3 -i tts_facemosaic_${LANG}/scene4.mp3 \
  -i tts_facemosaic_${LANG}/scene5.mp3 -i tts_facemosaic_${LANG}/scene6.mp3 \
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
