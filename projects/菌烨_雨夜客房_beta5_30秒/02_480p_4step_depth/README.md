# 02 段 · 480p 四步深度参考测试

从上一条 480p 测试（`task_7d24172892d2`）的 3.500 秒位置提取彩色源帧，再用 Depth Anything V2 Small F16 生成 864×480、8 位灰度深度图。

- Picture 1 绑定菌烨的身份。Picture 2 使用本目录的 `pose_depth.png`，约束双人体位、支撑点和前后层次。
- 未将彩色源帧接入工作流。深度图只提供静态几何，动作节奏来自提示词。
- 沿用相同 Beta5 模型、LoRA、随机种子、4 步和 LoRA 0.5。
- RH Desk `task_1ac55be33677`，RunningHub `2125207013705469953`。
