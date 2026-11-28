# 千夏南宫羽｜自律查手机｜竖屏 15 秒

## 目标

三镜头竖屏对白喜剧：千夏宣布自律，南宫羽要求她放下手机，千夏立刻搜索“怎么放下手机”。千夏设定为胆小怕生、轻声谨慎；说话时保持闭口或微张嘴的小幅口型，不使用夸张张口。先用 480p 生成验证人物、口型、对白和节奏；验收通过后使用独立上采样工作流提升到 720p。

## 输入映射

| H3 标签 | 工作流节点 | 资源 | 用途 |
| --- | --- | --- | --- |
| `<Picture 1>` | `13:image` | `ref/character/千夏/千夏-全身三视图-方形-v2.png` | 千夏身份与核心服装 |
| `<Picture 2>` | `76:image` | `ref/character/千夏/千夏_正脸头像_v4.png` | 千夏脸部、发型与发饰 |
| `<Picture 3>` | `75:image` | `ref/character/南宫羽/南宫羽_角色三视图.png` | 南宫羽身份与核心服装 |
| `<Audio 1>` | `52:audio` | `ref/character/千夏/千夏音色6秒.mp3` | 千夏参考音色 |
| `<Audio 2>` | `53:audio` | `ref/character/南宫羽/南宫羽音色6秒.mp3` | 南宫羽参考音色 |

本次工作流接入三张人物图和两条参考音色；音色仅用于引导对应角色的音色与表达，不复制原录音台词或信号。对白仍由 H3 原生生成。

## 工作流

- 480p 初采：`千夏南宫羽_自律查手机_480p_workflow_api.json`
- 后续上采样：`千夏南宫羽_自律查手机_上采样_workflow_api.json`
- 初采画幅：9:16，`ResolutionSelector.megapixels=0.4`，24 FPS，时长参数 15 秒，帧数由模板表达式按 `17n+5` 对齐。
- 上采样沿用模板的 `device=cuda`、`precision=fp16` 和视频/音频 latent 合并路径。

## RH 提交流程

按 VideoMake 规则通过 RH_CLI 本地 Web App 的 `POST http://127.0.0.1:8766/api/tasks` 提交，不直接调用 RunningHub API。任务 ID、调度站点、输出路径和最终 QA 结果写入 `qa/`。480p 初采完成后必须先交用户 review，收到明确确认前不提交上采样。

## 当前 review 版本

- 最新 480p 初采：`output/480p_v3/task_910c74ebec44/output_1.mp4`
- RH 本地 task ID：`task_910c74ebec44`；远程 task ID：`2095967807831863297`；状态：`completed`
- QA：480×864、24 FPS、约 15.08 秒、双声道；场景切点约为 4.833 秒和 8.917 秒。
- 接触表：`qa/480p_v3_contact_sheet.jpg`；对白核验：`qa/asr_480p_v3/480p_v3_audio.srt`
- 当前闸门：等待用户 review；此前误提交的上采样任务 `task_057bda4fa8ce` 已取消，未采用其结果。
