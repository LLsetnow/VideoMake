# AIGate Qwen3.8 与 DSH 手动启动指南

这份指南用于手动启动 AIGate 实例中的 Qwen3.8-27B，并让本机 DSH 通过 SSH 隧道访问它。

## 当前配置

- 模型：`Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-Q6_K_P.gguf`
- 识图模型：`mmproj-Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-BF16.gguf`
- 模型目录：`/home/waas/models/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive`
- llama-server：远端 `127.0.0.1:6007`
- Qwen API 代理：远端 `0.0.0.0:6006`
- KV Cache：`q4_0`
- 上下文：`262144`（256K）
- 最大输出：`32768`（32K）
- 本地 SSH 转发：`127.0.0.1:16008 -> 远端 127.0.0.1:6006`
- 本地 DSH Web：<http://127.0.0.1:3080>

模型服务使用全 GPU 加载；`q4_0` KV Cache 用于降低显存和延迟。每次更换实例时，SSH 主机、端口和密码都必须重新查询，不要写死。

## 1. 本地终端：查询实例和 SSH 信息

在本机 OPC 仓库执行。以下命令不会打印 SSH 密码：

```bash
cd /Users/apple/Documents/github/OPC
source .venv/bin/activate
set -a; source .env; set +a

export AIGATE_INSTANCE_ID="实例ID"
opc aigate --status --instance "$AIGATE_INSTANCE_ID" --no-proxy

export AIGATE_SSH_HOST="$(python3 -c 'from opc_cli.aigate import get_instance_detail; import os; d=get_instance_detail(os.environ["AIGATE_TOKEN"], os.environ["AIGATE_INSTANCE_ID"]); s=next(x for x in d["instanceUtilList"] if x.get("name")=="ssh"); print(s["host"],end="")')"
export AIGATE_SSH_PORT="$(python3 -c 'from opc_cli.aigate import get_instance_detail; import os; d=get_instance_detail(os.environ["AIGATE_TOKEN"], os.environ["AIGATE_INSTANCE_ID"]); s=next(x for x in d["instanceUtilList"] if x.get("name")=="ssh"); print(s["instancePort"],end="")')"
export SSHPASS="$(python3 -c 'from opc_cli.aigate import get_instance_detail; import os; d=get_instance_detail(os.environ["AIGATE_TOKEN"], os.environ["AIGATE_INSTANCE_ID"]); s=next(x for x in d["instanceUtilList"] if x.get("name")=="ssh"); print(s.get("password", ""),end="")')"
```

确认实例状态为 `运行中(2)` 后再继续。

## 2. 登录远端实例

仍在本地终端执行：

```bash
sshpass -e ssh -tt \
  -o StrictHostKeyChecking=no \
  -o PreferredAuthentications=password \
  -o PubkeyAuthentication=no \
  -p "$AIGATE_SSH_PORT" \
  "root@$AIGATE_SSH_HOST"
```

进入远端后，先启用实例代理：

```bash
source /etc/profile.d/ssh-env.sh
source /etc/waas-script/proxy.sh
```

## 3. 远端启动 Qwen3.8

先检查是否已经运行，已有服务时不要重复启动：

```bash
pgrep -a -x llama-server || true
ss -ltnp | grep -E ':6006|:6007' || true
```

确认没有 `llama-server` 后执行：

```bash
MODEL_DIR=/home/waas/models/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive

nohup /home/waas/llama.cpp/build/bin/llama-server \
  -m "$MODEL_DIR/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-Q6_K_P.gguf" \
  --mmproj "$MODEL_DIR/mmproj-Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-BF16.gguf" \
  --host 127.0.0.1 \
  --port 6007 \
  --api-key-file /home/waas/qwen-api.key \
  --alias qwen3.8-27b-aggressive \
  --ctx-size 262144 \
  --parallel 1 \
  -ngl 99 \
  --flash-attn on \
  --cache-type-k q4_0 \
  --cache-type-v q4_0 \
  --jinja \
  --no-webui \
  > /home/waas/llama-server-qwen3.8-256k.log 2>&1 </dev/null &
```

