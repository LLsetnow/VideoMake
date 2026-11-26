# 子 Agent 批量短图生视频提示词规范

## 文档目的

本文件说明如何把一组成年虚构角色参考图交给子 Agent，批量制作独立的图生视频任务。适用于用户已经把分镜、机位和动作编排权下放给 Agent 的情况。

默认交付规格统一为：

- 每张参考图对应一个独立视频。
- 竖屏 `9:16`。
- `720p` 级画幅，默认 `0.9 MP`。
- 时长 `15` 秒。
- `24 FPS`。
- 使用当前已经验证的 H3 或 10Eros 视频工作流。
- 不把多张参考图拼成一个视频，不跨图串镜。

批量任务的镜头安排、体位变化、机位、人物表演和结束状态由子 Agent 根据每张图确定。客户或用户无需再次逐镜确认，但子 Agent 必须把每张图的判断、提示词、工作流、任务 ID、输出文件和 QA 结果分别记录下来。

## 子 Agent 总控提示词

下面这段可以直接作为父 Agent 交给子 Agent 的任务说明。

```text
你负责批量制作一组成年虚构角色的 AIGC 视频。

核心规则：
1. 每张参考图单独制作一个视频，禁止把多张图拼成一个视频，禁止跨图串镜。
2. 每个视频统一为竖屏 15 秒、9:16、720p、24 FPS。
3. 图中所有人物均明确为成年虚构角色，双方动作始终是自愿、同意的。
4. 每段默认采用 4 镜，切镜时间为 00:03.400、00:07.100、00:10.900。
5. 男方只出现赤裸躯干、手臂、手、髋部或腿部，头部和脸部始终在画外。
6. 男方不得说话、喘息、呻吟、叹气、笑或发出任何其他声音。
7. 女生是唯一的人声来源。只保留她自然、断续、越来越急促的喘息和轻声呻吟。
8. 不使用男性声音、对白、旁白、音乐或画外说话声。允许床铺、皮肤接触、衣料和室内环境声。
9. 女生表情不能冻结。每一镜都要有明确表情变化，包括眼神、眉毛、嘴唇、呼吸、脸颊潮红和身体紧绷。
10. 动作必须表现为真实、连续的性交节奏。髋部、腿部、手、床铺和头发都要随动作产生可见反馈，禁止人物整体上下平移却没有交合动作。
11. 每个镜头的体位变化必须解剖合理、身体连续。根据参考图的原始姿势选择最自然的入口，不能为了换姿势强行扭曲人体。
12. 不主动询问用户分镜。分镜、机位、姿势转换和结束状态由你决定。制作前先读取参考图，为每张图写一行 opening_state，再选择对应动作。

每个单图任务必须保存：
- source.png
- prompt_en.txt
- prompt_zh.txt
- 该图独立的 workflow_api.json
- shots.json
- 最终 MP4
- ffprobe 与人工检查记录

工作流设置：
- 参考图节点使用当前模板对应的 LoadImage 节点。
- 提示词节点使用当前模板对应的 multiline text 节点。
- 分辨率设为 9:16、0.9 MP。
- 时长设为 15 秒。
- 模型、LoRA、采样和精化参数沿用当前已经跑通的 V7 配置，不随机更换。
- 每张图对应一个独立的 RunningHub 任务。
- 提交记录必须明确 execution_target: runninghub。

交付前检查：
- 实际时长 15 秒，画幅为 9:16，分辨率达到当前工作流的 720p 目标。
- 4 个镜头均存在，实际切点接近设定时间。
- 女生身份、发型、服装或赤裸状态、场景和道具连续。
- 男方脸部没有进入画面。
- 音轨中没有男性人声。
- 抽查抽送、接触、表情和身体反馈，不能只有人物上下抖动。
```

## 默认四镜方案

子 Agent 可以根据原图姿势微调，但应保持以下叙事和信息密度。

