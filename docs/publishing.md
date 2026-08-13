# 视频发布流程

本文档记录 VideoMake 成片发布到 Bilibili 和小黑盒的实际流程。发布前先确认最终视频已经留在对应项目的 `output/` 或 `04_输出/` 目录，并完成 `ffprobe` 检查。

## 1. 发布前检查

```bash
VIDEO="/绝对路径/项目/output/最终视频.mp4"

test -f "$VIDEO"
ffprobe -v error \
  -show_entries format=duration:stream=codec_name,width,height \
  -of default=nw=1 "$VIDEO"
```

建议同时准备封面。Bilibili 和小黑盒都可能拒绝没有封面的投稿；没有单独封面时可以取首帧：

```bash
ffmpeg -y -v error -i "$VIDEO" -frames:v 1 "/绝对路径/项目/封面.png"
```

封面生成后用图片查看工具确认主体没有被裁切，竖屏视频尤其要检查人物和文字安全区。

## 2. Bilibili

### 2.1 登录和校验

`sau` 使用账号名隔离登录状态。首次登录在用户自己的本地终端完成：

```bash
sau bilibili login --account creator
sau bilibili check --account creator
```

预期校验结果为 `valid`。不要把 Cookie、`SESSDATA`、`bili_jct` 或二维码信息写进项目文件。

### 2.2 立即投稿

```bash
sau bilibili upload-video \
  --account creator \
  --file "/绝对路径/项目/output/最终视频.mp4" \
  --title "标题" \
  --desc "简介" \
  --tid 193 \
  --tags "标签1,标签2,标签3" \
  --thumbnail "/绝对路径/项目/封面.png"
```

常用字段：

- `--tid`：Bilibili 分区 ID，发布前确认当前分区映射。近期使用过 `193`（音乐/MV）、`172`（游戏/手机游戏）、`47`（动画/同人·手书）。
- `--tags`：使用英文逗号分隔，不要写成空格分隔。
- `--thumbnail`：封面图片路径；不指定时可能使用默认封面或被平台要求补充。

### 2.3 定时投稿

```bash
sau bilibili upload-video \
  --account creator \
  --file "/绝对路径/项目/output/最终视频.mp4" \
  --title "标题" \
  --desc "简介" \
  --tid 172 \
  --tags "绝区零,妄想天使,AI视频" \
  --thumbnail "/绝对路径/项目/封面.png" \
  --schedule "2026-08-14 20:30"
```

`--schedule` 使用本机上海时区的 `YYYY-MM-DD HH:MM` 格式。命令返回 `submitted` 只代表投稿已提交，仍需查询稿件状态。

### 2.4 查询投稿记录

`sau` 本身不保存完整投稿历史；稿件记录保存在 Bilibili 服务器。当前本机的 `biliup` 运行时路径如下：

```bash
BILIUP="/Users/apple/.social-auto-upload/tools/biliup/macos-aarch64/biliup"
ACCOUNT_FILE="/Users/apple/Documents/github/social-auto-upload/cookies/bilibili_creator.json"

"$BILIUP" -u "$ACCOUNT_FILE" list --pubed --max-pages 100
"$BILIUP" -u "$ACCOUNT_FILE" list --is-pubing --max-pages 100
"$BILIUP" -u "$ACCOUNT_FILE" list --not-pubed --max-pages 100
```

已知 BV 号时查看完整详情：

```bash
"$BILIUP" -u "$ACCOUNT_FILE" show BV号
```

重点核对 `title`、`tag`、`cover`、`dtime` 和 `state_desc`。定时稿件常见状态是“通过审核，等待发布”。

## 3. 小黑盒

### 3.1 登录和校验

小黑盒使用浏览器自动化，首次登录必须打开可见浏览器：

```bash
sau xiaoheihe login --account creator --headed
sau xiaoheihe check --account creator
```

预期校验结果为 `valid`。后续上传可以使用 `--headless`。

### 3.2 发布视频

```bash
sau xiaoheihe upload-video \
  --account creator \
  --file "/绝对路径/项目/output/最终视频.mp4" \
  --title "标题" \
  --desc "简介" \
  --communities "社区名称" \
  --tags "话题1,话题2,话题3" \
  --thumbnail "/绝对路径/项目/封面.png" \
  --headless
```

小黑盒视频发布约束：

- 当前集成只支持立即发布，不支持 `--schedule`。
- 必须选择至少一个社区/分区；最多 2 个社区。
- 最多 5 个话题，使用英文逗号分隔；应选择搜索结果中的已有话题，避免无意创建新话题。
- 必须提供封面。没有项目封面时，使用前面的 `ffmpeg` 命令生成首帧封面。
- 支持 `.mp4` 和 `.mov`。

本次使用过的社区示例：`绝区零`、`盒友杂谈`。非游戏类 AI 动画可以使用 `盒友杂谈`，具体仍应以当前账号可搜索到的社区为准。

### 3.3 验证发布结果

小黑盒当前 CLI 没有完整的投稿列表命令。发布成功后打开创作者后台：

```text
https://www.xiaoheihe.cn/creator/content_management/home
```

在“内容管理 → 视频”中按标题核对内容是否出现。编辑已有视频时，进入对应卡片的“编辑内容”，只修改简介或其他目标字段，再点击“修改”；不要为了修改元数据重新上传视频。

## 4. 当前三个项目的发布示例

### I Can't Wait

```text
项目：projects/I_Cant_Wait_GUMI_歌曲MV_96s/
视频：output/I_Cant_Wait_GUMI_MV_final.mp4
封面：封面.png
Bilibili：I Can’t Wait，tid=193
小黑盒社区：盒友杂谈
```

### 绝区零三人动画

```text
项目：projects/绝区零_保底参考_横屏30秒/
视频：output/绝区零_保底参考_横屏30秒_最终.mp4
封面：封面.png
Bilibili：三人同框太犯规啦！，tid=172
小黑盒社区：绝区零
```

### 七面棱镜

```text
项目：projects/粉色长发奇幻构成主义_15秒/
视频：04_输出/pink_constructivist_fantasy_15s_00001-audio.mp4
封面：封面.png（由首帧生成）
Bilibili：七面棱镜的开启，tid=47
小黑盒社区：盒友杂谈
```

## 5. 故障排查

- `sau bilibili` 提示账号无效：重新执行 `sau bilibili check --account creator`，必要时在真实终端重新登录。
- Bilibili 返回 `submitted`：不要立即重复上传；使用 `biliup list` 或 `show BV号` 查询远端状态。
- 小黑盒提示“请添加分区”：补充 `--communities`，并确认社区名称来自搜索结果。
- 小黑盒提示“投稿请添加封面”：补充 `--thumbnail`；没有封面时从首帧生成。
- 小黑盒提示“未找到小黑盒视频上传按钮”：检查 `social-auto-upload` 当前版本是否包含编辑页登录校验的修复；登录校验应刷新当前编辑页，不能把页面跳回内容管理首页。
- 小黑盒上传失败后，不要假定已经公开；回到创作者后台检查是否只是草稿或未完成编辑页。

发布命令成功后，必须做一次平台侧核对；本地命令退出码不能单独证明视频已经公开。
