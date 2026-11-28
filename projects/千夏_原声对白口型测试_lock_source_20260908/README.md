# 千夏原声对白口型测试（lock_source）

本次实验只验证 MiniMax H3 是否能让千夏角色的嘴部动作跟随千夏 GPT-SoVITS 原声对白。

- 角色参考图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`
- 千夏 TTS 模型：`/Users/apple/Documents/VideoMake/ref/tts/千夏/`
- 驱动音频：`input/tts_run/output.wav`
- 模式：`Ref2VA` + `audio_mode: lock_source`
- 目标时长：5.16 秒，单镜头正面中近景，无配乐和额外音效
- RH 路线：RH_CLI 本地 `POST http://127.0.0.1:8766/api/tasks`

输入文件只在任务清单中记录路径，不复制或覆盖原始角色资产。

## 实验结果

- 本地任务：`task_6925ab3ff8b9`
- 远端任务：`2097235719127867394`
- 输出：`output/task_6925ab3ff8b9/qianxia_lock_source_lipsync_test_1.mp4`
- 媒体核验：736×1280、24 fps、5.166667 秒；H.264 视频 + AAC 双声道音轨；整段解码通过。
- 音频核验：输出音轨解码后与输入 TTS 音频时长一致，归一化波形相关度约 0.8985；画面抽帧可见嘴部在对白过程中开合变化。
- 结论：本次 `lock_source` 口型测试成功，视频保留了源对白作为最终音轨，没有加入额外配乐或音效。
