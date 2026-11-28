# 千夏参考音频环境声与独白测试（native）

本次实验与上一次 `lock_source` 保持相同角色、画面和对白，唯一改变是：把“千夏独白 + 室内环境底噪”作为参考音频，而不是最终音频。

- 角色参考图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`
- 原始千夏独白：`/Users/apple/Documents/VideoMake/projects/千夏_原声对白口型测试_lock_source_20260908/input/tts_run/output.wav`
- 参考音频：`input/千夏_环境音+独白_参考音频.wav`
- 音频模式：`Ref2VA` + `audio_mode: native`
- 参考音频角色：`ref_audios.ref_audio_0`
- 目标时长：5.16 秒，单镜头正面中近景；让 H3 新生成对白和环境声
- RH 路线：RH_CLI 本地 `POST http://127.0.0.1:8766/api/tasks`

输入文件只在任务清单中记录路径，不复制或覆盖原始角色资产。

## 实验结果

- 本地任务：`task_e90222ef33d5`
- 远端任务：`2097239324069240833`
- 输出：`output/task_e90222ef33d5/qianxia_audio_reference_ambient_monologue_test_1.mp4`
- 媒体核验：736×1280、24 fps、5.166667 秒；H.264 视频 + AAC 双声道音轨；整段解码通过。
- 参考关系核验：输出音频与参考音频解码后的归一化波形相关度约 0.0096，说明不是原音频直接复制；输出仍保持同样的 5.152 秒有效音频长度。
- 画面核验：抽帧可见千夏在室内背景中持续进行张口、闭口和圆唇变化，口型测试通过。
- 复核结论：`52:audio → 53:TrimAudioDuration → 6:ref_audios.ref_audio_0` 连线正确，但 `audio_mode: native` 只生成新的最终音频，不能稳定继承参考录音中的环境层；本次没有听到环境音，因此不能把它视为“参考音频保留环境声”的有效验证。
- 下一次正确验证应改为 `audio_mode: reference_only`，把 `53` 接到 `drive_audio`，并启用 `add_source_as_reference: true`；`final_audio` 不应接入当前 `VHS_VideoCombine` 的最终音频路径。
