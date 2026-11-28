# H3 skeleton pose-constraint test

## Test setup

- Mode: `Ref2VA`
- Duration: 5 seconds; 24 FPS; 124 frames (`17n+5`)
- Canvas: 9:16, 0.9 MP target
- Audio: H3 native audio
- `Picture 1` / `37:image`: `ref/pose/color/站立-一手抬至脸侧_正面_竖图.jpg`
- `Picture 2` / `54:image`: `ref/pose/skeleton/站立-一手抬至脸侧_正面_竖图_skeleton.png`
- Prompt: `36:prompt`

## Submission record

- Submission path: RH_CLI local Web API, `POST /api/tasks`
- Local task: `task_135a4811096a`
- Remote workflow: `2094755110367227906`
- Remote task: `2095930393104748546`
- Result: completed; one MP4 downloaded
- Remote duration: 143 seconds
- Recorded cost: 29 RH coins

## QA conclusion

The generated subject follows the skeleton-defined configuration across the opening, middle, and final sampled frames: the raised hand stays beside the face, the opposite arm stays bent outward, the torso remains upright, and the shoulder/hip and leg directions remain stable.

The result is not yet a clean pose-control output. The colored skeleton lines and keypoint dots are visibly rendered over the subject in all sampled frames. This indicates that the current H3 `Ref2VA` multi-picture route uses the skeleton image as a visual reference that can influence pose, but does not provide a hidden pose-conditioning channel for this input. A later clean-output version needs a dedicated pose/control input in the remote workflow, or a pre/post-processing route that prevents the skeleton artwork from being treated as visible reference content.

Output: `output/task_135a4811096a/output_1.mp4`

## Cross-character transfer test

The second test uses the independent full-body character sheet `ref/character/千夏/千夏-全身三视图-方形-v2.png` as `Picture 1` and the same skeleton map as `Picture 2`. It was submitted through the same RH_CLI local Web API route.

- Workflow: `character-pose-transfer_workflow_api.json`
- Local task: `task_19d5a8310677`
- Remote task: `2095933213122785281`
- Result: completed; one MP4 downloaded
- Remote duration: 154 seconds
- Recorded cost: 31 RH coins
- Output: `output/task_19d5a8310677/output_1.mp4`

This cross-character test preserves the anime character's face, silver-gray hair, turquoise bow, costume, wings, and accessories from the full-body sheet while reproducing the skeleton pose. The pose transfer is successful, but the skeleton lines and keypoints are still visibly overlaid on the character, confirming that the current Ref2VA image-reference channel is not a hidden pose-control channel.

## Special-pose transfer test

The third test keeps the same full-body character sheet as `Picture 1` and replaces `Picture 2` with the distinctive seated pose `ref/pose/skeleton/坐姿-双腿抬起外展_正面_竖图_skeleton.png`: torso centered, both legs bent and lifted toward the camera, knees spread outward, shoe soles facing forward, and both hands raised near the shoulders.

- Workflow: `special-pose-transfer_workflow_api.json`
- Local task: `task_2e220fc727fe`
- Remote task: `2095935105304948738`
- Result: completed; one MP4 downloaded
- Remote duration: 91 seconds
- Recorded cost: 19 RH coins
- Output: `output/task_2e220fc727fe/output_1.mp4`

The special pose is reproduced clearly from the opening through the final sampled frame: the character remains seated with both legs raised and splayed toward the camera, while the hands stay lifted near the shoulders. No colored skeleton lines or keypoint dots are visible in the generated frames. This confirms that this prompt/reference combination can constrain a markedly non-standing pose while preserving the character identity and costume.

## Chinatsu showcase: 15 seconds, vertical, 480p

This version turns the Chinatsu character sheet and five reusable skeleton pose references into a clean vertical showcase. The requested Bilibili reference is used for pacing and cute pose energy only; it is not submitted as an H3 input. The music is the first 15 seconds of the selected NetEase Cloud Music track, submitted as locked source audio.

