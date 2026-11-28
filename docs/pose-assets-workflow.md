# 姿势参考图识别、归档、重命名与索引流程

本文用于把“彩色原图 + 对应深度图 + 可选骨骼图”整理为可复用的 `pose` 姿势参考资产，并同步登记到动作索引。流程适用于一批深度图文件名带有 `_depth` 后缀、骨骼图文件名带有 `_skeleton` 后缀的情况。

## 流程目标

完成后，每张姿势参考图应同时具备：

- `ref/pose/color/` 下的一张彩色原图；
- `ref/pose/depth/` 下的一张同名 `_depth.png` 深度图；
- `ref/pose/skeleton/` 下的一张同名 `_skeleton.png` 骨骼图；
- `ref/pose/pose.json` 中的动作对象、原图路径、深度图路径、骨骼图路径和姿势提示词描述；
- 基于画面内容、动作、身体位置和镜头关系生成的稳定文件名。

深度图只承担空间层次和姿势结构辅助职责。姿势提示词只描述身体朝向、四肢位置、主体位置、镜头角度、景别和透视，不写入角色身份、发型、脸部特征、服装、材质、颜色、背景、文字、水印或与姿势无关的道具信息。

## 目录约定

| 用途 | 路径 |
| --- | --- |
| 原始彩色图 | `ref/<来源目录>/` |
| 原始深度图 | `<源深度目录>/`（如果已有） |
| 姿势彩色图归档 | `ref/pose/color/` |
| 姿势深度图归档 | `ref/pose/depth/` |
| 姿势骨骼图归档 | `ref/pose/skeleton/` |
| 资产索引和提示词 | `ref/pose/pose.json` |

以本批次为例：

```text
原图：     ref/<来源目录>/<文件名>.jpg
深度图：   <源深度目录>/<文件名>_depth.png
目标原图： ref/pose/color/<重命名后的文件名>.jpg
目标深度： ref/pose/depth/<重命名后的文件名>_depth.png
目标骨骼： ref/pose/skeleton/<重命名后的文件名>_skeleton.png
索引：     动作索引中的同一个动作对象
```

## 1. 前置检查与范围确认

处理前先阅读根目录和目标目录最近的 `AGENTS.md`，确认 `ref/`、`docs/` 和 `pose.json` 的规则。检查当前工作区状态，不要因为批处理顺手清理、覆盖或暂存其他用户改动。

```bash
git status --short
find "<源深度目录>" -maxdepth 1 -type f -iname '*_depth.png' -print | sort -V
find "ref/<来源目录>" -maxdepth 1 -type f -print | sort -V
```

只处理真正的 `*_depth.png` 文件；`.DS_Store`、缩略图、临时文件和其他非深度图文件不属于批次。目标目录中已有的姿势资产不得覆盖，先检查重名：

```bash
test -e "ref/pose/color/<新文件名>.jpg" && echo "color collision"
test -e "ref/pose/depth/<新文件名>_depth.png" && echo "depth collision"
```

如果目标名已经存在，应先人工确认是否为同一份资产。除非用户明确要求替换，否则使用新版本名或停止处理该条目。

## 2. 生成深度图（如尚未生成）

如果只有彩色原图而没有对应深度图，可先使用本机的 Depth Anything V2 Small · Core ML F16 运行时生成。该步骤在 macOS 上执行，不依赖 ComfyUI；运行时资源属于本机环境，不写入仓库。

当前运行时约定如下：

```text
模型：       .runtime/depth_anything_v2_small_f16/DepthAnythingV2SmallF16.mlpackage
Python：     .runtime/depth_anything_v2_small_f16/venv/bin/python
生成脚本：   tools/depth_anything_macos.py
依赖清单：   tools/requirements-depth-anything-macos.txt
```

模型包和虚拟环境已经存在时可直接跳过安装。需要重建运行时时，从仓库根目录执行：

```bash
python3 -m venv .runtime/depth_anything_v2_small_f16/venv
.runtime/depth_anything_v2_small_f16/venv/bin/python -m pip install \
  -r tools/requirements-depth-anything-macos.txt
```

单张生成时，输入使用彩色原图，输出写到原始深度图目录，并保留原图 stem、添加 `_depth.png`：

