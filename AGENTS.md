# VideoMake 全局代理规则

本文件是仓库的全局入口。详细规则按职责拆分到 `docs/`，各主要目录再通过同名 `AGENTS.md` 声明本目录的适用范围。

## 项目定位

VideoMake 用于制作 AIGC 视频，当前重点是使用 MiniMax H3 生成带原生音频的视频，并对多个片段进行剪辑与拼接。它不是传统软件工程项目，主要产物是素材、ComfyUI 工作流、提示词和视频输出；处理任务前先理解已有资产和工作流，再做增量修改。

## 项目文件结构与内容说明

```text
.
├── AGENTS.md                 # 全局代理规则和项目文件结构说明
├── audio/                    # 通用音乐、源音频、驱动音频和参考音频
├── background/               # 可复用背景图案和场景背景
├── character/<角色名>/       # 角色身份图、服装/场景参考图和角色音色
├── videoRef/                 # 只用于风格、动作、镜头或效果研究的参考视频
├── projects/<项目名>/        # 每个视频项目的完整工作区
│   ├── README.md             # 可选：项目目标、时间线和复现入口
│   ├── *_prompt.txt          # 可执行的英文 H3 提示词
│   ├── *_prompt_zh.txt       # 可选：对应的完整中文翻译
│   ├── *_workflow_api.json   # ComfyUI API 格式工作流
│   ├── analysis/             # 鼓点、曲风、场景检测和素材分析
│   ├── shots/                # 镜头级提示词、音频、工作流和结果
│   ├── output/               # 当前项目生成的中间结果和最终成品
│   └── qa/                   # ffprobe、接触表、帧数和拼接核验资料
├── workflows/                # 既有/共享的 ComfyUI 工作流模板
├── videoOutput/              # 指向项目 output 成品的统一软链接入口
├── temp/                     # 临时任务提示音等临时文件
└── docs/                     # 拆分后的长期规则、流程和专题知识
```

项目文件的职责边界如下：

| 文件或目录 | 内容和使用方式 |
| --- | --- |
| `AGENTS.md` | 当前目录及其子目录适用的代理规则；不是项目素材或生成结果。 |
| `README.md` | 项目目标、角色/素材清单、时间线、工作流入口和复现说明；不替代规则文件。 |
| `*_prompt.txt` | 提交给 MiniMax H3 的英文可执行提示词；媒体标签必须和 workflow 输入一致。 |
| `*_prompt_zh.txt` | 与英文提示词对应的完整中文翻译，不能混入英文执行提示词。 |
| `*_workflow_api.json` | ComfyUI API 格式工作流，保存节点、参数、输入映射和输出设置。 |
| `analysis/`、`shots/` | 项目分析资料和镜头级生成资料；只属于当前项目，不放共享模板。 |
| `output/` | 当前项目的生成、剪辑中间文件和最终成品；不得覆盖原始资产。 |
| `qa/` | 帧数、音频、场景检测、接触表和拼接结果等验证证据。 |
| `workflows/` | 跨项目复用的模板和历史共享工作流；新项目应复制后再修改。 |
| `videoOutput/` | 只放指向 `projects/<项目名>/output/` 的软链接，不存放第二份视频实体。 |
| `temp/` | 只存放临时任务提示音等可随时重建的临时文件，不作为项目交付物或长期素材目录。 |
| `docs/` | 详细规则和长期文档；不放视频、音频、图片或 workflow JSON。 |

新项目必须在 `projects/<项目名>/` 中保存自己的工作流、提示词和结果。项目较长时，再按时间序列拆成独立子项目；每个子项目都应能独立提交和复现。角色、背景、通用音频和参考视频等可复用资产分别归档到对应资产目录，不为每个项目重复复制。

## 阅读规则

