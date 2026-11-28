# MiniMax H3 工作流与 Prompt Group 生成 Agent 规范

## 文档目的

本文件是给负责视频制作辅助工作的 AI Agent 使用的执行规范。Agent 的任务不是只写一段可以复制的提示词，而是根据用户的视频要求，同时产出：

1. 可被 ComfyUI、AIGate 或 RH Workflow Desk 重新加载的 API 格式工作流 JSON；
2. 与工作流实际输入顺序一致、可以在 RH Workflow Desk 提示词工坊中重新组装的 Prompt Group；
3. 工作流、Prompt Group、sidecar 和索引之间可追溯的一致关联；
4. 必要时，VideoMake 项目目录中的英文提示词、中文翻译和复现记录。

本文件描述的是生成前、生成中和保存后的规则，不代表已经提交远程任务，也不代表视频已经生成成功。除非用户明确要求提交或运行，否则只生成并校验本地文件。

### “走 rh 流程”的固定提交入口

当用户说“走 rh 流程”或要求按本文流程提交 workflow 时，必须使用本文件第 8.4 节的 RH_CLI 本地 Web App API：`POST http://127.0.0.1:8766/api/tasks`。

这里的“走 rh 流程”不等于直接执行 `rh workflow run`，也不等于直接调用 RunningHub 的 `/task/openapi/create`。前端或 Agent 只把本地 workflow ID、远程 `workflowId`、输入文件路径和运行参数交给 RH_CLI 本地服务；由本地 `TaskManager` 负责上传、远程提交、轮询和下载。只有用户明确指定直接 RunningHub CLI/API 时，才使用 [`runninghub.md`](runninghub.md) 的独立路径。

## 1. 适用范围与权威顺序

执行任务时按以下顺序读取规则；发生冲突时，前面的规则覆盖后面的规则：

1. 用户明确提出的主体、动作、场景、时长、画幅、音频、镜头、对白、保留和修改要求；
2. 当前仓库的 `AGENTS.md`；
3. [`project-workflow.md`](project-workflow.md)、[`h3.md`](h3.md)、[`resources.md`](resources.md)、[`media-assets.md`](media-assets.md)、[`runninghub.md`](runninghub.md) 和相关项目规则；
4. 项目内 `minimax-h3-prompt` 及其下游 H3 Skill 的格式要求；
5. RH_CLI Web 的 `web/AGENTS.md` 和 `web/docs/h3-prompt-agent-guide.md`；
6. 当前资源 JSON、已验证工作流模板和当前 RH_CLI 的实际 schema；
7. 自由文本，只用于连接已有卡片、补充资源库没有覆盖的用户专属要求。

不要因为某个旧项目、截图、文件名或历史提示词看起来相似，就绕过当前规则。截图中的标题、按钮、数字和路径只能作为线索；工作流 ID、节点、输入顺序和资源 ID 必须从实际 JSON 或索引中确认。

## 2. 文件根目录与交付位置

文档所在项目为 VideoMake；如果任务要把结果登记到 RH Workflow Desk，目标是 RH_CLI 的 `web/data/`。在 Agent 的返回值、文档和内部记录中优先使用仓库相对路径，不要把 RH_CLI checkout 的绝对路径写入 Prompt Group。用户提供的临时媒体可按当前 schema 保留本机绝对 `media_path`，但不要把它误写成 RH_CLI 仓库路径或资源库路径。

```text
VideoMake/
├── ref/Resources.json                 # 资源清单入口
├── ref/prompt/library.json             # 固定提示词积木
├── ref/pose/pose.json                  # 动作/姿势卡
├── ref/character/character.json        # 人物和人物参考
├── ref/audio/audio.json                # 音频参考
├── ref/background/background.json      # 背景参考
├── ref/clothes/clothes.json            # 服装参考
├── workflows/                          # 已验证的共享模板
│   ├── 10erosBeta4生视频.json           # 默认一采
│   ├── 10ErosV7_单图图生视频_api.json    # V7 单图一采
│   └── 上采样.json                       # 提高 AI 视频分辨率
└── projects/<项目名>/                   # VideoMake 项目产物

RH_CLI/
└── web/data/
    ├── workflows/<workflow-file>.json
    ├── workflows/<workflow-id>.prompt_group.json
    ├── outputs/<task-id>/
    │   ├── workflow_api.json
    │   ├── prompt_group.json
    │   └── manifest.json
    ├── workflow-registry/
    │   ├── wf_81a715c3011b.json          # 直接生成 AI 视频的登记入口
    │   └── wf_a17e80d7ccc1.json          # 视频分辨率提升的登记入口
    ├── prompt/groups/<group-id>.json
    ├── prompt/groups.json
    └── workflow-registry.json
```

如果只为 VideoMake 项目制作文件，工作流和提示词应放在 `projects/<项目名>/`；如果要让 RH Workflow Desk 重新加载，必须另外完成 `web/data/` 下的 Prompt Group、sidecar 和索引关联。不要把最终视频、音频、图片或 workflow JSON 放进 `docs/`。

## 3. 不可违反的总原则

- 不覆盖已经验证的工作流、提示词、输出或用户的未相关修改；修改现有方案时先复制并使用新的版本名。
- 不创建或猜测 API Key、账号、远程 `workflowId`、代理密码、cookie、带 token 的 URL 或不存在的资源 ID。
- 不把资源库中的所有卡片机械塞进每条提示词；只选与当前需求相关且不冲突的卡片。
- 不把姿势深度图当作另一位角色、另一张独立动作或风格参考；彩色原图和深度图属于同一动作卡。
- 不把“Prompt Group”理解成六段文字模板。用户要求使用媒体时，组内必须存在真实的 `reference`、`action` 或 `media` 项。
- 不先写 `<Picture N>`、`<Video N>` 或 `<Audio N>`，再猜它们对应哪个文件。先读取工作流实际输入顺序，再建立标签。
- 不以 JSON 写入成功、任务入队或接口返回成功作为视频生成成功；生成后必须检查实际输出文件。
- 不在提示词中加入资源卡片已经确定但用户没有要求修改的相互矛盾细节。

## 4. Agent 的输入与需求解析

收到用户的视频要求后，先建立内部需求记录。没有被用户指定的字段保持未指定，不要擅自增加身份、服装、镜头、音乐或剧情限制。

```text
project: 项目名或待创建的项目名
shot_scope: 单段工作流 / 长片段分段 / 明确多镜头
mode: T2VA | I2VA | FL2VA | L2VA | Full-reference/Ref2VA
duration: 目标秒数和全局时间线位置
aspect_ratio: 横屏 / 竖屏 / 自定义比例
resolution: 默认 0.9 MP/720p，或用户明确要求的规格
visual_inputs: images / videos / none
audio_inputs: audio / none
subjects: 人物、物体、服装、道具和身份特征
setting: 背景、空间、时间、光线和材质
action: 起始状态、动作启动、发展过程和结果状态
camera: 景别、角度、运动类型、方向、幅度和速度
dialogue: 稳定说话人 ID、语言和逐字对白
sound: 环境声、物理声、非语言人声和画面内音乐
score: 观众专属的非叙事配乐，或无
visible_text: 画面中必须出现的原文文字
retention: 哪些内容 fully_preserved、partially_preserved、attribute_transfer 或 weak_reference
output: 期望的 workflow、Prompt Group、项目文件和输出位置
```

如果用户明确要求多个镜头、分镜、切镜或蒙太奇，先确认镜头数量，再按播放顺序逐镜确认。视频达到 10 秒而用户没有说明单镜头或多镜头时，先询问是否采用多镜头；未得到确认前不要格式化最终多镜头提示词。只有逐镜计划已确认，才允许写最终 `[Shot]` 时间轴。