```bash
SOURCE_COLOR_DIR="ref/pose/color"
SOURCE_DEPTH_DIR="ref/pose/depth"
DEPTH_PYTHON=".runtime/depth_anything_v2_small_f16/venv/bin/python"
DEPTH_SCRIPT="tools/depth_anything_macos.py"

mkdir -p "$SOURCE_DEPTH_DIR"
INPUT="$SOURCE_COLOR_DIR/<原图文件名>.jpg"
OUTPUT="$SOURCE_DEPTH_DIR/<原图文件名>_depth.png"

"$DEPTH_PYTHON" "$DEPTH_SCRIPT" "$INPUT" -o "$OUTPUT"
```

批量生成时，先确认原图目录和输出目录范围，再跳过已经存在的深度图，避免覆盖已验证结果：

```bash
SOURCE_COLOR_DIR="ref/pose/color"
SOURCE_DEPTH_DIR="ref/pose/depth"
DEPTH_PYTHON=".runtime/depth_anything_v2_small_f16/venv/bin/python"
DEPTH_SCRIPT="tools/depth_anything_macos.py"

mkdir -p "$SOURCE_DEPTH_DIR"
find "$SOURCE_COLOR_DIR" -maxdepth 1 -type f \
  \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' \) \
  -print | sort -V |
while IFS= read -r input_image_file; do
  image_filename="$(basename "$input_image_file")"
  image_stem="${image_filename%.*}"
  output_depth_file="$SOURCE_DEPTH_DIR/${image_stem}_depth.png"

  if test -e "$output_depth_file"; then
    printf 'SKIP existing: %s\n' "$(basename "$output_depth_file")"
    continue
  fi

  "$DEPTH_PYTHON" "$DEPTH_SCRIPT" \
    "$input_image_file" -o "$output_depth_file" || exit 1
done
```

生成脚本会将输入图按比例放入 Core ML 的固定输入尺寸 `518×392`，推理后用有效深度值的第 1～99 百分位归一化，再裁去留白并恢复到原图尺寸。输出应为与原图同宽高的 `PNG、8-bit grayscale` 相对深度图；它不是带真实物理距离单位的 metric depth，不应把不同图片的灰度值直接当作绝对距离比较。

生成后立即核验：

```bash
sips -g pixelWidth -g pixelHeight "$INPUT" "$OUTPUT"
file "$OUTPUT"
```

确认输出存在、宽高与输入一致、文件类型为 PNG 且显示 `8-bit grayscale` 后，再进入下一步的文件名匹配。若深度图已经存在但尺寸不符、格式不是灰度 PNG 或内容明显错位，应先重新生成到新版本文件，不能直接覆盖已验证结果。

## 2.5 生成 OpenPose 风格骨骼图（如尚未生成）

骨骼图使用本机的 DWPose ONNX 推理器检测人体、面部和手部关键点，再绘制为黑底、彩色肢体线的姿态图。它与深度图职责不同：深度图表达前后层次，骨骼图只表达关节位置和连接，不保留原图颜色、纹理和背景。

当前运行时约定如下：

```text
模型：       .runtime/pose_dwpose/checkpoints/dw-ll_ucoco_384.onnx
检测器：     .runtime/pose_dwpose/checkpoints/yolox_l.onnx
Python：     .runtime/pose_dwpose/venv/bin/python
生成脚本：   tools/pose_skeleton_macos.py
依赖清单：   tools/requirements-pose-dwpose-macos.txt
```

单张生成时，输入使用彩色原图，输出写到 `ref/pose/skeleton/`，保留原图 stem 并添加 `_skeleton.png`：

```bash
POSE_PYTHON=".runtime/pose_dwpose/venv/bin/python"
POSE_SCRIPT="tools/pose_skeleton_macos.py"
POSE_MODEL=".runtime/pose_dwpose/checkpoints/dw-ll_ucoco_384.onnx"
POSE_DETECTOR=".runtime/pose_dwpose/checkpoints/yolox_l.onnx"
INPUT="ref/pose/color/<文件名>.jpg"
OUTPUT="ref/pose/skeleton/<文件名>_skeleton.png"

mkdir -p "ref/pose/skeleton"
"$POSE_PYTHON" "$POSE_SCRIPT" "$INPUT" -o "$OUTPUT" --model "$POSE_MODEL" --det-model "$POSE_DETECTOR"
```