- 处理某个目录时，先阅读从仓库根目录到目标文件最近的 `AGENTS.md`，再阅读本文件列出的相关 `docs/` 文档。
- 目录级规则只补充本文件，不得放宽全局的安全、资产保护、H3 路由和复现要求。
- 新项目的工作流、提示词和结果必须放在 `projects/<项目名>/`，不得新增到根目录的 `workflows/` 或 `output/`。
- 不要把 API 密钥、登录令牌、实例凭据、cookies、SSH 密钥或其他敏感信息写入仓库、提示词或 workflow JSON。
- 保留用户已有资源和未相关改动；重跑或改参数时使用新目录或版本名，不覆盖已验证结果。

## 规则索引

| 主题 | 详细文档 |
| --- | --- |
| 项目结构、时长、鼓点卡点、标准流程 | [`docs/project-workflow.md`](docs/project-workflow.md) |
| 角色、背景、音频、参考视频和下载/分析 | [`docs/media-assets.md`](docs/media-assets.md) |
| H3 Skill、提示词和 T8 节点 | [`docs/h3.md`](docs/h3.md) |
| AIGate 实例、提交、队列和生命周期 | [`docs/aigate.md`](docs/aigate.md) |
| 剪辑、核验、交付和复现 | [`docs/editing-delivery.md`](docs/editing-delivery.md) |
| 文档目录约定 | [`docs/AGENTS.md`](docs/AGENTS.md) |

## 主要目录分工

- `audio/AGENTS.md`：通用音频、锁定源音频和音乐分析。
- `background/AGENTS.md`：可复用背景和栅格参考图。
- `character/AGENTS.md`：角色身份图、服装/场景图和角色音色。
- `projects/AGENTS.md`：项目目录、提示词、工作流生成、AIGate、剪辑和结果归档。
- `videoRef/AGENTS.md`：仅用于研究的参考视频及其下载归档。
- `workflows/AGENTS.md`：共享 ComfyUI 模板和 JSON 校验。
- `videoOutput/AGENTS.md`：最终成品软链接的统一入口。
- `docs/AGENTS.md`：说明文档自身的组织规则。

## 任务完成语音提示

- 如需用语音提示用户当前任务已完成，可以使用 OPC TTS 合成简短提示音：`mkdir -p temp && opc tts "当前任务已完成" -o temp/task-complete.wav`。
- 合成的音频必须放在仓库根目录的 `temp/` 下；它是临时文件，不得替代项目输出或写入长期素材目录。
- 合成成功后可以使用 `afplay temp/task-complete.wav` 播放。使用前台命令，待命令返回后再将播放视为完成；`afplay` 使用 macOS 当前默认音频输出设备，并应遵守用户对播放设备的明确要求。

## H3 全局约束

- 所有 MiniMax H3 任务必须先进入项目内的 `minimax-h3-creative-director`，再选择唯一的下游 Skill；不要在本项目工作流中用全局 `h3-prompt-writing` 替代它。
- 纯文字使用 `minimax-h3-text-video-prompt`；涉及人物、物品、场景、风格、动作、镜头或音频参考使用 `minimax-h3-reference-video-prompt`；只有明确声明为无其他参考职责的纯首帧/首尾帧边界任务才使用 keyframe 专项；已有提示词审查使用 reviewer。
- 明确的多镜头、分镜、切镜或蒙太奇任务必须先完成镜头数量和逐镜确认；只有 `multishot_plan_status: confirmed` 才能格式化最终提示词。
- H3 生成边界和最终剪辑边界不是同一概念。生成段是素材容器，提示词中的 `[Shot]` 时间戳只是意图；最终切点必须经场景检测、接触表或帧级检查确认。
- 默认工作流分辨率为 `0.9 MP`/`720p`，除非任务明确覆盖；源音频锁定任务使用 `audio_mode: lock_source`，最终输出按实际帧率和音频核验。

## 交付前检查

完成任务前至少检查：文件路径和链接、JSON 可解析性、提示词与实际输入媒体标签、视频帧率/时长/音轨，以及 `git diff --stat` 和 `git status --short`。不要因本次任务顺手清理其他用户改动。
