# VideoMake

VideoMake 是一个面向 AIGC 短视频制作的素材与工作流仓库，当前以 **MiniMax H3 + ComfyUI** 为核心，集中管理角色参考图、场景素材、音频、参考视频、提示词、ComfyUI API 工作流和生成结果。

仓库地址：[github.com/LLsetnow/VideoMake](https://github.com/LLsetnow/VideoMake)

## 示例视频

[Bilibili 示例视频](https://space.bilibili.com/39493006/upload/video)

## 当前项目

| 项目 | 内容 |
| --- | --- |
| `projects/千夏_夏_三人短片/` | 按 `1-15秒`、`16-30秒` 拆分的 30 秒短片，包含参考分析、角色合成参考、音频、提示词和工作流 |
| `projects/青春的幻象15秒测试-千夏/` | 千夏 15 秒 MiniMax H3 视频测试及其提示词、工作流和输出 |
| `projects/音乐棚蹦跳-千夏/` | 千夏猫娘音乐棚 10 秒视频，包含提示词、工作流和最终视频 |

## 目录结构

```text
.
├── audio/                 # 通用音频和音频片段
├── background/            # 可复用的背景与场景素材
├── character/             # 角色身份参考图、服装版本、场景图和音色
│   ├── 千夏/
│   ├── 南宫羽/
│   ├── 爱芮/
│   ├── 蕾米埃尔/
│   └── 铃/
├── projects/              # 按任务归档的工作流、提示词和生成结果
├── videoRef/              # 风格、动作和镜头参考视频
├── AGENTS.md              # 项目协作与素材管理约定
└── README.md
```

单个视频项目建议保持以下结构：

```text
projects/<项目名>/
├── <项目名>_workflow_api.json
├── <项目名>_prompt.txt
└── output/
```

较长的视频按时间段拆分，每个片段独立保存自己的工作流、提示词、音频和输出，最后再按时间顺序剪辑拼接。

## 快速开始

### 1. 获取仓库

```bash
git clone https://github.com/LLsetnow/VideoMake.git
cd VideoMake
```

### 2. 准备生成环境

运行工作流前，需要在本地或 Aigate 实例中准备：

- ComfyUI；
- `comfyui-minimax-h3-audio-T8` 自定义节点；
- 工作流所需的 MiniMax H3 模型、VAE、CLIP 和 LoRA 权重；
- 当前任务引用的角色图、场景图、参考视频和音频；
- 可访问 ComfyUI API 的运行环境。

自定义节点仓库：<https://github.com/T8mars/comfyui-minimax-h3-audio-T8>

模型权重不存放在本仓库中。请根据当前 ComfyUI、自定义节点和模型版本检查工作流兼容性，不要直接假设旧工作流仍适用于新版本。

### 3. 校验工作流 JSON

提交或运行工作流前，可以先检查 JSON 格式：

```bash
python -m json.tool \
  projects/音乐棚蹦跳-千夏/Minimax双时钟图生视频V1_qianxia_catgirl_audio10s_api.json \
  >/dev/null
```

其他项目的 `*_workflow_api.json` 也可以使用相同方式校验。提交到 Aigate 前，还需要确认输入素材已经上传或映射到实例可访问的路径。

### 4. 运行与复核

根据使用的环境，通过 ComfyUI API 或来自 [OPC](https://github.com/LLsetnow/OPC) 仓库的 `opc aigate` 提交工作流。具体 CLI 参数以当前环境的帮助信息为准：

```bash
opc aigate --help
```

`opc aigate` 的 CLI 实现和云扉 AIGate 实例管理逻辑不在本仓库中维护，详见 [LLsetnow/OPC](https://github.com/LLsetnow/OPC)。如需安装或配置该命令，请按照 OPC 仓库中的说明操作；AIGate Token 等凭据应保存在 OPC 的本地 `.env` 中，不要写入本项目。

生成完成后，检查输出视频的时长、帧率、画幅、角色一致性、音频同步和片段衔接，不要只以任务提交成功作为生成成功的判断。

## 工作流约定

- 单个 MiniMax H3 工作流最长生成 15 秒，但应根据分镜实际需要设置时长，不必强行生成 15 秒。
- 常见视频规格为 24 fps；帧数、画布尺寸和显存占用需要遵循当前节点与模型的约束。
- 提示词使用带时间轴的视听制作简报，明确角色、场景、镜头运动、动作、声音和参考媒体的用途。
- 提示词中的 `<Picture N>`、`<Video N>`、`<Audio N>` 必须与工作流实际接入的媒体顺序一致。
- 角色口播或角色声音优先使用对应角色目录中的音色参考，不要误接其他角色的音频。
- 新任务放在 `projects/` 下，不要把新项目的工作流、提示词和输出散落到根目录。
- 修改已验证的工作流时，优先复制并版本化文件，保留原始结果和可复现信息。

完整的项目文件结构、素材管理、H3 提示词和工作流规则见 [`AGENTS.md`](AGENTS.md)。

## 素材说明

- `character/` 中的图片用于角色身份、服装、姿态或场景参考。
- `background/` 中的图片用于可复用背景或场景条件。
- `audio/` 中的音频用于音乐、音频驱动或参考输入；角色专属音色保存在对应角色目录中。
- `videoRef/` 中的视频仅作为风格、动作、镜头或效果参考，使用前请确认其授权和分发范围。
- `projects/*/output/` 中保存生成结果和中间结果，重跑任务时建议使用新目录或版本化文件名。

本仓库不应提交 API 密钥、登录令牌、实例凭据或其他敏感信息。公开发布包含第三方素材的项目时，请自行确认素材的版权、授权和平台分发限制。

## 复现记录

每个生成项目建议至少保留以下信息：

- 工作流和提示词文件路径；
- 角色、背景、参考视频和音频输入；
- H3 模式、seed、分辨率、时长和帧数；
- Aigate 实例或 ComfyUI 环境信息；
- 最终输出路径，以及是否经过裁切、剪辑或音频替换。
