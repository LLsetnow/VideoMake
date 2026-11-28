# VideoMake 说明文档导航

这里是 `docs/` 的阅读入口。根目录 [`AGENTS.md`](../AGENTS.md) 负责项目级协作规则和目录约束；本页负责告诉你在不同制作阶段应该阅读哪份说明文档。

## 推荐阅读路线

```text
项目流程
   ↓
资产索引与资产处理
   ↓
H3 提示词与工作流
   ↓
AIGate 生成
   ↓
剪辑、交付与复现
   ↓
发布
   ↓
清理与归档
```

日常制作可以按下面的顺序阅读：

1. 先看 [`project-workflow.md`](project-workflow.md)，确定项目目录、时间线和标准流程。
2. 需要挑选角色、服装、背景或姿势时看 [`resources.md`](resources.md)，再按需要阅读 [`media-assets.md`](media-assets.md) 的生成、下载和分析流程。
3. 编写 MiniMax H3 提示词或修改 ComfyUI 工作流时看 [`h3.md`](h3.md)。
4. 使用 AIGate 生成时看 [`aigate.md`](aigate.md)；用户说“走 rh 流程”或要求通过 RH Workflow Desk 提交时看 [`h3-workflow-prompt-group-agent.md`](h3-workflow-prompt-group-agent.md)；只有明确要求直接使用 RunningHub CLI/API 时才看 [`runninghub.md`](runninghub.md)。
5. 生成完成后看 [`editing-delivery.md`](editing-delivery.md)，完成剪辑、音频、帧率、输出和复现核验。
6. 需要上传平台时看 [`publishing.md`](publishing.md)；项目结束后按 [`project-cleanup.md`](project-cleanup.md) 评估中间文件。

## 按主题查找

| 主题 | 文档 | 适合什么时候阅读 |
| --- | --- | --- |
| 项目结构与完整流程 | [`project-workflow.md`](project-workflow.md) | 新建项目、拆分长视频、安排时间线和标准制作流程 |
| 资产索引使用 | [`resources.md`](resources.md) | 从 `ref/Resources.json` 总入口读取六类 JSON 资源索引 |
| 资产生成、下载与分析 | [`media-assets.md`](media-assets.md) | 生成参考图、下载媒体、生成深度图、分析音频或参考视频 |
| 姿势参考图归档与索引 | [`pose-assets-workflow.md`](pose-assets-workflow.md) | 生成/匹配深度图与原图、归档到 `ref/pose`、按内容重命名并更新 `ref/pose/pose.json` |
| H3 提示词与 T8 节点 | [`h3.md`](h3.md) | 选择 H3 模式、编写提示词、配置参考标签和检查节点 |
| H3 工作流与 Prompt Group Agent | [`h3-workflow-prompt-group-agent.md`](h3-workflow-prompt-group-agent.md) | 根据视频要求生成 API 工作流、提示词组、sidecar 和索引；“走 rh 流程”通过 RH_CLI 本地 Web App API 提交 |
| AIGate 实例生命周期 | [`aigate.md`](aigate.md) | 查询 GPU、创建实例、提交工作流、下载结果和停止/释放实例 |
| RunningHub CLI 工作流提交 | [`runninghub.md`](runninghub.md) | 仅在用户明确要求直接使用 RunningHub CLI/API 时，通过 `rh workflow run` 上传输入、提交 API 工作流和下载结果 |
| 剪辑、交付与复现 | [`editing-delivery.md`](editing-delivery.md) | 帧级剪辑、音频核验、最终输出、软链接和复现记录 |
| 视频发布 | [`publishing.md`](publishing.md) | 发布到 Bilibili 或小黑盒并核对平台状态 |
| 中间产物清理 | [`project-cleanup.md`](project-cleanup.md) | 项目验收后评估缓存、备用输出和中间文件 |
| 绝区零专题 | [`绝区零.md`](绝区零.md) | 使用千夏、南宫羽、爱芮的人物参考图、音色和风格约束 |
| `docs/` 目录规则 | [`AGENTS.md`](AGENTS.md) | 新增或维护说明文档时确认目录边界和文档规范 |

## 按制作阶段查找

### 资产准备

- 资产入口：[`resources.md`](resources.md)
- 资产目录、图片检查、深度图和媒体分析：[`media-assets.md`](media-assets.md)
- 姿势参考图批处理、重命名和索引：[`pose-assets-workflow.md`](pose-assets-workflow.md)
- 实际资产总入口：[`ref/Resources.json`](../ref/Resources.json)
- 提示词积木：[`ref/prompt/library.json`](../ref/prompt/library.json)
- 角色索引：[`ref/character/character.json`](../ref/character/character.json)
- 服装索引：[`ref/clothes/clothes.json`](../ref/clothes/clothes.json)
- 背景索引：[`ref/background/background.json`](../ref/background/background.json)
- 姿势索引：[`ref/pose/pose.json`](../ref/pose/pose.json)
- 音频索引：[`ref/audio/audio.json`](../ref/audio/audio.json)

### 提示词与生成

- 项目、镜头和分段：[`project-workflow.md`](project-workflow.md)
- H3 Skill、提示词和 T8：[`h3.md`](h3.md)
- H3 工作流与 Prompt Group Agent：[`h3-workflow-prompt-group-agent.md`](h3-workflow-prompt-group-agent.md)
- AIGate、队列和实例：[`aigate.md`](aigate.md)
- RunningHub CLI 工作流提交：[`runninghub.md`](runninghub.md)

### 后期与交付

- 剪辑、帧数、音频和复现：[`editing-delivery.md`](editing-delivery.md)
- 平台发布：[`publishing.md`](publishing.md)
- 清理和归档：[`project-cleanup.md`](project-cleanup.md)

## 入口关系说明

- 从仓库根目录开始：先看 [`README.md`](../README.md)，再进入 [`AGENTS.md`](../AGENTS.md) 或本页。
- 从 `projects/` 开始：先看 [`projects/AGENTS.md`](../projects/AGENTS.md)，再按项目流程进入 `project-workflow.md`、`h3.md`、`aigate.md` 和 `editing-delivery.md`。
- 从 `ref/` 开始：先看对应目录的 `AGENTS.md`，资产通用规则集中在 `media-assets.md`，资产选择和职责映射集中在 `resources.md`。
- 从 `workflows/` 开始：先看 [`workflows/AGENTS.md`](../workflows/AGENTS.md)，再看 `h3.md`、`aigate.md` 和 `project-workflow.md`。

专题文档可以独立阅读，但涉及通用制作流程时，应回到本页或对应的通用文档，不要在专题文档中重复维护整套项目规则。
