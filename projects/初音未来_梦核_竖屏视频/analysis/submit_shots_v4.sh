#!/bin/bash
# v4 提交脚本（全 8 段）：按时间序列子项目为每段上传对应场景背景图并提交
# 用法: bash analysis/submit_shots_v4.sh <实例ID>
set -u
ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
P="$ROOT_DIR/projects/初音未来_梦核_竖屏视频"
NAME="初音未来_梦核_竖屏视频"
MANIFEST="$P/analysis/manifest.json"
if [ $# -lt 1 ]; then echo "用法: bash analysis/submit_shots_v4.sh <实例ID>"; exit 1; fi
INST="$1"
for n in 1 2 3 4 5 6 7 8; do
  RNG=$(python3 -c "import json;m=json.load(open('$MANIFEST'));print([x['range'] for x in m if x['segment']==$n][0])")
  BG=$(python3 -c "import json;m=json.load(open('$MANIFEST'));print([x['bg'] for x in m if x['segment']==$n][0])")
  echo "===== SUBMIT $RNG ($BG) $(date '+%H:%M:%S') ====="
  opc aigate --run --instance "$INST" \
    -w "$P/$RNG/${NAME}_${RNG}_workflow_api.json" \
    --reference-image "$ROOT_DIR/ref/character/初音未来/初音未来_三视图_1x1_v1.png" --reference-image-node 37 \
    --image "$ROOT_DIR/$BG" --load-image-node 60 \
    --audio "$P/$RNG/${NAME}_${RNG}_音频切片.mp3" --audio-node 52 \
    --timeout 1800 \
    -o "$P/$RNG/output" 2>&1 | tee "$P/qa/${RNG}_run_v4.log"
  rc=${PIPESTATUS[0]}
  echo "===== $RNG rc=$rc ====="
done
echo "ALL SUBMISSIONS DONE"
