# VideoMake 项目说明

## 项目定位

本项目用于制作 AIGC 内容，当前重点是使用 MiniMax H3 生成带原生音频的 AI 视频，并对多个片段进行剪辑与拼接。

本项目不是传统的软件工程项目，当前没有应用源码、构建脚本或自动化测试；主要产物是素材、ComfyUI 工作流、提示词和视频输出。处理任务时，应先理解现有资产和工作流，再进行增量修改。

本项目使用项目级 Claude Skill，位置为 `.claude/skills/`。MiniMax H3 工作流依赖本项目内的 `minimax-h3-prompt` 及其下游 Skill，不依赖 `h3-prompt-writing`。

## Claude 项目级 Skill 调用约定

- 所有 MiniMax H3 任务必须先进入 `minimax-h3-creative-director`，不要直接跳过总导演调用最终格式化 Skill。
- `minimax-h3-creative-director` 必须先读取同级的 `../minimax-h3-prompt/SKILL.md`，并按任务读取其 `reference/VIDEO_PROMPT_WRITING_GUIDE_base_en.md` 或 `reference/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`。这些文件是本项目的提示词格式依据。
- 不要在本项目 H3 工作流中调用 `h3-prompt-writing`；如果全局或其他 Skill 提到它，以本项目内的 `minimax-h3-prompt` 为准。
- 总导演完成方向确认后，只选择一个最终 Skill：纯文字使用 `minimax-h3-text-video-prompt`；含人物、物品、场景、风格、动作、镜头或音频参考时使用 `minimax-h3-reference-video-prompt`；明确的纯首帧/首尾帧边界任务才使用 `minimax-h3-keyframe-video-prompt`；审查已有提示词使用 `minimax-h3-prompt-reviewer`。
- 用户明确要求多镜头、分镜、切镜或蒙太奇时，先进入 `minimax-h3-multishot-planner`；视频达到 10 秒且用户未说明单镜头/多镜头时，先询问是否启用多镜头。规划器必须先确认镜头数量，再逐镜确认，只有得到 `multishot_plan_status: confirmed` 后才能生成最终提示词。
- 需要提问时，优先使用 Claude 的结构化提问工具 `AskUserQuestion`；严格的是非题使用 2 个选项，其他选择题至少提供 5 个有实际差异的选项，并把推荐项放在第一位。若当前环境没有结构化提问工具，再使用简洁的自然语言提问。
- 最终交付应包含可直接提交的英文 H3 提示词和完整中文翻译；英文提示词中的描述性字段保持英文，只有对白/歌词和画面中实际出现的文字保留原文。

## 项目结构

```text
.
├── audio/                         # 可直接使用或作为驱动/参考的音频
├── background/                    # 背景图案、场景背景图
├── character/                     # 角色参考资产，按角色分目录
│   ├── 千夏/
│   │   └── 场景图/                # 角色相关的场景图
│   ├── 南宫羽/
│   ├── 爱芮/
│   ├── 蕾米埃尔/
│   └── 铃/
├── videoRef/                      # 参考视频，用于研究风格、动作或工作流效果
├── projects/                      # 每个视频生成项目的工作流、提示词和输出
├── workflows/                     # 既有/共享的 ComfyUI workflow_api JSON 与提示词
└── output/                        # 既有/历史的 Aigate/ComfyUI 生成结果
```

当前已有的典型文件包括：

- `workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json`：MiniMax H3 图生视频 API 工作流。
- `workflows/minimax_h3_qianxia_audio15s_prompt.txt`：该工作流对应的 H3 提示词。
- `output/aigate-minimax-h3-qianxia-15s/`：一次 Aigate 生成任务的音频、精确时长和最终视频结果。

实际目录可能随着新角色、新场景和新任务增加而变化。不要把当前示例文件名当成固定接口；新增任务应使用清晰、可追溯的任务名建立对应的工作流和输出目录。

## 项目目录与文件管理规则

每次开始新的视频生成项目时，必须先在 `projects/` 下创建一个总文件夹。总文件夹名称由项目内容决定，应能让人直接看出项目的角色、主题或场景，例如：

```text
projects/千夏_青春的幻象_音乐工作室/
```

对于单个短视频项目，目录结构如下：

```text
projects/<项目名>/
├── <项目名>_workflow_api.json  # 本项目提交用的 ComfyUI workflow_api
├── <项目名>_prompt.txt         # 本项目使用的 MiniMax H3 提示词
└── output/                     # 本项目生成的所有结果
```

