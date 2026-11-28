#!/bin/bash
# 补交缺失的 v4 段落（每段最多重试 3 次，输出前缀带 _retry 避免覆盖）
# 用法: bash analysis/retry_missing_v4.sh <实例ID>
set -u
ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
P="$ROOT_DIR/projects/初音未来_梦核_竖屏视频"
NAME="初音未来_梦核_竖屏视频"
MANIFEST="$P/analysis/manifest.json"
if [ $# -lt 1 ]; then echo "用法: bash analysis/retry_missing_v4.sh <实例ID>"; exit 1; fi
INST="$1"
for n in 2 3 4 5 6 7 8; do
  RNG=$(python3 -c "import json;m=json.load(open('$MANIFEST'));print([x['range'] for x in m if x['segment']==$n][0])")
  BG=$(python3 -c "import json;m=json.load(open('$MANIFEST'));print([x['bg'] for x in m if x['segment']==$n][0])")
  HIT=$(ls "$P/$RNG/output"/menghe_miku_v4_S${n}_*.mp4 2>/dev/null | head -1)
  if [ -n "$HIT" ]; then echo "== $RNG 已有输出，跳过"; continue; fi
  echo "===== RETRY $RNG ($BG) $(date '+%H:%M:%S') ====="
  for attempt in 1 2 3; do
    opc aigate --run --instance "$INST" \
      -w "$P/$RNG/${NAME}_${RNG}_workflow_api.json" \
      --reference-image "$ROOT_DIR/ref/character/初音未来/初音未来_三视图_1x1_v1.png" --reference-image-node 37 \
      --image "$ROOT_DIR/$BG" --load-image-node 60 \
      --audio "$P/$RNG/${NAME}_${RNG}_音频切片.mp3" --audio-node 52 \
      --output-prefix "MiniMaxH3/menghe_miku_v4_S${n}_retry" \
      --timeout 1800 \
      -o "$P/$RNG/output" 2>&1 | tee -a "$P/qa/${RNG}_run_v4.log"
    rc=${PIPESTATUS[0]}
    echo "== $RNG attempt $attempt rc=$rc"
    if [ $rc -eq 0 ]; then break; fi
    sleep 20
  done
done
echo "RETRY DONE"
