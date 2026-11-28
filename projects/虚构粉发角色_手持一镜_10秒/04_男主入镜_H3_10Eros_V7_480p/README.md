# 男主入镜 · 10Eros V7 480p 对照

使用用户提供的 10Eros V7 API 节点图，通过 RH Desk 提交 RunningHub AI。与 H3 Beta5 对照使用同一张 [480×864 首帧](../source/picture_1_480x864.png)、逐字相同的 [英文提示词](prompt.txt) 和同一随机种子，目标 10 秒、24 fps、原生音轨。

沿用附件中的 Beta7、SelfLift 和 6 步基础调度加 1 步 sigma 精化。仅接入图生视频首帧，清除模板示例图和音频输入，直接将原提示词送入模型，保留 MP4 输出。

RH Desk 任务 `task_207b224f48bf`，RunningHub 任务 `2125916172121894913`。使用 [RunningHub 公开工作流](https://www.runninghub.ai/post/2076684097694466049) 作为执行入口。公开 API 图的节点 ID、类型及输入值与附件逐项一致。用户打开的副本返回 `WORKFLOW_NOT_SAVED_OR_NOT_RUNNING`，未向该副本提交。

[480p 原始回片](output/task_207b224f48bf/pink-partner-h3-10eros-v7-480p_1.mp4)

实际输出 480×864、24 fps、243 帧、10.125 秒，带原生双声道 AAC 音轨。完整解码通过，场景检测未发现硬切。男主约在第 1 秒从画面右上方进入，之后的靠近和扶臂动作可见。抽帧中画面比 LTX 对照更稳定，仍有男主遮挡，无法确认后段动作完整执行。平均音量 −24.7 dBFS。