如果项目时长较长，需要拆成多个视频子项目（例如 1 分钟拆成 4 个 15 秒片段），则在总文件夹下按子项目的时间序列创建文件夹。每个子项目文件夹都必须独立保存自己的工作流、提示词和输出：

```text
projects/<项目名>/
├── 1-15秒/
│   ├── <项目名>_1-15秒_workflow_api.json
│   ├── <项目名>_1-15秒_prompt.txt
│   └── output/
├── 16-30秒/
│   ├── <项目名>_16-30秒_workflow_api.json
│   ├── <项目名>_16-30秒_prompt.txt
│   └── output/
├── 31-45秒/
│   ├── <项目名>_31-45秒_workflow_api.json
│   ├── <项目名>_31-45秒_prompt.txt
│   └── output/
└── 46-60秒/
    ├── <项目名>_46-60秒_workflow_api.json
    ├── <项目名>_46-60秒_prompt.txt
    └── output/
```

长项目的每个子项目应视为可独立提交和复现的生成任务，同时在提示词和文件名中注明它在整条视频时间线中的位置。最终剪辑时，再按时间序列合并各子项目的 `output/` 结果。

单次本地工作流提交的视频时长范围为 2–15 秒：最短 2 秒，最长 15 秒，但 15 秒不是固定要求。每个工作流的实际时长应根据分镜中的时间序列、动作节奏、对白和镜头切换决定；如果一个分镜只需要 6 秒，就生成 6 秒，不要为了凑满 15 秒而延长或填充内容。拆分长视频时，要避免产生不足 2 秒的子项目；例如 16 秒视频不要拆成 `15+1`，应根据分镜和剪辑节奏拆成 `8+8` 或其他均衡且不低于 2 秒的组合。若改用官方在线/API 运行时，遵循当前 H3 Skill 的 4–15 秒、24 FPS 和 7000 字符提示词限制；若本地 ComfyUI 工作流有更窄的限制，以本地运行时为准。

新项目不得把工作流、提示词和结果散落到根目录的 `workflows/` 或 `output/` 中；这两个目录保留用于已有示例、共享模板或历史结果。角色、背景和通用音频等源资产仍放在各自的资产目录中，不需要为了每个项目重复复制。

## 资产使用约定

- `audio/` 存放通用音频；角色专属音色或角色语音可以放在对应的 `character/<角色名>/` 目录中。
- `background/` 存放可复用的背景图案或场景背景。需要角色与场景绑定时，也可以放到该角色的 `场景图/` 子目录。
- `character/<角色名>/` 存放角色身份参考图，以及该角色的音色参考文件，例如全身三视图、正面图、面部图、服装版本、姿态/场景参考图和角色音色音频。
- 如果视频包含人物口播或角色台词，必须优先从对应角色目录中选择并接入角色音色参考音频。例如，千夏的音色参考文件为 `/Users/apple/Documents/VideoMake/character/千夏/千夏音色6秒.mp3`。不要把其他角色的音色文件误接入当前角色。
- `videoRef/` 中的视频只作为风格、动作、镜头或效果参考。除非任务明确要求，不要把参考视频误当作最终素材或自动提交到工作流。
- `output/` 中的文件是生成结果和中间结果，不应覆盖原始资产。每次重跑或改参数时，优先新建任务目录或使用带版本号的文件名。
- 使用已有资产前，先确认文件真实存在、格式可被 ComfyUI/Aigate 读取，并确认它在工作流中的角色：主体身份、首帧、尾帧、背景、动作参考或音频参考。
- 不要把 API 密钥、登录令牌、实例凭据或其他敏感信息写入本项目、提示词或 workflow JSON。

建议的新增命名方式：

```text
<角色>_<场景>_<用途>_<比例或时长>_<版本>.<扩展名>
```

例如：`千夏_音乐工作室_首帧_9x16_v2.png`、`千夏_片段01_15s_v3.mp4`。

## 标准工作流程

### 1. 初始化项目目录

根据项目内容在 `projects/` 下创建项目总文件夹。先判断项目是单个短视频还是需要按时间段拆分的长视频：

- 短视频直接使用 `projects/<项目名>/`，在其中保存 workflow_api JSON、提示词 TXT 和 `output/`；
- 长视频先创建 `projects/<项目名>/`，再按 `1-15秒`、`16-30秒` 等时间序列创建子项目文件夹，每个子项目包含自己的 workflow_api JSON、提示词 TXT 和 `output/`。

