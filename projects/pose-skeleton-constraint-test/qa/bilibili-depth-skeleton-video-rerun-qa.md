# Bilibili 深度 + 骨骼参考视频输入重跑 QA

## 8.7 动作迁移输入

- 原始 Bilibili 视频：`analysis/bilibili_reference/source/bilibili_action_reference.mp4`
- 原始 probe：720×1280，151/6 fps，10.021 秒，仅作为动作分析源。
- 24fps 抽帧：`analysis/bilibili_depth_skeleton_8_7/source_24fps_frames/`，241 帧，720×1280。
- 深度图：`analysis/bilibili_depth_skeleton_8_7/depth/`，241 帧；样本为 PNG、720×1280、8-bit grayscale。
- DWPose：`analysis/bilibili_depth_skeleton_8_7/skeleton/`，241 帧；样本为 PNG、720×1280、8-bit/color RGB。
- VRAM 适配后的控制图：`depth_480p/` 与 `skeleton_480p/`，两者均为 241 帧、480×864，分别保持 grayscale L 与 RGB。
- H3 Video 输入：`analysis/bilibili_depth_skeleton_8_7/reference_480p/bilibili_depth_skeleton_reference_480p_24fps.mp4`
- 控制 Video probe：H.264、480×864、24fps、241 帧、10.041667 秒，无音轨。

每一帧的深度图与骨骼图使用相同帧号、相同画幅，最后以 screen blend 合成为单一静音 Video。workflow 的 `97` 节点为 `VHS_LoadVideo`，并连接到 `MiniMaxH3AudioConditioningT8` 的 `ref_videos.ref_video_0`；没有把五张静态姿态图作为 Picture 输入。

## 尺寸预处理效率记录

本次首次尝试是先用 720×1280 帧生成深度图、骨骼图和控制 Video，再缩放到 480×864；该顺序增加了逐帧文件读写、合成和上传体积，并在 H3 读取参考 Video 时触发了 VRAM OOM。后续重跑改为使用同一套逐帧数据的 480×864 控制 Video，成功完成。

下次应保留原始 Bilibili 视频不变，但先生成 480×864 / 24fps 工作副本，再抽帧、推理和同帧合成。当前 Depth Anything 包装器固定输入 518×392、DWPose 固定检测分辨率 512，所以模型前向时间不会严格按像素比例下降；主要收益是减少 PNG I/O、后处理、编码/上传体积和 H3 参考 Video 的显存占用。

## Workflow 与提示词

- Workflow：`chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source-retry480_workflow_api.json`
- Prompt：`chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source_prompt.txt`
- 中文翻译：`chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source_prompt_zh.txt`
- 角色图：`ref/character/千夏/千夏-全身三视图-方形-v2.png`
- 面部图：`ref/character/千夏/千夏_正脸头像_v4.png`
- 音频：`audio/SCARED_LONELY_FUNK_0-15s.wav`
- `task_type=Ref2VA`、`audio_mode=lock_source`、输出分辨率选择器为 9:16 / 0.4 MP；提示词使用 `<Picture 1>`、`<Picture 2>`、`<Video 1>`、`<Audio 1>` 稳定标签。

## 远程运行记录

- 初次 720×1280 控制 Video 任务：`task_59ce8796c545` / remote `2096259049000562690`；失败原因为 `SamplerCustomAdvanced` VRAM OOM，未生成产物。
- 路径修正任务：`task_7e669bc0cf8a`；因首次使用相对输出路径，已在远程 task `2096260328024207362` 返回后取消，不作为成片。
- 成功重跑：`task_fccfe6918a47` / remote `2096260614453227521`
- 状态：completed；远程执行 279 秒；记录成本 56 RH coins；保存 1 个 MP4。
- 输出目录：`output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/`

## 成片核验

- Raw H3：`output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/task_fccfe6918a47/output_1.mp4`
- Raw probe：H.264、480×864、24fps、361 帧、15.075 秒；AAC stereo，32kHz。
- 最终成片：`output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/chinatsu_showcase_480p_bilibili_depth_skeleton_final.mp4`
- 最终 probe：H.264、480×864、24fps、360 帧；视频流时长 15.000 秒；AAC 48kHz stereo。容器总时长因 AAC 编码 priming 显示约 15.021 秒，视频边界严格为 15 秒。
- 解码核验：视频流与音频流均通过 `ffmpeg -f null` 完整解码。
- 视觉核验：`output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/final_contact_sheet.png`；五个节拍均为千夏画面，浅色背景干净，未见骨骼线、关键点、深度伪影、源表演者、源场景或水印。
- `videoOutput`：`videoOutput/chinatsu-showcase-480p-bilibili-depth-skeleton.mp4`
- 本版本按用户要求不做 720p 上采样，也未新增 Bilibili 发布任务。