默认使用 `detect-resolution=512`、最多 2 个人体；若画面严重遮挡或人体被裁出画面，模型可能无法稳定定位。批量处理时可加 `--skip-failures`，失败项不写入空图：

```bash
find "ref/pose/color" -maxdepth 1 -type f \
  \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' \) \
  -print0 | xargs -0 "$POSE_PYTHON" "$POSE_SCRIPT" \
  --output-dir "ref/pose/skeleton" --model "$POSE_MODEL" --det-model "$POSE_DETECTOR" --skip-failures
```

生成后检查输入和输出的像素尺寸；骨骼图应为 `PNG、RGB`，背景为黑色，文件名必须与原图 stem 对应。对比参考图时重点检查头、肩、肘、腕、髋、膝、踝是否连贯；明显误检的图片保留为缺失状态，不要用手工猜测的线条冒充模型结果。

## 3. 按 `_depth` 后缀匹配原图

深度图的匹配规则是：去掉文件名末尾的 `_depth.png`，得到原图 stem，再在原图目录中查找相同 stem 的彩色图。

例如：

```text
10_depth.png → 10 → 10.jpg
无标题_depth.png → 无标题 → 无标题.jpg
```

不要只根据文件排序位置配对，也不要把不同 stem 的图片凭相似画面或相邻编号强行配对。可使用下面的检查逻辑，支持常见栅格扩展名，并对文件名统一加引号：

```bash
SOURCE_DEPTH_DIR="ref/pose/depth"
SOURCE_COLOR_DIR="ref/pose/color"

find "$SOURCE_DEPTH_DIR" -maxdepth 1 -type f -iname '*_depth.png' -print | sort -V |
while IFS= read -r source_depth_file; do
  image_stem="$(basename "${source_depth_file%_depth.png}")"
  source_color_file=""

  for image_ext in jpg jpeg png webp; do
    candidate_file="$SOURCE_COLOR_DIR/$image_stem.$image_ext"
    if test -f "$candidate_file"; then
      source_color_file="$candidate_file"
      break
    fi
  done

  if test -z "$source_color_file"; then
    printf 'MISSING color for %s\n' "$(basename "$source_depth_file")" >&2
    exit 1
  fi

  printf 'MATCH %s ↔ %s\n' \
    "$(basename "$source_color_file")" \
    "$(basename "$source_depth_file")"
done
```

## 4. 检查图片并提取姿势信息

每一对匹配文件至少检查一次彩色原图和深度图。彩色图用于识别动作与构图，深度图用于确认前后层次、身体轮廓和靠近镜头的部位。

```bash
sips -g pixelWidth -g pixelHeight \
  "ref/pose/color/<文件名>.jpg" \
  "ref/pose/depth/<文件名>_depth.png"

file "ref/pose/color/<文件名>.jpg"
file "ref/pose/depth/<文件名>_depth.png"
```

识别时只记录以下信息：

1. 画面是横图还是竖图，主体位于画面哪个区域；
2. 主体是站立、坐姿、仰躺、侧卧、半躺或其他身体姿态；
3. 躯干和头部朝向；
4. 双臂、双手、双腿、膝盖和脚的具体位置；
5. 哪个身体部位更靠近镜头，是否形成明显前后层次；
6. 镜头是正面、背面、侧面或斜侧方，以及高位、平视还是低位；
7. 景别、俯拍/平拍/仰拍和透视关系。

提示词应以 `The subject ...` 开始，描述动作的起始状态和镜头构图。姿势图中的角色外观、服装、背景和文字不应被写进姿势提示词；这些职责应由独立的角色、服装和背景参考控制。

## 5. 根据画面内容设计文件名

文件名应让人不打开图片也能快速判断姿势，推荐格式：

```text
<主要姿势>-<关键肢体位置>_<镜头视角>_<横图或竖图>.<原图扩展名>
<主要姿势>-<关键肢体位置>_<镜头视角>_<横图或竖图>_depth.png
```

命名规则：

