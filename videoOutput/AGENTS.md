# videoOutput 目录规则

本目录是最终成品的统一访问入口，只保存指向项目内真实成品的软链接。

- 成品实体必须保留在 `projects/<项目名>/output/`；不要把 `videoOutput/` 当作生成或剪辑工作目录。
- 创建链接前确认没有同名文件/链接；创建后使用 `readlink` 确认目标正确且文件可读。
- 不因创建链接而删除、覆盖或移动项目输出。

详细交付和复现规则见 [`docs/editing-delivery.md`](../docs/editing-delivery.md)。