后续所有本次项目的工作流、提示词和生成结果都必须放在对应的项目目录中。

### 2. 确定故事剧本

先确定故事目标、角色、场景、片段数量、每个片段时长、画幅比例、对白/歌词、音乐和最终剪辑顺序。每个分镜应根据其时间序列确定实际时长，单个工作流必须为 2–15 秒，但不要求每个工作流都生成 15 秒。优先把长故事拆成可独立生成的短镜头，避免一次工作流承担过多动作和场景变化；拆分时应让各子项目时长合理均衡，不能出现 2 秒以下的子项目。

### 3. 生成脚本内容

把剧本拆成镜头级内容，至少明确：

- 镜头中的角色和角色身份参考；
- 场景、背景和画面构图；
- 可观察的动作变化及其时间顺序；
- 镜头运动、景别、光线和画面风格；
- 对白、歌词、环境声、角色声音和非叙事音乐；
- 首帧/尾帧/参考图/参考视频/音频各自的用途。

### 4. 使用 `imagegen` skill 生成配图

使用项目可用的 `imagegen` skill 根据脚本生成每个镜头所需的静态图。默认使用内置 image generation/editing 流程；这些图片既是脚本配图，也可能是后续视频生成的参考图，因此应优先保证角色身份、服装、构图、场景和画幅比例稳定。

#### 人物卡片生图规则

生成人物卡片或角色参考三视图时，使用内置 `imagegen` 生成模式，并固定采用整体 `1:1` 方形画布：

- 左侧约 `2/3` 画面：角色正面半身；
- 右上区域：角色侧面全身；
- 右下区域：角色背面全身。

三个人物视图必须保持同一角色的发型、服装、配色和身份特征一致。生成完成后，将可复用的人物卡片归档到 `character/<角色名>/`，后续作为角色参考图使用。普通分镜配图仍按脚本需求使用 `imagegen`。

生成后按用途归档：

- 可复用的角色身份图放入 `character/<角色名>/`；
- 可复用的背景或场景图放入 `background/`，或放入对应角色的 `场景图/`；
- 仅属于一次任务的临时首帧/尾帧可以与任务工作流或输出目录一起管理。

不要只凭文件名猜测图片用途；在工作流中接入前，确认图片实际内容和方向比例。

### 5. 通过 H3 Skill 工作流生成提示词

在提交工作流之前，必须先调用 `minimax-h3-creative-director`，由它读取本项目内的 `minimax-h3-prompt`，再根据已确定的剧本、镜头拆分、视频模式和参考素材路由到唯一的最终提示词 Skill。不得用 `h3-prompt-writing` 替代这一流程。

生成时应明确：

- 使用的模式：`T2VA`、`I2VA`、`FL2VA`、`L2VA` 或 Full-reference/`Ref2VA`；
- 角色、场景、首帧/尾帧、参考视频和音频的标签及用途；
- 镜头时间轴、动作、镜头运动、光线和画面变化；
- 对白/歌词、环境声、角色声音和非叙事音乐；
- 提示词中的媒体标签与即将接入工作流的实际输入保持一致。

将生成并确认后的提示词保存到当前项目目录或对应的子项目目录，建议与 API 工作流使用相同任务名，例如：

```text
projects/<项目名>/<项目名>_prompt.txt
projects/<项目名>/<项目名>_workflow_api.json
```

生成后先按 `minimax-h3-prompt` 的质量检查清单以及最终 Skill 的格式要求复核模式、镜头时间戳、说话人 ID、参考标签和声音字段，再进入下一步。

### 6. 修改并提交 ComfyUI 工作流

1. 默认以 `/Users/apple/Documents/VideoMake/workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json` 作为视频工作流参考，复制到当前项目目录或子项目目录后再修改，不要直接修改默认模板。
2. 根据项目需求灵活增删和修改输入节点：
   - 有多个参考图时，为每张参考图增加对应的 `Load Image` 节点，并分别接入工作流；
   - 需要参考音频时，增加 `Load Audio` 节点，并接入对应音频；人物口播时优先接入角色目录中的音色参考文件；
   - 需要参考视频时，增加 `VHS Load Video` 节点，并确认视频及其音频是否都需要作为参考；
   - 输入节点的数量、连接关系和参考媒体类型必须以当前项目要求为准，不要机械沿用模板中的输入数量。
