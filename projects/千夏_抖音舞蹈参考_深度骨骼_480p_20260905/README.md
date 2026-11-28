# 千夏·抖音舞蹈参考·深度+骨骼·480p

## 任务

- 基于原抖音视频生成同帧的深度 + DWPose 骨骼结构参考视频，再用该参考视频跑一版 MiniMax H3 Ref2VA。
- 原视频：`/Users/apple/Downloads/最怕这种了感觉至上 永恩 - 抖音.mp4`
- 角色参考：`ref/character/千夏/千夏-全身三视图-方形-v2.png`（原皮）、`ref/character/千夏/千夏_正脸头像_v4.png`（面部）。
- 深度骨骼参考：`reference/千夏_抖音_深度骨骼参考.mp4`；每帧为灰度深度图与彩色 DWPose 身体/面部/手部骨骼的同帧叠加，静音，仅作为结构控制参考。
- 目标生成：9:16 竖屏、0.4 MP（实际 480×864）、约 13.46 秒，使用 H3 原生新音频。

## 本地处理

- 原视频按 24fps 抽取 323 帧。
- Depth Anything V2 Small Core ML 生成 323 张 8-bit grayscale 深度图。
- DWPose 逐帧检测，323 帧均识别到 1 个人体。
- 深度与骨骼通过 `screen` 叠加合成同一条静音 MP4；原视频未被修改。

## RH 提交

- 生成模板：`workflows/10erosBeta4生视频.json`
- RH 本地登记工作流：`wf_81a715c3011b`
- RH 远程 workflowId：`2094755110367227906`（站点 `ai`，账号 `akai`）。
- 参考视频通过 `VHS_LoadVideo` 以 24fps 帧接入 H3 的 `ref_videos.ref_video_0`；原皮和面部分别接入 Picture 1/2。
- 本次 RH 任务：`task_519dc697157a`；远程 taskId：`2096245394319667201`；耗时约 387 秒；成本 78 coins。
- 使用 API Key：`ai-rh`（站点 `ai`）；输出已完成并通过解码与接触表核验。

## 文件

- [英文提示词](千夏_抖音舞蹈参考_深度骨骼_480p_prompt.txt)
- [中文翻译](千夏_抖音舞蹈参考_深度骨骼_480p_prompt_zh.txt)
- [API 工作流](千夏_抖音舞蹈参考_深度骨骼_480p_workflow_api.json)
- [深度+骨骼参考视频](reference/千夏_抖音_深度骨骼参考.mp4)
- 参考视频核验接触表：`reference/qa/contact_sheet.png`
- [第二版成品](output/task_519dc697157a/output_1.mp4)：480×864、24fps、13.67 秒、H.264/AAC 双声道。
- 成品统一入口：`/Users/apple/Documents/VideoMake/videoOutput/千夏_抖音舞蹈参考_深度骨骼_480p_20260905.mp4`。
- RH 任务级 `workflow_api.json`、`prompt_group.json`、`manifest.json` 和 QA 接触表位于 `output/task_519dc697157a/`。
