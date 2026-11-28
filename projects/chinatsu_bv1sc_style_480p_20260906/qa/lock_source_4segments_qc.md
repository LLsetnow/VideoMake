# Lock-source four-segment QC

## RH runs

| Segment | Local task | Remote task | Status |
| --- | --- | --- | --- |
| 01 · 00:00–00:02 | `task_1b87a737f49d` | `2096337602871881729` | completed |
| 02 · 00:02–00:04 | `task_2bc55bbbc267` | `2096338429640183809` | completed |
| 03 · 00:04–00:06 | `task_57e2b70418f3` | `2096338428533207041` | completed |
| 04 · 00:06–00:08 | `task_76b4a164791e` | `2096341019734863874` | completed |

All four final workflows use remote workflow `2094755110367227906`, `task_type=Ref2VA`, `audio_mode=lock_source`, three picture inputs (literal first frame, literal last frame, face identity), one derived depth+DWPose video, and the matching source-audio cut.

## Final assembly

- Delivery: `output/chinatsu_bv1sc_4segments_lock_source_480p.mp4`
- Video: H.264, 480×864, 24 fps, 267 frames
- Audio: AAC, 48 kHz, stereo
- Duration: 11.125000 seconds
- Visual timeline: 00:00 gray opening; 00:02 coral/aqua/pink; 00:04 blue/red denim; 00:06 yellow/blue/brown; 00:08 blue/green/brown; 00:08–00:11.125 held on the final wardrobe.
- Audio: the four source cuts are concatenated continuously from the downloaded reference video's audio; no newly generated music or voice is used.
- Full decode: passed with `ffmpeg -f null -`.
- Visual evidence: `final_keyframes_0_2_4_6_8_10s.png`.

The fourth RH segment is exactly 00:06–00:08 for a strict last-frame landing. Its generated last frame is held locally for the remaining 3.125 seconds so the 00:08 wardrobe node and the full 11.125-second duration both remain exact.

## Rotation-prompt rerun

The first visual review found that seg01/03/04 described the turn too weakly, allowing a mostly static wardrobe morph. The prompts were strengthened to require continuous full-body yaw with coordinated feet, hips, waist, shoulders, arms, and legs, and to forbid a static clothing morph. The seg04 prompt also explicitly resolves the direction mismatch between its control clip and literal boundary frames by prioritising Picture 1 → Picture 2.

| Segment | New local task | New remote task | Status |
| --- | --- | --- | --- |
| 01 · 00:00–00:02 | `task_571f484f2089` | `2096345665698295810` | completed |
| 03 · 00:04–00:06 | `task_28d4d522acec` | `2096345664406450178` | completed |
| 04 · 00:06–00:08 | `task_5eedf1eac943` | `2096345673354186753` | completed |

New delivery: `output/chinatsu_bv1sc_4segments_lock_source_480p_rotation_rerun.mp4`.

- Video: H.264, 480×864, 24 fps, 267 frames
- Audio: AAC, 48 kHz, stereo; source audio retained continuously
- Duration: 11.125000 seconds
- Full decode: passed with `ffmpeg -f null -`

## Front-facing tail correction

The previous regenerated tail reference was incorrectly rear-facing. The actual reference-video tail was rechecked and is front-facing/near-front. A new tail reference was generated from the reference-video tail pose, full control-video tail, Chinatsu face identity, and the blue-green-brown wardrobe reference. The prompt now explicitly forbids a back-facing or rear three-quarter final pose.

- Corrected tail reference: `02_character_refs/chinatsu_key_08_blue_green_brown_front_tail_v3.png`
- Reference evidence: `05_segments/control/reference_video_tail_11.125.png`
- Local task: `task_e95651fa5f7b`
- Remote task: `2096355043324465153`
- Seg04 output: `output/rerun_segments/seg04_front_tail/task_e95651fa5f7b/output_1.mp4`
- Tail motion evidence: `front_tail_final/tail_motion_contact.jpg`
- Final delivery: `output/chinatsu_bv1sc_4segments_lock_source_480p_front_tail_final.mp4`
- Video: H.264, 480×864, 24 fps, 267 frames
- Audio: AAC, 48 kHz, stereo; duration 11.125000 seconds
- Full decode: passed with `ffmpeg -f null -`
- Boundary check: verified at 00:00/02/04/06/08/10; contact sheet: `final_rerun_keyframes_verified.jpg`
- Motion check: `diagnosis/seg01_rerun_contact_8x1.png`, `diagnosis/seg03_rerun_contact_8x1.png`, `diagnosis/seg04_rerun_contact_8x1.png`

## Continuous seg04 tail rerun

The previous assembly held the seg04 last frame after 00:08.000. To remove the static tail and prevent human/control-video leakage, a new literal tail-frame reference was generated from the 00:11.125 control-video tail pose plus the Chinatsu face identity reference, with the blue-green-brown wardrobe retained. Seg04 was then regenerated continuously for the full 00:06.000–00:11.125 interval.

- Tail reference: `02_character_refs/chinatsu_key_08_blue_green_brown_tail_v2.png`
- Local task: `task_f01847597481`
- Remote task: `2096351316797321217`
- Workflow: `05_segments/workflows/seg04_6.000-11.125_rotation_rerun_workflow_api.json`
- Prompt group: `05_segments/prompt_groups/seg04_rotation_rerun_6.000-11.125_prompt_group.json`
- Seg04 output: `output/rerun_segments/seg04_long/task_f01847597481/output_1.mp4`
- Tail motion evidence: `continuous_seg04/tail_motion_contact.jpg`
- Final delivery: `output/chinatsu_bv1sc_4segments_lock_source_480p_continuous_seg04.mp4`
- Video: H.264, 480×864, 24 fps, 267 frames
- Audio: AAC, 48 kHz, stereo; duration 11.125000 seconds
- Full decode: passed with `ffmpeg -f null -`
