# background 目录规则

本目录保存可复用的背景图案和场景背景。

当前背景索引是 [`background.json`](background.json)，其 `references` 数组保存分类、标签、场景描述和媒体路径；媒体路径优先相对于本索引所在的 `ref/background/` 目录解析。新增或迁移背景时同步维护该 JSON，不恢复已删除的分类 Markdown 索引。

- 参考图必须使用 `image-gen` 生成，并为 ComfyUI/AIGate 可读取的 PNG、JPG 或 WEBP 等栅格图像；禁止使用 SVG 等矢量图作为参考输入。
- 接入工作流前确认文件真实存在、方向和比例正确，并明确它是背景参考还是首帧/尾帧。
- 可复用背景放在这里；只属于一次任务的临时图放在对应项目目录。
- 不覆盖已验证背景，不写入凭据。

详细资产规则见 [`docs/media-assets.md`](../../docs/media-assets.md)；项目和时间线规则见 [`docs/project-workflow.md`](../../docs/project-workflow.md)。