3. 修改输入参考内容：角色图、背景图、首帧/尾帧、参考视频和音频路径或上传对象。若视频包含人物口播，还要将对应角色目录中的音色参考文件接入工作流；例如千夏使用 `character/千夏/千夏音色6秒.mp3`。
4. 切忌将多个角色的参考图融合为一张图作为单参考图。多个角色必须保留为多个独立参考图，并通过独立的 `Load Image` 节点和正确的 `<Picture N>`/角色标签表达，以避免角色身份、服装和动作参考混淆。
5. 将第 5 步生成的提示词填入对应文本节点，并确保提示词中的 `<Picture N>`、`<Video N>`、`<Audio N>` 与实际接入的媒体编号一致。
6. 修改 `MiniMax H3 Audio Conditioning (T8)` 的任务类型、参考内容、音频模式及其他与当前任务有关的配置。
7. 检查分辨率、时长、帧数、seed、采样步数、输出文件名和保存节点。确认单个工作流时长在 2–15 秒之间，并且实际时长与分镜时间序列、动作节奏和台词长度匹配；不要默认全部使用 15 秒，也不要将长视频拆出不足 2 秒的尾段。
8. 用 JSON 校验工具检查文件格式，再提交到 Aigate。

本地校验示例：

```bash
python -m json.tool projects/<项目名>/<项目名>_workflow_api.json >/dev/null
```

### 7. 通过 `opc aigate` 创建实例并生成视频

通过 `opc aigate` CLI 在 Aigate 平台创建实例。默认 GPU 选择 `4090-48G`，除非任务明确要求其他配置。

命令的具体子命令和参数以当前 CLI 的帮助信息为准，不要凭记忆猜测参数名：

```bash
opc aigate --help
```

#### `opc aigate` 常用用法

`opc aigate` 负责查询 Aigate 资源、启动/创建云端 ComfyUI 实例、提交 `workflow_api` 工作流，并将生成结果下载到本地。认证默认读取环境变量 `AIGATE_TOKEN`，也可以通过 `--token` 或 `--env-file` 指定；Token 不得写入项目文件。

查询资源和本地工作流：

```bash
opc aigate --status
opc aigate --gpus --area "<区域>"
opc aigate --images
opc aigate --community-images --area "<区域>" --sku "4090-48G"
opc aigate --workflows --workflow-dir "projects/<项目名>"
```

启动已有实例：

```bash
opc aigate --start --instance "<INSTANCE_ID>"
```

创建并启动新实例时，必须同时使用 `--start` 和 `--create`，并明确提供 GPU SKU、区域和镜像。新项目默认使用 `4090-48G`，但应先通过 `--gpus` 确认该区域当前可用：

```bash
opc aigate --start --create \
  --sku "4090-48G" \
  --area "<区域>" \
  --image-id "<镜像ID>" \
  --image-type 2
```

其中 `--image-type 2` 表示社区镜像，个人镜像使用 `3`。创建实例可能产生云资源费用；不要因为一次工作流提交而误加 `--create`。

提交工作流并下载结果：

```bash
opc aigate --start --instance "<INSTANCE_ID>" --run \
  --workflow "projects/<项目名>/<项目名>_workflow_api.json" \
  --output "projects/<项目名>/output" \
  --timeout 1200
```

`--workflow`/`-w` 必须指向 ComfyUI API 格式 JSON；`--output`/`-o` 是结果下载到本机的目录。`--prompt`/`-p`、`--seed`/`-s`、`--output-prefix` 可以临时覆盖工作流中的提示词、seed 和输出前缀；如果提示词已经写入 workflow JSON，则不需要重复传入 `--prompt`。

输入媒体可以由 CLI 上传并自动写入工作流中检测到的节点：

```bash
opc aigate --start --instance "<INSTANCE_ID>" --run \
  -w "projects/<项目名>/<项目名>_workflow_api.json" \
  --image "<输入图片路径>" \
  --reference-image "<角色参考图路径>" \
  --audio "<参考音频路径>" \
  --video "<参考视频路径>" \
  -o "projects/<项目名>/output"
```

如果工作流中存在多个同类输入节点，或 CLI 自动检测到了错误的节点，使用节点 ID 参数明确指定：`--load-image-node`、`--reference-image-node`、`--audio-node`、`--video-node`、`--prompt-node`、`--seed-node` 和 `--video-output-node`。当前 CLI 的 `--image`、`--reference-image`、`--audio`、`--video` 参数每次调用各对应一个输入；多个参考媒体应在 workflow JSON 中预先配置多个独立节点，并按实际支持的上传方式分别处理，不能通过重复覆盖同一个节点解决，更不能把多个角色合并成一张参考图。

