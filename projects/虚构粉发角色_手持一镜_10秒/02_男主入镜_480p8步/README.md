# 粉发角色 · 男主画外进入

通过 RH Workflow Desk 的本地 Web API 提交至 RunningHub AI 站点。沿用 [上一轮的竖屏首帧](../source/picture_1_480x864.png)、一采模型、随机种子与 LoRA 0.5。设置为 480p、10 秒、24 fps、8 步、原生音频。

- [英文执行提示词](prompt.txt) · [中文译文](prompt_zh.txt) · [API 节点图](workflow_api.json)
- 首次任务 `task_16211c0b7bea` 在上传参考图时遇到 SSL 连接中断。以相同输入和参数重试后，RH Desk 任务 `task_b9ec6695e93f` 对应 RunningHub 任务 `2125908327649333249`。

[480p 原始回片](output/task_b9ec6695e93f/pink-partner-enters-10s-480p-8step_1.mp4)

实际输出为 480×864、24 fps、243 帧、10.125 秒，带双声道 AAC。完整解码通过，场景检测未检出硬切。抽帧显示男主在约第 1 至 2 秒从画面右侧入镜，之后留在女主身前。两人靠近及女主手扶男主手臂的动作可见，后段髋部有遮挡。
