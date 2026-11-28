# 蕾米埃尔｜沙滩玩耍｜绝区零｜竖屏 15 秒

## 目标

使用蕾米埃尔原皮与独立面部参考图，制作一条 15 秒、9:16 竖屏的《绝区零》场景沙滩玩耍片段。三镜头结构包含全身玩球、面部特写和全身收束动作；本片不安排可辨识对白，避免在人物库缺少蕾米埃尔音色时伪造参考音色。

## 输入映射

| H3 标签 | 工作流节点 | 资源 | 用途 |
| --- | --- | --- | --- |
| `<Picture 1>` | `13:image` | `ref/character/蕾米埃尔/蕾米埃尔_角色三视图.png` | 原皮身份、全身比例、服装、翅膀与配色 |
| `<Picture 2>` | `75:image` | `ref/character/蕾米埃尔/exec-e724fa5d-a2fb-4858-b259-213277a73a94.png` | 面部、发型包脸方式、眼睛高光与发饰 |

人物库 `ref/character/蕾米埃尔/` 当前没有音色文件；因此工作流没有接入 `<Audio N>`，提示词不生成对白，只生成海浪和动作原生同步音频。

## 方案与工作流

- 生成模式：`Ref2VA`，原生同步音频。
- 画幅/初采：9:16，`ResolutionSelector.megapixels=0.4`，24 FPS，15 秒参数，362 帧按 `17n+5` 对齐。
- 视觉：必须包含 `Zenless Zone Zero Cartoon rendering style`；原皮保持不变，不改成泳装或便装。
- 提示词：[`蕾米埃尔_沙滩玩耍_480p_prompt.txt`](蕾米埃尔_沙滩玩耍_480p_prompt.txt)
- 中文翻译：[`蕾米埃尔_沙滩玩耍_480p_prompt_zh.txt`](蕾米埃尔_沙滩玩耍_480p_prompt_zh.txt)
- API 工作流：[`蕾米埃尔_沙滩玩耍_480p_workflow_api.json`](蕾米埃尔_沙滩玩耍_480p_workflow_api.json)
- RH 本地工作流：`wf_fad2de161dd0`；远程 workflow：`2094755110367227906`；Prompt Group：`group-da9b415a8701`

## 480p 初采与 Review 闸门

- RH 本地 task：`task_9aeede17ad2a`
- 远程 task：`2095983735343181826`
- 状态：`completed`
- 480p 成片：[`output_1.mp4`](output/480p/task_9aeede17ad2a/output_1.mp4)
- 接触表：[`480p_contact_sheet.jpg`](qa/480p_contact_sheet.jpg)
- 实测：480×864，24 FPS，15.083333 秒，362 帧，AAC 32000 Hz 双声道。
- 场景检测到的实际切点：约 5.916667 秒、10.083333 秒；提示词中的时间轴仅作 H3 创作意图，QA 以实际画面为准。

当前仅交付 480p review 版本。未提交、未创建、未采用任何上采样任务或上采样成品；只有用户明确确认后，才可另行提交独立上采样任务。