等待模型加载后验证：

```bash
curl http://127.0.0.1:6007/health
tail -n 30 /home/waas/llama-server-qwen3.8-256k.log
nvidia-smi
```

看到 `{"status":"ok"}`、`model loaded` 和 `listening on http://127.0.0.1:6007` 才算就绪。

## 4. 远端启动 6006 API 代理

该镜像使用 Miniconda 的 Python；系统 `python3` 可能没有 `aiohttp`，所以使用下面的解释器：

```bash
PROXY_PID="$(pgrep -f '^/root/miniconda3/bin/python .*qwen-proxy.py$' | head -n 1 || true)"
if [ -n "$PROXY_PID" ]; then
  echo "qwen-proxy 已运行，PID=$PROXY_PID"
else
  nohup /root/miniconda3/bin/python /home/waas/qwen-proxy.py \
    > /home/waas/qwen-proxy-qwen3.8.log 2>&1 </dev/null &
fi

sleep 2
curl http://127.0.0.1:6006/health
```

## 5. 本地另开终端建立 SSH 隧道

如果是新终端，需要重新执行第 1 步获取 `AIGATE_SSH_HOST`、`AIGATE_SSH_PORT` 和 `SSHPASS`。然后执行下面的命令，并保持这个终端不要关闭：

```bash
sshpass -e ssh -N \
  -L 16008:127.0.0.1:6006 \
  -o StrictHostKeyChecking=no \
  -o ServerAliveInterval=30 \
  -o ServerAliveCountMax=3 \
  -p "$AIGATE_SSH_PORT" \
  "root@$AIGATE_SSH_HOST"
```

再开一个本地终端验证：

```bash
curl http://127.0.0.1:16008/health
```

预期返回：

```json
{"status": "ok"}
```

## 6. 启动本地 DSH

当前 `/Users/apple/.dsh/settings.yaml` 已配置为：

- provider：`local-qwen38`
- model：`qwen3.8-27b-aggressive`
- baseURL：`http://127.0.0.1:16008/v1`
- contextWindow：`262144`（256K）
- maxTokens：`32768`（32K）
- input：`[text, image]`

本地执行：

```bash
cd /Users/apple/Documents/github/deepseek-harness
pnpm dsh web --port 3080
```

访问 <http://127.0.0.1:3080>。

如果 DSH 已经运行，先在它所在终端按 `Ctrl-C`，再重新执行上面的启动命令。

## 7. 快速检查

```bash
curl -sS http://127.0.0.1:16008/health

QWEN_KEY=$(sed -n 's/^LOCAL_QWEN_API_KEY: //p' /Users/apple/.dsh/.credentials.yaml)
curl -sS http://127.0.0.1:16008/v1/models \
  -H "Authorization: Bearer $QWEN_KEY"
unset QWEN_KEY
```

模型列表中应包含：`qwen3.8-27b-aggressive`。

## 8. 重启和停止

只重启 DSH：在 DSH 终端按 `Ctrl-C`，再执行第 6 步。远端 Qwen 和 SSH 隧道不需要重启。

停止远端 Qwen 前，先确认 PID：

```bash
pgrep -a -x llama-server
```

确认无误后：

```bash
kill -TERM "确认过的 llama-server PID"
```

关闭 SSH 隧道：在隧道终端按 `Ctrl-C`。不要使用宽泛的 `killall` 或按关键字批量杀进程。

## 常见问题

- SSH 认证失败：重新执行第 1 步，AIGate 的 SSH 密码可能已刷新。
- 6006 没有启动：确认使用 `/root/miniconda3/bin/python`，不要使用系统 `python`。
- DSH 提示不支持图片：确认 `settings.yaml` 中模型条目包含 `input: [text, image]`。
- CUDA OOM：先将 `--ctx-size`、`contextWindow` 同时降到 `131072`（128K），保留 q4_0 KV；仍不足时再降到 `65536`。