- Format: 9:16 portrait, 480x864, 24 FPS, 15.000 seconds
- Structure: five shots, with planned transitions at 3.797, 6.613, 9.824, and 12.064 seconds
- Workflow: `chinatsu-showcase-15s-480p-lock-source_workflow_api.json`
- Prompt: `chinatsu-showcase-15s-480p-lock-source_prompt.txt`
- Chinese shot plan: `shots/chinatsu-showcase-15s-480p-shot-plan.md`
- Local task: `task_9118c41911ef`
- Raw H3 output: `output/chinatsu-showcase-15s-480p-lock-source/task_9118c41911ef/output_1.mp4`
- Final trimmed delivery: `output/chinatsu-showcase-15s-480p-lock-source/chinatsu_showcase_480p_final.mp4`

QA confirms a readable H.264/AAC MP4, consistent character identity, clean pale background, the intended standing-to-seated action progression, and no visible skeleton lines or keypoint dots. The raw H3 container was 15.075 seconds; the final delivery derivative is trimmed to exactly 15.000 seconds.

## Chinatsu showcase: face-reference rerun

This rerun adds `ref/character/千夏/千夏_正脸头像_v4.png` as `Picture 7`, used only for face, eyes, bangs, earrings, bow silhouette, hairstyle, and facial-proportion consistency. The original character sheet remains the whole-body identity reference and the five skeleton maps remain hidden pose references.

- Format: 9:16 portrait, 480x864, 24 FPS, 15.000 seconds
- Workflow: `chinatsu-showcase-15s-480p-face-ref-lock-source_workflow_api.json`
- Prompt: `chinatsu-showcase-15s-480p-face-ref-lock-source_prompt.txt` (6993 characters)
- Chinese translation: `chinatsu-showcase-15s-480p-face-ref-lock-source_prompt_zh.txt`
- Face reference: `ref/character/千夏/千夏_正脸头像_v4.png`
- Local task: `task_aed27a743a8b`
- Raw H3 output: `output/chinatsu-showcase-15s-480p-face-ref-lock-source/task_aed27a743a8b/output_1.mp4`
- Final trimmed delivery: `output/chinatsu-showcase-15s-480p-face-ref-lock-source/chinatsu_showcase_480p_face_ref_final.mp4`

The face-reference rerun completed successfully. Contact-sheet QA shows consistent Chinatsu identity, clean pale background, the same five-shot progression, and no visible skeleton lines or keypoint dots. The raw H3 container was 15.075 seconds; the final delivery derivative is trimmed to exactly 15.000 seconds.

## Chinatsu showcase: 720p upscale

The reviewed face-reference-enhanced 480p delivery was passed through the shared H3 3D latent upscaling workflow. The source video, action timing, five-shot structure, and locked music were preserved; the H3 upscale was then normalized to the requested exact 720×1280 portrait canvas.

- Source: `output/chinatsu-showcase-15s-480p-face-ref-lock-source/chinatsu_showcase_480p_face_ref_final.mp4`
- Workflow: `chinatsu-showcase-720p-upscale_workflow_api.json`
- Local task: `task_db7cd0655a9b`
- Raw H3 upscale: `output/chinatsu-showcase-720p-upscale/task_db7cd0655a9b/output_1.mp4` (768×1376, 15.083 seconds)
- Final delivery: `output/chinatsu-showcase-720p-upscale/chinatsu_showcase_720p_final.mp4` (720×1280, 15.000 seconds)

QA confirms 360 frames at 24 FPS, stereo AAC audio, readable playback, preserved pale background and character details, and no visible skeleton lines or keypoint dots.

## Bilibili scheduled publication

- Video: `output/chinatsu-showcase-720p-upscale/chinatsu_showcase_720p_final.mp4`
- Bilibili BV: `BV11ytC6uE1E`
- Title: `SCARED LONELY FUNK`
- Tags: `SCARED LONELY FUNK,千夏,二次元,角色展示,可爱动作,AI动画,AIGC,竖屏短视频`
- Category: `47`（动画 / 同人·手书）
- Scheduled time: `2026-09-05 12:11`（Asia/Shanghai）
- Platform status: `通过审核，等待发布`
- Cover: `output/chinatsu-showcase-720p-upscale/cover_bilibili.png`

## Chinatsu showcase: Bilibili action-frame-constrained independent rerun

