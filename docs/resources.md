# `ref/Resources.md` 资产库索引与使用方法

## 文档定位

[`ref/Resources.md`](../ref/Resources.md) 是 VideoMake 的可复用视频资产库索引，不是生成结果目录，也不是某一个项目的工作流。它集中记录参考图的文件路径、图像内容说明和适用用途，方便在制作 MiniMax H3 视频前快速选择人物、服装、背景和姿势参考。

索引中的图片实体保存在 `ref/` 下的对应资产目录；`Resources.md` 负责说明“这张图是什么、应该约束什么、不能误用什么”。使用时必须同时确认索引描述和实际文件，不能只根据文件名猜用途。

## 资产分类

| 分类 | 目录 | 主要用途 | 使用时锁定的内容 |
| --- | --- | --- | --- |
| `character` | `ref/character/` | 角色身份、脸部、发型、服装、场景或音色参考 | 按条目用途选择；身份图主要锁定脸部、发型和角色识别特征 |
| `clothes` | `ref/clothes/` | 独立服装或搭配参考 | 服装款式、材质、颜色、结构和装饰，不自动替换角色身份 |
| `background` | `ref/background/` | 场景、建筑、舞台和环境参考 | 空间结构、陈设、色彩、时间和光线；不自动引入图中的人物或文字 |
| `pose` | `ref/pose/` | 姿势、构图、人物相对位置和镜头角度参考 | 身体朝向、四肢位置、主体位置、景别、视角和透视关系 |

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
- `ref/pose/video/`：部分条目的动作示例视频，用于研究动作变化或节奏。

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

### 2. 在 `Resources.md` 中定位条目

使用角色名、服装名、场景名或姿势关键词搜索。条目中的图片链接、描述和“用途”说明应一起阅读：

- 图片链接确认实际资产文件；
- `[人物描述]` 或 `[English Translation]` 可用于构造身份文字约束；
- `[AI识图]`、`场景描述` 等内容用于理解构图、色彩和用途；
- “用途”字段决定这张图应当作为身份、服装、背景、姿势还是其他参考。

### 3. 确认文件真实存在和格式

索引路径以 `ref/Resources.md` 所在位置为基准。接入前至少确认文件存在、格式可读、方向和比例正确：

```bash
test -f "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
sips -g pixelWidth -g pixelHeight "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
file "/Users/apple/Documents/VideoMake/ref/<分类>/<文件名>"
```

视频或音频参考还要用 `ffprobe` 检查时长、帧率、音轨或编码。索引中的相对链接和实际文件不一致时，先修正索引或资产归档，再接入工作流。

### 4. 分配 H3 参考标签

`<Picture N>`、`<Video N>` 和 `<Audio N>` 的编号由当前工作流的实际上传顺序决定，不由 `Resources.md` 的章节顺序决定。每次调整上传顺序，都要同步检查：

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

`Resources.md` 在 `pose` 开头提供了可复用的结构模板。其核心含义是：把姿势图绑定到一个明确的参考主体，再在 `detailed_description` 中说明动作起始状态和镜头位置：

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

### `magapixels` 备注怎么用

部分姿态条目记录了 `magapixels = 0.4` 或 `1`。这是过去测试中较容易得到可辨识构图的分辨率起点，不是所有工作流都通用的固定值，也不保证一次生成成功。

实际工作流通常使用 `megapixels` 字段。使用索引备注时：

1. 先确认当前工作流的 `ResolutionSelector` 或等效节点实际字段名；
2. 把条目中的数值作为待验证的起始配置，不要无条件覆盖项目已有参数；
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
2. 在 `Resources.md` 增加一个清晰的标题、图片链接和用途说明。
3. 图片路径使用相对于 `ref/Resources.md` 的相对路径，例如 `character/角色名/文件.png`。
4. 姿势条目如果有深度图，应同时登记彩色图和 `_depth` 图，并说明两者的职责。
5. 新增人物描述时，区分通用五官、发型、服装和配饰；不要让通用五官描述隐含某一套衣服。
6. 生成或迁移资产后确认文件真实存在、格式可读、链接可打开；不要覆盖已验证资产。
7. 修改索引前后检查 `git diff --check`，并在提交前确认没有把凭据、cookies 或临时文件写入文档。

## 交付前检查清单

- [ ] 已从 `Resources.md` 选择了职责明确的参考图。
- [ ] 每个参考文件真实存在，格式、比例和方向符合任务。
- [ ] `<Picture N>`、`<Video N>`、`<Audio N>` 与实际上传顺序一致。
- [ ] 提示词已声明人物、服装、背景和姿势参考各自负责的内容。
- [ ] 姿势描述包含主体位置、身体朝向、四肢位置、镜头角度、景别和透视。
- [ ] 深度图只承担结构辅助职责，没有被误当作身份或风格参考。
- [ ] 图中不需要的 NPC、文字、Logo、水印和背景元素已明确排除。
- [ ] 已按 [`docs/h3.md`](h3.md) 和项目规则完成模式、音频与提示词字段检查。