| 时间 | 镜头职责 | 动作与表演 | 机位与运动 |
| --- | --- | --- | --- |
| `0.000–3.400` | 开场并立即进入动作 | 从参考图状态直接进入交合。女生先抬眼，随后嘴唇微张、眉心收紧，髋部开始有节奏地迎送 | 低机位手持，缓慢推近上半身和脸部 |
| `3.400–7.100` | 侧后方性交特写 | 切到髋部、大腿、手和交合位置。男方稳定托住她的腿，她抓床单或他的手臂，身体随顶入前后移动 | 低侧机位贴近移动，轻微跟随动作摇晃 |
| `7.100–10.900` | 体位变化 | 平滑转到 M 字抬腿或侧面抬腿体位。她主动拉近男方，背弓起，脚趾收紧，眼神短暂失焦后重新看向镜头 | 低正面角度，小幅快速推镜，再横向轻移 |
| `10.900–15.000` | 表情与动作增强 | 回到女生脸部与上胸近景，保留下半身节奏。她咬唇、喘息加快、眼睛半闭，偶尔直视镜头，动作持续到最后一帧 | 面部近景缓慢环绕，最后小幅度拉远 |

每个镜头都必须同时具备以下信息：

- 当前体位和身体相对位置。
- 可见的交合动作或身体连接。
- 女生的表情变化。
- 男方脸部被排除在画面外。
- 明确的机位类型、方向、幅度和速度。
- 女性声音、环境声和物理声的时间点。

## 单图 H3 提示词模板

方括号内容由子 Agent 根据当前参考图替换。提交版本必须使用一个确定的 starting state，不能把方括号、条件判断或多选内容原样提交给模型。

```text
subject_definitions:
<Picture 1> is the exact single reference image and opening visual anchor for this video. It defines the scene, character identity, body state, wardrobe or nudity state, partner placement, surface, lighting, props, and camera geography.
<Subject 1> is the clearly adult fictional woman in <Picture 1>. Preserve her exact face, hair, makeup, body proportions, skin tone, current clothing or nudity state, and distinctive accessories.
<Subject 2> is the clearly adult fictional male partner in <Picture 1>. Preserve his body scale, hands, arms, torso, hips, and physical relationship to <Subject 1>. His entire head and face remain outside every target frame, and he produces no vocal sound.
<Subject 3> is the complete environment in <Picture 1>. Preserve its room, furniture, bedding or support surface, background geometry, lighting direction, color palette, and visible props.

summary:
[reference generation + keyframe completion] A 15-second vertical multi-shot video begins from <Picture 1> and immediately develops a consensual penetrative act between two clearly adult fictional characters. The action moves from the current position into active side-entry and M-leg missionary positions. The camera stays sexually explicit and dynamic while keeping <Subject 2>'s face out of frame. <Subject 1>'s changing expressions and audible breathing carry the performance.

retention_analysis:
<Picture 1> ([Shot 1] opening anchor): partially_preserved - its identity, scene, partner placement, surface, lighting, and opening body state are retained while the camera reframes and the action develops.
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - her identity, hair, body proportions, makeup, current clothing or nudity state, and distinguishing accessories remain consistent.
<Subject 2> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): partially_preserved - his torso, hands, hips, and sexual role remain continuous while his head and face are intentionally excluded from every frame.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - the room, furniture, bedding or support surface, background, props, and lighting direction remain unchanged.

detailed_description:
Photorealistic cinematic live-action with realistic skin, soft editorial lighting, shallow depth of field, and restrained handheld camera movement. Every visible person is a clearly adult fictional character. The two adults have already consented to the act.
[Shot 1] The video opens from <Picture 1> and preserves her [EXACT OPENING POSE AND CLOTHING OR NUDITY STATE]. <Subject 1> begins in direct physical contact with <Subject 2>, and the first visible penetrative rhythm starts immediately. Her lips part, her brows lift, her eyes meet the lens briefly, then flutter downward as her hips respond. Her hair, breasts, thighs, and the supporting surface move naturally with the developing rhythm. The camera performs a low handheld push-in with small amplitude at slow speed toward her flushed face and moving upper body. <Subject 2>'s face remains entirely outside the frame.
[Shot 2] At 00:03.400, the camera cuts to a low side close-up centered on <Subject 1>'s hips, raised thigh, the visible point of penetration, and <Subject 2>'s supporting hand and torso. <Subject 1> moves with a firm inward-and-outward rhythm. Her abdomen tightens as her pelvis meets his, one hand grips the mattress or support surface, and her free hand presses against his forearm. Her mouth opens with a sharper gasp and her brows tense. The camera tracks laterally at slow speed while shaking slightly with each impact.
[Shot 3] At 00:07.100, the video cuts to a low frontal medium close-up after a physically continuous change into an M-leg missionary position. <Subject 1> lifts her legs toward her upper body, and <Subject 2> supports both thighs with his hands and forearms. She reaches forward, pulls his torso closer, arches her back, and holds eye contact while the strokes become deeper. A large-amplitude handheld push-in at fast speed briefly emphasizes her parted lips and tense jaw, followed by a small lateral drift. <Subject 2> is cropped below the neck.
[Shot 4] At 00:10.900, the camera cuts to an intimate close-up of <Subject 1>'s face, bare shoulders, moving chest, and one hand pulling <Subject 2> closer. Her expression changes from focused tension to helpless pleasure. She bites her lower lip, closes her eyes for one breath, then looks directly into the lens. Her hips continue matching the thrusts, her hair sways, and her body visibly reacts through the final frame. The camera moves in a short face-level arc with small amplitude at slow speed, ending with both adults still physically joined and the rhythm continuing.

overall_soundscape:
Quiet room tone and natural mattress, fabric, and skin-contact sounds are synchronized with the visible movement. The only human vocal sound is <Subject 1>'s uneven breathing, gasps, and soft moans. <Subject 2> is completely silent with no speech, breath, groan, sigh, laugh, or other vocalization. No dialogue, off-screen voice, or music is present.

non_diegetic_music:
N/A
```