- 使用动作、姿势、肢体位置、视角和画幅信息；
- 不使用角色名、发色、脸部特征、服装、场景或身份标签；
- 不把原始编号作为最终名称，除非图片内容确实无法进一步区分；
- 同一对图片必须共享完全相同的彩色图 basename，深度图只额外添加 `_depth`；
- 名称应避免 `/`、控制字符和会造成 shell/Markdown 歧义的未转义字符；
- 不改变原始图片的尺寸、编码或深度图灰度格式。

本批次的命名示例：

| 原始配对 | 彩色图新名称 | 深度图新名称 |
| --- | --- | --- |
| `1.jpg` + `1_depth.png` | `站立-一手抬至脸侧_正面_竖图.jpg` | `站立-一手抬至脸侧_正面_竖图_depth.png` |
| `6.jpg` + `6_depth.png` | `坐姿蛙式-双膝外展_正面_竖图.jpg` | `坐姿蛙式-双膝外展_正面_竖图_depth.png` |
| `17.jpg` + `17_depth.png` | `仰躺-双腿抬起外展_正面_横图.jpg` | `仰躺-双腿抬起外展_正面_横图_depth.png` |
| `无标题.jpg` + `无标题_depth.png` | `站立-一手覆胸_近景_竖图.jpg` | `站立-一手覆胸_近景_竖图_depth.png` |

除非任务明确要求，否则只重命名复制到 `ref/pose/` 的资产，保留原始目录中的文件名和目录结构，方便回溯源文件。

## 6. 复制或重命名到 `ref/pose`

更安全的做法是先建立“原始 stem → 最终 basename”的映射，然后直接以最终名称复制，避免先复制成数字名后忘记同步深度图或索引。复制前确保目标文件不存在：

```bash
TARGET_COLOR_DIR="ref/pose/color"
TARGET_DEPTH_DIR="ref/pose/depth"
mkdir -p "$TARGET_COLOR_DIR" "$TARGET_DEPTH_DIR"

cp "$SOURCE_COLOR_DIR/<原始文件名>.jpg" \
  "$TARGET_COLOR_DIR/<重命名后的文件名>.jpg"
cp "$SOURCE_DEPTH_DIR/<原始文件名>_depth.png" \
  "$TARGET_DEPTH_DIR/<重命名后的文件名>_depth.png"
```

如果文件已经以旧名称复制到目标目录，则只对目标中的成对文件执行重命名：

```bash
mv "$TARGET_COLOR_DIR/<旧文件名>.jpg" \
  "$TARGET_COLOR_DIR/<重命名后的文件名>.jpg"
mv "$TARGET_DEPTH_DIR/<旧文件名>_depth.png" \
  "$TARGET_DEPTH_DIR/<重命名后的文件名>_depth.png"
```

两次操作必须成对完成。不要只改彩色图名称，也不要把深度图改成没有 `_depth` 后缀的普通图片名。

## 7. 写入并引用 `pose.json`

姿势资产应写在 `ref/pose/pose.json` 的同一个 `actions` 对象中；每条记录至少包含稳定 ID、分类、标题、英文姿势描述、彩色原图、深度图和配对键，骨骼图作为可选姿态控制资源。当前 JSON 中的媒体路径都相对于 `ref/` 根目录：

```json
{
  "id": "pose-<stable-id>",
  "category": "坐姿",
  "tags": [],
  "title": "侧坐-一腿屈起一腿伸展_三分之四视角_竖图",
  "text": "The subject sits in a three-quarter side pose. ...",
  "image_path": "pose/color/<basename>.jpg",
  "color_image_path": "pose/color/<basename>.jpg",
  "depth_image_path": "pose/depth/<basename>_depth.png",
  "pair_key": "<basename>",
  "skeleton_image_path": "pose/skeleton/<basename>_skeleton.png"
}
```

`color_image_path`、`depth_image_path` 和 `skeleton_image_path` 是当前字段；`image_path` 仍作为兼容别名保留。标题、彩色图 basename、深度图 basename、`pair_key` 和实际文件必须完全一致。

注意事项：

