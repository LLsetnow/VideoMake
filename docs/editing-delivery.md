# 剪辑、核验、交付与复现

## 剪辑核验

生成完成后，从当前项目或子项目的 `output/` 按时间序列收集镜头，完成裁切、排序、转场、音频对齐、字幕/音效和最终导出。至少检查：

- 每段实际时长是否符合脚本；
- 帧率、画幅和方向是否统一；
- 角色声音、背景音乐和环境音是否错位或重复；
- 衔接处是否有突兀首尾帧、音频断裂或音量跳变；
- 最终文件是否含正确音轨并能正常播放。

生成段落边界和提示词 `[Shot]` 时间戳不是自动最终切点。源音频锁定项目应以源音频主时间线为准，使用场景检测、接触表和帧级硬切确认候选边界；拼接按 24fps 计算共享整数帧边界，目标帧数必须与实际时长一致，并重新挂载完整目标源音频。

卡点（beat-locked）视频的剪辑（含段内分镜切点处理）必须读取并遵循 `.codex/skills/beat-locked-redundant-video-edit/SKILL.md`：以锁定源音频为唯一主时钟，生成的视频只作素材池；切点选择强拍/强起音且间距约 2–3 秒；检测到的场景切点只作排除信息，在其周围保留 guard band（约 6 帧）再切；用 `trim=start_frame/end_frame` 帧级裁剪、统一规格后拼接，最后 remux 原始源音频；交付前逐段校验帧数并用 `ffprobe` 核对 FPS、时长、尺寸与音轨。规范实现可参考 `projects/情感失色症_60秒/analysis/` 的 `detect_generated_assets.py` 与 `build_beat_locked_edit.py`。

先验证视频帧数、音频起止、段落边界和输出可读性，再停止或释放 AIGate 实例。必要时使用 `ffprobe`、接触表和帧计数进行验证。

## 最终输出

最终成品保留在当前项目的 `output/`，并在 `/Users/apple/Documents/VideoMake/videoOutput/` 创建指向该文件的软链接：

```bash
mkdir -p /Users/apple/Documents/VideoMake/videoOutput
ln -s "/绝对路径/项目目录/output/最终成品.mp4" \
  "/Users/apple/Documents/VideoMake/videoOutput/最终成品.mp4"
readlink /Users/apple/Documents/VideoMake/videoOutput/最终成品.mp4
```

创建前确认目标没有同名文件或软链接；创建后确认链接指向真实成品。不要把最终视频实体复制到 `videoOutput/` 代替项目内的源文件。

## 复现记录

每次生成至少保留：故事/镜头编号和用途；角色、背景、参考图、参考视频和音频；workflow_api 路径；H3 模式、提示词路径和主要节点配置；AIGate 实例、GPU、seed、分辨率、时长和帧数；结果路径及是否剪辑/裁切/替换音频；项目 `output/` 真实成品路径和 `videoOutput/` 软链接路径。

修改时优先复制并版本化工作流和提示词，不覆盖已验证版本。生成失败时先区分输入路径、节点/模型缺失、JSON/API 参数、显存/时长约束以及提示词与参考内容不一致，再针对原因修改。