ComfyUI 服务器自身维护工作队列。每次 `--run` 会提交一个任务并等待该任务结果；多个任务可以继续提交到同一实例的队列中，长视频子项目按 `1-15秒`、`16-30秒` 等顺序提交即可。当前单次 `opc aigate --run` 只接收一个 workflow JSON；如果要提前把多个任务放入队列，应使用多个提交调用或其他支持批量提交的方式，不必等待前一个视频生成完成。批量提交时要确保每个任务使用独立的 `output/` 目录或输出前缀，并保存各自的任务记录，便于按时间序列整理结果。

停止或释放实例：

```bash
opc aigate --stop --instance "<INSTANCE_ID>"
opc aigate --release --instance "<INSTANCE_ID>"
```

`--stop` 用于暂时关闭实例；`--release` 会释放并删除实例资源，确认结果已下载和归档后才能使用。

一般顺序如下：

1. 创建 Aigate 实例，选择 `4090-48G`；
2. 确认实例中已安装所需的 ComfyUI 自定义节点、模型、VAE、CLIP 和 LoRA；
3. 提交当前项目目录或子项目目录中的 `*_workflow_api.json` ComfyUI API 工作流；
4. ComfyUI 服务器自带工作队列，可以一次性直接提交多个任务。长视频拆分出的多个时间段子项目可以按时间顺序批量加入队列，不需要等待前一个任务完成后再手动提交下一个任务；
5. 确认每个排队任务所引用的输入素材已上传、挂载或改写为 Aigate 实例可访问的路径，并确认不同任务使用独立的输出文件名和 `output/` 目录，避免结果互相覆盖；
6. 将生成结果保存或整理到当前项目目录下对应的 `output/`，并记录队列顺序、任务/实例 ID、工作流文件、提示词、seed、分辨率、帧数和输出位置，便于复现；
7. 等待队列中的任务完成，逐项检查日志和输出文件，不要只以任务提交成功判断视频生成成功。

### 8. 视频剪辑与拼接

生成完成后，将当前项目目录或各子项目目录下的 `output/` 中的镜头按时间序列收集到剪辑流程中，完成裁切、排序、转场、音频对齐、字幕/音效和最终导出。重点检查：

- 每段视频实际时长是否符合脚本；
- 画面帧率、画幅和方向是否统一；
- 角色声音、背景音乐和环境音是否错位或重复；
- 片段衔接处是否出现突兀的首尾帧、音频断裂或音量跳变；
- 最终视频是否包含正确的音轨，并能在目标播放器中正常播放。

最终成品视频必须保留在当前项目的 `output/` 目录中，并在 `/Users/apple/Documents/VideoMake/videoOutput/` 下创建一个指向该成品文件的软链接，便于统一访问和后续使用。软链接示例：

```bash
mkdir -p /Users/apple/Documents/VideoMake/videoOutput
ln -s "/绝对路径/项目目录/output/最终成品.mp4" \
  "/Users/apple/Documents/VideoMake/videoOutput/最终成品.mp4"
```

创建前确认 `videoOutput/` 中不存在同名文件或软链接；创建后用以下命令确认链接目标正确：

```bash
readlink /Users/apple/Documents/VideoMake/videoOutput/最终成品.mp4
```

## MiniMax H3 提示词规范

编写或改写 H3 提示词时，必须通过 `minimax-h3-creative-director` 进入本项目 Skill 工作流，并以 `minimax-h3-prompt` 作为格式权威。H3 提示词应写成带时间轴的视听制作简报，而不是单纯的静态图片描述。

