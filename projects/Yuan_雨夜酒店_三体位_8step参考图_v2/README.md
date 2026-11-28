# Yuan 雨夜酒店 · 三体位 8-step 参考图（第二组深度参考）

从 `ref/pose/depth/` 另选三种体位，制作 16:9、1280×720 的双人写实参考图，用于后续关键帧与视频生成讨论。两名参与者均为明确自愿的成年人。

文中的 `ref/...` 均为仓库根目录 `VideoMake/` 下的相对路径。

## 最终选图

| 体位 | 文件 | Seed | 深度参考 |
| --- | --- | --- | --- |
| 女上位（床侧三分之四） | `output/yuan_rain_hotel_cowgirl_front_8step_v7.png` | 20261183 | `ref/pose/depth/猫娘女上位-手捂嘴_竖图_实拍_depth.png`（仅取体位意图） |
| 床边跪姿口交（侧面） | `output/yuan_rain_hotel_oral_side_8step_v4.png` | 20261162 | `ref/pose/depth/跪姿口交-站立男性_侧面_竖图_depth.png` |
| 传教士式（床侧三分之四） | `output/yuan_rain_hotel_missionary_side_8step_v6.png` | 20261181 | `ref/pose/depth/传教士式性交-毛绒连体衣_横图_depth.png`（仅取体位意图） |

三联对比图：`output/yuan_rain_hotel_three_poses_v2_8step_contact_sheet.jpg`

## 生成参数

- 模型：`Qwen-Image-Edit-2511`（`qwen_image_ablitrated_v1.6_fp8_scaled`）+ `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16` LoRA
- 采样：8 steps，cfg 1.0，euler，simple，1280×720
- 模板：`../Yuan_雨夜酒店_双人关键帧_Qwen2511/v3_8step_workflow_api.json`
- 角色参考：`refs/yuan_identity.png`（Yuan，深棕高马尾、直刘海、深色杏眼、白皙肤色）
- 场景：雨夜酒店客房、白色床单、琥珀床头灯、冷蓝窗光、深绿缎面吊带睡裙、同一男性伴侣

## 深度参考的使用说明

局部姿态图对多人性行为的肢体遮挡本来就含糊，Qwen 2511 在严格继承这些灰度图时会出现两类问题：

1. 竖构图近景深度图直接决定裁切，导致 Yuan 头顶被切掉（女上位参考图本身只有颈以下）；
2. 灰度肢体轮廓被当成实体，产生玩偶关节、接缝或多余脚。

因此：

- 口交图（`oral_side_v4`）严格来自深度参考；它是在 `oral_side_v2` 基础上做了一次只改发型的 8-step 编辑，姿态、构图、光线未变。
- 女上位与传教士式最终版改为「身份参考 + 文本」重新构图，保持体位语义与场景连续性，但不再逐像素贴合原深度图。若必须严格锁深度，需要接受竖裁或改用其它姿态控制方式。

所有中间尝试都保留在 `output/`，未覆盖旧图，提交记录见 `qa/submissions.json`。

## 复现

```bash
python3 scripts/generate_8step.py <slug> \
  --prompt-file prompts/<slug>.txt \
  --seed <seed> \
  --depth <comfyui-input-filename> \
  --output-name <output.png>
```

加 `--identity-only` 时只用身份图、不接深度图（对应本轮女上位/传教士式的最终版）。
