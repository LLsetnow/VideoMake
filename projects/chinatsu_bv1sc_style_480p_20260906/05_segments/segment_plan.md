# 四段首尾帧并行提交计划

所有段落都使用同一条参考视频的 480p 深度+DWPose 控制视频切片和对应源音频切片。工作流采用 H3 `Ref2VA` 的首尾帧边界用法：`Picture 1` 只作为该段 literal first frame，`Picture 2` 只作为该段 literal last frame，`Picture 3` 是额外的千夏面部身份参考；`Video 1` 只提供动作/深度/机位结构，`Audio 1` 以 `lock_source` 直接复用参考视频音频。

| 段 | 全局时间 | 首帧 | 尾帧 | 控制视频 | 源音频 |
| --- | --- | --- | --- | --- | --- |
| 01 | 00:00.000–00:02.000 | `chinatsu_boundary_00_gray.png` | `chinatsu_key_02_coral_aqua_pink.png` | `seg01_0.000-2.000_control.mp4` | `seg01_0.000-2.000_source.wav` |
| 02 | 00:02.000–00:04.000 | `chinatsu_key_02_coral_aqua_pink.png` | `chinatsu_key_04_blue_red_denim.png` | `seg02_2.000-4.000_control.mp4` | `seg02_2.000-4.000_source.wav` |
| 03 | 00:04.000–00:06.000 | `chinatsu_key_04_blue_red_denim.png` | `chinatsu_key_06_yellow_blue_brown.png` | `seg03_4.000-6.000_control.mp4` | `seg03_4.000-6.000_source.wav` |
| 04 | 00:06.000–00:08.000 | `chinatsu_key_06_yellow_blue_brown.png` | `chinatsu_key_08_blue_green_brown.png` | `seg04_6.000-8.000_control.mp4` | `seg04_6.000-8.000_source.wav` |

四个 RH 工作流严格覆盖 00:00–00:08 的四个相邻首尾帧变装段；第 4 段尾帧是 00:08 的蓝绿棕造型。最终装配在 00:08–00:11.125 冻结该尾帧，同时保留对应的参考视频原音，因此交付片仍是完整 11.125 秒。
