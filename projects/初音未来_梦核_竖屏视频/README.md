# 初音未来_梦核_竖屏视频

梦核（dreamcore）风格的初音未来（Hatsune Miku）竖屏（9:16）视频项目。

## 项目目标

- 风格：梦核 dreamcore —— 阈限空间、柔和过曝、蓝绿色（teal/青绿）主色调、复古 2000 年代数字质感、怀旧忧伤的空灵感。
- 角色：初音未来（青绿色双马尾、蓝绿色眼睛、默认制服造型）。
- 画幅：9:16 竖屏。
- 配乐：MiniMax Music 生成的梦核氛围纯音乐（instrumental）。

## 参考资产

| 资产 | 路径 | 用途 |
| --- | --- | --- |
| 风格参考图 v1（粉彩走廊，含角色） | `analysis/梦核miku_风格参考图_v1.png` | 早期风格变体，可作风格参考 |
| 风格参考图 v2（云海房间，含角色） | `analysis/梦核miku_风格参考图_v2.png` | 早期风格变体，可作风格参考 |
| 角色参考三视图（1:1 人物卡片） | `ref/character/初音未来/初音未来_三视图_1x1_v1.png` | 角色身份参考（Full-reference 主体，全段共用） |
| 泳池背景（蓝绿主色调，9:16，无人物） | `ref/background/assets/初音未来_梦核_背景_9x16_v1.png` | 场景参考（S1/S5/S6/S8） |
| 无尽走廊背景（9:16，无人物） | `ref/background/assets/初音未来_梦核_走廊_9x16_v1.png` | 场景参考（S2） |
| 云海房间背景（9:16，无人物） | `ref/background/assets/初音未来_梦核_云海房间_9x16_v1.png` | 场景参考（S3） |
| 天空云海背景（9:16，无人物） | `ref/background/assets/初音未来_梦核_天空云海_9x16_v1.png` | 场景参考（S4/S7） |
| 梦核氛围纯音乐（112.38s） | `analysis/梦核miku_纯音乐_v1.mp3` | 视频配乐 / 锁定音频（lock_source） |

## 当前进度

- [x] 生成风格参考图 v1 / v2（角色+场景一体，9:16）
- [x] 视觉模型核验风格参考图（`opc image understand`，结论见 `analysis/*_check.txt`）
- [x] MiniMax 生成梦核氛围纯音乐（112.38s，instrumental）
- [x] 生成角色参考三视图（1:1 人物卡片，`ref/character/初音未来/`）并核验
- [x] 生成 4 张蓝绿主色调梦核背景图（泳池/走廊/云海房间/天空云海，9:16 无人物）并核验
- [x] 风格/音乐确认与定稿
- [x] 分镜方案 v4（桌面参考图 7 场景，无天堂意象，每镜头约 3 秒共 38 镜头，低清/噪点/手持质感，见 `分镜方案.md`）
- [x] v4 提示词 8 段（EN+ZH）与 workflow JSON（0.5MP 低清），按时间序列子项目归档（`1-15秒/`…`106-112秒/`，文件名含 `初音未来_梦核_竖屏视频_<区间>_prompt*.txt / _workflow_api.json`；段-场景映射 `analysis/manifest.json`）
- [x] 音乐切片 8 段（各子项目 `初音未来_梦核_竖屏视频_<区间>_音频切片.mp3`，合计 112.3846s）
- [x] v1 提交失败复盘：仅 S1 成功（已保留为 v1 变体），实例已由用户释放
- [x] v4 生成完成（实例 1140787515177439232；S1–S8 全部成功，含云端孤儿结果找回与 S3 去重）
- [x] 8 段生成结果下载与核验（544×960/24fps，画面/场景/角色抽查通过）
- [x] 拼接成品（112.384s = 原曲时长，混流原始音乐，CFR 24fps；`bash analysis/concat_qa.sh`）
- [x] 交付：`output/初音未来_梦核_竖屏视频_112s_v3.mp4`（29MB，S2 穿墙修复版）+ `videoOutput/初音未来_梦核_竖屏视频_112s_v3.mp4` 软链接 + QA 记录（`qa/`）
- [x] S2 修复：16–30秒 改为画面右缘入场+全程与墙壁分离（旧版存 `qa/v4_dedup/S2_旧版_穿墙问题.mp4`），新实例 1140807480139976704 重生成并重新拼接
- [x] 发布：标题《梦核 Miku》，Bilibili 定时 2026-08-15 20:00（BV1fagM6UEu4，tid 193，状态“通过审核，等待发布”）；小黑盒已提交；文案与命令见 `发布/发布文案.md`

## 复现信息

### 风格参考图

- 生成通道：`codex exec`（内置 imagegen / gpt-image 驱动）
- 提示词：`analysis/风格参考图_v1_prompt.txt`、`analysis/风格参考图_v2_prompt.txt`、`analysis/三视图_prompt.txt`、`analysis/背景图_prompt.txt`
- 输出：`analysis/梦核miku_风格参考图_v1.png`、`analysis/梦核miku_风格参考图_v2.png`、`ref/character/初音未来/初音未来_三视图_1x1_v1.png`、`ref/background/assets/初音未来_梦核_背景_9x16_v1.png`
- 核验：`analysis/风格参考图_v1_check.txt`、`analysis/风格参考图_v2_check.txt`、`analysis/三视图_check.txt`、`analysis/背景图_check.txt`
- 用途：后续 H3 视频生成的风格/角色/场景参考图（Full-reference）

### 音乐

- 生成通道：`opc music generate --provider minimax`
- 模型：music-3.0-free（MiniMax Music）
- 模式：instrumental 纯音乐
- 提示词：`analysis/纯音乐_prompt.txt`
- 输出：`analysis/梦核miku_纯音乐_v1.mp3`
