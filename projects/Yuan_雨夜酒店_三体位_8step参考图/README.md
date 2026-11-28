# Yuan 雨夜酒店三体位 8 step 参考图

使用 `Qwen-Image-Edit-2511`、8 步、1280×720，把三张不同体位的深度图与 Yuan 身份图合成为同一间雨夜酒店客房中的写实关键帧。

## 最终选用

| 顺序 | 体位 | 输出 | 深度参考 | 种子 |
| --- | --- | --- | --- | --- |
| 1 | 床边侧后入·单腿抬高 | `output/yuan_rain_hotel_standing_8step.png` | `refs/pose_standing_depth.png` | 20261128 |
| 2 | 传教士 M 字抬腿 | `output/yuan_rain_hotel_missionary_m_8step.png` | `refs/pose_missionary_m_depth.png` | 20261125 |
| 3 | 女上位跪姿 | `output/yuan_rain_hotel_cowgirl_8step.png` | `refs/pose_cowgirl_depth.png` | 20261126 |

三合一预览：`output/yuan_rain_hotel_three_poses_8step_contact_sheet.jpg`

## 生成参数

- 模型：`Qwen-Image-Edit-2511`
- 采样：`euler` / `simple` / `cfg 1.0`
- 步数：`8`
- 尺寸：`1280×720`
- 身份参考：`refs/yuan_identity.png`
- 工作流：`workflows/*.json`
- 提示词：`prompts/*.txt`
- 输出清单：`pose_references.final.json`

## 未采用

后入跪姿深度图 `ref/pose/depth/后入式性交-跪姿前倾_正面_横图_depth.png` 的两版结果都出现男性大腿比例失真，已保留为对照，不纳入最终参考组：

- `output/yuan_rain_hotel_doggy_8step.png`
- `output/yuan_rain_hotel_doggy_v2_8step.png`
