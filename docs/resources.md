# `ref/Resources.json` 资产库索引与使用方法

本文件说明如何使用资产索引；资产生成、下载、深度图和媒体分析见 [`media-assets.md`](media-assets.md)，项目阶段和目录安排见 [`project-workflow.md`](project-workflow.md)。

## 文档定位

[`ref/Resources.json`](../ref/Resources.json) 是 VideoMake 的通用可复用视频资产总入口。它通过 `sources` 指向提示词积木、姿势、角色、音频、背景和服装六类 JSON 索引；这些索引记录条目 ID、分类、标签、文字描述和媒体路径，方便在制作 MiniMax H3 视频前选择参考资产。

索引中的媒体实体保存在 `ref/` 下的对应资产目录；`Resources.json` 只负责声明索引入口和媒体根目录，具体条目分别保存在对应 JSON 的 `blocks`、`actions` 或 `references` 数组中。`sources` 路径相对于 `ref/` 根目录；分类 JSON 中的媒体路径优先相对于所属索引文件所在目录解析，并兼容相对于 `ref/` 根目录的旧路径；`pose.json` 当前使用 `pose/...` 路径。使用时必须同时确认 JSON 描述和实际文件，不能只根据文件名猜用途。

当前索引快照如下；数量是当前文件内容的核对结果，后续检索和 Agent 逻辑必须动态读取 JSON，不能把这些数字写死：

| 来源 | 顶层数组 | 当前条目数 | 媒体字段 |
| --- | --- | ---: | --- |
| [`prompt/library.json`](../ref/prompt/library.json) | `blocks` | 125 | 文本积木，无媒体路径 |
| [`pose/pose.json`](../ref/pose/pose.json) | `actions` | 57 | 彩色原图、深度图、骨骼图 |
| [`character/character.json`](../ref/character/character.json) | `references` | 157 | 图片和角色音色 |
| [`audio/audio.json`](../ref/audio/audio.json) | `references` | 6 | 音频路径 |
| [`background/background.json`](../ref/background/background.json) | `references` | 14 | 背景图片路径 |
| [`clothes/clothes.json`](../ref/clothes/clothes.json) | `references` | 6 | 服装图片路径 |

`ref/character/人物描述.md` 仍作为角色五官、发型和配饰的补充文字资料使用；它不是六类 JSON 的替代索引。当前索引核验还发现 `character.json` 中 `蜜汁猫裘/15.jpg` 的媒体文件尚未在工作区找到，使用该卡片前必须先处理这一缺失，不要自行替换成相似图片。

`ref/` 各目录可以保留未纳入当前索引的历史或项目专属文件（例如 `ref/background/assets/` 下的梦核背景、`ref/pose/video/` 下的动作视频）。它们可以在项目复现记录中按真实路径引用，但不能冒充已有 JSON 卡片；要在 Prompt Group 或 Agent 中作为资源卡选择，必须先补入对应 JSON 并完成路径核验。

## 资产分类

| 分类 | 目录 | 独立索引 | 主要用途 | 使用时锁定的内容 |
| --- | --- | --- | --- | --- |
| `prompt` | `ref/prompt/` | [`library.json`](../ref/prompt/library.json) | H3 字段、对象、镜头、场景、声音和配乐固定积木 | 只复用真实 `block_id` 和文本快照，不把它当媒体参考 |
| `audio` | `ref/audio/` | [`audio.json`](../ref/audio/audio.json) | 音乐、源音频、音频驱动和角色音色参考 | 按 `audio_path` 和用途接入；锁定源音频时保持原轨不变 |
| `character` | `ref/character/` | [`character.json`](../ref/character/character.json) | 角色身份、脸部、发型、服装、场景或音色参考 | 按条目用途选择；身份图主要锁定脸部、发型和角色识别特征 |
| `clothes` | `ref/clothes/` | [`clothes.json`](../ref/clothes/clothes.json) | 独立服装或搭配参考 | 服装款式、材质、颜色、结构和装饰，不自动替换角色身份 |
| `background` | `ref/background/` | [`background.json`](../ref/background/background.json) | 场景、建筑、舞台和环境参考 | 空间结构、陈设、色彩、时间和光线；不自动引入图中的人物或文字 |
| `pose` | `ref/pose/` | [`pose.json`](../ref/pose/pose.json) | 姿势、构图、人物相对位置和镜头角度参考 | 身体朝向、四肢位置、主体位置、景别、视角和透视关系 |

### `prompt`

`prompt/library.json` 的 `blocks` 数组只保存可复用文本积木，不保存图片或音频。使用时必须引用真实 `id`，并根据当前 H3 模式选择结构、对象、镜头、声音、对白或音乐字段；用户专属限制再用自由文本补充。

