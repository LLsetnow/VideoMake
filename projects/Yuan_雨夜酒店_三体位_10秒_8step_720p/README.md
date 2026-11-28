# Yuan 雨夜酒店 · 三体位 10 秒单工作流（8 step / 720p）

把第二组三张 8-step 关键帧接成一条 10 秒 H3 视频，走 RH_CLI 本地 Web App API 提交到 RunningHub（`execution_target: runninghub`，账号 `akai / ai`，凭据 `ai-rh`）。

## 分镜

| 镜头 | 时间 | 首帧 | 动作 |
| --- | --- | --- | --- |
| 1 | 0–3.375 秒 | `../Yuan_雨夜酒店_三体位_8step参考图_v2/output/yuan_rain_hotel_oral_side_8step_v4.png` | 床边跪姿口交，侧面固定机位；头部前后小幅两次，手指压大腿。 |
| 2 | 3.375–6.750 秒 | `../Yuan_雨夜酒店_三体位_8step参考图_v2/output/yuan_rain_hotel_cowgirl_front_8step_v7.png` | 床侧三分之四女上位；骨盆前后小幅两次，双手位置不变。 |
| 3 | 6.750–10.125 秒 | `../Yuan_雨夜酒店_三体位_8step参考图_v2/output/yuan_rain_hotel_missionary_side_8step_v6.png` | 床侧三分之四传教士；髋部两次前送，肩线高度不变。 |

切点均为硬切，三镜固定机位，原生音频（雨声、呼吸、床垫声），无对白、无配乐。

## 参数

- 模型：`10Eros_Max_h3_hybrid_beta5.safetensors` + `h3ErosMax_beta5_turbo_lora_v1_rank_128_bf16.safetensors`（strength 0.5）
- 采样：8 steps，shift_video 12，shift_audio 3，dual_clock_euler / native_flow
- 画面：16:9，0.9 MP（约 1280×736），24 fps
- 时长：10 秒 → 243 帧（17n+5 对齐，实际 10.125 秒）
- 工作流模板：`../yuan_四镜分镜帧_10秒/720p_8step_单工作流10秒/workflow_api.json`（`wf_6183e6174d00` → 远程 `2094755110367227906`）
- 工作流副本：`workflow_api.json`

## 提交

- 本地任务：`task_4481317b0e98`
- 远程任务：`2125451801440645121`
- 调度：`ai-rh / ai`，账号 `account_9946f5228811`
- 提交记录：`qa/submission_payload.json`、`qa/submission_response_8799.json`
- 输出目录：`output/task_4481317b0e98/`

提交使用 RH_CLI 本地 Web App API `POST /api/tasks`，`execution_target: runninghub`，未直接调用 RunningHub API。

桌面端常驻的旧后端（50334，启动于代码更新前）不识别 `execution_target`，会退回本地 ComfyUI 并报“无法连接 ComfyUI”；该次尝试 `task_aeffa2472d96` 已失败并保留作记录。最终提交改由同一数据目录的新后端（8799，`scripts/start.sh`）完成。

## 结果

- 成片：`output/task_4481317b0e98/yuan-three-poses-single-10s-720p-8step_1.mp4`
- 软链接：`../../videoOutput/Yuan_雨夜酒店_三体位_10秒_720p_最终.mp4`
- 1280×736 / 24 fps / 243 帧 / 10.125 秒 / AAC 立体声，全片可解码
- 实测硬切点 3.292 秒、6.333 秒（意图 3.375 / 6.750）
- 核验与接触表：`qa/validation.txt`、`qa/contact_sheet.jpg`