- 除对白/歌词 `<d>...</d>` 内的原文，以及画面中实际出现的文字外，提示词字段使用英文。
- 先选择模式：`T2VA`（纯文本）、`I2VA`（首帧图生视频）、`FL2VA`（首尾帧）、`L2VA`（尾帧）或 Full-reference/`Ref2VA`。
- 基础模式使用 `integrated_multimodal_description`、`overall_soundscape` 和 `non_diegetic_music` 三个核心字段；I2VA/FL2VA/L2VA 要在第一行写清参考图与目标视频时间点的对齐关系。
- Full-reference 模式按固定顺序使用 `subject_definitions`、`summary`、`retention_analysis`、`detailed_description`、`overall_soundscape`、`non_diegetic_music` 六个字段。
- `[Shot 1]` 不带时间戳；后续镜头使用严格递增的时间戳，且时间必须落在目标视频时长内。
- 镜头运动写在镜头描述中，包含运动类型，必要时补充幅度和速度；不要把抽象情绪当作唯一指令，要写成可观察、可听见的动作和变化。
- 对白使用稳定的 `(S1)`、`(S2)` 说话人 ID；对白原文只放进 `<d>[Language] ...</d>`，不要在其中翻译或添加解释。
- 环境声和身体/人声的非语言声音写入 `overall_soundscape`；角色能听到的现场音乐写入镜头描述；观众专属的配乐写入 `non_diegetic_music`。
- 同一参考标签在所有字段中保持同一含义。严格模式下，不要在提示词中引用未接入工作流的媒体标签。
- 人物口播时，将角色音色参考音频作为对应的 `<Audio N>` 输入，并在提示词中把该音频与稳定的说话人 ID（如 `(S1)`）对应起来；确认音色文件、台词角色和实际音频输入一致。
- 最终交付同时保存英文可执行提示词和完整中文翻译；中文翻译不得混入英文执行提示词代码块，也不得改写对白、歌词或画面文字的原文。

## `comfyui-minimax-h3-audio-T8` 自定义节点

上游仓库：<https://github.com/T8mars/comfyui-minimax-h3-audio-T8>

该节点包主要用于 MiniMax H3 的音画条件、音频控制、双时钟采样和参考图像条件。使用前以仓库 README、示例 API JSON 和当前安装版本为准；节点版本或 ComfyUI 版本变化时，不要假设旧工作流的控件和默认值仍然完全相同。

安装位置通常为 ComfyUI 的 `custom_nodes/minimax-h3-audio-T8/`，安装或更新后需要重启 ComfyUI。模型权重仍使用 ComfyUI 的标准模型目录，不要复制进本项目。

### 重点节点：`MiniMax H3 Audio Conditioning (T8)`

修改现有工作流时重点检查：

- `task_type`：根据任务选择 `T2VA`、`I2VA`、`FL2VA`、`L2VA`、`Ref2VA`/Full-reference 或 `Hybrid`；
- 输入参考内容：确认每张 Picture、每个 Video 和每条 Audio 的实际输入及顺序；
- 音频模式：根据需求选择锁定源音频、重绘源音频、仅作参考或原生生成；
- 提示词中的参考标签：必须与节点生成的媒体映射一致；
- 时长、帧数、画布尺寸及输出音频：必要时同时检查 `Duration Planner`、`Audio Window`、`AV Decode` 和 `Output Trim` 等配套节点。

上游节点的关键约束包括：固定 24fps、帧数按 `17n+5` 对齐、画布宽高使用 32 的倍数、原生 H3 通常为 batch size 1；引用数量通常不超过 9 张 Picture、3 个 Video 和 3 个独立 Audio。生成前应让 Preflight 或等价检查暴露时长、尺寸、显存和输入契约问题。

### 双时钟采样注意事项

如果任务使用 `MiniMax H3 Dual-Clock Sampler (T8)`，推荐先以工作流已验证的稳定配置为基线：4 步、`shift_video=12`、`shift_audio=3`、`dual_clock_euler`、`native_flow`。不要在该节点之后重复叠加 Sigma Shift、`KSamplerSelect` 或 `BasicScheduler`；需要改变采样器或调度器时，优先使用节点自身提供的配置，并参考上游示例验证结果。

## 任务交付与复现要求

每次生成至少保留以下信息：

- 故事/镜头编号和最终用途；
- 使用的角色、背景、参考图、参考视频和音频文件；
- workflow_api JSON 路径；
- H3 模式、提示词文件路径和主要节点配置；
- Aigate 实例信息、GPU 类型、seed、分辨率、时长和帧数；
- 生成结果路径及是否经过剪辑、裁切或音频替换；
- 最终成品在项目 `output/` 中的真实路径，以及 `/Users/apple/Documents/VideoMake/videoOutput/` 中对应的软链接路径。

修改时优先复制并版本化工作流和提示词，不直接覆盖已经验证过的版本。若生成失败，先区分是输入路径、节点/模型缺失、JSON/API 参数、显存/时长约束，还是提示词与参考内容不一致，再针对原因修改。
