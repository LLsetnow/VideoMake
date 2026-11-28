# 千夏明显环境音 + 人物独白参考音频测试（reference_only）

本次专门验证：H3 能否从“明显雨声/室内环境 + 千夏独白”的参考音频中，重新生成同时包含环境声和人物语音的最终音轨。

- 角色参考图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`
- 原始千夏独白：`/Users/apple/Documents/VideoMake/projects/千夏_原声对白口型测试_lock_source_20260908/input/tts_run/output.wav`
- 主要参考音频：`input/千夏_雨声+室内底噪+独白_参考音频.wav`
- 音频模式：`Ref2VA` + `audio_mode: reference_only`
- 关键连线：`53 → drive_audio`，`add_source_as_reference: true`，`prompt_primary_audio_ordinal: 1`
- 目标时长：5.16 秒，单镜头正面中近景；要求明显雨声/室内声 + 清晰人物独白
- RH 路线：RH_CLI 本地 `POST http://127.0.0.1:8766/api/tasks`

输入文件只在任务清单中记录路径，不复制或覆盖原始角色资产。