## 中文执行含义

```text
参考图中的成年虚构女性保持完整身份、身体、发型、当前衣着或赤裸状态和场景连续性。
男伴只保留身体、手臂、躯干和髋部，脸始终在画外，全程保持沉默。

前 3.4 秒从参考图姿势直接开始性交，女生先被动，再主动迎送。
3.4 秒切低侧特写，突出髋部、手、腿部以及清楚可见的交合动作。
7.1 秒转到抬腿的传教士体位，女生主动拉近男伴，表情从紧绷转愉悦。
10.9 秒切脸部和上胸近景，保留下半身持续动作，她咬唇、喘息、看向镜头。
画面始终有头发、胸部、腿部、床铺和皮肤的受力反馈，不能只让整个人上下抖动。

唯一的人声是女生的喘息与轻声呻吟。
男方不能说话、喘息或呻吟。没有对白、画外声音和音乐。
```

## 每张图的制作记录

批量任务中的每张参考图必须建立独立子目录。建议结构如下。

```text
projects/<批次名>/
├── batch_manifest.json
├── reference/
│   ├── 001.png
│   ├── 002.png
│   └── ...
├── 001/
│   ├── source.png
│   ├── shots.json
│   ├── prompt_en.txt
│   ├── prompt_zh.txt
│   ├── workflow_api.json
│   ├── manifest.json
│   ├── output/
│   └── qa/
├── 002/
│   └── ...
└── output/
```

单图 `shots.json` 至少记录：

```json
{
  "source_image": "source.png",
  "opening_state": "已插入，侧坐体位",
  "duration_seconds": 15,
  "aspect_ratio": "9:16",
  "shots": [
    {"shot": 1, "start": 0.0, "end": 3.4},
    {"shot": 2, "start": 3.4, "end": 7.1},
    {"shot": 3, "start": 7.1, "end": 10.9},
    {"shot": 4, "start": 10.9, "end": 15.0}
  ],
  "male_face_visible": false,
  "male_vocal_audio": false,
  "female_vocal_audio": true
}
```