### `audio`

`audio/audio.json` 的 `references` 数组保存音乐、源音频、音频驱动和音色卡片。直接复用时检查真实 `audio_path` 和格式；只借鉴曲风时不要声称已经复制原音频。角色音色仍优先从对应角色目录或角色卡中的 `audio_path` 选择。

### `character`

当前主要按 `二次元`、`真人` 和角色名称组织。一个角色可能有多种不同职责的图片，例如：

- 通用五官描述：用于把脸型、眼睛、眉毛、鼻子、嘴唇和肤色等身份特征写入提示词；
- 正脸头像或大头照：适合锁定脸部、发型和表情；
- 全身正视图或三视图：适合补充服装结构、身体比例、侧面和背面信息；
- 服装变体、猫娘版或其他造型：只在项目明确需要该造型时使用；
- 音色：通常作为角色声音参考，不应当误接到其他角色。

同一角色的多张图不一定可以全部上传。先根据任务确定每张图的职责，再决定是否接入工作流。

### `clothes`

`clothes` 中的图片主要是无人物或弱人物依赖的服装展示图。它们用于描述服装本身，不应被当作角色身份图。使用时应在提示词中明确：

```text
Use the clothing reference only for the outfit design, materials, colors, and construction. Preserve the character identity, face, hair, and body proportions from the character reference.
```

如果服装图上带有品牌、印花、道具或人体模特，必须判断这些元素是否需要保留；不需要时在提示词中明确排除。

### `background`

`background` 中的图片用于场景空间和环境气氛。使用前检查：

- 场景是否为空镜，是否含有不希望出现的 NPC、人物或道具；
- 画面中的 Logo、招牌、海报和文字是否需要保留；
- 图片的横竖比例是否适合目标视频；
- 该图是普通背景参考，还是明确要作为首帧/尾帧。

背景参考只负责场景，不应覆盖人物身份、服装或姿势职责。若场景图中存在不需要的角色或文字，应在提示词中写明排除项。

### `pose`

`pose` 条目通常同时提供：

- `ref/pose/color/`：彩色姿势原图，用于理解人物姿态、构图和镜头关系；
- `ref/pose/depth/`：对应的深度图，用于辅助空间层次、前后关系和姿势结构；
- `ref/pose/skeleton/`：对应的骨骼图，用于辅助关节位置和身体结构；
- `ref/videoRef/`：独立的参考视频目录，不属于当前 `pose.json` 动作卡的媒体字段。

深度图是结构辅助，不是人物身份、服装、材质或画面风格参考。除非当前工作流明确支持该输入，否则不要把深度图当作普通彩色参考图上传。

当前 `pose` 分类包含成人敏感姿势参考。使用前应确认角色均为成年人、素材具有授权且任务符合平台和项目规范；不要把索引中的敏感素材自动接入普通角色或公开项目。

## 从索引选择资产的标准流程

### 1. 先确定任务需要哪些职责

先把需求拆成身份、服装、场景、姿势、声音和首帧/尾帧等职责。例如：

```text
角色身份：锁定脸部、发型和角色识别特征
服装：锁定服装款式和材质
背景：锁定空间、陈设和光线
姿势：锁定身体位置、动作起始状态和镜头关系
声音：锁定角色音色或源音频
```

不要因为一张图同时包含人物和背景，就默认它能同时承担所有职责。优先使用用途明确的参考图；需要混合职责时，在提示词中明确每张图的范围。

### 2. 在对应 JSON 索引中定位条目

使用角色名、服装名、场景名或姿势关键词搜索；先读取 `Resources.json` 的 `sources`，再在对应 JSON 的 `category`、`tags`、`title` 和 `text` 中检索。条目中的媒体路径、描述和用途应一起阅读：

- 图片链接确认实际资产文件；
- `text` 可用于构造身份、场景、姿势或服装文字约束；
- `category`、`tags` 和 `title` 用于检索和判断用途；
- `image_path`、`audio_path`、`color_image_path`、`depth_image_path` 和 `skeleton_image_path` 决定可接入的真实媒体；
- 角色的细化五官描述还要结合 `ref/character/人物描述.md`，不能只依赖图片。

### 3. 确认文件真实存在和格式

`Resources.json` 和各 `sources` 入口以 `ref/` 为基准；解析具体媒体时，先按所属分类 JSON 的目录查找，姿势卡再按 `ref/` 根目录查找其 `pose/...` 路径。接入前至少确认文件存在、格式可读、方向和比例正确：

