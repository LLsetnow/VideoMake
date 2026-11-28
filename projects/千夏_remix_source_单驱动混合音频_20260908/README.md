# 千夏：remix_source 单驱动混合音频测试

本次测试验证：只连接一条已经混合“人物语音 + 明显环境声”的 `drive_audio`，并使用 `audio_mode: remix_source`，能否在 H3 重混后同时保留人声和环境声。

- `drive_audio`：`千夏_参考音频_明显环境音_reference_only_20260908/input/千夏_雨声+室内底噪+独白_参考音频.wav`
- `audio_mode`：`remix_source`
- `audio_denoise_strength`：`0.0`，尽量减少对源音频的改动
- `add_source_as_reference: true`、`prompt_primary_audio_ordinal: 1`：把唯一的 `drive_audio` 注册为 `<Audio 1>`
- 不连接 `ref_audios.ref_audio_0`
- 不设置 `final_audio`；最终 MP4 使用 H3 解码节点输出的生成音频
- 角色图：`/Users/apple/Documents/VideoMake/ref/character/千夏/千夏_正脸头像_v4.png`

## 验收

1. 口型跟随原对白；
2. 人物语音清晰；
3. 雨声/室内底噪在整段音轨中明显、连续；
4. `ffprobe`、`ffmpeg` 解码、画面接触表和输出频谱均通过检查。

注意：`remix_source` 是重混，不是 `lock_source` 的逐波形锁定；即使降噪强度为 0，也可能改变源音频的环境层或语音细节。

## 本次结果（2026-09-08）

- RH 本地任务：`task_2f0f2944c0bf`
- 远程任务：`2097249539839270914`
- 消耗：29 coins
- 输出：`output/task_2f0f2944c0bf/qianxia_remix_source_single_drive_test_1.mp4`
- MP4：736×1280、24 fps、5.166667 秒、H.264 + AAC 32 kHz stereo；ffmpeg 解码通过。
- 画面：雨窗前千夏近景，口型帧间有明显变化。
- 音频：输出高频环境区间平均电平约 `-27.6 dB`，输入混合源约 `-26.2 dB`；`silencedetect=noise=-42dB:d=0.15` 未检出静音断层。频谱显示整段存在连续宽频环境层，同时保留人声谐波带。
- 结论：本次“只连 `drive_audio` + `remix_source`”达到了明显环境音 + 人物语音的结构性验收；与 `reference_only` 版本相比，环境层连续性明显改善，但它仍是 H3 重混后的新音频，不是源音频逐波形复制。
- 证据：`qa/contact_sheet.jpg`、`qa/output_spectrogram.png`、`qa/output_audio_decoded.wav`。
