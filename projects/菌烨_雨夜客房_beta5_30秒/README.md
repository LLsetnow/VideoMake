# 菌烨 · 雨夜客房

30 秒横屏方案分三段，每段请求 10 秒、24 FPS。各段目录内包含英文执行提示词、中文译文和 ComfyUI API 工作流。

- 女主采用创作者提供的虚构成年角色菌烨。首个参考输入绑定其脸部和发型，男主采用固定的文字外观描述。
- 使用 `10Eros_Max_h3_hybrid_beta5.safetensors` 和 `h3ErosMax_beta5_turbo_lora_v1_rank_128_bf16.safetensors`，一采 15 步，LoRA 强度 0.5，16:9，0.9 MP。
- RunningHub AI 站点一采工作流 `2094755110367227906`。本地队列任务见 [tasks_rh.txt](tasks_rh.txt)，每段的任务快照和下载产物保存在对应的 `output/` 子目录。
- [tasks.txt](tasks.txt) 记录首次被 RH Desk 路由至本地 ComfyUI 的失败请求。
