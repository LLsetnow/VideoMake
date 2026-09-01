# RunningHub CLI 工作流提交

VideoMake 除了通过 `opc aigate` 提交本地 ComfyUI 工作流，也可以通过 `RH_CLI` 的 `rh workflow run` 提交到 RunningHub。两条路径互相独立：RunningHub 不需要创建或启动 AIGate 实例。

接口依据：[RunningHub 发起 ComfyUI 任务（高级）](https://www.runninghub.cn/runninghub-api-doc-cn/api-425749013) 与 [上传资源（图片、视频、音频、压缩包）](https://www.runninghub.cn/runninghub-api-doc-en/api-425761099)。

## 前置条件

`RH_CLI` 使用 `/Users/apple/Documents/github/RH_CLI` 中的 fork。首次安装或更新后，在该仓库中执行：

```bash
cd /Users/apple/Documents/github/RH_CLI
uv tool install . --editable --with socksio
```

配置 RunningHub Key（写入本机用户配置，不写入 VideoMake）：

```bash
rh auth set-key "<RUNNINGHUB_API_KEY>"
rh check
```

也可以通过环境变量 `RUNNINGHUB_API_KEY` 临时提供 Key。不要把 Key、浏览器 token 或带 token 的 URL 写入项目文件。

## 提交单个工作流

工作流必须是 ComfyUI **API 格式**导出的节点字典，`workflowId` 是 RunningHub 工作流页面 URL 末尾的数字：

```bash
cd /Users/apple/Documents/VideoMake
rh workflow run \
  "projects/<项目名>/<项目名>_workflow_api.json" \
  --workflow-id "<WORKFLOW_ID>" \
  -o "projects/<项目名>/output/"
```

单图片工作流可以使用 `--input`，它会上传图片并自动注入第一个 `LoadImage` 节点：

```bash
rh workflow run "projects/<项目名>/<工作流>.json" \
  -w "<WORKFLOW_ID>" \
  --input "<图片路径>" \
  -o "projects/<项目名>/output/"
```

## H3 工作流的图片、音频和视频输入

H3 工作流通常需要锁定音频和一张或多张参考图。使用可重复的 `--file`，按实际 workflow JSON 的节点 ID 和字段名上传并注入：

```bash
rh workflow run "projects/<项目名>/<工作流>.json" \
  -w "<WORKFLOW_ID>" \
  --file "37:image=<参考图路径>" \
  --file "52:audio=<锁定音频路径>" \
  -o "projects/<项目名>/output/"
```

`--file "nodeId:fieldName=本地路径"` 可重复，支持图片、音频、视频和其他工作流输入文件。多个 `LoadImage` 节点分别传多个 `--file`，不要把多个角色合并为一张图。例如：

```bash
rh workflow run "<workflow.json>" -w "<WORKFLOW_ID>" \
  --file "37:image=<角色参考图>" \
  --file "60:image=<场景背景图>" \
  --file "52:audio=<本段音频>" \
  -o "<项目>/output/"
```

`--set "nodeId:field=value"` 可临时覆盖 seed、时长或其他普通节点参数；它只修改本次提交内存中的工作流，不改写项目 JSON：

```bash
rh workflow run "<workflow.json>" -w "<WORKFLOW_ID>" \
  --set "9:denoise=0.4" \
  -o "<项目>/output/"
```

## 提交前检查

先校验本地 JSON 和输入文件，再提交：

```bash
python -m json.tool "<workflow.json>" >/dev/null
test -f "<参考图路径>"
test -f "<音频路径>"
rh workflow run --help
```

RunningHub 的工作流环境仍必须具备该工作流所需的自定义节点、模型和 VAE；本地 JSON 能解析不代表云端节点已经安装。提交成功只代表任务已入队，仍需确认 `OUTPUT_FILE` 指向的实际文件，并按 [`editing-delivery.md`](editing-delivery.md) 检查视频帧率、时长、画幅和音轨。

## 复现记录

项目 README 或 QA 记录中至少保存：提交路径、RunningHub `workflowId`、实际输入文件、节点映射、seed、输出目录和任务 ID。不要把 API Key 写入记录。