- 动作库沿用相对于 `ref/` 的 `pose/color/...`、`pose/depth/...` 和 `pose/skeleton/...` 链接约定；
- 标题、彩色图 basename、深度图 basename 和实际文件必须完全一致；
- 提示词使用英文执行描述时，保持只描述姿势、身体位置和镜头关系；
- 不要在没有实际工作流输入的情况下擅自加入 `<Picture N>`、`<Subject N>` 或 `<Video N>`；
- 如果当前工作流接入姿势图，标签编号必须按照实际上传顺序维护，而不是按照 JSON 数组顺序猜测；
- 深度图是结构辅助，不应作为普通彩色参考图、身份参考图或风格参考图使用。

## 8. 与动作库保持一致

### 唯一事实源

网页端动作库直接读取 `ref/pose/pose.json` 的 `actions` 数组，不再解析旧的 Markdown 索引，也不生成 `prompt-actions.json` 缓存。每个动作对象同时保存：

- 一个 `pose/color/` 原图路径；
- 一个 `pose/depth/` 深度图路径；
- 一个 `pair_key` 配对键；
- 一个可选的 `pose/skeleton/` 骨骼图路径；
- 对应的姿势提示词。

如果资产尚未齐全，可以保留临时条目，但标题必须明确标注“待补”或“仅深度图”，不能把它当作完整动作发布。动作库会保留并显示这类条目的缺失状态，补齐文件和链接后再变成可用的完整动作。

RH Workflow Desk 会从配置的媒体库根目录读取 `pose.json`，并在打开动作库或请求动作列表时实时刷新。动作图片仍从 `VideoMake/ref/pose/` 原目录读取，不会复制到 RH_CLI；不要直接编辑 RH_CLI 的派生数据。

动作库为每条记录生成稳定 ID，并暴露原图、深度图和骨骼图查看入口。页面可以在三种资源之间切换、点击放大，并显示原图/深度图配对状态；骨骼图是可选附加资源。

| 状态 | 含义 | 处理方式 |
| --- | --- | --- |
| `paired` | 彩色图和深度图都存在，且 basename 与 `pair_key` 匹配 | 可正常使用 |
| `missing_color` | 深度图存在，但彩色原图不存在 | 补回原图或修正 JSON 路径 |
| `missing_depth` | 彩色原图存在，但深度图不存在 | 生成并登记对应 `_depth.png` |
| `mismatched` | 两张图片都存在，但 basename 或 `pair_key` 不一致 | 修正文件名或 JSON，不得强行配对 |
| `missing_both` | 两张图片都不存在 | 检查目录、路径和大小写 |

动作库中的“原图 + 深度图”只表示文件和链接校验通过，不代表深度值具有真实物理距离含义；深度图仍应遵守本文前面的尺寸和 `PNG、8-bit grayscale` 要求。

### 新增动作的标准顺序

以后扩展动作时，只修改素材目录和 `pose.json`，按以下顺序操作：

1. 确定一个不会与现有资产重复的最终 basename，例如 `侧坐-一腿屈起_三分之四视角_竖图`。
2. 将彩色原图放入 `ref/pose/color/`，将同一张图生成的深度图放入 `ref/pose/depth/`，可用的骨骼图放入 `ref/pose/skeleton/`；三者直接使用同一 basename，并分别追加 `_depth`、`_skeleton` 后缀。
3. 在 `ref/pose/pose.json` 的 `actions` 数组新增一个对象，填写稳定 ID、分类、标签、标题、英文描述、媒体路径和 `pair_key`。
4. 运行文件、尺寸、格式和链接核验；打开动作库后点击“重新扫描”，确认显示“原图 + 深度图”。

推荐的动作对象格式如下：

```json
{
  "id": "pose-<stable-id>",
  "category": "坐姿",
  "tags": ["侧坐"],
  "title": "侧坐-一腿屈起一腿伸展_三分之四视角_竖图",
  "text": "The subject sits in a three-quarter side pose. One knee is raised and bent toward the chest, the opposite leg extends diagonally across the lower frame, and the camera uses a close three-quarter view.",
  "image_path": "pose/color/侧坐-一腿屈起一腿伸展_三分之四视角_竖图.jpg",
  "color_image_path": "pose/color/侧坐-一腿屈起一腿伸展_三分之四视角_竖图.jpg",
  "depth_image_path": "pose/depth/侧坐-一腿屈起一腿伸展_三分之四视角_竖图_depth.png",
  "pair_key": "侧坐-一腿屈起一腿伸展_三分之四视角_竖图",
  "skeleton_image_path": "pose/skeleton/侧坐-一腿屈起一腿伸展_三分之四视角_竖图_skeleton.png"
}
```

