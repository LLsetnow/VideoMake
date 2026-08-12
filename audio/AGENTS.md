# audio 目录规则

本目录保存通用音乐、源音频、驱动音频和参考音频。

- 锁定源音频项目使用 `audio_mode: lock_source`；各生成段必须引用对应的同一源音频时间范围，不重复、不遗漏、不重新生成音乐。
- 下载音频后先检查完整性、格式和可读性，再归档；项目专属音频也可保存在对应 `projects/<项目名>/` 下。
- 用 `opc audio librosa` 检测鼓点/起音，用 `opc audio` 分析曲风和听感；分析结果保存到对应项目目录，而不是覆盖源音频。
- 不把 cookies、令牌或其他敏感凭据放入此目录。

详细规则和命令见 [`docs/media-assets.md`](../docs/media-assets.md) 与 [`docs/project-workflow.md`](../docs/project-workflow.md)。
