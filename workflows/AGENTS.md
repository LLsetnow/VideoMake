# workflows 目录规则

本目录只保存已有/共享的 ComfyUI `workflow_api` 模板和提示词。

- 新项目必须先复制模板到 `projects/<项目名>/`，再修改；不要直接改写已验证的共享模板。
- 修改输入节点时，按实际参考图、视频和音频数量建立独立节点；提示词中的 `<Picture N>`、`<Video N>`、`<Audio N>` 必须与映射一致。
- 重点核对任务类型、音频模式、时长、帧数、画布、seed、采样步数、输出文件名和保存节点；H3/T8 规则见 `docs/h3.md`。
- 提交前运行 `python -m json.tool <workflow.json> >/dev/null`，并确认 workflow 使用的路径和媒体确实存在。
- 不在此目录保存项目生成结果或敏感凭据。

详细工作流和 H3 规则见 [`docs/h3.md`](../docs/h3.md)、[`docs/aigate.md`](../docs/aigate.md) 与 [`docs/project-workflow.md`](../docs/project-workflow.md)。