不要只新增原图或只新增深度图，也不要把一对图片拆到两个动作对象。已有动作一旦被加入组状态，尽量不要修改其最终 basename；动作 ID 基于资源路径生成，重命名会被视为新动作，旧组状态可能无法找到原动作。

### 发布或提交前的最小配对检查

下面的检查直接读取当前 JSON，验证每个动作的彩色图、深度图、`pair_key` 和可选骨骼图路径：

```bash
python3 - <<'PY'
import json
from pathlib import Path

index_path = Path("ref/pose/pose.json")
document = json.loads(index_path.read_text(encoding="utf-8"))
entries = document.get("actions", [])
errors = []

for entry in entries:
    label = entry.get("title") or entry.get("id") or "<untitled>"
    color = str(entry.get("color_image_path") or entry.get("image_path") or "")
    depth = str(entry.get("depth_image_path") or "")
    skeleton = str(entry.get("skeleton_image_path") or "")
    if not color or not depth:
        errors.append(f"{label}: color_image_path/depth_image_path 不完整")
        continue
    color_key = Path(color).stem
    depth_key = Path(depth).stem.removesuffix("_depth")
    if color_key != depth_key or entry.get("pair_key") != color_key:
        errors.append(f"{label}: basename 或 pair_key 不匹配")
    for field, relative in (("color", color), ("depth", depth), ("skeleton", skeleton)):
        if relative and not (Path("ref") / relative).is_file():
            errors.append(f"{label}: {field} 文件不存在: {relative}")

if errors:
    print(*errors, sep="\n")
    raise SystemExit(1)
print(f"pose actions: {len(entries)}")
print("all color/depth pairs and declared skeleton paths are valid")
PY
```

## 9. 完成后的核验

### 文件和配对核验

对每一张源深度图确认目标彩色图和目标深度图都存在，并确认复制没有改变文件内容：

```bash
shasum -a 256 \
  "ref/pose/color/<文件名>.jpg" \
  "ref/pose/depth/<文件名>_depth.png" \
  "ref/pose/skeleton/<文件名>_skeleton.png"
```

彩色图、深度图和骨骼图的 basename 必须按 JSON 声明配对；彩色图和深度图应有相同的像素宽高，深度图应保持 `PNG、8-bit grayscale`，骨骼图应保持可读的 `PNG` 图像。

### 引用核验

不要再用 Markdown 标题或图片链接推断动作条目，直接检查 JSON 和文件路径：

```bash
python3 -m json.tool ref/pose/pose.json >/dev/null
rg -n '"(id|title|color_image_path|depth_image_path|skeleton_image_path|pair_key)"' ref/pose/pose.json
```

### 文档和工作区核验

- 检查新增文档和 `pose.json` 没有尾随空格、断裂代码围栏或错误相对路径；
- 检查旧数字文件名没有继续出现在 `pose.json` 的新增动作对象中；
- 检查原始目录仍然存在，且没有被覆盖、删除或移动；
- 最后查看 `git diff --stat` 和 `git status --short`，只确认本次流程产生的文档、索引和目标资产；
- 若需要提交，只暂存本次任务相关路径，不要把 `.env`、cookies、认证文件、临时目录或其他未相关改动一并加入。

## 交付标准

只有同时满足以下条件，才算完成一批姿势资产整理：

- 每个 `*_depth.png` 都找到 stem 完全匹配的原图；
- 每对原图和深度图都已放入 `ref/pose/color/` 与 `ref/pose/depth/`；
- 可用骨骼图已放入 `ref/pose/skeleton/`，并以 `_skeleton` 后缀配对；
- 彩色图、深度图和 `pair_key` 使用同一最终 basename；
- 文件名能表达动作、身体位置和镜头关系，且不夹带人物身份或背景特征；
- `pose.json` 的每个动作对象都同时登记彩色图、深度图和姿势提示词；
- 所有链接、格式、尺寸、哈希和工作区范围均已核验；
- 原始素材保持不变，可根据映射关系回溯。
