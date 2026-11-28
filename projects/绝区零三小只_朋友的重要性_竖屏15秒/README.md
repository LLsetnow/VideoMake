# 绝区零三小只 · 朋友的重要性 · 竖屏 15 秒

## 任务

- 目标：制作一条 9:16 竖屏、15.000 秒、24 fps 的《绝区零》三人友情音乐短片。
- 角色：千夏、南宫羽、爱芮；三张独立身份参考图，不合并人物图。
- 画风：`Zenless Zone Zero Cartoon rendering style`，二维动画线稿、赛璐璐平涂、都市波普高饱和色块。
- 参考视频：Bilibili `BV1SQ8X6VEfh`《朋友的重要性》；仅离线提取节奏和“独处到群体协同”的结构，不上传视频、不复刻人物和文字。
- 音频：`source_audio_0-15.wav`，从参考视频提取并补齐至 15.000 秒；H3 使用 `audio_mode=lock_source`。

## 文件

- 英文提示词：`绝区零三小只_朋友的重要性_竖屏15秒_prompt.txt`
- 中文翻译：`绝区零三小只_朋友的重要性_竖屏15秒_prompt_zh.txt`
- 多镜头方案：`analysis/multishot_plan.md`
- 参考视频分析：`analysis/reference_video_understand.txt`
- 节拍分析：`analysis/music_beats.txt`
- 音乐理解：`analysis/music_understand.txt`
- OPC 视频理解：`analysis/reference_video_opc_understand.txt`
- OPC 音频理解：`analysis/source_audio_opc_understand.txt`
- 原曲识别记录：`analysis/song_identification.txt`
- RH/H3 工作流：`绝区零三小只_朋友的重要性_竖屏15秒_workflow_api.json`
- 第一版成品：`output/绝区零三小只_朋友的重要性_竖屏15秒_480p.mp4`
- 第二版成品：`output/绝区零三小只_朋友的重要性_竖屏15秒_v2_480p.mp4`
- 第三版成品：`output/绝区零三小只_朋友的重要性_竖屏15秒_v3_480p.mp4`
- 第三版质检接触表：`qa/final_v3_contact_sheet.jpg`

## 输入映射

| H3 标签 | 工作流节点 | 文件 | 职责 |
|---|---:|---|---|
| `<Picture 1>` | 37 | `ref/background/绝区零/404Bar.png` | 404 Live Bar 场景 |
| `<Picture 2>` | 38 | `ref/background/绝区零/404舞台.png` | 404 Stage 场景 |
| `<Picture 3>` | 39 | `ref/background/绝区零/六分街.png` | 六分街场景 |
| `<Picture 4>` | 40 | `ref/character/千夏/千夏-全身三视图-方形-v2.png` | 千夏身份 |
| `<Picture 5>` | 41 | `ref/character/南宫羽/南宫羽_角色三视图.png` | 南宫羽身份 |
| `<Picture 6>` | 42 | `ref/character/爱芮/爱芮_角色三视图.png` | 爱芮身份 |
| `<Picture 7>` | 43 | `ref/character/千夏/千夏_正脸头像_v4.png` | 千夏正脸身份 |
| `<Picture 8>` | 44 | `ref/character/南宫羽/exec-e658e3d5-6076-41ee-bc9f-d6ca9c6c0063.png` | 南宫羽正脸身份 |
| `<Picture 9>` | 45 | `ref/character/爱芮/爱芮-正脸大头照.png` | 爱芮正脸身份 |
| `<Audio 1>` | 52 → 53 | `source_audio_0-15.wav` | 完整锁定源音频 |

## RH 提交流程

使用 VideoMake 项目规则要求的 RH_CLI 本地 Web API：

1. 检查 `GET http://127.0.0.1:8766/api/health`。
2. 用 `POST http://127.0.0.1:8766/api/tasks` 提交本项目 API 工作流，远端 workflowId 使用 RH 已登记的 `2094755110367227906`。
3. 输出目录为本项目 `output/`；完成后检查真实 MP4、24 fps、9:16、480p、15.000 秒、音轨和帧数。

## 状态

- 工作流 JSON：已基于已验证 Ref2VA 锁源音频基线复制并完成本项目化修改。
- RH 本地服务：提交前健康检查通过。
- RH 本地任务：第一版 `task_1daa33e0b91f`、第二版 `task_e8430123acb8`、第三版 `task_81acfad57b00` 均已完成并各保存 1 个远端产物。
- 输出核验：第三版通过；最终文件为 480×864、24 fps、15.000 秒容器时长，含 44.1 kHz 双声道 AAC 锁定源音轨。
- 人数/身份核验：第三版按 6 段检查通过，单人段为 1 人，三人段为千夏/南宫羽/爱芮各 1 人，无重复、交换、第四人或背景路人。
- 交付入口：`videoOutput/绝区零三小只_朋友的重要性_竖屏15秒_480p.mp4` 已切换为指向第三版；另保留 `_v1_`、`_v2_` 与 `_v3_` 软链接。
- OPC 复核：参考视频和第三版成片均已完成视频理解；视频理解使用 Qwen3-VL，音频理解使用 Qwen3-Omni Captioner。新版以人数反差为核心；音频风格、人声台词等内容仍属于模型听感分析，不能替代人工听审或 ASR 逐字核验。
