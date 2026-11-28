# 苍蓝_六分街_可爱觉醒_10秒

原创角色「苍蓝」在绝区零风格六分街场景的可爱觉醒开场动画。复刻参考视频的"战斗开场"运镜结构（低角度推镜→摇镜面部→环绕拉远→后拉亮相），内容改为可爱觉醒（星星爆发代替武器展开、比耶亮相）。

## 规格

- 时长：10.125 秒（243 帧 = 17×14+5，24fps）
- 画幅：1280×736（16:9，0.9MP，32 倍数）
- 模式：MiniMax H3 Ref2VA（Full-reference），原生音频（audio_mode=native）
- 音频：H3 原生生成双声道 AAC 32kHz（电子流行+街景环境声）
- Aigate 实例：1140785445116452864（4090-48GB-DDR5，华东一区，个人镜像 comfypsV4），已完成并停止

## 参考资产

| 标签 | 资产 | 用途 |
| --- | --- | --- |
| <Picture 1> | `ref/character/苍蓝/苍蓝_绝区零风格_三视图_1x1_v2.png` | 角色身份（可爱版，fully_preserved） |
| <Picture 2> | `ref/background/绝区零/六分街.png` | 六分街场景（partially_preserved） |
| 运镜参考（离线分析） | `videoRef/榎本京介 - ...ゼンゼロ戦闘開始モーション...mp4` | 仅分析运镜写入提示词，不上传工作流 |

## 镜头结构（multishot_plan_status: confirmed，见 analysis/multishot_plan.md）

| 镜 | 时间 | 内容 | 运镜 |
|---|---|---|---|
| S1 | 0–3.0s | 黑场淡入，苍蓝轻快步行登场 | 低机位从鞋袜特写向上推镜 |
| S2 | 3.0–5.5s | 停步抬头微笑，猫耳耳机青色光圈亮起 | 快速摇镜+抬升扫向面部特写 |
| S3 | 5.5–7.5s | 转身蹲跳，星星+霓虹光带爆发 | 环绕+快速后拉 |
| S4 | 7.5–10s | 落地比耶+wink，星环收束 | 后拉+旋转约30°至大全景定格 |

## 文件

- `苍蓝_六分街_可爱觉醒_10秒_prompt.txt` — 英文执行提示词（Ref2VA 六段式）
- `苍蓝_六分街_可爱觉醒_10秒_prompt_zh.txt` — 中文翻译
- `苍蓝_六分街_可爱觉醒_10秒_workflow_api.json` — ComfyUI API 工作流（T8: Ref2VA+native；双 LoadImage 节点 37/38；10s；16:9）
- `analysis/` — 运镜分析、背景识别、多镜头方案
- `qa/` — 视觉核验记录、接触表
- `output/canglan_sixthstreet_awaken_10s_00001-audio.mp4` — 最终视频

## 复现

```bash
opc aigate --start --instance <实例> --run \
  -w "projects/苍蓝_六分街_可爱觉醒_10秒/苍蓝_六分街_可爱觉醒_10秒_workflow_api.json" \
  --load-image-node 37 --image "ref/character/苍蓝/苍蓝_绝区零风格_三视图_1x1_v2.png" \
  --reference-image-node 38 --reference-image "ref/background/绝区零/六分街.png" \
  -o "projects/苍蓝_六分街_可爱觉醒_10秒/output" --timeout 1200
```

注：CLI 直连提交在部分网络环境下会报"无法连接云扉 ComfyUI 服务"（代理干扰），可用 OPC 模块直调绕过（本次采用），或先 unset http_proxy/https_proxy/all_proxy 再提交。

## 交付

- 成品（4 步）：`projects/苍蓝_六分街_可爱觉醒_10秒/output/canglan_sixthstreet_awaken_10s_00001-audio.mp4`
- 软链接：`videoOutput/苍蓝_六分街_可爱觉醒_10秒_最终.mp4`

## 8 步重跑（v2，2026-08-14 23:34）

- 工作流：`苍蓝_六分街_可爱觉醒_10秒_8步_workflow_api.json`（仅 DualClockSampler steps 4→8，其余不变）
- 提交：OPC 模块直调（CLI 受代理影响仍报连接错误），实例 1140785445116452864，已完成并停止
- 输出：`output/canglan_sixthstreet_awaken_10s_8step_00001-audio.mp4`（7.2MB，1280×736/24fps/10.125s/AAC 双声道）
- 核验：`qa/video_content_check_8step.txt` —— 角色一致✅ 街道场景✅ 特效+比耶wink✅ 无明显瑕疵✅
- 软链接：`videoOutput/苍蓝_六分街_可爱觉醒_10秒_8步_最终.mp4`

## 二采工作流版（v3，2026-08-15 00:23）

- 工作流：`苍蓝_六分街_可爱觉醒_10秒_二采_workflow_api.json`（基于 `workflows/H3 极速二采高质量图_文生视频_api.json`）
- 结构：一采 0.4MP 6 步快速出片 → 放大到 1MP（1376×768）→ 二采 res_multistep+beta+denoise 0.2 精修；Ref2VA + 原生音频，内容/提示词与 v1 完全相同
- 实例侧修复（1140787515177439232）：SSH 安装缺失节点 `ComfyUI-PT_H3ConcatAVLatent`（github.com/ptmaster/…）；pip 安装 `nvidia-vfx`；强制重启 ComfyUI 加载节点
- 改动点：① 缺 LoRA `minimax_h3_turbo_4步加速_comfyui.safetensors` → 改用实例已有的 `minimax_h3_turbo_4step.safetensors`（同源 ModelTC）；② `nvidia_rtx_vsr` 需 NGX 模型（实例无）→ 改 `lanczos`（保持二采管线，仅换放大算法）
- 输出：`output/canglan_sixthstreet_awaken_2pass_00001-audio.mp4`（6.5MB，1376×768/24fps/10.125s/AAC 双声道）+ `canglan_sixthstreet_awaken_2pass_draft_00003-audio.mp4`（一采草稿 3.7MB）
- 核验：`qa/video_content_check_2pass.txt`
- 软链接：`videoOutput/苍蓝_六分街_可爱觉醒_10秒_二采1MP_最终.mp4`

### nvidia_rtx_vsr 环境排查结论（2026-08-15）

- 已装好：`nvidia-vfx` 0.1.0.1（nvvfx，Linux 官方包，含 libnvidia-ngx-vsr 1.8.2 + TensorRT10/NPP/cuDNN）；系统 NGX 运行时 libnvidia-ngx.so.1 (590.44.01) 已确认被加载（strace）
- 阻断点（上游限制，非实例缺包）：① VSR 专有模型文件需 NVIDIA NGC 账号下载（nvvfxsuperres 集合），pip/apt 无此包；② nvvfx 0.1.0.1（Alpha）的 `set_string(NVVFX_MODEL_DIRECTORY)` 返回 "not yet implemented (code -2)"——Python 封装层未实现模型目录设置，VFX SDK 文档要求 Load 前必须设置；③ 故 `NvVFX_Load` 报 code -12
- 结论：`nvidia_rtx_vsr` 暂无法在 Linux + 0.1.0.1 上生效；等待 NVIDIA 更新封装或提供可公开获取的模型；当前用 `lanczos` 替代并已验证可用
