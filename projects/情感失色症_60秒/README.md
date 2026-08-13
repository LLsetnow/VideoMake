# 《情感失色症》60 秒 H3 音频锁定视频

## 任务摘要

- 源链接：`https://music.163.com/#/album?id=365369307`
- 解析得到的单曲：`情感失色症`，网易云单曲 ID `3357295057`，专辑 ID `365369307`，原始时长约 `144.64s`。
- 制作范围：源曲前 `60.000s`。
- 音频策略：四个 15 秒 WAV 片段分别作为 H3 `MiniMaxH3AudioConditioningT8` 的 `lock_source`，最终成片再回封装源 MP3 前 60 秒。
- 视觉策略：原创白色情绪实验室；源曲只作为音乐与节拍驱动，不上传网易云页面或源视频画面。
- 画面：16:9，H3 24 fps；最终输出裁到 `1280x720`。
- 节奏：23 个视觉镜头，平均约 `2.61s/镜头`；切点见 `cutlist.csv`。

## 音频分析

- 曲风报告：`analysis/music_style_opc_audio.txt`
- 鼓点报告：`analysis/drumbeats_librosa.txt`
- 识别摘要：现代电子流行/舞曲，带 electro-pop 与 chiptune 色彩，四拍底鼓、类钢琴合成器动机、温暖贝斯与短合成器填充。
- Librosa：估计 BPM `95.34`；使用强度阈值 `0.15`、最小事件间隔 `0.50s`。

## H3 工作流

- `1-15秒/情感失色症_00-15_prompt.txt`
- `15-30秒/情感失色症_15-30_prompt.txt`
- `30-45秒/情感失色症_30-45_prompt.txt`
- `45-60秒/情感失色症_45-60_prompt.txt`
- 对应工作流为同目录 `*_workflow_api.json`；四段均使用 `Ref2VA`、`audio_mode: lock_source`、`audio_denoise_strength: 0`、`add_source_as_reference: false`。
- 参考图：`visual_refs/style_reference_16x9.png`，由 imagegen 生成并裁成 16:9 栅格图。

## 交付与验收

生成结果、拼接中间文件与 QA 联系表归档在 `output/` 和 `qa/`。必须完成 `ffprobe` 的时长、分辨率、帧率、音频编码、采样率、声道检查，并抽帧检查视觉连续性；确认文件完整后才释放本次 AIGate 实例。
