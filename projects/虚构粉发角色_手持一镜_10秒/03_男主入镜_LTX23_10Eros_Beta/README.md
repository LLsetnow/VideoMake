# LTX 2.3 · 10Eros Beta 对照测试

使用 [上一版首帧](../source/picture_1_480x864.png) 和逐字相同的 [英文提示词](prompt.txt)。沿用上一版种子，单段 480×864、24 fps、241 帧，保留原生音频。

通过 RH Desk 提交至 RunningHub AI。以 [RH LTX 2.3 模板](https://www.runninghub.ai/post/2031935763281092609) 的 API 图为基础，使用 [10Eros Beta checkpoint](https://www.runninghub.ai/model/public/2031467159095873537)，保留单图首帧条件，使用作者图的 13 步 sigma 序列及 DPM++ SDE，CFG 2，不叠加额外 LoRA，不执行超分。

RH Desk 任务 `task_b5d5c4badd99`，RunningHub 任务 `2125912824723369986`。 [480p 原始回片](output/task_b5d5c4badd99/ltx23-10eros-beta-480p_1.mp4)

实际输出 480×864、24 fps、241 帧、10.042 秒，带双声道 AAC，完整解码通过。场景检测未检出硬切。约第 2 秒男主进入，主要动作是靠近和拥抱。中段有明显拖影，腿部重叠，无法确认性交动作。平均音量约 −50.7 dBFS，上一版 H3 为 −29.8 dBFS。
