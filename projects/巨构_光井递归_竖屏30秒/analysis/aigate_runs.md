# AIGate 生成记录

## 实例

- instance：`1141836100341997568`
- GPU：`4090D-48G-DDR5`
- area：`华东二区`
- image：个人镜像 `comfypsV5`，ID `1141060360767930368`
- ComfyUI：已在 2026-08-17 启动并确认就绪
- workflow：复制自 `workflows/H3 极速二采高质量图_文生视频_api.json`
- 模式：T2VA、native H3 audio、9:16、24 fps、约 0.4 MP 一采 + 1 MP 二采
- 二采放大：项目副本使用 `lanczos`；共享模板中的 `nvidia_rtx_vsr` 在该实例上触发 `NvVFX_Load code -12`，因此未继续使用。

## 提交计划

| 段落 | seed | 输出目录 | 状态 |
|---|---:|---|---|
| 00–10 秒 | 2026081701 | `output/00-10秒/` | 已完成；prompt `37ae9964-f040-48e0-8b4a-de75667729b3`；二采文件已核验 |
| 10–20 秒 | 2026081702 | `output/10-20秒/` | 已完成；prompt `a1c7b3f7-ed7e-409c-bf94-bfbf3c1f3e3c`；二采文件已核验 |
| 20–30 秒 | 2026081703 | `output/20-30秒/` | 已完成；prompt `6974ca4a-ad3d-4b9b-b1e1-fa5be524b8df`；二采文件已核验 |

每段二采输出实际为 768×1376、24 fps、243 帧、10.125 秒；最终按帧裁为每段 240 帧。输出核验完成后已释放实例，`opc aigate --status` 确认云扉控制台无实例。
