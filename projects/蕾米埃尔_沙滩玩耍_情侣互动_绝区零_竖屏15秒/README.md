# 蕾米埃尔 × 哲｜绝区零海滩情侣互动（480p v2）

## 目标

制作一段 15 秒、竖屏 9:16、480p 的《绝区零》风格多镜头视频。相较上一版，本版将节奏加密为 6 个约 2–3 秒的镜头，依次包含排球准备、击球瞬间、浅水嬉戏、蕾米埃尔面部特写、共享冰沙和情侣收束画面。哲按要求部分出场，并通过扶手腕、拂脸颊、递冰沙、靠肩与短暂碰手表达含蓄亲密关系。

## 生成约束

- H3 模式：`Ref2VA` 全参考生成。
- 参考风格：`Zenless Zone Zero Cartoon rendering style`。
- 画幅：9:16 竖屏；初采目标 480p；24fps；15 秒。
- 角色：蕾米埃尔原皮 + 面部；哲学院皮 + 面部。
- 音频：无角色参考音色，因此不生成对白或可辨识人物声音；保留原生同步海浪和动作音效。
- 生成 480p 后必须由用户 review；未收到明确确认前不得上采样。

## 资产映射

| Picture | 角色/用途 | 实际文件 |
| --- | --- | --- |
| Picture 1 | 蕾米埃尔原皮全身 | `ref/character/蕾米埃尔/蕾米埃尔_角色三视图.png` |
| Picture 2 | 蕾米埃尔面部 | `ref/character/蕾米埃尔/exec-e724fa5d-a2fb-4858-b259-213277a73a94.png` |
| Picture 3 | 哲服装/身体 | `ref/character/哲/哲_角色三视图_1x1.png` |
| Picture 4 | 哲面部 | `ref/character/哲/哲_大头照.png` |

## 文件

- 英文执行提示词：`蕾米埃尔_沙滩玩耍_情侣互动_480p_prompt.txt`
- 中文对应翻译：`蕾米埃尔_沙滩玩耍_情侣互动_480p_prompt_zh.txt`
- RH API 工作流：`蕾米埃尔_沙滩玩耍_情侣互动_480p_workflow_api.json`
- 镜头计划与 review 规则：`qa/multishot_plan.md`
- 480p QA：`qa/480p_qa.md`
- 480p 输出：`output/480p/`
- 上采样输出：`output/upscale/task_256b6f98fa34/output_1.mp4`
- 最终成品入口：`videoOutput/蕾米埃尔_沙滩玩耍_情侣互动_15秒_1MP_最终.mp4`

## RH 记录

- 提交入口：RH_CLI 本地 Web App API `POST http://127.0.0.1:8766/api/tasks`
- 本地 workflow ID：`wf_8618a750a8e1`
- Prompt Group ID：`group-e5c56e175095`
- 本地 task ID：`task_1ee9c284cc0f`
- 远程 task ID：`2095990843246907393`

### 上采样

- 本地 workflow ID：`wf_5c8441c1373a`
- 本地 task ID：`task_256b6f98fa34`
- 远程 task ID：`2095992945799884802`
- 目标：1.0 MP 竖屏；实际 768×1376

## 当前阶段

已完成 480p review、用户确认和独立上采样。上采样输出已完成规格与画面 QA，最终成品入口已建立；早先的 `task_9b50baec72c6` 保留在同一 480p 输出目录作为备份。
