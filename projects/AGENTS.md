# projects 目录规则

本目录保存每个视频项目的 workflow_api、提示词、素材分析和输出。

- 每个新任务先建立 `projects/<项目名>/`；短视频直接放 workflow、prompt 和 `output/`，长视频按时间序列建立独立子项目。
- 单个本地工作流为 2–15 秒；不要机械填满 15 秒，也不要拆出低于 2 秒的尾段。工作流段落优先落在已确认的自然切点或鼓点切点。
- 先完成故事/镜头脚本和媒体用途，再进入 `minimax-h3-creative-director`；明确多镜头任务必须确认逐镜计划后再格式化提示词。
- workflow 中的 Picture/Video/Audio 标签必须与实际独立输入节点一致；默认 `0.9 MP`/`720p`，除非任务明确覆盖。
- 使用 AIGate 前先查询并优先创建 48G 4090/4090D 实例；不使用 5090/24G，不因已有实例而自动复用。生成后检查实际文件，不以提交成功为完成。
- 最终成品留在项目 `output/`，再在 `videoOutput/` 建立并验证软链接；确认输出已下载和核验后才停止/释放实例。

详细流程：[`docs/project-workflow.md`](../docs/project-workflow.md)、[`docs/h3.md`](../docs/h3.md)、[`docs/aigate.md`](../docs/aigate.md)、[`docs/editing-delivery.md`](../docs/editing-delivery.md)。
