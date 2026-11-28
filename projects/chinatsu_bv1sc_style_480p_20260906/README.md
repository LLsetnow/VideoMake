# 千夏｜BV1SCtV6tE1c 风格模仿｜竖屏 480p

## 目标

参考视频：<https://www.bilibili.com/video/BV1SCtV6tE1c/?vd_source=d44f9d802b17bdbbe7072b5aa7011306>

把参考视频重构为同一段连续时长的竖屏千夏人物时装变装视频：保留白色摄影棚、中央全身展示、色卡构图、旋转变装节奏和人物运动方向；角色身份、服装设计、画面和声音由 H3 重新生成。

## 已准备素材

- 下载参考：`00_reference/reference.mp4`，源时长 11.178667 秒；为兼容 24 fps 控制视频，生成目标时长 11.125 秒。
- 参考理解：`01_analysis/video_understanding.txt`；关键节点接近 2/4/6/8 秒。
- 四套千夏服装参考图：`02_character_refs/`。
- 480p 深度+骨骼控制视频：`03_control/depth_skeleton_control_480p_24fps.mp4`，480×864、24 fps、无音轨；仅用于姿态、转身、深度层次和动作节奏。
- H3 英文提示词：`chinatsu_bv1sc_style_480p_prompt.txt`；中文对照：`chinatsu_bv1sc_style_480p_prompt_zh.txt`。
- RH API 工作流：`04_workflow/chinatsu_bv1sc_style_480p_workflow_api.json`。

## 服装锚点

| 时间 | 参考图 | 服装色彩 |
| --- | --- | --- |
| 00:02 | `chinatsu_key_02_coral_aqua_pink.png` | 珊瑚橙、浅水蓝、粉色 |
| 00:04 | `chinatsu_key_04_blue_red_denim.png` | 浅蓝牛仔、红色、浅蓝 |
| 00:06 | `chinatsu_key_06_yellow_blue_brown.png` | 明黄、浅蓝、深棕 |
| 00:08 | `chinatsu_key_08_blue_green_brown.png` | 天蓝、森林绿、暖棕 |

四张图作为 H3 Ref2VA 的图片参考输入，并在提示词中以 2/4/6/8 秒作为服装状态锚点；控制视频是无声的深度+DWPose 合成图，不会被直接渲染到成片中。

## 生产与验证

最终版本使用 RH_CLI 本地 Web App API `POST http://127.0.0.1:8766/api/tasks` 并行提交四段工作流，远端工作流为 `2094755110367227906`，站点/账号为 `ai` / `account_9946f5228811`。每段都使用 `audio_mode=lock_source`，并额外接入 `02_character_refs/chinatsu_face_identity.png`。

初版成片：`output/chinatsu_bv1sc_4segments_lock_source_480p.mp4`。在动作复核中发现 seg01/03/04 的转体提示词约束偏弱，已保留 seg02，并强化其余三段的全身连续转体提示词后重新提交。随后发现尾部静帧和 seg4 人体/控制图泄漏风险，已用控制视频尾帧 + 千夏面部身份图重新生成尾帧参考图，并将 seg4 改为连续 5.125 秒生成。最终又根据参考视频实际结尾，将尾帧改为正面/近正面姿态并重新提交。当前成片：`output/chinatsu_bv1sc_4segments_lock_source_480p_front_tail_final.mp4`。四段 RH 产物按 2/2/2/5.125 秒连续拼接，源片音频连续回填整片。规格、重提任务号、动作接触表、完整解码和关键帧核验见 `qa/lock_source_4segments_qc.md`。

此前的单段原生音乐版本保留为 `output/native_single_pass_preview_480p.mp4`，不作为本次最终交付。
