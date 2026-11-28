# 千夏·抖音舞蹈参考·480p

## 任务

- 使用 RH_CLI 本地 Web API 生成一段 MiniMax H3 Ref2VA 视频。
- 参考视频：`/Users/apple/Downloads/最怕这种了感觉至上 永恩 - 抖音.mp4`
- 角色参考：`ref/character/千夏/千夏-全身三视图-方形-v2.png`（原皮）、`ref/character/千夏/千夏_正脸头像_v4.png`（面部）。
- 目标：9:16 竖屏、约 13.46 秒、0.4 MP 480p、单连续镜头。
- 参考视频只用于动作、节奏、机位和室内构图；不复用源音频。

## 工作流与提交

- 生成基础模板：`workflows/10erosBeta4生视频.json`
- RH 本地登记工作流：`wf_81a715c3011b`
- RH 远程 workflowId：`2094755110367227906`（站点 `ai`，账号 `akai`）
- `VHS_LoadVideo` 输出的 24fps 图像帧接入 H3 conditioning 的 `ref_videos.ref_video_0`；两个未使用的旧图片节点旁路。
- 本次 RH 任务：`task_0d04f841af65`；远程 taskId：`2096139944255844353`；耗时约 416 秒；成本 84 coins。
- 使用 API Key：`ai-rh`（站点 `ai`）；输出已完成并通过解码校验。

## 文件

- [英文提示词](千夏_抖音舞蹈参考_480p_prompt.txt)
- [中文翻译](千夏_抖音舞蹈参考_480p_prompt_zh.txt)
- [API 工作流](千夏_抖音舞蹈参考_480p_workflow_api.json)
- 成品：`output/task_0d04f841af65/output_1.mp4`，480×864、24fps、13.67 秒、H.264/AAC 双声道。
- 统一入口：`/Users/apple/Documents/VideoMake/videoOutput/千夏_抖音舞蹈参考_480p_20260905.mp4`。
- RH 任务级 `workflow_api.json`、`prompt_group.json`、`manifest.json` 位于 `output/task_0d04f841af65/`。
