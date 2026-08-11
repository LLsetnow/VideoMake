# BV1P2ux6gEF8 参考创作

本项目根据 B 站视频 `BV1P2ux6gEF8` 的视觉语言进行原创再创作。源视频仅用于观察风格、镜头节奏和构成主义视觉特征；它没有进入任何 H3/ComfyUI 视频输入节点。

## 已确认素材

- 源视频：`source_reference.mp4`，38.382585 秒，1920×1080，30 fps
- 源音频：`海螺绝绝子 这一天遇见文生天花板 MiniMaxH3开源/海螺绝绝子 这一天遇见文生天花板 MiniMaxH3开源.m4a`
- 原创视觉参考图：`visual_reference_16x9_v1.png`
- 音频切片：`source_audio_0-15.wav`、`source_audio_15-30.wav`、`source_audio_30-38.382585.wav`

## 生成策略

由于 MiniMax H3 单段时长上限为 15 秒，完整视频拆为 15 + 15 + 8.382585 秒三段。三段均使用 16:9、24 fps、`Ref2VA`、`audio_mode=lock_source`，只上传原创视觉参考图和对应音频切片。三段结果按时间顺序拼接，并以原始音频切片作为最终音轨。

提示词：

- `BV1P2ux6gEF8_参考创作_0-15s_prompt.txt`
- `BV1P2ux6gEF8_参考创作_15-30s_prompt.txt`
- `BV1P2ux6gEF8_参考创作_30-38.382585s_prompt.txt`

工作流：

- `BV1P2ux6gEF8_参考创作_0-15s_workflow_api.json`
- `BV1P2ux6gEF8_参考创作_15-30s_workflow_api.json`
- `BV1P2ux6gEF8_参考创作_30-38.382585s_workflow_api.json`

## AIGate

提交前已检测到现有实例 `1139404372570669056`，未创建新实例。生成完成后应停止该实例；不会释放或删除用户原有实例资源。
