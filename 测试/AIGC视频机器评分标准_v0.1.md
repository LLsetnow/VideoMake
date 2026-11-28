# AIGC 视频机器评分标准 v0.1

- 制定日期：2026-10-02。
- 用途：自动比较 H3 / 10Eros 的模型、LoRA、采样步数、分辨率和二采方案。
- 本版评分对象：**单镜头图生视频的视觉质量**。输出七项分数、一个综合指数、质量耗时比及异常记录。
- 配套规则：[aigc_scoring_profile_v0.1.json](aigc_scoring_profile_v0.1.json)。
- 实施状态：本文和 JSON 是可实现的评分规范；现有首帧 SSIM 程序可用，VideoScore2 / VBench 尚未在本机部署或完成推理。本版没有产生新的整段视频评分。

## 1. 评分维度与自动算法

| 维度 | 权重 | 主算法与原始输出 | 主要衡量内容 |
| --- | ---: | --- | --- |
| 首帧保真 R | 20% | 已有程序的 `ssim_luma` | 首帧结构与参考图是否接近 |
| 画面质量 V | 20% | VideoScore2：visual quality，整数 1–5 | 清晰度、伪影和整体画面质量 |
| 跨帧一致性 T | 15% | VBench：`subject_consistency` | 跨帧内容和主体表征是否稳定 |
| 运动平滑度 M | 10% | VBench：`motion_smoothness` | 运动是否连续、插帧预测与实际帧是否一致 |
| 提示词匹配 A | 20% | VideoScore2：text-to-video alignment，整数 1–5 | 主体、场景、动作、镜头是否符合生成提示词 |
| 物理与常识 P | 10% | VideoScore2：physical/common-sense consistency，整数 1–5 | 运动、接触、物体变化是否合理 |
| 审美 E | 5% | VBench：`aesthetic_quality` | 构图、色彩与整体视觉吸引力的模型预测 |

