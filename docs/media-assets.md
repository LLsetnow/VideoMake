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

## `opc` 下载示例

```bash
# 视频
opc bili "<Bilibili_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"
opc douyin "<Douyin_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"
opc x "<X_URL>" -o "/Users/apple/Documents/VideoMake/videoRef"

# 音频
opc bili "<Bilibili_URL>" --audio-only -o "/Users/apple/Documents/VideoMake/audio"
opc music "<Netease_URL>" -o "/Users/apple/Documents/VideoMake/audio" --bitrate 320
```

需要完整参数时先运行 `opc bili --help`、`opc douyin --help`、`opc x --help` 或 `opc music --help`。

## `opc audio` 分析

- `opc audio librosa <音频文件>`：检测鼓点/节拍，用于安排镜头切换、动作节奏和片段拆分。
- `opc audio <音频文件>`：分析曲风、内容和听感，用于脚本、剪辑和 H3 提示词。

```bash
opc audio librosa "/Users/apple/Documents/VideoMake/audio/<音频文件>.mp3" \
  -o "projects/<项目名>/beat_analysis.txt"
opc audio "/Users/apple/Documents/VideoMake/audio/<音频文件>.mp3" \
  -o "projects/<项目名>/music_analysis.txt"
```

`librosa` 模式可用 `--beat-strength-threshold` 调整鼓点强度阈值、`--beat-min-interval` 调整最小间隔；需要完整参数时使用 `opc audio --help`。
