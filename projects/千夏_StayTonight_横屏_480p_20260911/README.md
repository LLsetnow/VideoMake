# 千夏 · StayTonight 横屏 480p

## 成品

- 成品：`output/task_5726147e61f7/qianxia_stay_tonight_landscape_480p_1.mp4`
- 稳定链接：`output/千夏_StayTonight_横屏_480p_final.mp4`
- 统一入口：`../../videoOutput/千夏_StayTonight_横屏_480p_20260911.mp4`

## 输入与约束

- 动作/镜头参考：`/Users/apple/Downloads/Sour初音ミク_StayTonight_no_twintails_white_clay_f0120-0480.mp4`
- 实际送入 RH 的静音结构参考：`reference/StayTonight_reference_864x480_24fps_silent.mp4`
- 原皮三视图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏-全身三视图-方形-v2.png`
- 面部特征图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`
- 舞台参考：`/Users/apple/Documents/VideoMake/ref/background/绝区零/404舞台.png`
- 93 号节点 LoRA：`minimax_h3_fl2v_turbo_4step_v1.2_768p_bf16.safetensors`
- 舞台灯光：冷蓝顶部主洗，穿雾青白聚光束，粉/黄侧面霓虹，两只镜面球的移动高光，人物头发/翅膀/面颊/肩线的浅色轮廓光，以及红色护栏和粉色旗帜的低强度暖色前景反差。

## RH 记录

- 提交方式：RH_CLI 本地 Web API `POST http://127.0.0.1:8766/api/tasks`
- 工作流：`wf_81a715c3011b` / RunningHub `2094755110367227906`
- 本地任务：`task_5726147e61f7`
- 远端任务：`2098400302808465410`
- 旧配置任务 `task_4b9222d5225a` 已取消，其记录未作为成品使用。
- 源视频为 12.033333 秒、30fps；H3 采用 24fps 合法长度约束，成片为 12.25 秒（294 帧），为最接近的可生成时长。
- 成片使用全新原生 AAC 双声道音频，不复用源视频音轨。

## QA

- `qa/ffprobe_output.json`：实际媒体流信息
- `qa/contact_sheet/output_contact_sheet.jpg`：抽帧检查
- `qa/submission_payload.json`：本次提交载荷
- `qa/submission_response_v2.json`：本次 RH 返回
- `qa/task_final_response.json`：本次 RH 完成态响应
- `output/task_5726147e61f7/workflow_api.json`：任务工作流快照
- `output/task_5726147e61f7/prompt_group.json`：任务参考组快照
- `output/task_5726147e61f7/manifest.json`：任务清单快照
