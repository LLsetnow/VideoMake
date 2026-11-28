# 千夏：分离语音与明显环境参考测试

本次测试验证 MiniMax H3 在两条分工明确的音频参考下，能否同时生成明显的环境音和人物语音：

- `<Audio 1>`：千夏纯 TTS 人声，作为 `drive_audio` 和主要音频参考；
- `<Audio 2>`：纯环境声，包含明显连续的雨声、室内底噪和低频嗡鸣，作为 `ref_audios.ref_audio_0`；
- `audio_mode: reference_only`：最终音轨由 H3 重新生成，不锁定源音频；
- `add_source_as_reference: true`、`prompt_primary_audio_ordinal: 1`：把驱动人声注册为 `<Audio 1>`；环境声单独注册为 `<Audio 2>`；
- 不设置 `final_audio`，避免把源人声直接替换成输出音轨；最终 MP4 仍使用 H3 解码输出音频（节点 11 的音频输出连接到节点 12）。

## 输入

- 人声：`../千夏_原声对白口型测试_lock_source_20260908/input/tts_run/output.wav`
- 环境：`../千夏_参考音频_明显环境音_reference_only_20260908/qa/environment_only.wav`
- 角色图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`

## 预期验收

1. 画面为雨窗前千夏近景，口型跟随原对白；
2. 最终音轨同时有清晰人物语音和可辨认、连续的雨声/室内环境；
3. 用 `ffprobe` 检查视频、音频流与时长；用 `ffmpeg` 解码；抽取画面接触表；对输入和输出音轨做频谱对比。

如果 H3 仍然把环境层压低或切断，应记录为参考生成的能力边界；要保证“明显环境音 + 人物语音”，则需要 `lock_source` 使用混合源音频，或在 H3 生成人声后进行后期环境声混音。

## 本次结果（2026-09-08）

- RH 本地任务：`task_027d320135d9`
- 远程任务：`2097245299922010114`
- 消耗：23 coins
- 输出：`output/task_027d320135d9/qianxia_split_reference_clear_ambient_test_1.mp4`
- MP4：736×1280、24 fps、5.166667 秒、H.264 + AAC 32 kHz stereo；ffmpeg 解码通过。
- 画面：角色近景和口型变化正常，雨窗背景保持可见。
- 音频结论：未达到“明显连续环境音 + 人物语音”的验收标准。输出频谱在约 0.17–0.26 秒的多个停顿区出现明显断层；输出高频环境区间的平均电平约为 -31.3 dB，而纯环境参考约为 -28.9 dB。说明即使把纯人声和纯环境拆成 `<Audio 1>`、`<Audio 2>`，`reference_only` 仍可能把环境层压低或切断。
- 证据：`qa/contact_sheet.jpg`、`qa/output_spectrogram.png`、`qa/reference_environment_spectrogram.png`、`qa/output_audio_decoded.wav`。
