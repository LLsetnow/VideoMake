# AIGate 生成与实例生命周期

## 资源和 GPU 规则

通过 `opc aigate` 查询资源、创建云端 ComfyUI 实例、提交 workflow_api 并下载结果。GPU 只允许 48G 显存的 RTX 4090 或 RTX 4090D；通常优先 `4090-48G`，禁止 RTX 5090 和任何 24G 显存实例。

每个新的视频生成项目优先新建一个符合要求的实例，不自动复用其他实例。同一项目拆分的子项目可以继续使用该项目新建的实例；只有用户明确要求或确认已有实例就是本项目专用实例时才可复用。若没有可用 48G 4090/4090D，等待并重新查询，不得降级。

命令参数以当前 CLI 帮助为准：

```bash
opc aigate --help
opc aigate --status
opc aigate --gpus --area "<区域>"
opc aigate --images
opc aigate --community-images --area "<区域>" --sku "4090-48G"
opc aigate --workflows --workflow-dir "projects/<项目名>"
```

认证默认读取 `AIGATE_TOKEN`，也可通过 `--token` 或 `--env-file`；Token 不得写入项目文件。

## 创建、提交和校验

创建新实例必须同时使用 `--start` 和 `--create`，并明确符合要求的 SKU、区域和镜像。`--image-type 2` 是社区镜像，个人镜像使用 `3`：

```bash
opc aigate --start --create \
  --sku "4090-48G" \
  --area "<区域>" \
  --image-id "<镜像ID>" \
  --image-type 2
```

创建前确认 `--gpus` 结果确实是 48G；不要为了单次提交误加 `--create`。已有实例仅在例外情况下启动：

```bash
opc aigate --start --instance "<INSTANCE_ID>"
```

提交 workflow_api 并下载结果：

```bash
opc aigate --start --instance "<INSTANCE_ID>" --run \
  --workflow "projects/<项目名>/<项目名>_workflow_api.json" \
  --output "projects/<项目名>/output" \
  --timeout 1200
```

`--workflow`/`-w` 必须指向 ComfyUI API JSON，`--output`/`-o` 是本地下载目录。`--prompt`、`--seed`、`--output-prefix` 可临时覆盖；提示词已写入 workflow JSON 时不重复传入。

输入媒体可以由 CLI 上传：

```bash
opc aigate --start --instance "<INSTANCE_ID>" --run \
  -w "projects/<项目名>/<项目名>_workflow_api.json" \
  --image "<输入图片路径>" \
  --reference-image "<角色参考图路径>" \
  --audio "<参考音频路径>" \
  --video "<参考视频路径>" \
  -o "projects/<项目名>/output"
```

多个同类输入或自动检测错误时，明确使用 `--load-image-node`、`--reference-image-node`、`--audio-node`、`--video-node`、`--prompt-node`、`--seed-node` 和 `--video-output-node`。每次调用的 CLI 同类参数对应一个输入；多个参考媒体预先在 workflow JSON 中配置多个独立节点，不能靠重复参数覆盖同一个节点，也不能把多个角色合成一张图。

提交多个任务时，每个任务使用独立的输出目录或输出前缀，保存队列顺序、任务/实例 ID、工作流、提示词、seed、分辨率、帧数和输出位置。`--run` 一次接收一个 workflow JSON；可用多次提交把任务按时间顺序加入服务器队列。

本地校验 workflow：

```bash
python -m json.tool projects/<项目名>/<项目名>_workflow_api.json >/dev/null
```

等待时间只能作为估算：约每 1 秒视频需要 30 秒基础生成时间，另加实例启动、排队、上传和下载缓冲；不要只因提交成功就判断完成。必须逐项检查日志和实际输出文件。

## 停止与释放

```bash
opc aigate --stop --instance "<INSTANCE_ID>"
opc aigate --release --instance "<INSTANCE_ID>"
```

`--stop` 只是暂时关闭；`--release` 会释放并删除资源。确认结果已下载、归档和核验后才可释放。标准顺序是：查询并创建合规实例，确认节点/模型，提交任务，确认输入媒体可访问，检查每项结果，最后决定停止或释放。
