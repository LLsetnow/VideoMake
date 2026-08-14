# 波普艺术 weird-girl 卡点视频 — 交付与复现记录

## 成品
- 视频 v2（最终版）：`projects/波普艺术_weird-girl_卡点视频/output/波普艺术_weird-girl_卡点视频_76s_v2.mp4`
  - 1280×736（16:9），24fps，H.264 + AAC 44.1kHz 立体声
  - 时长：76.416667s（1834 帧），与 v3 音乐完全一致
  - v2 = 段内分镜切点量化到节拍网格（见"场景切点检测"节）；v1 保留为未量化版本
- 软链接：`videoOutput/波普艺术_weird-girl_卡点视频_76s_v2.mp4`
- 音轨：`projects/波普艺术_weird-girl_主题曲/output/weird-girl_主题曲_复古另类少女流行_60s_v3.mp3`（完整复用）

## 音乐
- v3（76.4s）：MiniMax Music `music-3.0-free`，复古另类少女流行 Pop，约 110 BPM
- 鼓点检测：`analysis/v3_beats.txt`（librosa，BPM 109.96，强拍/起音列表）
- 音乐理解：`analysis/v3_music_understanding.txt`

## 分段与卡点切点（全部落在检测到的强拍/起音上）
| 段 | 时间（s） | 帧数 | 音乐段落 | 提示词 | 工作流 | seed |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | 0.000–12.725 | 305 | Intro+主歌1 | 1_0-12.725秒/S1_prompt.txt | S1_workflow_api.json | 575029984620997 |
| S2 | 12.725–23.812 | 266 | 主歌1→副歌 | 2_.../S2_prompt.txt | S2_workflow_api.json | 575029984731108 |
| S3 | 23.812–38.092 | 343 | 副歌1+Anthem | 3_.../S3_prompt.txt | S3_workflow_api.json | 575029984841219 |
| S4 | 38.092–51.177 | 314 | do-do-do+副歌回归 | 4_.../S4_prompt.txt | S4_workflow_api.json | 575029984951330 |
| S5 | 51.177–63.158 | 288 | 尾段主歌 | 5_.../S5_prompt.txt | S5_workflow_api.json | 575029985061441 |
| S6 | 63.158–76.416 | 318 | 收尾副歌+渐出 | 6_.../S6_prompt.txt | S6_workflow_api.json | 575029985171552 |

- 每段锁定音频切片：`lock_source_S{i}.wav`（从 v3 精确切割，44.1kHz）
- 参考图：`character/波普艺术/微信图片_20260811163716_103_80.png`（Ref2VA `<Picture 1>`，身份/风格/文字锚）

## H3 模式与流程
- 全流程经 `minimax-h3-creative-director` → `minimax-h3-multishot-planner`（18 镜方案已确认 `multishot_plan_status: confirmed`）→ `minimax-h3-reference-video-prompt`（Ref2VA 六段式，英文+中文双语）
- T8 节点：task_type=Ref2VA，audio_mode=lock_source，audio_denoise_strength=0，prompt_primary_audio_ordinal=1，reference_video_policy=official_2_to_15s
- 双时钟采样：4 步，shift_video=12，shift_audio=3，dual_clock_euler，native_flow
- 分辨率：0.9MP（1280×736），帧对齐 17n+5

## Aigate 实例（华东一区 4090D-48G，镜像 comfypsV4）
- 实例1 1140744668680167424：S5、S6（S1-S4 曾入队后被删除重分布）；实例使用中自动被平台回收
- 实例2 1140747252539203584：S1、S2（后被平台回收）
- 实例3 1140747256192442368：S3、S4、S5（重生成）
- 注：实例 1/2 生成完毕后被平台自动释放，S5 输出丢失，已在实例3 重生成（文件后缀 _00002）

## 剪辑
- 每段按目标帧数精确裁切（305/266/343/314/288/318 帧），concat 后 1834 帧 = 76.4167s
- 音轨整体复用 v3（44.1kHz AAC 256k），保证鼓点卡点精确
- QA：`qa/contact_sheet.jpg`（接触表）、`qa/cut_frames_0*.jpg`（各切点帧）
- 视觉验证（z.ai GLM 识图）：粉黑白复古印刷拼贴风格、深色齐刘海女孩、"weird-girl"/"STRANGE GIRLS CLUB" 文字均保留，各帧画面有动态差异

## 场景切点检测（scdet 核验）
- 逐段：`qa/scdet/S{i}_scdet.txt`；成品 v1：`qa/scdet/final_scdet.txt`；成品 v2：`qa/scdet/final_v2_scdet.txt`（ffmpeg scdet，阈值 0.30-0.35）
- **v2（最终版）17 个切点全部命中量化位置（±0.35s 内）**：
  - 5 个段边界：12.708 / 23.792 / 38.083 / 51.167 / 63.167s（硬切分 14.6~24.9）
  - 12 个段内分镜切点已量化到节拍网格（完整 164 点网格，`analysis/v3_beats_full_grid.txt`）：
    S1: 4.27/7.70, S2: 15.99/20.07, S3: 28.82/33.02, S4: 42.46/46.80, S5: 55.01/58.82, S6: 67.28/71.36（段内时间见 `analysis/quantized_inner_cuts.json`）
- 量化依据：H3 模型对提示词时间戳为近似执行（实测偏移 ±0.3~0.8s），v2 通过二次剪辑把每个检测到的段内切点移动到最近打击点（偏移 ≤0.21s），重拼接帧数不变（305/266/343/314/288/318）
- 剪辑中间产物（`analysis/trimmed/`、`analysis/beat_edit/` 视频部分）已按 `docs/project-cleanup.md` 分级清理（P3 移入回收站，2026-08-14）；帧级时间轴保留在 `analysis/beat_edit/frame_plan.json`，切点量化依据见 `analysis/quantized_inner_cuts.json`

## 复现
1. `opc aigate --start --create --sku "4090D-48G" --area "华东一区" --image-id 1138522483051855872 --image-type 3`
2. 对每段：`python3 analysis/aigate_helper.py submit <实例URL> <段>/S{i}_workflow_api.json character/波普艺术/微信图片_20260811163716_103_80.png <段>/lock_source_S{i}.wav <段>/output MiniMaxH3/weirdgirl_beat_S{i}`
3. 按本文件"剪辑"节裁切拼接（各段先按目标帧数 305/266/343/314/288/318 用 `-frames:v` 裁切，段内切点按 `analysis/quantized_inner_cuts.json` 拆分后 concat；中间文件已清理，需重跑时按此重建）