## 5. 选择 H3 模式与生成分段

### 5.1 模式选择

| 模式 | 实际输入 | 选择条件 | 提示词起点 |
| --- | --- | --- | --- |
| `T2VA` | 无视觉参考 | 完全由文字描述生成 | 直接进入三个基础字段，不写首帧对齐声明 |
| `I2VA` | 一张首帧图 | 从给定画面向后延展 | 从首帧可见状态开始，随后写动作启动、发展和结果 |
| `FL2VA` | 首帧图和尾帧图 | 需要在两个确定画面之间完成转场 | 明确首帧与尾帧时间点，中间写可观察的变化 |
| `L2VA` | 一张尾帧图 | 让模型推断前置动作并落到给定结尾 | 先写合理的前置状态，再写收束到尾帧的转场 |
| `Full-reference/Ref2VA` | 任意图片、视频和音频参考组合 | 需要复用身份、场景、动作、镜头、音色或源音频 | 必须使用六个固定字段和稳定参考标签 |

有图片、视频或音频参考职责时，默认优先使用 Full-reference；只有用户明确声明图片只是纯首帧/尾帧边界、没有其他可复用参考职责时，才使用 keyframe 专项模式。普通角色图、背景图、服装图、姿势图、参考视频或音色都不是“只负责首帧”的图片。

### 5.2 时长、帧数与分辨率

- 本地单个工作流通常为 2–15 秒；官方在线/API 约束按当前 H3 Skill 执行，通常为 4–15 秒；本地运行时更窄时以本地限制为准。
- 固定 24 FPS，H3 帧数使用 `17n+5` 对齐，画布宽高为 32 的倍数，原生 H3 通常使用 batch size 1。
- 若长度节点接收帧数，可用下式将秒数向上对齐到合法帧数；`a` 是目标秒数：

  ```text
  max(5, round(a * 24)) + (5 - (max(5, round(a * 24)) % 17)) % 17
  ```

- 默认分辨率为 `0.9 MP`/`720p`，除非用户明确要求覆盖。
- 目标为 1080p 级视频时，将 `ResolutionSelector.megapixels` 设为 `2`；此时每段最长 10 秒，仍需满足 24 FPS、`17n+5` 和 32 倍数。
- 长片优先按自然画面切点、鼓点或起音点分段。不要机械固定使用 15 秒（2MP 时 10 秒），不要拆出低于 2 秒的尾段，也不要默认把每个 2–3 秒镜头都拆成独立工作流。
- 锁定源音频时，每个工作流的音频裁切范围必须与该段全局起止时间完全一致；最终剪辑边界不能只采用提示词中的时间戳。

图片、视频、音频输入数量通常分别不超过 9 张 Picture、3 个 Video 和 3 个独立 Audio，总文件数不超过 12 个。若当前本地节点或模板有更窄限制，以实际节点 schema 为准。

## 6. 读取资源并建立输入映射

### 6.1 资源读取顺序

先读取 `ref/Resources.json`，使用它的 `media_root` 从 `ref/` 定位六类 JSON，再读取这些 JSON。解析媒体时，角色、音频、背景和服装条目优先相对于各自索引文件所在目录，姿势条目的 `pose/...` 路径相对于 `ref/` 根目录：

| 来源 | schema | 资源用途 | Prompt Group 类型 |
| --- | --- | --- | --- |
| `prompt/library.json` | `blocks` | 模式字段、对象、镜头、场景、声音和配乐积木 | `fixed` |
| `pose/pose.json` | `actions` | 姿势、动作起点和空间关系；含彩色原图/深度图配对及可选骨骼图 | `action` |
| `character/character.json` | `references` | 人物身份、外貌、体型、配饰和音色 | `reference` |
| `audio/audio.json` | `references` | 源音频、音乐或音色参考 | `reference` |
| `background/background.json` | `references` | 地点、空间结构、环境和光线 | `reference` |
| `clothes/clothes.json` | `references` | 服装款式、材质、颜色和结构 | `reference` |

每次都读取 JSON 当前内容，不把数量、分类或 ID 写死在 Agent 逻辑中。检索同时使用 `category`、`tags`、`title` 和 `text`；空的 `image_path`、`audio_path`、`color_image_path` 或 `depth_image_path` 不能被当成可用媒体。

### 6.2 资产职责

- 人物卡负责身份、五官、发型、体型、比例、配件或角色音色；包含人物参考图时，还要读取 `ref/character/人物描述.md` 中对应角色的脸型、眼睛、眉毛、鼻子、嘴唇、肤色、发型和配饰，并将这些文字约束写进 `<Subject N>`。不能只依赖图片。
- 服装卡负责服装，不自动替换人物身份、脸、发型或体型。
- 背景卡负责空间、陈设、色彩、时间和光线，不自动引入其中的人物、Logo、招牌或文字。
- 动作卡负责姿势、身体朝向、主体相对位置、动作起点和镜头关系。需要动作参考时保留 `color_image_path`、`depth_image_path`、可用的 `skeleton_image_path` 和同一 `pair_key`；深度图和骨骼图只承担结构辅助职责。
- 音频卡直接复用时使用真实 `audio_path`；仅借鉴曲风时写成音频参考，不声称已经复制原音频。
- 参考视频默认只用于研究风格、动作、镜头或效果；只有用户明确要求才接入工作流的 Video 输入。

如果多个卡片描述同一属性，选择更具体、与用户要求匹配度更高的一张，不要无条件拼接两个冲突的人物、背景、服装或动作。敏感姿势或成人参考只有在角色为成年人、素材有授权且任务符合平台和项目规范时才允许接入，不能自动带入普通项目。

### 6.3 输入顺序和标签

先从 H3 conditioning 节点读取真实的 `ref_images.ref_image_N`、`ref_videos.ref_video_N` 和 `ref_audios.ref_audio_N` 连接，再建立映射表：

| H3 标签 | 工作流节点/字段 | Prompt Group 项 | 资源 ID 或路径 | 参考职责 |
| --- | --- | --- | --- | --- |
| `<Picture N>` | `node:field` 或 `ref_images.ref_image_N` | `reference` / `action` / `media` | 真实资源或用户输入 | 首帧、人物、服装、背景、动作等 |
| `<Video N>` | `node:field` 或 `ref_videos.ref_video_N` | `media` 或外部参考记录 | 真实视频路径 | 剪辑、续写、动作或镜头结构 |
| `<Audio N>` | `node:field` 或 `ref_audios.ref_audio_N` | `reference` / `media` | 真实音频路径 | 源音频、音频参考或音色 |

编号由工作流实际接收顺序决定，不由资源索引顺序决定。一个媒体文件只分配一个明确角色；同一个角色可以由多个不同职责的媒体共同约束，但必须在 `subject_definitions` 中写清职责边界。动作彩色图和深度图属于同一动作参考，不能产生两个不相关的 `<Subject>`。

## 7. 生成英文 H3 提示词

H3 提示词是带时间轴的视听制作简报，不是静态图片说明。字段和描述默认全部使用英文，只有以下两类内容保留原文：

- 对白/歌词：放在 `<d>[Language] ...</d>` 中，逐字保留，不放翻译、动作或音效；
- 画面中实际出现的文字：放在英文双引号中，保留原文、大小写和标点。

### 7.1 基础模式模板

T2VA 不写对齐首行；I2VA、FL2VA、L2VA 必须把对齐声明放在最前面，然后空一行，再写三个字段：

