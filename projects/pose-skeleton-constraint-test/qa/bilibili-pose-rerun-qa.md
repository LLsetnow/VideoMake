# Bilibili 动作帧约束独立版 QA

## 输入与动作约束

- Bilibili source: `analysis/bilibili_reference/source/bilibili_action_reference.mp4`
- Source probe: 720×1280，约 25fps，10.021 秒；仅用于抽帧分析。
- Selected frames: 00:02.750、00:04.250、00:05.500、00:07.750、00:09.250。
- DWPose outputs: `analysis/bilibili_reference/skeleton/shot1_t2.75_skeleton.png` through `shot5_t9.25_skeleton.png`。
- H3 input policy: workflow loads the five generated skeleton PNGs, not the Bilibili video or source frames；prompt excludes performer identity、服装、场景、道具、UI 和水印。

## 480p 初采

- Local task: `task_eef550186392`
- Remote task: `2096246157351645186`
- Status: completed；cost 29 coins；remote duration 144 seconds。
- Raw: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/task_eef550186392/output_1.mp4`
- Raw probe: 480×864，24fps，361 frames，15.075 seconds，AAC stereo。
- Delivery derivative: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/chinatsu_showcase_480p_bilibili_pose_final.mp4`
- Delivery probe: 480×864，24fps，360 frames，15.000 seconds，AAC 48kHz stereo。
- Visual QA: 五个采样节点呈现站立、跪坐双手、站立展示、近景抬手、单膝坐姿；千夏脸部与服装连续；浅色背景干净；未见骨骼线、关键点、源视频场景或水印。

## 720p 上采样

- Local task: `task_800c68a1c003`
- Remote task: `2096247616998797313`
- Status: completed；cost 80 coins；remote duration 399 seconds。
- Raw: `output/chinatsu-showcase-720p-bilibili-pose-upscale/task_800c68a1c003/output_1.mp4`（768×1376，362 frames，15.083 seconds）。
- Final: `output/chinatsu-showcase-720p-bilibili-pose-upscale/chinatsu_showcase_720p_bilibili_pose_final.mp4`
- Final probe: 720×1280，24fps，360 frames，15.000 seconds，AAC 48kHz stereo。
- SHA-256: `963d920ba6f2ce3b8483c07735c83c7fb85cf0d1fec60fe094bce3eb36408310`
- Visual QA: 720p 接触表中五个动作和面部一致性保持；画面无可见骨骼叠加；可读性正常。
- Output link: `videoOutput/chinatsu-showcase-720p-bilibili-pose.mp4`

## Reproduction snapshots

- 480p workflow snapshot: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/task_eef550186392/workflow_api.json`
- 480p prompt group snapshot: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/task_eef550186392/prompt_group.json`
- 480p manifest: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/task_eef550186392/manifest.json`
- 720p workflow snapshot: `output/chinatsu-showcase-720p-bilibili-pose-upscale/task_800c68a1c003/workflow_api.json`
- 720p prompt group snapshot: `output/chinatsu-showcase-720p-bilibili-pose-upscale/task_800c68a1c003/prompt_group.json`
- 720p manifest: `output/chinatsu-showcase-720p-bilibili-pose-upscale/task_800c68a1c003/manifest.json`
