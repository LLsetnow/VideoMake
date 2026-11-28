# 千夏竖屏可爱展示｜15 秒｜480p｜面部参考增强｜锁定源音乐

## 方案状态

- 任务：在 `pose-skeleton-constraint-test` 已验证角色基础上制作新的角色展示片。
- 形态：9:16 竖屏，15.000 秒，24 FPS，`17n+5` 合法帧数为 362 帧，480p 目标为约 0.4 MP（本地输出为 480×864）。
- 镜头：5 镜头，按源音乐事件切换。
- 视觉参考：`output/task_2e220fc727fe/output_1.mp4` 只用于确认千夏的既有外观、服装和浅色背景表现；新 workflow 不把这段特殊坐姿视频作为视频输入。
- 新增面部参考：`ref/character/千夏/千夏_正脸头像_v4.png`，只用于加强脸部、眼睛、刘海、耳饰、蝴蝶结轮廓和发型一致性，不复制近景裁切或白色背景。
- B 站分镜参考：[`BV1xHPzzjEZk`](https://www.bilibili.com/video/BV1xHPzzjEZk/)，只借鉴可爱展示的节奏、动作递进和近景/全身切换，不复制表演者、画面、水印或网页 UI。
- 音乐：网易云音乐专辑 [`373093511`](https://music.163.com/#/album?id=373093511) 中的《SCARED LONELY FUNK》；实际输入为 `audio/SCARED_LONELY_FUNK_0-15s.wav`，`audio_mode=lock_source`。

## 镜头时间线

| 镜头 | 时间 | 画面职责 | 动作 / 姿态参考 | 运镜 | 切点依据 |
|---|---:|---|---|---|---|
| 1 | 00:00.000–00:03.797 | 全身建立千夏与干净白色棚景 | `站立-一手抬至脸侧_正面_竖图_skeleton`；抬手、双指挥手、眨眼 | 固定机位，极慢小幅推进 | 3.797s 强拍 |
| 2 | 00:03.797–00:06.613 | 正面近景，展示胸口手势与表情 | `站立-一手覆胸_近景_竖图_skeleton`；前倾、点胸、张手 | 小幅慢速弧线 | 6.613s 强拍 |
| 3 | 00:06.613–00:09.824 | 三分之四中大全身，展示侧倾与手指爱心 | `站立-身体侧倾_正面_竖图_skeleton`；侧倾、髋部转移、手指爱心 | 小幅向右平移 | 9.824s 起音 |
| 4 | 00:09.824–00:12.064 | 中近景，展示抬手挥动与眨眼 | `站立-单臂抬起_近景_竖图_skeleton`；单腿承重、抬手、挥手 | 小幅慢速推进 | 12.064s 起音 |
| 5 | 00:12.064–00:15.000 | 中大全身收束，坐姿与最终定格 | `坐姿-单膝抬起手靠近脸部_正面_竖图_skeleton`；猫爪、耸肩、眨眼 | 极小幅慢速拉远 | 15.000s 准确结束 |

## 连续性与负面约束

- 角色身份、脸、银灰卷发、青绿色蝴蝶结、白红黑粉薄荷色服装、翅膀、背包与配饰全程一致。
- 背景始终是纯白或极浅薄荷色的干净无缝棚景；允许很淡的落地阴影，不引入场景物件。
- 骨骼图只约束姿态，禁止出现黑底、彩色线条、关键点或任何姿态叠加。
- 不出现额外人物、道具、对白字幕、Logo、水印、网页 UI、裸露或挑逗性展示。
- 源音乐全程 1:1 复制，不生成新音乐、对白、环境声或音效。

## 生产文件

- 英文提示词：`chinatsu-showcase-15s-480p-face-ref-lock-source_prompt.txt`
- 中文翻译：`chinatsu-showcase-15s-480p-face-ref-lock-source_prompt_zh.txt`
- API 工作流：`chinatsu-showcase-15s-480p-face-ref-lock-source_workflow_api.json`
- 720p 上采样工作流：`chinatsu-showcase-720p-upscale_workflow_api.json`
- 锁定源音频：`audio/SCARED_LONELY_FUNK_0-15s.wav`
- 节拍分析：`analysis/SCARED_LONELY_FUNK_beats.txt`
- 音乐理解：`analysis/SCARED_LONELY_FUNK_understanding.txt`