```text
[I2VA/FL2VA/L2VA alignment instruction]

integrated_multimodal_description:
[Shot 1] Describe the opening state, subject, setting, style, action, and camera.
[Shot 2] At MM:SS.mmm, describe a new observable action, cut, or transition.

overall_soundscape:
[Ambience, physical sounds, and non-verbal human sounds only.]

non_diegetic_music:
[Audience-only score with instrumentation, tempo, rhythm, and dynamics; or N/A.]
```

模式内时间轴规则：`[Shot 1]` 不带时间戳；后续 `[Shot N]` 的时间戳严格递增、落在目标时长内；每次切镜必须带来新的主体状态、空间、视角、时间或叙事信息。只有景别或角度的小变化时，优先使用相机运动而不是无意义切镜。

动作必须写成可观察的因果链：起始姿态 → 动作启动 → 动作发展 → 结果状态。相机运动使用可执行英文，并可写明幅度和速度，例如 `Push In with small amplitude at slow speed`、`Tracking Shot at fast speed`、`Static Shot`、`Arc Shot with large amplitude`。

### 7.2 Full-reference / Ref2VA 模板

有多个图片、视频、音频参考，或需要身份/场景/动作/音频职责分离时，严格按以下六个字段和顺序输出：

```text
subject_definitions:
<Subject 1>: [Stable identity and visible attributes.]
<Picture 1>: [Concrete frame or image-reference role.]
<Audio 1>: [Audio role, if present.]

summary:
[keyframe completion + reference generation] [Requested result using the defined labels.]

retention_analysis:
<Subject 1>: fully_preserved
<Picture 1>: partially_preserved
<Audio 1>: reference

detailed_description:
[Style and composition before the first shot.]
[Shot 1] Describe the opening state and the first observable action.
[Shot 2] At MM:SS.mmm, describe the next causal change and camera behavior.

overall_soundscape:
[Ambience, physical sounds, and non-verbal sounds only.]

non_diegetic_music:
[Audience-only score, or N/A.]
```

`detailed_description` 通常写约 350–500 个英文单词；先写风格和构图，再写按时间推进的镜头。`summary` 的目的前缀只能来自真实用途：`keyframe completion`、`reference generation`、`video editing`、`video continuation`、`audio reuse`、`audio reference`，不要堆叠无关前缀。

可见内容的保留标记只能使用 `fully_preserved`、`partially_preserved`、`attribute_transfer`、`weak_reference`；音频只能使用 `fully_copy`、`partially_copy`、`reference`、`weak_reference`。参考不等于复制，发生换装、转场、重绘或音频变化时不能标成全程完全保留。

### 7.3 声音、对白和文字分层

- `integrated_multimodal_description`：角色动作、对白、歌唱、角色能听到的现场音乐和与画面同步的声音事件；
- `overall_soundscape`：环境声、物理声和非语言人声，通常 1–4 个英文句子；
- `non_diegetic_music`：只有观众听到、画面角色听不到的配乐，通常 1–3 个英文句子，说明乐器、速度、节奏和动态；没有配乐但有环境声时写 `N/A`，完全静音时也写 `N/A`。

每个说话人分配稳定的 `(S1)`、`(S2)` 编号，并在所有镜头中保持不变。第一次出现时先在 `<d>` 外说明声音特征和身份；`<d>` 内只放 `[Language]` 和逐字原文。画外音使用 `says in an off-screen voiceover`，并说明嘴唇保持闭合。跨切镜对白使用 `<scenetrans>` 和连续性描述，被截断的对白以 `<cutoff>` 结尾。

## 8. 生成 API 工作流 JSON

### 8.1 先复用已验证模板

按任务选择已验证的模板。默认一采和独立上采样使用下表入口。明确使用 10Eros V7 单图生成时，使用下文的 V7 模板。

| 用途 | 唯一 RH_CLI 登记入口 | 实际 API 节点图 | VideoMake 工作副本 |
| --- | --- | --- | --- |
| 直接生成 AI 视频 | `RH_CLI/web/data/workflow-registry/wf_81a715c3011b.json` | `RH_CLI/web/data/workflows/wf_81a715c3011b_10Eros一采.json` | `workflows/10erosBeta4生视频.json` |
| 提高 AI 视频分辨率 | `RH_CLI/web/data/workflow-registry/wf_a17e80d7ccc1.json` | `RH_CLI/web/data/workflows/wf_a17e80d7ccc1_10Eros第二采.json` | `workflows/上采样.json` |

这里的 `workflow-registry/<workflow-id>.json` 是工作流登记入口，保存工作流名称、账号、远程 `workflowId`、输入配置和 Prompt Group 关联；真正可提交的 ComfyUI API 节点图是对应的 `web/data/workflows/*.json` 文件。Agent 必须先读取登记入口确认关联，再以对应的实际 API 节点图或 VideoMake 副本为修改基础。

