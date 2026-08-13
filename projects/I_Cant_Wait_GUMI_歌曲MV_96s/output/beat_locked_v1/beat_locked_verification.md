# 精准卡点版验收报告

## 时间轴

- 主时钟：原始音频 `00_素材/I Can't Wait (feat. GUMI).mp3`
- 音频模式：`lock_source`
- 素材池：9 个 H3 生成视频，覆盖 A01–A09；包含 15–22 秒修复重做素材 A04
- 卡点区间：35 个
- 目标帧率：24 fps
- 目标总帧数：2280
- 目标总时长：95.000000 秒
- 节拍量化误差：起点和终点最大绝对误差 20.333 ms，符合 24fps 单帧量化范围

## 素材与剪辑

- `asset_manifest.csv`：保存场景检测的原始边界、安全窗口、检测阈值和可用性
- `beat_locked_timeline.csv`：保存每个目标区间、整数帧边界、素材窗口、复用次数和误差
- `segment_validation.csv`：35 个逐段视频均为 1280×720、24fps，实际帧数与目标帧数一致
- 所有生成片段自带音频已丢弃，最终仅回封原始 MP3
- 所有素材统一中心裁剪：1280×736 → 1280×720

## 最终文件

- `I_Cant_Wait_GUMI_MV_beat_locked.mp4`
- 视频：H.264、1280×720、yuv420p、24fps、2280 帧、95.000000 秒
- 音频：MP3、48000 Hz、双声道，来自原始歌曲
- `ffmpeg -v error -i ... -f null -` 解码检查通过
- `beat_locked_contact_sheet.jpg`：全片视觉验收
- `beat_locked_14-24_contact_sheet.jpg`：15 秒附近卡点区域验收
