#!/bin/bash
# v3 提交脚本：按时间序列子项目为每段上传对应场景背景图并提交
# 用法: bash analysis/submit_shots_v3.sh <实例ID>
set -u
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJ="projects/初音未来_梦核_竖屏视频"
NAME="初音未来_梦核_竖屏视频"
MANIFEST="$ROOT_DIR/$PROJ/analysis/manifest.json"
if [ $# -lt 1 ]; then echo "用法: bash analysis/submit_shots_v3.sh <实例ID>"; exit 1; fi
INST="$1"
RANGES=(1-15秒 16-30秒 31-45秒 46-60秒 61-75秒 76-90秒 91-105秒 106-112秒)
n=0
for rng in "${RANGES[@]}"; do
  n=$((n+1))
  BG=$(python3 -c "import json;m=json.load(open('$MANIFEST'));print([x['bg'] for x in m if x['segment']==$n][0])")
  echo "===== SUBMIT $rng ($BG) $(date '+%H:%M:%S') ====="
  opc aigate --run --instance "$INST" \
    -w "$PROJ/$rng/${NAME}_${rng}_workflow_api.json" \
    --reference-image "ref/character/初音未来/初音未来_三视图_1x1_v1.png" --reference-image-node 37 \
    --image "$BG" --load-image-node 60 \
    --audio "$PROJ/$rng/${NAME}_${rng}_音频切片.mp3" --audio-node 52 \
    --timeout 1800 \
    -o "$PROJ/$rng/output" 2>&1 | tee "$PROJ/qa/${rng}_run_v3.log"
  rc=${PIPESTATUS[0]}
  echo "===== $rng rc=$rc ====="
done
echo "ALL SUBMISSIONS DONE"
