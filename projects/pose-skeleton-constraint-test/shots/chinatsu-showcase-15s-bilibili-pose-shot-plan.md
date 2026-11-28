# 千夏竖屏可爱展示｜15 秒｜Bilibili 动作帧约束独立版｜面部参考｜锁定源音乐

## 方案状态

- 版本：独立重跑，不覆盖先前的面部参考版或 720p 上采样版。
- 形态：9:16 竖屏，15.000 秒，24 FPS；480p 初采为 480×864，完成 QA 后上采样到 720×1280。
- 镜头：5 镜头，沿用已确认的音乐切点：3.797、6.613、9.824、12.064 秒。
- 角色参考：`ref/character/千夏/千夏-全身三视图-方形-v2.png`；面部参考为 `ref/character/千夏/千夏_正脸头像_v4.png`。
- 动作来源：Bilibili 视频 `BV1xHPzzjEZk` 的视频流抽帧，实际抽帧源约 10.021 秒、720×1280、约 25fps；仅提取姿态结构，不把源视频直接作为 H3 视频参考。
- 动作骨骼：DWPose 从下列五个抽帧生成，仅作为隐藏姿态参考；不复用 `ref/pose/skeleton/` 中的旧姿态图。
- 音乐：网易云音乐专辑 `373093511` 中的《SCARED LONELY FUNK》前 15 秒，输入为 `audio/SCARED_LONELY_FUNK_0-15s.wav`，`audio_mode=lock_source`。

## Bilibili 动作帧证据

| 图号 | 源帧时间 | 抽帧 | 姿态骨骼 | 只保留的动作信息 |
|---|---:|---|---|---|
| Picture 2 | 00:02.750 | `analysis/bilibili_reference/frames/selected/shot1_t2.75.png` | `analysis/bilibili_reference/skeleton/shot1_t2.75_skeleton.png` | 歪头、单手抬到头侧、另一手弯曲、紧凑上半身轮廓 |
| Picture 3 | 00:04.250 | `analysis/bilibili_reference/frames/selected/shot2_t4.25.png` | `analysis/bilibili_reference/skeleton/shot2_t4.25_skeleton.png` | 双膝跪坐、躯干直立、双肘弯曲、双手抬到肩侧 |
| Picture 4 | 00:05.500 | `analysis/bilibili_reference/frames/selected/shot3_t5.50.png` | `analysis/bilibili_reference/skeleton/shot3_t5.50_skeleton.png` | 单腿承重、另一脚内收、单臂向外弯曲、非对称肩线 |
| Picture 5 | 00:07.750 | `analysis/bilibili_reference/frames/selected/shot4_t7.75.png` | `analysis/bilibili_reference/skeleton/shot4_t7.75_skeleton.png` | 歪头、单手抬到脸侧、另一手低位弯曲 |
| Picture 6 | 00:09.250 | `analysis/bilibili_reference/frames/selected/shot5_t9.25.png` | `analysis/bilibili_reference/skeleton/shot5_t9.25_skeleton.png` | 单膝抬起、另一腿低位弯曲、躯干轻微转向、上半身收拢 |

源帧只保存在 `analysis/bilibili_reference/` 作为动作分析证据；H3 workflow 只加载由这些帧生成的骨骼 PNG，不加载源视频或源帧。

## 镜头时间线

| 镜头 | 时间 | 画面职责 | Bilibili 帧约束 | 动作与运镜 |
|---|---:|---|---|---|
| 1 | 00:00.000–00:03.797 | 正面中大全身建立角色 | Picture 2 | 歪头、手到脸侧、双指挥手、眨眼；固定机位极慢推进 |
| 2 | 00:03.797–00:06.613 | 正面中景的跪坐猫爪动作 | Picture 3 | 双膝着地、双手抬起、交替猫爪、张手；小幅弧线运镜 |
| 3 | 00:06.613–00:09.824 | 三分之四站立展示 | Picture 4 | 单腿承重、脚尖内收、胸口手指爱心、轻微耸肩；小幅向右平移 |
| 4 | 00:09.824–00:12.064 | 近景抬手与眨眼 | Picture 5 | 歪头、手到脸侧、小幅挥手、重音眨眼；小幅推进 |
| 5 | 00:12.064–00:15.000 | 坐姿收束与定格 | Picture 6 | 单膝抬起、猫爪两次、13.205 秒耸肩、14.667 秒眨眼；极小幅拉远 |

## 连续性与负面约束

- `Picture 1` 负责千夏身份、服装、翅膀、背包、配饰和身体比例；`Picture 7` 负责脸、眼睛、刘海、耳饰、蝴蝶结轮廓和发型。
- Picture 2–6 只负责姿态几何；禁止出现黑底、彩色骨骼线、面部关键点、关键点、姿态叠加或任何源帧画面。
- 背景始终为纯白或极浅薄荷色无缝棚景，只允许很淡的落地阴影；不引入源视频中的钢琴、玩偶、花朵、房间或其他道具。
- 不出现额外人物、对白字幕、Logo、水印、网页 UI、裸露或挑逗性展示。
- 源音乐全程 1:1 复制，不生成新音乐、对白、环境声或音效。

## 生产文件

- 英文提示词：`chinatsu-showcase-15s-bilibili-pose-lock-source_prompt.txt`
- 中文翻译：`chinatsu-showcase-15s-bilibili-pose-lock-source_prompt_zh.txt`
- API 工作流：`chinatsu-showcase-15s-bilibili-pose-lock-source_workflow_api.json`
- 720p 上采样工作流：`chinatsu-showcase-720p-bilibili-pose-upscale_workflow_api.json`
- 动作帧与骨骼图：`analysis/bilibili_reference/`
