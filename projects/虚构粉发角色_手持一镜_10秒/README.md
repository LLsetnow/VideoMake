# 粉发角色 · 手持一镜 10 秒

通过 RH Workflow Desk 本地 Web API 提交至 RunningHub AI 站点。目标为 480p 竖屏、10 秒、24 fps、单镜头，使用原生音频。沿用上一轮的一采主模型与 LoRA，采样 8 步、LoRA 强度 0.5。

- [英文执行提示词](prompt.txt) · [中文译文](prompt_zh.txt) · [API 节点图](workflow_api.json)
- `source/original.png` 是附件原件。`source/picture_1_480x864.png` 等比缩放原图并在上下延伸、柔化边缘，以保留左右构图。
- `13:image` 为唯一参考输入，绑定 `<Picture 1>` 并在提示词中指定 0.00 秒起镜。Ref2VA 用该图约束开场与角色外观。
- RH Desk 任务 `task_ccbe3734ac13`，RunningHub 任务 `2125906348424388609`。

[480p 原始回片](output/task_ccbe3734ac13/pink-handheld-10s-480p-8step_1.mp4)

实际输出为 480×864、24 fps、243 帧、10.125 秒，带双声道 AAC。全片完整解码通过，场景检测未检出硬切。抽帧可见首帧适配产生的上下边缘延伸，生成音轨整体音量偏低。
