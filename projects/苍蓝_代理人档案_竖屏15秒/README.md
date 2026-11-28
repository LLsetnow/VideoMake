# 苍蓝_代理人档案_竖屏15秒

为原创角色“苍蓝”制作的 15 秒竖屏代理人档案视频。镜头语法参考 B 站视频 [BV1RUu46oEwd](https://www.bilibili.com/video/BV1RUu46oEwd)，但参考视频只离线分析，不作为 H3 输入；角色、文案、音乐和画面构图均为本项目原创。

## 规格

- 时长：15 秒；目标 360 帧；24fps
- 画幅：9:16 竖屏；0.9MP；目标 736×1280（32 倍数）
- H3 模式：Ref2VA / Full-reference；角色身份参考 + `audio_mode: lock_source`
- 采样：MiniMax H3 T8 Dual Clock，4 steps，`shift_video=12`，`shift_audio=3`
- 音频：使用 `opc music generate --provider minimax --instrumental` 生成，从完整候选曲第 45–60 秒取出并做 1.4 秒自然淡出，作为 v2 锁定源音乐
- 实际输出：v2 严格 15.000 秒、360 帧；AIGate 实例 `1140808926688317440`

## 资产与用途

| 资产 | 用途 |
|---|---|
| `ref/character/苍蓝/苍蓝_绝区零风格_三视图_1x1_v2.png` | `<Picture 1>`；角色身份、服装、配色、比例和配饰参考 |
| `audio/苍蓝_代理人档案_minimax_15s_v2.wav` | `<Audio 1>`；当前 v2 的 15 秒锁定源音轨 |
| `audio/苍蓝_代理人档案_minimax_15s.wav` | v1 音轨，保留作对照，不再作为当前交付音频 |
| `analysis/代理人档案丨洛克茜.mp4` | B 站参考视频的离线研究副本，不进入工作流 |
| `苍蓝_代理人档案_竖屏15秒_prompt.txt` | H3 六段式英文执行提示词 |
| `苍蓝_代理人档案_竖屏15秒_prompt_zh.txt` | 完整中文翻译 |
| `苍蓝_代理人档案_竖屏15秒_workflow_api.json` | ComfyUI API 工作流；包含角色图、LoadAudio、TrimAudioDuration 和 `lock_source` |

## 分镜

六镜头确认方案见 `analysis/multishot_plan.md`：装备细节 → 服装向上扫描 → 眼神锁定 → 全身英雄亮相 → `AZ` 徽记 → 最终档案卡。提示词中的时间点是 H3 创作意图；生成后仍需通过接触表、场景检测和帧级检查确认最终剪辑边界。

## 音乐生成与分析

```bash
opc music generate '为一条竖屏游戏角色代理人档案视频创作一段15秒可循环的纯音乐：赛博朋克电子档案风，冷色合成器与低沉脉冲贝斯，稀疏金属打击和颗粒化故障音，约112 BPM，前2秒像扫描启动，3到5秒加入清晰的鼓点推进，6到10秒出现有冲击力的主旋律和明亮合成器上行，10到13秒加入短促的英雄亮相重拍，最后2秒以干净的数字徽记音和余响收束；节奏要利落、适合角色细节特写到全身档案卡的镜头切换；无歌词、无人声、无环境对白。' \
  --provider minimax --instrumental --format wav \
  -o 'audio/苍蓝_代理人档案_minimax_full.wav'
```

候选生成后，从完整 MiniMax 曲目中选择 45–60 秒窗口，使用 `ffmpeg` 仅做结尾自然淡出，得到 `audio/苍蓝_代理人档案_minimax_15s_v2.wav`，再用 `opc music beats` 输出本项目的节拍证据。v1 音频保留但不再交付。

## AIGate 复现

先确认新实例为符合项目规则的 `4090-48GB-DDR5`，再提交：

```bash
opc aigate --start --create \
  --sku '4090-48GB-DDR5' \
  --area '华东一区' \
  --image-id '<COMFYPS_V4_IMAGE_ID>' \
  --image-type 3

opc aigate --start --instance '<INSTANCE_ID>' --run \
  -w 'projects/苍蓝_代理人档案_竖屏15秒/苍蓝_代理人档案_竖屏15秒_workflow_api.json' \
  --reference-image 'ref/character/苍蓝/苍蓝_绝区零风格_三视图_1x1_v2.png' \
  --reference-image-node 37 \
  --audio 'projects/苍蓝_代理人档案_竖屏15秒/audio/苍蓝_代理人档案_minimax_15s_v2.wav' \
  --audio-node 52 \
  --output 'projects/苍蓝_代理人档案_竖屏15秒/output' \
  --timeout 1800
```

提交成功不等于完成。必须下载并检查实际 MP4、`ffprobe` 帧数/音轨/时长、接触表和视频可读性；确认结果后再停止或释放实例。

## 交付

当前最终视频：`output/canglan_agent_profile_15s_final_v2.mp4`；统一入口：`../../videoOutput/苍蓝_代理人档案_竖屏15秒_最终.mp4`。完整 v2 技术与视觉核验见 `qa/v2_final_verification.txt`。v1 成品和核验记录保留作对照，当前项目文件夹保留生成日志、提示词、工作流、音频和 QA 证据，不覆盖其他项目或已有用户改动。