默认直接生成使用 `10erosBeta4生视频.json`。将已有视频提高到 720p 或 1080p 时使用 `上采样.json`，按 [§8.5](#85-480p-初采后的人工-review-闸门) 确认初采结果。复制模板后仅修改必要字段，保留各模板的 latent、音频、采样器和输出路由。

#### 10Eros V7 单图图生视频

从 [V7 API 模板](../workflows/10ErosV7_单图图生视频_api.json) 复制一份到 `projects/<项目名>/`，再填写参考图和最终英文提示词。模板依据已跑通的 RH 任务 `2125916172121894913`，默认请求 10 秒、480p 级 9:16 竖屏、24 fps，输出带原生音频的 MP4。实测回片为 **480×864、243 帧、10.125 秒**，通过完整解码。实际时长以回片帧数为准。 [RunningHub 公开工作流](https://www.runninghub.ai/post/2076684097694466049)

**涉及人物运动时，采样必须固定为 5 低分辨率 + 3 高分辨率 + 1 步 sigma 精化。** 人物运动包括人物动作、位移、转身、手势、脱衣、身体表演以及性交等可观察的运动状态变化。复制模板后必须设置：

```text
124.inputs.steps = 8
235.inputs.transition_step = 5
235.inputs.lowres_scale = 0.4
147.inputs.extra_steps = 1
```

这是同一条 8 步基础调度在 SelfLift 第 5 步切换分辨率：前 5 步低分辨率，后 3 步高分辨率；不是两个独立采样器的拼接。`H3SigmaRefiner` 随后再加 1 步 sigma 精化，所以最终总评估次数为 9。模板原有的 6 步基础调度加 1 步精化仅可作为非人物运动的对照基线，不得直接用于人物运动。

| 节点 | 使用方法 |
| --- | --- |
| `150` · LoadImage | `inputs.image` 填本次参考图。它连接 `136.inputs.ref_images.ref_image_0`，对应提示词的 `<Picture 1>`。首帧意图写在提示词里。 |
| `232` · Text (Multiline) | `inputs.value` 填完整英文 H3 提示词。它直接连接 `136.inputs.prompt`。图里已移除 Gemma、llama.cpp 和提示词切换分支，模型收到的就是这段文字。 |
| `115` · ResolutionSelector | 480p 级竖屏使用 `9:16 (Portrait Widescreen)`、`megapixels: 0.41472`、`multiple: 32`。更换画幅时尽量先匹配参考图的宽高比。 |
| `132` · Duration | `inputs.value` 按秒填写，默认 10。帧数由 `131` 计算。 |
| `235` · SelfLiftH3Sampler | 更换 `inputs.seed` 可生成变体；涉及人物运动时必须设置 `transition_step: 5`、`lowres_scale: 0.4`，实现前 5 步低分辨率、后 3 步高分辨率。 |
| `124` / `147` | 涉及人物运动时固定为：基础调度 `steps: 8`，sigma 精化 `extra_steps: 1`。不要把 8 步理解成两套独立采样器。 |
| `239` / `180` | `239` 加载 V7 模型。 `180.inputs.filename_prefix` 可改成当前项目名，视频和原生音轨会一起输出。 |

通过 [§8.4 的 RH Desk 本地 API](#84-通过-rh_cli-本地-web-api-提交工作流) 提交。发送项目副本的完整节点图作为 `workflow`，并使用以下字段映射：

```json
{
  "execution_target": "runninghub",
  "remote_workflow_id": "2076684097694466049",
  "workflow_input_config": {"mode": "auto", "items": []},
  "files": {"150:image": "/absolute/path/to/reference.png"},
  "prompts": {"232:value": "<与节点 232 一致的完整英文提示词>"}
}
```

同时提供本次 `prompt_group` 和项目的 `output_dir`。远程编号适用于已验证的 RunningHub AI 公开入口，复用时核对当前账号和入口权限。若使用自己的云端副本，先保存该副本，再填它的实际工作流编号。完成后检查 MP4、帧率、时长、音轨和完整解码。

### 8.2 API JSON 最低结构

工作流必须是 ComfyUI API 格式：顶层以节点 ID 为键，每个节点至少有 `inputs` 和 `class_type`，可有 `_meta`。例如：

```json
{
  "6": {
    "inputs": {
      "prompt": ["59", 0],
      "width": ["16", 0],
      "height": ["16", 1],
      "length": ["15", 1],
      "task_type": "Ref2VA",
      "audio_mode": "lock_source",
      "strict_prompt_tags": true,
      "ref_images.ref_image_0": ["13", 0],
      "ref_audios.ref_audio_0": ["52", 0]
    },
    "class_type": "MiniMaxH3AudioConditioningT8",
    "_meta": {"title": "MiniMax H3 Audio Conditioning (T8)"}
  }
}
```

实际节点 ID、输出端口和字段必须从复制的模板读取。以下清单以 T8 图为例，V7 图按上文的节点表核对对应输入与输出。

- H3 conditioning 节点的 `prompt`、`task_type`、`audio_mode`、`width`、`height`、`length`；
- `ref_images.ref_image_N`、`ref_videos.ref_video_N`、`ref_audios.ref_audio_N` 的输入连接和顺序；
- `ResolutionSelector` 的 `aspect_ratio`、`megapixels` 和 `multiple`；
- `LoadImage`、`LoadVideo`、`LoadAudio` 的实际文件路径或可注入字段；
- 音频是 `native`、`lock_source`、`remix_source`、`reference_only` 还是其他当前节点支持的模式；
- `MiniMaxH3DualClockSamplerT8`、`PT_H3ConcatAVLatent`、AV Decode 和最终视频输出的原有连接；
- `VHS_VideoCombine` 的 24 FPS、输出格式、音频连接和是否按音频裁切。

### 8.3 允许的最小修改

从模板复制后，通常只修改：

1. H3 prompt 节点或其连接的文本节点中的最终英文提示词；
2. 用户选择的 `LoadImage`、`LoadVideo`、`LoadAudio` 路径；
3. 时长输入和由它计算出的合法帧数；
4. 画幅、`ResolutionSelector.megapixels` 和尺寸相关节点；
5. 与用户明确要求一致的 `task_type`、`audio_mode`、`prompt_primary_audio_ordinal`、参考输入开关和输出前缀；
6. 已确认失效的路径或节点契约。

不要擅自修改未知的模型、采样器、scheduler、LoRA、VAE、latent 类型、连线、输入数量或质量参数。已知的 H3 3D latent upscaler 契约是：`device` 使用后端字符串（如 `"cuda"`），`precision` 使用 `"fp16"`；不能把布尔值当作设备或精度。如果原模板使用 `PT_H3ConcatAVLatent`，保留其视频和音频 latent 到最终采样器的连接。V7 使用 `MiniMaxH3ReferenceToVideo` 到 SelfLift 的原有音视频 latent 连接。

### 8.4 通过 RH_CLI 本地 Web API 提交工作流

本文所说的“Web App API”特指 RH_CLI 的本地 Web/Electron 应用 API。只有用户明确要求远程提交或运行时，才执行本节；默认仍只生成和校验本地文件。RH Workflow Desk 的浏览器页面只负责调用本机 HTTP 服务；本地 `TaskManager` 会校验并保存任务，再按 `execution_target` 将工作流提交到 RunningHub 或本地 ComfyUI，轮询并下载结果。

**易错约定：** 提交 workflow 文件时，默认入口只能是本地 `POST http://127.0.0.1:8766/api/tasks`，不能改用 `rh workflow run`，也不能绕过 RH_CLI 直接请求 RunningHub API。每次提交都必须显式标注执行目标：`execution_target: "runninghub"` 表示交给 RH/RunningHub，`execution_target: "comfyui"` 表示交给已配置的本地 ComfyUI。请求中的 `workflow_id` 是本地 `wf_...` 登记 ID；`remote_workflow_id` 只在 RunningHub 目标下用于调度远端 workflow。

RH_CLI 本地 Web API 与原始 ComfyUI 工作流 API 的关系如下：

| 提交路径 | 适用对象 | 提交内容 |
| --- | --- | --- |
| RH_CLI 本地 `/api/tasks` | RH Workflow Desk 本地任务队列 | 工作流引用或 API 节点图、明确的执行目标、输入路径、Prompt 和运行参数 |
| RunningHub `/task/openapi/create` | 原始 ComfyUI API 工作流 | 由本地 TaskManager 发送的完整节点图 |

**单文件 4MB 硬限制。** `files` 中每个路径对应的输入文件都必须不超过 **4 MB**。为消除 MB 与 MiB 的差异，按严格 **4,000,000 bytes** 检查。该规则适用于 RH Workflow Desk 和 `execution_target: "runninghub"`，并优先于 RunningHub 接口文档中的平台上限说明。超限文件应先缩小、转码或压缩，再生成提交请求。检查方法和处理要求见 [`runninghub.md`](runninghub.md) 的“单个输入文件限制”。

从 RH_CLI 仓库根目录启动本地服务：

```bash
./web/start.sh --no-browser
```

默认服务地址为 `http://127.0.0.1:8766`。提交前先检查 `GET /api/health`，再使用 `POST /api/tasks`。下面是标注为 RH/RunningHub 目标的请求示例：

```json
{
  "workflow_id": "<local-workflow-id>",
  "execution_target": "runninghub",
  "remote_workflow_id": "<runninghub-workflow-id>",
  "files": {
    "<node-id>:<field>": "/absolute/path/to/input.png"
  },
  "prompts": {
    "<node-id>:<prompt-field>": "<final-english-prompt>"
  },
  "prompt_group": {
    "id": "<task-group-id>",
    "name": "<group-name>",
    "updated_at": 0,
    "items": []
  },
  "custom_inputs": {},
  "random_noise": {},
  "resolution": {},
  "bypassed_nodes": [],
  "instance_type": "default",
  "output_dir": "/absolute/path/to/output",
  "output_prefix": "chinatsu-showcase"
}
```

请求规则：

1. 每次请求都必须显式指定 `execution_target`：`runninghub` 走 RH/RunningHub，必须提供 `remote_workflow_id`；`comfyui` 走设置中保存的本地 ComfyUI 服务器，不需要 `remote_workflow_id`。省略时服务端会退回设置里的默认平台，但 Agent 提交时不得省略；同时在项目 README 或任务记录中写明“RH”或“本地 ComfyUI”。
2. `workflow_id` 使用 RH_CLI 工作流库中的本地 ID；如果提交尚未保存的 API 工作流，可在请求中传入 `workflow` 节点字典。目标为 `runninghub` 时仍须提供真实的 `remote_workflow_id`。
3. `files` 的键必须与工作流实际识别出的 `node:field` 一致，值必须是存在的本机文件；不要把资源库 ID、浏览器 Blob URL 或远程下载 URL 当成本地输入路径。
4. Agent 提交时应显式传 `prompt_group` 完整对象，或传已保存的 `prompt_group_id`；不要依赖浏览器当前选中的组或 localStorage 状态。若省略二者，本地服务才会捕获当前提示词工坊组装台状态。
5. `prompts` 的键必须指向实际的 Prompt 字段；最终 Prompt 应与 `prompt_group.items` 的组装结果保持非空文本行一致。即使提示词组为空，也应显式传 `items: []`，不要传 `prompt_group: null`。
6. `output_dir` 是本次任务的有效输出根目录；任务级复现文件会写入 `<output_dir>/<local-task-id>/`。输入媒体不会复制到该目录，`manifest.json` 只保存 `files` 中的原始路径。
7. `output_prefix` 是可选的本地下载文件名前缀，只填写基础名称，不要填写目录路径或扩展名。例如 `chinatsu-showcase` 会生成 `chinatsu-showcase_1.mp4`、`chinatsu-showcase_2.png`；省略时继续生成 `output_1.mp4`。它控制 RH_CLI 本地落盘名称，不替代工作流 `SaveVideo`/`SaveImage` 节点中的 `filename_prefix`。
8. 本地接口返回 `202` 只表示任务已加入 RH_CLI 本地队列；响应中的 `task.id` 是本地任务 ID，不等于 RunningHub 远程 `taskId`。
9. 使用 `GET /api/tasks/<local-task-id>` 读取本地状态，直到状态为完成或失败；完成后检查任务产物和 `/api/tasks/<local-task-id>/output/<index>` 实际返回的媒体文件，并确认任务目录内的三个快照文件存在。
10. 本地 API 不接收前端提交的 API Key；凭据由 RH_CLI 本机配置和任务调度器读取。不得把密钥写入请求示例、工作流、Prompt Group、manifest 或任务记录。

每次提交成功后，任务目录应形成一个可复现包：

```text
<output_dir>/<local-task-id>/
├── workflow_api.json    # 提交前已应用 files/prompts/参数覆盖的工作流快照
├── prompt_group.json    # 本次提交实际使用的 Prompt Group 快照
└── manifest.json        # 两者、运行参数和输入路径的绑定清单；不含输入文件副本
```

`web/data/workflows/<workflow-id>.prompt_group.json` 是工作流库级 sidecar，供工作流库加载；`<output_dir>/<task-id>/prompt_group.json` 是任务级快照，供历史任务复现。二者不是同一个索引，历史任务加载必须以任务目录中的快照为准。

本地 Web API 最适合从 VideoMake 生成内容、再交给 RH Workflow Desk 排队执行的场景。它提交的是原始 ComfyUI API 工作流。

### 8.5 480p 初采后的人工 Review 闸门

当用户要求“先生成 480p，确认效果后再上采样”或等价的分阶段流程时，480p 初采必须作为人工 review 闸门，不得自动进入上采样：

1. 480p 任务完成后，先确认本地任务状态为 `completed`，并检查实际视频文件、分辨率、帧率、时长、音轨和可读性；需要时生成接触表并核对白词或字幕时间。
2. 将 480p 实际成片路径交给用户 review；在用户明确回复“确认上采样”或同等含义前，不得提交上采样任务、创建上采样成品软链接或把上采样版本标记为最终交付。
3. 上采样必须是独立的后续 RH 任务，输入只能是已经交给用户 review 的 480p 成片，并单独记录本地 task ID、远程 task ID 和实际输出路径。
4. 如果误提交了未获确认的上采样任务，应立即通过 `POST /api/tasks/<local-task-id>/cancel` 请求取消；即使远端无法撤回，也不得采用或交付该结果，并在复现记录中标明取消/弃用状态。

### 8.6 Web App API 提交的站点与账号绑定教训

远程 `workflowId` 不只是一个数字，它还属于特定的 RunningHub 站点和账号。提交前必须同时核对：

- 当前 RH Web App 账号是目标站点对应的账号；本次二采工作流应使用 `akai / ai`；
- 调度凭据使用本机已配置的 `ai-rh`，不能让通用模式自动选到 `cn-rh`；
- `remote_workflow_id`、`workflow_id`、文件节点键（如 `52:audio`）和输入路径都来自当前实际工作流，而不是历史截图或相似任务。

本次实际教训是：在通用模式下把二采任务交给 `POST /api/tasks` 后，调度器自动选择了 `cn-rh`，远程端返回 `workflow not exists`（错误码 380）。这不是工作流 JSON 本身不存在，而是远程 workflow 所属站点与被选 API Key 不匹配。改用 `akai / ai` 账号并绑定 `ai-rh` 后，同一工作流和输入才获得了远程 taskId。

推荐的重试顺序：

1. 用 `GET /api/tasks/<local-task-id>` 检查 `error`、`dispatch_key_name`、`dispatch_key_site` 和 `remote_task_id`；不要把 `202` 或“本地已入队”当成远程提交成功。
2. 若出现 `workflow not exists`，先停止或取消仍在本地等待的错误任务，切换当前账号到目标站点（本次为 `akai / ai`），再使用本机配置的 `ai-rh` 重新提交；不要盲目重复同一个错误站点。
3. 重试后继续读取本地任务，必须看到 `dispatch_key_name=ai-rh`、`dispatch_key_site=ai` 和非空的远程 `taskId`，再记录为“已提交”；任务完成后仍需检查实际视频产物。

切换账号可通过 RH Web App 的本地接口完成（`<ai-account-id>` 使用 `GET /api/state` 返回的真实账号 ID，不写入 API 密钥）：

```http
PATCH http://127.0.0.1:8766/api/settings
Content-Type: application/json

{"current_account_id":"<ai-account-id>"}
```

然后仍使用 `POST http://127.0.0.1:8766/api/tasks` 提交；如需锁定本机凭据，可在请求中传入已配置凭据的本地 `key_id`，但绝不把 API Key 本身放进请求、工作流、Prompt Group 或文档。

### 8.7 动作迁移：用深度+骨骼参考视频作为 Video 输入

当用户要求“基于参考视频做动作迁移”，且希望同时利用身体姿态和前后空间关系时，先把参考视频制作成一条结构控制视频，再把这条视频接入 H3 的 Video 输入。不要把原真人视频直接当作唯一控制依据，也不要把深度图、骨骼图拆成互不关联的多条视频。

标准数据流如下：

```text
原始参考视频
    ↓ 24fps 逐帧抽取
每帧彩色图 ──→ Depth Anything V2 ──→ 黑白灰度深度图（8-bit grayscale）
       └────→ DWPose body/face/hands ─→ RGB skeleton
depth + skeleton（同一帧合成）
    ↓ 保持原时序、画幅和时长，建议静音
深度+骨骼参考视频
    ↓ VHS_LoadVideo 输出 0
H3 conditioning.ref_videos.ref_video_N
```

本项目的颜色约束必须保持不变：**深度图是黑白连续灰阶图，骨骼图保留 RGB 彩色线条和关键点**。不要为了统一格式把骨骼图转成黑白；只有在制作控制视频时，才将黑白深度底图与彩色骨骼图按相同帧号叠加。

#### 8.7.1 逐帧制作与合成

0. **优先先缩放到目标控制尺寸，再抽帧和推理。** 先读取当前 H3 `ResolutionSelector` 的目标宽高，制作保持画幅和时序的低分辨率工作副本；例如本项目 480p 版本使用 480×864 控制画幅。保留原始参考视频作为只读来源，但不要先对 720p/1080p 帧生成整套深度与骨骼图、再把派生图整体缩小。
   - 先缩放主要减少逐帧 PNG 的读写、内存、合成视频编码和远程上传体积，也能降低 H3 读取参考 Video 时的显存压力。
   - 不要假设推理时间会按像素比例下降：当前项目的 Depth Anything 包装器固定将输入 letterbox 到 518×392，DWPose 也先缩放到 `detect-resolution=512`；因此速度收益主要来自 I/O、后处理和远程显存，而不是模型前向本身。
   - 缩放后再按 24fps 抽帧，深度图和骨骼图从同一批目标尺寸帧生成；保持帧号、尺寸、画幅和时长一致。若需要更高精度对比，可保留高分辨率派生副本，但提交给 H3 的控制 Video 应优先使用目标尺寸版本。
1. 保留原始参考视频不变，在项目的中间目录或可重建的临时目录中按 24fps 抽帧。输入视频应符合 H3 Video 参考的 2–15 秒范围；帧文件按播放顺序使用稳定的六位编号。
2. 使用 Depth Anything V2 为每帧生成与目标尺寸帧相同宽高的黑白深度图，格式为 `PNG、8-bit grayscale`。这里的“黑白”指黑、白之间的连续灰阶，不是彩色图，也不是只有纯黑/纯白的二值遮罩。该深度图是相对深度结构，不是带物理单位的距离图；不能把不同视频的灰度值当作绝对距离直接比较。
3. 使用 DWPose 逐帧生成与目标尺寸帧相同宽高的 `PNG、RGB` 骨骼图，至少检查头、肩、肘、腕、髋、膝、踝；如果还需要手势，保留手部关键点。检测不到人体、人体数量异常或关键点明显跳变时，先修复输入或标记失败，不用手工猜线补帧。
4. 对同一编号的深度图和骨骼图做同帧合成，输出一条视频。必须以黑白灰度深度作为底图、保留高对比彩色骨骼线叠加；禁止先把骨骼帧转灰度。保持目标控制 Video 的 9:16/横竖画幅、24fps、帧数和动作时序。参考视频只承担结构控制职责，建议移除音频，避免把源音频误当成 H3 音频要求。
5. 深度图、骨骼图和合成视频都属于派生中间资产；最终项目至少保留合成视频、来源路径、目标尺寸、处理方式和 QA 记录，逐帧目录可按项目清理规则删除并由脚本重建。

#### 8.7.2 接入 H3 工作流

工作流中把深度+骨骼合成视频作为一个独立的 Video 文件输入，不要把它伪装成普通 `LoadImage` 或拆成两个无时序关系的 Picture：

```json
{
  "97": {
    "inputs": {
      "video": "/absolute/path/to/depth_skeleton_reference.mp4",
      "force_rate": 24
    },
    "class_type": "VHS_LoadVideo"
  },
  "6": {
    "inputs": {
      "ref_videos.ref_video_0": ["97", 0]
    },
    "class_type": "MiniMaxH3AudioConditioningT8"
  }
}
```

实际节点 ID、字段和端口必须从当前核心模板读取；上例中的 `97`、`6` 只是结构示意，不能直接照抄。人物身份、服装和面部仍使用独立的 Picture 输入，不能要求深度/骨骼视频同时承担角色身份职责。

提示词必须为合成视频分配稳定的 `<Video N>` 标签，并明确：

- 保留骨骼定义的关节位置、肢体方向、手势时序、身体节奏、走位、机位和前后深度层次；
- 将深度灰度场、彩色骨骼线、关键点、跟踪标记、真人身份、脸部、服装、皮肤纹理、水印和源音频视为技术参考，不渲染到成片；
- `retention_analysis` 通常标记为 `partially_preserved`，因为保留的是动作和结构，不是参考视频的可见外观；
- 若没有明确要求复用音频，使用 `audio_mode: native`，由 H3 生成新的原生双声道音频。

#### 8.7.3 提交前和生成后验收

至少完成以下检查后才提交和交付：

- 深度帧、骨骼帧和合成视频数量一致；深度图必须是黑白连续灰阶 PNG（`8-bit grayscale`，禁止彩色或二值遮罩），骨骼图为 RGB PNG，所有帧尺寸一致；
- 合成参考视频通过 `ffprobe` 检查为 24 FPS、时长在 2–15 秒、画幅与原动作参考一致；若按结构控制使用，确认音频已移除；
- 工作流中 `VHS_LoadVideo` 输出 0 确实连接到 `ref_videos.ref_video_N`，提示词中的 `<Video N>` 与该输入一一对应；
- `files` 使用合成参考视频的绝对路径，角色 Picture 使用独立的真实文件路径；所有文件在本机可读；
- H3 英文提示词不超过 7000 字符，且明确禁止把深度/骨骼技术图渲染到最终视频；
- 通过 RH_CLI 本地 `POST /api/tasks` 提交时，先检查账号、站点和 `ai-rh`，再轮询本地任务直到出现非空远程 taskId 和 `completed`；
- 生成完成后用 `ffprobe`、完整解码和接触表检查成片的尺寸、帧率、时长、音轨、角色一致性、动作迁移效果以及是否出现深度/骨骼图泄漏。

如果项目副本删除或替换了模板中的旧输入节点，且 RH_CLI 工作流登记中仍保存旧的输入配置，提交请求应显式传入当前 `workflow` 节点字典和 `workflow_input_config: {"mode":"auto","items":[]}`，避免旧节点 ID 被重新套用；提交后以任务级 `workflow_api.json` 和 `manifest.json` 作为实际复现依据。

## 9. 生成 Prompt Group、sidecar 和索引

### 9.1 Prompt Group 的组装模型

Prompt Group 是有顺序的项目数组。固定字段标题、真实媒体卡片和自由文本都作为独立 item 保存；UI 会按 item 顺序组装英文提示词。固定积木、媒体资源和自由文本的职责如下：

- `kind: "fixed"`：只能引用 `prompt/library.json` 中真实存在的 `block_id`，并保存快照；
- `kind: "reference"`：引用 `character`、`audio`、`background`、`clothes` 等 JSON 中真实存在的 `reference_id`，并保存资源职责和快照；
- `kind: "action"`：引用 `pose/pose.json` 中真实存在的 `action_id`，保存动作文字、彩色原图、深度图和 `pair_key` 的可追溯信息；
- `kind: "media"`：用户提供的首帧、尾帧、临时图片、视频或音频，不虚构媒体库 ID；
- `kind: "text"`：只补资源库没有覆盖的动作衔接、时间推进、结果状态或用户专属限制。

Prompt Group 不能只有 `kind: "text"`。如果用户要求使用人物、姿势、背景、服装、音频或首帧，必须把真实 `reference`、`action` 或 `media` 放进组内，并在保存前检查 ID 和路径。

### 9.2 单个组文件的结构

组文件保存为 `web/data/prompt/groups/<group-id>.json`，由 PromptStore 读取。以下是结构模板；占位符必须替换为真实值：

```json
{
  "version": 1,
  "id": "group-<unique-id>",
  "name": "<human-readable group name>",
  "updated_at": 0,
  "items": [
    {
      "instance_id": "fixed-<unique-id>-subjects",
      "kind": "fixed",
      "block_id": "<real-block-id>",
      "snapshot": {
        "category": "对象与留存",
        "tags": [],
        "title": "对象定义",
        "text": "subject_definitions:"
      }
    },
    {
      "instance_id": "reference-<unique-id>-character",
      "kind": "reference",
      "reference_id": "<real-character-reference-id>",
      "reference_kind": "character",
      "snapshot": {
        "title": "<resource title>",
        "text": "<resource English description>",
        "tags": [],
        "image_path": "<resource relative image path>",
        "audio_path": "",
        "media_type": "image"
      }
    },
    {
      "instance_id": "action-<unique-id>-pose",
      "kind": "action",
      "action_id": "<real-pose-action-id>",
      "snapshot": {
        "category": "<pose category>",
        "title": "<pose title>",
        "text": "<pose English description>",
        "tags": [],
        "color_image_path": "<paired color path>",
        "depth_image_path": "<paired depth path>",
        "pair_status": "<verified pair status>"
      }
    },
    {
      "instance_id": "media-<unique-id>-first-frame",
      "kind": "media",
      "media_path": "<local user-provided path>",
      "media_name": "<file name and role>",
      "media_kind": "image",
      "media_mime": "image/png"
    },
    {
      "instance_id": "text-<unique-id>-transition",
      "kind": "text",
      "text": "<only the user-specific transition not covered by a card>",
      "translated_text": "<optional Chinese translation>",
      "generated_type": "workflow-specific"
    }
  ]
}
```

实际保存时遵循当前 RH_CLI PromptStore 的字段规范：`fixed` 使用 `block_id`，`reference` 使用 `reference_id`，`action` 使用 `action_id`，`media` 使用 `media_path`/`media_kind`/`media_mime`。动作的 color/depth 文件和 `pair_key` 必须从 `pose.json` 重新核验；如果当前版本的规范化逻辑把它们放进 `snapshot`，仍不能丢失这组配对关系。

`text` 是最终进入英文提示词的文本；不能把中文说明写进 `text`。`translated_text` 可保存中文翻译或 UI 翻译结果；当文本已经是最终生成的英文，必要时设置 `translation_disabled: true`，避免 UI 再次误翻译。

### 9.3 sidecar 与两个索引

与工作流关联的 sidecar 保存为：

```text
web/data/workflows/<workflow-id>.prompt_group.json
```

sidecar 至少包含与组文件一致的 `id`、`name`、`updated_at` 和 `items`。它是工作流包的提示词组快照；组文件是提示词工坊的可复用组，两者内容必须一致。

任务级快照另存于：

```text
<output_dir>/<local-task-id>/prompt_group.json
```

它记录“这一次提交实际使用的组”，不依赖之后工作流库中的 sidecar 是否被替换。历史任务页面加载时，应优先读取这个任务级文件；工作流库页面加载时，才读取 `web/data/workflows/<workflow-id>.prompt_group.json`。因此，不能只把任务目录里的文件放着而不把路径绑定到 task 记录，也不能用工作流级 sidecar 代替任务级快照。

`web/data/prompt/groups.json` 只保存索引，不重复承载完整 items：

```json
{
  "version": 1,
  "folders": [],
  "groups": [
    {
      "id": "group-<unique-id>",
      "name": "<same group name>",
      "updated_at": 0,
      "file": "groups/group-<unique-id>.json"
    }
  ]
}
```

`web/data/workflow-registry.json` 中只更新对应工作流记录的关联字段，并保留已有字段：

```json
{
  "prompt_group_id": "group-<unique-id>",
  "prompt_group_name": "<same group name>"
}
```

如果修改了工作流输入路径、节点默认值、时长或分辨率，同时同步 registry 中的 `input_config`；其中每项至少应能追溯到 `node_id`、`field`、实际默认值和输入顺序。不要只改 API JSON 而让 UI 的默认输入仍指向旧文件。

### 9.4 保存顺序

按以下顺序保存，便于出现中断时恢复：

1. 复制并写入新的 API 工作流 JSON；
2. 写入 `web/data/prompt/groups/<group-id>.json`；
3. 写入 `web/data/workflows/<workflow-id>.prompt_group.json`；
4. 更新 `web/data/prompt/groups.json` 的 group 索引；
5. 更新 `web/data/workflow-registry.json` 的 `prompt_group_id`、`prompt_group_name` 和必要的 `input_config`；
6. 如果同时提交任务，在任务自己的 `<output_dir>/<local-task-id>/` 中写入 `workflow_api.json`、`prompt_group.json` 和 `manifest.json`，并将三个路径绑定回本地 task 记录；
7. 若是 VideoMake 项目交付，同时保存 `projects/<项目名>/..._prompt.txt`、可选的 `..._prompt_zh.txt` 和项目 README/QA 复现信息。

任务级保存不复制输入文件。`manifest.json` 只记录 `files`、`prompts` 的路径/字段映射和其他提交参数；如果原输入路径日后失效，任务仍能被识别和复盘，但不能保证重新运行成功。

## 10. 保存后的最低校验

### 10.1 结构和引用校验

- API JSON、任务级 `prompt_group.json`、任务级 `manifest.json`、Prompt Group、sidecar、`groups.json` 和 `workflow-registry.json` 都能被 JSON 解析；
- API JSON 是顶层节点字典，每个节点的 `class_type` 和 `inputs` 结构完整；
- `block_id` 能在 `prompt/library.json` 中找到；`reference_id` 能在对应参考 JSON 中找到；`action_id` 能在 `pose.json` 中找到；
- 每个选中的图片、视频、音频、动作原图和深度图路径都存在；明确声明为“等待用户提供”的输入除外；
- 动作的彩色图和深度图存在，且来自同一个 `pair_key`；
- 所有 `<Picture N>`、`<Video N>`、`<Audio N>` 都能映射到真实的工作流输入；没有未绑定标签；
- `Prompt Group` 不只有自由文本；媒体职责、资源 ID、路径和快照可追溯；
- group 文件、sidecar 和 registry 的 group ID、名称和 items 关联一致；
- API JSON 中的最终 prompt 与 Prompt Group 的组装结果非空文本行一致，允许 UI 组装造成额外空行。
- 每个已提交任务都能从 task 记录定位到 `workflow_snapshot_path`、`prompt_group_snapshot_path` 和 `manifest_path`；三个文件位于同一个任务目录；
- `manifest.json` 的 `inputs.policy` 为 `paths-only`，任务目录没有输入媒体副本；
- 历史任务若已有有效任务级 `prompt_group.json`，已补齐上述绑定；没有该文件的旧任务不伪造 Prompt Group。

### 10.2 H3 语义校验

- 模式与输入类型匹配；I2VA/FL2VA/L2VA 对齐声明在首行，Full-reference 六字段顺序正确；
- `[Shot 1]` 无时间戳，后续时间戳严格递增且不超时长；
- 动作包含可观察的起始状态、发展过程和结果，不只写抽象情绪或“更电影感”；
- 相机运动写明类型，必要时写幅度和速度；
- `(S1)` 等说话人 ID 在所有镜头中稳定；对白逐字放在正确的 `<d>` 中；
- `overall_soundscape`、画面叙事声音和 `non_diegetic_music` 没有互相混入；
- 参考标签的职责在 `subject_definitions`、`summary`、`retention_analysis` 和 `detailed_description` 中保持一致；
- 提示词总字符数符合当前 H3 Skill/运行时限制，必要时控制在 7000 字符以内并留出结构调整空间；
- 中文只存在于翻译字段、对白原文或画面实际文字，不进入英文执行提示词的描述字段。

### 10.3 工作流和媒体校验

- 时长、24 FPS、`17n+5` 帧数、32 倍数尺寸和 0.9 MP/2MP 规格符合项目要求；
- 2MP 段落不超过 10 秒；普通段落不超过当前运行时允许的上限；
- 锁定源音频时 `audio_mode`、音频输入顺序、驱动音频、最终音频和输出音轨连接一致；
- 保留模板中已验证的 H3 latent、音频 latent、AV decode、双时钟 sampler 和最终输出路径；
- `VHS_VideoCombine` 实际输出为可播放视频，并接收到正确的图像和音频；
- 若提交原始 ComfyUI 工作流，先用 JSON 工具和本地文件检查，再使用与节点字段一致的 `rh workflow run` / `--file "nodeId:field=path"` 注入输入；
- 若通过 RH Workflow Desk 本地 Web API，先确认 `/api/health`，再 `POST /api/tasks`；`202` 只代表进入本地队列，必须继续读取本地任务状态并检查实际输出；
- 每个待上传输入文件均不超过 4 MB，并按严格 4,000,000 bytes 核验；
- 若远程 workflow 属于 `ai` 站点，确认当前账号为对应的 `akai / ai`，调度凭据为 `ai-rh`；若错误选到 `cn-rh`，先修正站点/账号再重试；
- 最后运行相关测试、`git diff --check`、`git status --short`，并确认没有把凭据或不相关改动带入本次交付。

## 11. VideoMake 项目文件与 RH_CLI 文件的对应关系

当一次任务同时需要两个项目的产物时，使用以下对应关系：

| 内容 | VideoMake | RH_CLI Web |
| --- | --- | --- |
| API 工作流 | `projects/<项目名>/<segment>_workflow_api.json`（从 §8.1 对应模板复制） | `web/data/workflows/<workflow-file>.json`，登记入口为对应的 `workflow-registry/wf_*.json` |
| 英文提示词 | `projects/<项目名>/<segment>_prompt.txt` | 写入 API prompt 节点并由 Prompt Group 组装 |
| 中文翻译 | `projects/<项目名>/<segment>_prompt_zh.txt` | Prompt Group 自由文本的 `translated_text`（如 UI 需要） |
| 提示词组 | 可在项目 README/QA 中记录 group ID | `web/data/prompt/groups/<group-id>.json` |
| 工作流关联快照 | 项目 README/QA 记录 | `web/data/workflows/<workflow-id>.prompt_group.json` |
| 索引关联 | 项目 README/QA 记录 | `web/data/prompt/groups.json`、`web/data/workflow-registry.json` |
| RH_CLI 本地 Web API 提交记录 | 项目 README/QA 记录本地 API 请求摘要、本地 task ID 和输出路径 | `POST /api/tasks`、任务历史、任务级工作流/Prompt Group/manifest 快照和本地输出目录；输入只保留路径 |
| 生成结果 | `projects/<项目名>/output/` | 任务自己的 `web/data/outputs/<task-id>/` 或用户指定目录 |

VideoMake 的英文提示词文件必须是可执行英文正文；中文翻译是完整对应版本，不能把中文解释混进英文文件。RH_CLI 的 Prompt Group 不是 VideoMake 项目的替代品，而是让提示词可以按资源卡片在 Web 工具中重新编辑、恢复和追溯。

## 12. Agent 默认返回契约

除非用户明确只要求某一份文件，否则返回结果至少包含：

1. `Mode`、分段时长、画幅、分辨率、音频模式和输入类型；
2. 已选媒体卡片：来源、标题、真实 ID、文件路径、参考职责；动作卡注明原图/深度图配对；
3. 已选固定积木：标题、真实 `block_id` 和用途；
4. 自由文本补充点：只列资源库未覆盖的内容；
5. API 工作流、Prompt Group、sidecar 和索引的相对路径；
6. 最终英文 H3 提示词，以及 VideoMake 项目需要的中文翻译路径；
7. 校验结果：JSON、资源路径、输入顺序、标签、时间轴、音频分层、帧数/分辨率和关联索引是否通过；
8. 如果用户要求提交：提交路径（RH_CLI 本地 Web API 或原始工作流 API）、执行目标（RH/RunningHub 或本地 ComfyUI）、真实 `workflowId`（适用时）、本地/远程 task ID、节点映射、输出路径和实际完成状态；若走本地 Web API，必须记录任务级 `workflow_api.json`、`prompt_group.json`、`manifest.json` 路径；
9. 未解决事项：例如“未找到匹配卡片”“首帧等待用户提供”“本地节点 schema 未确认”。

如果资源库没有匹配项，明确写出“未找到匹配卡片”，再用最少量自由文本补齐。绝不虚构人物设定、卡片 ID、媒体路径、音频内容、远程 workflowId 或生成成功状态。

## 13. 最终执行清单

```text
[ ] 已读取根 AGENTS、H3/项目/资源规则和 RH_CLI Web 指南
[ ] 已解析用户需求，未擅自增加未指定约束
[ ] 已确认 H3 模式、单镜头/多镜头状态、段落时长和全局时间线
[ ] 已读取 Resources.json 及其指向的六类 JSON
[ ] 已选择真实且不冲突的媒体卡片，并确认文件存在
[ ] 已确认动作 color/depth 与 pair_key
[ ] 已按工作流真实输入顺序建立 Picture/Video/Audio 映射
[ ] 已按对应 H3 格式生成英文提示词
[ ] 已复制匹配的 API 工作流模板并只做有证据的最小修改
[ ] 已按 §8.1 选择默认一采、V7 单图一采或独立上采样模板
[ ] 已保留 H3 latent、音频、采样器和输出节点的有效路由
[ ] 已区分 RH_CLI 本地 `POST /api/tasks` 与原始工作流 API `/task/openapi/create`
[ ] 若使用 RH_CLI 本地 Web API，已验证 `/api/health`、本地 task ID、任务状态和实际输出
[ ] 若采用“先 480p 后上采样”，480p 已完成基础 QA 并已交给用户 review；未获明确确认前未提交上采样
[ ] 若使用本地 Web API，已确认工作流 ID、远程 workflowId、节点字段和输入路径
[ ] 若使用本地 Web API，已显式提交 `prompt_group` 或 `prompt_group_id`，并确认它与最终 `prompts` 一致
[ ] 若使用本地 Web API，已确认任务目录含 `workflow_api.json`、`prompt_group.json`、`manifest.json`，且 task 记录绑定了三者路径
[ ] 已确认 `manifest.json` 只记录输入路径，没有复制输入媒体；原始输入路径仍然可访问
[ ] 已确认远程 workflow 所属站点与当前账号/API Key 一致（本次为 `akai / ai` + `ai-rh`）
[ ] Prompt Group 含真实 reference/action/media 项，不是全 text
[ ] 已同步 group 文件、sidecar、groups.json 和 workflow-registry.json
[ ] API JSON、Prompt Group、路径、ID、标签、时长、帧数和音频均已校验
[ ] 未写入任何密钥、token、cookie、凭据或带 token 的 URL
[ ] 已检查 git diff --check、git status --short 和相关测试
[ ] 未把“文件已写入”误报为“视频已生成成功”
```