This independent version responds to the pose-source correction: it downloads the Bilibili video as analysis material, extracts five selected action frames, generates DWPose skeletons from those frames, and uses the generated skeleton PNGs as the five pose references. The original Bilibili performer, face, clothing, room, props, source frames, UI, and watermark are explicitly excluded from the H3 prompt and workflow input. The face reference and locked source music remain unchanged.

- Bilibili analysis evidence: `analysis/bilibili_reference/`
- English prompt: `chinatsu-showcase-15s-bilibili-pose-lock-source_prompt.txt` (6999 characters)
- Chinese translation: `chinatsu-showcase-15s-bilibili-pose-lock-source_prompt_zh.txt`
- Five-shot plan: `shots/chinatsu-showcase-15s-bilibili-pose-shot-plan.md`
- 480p workflow: `chinatsu-showcase-15s-bilibili-pose-lock-source_workflow_api.json`
- 480p output: `output/chinatsu-showcase-15s-bilibili-pose-lock-source/chinatsu_showcase_480p_bilibili_pose_final.mp4`
- 480p task: `task_eef550186392` / remote `2096246157351645186`
- 720p upscale workflow: `chinatsu-showcase-720p-bilibili-pose-upscale_workflow_api.json`
- 720p output: `output/chinatsu-showcase-720p-bilibili-pose-upscale/chinatsu_showcase_720p_bilibili_pose_final.mp4`
- 720p task: `task_800c68a1c003` / remote `2096247616998797313`
- QA record: `qa/bilibili-pose-rerun-qa.md`
- `videoOutput` link: `videoOutput/chinatsu-showcase-720p-bilibili-pose.mp4`

## Chinatsu showcase: Bilibili depth + skeleton reference video rerun

This independent rerun follows the documented 8.7 motion-transfer route. The Bilibili source is normalized to 24 FPS; every frame receives an 8-bit grayscale Depth Anything V2 map and a same-frame RGB DWPose skeleton, then the paired maps are blended into one silent Video input. The H3 workflow connects that derived Video to `ref_videos.ref_video_0`; it does not use the earlier five static skeleton PNGs as Picture inputs. The face reference and locked source music remain active. The first full-resolution control-video attempt hit remote VRAM OOM, so the same per-frame control data was resized to 480x864 for the successful retry. No 720p upscale was requested for this version.

- English prompt: `chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source_prompt.txt`
- Chinese translation: `chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source_prompt_zh.txt`
- Five-beat shot plan: `shots/chinatsu-showcase-15s-bilibili-depth-skeleton-shot-plan.md`
- Derived control Video: `analysis/bilibili_depth_skeleton_8_7/reference_480p/bilibili_depth_skeleton_reference_480p_24fps.mp4`
- 480p workflow: `chinatsu-showcase-15s-bilibili-depth-skeleton-lock-source-retry480_workflow_api.json`
- Successful local task: `task_fccfe6918a47` / remote `2096260614453227521`
- Raw output: `output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/task_fccfe6918a47/output_1.mp4`
- Final delivery: `output/chinatsu-showcase-15s-bilibili-depth-skeleton-video-480p-retry/chinatsu_showcase_480p_bilibili_depth_skeleton_final.mp4`
- Final format: 480x864, 9:16, 24 FPS, 360 video frames, 15.000-second video stream, AAC 48kHz stereo locked source audio
- QA record: `qa/bilibili-depth-skeleton-video-rerun-qa.md`
- `videoOutput` link: `videoOutput/chinatsu-showcase-480p-bilibili-depth-skeleton.mp4`

### 8.7 尺寸预处理约定

后续动作迁移应保留原始 Bilibili 视频作为只读来源，但先按 H3 目标尺寸制作 24fps 工作副本，再抽帧生成深度图和骨骼图，最后合成控制 Video。这样能减少逐帧 I/O、后处理、编码/上传体积和 H3 参考 Video 的显存占用；由于当前 Depth Anything 与 DWPose 包装器分别使用固定的 518×392 与 512 检测尺寸，模型前向耗时不会严格按像素比例下降。当前 480p 项目的控制尺寸为 480×864。详见 `qa/bilibili-depth-skeleton-video-rerun-qa.md` 和全局流程文档 8.7.1。