```bash
test -f "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
sips -g pixelWidth -g pixelHeight "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
file "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
```

视频或音频参考还要用 `ffprobe` 检查时长、帧率、音轨或编码。索引中的相对链接和实际文件不一致时，先修正索引或资产归档，再接入工作流。

### 4. 分配 H3 参考标签

`<Picture N>`、`<Video N>` 和 `<Audio N>` 的编号由当前工作流的实际上传顺序决定，不由 JSON 数组顺序决定。每次调整上传顺序，都要同步检查：

- 提示词中的标签；
- ComfyUI `Load Image`、视频和音频节点；
- `subject_definitions` 中的主体定义；
- 项目 README 或复现记录中的资产清单。

推荐先建立一张项目内的映射表：

| H3 标签 | 资产路径 | 参考职责 |
| --- | --- | --- |
| `<Picture 1>` | `ref/character/<角色>/<文件名>` | 角色身份 |
| `<Picture 2>` | `ref/clothes/<文件名>` | 服装 |
| `<Picture 3>` | `ref/background/<文件名>` | 场景背景 |
| `<Picture 4>` | `ref/pose/color/<文件名>` | 姿势和镜头 |
| `<Picture 5>` | `ref/pose/depth/<文件名>` | 姿势结构辅助 |

上表只是编号示例；实际编号必须以当前工作流为准。没有接入工作流的标签不得写进严格模式提示词。

### 5. 在提示词中声明每张图的职责

Full-reference 提示词中，应让模型知道每个主体负责什么，避免不同参考图互相污染。可按实际标签调整下面的结构：

```text
subject_definitions:
<Subject 1> is the character identity reference, defined by <Picture 1>.
<Subject 2> is the clothing reference, defined by <Picture 2>.
<Subject 3> is the environment reference, defined by <Picture 3>.
<Subject 4> is the pose and camera-angle reference, defined by <Picture 4>.

detailed_description:
Preserve the identity from <Subject 1> and the outfit design from <Subject 2>.
Use <Subject 3> only for the environment and lighting.
Refer to the initial action and camera position shown in <Subject 4>.
Describe the final body orientation, limb placement, subject positions,
camera angle, shot size, perspective, and lighting in plain language.
```

如果使用的不是 Full-reference，而是 I2VA、FL2VA、L2VA 或其他模式，应按对应模式的提示词结构书写，并保持参考标签与实际输入一致。H3 模式和字段规则见 [`docs/h3.md`](h3.md)。

## `pose` 姿势参考的正确提示词用法

### 姿势参考只锁定空间关系

姿势图的主要作用是提供动作起始状态、身体朝向、人物相对位置和镜头语言。它不应自动决定：

- 角色是谁；
- 角色的脸、发型和身份特征；
- 服装、材质和颜色；
- 背景中的人物、Logo、文字或水印；
- 目标视频的最终动作强度或敏感内容。

当角色、服装和姿势来自不同参考图时，提示词必须明确职责边界，例如：

```text
The pose reference controls only the body arrangement, subject positions,
initial action, and camera framing. Preserve the character identity from
the character reference and the outfit from the clothing reference. Do not
copy the pose reference's face, hair, clothing, background, text, or watermark.
```

### 使用索引内的姿势模板

`pose/pose.json` 的每个 `actions` 条目提供可复用的姿势结构和英文提示词。使用时把姿势图绑定到一个明确的参考主体，再在 `detailed_description` 中说明动作起始状态和镜头位置：

```text
subject_definitions:
<Subject 4> is the pose and camera-angle reference, defined by <Picture 4>.

detailed_description:
Refer to the initial action and camera position shown in S4.
```

这里的 `4` 和 `S4` 是索引中的示例编号。若当前工作流使用其他上传编号，必须把 `<Picture 4>`、`<Subject 4>` 和 `S4` 统一替换为实际标签，不能只改其中一处。

### 不要只写“跟随姿势”

为了让姿势参考真正可执行，应继续用文字描述以下信息：

1. 画面横向或竖向，以及人物数量；
2. 主体位于画面的哪个区域，其他主体是否部分出画或被遮挡；
3. 躯干、头部、双臂和双腿的朝向与位置；
4. 哪个身体区域更靠近镜头，以及前景和背景的层次；
5. 镜头从正面、背面、侧面或斜侧方拍摄；
6. 镜头处于高位、平视或低位，采用俯拍、平拍或仰拍；
7. 景别、透视效果、运动方向和光线环境。

通用描述骨架如下：

