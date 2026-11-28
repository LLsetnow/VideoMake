#!/bin/bash
# 拼接 8 个时间序列子项目的输出为 112.38s 成品并核验（无后期噪点，直接流复制）
# 用法: bash analysis/concat_qa.sh
set -u
ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
P="$ROOT_DIR/projects/初音未来_梦核_竖屏视频"
NAME="初音未来_梦核_竖屏视频"
mkdir -p "$P/output" "$P/qa"
LIST="$P/qa/concat_list.txt"
: > "$LIST"

echo "=== 1) 逐段核验 ==="
RANGES=(1-15秒 16-30秒 31-45秒 46-60秒 61-75秒 76-90秒 91-105秒 106-112秒)
for rng in "${RANGES[@]}"; do
  f=$(ls "$P/$rng/output"/*.mp4 2>/dev/null | grep -v 旧版 | grep -v 预览 | head -1)
  if [ -z "$f" ]; then echo "$rng: MISSING OUTPUT"; exit 1; fi
  echo "$rng -> $f"
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate -show_entries format=duration -of default=nw=1 "$f"
  ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,channels,sample_rate -of default=nw=1 "$f"
  echo "file '$f'" >> "$LIST"
done

echo "=== 2) 拼接 (concat, stream copy) ==="
ffmpeg -y -v error -f concat -safe 0 -i "$LIST" -c copy "$P/output/${NAME}_112s_v1.mp4"
echo "=== 3) 成品核验 ==="
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height,avg_frame_rate -of default=nw=1 "$P/output/${NAME}_112s_v1.mp4"
echo "=== 4) 对比原曲时长 ==="
ffprobe -v error -show_entries format=duration -of csv=p=0 "$P/analysis/梦核miku_纯音乐_v1.mp3"
