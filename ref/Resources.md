# 可复用资源索引

ref/ 下的角色、服装、背景、姿势和音频索引分别维护；本文件只作为统一入口。

- [character 角色参考索引](character/character.md)
- [clothes 服装参考索引](clothes/clothes.md)
- [background 背景参考索引](background/background.md)
- [pose 姿势参考索引](pose/pose.md)
- [audio 音频参考索引](audio/audio.md)

## 索引条目格式

所有可被积木库扫描的索引统一使用以下结构：

```markdown
### 分类

#### 条目标题

![图片说明](相对于当前 Markdown 文件的图片路径)
[音频说明](相对于当前 Markdown 文件的音频路径)

> 对应提示词或资源说明
```

每个 `####` 条目都会生成一个可加入组装台的资源积木；图片和音频是可选媒体，`>` 开头的内容会作为积木文本。人物变体直接写成“角色名 · 变体名”的 `####` 标题，保持与 pose 相同的抽取层级。各索引中的媒体链接相对于各自 Markdown 文件所在目录；新增资源时先放入对应目录，再在对应索引追加条目，并检查实际文件。

## 新增资源流程

1. 将图片或音频放入对应的 `character/`、`audio/`、`background/` 或 `clothes/` 目录。
2. 在对应索引中新增一个 `####` 条目，写入媒体链接和 `>` 提示词。
3. 回到提示词工坊点击“重新扫描”；程序会按 Markdown 内容重建本机 `web/data/prompt/references.json` 缓存。
4. 不要手动编辑缓存 JSON；条目 ID 由类型、来源文件和标题稳定生成，组装台与组状态库保存的是该 ID 及当时的文本/媒体快照。