```text
The frame is [horizontal/vertical] and contains [number] subject(s).
The primary subject is positioned at [location] in the frame, with the
torso facing [direction] and the head turned [direction]. The arms and legs
are arranged as [clear placement]. [Describe foreground/background overlap
and which subject or body area is closest to the camera.] The camera is at
[front/back/side/oblique] and [high/eye-level/low] position, using a
[high-angle/level/low-angle] [shot size], creating [perspective effect].
The environment and lighting are [description].
```

最终提示词应把这段结构改写成符合当前角色和场景的英文描述；中文解释可以保存在对应的中文提示词文件中，但不要把中文说明混入英文执行提示词代码块。

### 历史 `magapixels` 备注怎么用

当前 `ref/pose/pose.json` 不记录 `magapixels` 字段。案例文档中出现的 `magapixels = 0.4` 或 `1` 是历史工作流参数备注，不能当成当前动作卡的资源属性，也不能从资源索引自动推导。

实际工作流通常使用 `megapixels` 字段。处理历史案例或引用旧参数时：

1. 先确认当前工作流的 `ResolutionSelector` 或等效节点实际字段名；
2. 把案例中的数值作为待验证的起始配置，不要无条件覆盖项目已有参数；
3. 生成后检查实际宽高、画幅、时长、帧数、姿势可辨识度和主体遮挡；
4. 如果结果不准确，优先修正姿势文字、镜头描述和参考图映射，再考虑调整分辨率。

## 常见误用

| 误用 | 正确做法 |
| --- | --- |
| 只看文件名，不看条目描述 | 同时阅读图片、描述和用途，并确认实际文件 |
| 把角色图、服装图、背景图、姿势图全部当成身份参考 | 在 `subject_definitions` 和提示词中声明每张图的职责 |
| 直接复制姿势参考图的脸、衣服或背景 | 明确姿势参考只控制空间关系和镜头，身份与服装由其他参考提供 |
| 把深度图当作普通彩色图或风格图 | 只在工作流支持时作为结构辅助，并保留对应彩色图的职责说明 |
| 使用图中自带的 NPC、Logo、文字或水印而未确认 | 在提示词中明确保留或排除，并进行生成后检查 |
| 参考标签与上传顺序不一致 | 维护项目级标签映射表，逐项检查提示词和工作流节点 |
| 把参考视频自动作为 `<Video N>` 输入 | 默认先作为动作/镜头研究；只有任务明确要求时才接入视频节点 |
| 用一个参考图承担互相冲突的多个职责 | 拆分为独立参考图，或在提示词中写清楚优先级和保留范围 |

## 新增或更新资产时的维护规则

1. 将可复用实体归档到 `ref/` 对应分类，不把一次性项目素材混入资源库。
2. 在对应 JSON 的 `blocks`、`actions` 或 `references` 数组中新增条目，填写稳定 `id`、分类、标签、文字描述和真实媒体路径；不要恢复已删除的分类 Markdown 索引。
3. `Resources.json` 的来源路径相对于 `ref/` 根目录；分类 JSON 的媒体路径优先相对于所属索引文件目录，姿势 JSON 沿用 `pose/...` 相对于 `ref/` 根目录的路径。项目或工作流记录资产时，统一使用完整的 `ref/<分类>/...` 路径。
4. 姿势条目应在同一个 action 对象中登记 `color_image_path`、`depth_image_path`、`pair_key` 和可用的 `skeleton_image_path`；`image_path` 仅保留为兼容别名。
5. 新增人物描述时，区分通用五官、发型、服装和配饰；详细角色特征可补充到 `ref/character/人物描述.md`，不要让通用五官描述隐含某一套衣服。
6. 生成或迁移资产后确认文件真实存在、格式可读、路径可打开；不要覆盖已验证资产，也不要用相似文件替代缺失路径。
7. 修改索引前后检查 JSON 可解析性和 `git diff --check`，并在提交前确认没有把凭据、cookies 或临时文件写入文档。

## 交付前检查清单

- [ ] 已从 `Resources.json` 指向的对应 JSON 索引中选择职责明确的参考图或文本卡片。
- [ ] 每个参考文件真实存在，格式、比例和方向符合任务。
- [ ] `<Picture N>`、`<Video N>`、`<Audio N>` 与实际上传顺序一致。
- [ ] 提示词已声明人物、服装、背景和姿势参考各自负责的内容。
- [ ] 姿势描述包含主体位置、身体朝向、四肢位置、镜头角度、景别和透视。
- [ ] 深度图只承担结构辅助职责，没有被误当作身份或风格参考。
- [ ] 图中不需要的 NPC、文字、Logo、水印和背景元素已明确排除。
- [ ] 已按 [`docs/h3.md`](h3.md) 和项目规则完成模式、音频与提示词字段检查。
