# 媒体资产、下载与音频分析

## 资产目录

- `audio/`：通用音乐、驱动音频、参考音频；锁定源音频项目的源轨必须保持不变。
- `background/`：可复用背景图案和场景背景。
- `character/<角色名>/`：角色身份图、三视图、面部/全身/服装/姿态/场景参考图及角色音色。
- `videoRef/`：仅用于研究风格、动作、镜头或效果的参考视频。

如果视频有人物口播或台词，优先接入对应角色目录的音色参考。例如千夏使用 `character/千夏/千夏音色6秒.mp3`；不要把其他角色音色误接入当前角色。

所有角色、背景和分镜参考图均使用 `image-gen` 生成，必须是 ComfyUI/Aigate 可读取的栅格图像（PNG、JPG 或 WEBP）。不要将多个角色合并为一张参考图；多个角色使用独立图片和独立 `Load Image` 节点。

使用已有资产前确认真实存在、格式可读、方向比例正确，并在工作流中明确其角色。若图片已有描述字段、元数据或随图保存的说明，优先复用；只有缺失、不完整或与图像明显不一致时才补充识图。

参考视频默认只用于风格、动作、镜头或效果分析，不要自动作为最终素材或上传到工作流；只有任务明确要求时才接入视频参考节点。

下载媒体后先检查完整性和格式，再归档到 `videoRef/` 或 `audio/`，不要把下载目录当生成结果目录。cookies 可通过命令参数临时提供，但不得复制到项目、提交版本库或写入说明文件。

## `image-gen` 生成图像（codex + gpt-image）

角色、背景和分镜参考图统一使用本机 `codex exec` 生成：codex 内置 `image_gen__imagegen` 工具（由 gpt-image 驱动，需 ChatGPT 账号登录，本机已验证 codex-cli 0.147+ 可用）。

关键命令格式（注意：codex exec 的位置参数 prompt 在某些版本会失效并报 `No prompt provided via stdin`，必须用 `-` 让提示词走 stdin）：

```bash
# 带参考图（-i 可重复传多张，保持角色/风格一致）
printf '%s' "<生成提示词>" | codex exec -i "/绝对路径/参考图.png" - 2>&1 | tail

# 纯文字生图
printf '%s' "<生成提示词>" | codex exec - 2>&1 | tail
```

提示词要点：

- 明确风格、配色、构图、画幅比例和用途（角色身份图/背景/分镜参考）；
- 在提示词里要求 codex 把图片保存到目标路径（如 `projects/<项目名>/analysis/<名称>.png`）并报告实际路径；
- 需要角色一致性时用 `-i` 附加角色参考图，并说明"延续参考图的角色与风格"。

输出与归档：

- 输出通常为 1536×1024 PNG；生成后用视觉模型核验风格与内容符合要求再归档，读图使用 `opc image understand <图片> [-p 提问] [-o 输出文件]`（旧命令 `opc read-img` 已移除）：

```bash
opc image understand "projects/<项目名>/analysis/<名称>.png" \
  -p "确认风格与参考角色一致性，并简短描述画面" \
  -o "projects/<项目名>/analysis/<名称>_check.txt"
```
- 可复用角色身份图 → `character/<角色名>/`；可复用背景 → `background/`；仅本次任务使用 → 项目 `analysis/` 或任务目录；
- 备用生图通道统一为 `opc image generate`：默认引擎 `qwen`（阿里云 Qwen Image，用 `ALIYUN_API_KEY`）；`--engine gpt-image` 走 OpenAI GPT-Image（原 `opc gpt-img` 已合并入该命令，需 `GPT_IMAGE_API_KEY`）。

## `opc media download` 下载示例

`opc media download` 根据 URL 自动识别平台（bilibili.com / b23.tv / douyin.com / x.com / twitter.com / music.163.com），统一入口下载视频或音频。

```bash
# 视频
opc media download "<Bilibili_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"
opc media download "<Douyin_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"
opc media download "<X_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"

# 音频
opc media download "<Bilibili_URL>" --audio-only -o "/Users/apple/Documents/VideoMake/audio"
opc media download "<Netease_URL>" -o "/Users/apple/Documents/VideoMake/audio" --bitrate 320

# B站/抖音/X 视频内容总结（下载 → ASR → 总结）
opc media download "<视频_URL>" --summarize -o "projects/<项目名>/analysis"
```

需要完整参数时先运行 `opc media download --help`。

## `opc music generate` 生成音乐

可以使用 `opc music generate` 调用 MiniMax Music 生成歌曲或纯音乐。使用 `--provider minimax` 指定 MiniMax，并将生成结果保存到 `audio/` 或当前项目的音频目录；API Key 保存在 OPC 的本地配置中，不要写入 VideoMake。

```bash
# MiniMax 生成纯音乐
opc music generate --provider minimax \
  "电影感钢琴与弦乐，逐渐推进，温暖收束" \
  --model music-3.0-free \
  --instrumental \
  -o "/Users/apple/Documents/VideoMake/audio/minimax-instrumental.mp3"
```

## `opc music` 音频分析

- `opc music beats <音频文件>`：检测鼓点/节拍，用于安排镜头切换、动作节奏和片段拆分。
- `opc music understand <音频文件>`：分析曲风、内容和听感，用于脚本、剪辑和 H3 提示词。

```bash
opc music beats "/Users/apple/Documents/VideoMake/audio/<音频文件>.mp3" \
  -o "projects/<项目名>/beat_analysis.txt"
opc music understand "/Users/apple/Documents/VideoMake/audio/<音频文件>.mp3" \
  -o "projects/<项目名>/music_analysis.txt"
```

`beats` 模式可用 `--beat-strength-threshold` 调整鼓点强度阈值、`--beat-min-interval` 调整最小间隔；需要完整参数时使用 `opc music beats --help`。

## `opc video understand` 视频理解

`opc video understand` 使用 Qwen3-VL 对视频进行内容和时间线分析，适合在生成或剪辑前理解已有视频的镜头语言。它可以辅助识别：

- 主体、场景、构图和画面风格；
- 景别以及推、拉、摇、移、跟拍、环绕等镜头运动；
- 主体动作、镜头节奏和关键时间段；
- 可用于 MiniMax H3 提示词的画面与运镜描述。

本地视频会由 OPC 编码后发送给 Qwen3-VL；也可以传入模型服务能够直接访问的 HTTP(S) 视频 URL。X、Bilibili 等帖子页面 URL 不是直接视频地址，应先用 `opc media download` 下载，再进行分析。API Key 和模型配置保存在 OPC 项目的本地 `.env` 中，不写入 VideoMake。

```bash
# 直接分析本地视频
opc video understand "/Users/apple/Documents/VideoMake/videoRef/<参考视频>.mp4"

# 重点分析运镜，并将结果保存到当前项目的 analysis 目录
opc video understand "/Users/apple/Documents/VideoMake/videoRef/<参考视频>.mp4" \
  -p "按时间段分析景别、镜头运动类型、运动方向、速度和主体动作" \
  -o "projects/<项目名>/analysis/video_understanding.txt"

# 查看可用参数
opc video understand --help
```

视频分析结果属于项目分析资料，建议保存到 `projects/<项目名>/analysis/`，作为 P1 级复现依据。`opc video understand` 只负责理解和描述，不会自动修改 H3 workflow，也不会自动将视频作为 `<Video N>` 参考输入；如果视频仅用于提示词参考，应保持“分析使用”和“工作流输入”两条路径分离。