VideoScore2 提供上述三个学习型评分维度；它需要视频及对应生成提示词。[官方模型与说明](https://github.com/TIGER-AI-Lab/VideoScore2)

VBench 的自定义视频模式支持主体一致性、运动平滑度、审美等维度，适合评估现有 MP4。本标准采用其中四项：三项计分，加 `dynamic_degree` 作为诊断。[官方自定义视频说明](https://github.com/Vchitect/VBench#new-evaluate-your-own-videos)

这些权重是本项目的初始选择，**综合指数不是已经经过人类评分校准的 MOS，也不是官方 VBench 总分**。首帧、跨帧和整段画面分别保留分数；VideoScore2 的画面评分与运动指标可能存在相关性，后续应检查重复计权。

## 2. 固定分数换算

所有计分项转换为 0–100，保留转换前的数值。

### 首帧

```text
R = 100 × clamp(ssim_luma, 0, 1)
```

沿用已有九组实验的口径：首个解码帧、BT.709 亮度、11×11 均匀窗口、Lanczos、`fit=cover`、最长边 480。画布尺寸由视频画幅决定，因此不同宽高比的结果仍包含裁切差异；报告必须保存实际画布和宽高比变化，不能把差异全部归因于模型。

R 是结构保真分。R=70 不表示主观画质为 70 分，也不表示损失了 30% 的全部视觉信息。

### VideoScore2

本版采用输出文本中的 **1–5 整数等级**：

```text
V = 25 × (visual_quality_grade − 1)
A = 25 × (text_alignment_grade − 1)
P = 25 × (physical_consistency_grade − 1)
```

等级 1、2、3、4、5 对应 0、25、50、75、100。解析失败、范围错误时记录 `failed`，不能补为 0。

为提高复现性，本版实现时固定 `do_sample=false`、抽帧参数、评审提示词、模型权重和推理精度。此处采用项目定义的等级换算；官方示例还计算带 token 概率的分数，该值不能直接当作 1–5 等级套用上述公式。项目结果需明确标注评分协议，与官方随机采样示例区分。[官方推理实现](https://github.com/TIGER-AI-Lab/VideoScore2/blob/main/vs2_inference.py)

### VBench

```text
T = 100 × clamp(subject_consistency, 0, 1)
M = 100 × clamp(motion_smoothness, 0, 1)
E = 100 × clamp(aesthetic_quality, 0, 1)
```

当前官方实现的主体一致性使用截断负值的 DINO 余弦相似度；运动分采用归一化插帧误差；审美输出已除以 10。读取这些维度的**每视频原始结果**，不要重复套用排行榜归一化。[主体实现](https://github.com/Vchitect/VBench/blob/master/vbench/subject_consistency.py)、[运动实现](https://github.com/Vchitect/VBench/blob/master/vbench/motion_smoothness.py)、[审美实现](https://github.com/Vchitect/VBench/blob/master/vbench/aesthetic_quality.py)

审美线性预测器不保证每次都落在 0–1；超出范围时保留原值，记录裁剪标志。所有维度拒绝 NaN / Infinity。

### 综合指数

```text
Q_visual = 0.20R + 0.20V + 0.15T + 0.10M + 0.20A + 0.10P + 0.05E
```

计算条件：技术检查通过，七项计分均成功，使用同一评分配置和模型版本。

- 任一必需模型未安装、失败或提示词缺失：`Q_visual = null`，报告列出缺项。
- 不按每个视频单独重分配权重；不把缺项补为 0。
- 不使用“本批最高=100、最低=0”的归一化；加入一个视频不能改变其他视频的分数。
- 第一版不设置“80 分优秀”等合格线；先积累样本，再固定阈值和校准版本。

## 3. 运动与一致性的防误判规则

1. `dynamic_degree` 只报告运动量，不直接加分。微动作、人像静镜和奔跑视频应分别评价；运动越大不代表质量越高。
2. 运动平滑度高可能来自几乎静止。报告同时展示动态程度和提示词匹配，判断是否完成了要求的动作。
3. DINO 主体一致性是内容表征指标，不能单独证明人物脸部身份一致；人物身份保持可另加人脸或主体区域特征指标。
4. `background_consistency` 作为诊断项。运镜、遮挡或背景变化有时符合提示词，不自动扣分。
5. 切镜视频不适用本版的全片一致性口径，应采用另一个配置，在各镜头内计算，再单独检查切镜是否符合提示词。
6. 不直接把相邻帧差值当作闪烁质量分。需要单独开发闪烁指标时，先处理切镜、运动补偿及遮挡；VBench 原始闪烁维度也不能直接套入任意运动视频。

## 4. 技术完整性检查

计分前用 `ffprobe` 及 FFmpeg 完整解码进行自动检查。

| 检查 | 处理 |
| --- | --- |
| 文件存在、包含视频流、能够完整解码 | 失败则本次评分无效，综合指数为 null |
| 尺寸、帧率、时长符合任务声明 | 不符合则记录失败；容差与允许尺寸由该任务的 manifest 指定 |
| 存在要求的音轨、音轨可解码 | 当任务要求音频时为必需检查 |
| 黑帧、冻结段、重复帧、音频静音 | 输出时间段和比例；结合提示词判断，默认不自动判定为坏视频 |

“720p 档”不可直接当作严格的 720×1280：前轮工作流实际输出还包括 736×1280、736×1312。manifest 应保存真实的预期规格。

## 5. 抽帧与可复现性

| 用途 | 规则 |
| --- | --- |
| 首帧 SSIM | 第一个有效解码帧；不使用视频缩略图 |
| VideoScore2 | 从 2 fps 的固定采样口径开始，记录实际帧索引、时间戳和处理器尺寸参数；短暂异常由密集指标补充 |
| VBench | 使用固定版本的官方逐维度预处理和采样；保存实际参数，不能对所有算法统一预先抽 16 帧 |
| 技术检查 | 全片完整解码；记录帧数、时长、帧率、音视频流 |

每次评分必须保存：视频/参考图/提示词 SHA-256、任务 ID、评分配置哈希、评审提示词全文、模型名及 revision、权重哈希、依赖版本、设备与精度、实际采样记录、原始输出和解析状态。

缓存以“输入哈希 + 配置哈希 + 模型版本”为键。使用冻结版本重新评分时，可以复用符合该键的结果；只按任务 ID 缓存会遗漏文件或配置变化。

同一配置下比较生成参数，应增加不同生成 seed 的重复样本，并报告均值、标准差。固定一次评审不能消除生成视频本身的随机性。

## 6. 质量耗时比

保留现有首帧指标：

```text
QTE_reference_per_second = clamp(SSIM, 0, 1)² / 平台生成秒数
QTE_reference_per_minute = 60 × QTE_reference_per_second
```

增加整段视觉指标，避免把百分制直接平方后与 SSIM 混用：

```text
QTE_visual_per_second = (Q_visual / 100)² / 平台生成秒数
QTE_visual_per_minute = 60 × QTE_visual_per_second
```

平台生成耗时不含本地排队与评分耗时。评分耗时另存 `evaluation_seconds`。二采从头比较时将一采与二采生成时间相加；评估已有 480p 视频的升级成本时另列二采阶段耗时，明确比较场景。不同硬件/平台实例需分组比较。

任一 QTE 的耗时缺失、非有限或不大于 0，该 QTE 为 null。没有 Q_visual 时不计算 QTE_visual。

## 7. 扩展项

| 项目 | 自动方法 | 本版处理 |
| --- | --- | --- |
| 感知保真 | 首帧 LPIPS / DISTS；参考主体与视频主体特征 | 保存原值作为诊断，后续校准后纳入另一个配置；不直接使用 `100×(1−LPIPS)` |
| 清晰度与技术画质 | MUSIQ 或 DOVER technical 分支 | 辅助区分“参考图接近”和“画面更好”；避免与 V 重复计权 |
| 视频审美交叉检查 | DOVER aesthetic 分支 | 辅助诊断；UGC 数据集排名不解释为通用画质百分比 |
| 对白与字幕 | ASR 文本匹配、OCR、语言检测 | 仅在提示词要求时运行 |
| 唇音同步 | 专项 AV 同步模型 | 有可检测说话人时运行；不从视频帧或 ASR 单独推断 |
| 音频质量与音画对应 | 音频质量模型、音频事件匹配、AV 对应模型 | 另建 H3 音视频配置，增加固定权重；本版 Q_visual 不代表音频质量 |

[IQA-PyTorch 模型与指标方向](https://github.com/chaofengc/IQA-PyTorch/blob/main/docs/ModelCard.md)、[DOVER 官方说明](https://github.com/VQAssessment/DOVER)

音频扩展后应输出 `Q_audiovisual`，保留 Q_visual。不能根据某条视频是否有音轨临时改变其他视频的计分权重。

## 8. 自动程序的数据与流程

```text
任务 manifest
  → 全片技术检查
  → 首帧 SSIM
  → VideoScore2 三项等级
  → VBench 三项分数与运动量诊断
  → 检查完整性、按固定规则换算
  → 输出 JSON / CSV / Markdown 排名与异常清单
```

manifest 输入字段：

```json
{
  "task_id": "task_xxx",
  "video_path": "/absolute/path/video.mp4",
  "reference_path": "/absolute/path/reference.png",
  "prompt_path": "/absolute/path/generation_prompt.txt",
  "platform_generation_seconds": 339,
  "source_task_id": null,
  "pipeline_generation_seconds": 339,
  "expected_video": {
    "allowed_sizes": [[480, 864]],
    "fps": 24,
    "duration_seconds": 10.125,
    "requires_audio": true
  }
}
```

JSON 结果应包含各项 `raw`、`score_100`、`status`、`model_revision`、技术检查、异常时间段、Q_visual 与两种 QTE。状态使用 `ok`、`not_run`、`not_applicable`、`failed`；本配置的必需项出现后三种状态时，综合指数为 null。

首帧计算可以直接复用已有程序：

```bash
python3 /Users/apple/Documents/github/rh-workflow-desk/scripts/measure_first_frame_fidelity.py \
  /Users/apple/Documents/VideoMake/测试/附件/lora_ab_reference_20261002.png \
  /Users/apple/Documents/VideoMake/测试/视频/task_982b909391ee/output_1.mp4 \
  --fit cover --max-side 480
```

深度模型部分优先部署到独立的 GPU 评估环境，锁定依赖和权重。VideoScore2 官方推理示例使用 CUDA；本机 macOS 上直接运行该示例并不可行，MPS / CPU 适配需要另外验证。评分阶段只读取已生成的视频，不提交新的生成任务。

## 9. 前轮实验如何接入

输入视频与原始结果见 [[测试/10Eros_H3_九组工作流对比_20261002]]。比较九组时统一使用本配置、同一原始生成提示词与参考图。

最终对比表建议使用：

| 任务 | 配置/步数 | R | V | T | M | A | P | E | Q_visual | 平台秒数 | QTE_reference/分钟 | QTE_visual/分钟 | 异常 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

只有全部模型实际运行成功后填写整段评分与排名。现有 SSIM 结果可以作为 R 接入，不能据此提前确定哪组的整段质量最好。