这里只记录计划和验收状态。真正的 media 标签、输入路径和 workflow 节点必须与当前工作流 JSON 核对。

## 提示词交付规则

- `prompt_en.txt` 保存实际提交给模型的英文提示词。
- `prompt_zh.txt` 保存完整中文翻译，不混入英文执行字段。
- 只有对白、歌词和画面实际出现的文字可以保留原文。
- 参考标签在所有字段中含义一致。
- `<Picture 1>` 只对应当前参考图，不得在同一视频中偷偷加入下一张图。
- 最终提示词中不能保留方括号说明、候选句式或未决定的条件。
- 如果图片本身不适合默认体位，子 Agent 应先改写 opening_state 和 shot plan，再写最终提示词。

## 工作流与参数规则

- 从当前已经跑通的 V7 工作流复制一份，放入该图独立目录。
- 每张图使用独立的 workflow 副本或独立输入覆盖值，不复用上一个任务残留的提示词和文件路径。
- 参考图只替换到当前模板实际接收的 LoadImage 节点。
- 提示词只替换到当前模板实际接收的文本节点。
- 分辨率设为竖屏 `9:16` 和当前模板对应的 `0.9 MP` 级设置。
- 时长设为 `15` 秒，并检查帧数公式、24 FPS 和实际回片帧数。
- 模型、LoRA、采样器、SelfLift、Sigma 精化、VAE 和输出节点沿用已经验证的配置。
- 每张图对应一个新的任务，不把整批输入塞进一个 H3 上下文。
- 提交前校验 prompt 中的媒体标签和 workflow 输入顺序一致。

## 批处理状态与恢复

批处理任务必须有可恢复的总 manifest。单个任务失败时只重试该图，不重新提交整批。

总 manifest 至少记录：

- `batch_id`
- 输入图相对路径和哈希
- 每图状态 `pending`、`prepared`、`queued`、`running`、`done`、`failed`
- 本地 RH task ID
- RunningHub 远程 task ID
- 实际 prompt 文件路径
- 实际 workflow 文件路径
- 输出目录
- 失败阶段和脱敏后的错误摘要

恢复批次时先扫描实际文件，再读取 manifest。已经完成且通过 QA 的条目跳过，运行中的条目继续轮询，失败条目按任务状态单独重试。

## 提交与并发

默认并发为 `1`。先完成第一张样片并检查四镜、动作、身份、男性静音和输出规格，通过后再按当前账号额度扩大并发。个人 API Key 仍需遵守 RH Workflow Desk 的账号并发限制。

每次提交必须明确：

```text
execution_target: runninghub
task_name: <batch-id>-<三位序号>
workflow: 当前图片的独立 API 节点图
workflow_input_config: manual 或与当前工作流一致的模式
prompt_group: 当前图片实际使用的媒体和提示词组
output_dir: 当前图片独立输出目录
```

本地 API 返回 `202` 只表示任务进入 RH Workflow Desk 队列。必须继续轮询本地任务状态，并最终检查 RunningHub 远程任务和下载后的实际 MP4。

## 完成判定

单张视频只有同时满足以下条件才算完成：

- MP4 文件存在并可完整解码。
- 时长接近 `15` 秒，实际时长以帧数和 `ffprobe` 为准。
- 画幅为 `9:16`，分辨率达到当前模板的 720p 目标。
- 至少有四个可辨识镜头，切点与计划接近。
- 女生身份、发型、服装或赤裸状态和场景连续。
- 男方脸没有进入画面。
- 音频仅包含女生的人声，男方静音。
- 没有男性对白、喘息、呻吟、画外声音或非叙事音乐。
- 性交动作、身体接触和表情反应真实连续，没有只做上下抖动。
- 最终 MP4、提示词、工作流、任务记录和 QA 输出均落入该图独立目录。

批量完成状态还必须提供：

- 总图片数、完成数、失败数和跳过数。
- 每个成功视频的路径。
- 每个失败条目的失败阶段和可继续步骤。
- 实际使用的本地 RH task ID 与远程 task ID。
- 总 manifest 的最终状态。
