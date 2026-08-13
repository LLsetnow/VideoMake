---
name: beat-locked-redundant-video-edit
description: Build frame-accurate beat-synced video edits from generated videos treated as a redundant asset pool. Use when editing AI-generated MP4s to a locked source track, detecting source shot boundaries, matching 2–3 second beat/onset intervals, hard-cutting at the verified project frame rate, remuxing the original audio, and validating exact frame counts.
---

# Beat-Locked Redundant Video Edit

## Operating contract

Treat generated video as visual source material, not as the authoritative edit. Let the locked source audio define the master timeline, let beat/onset analysis define target boundaries, and perform final cuts in post-production at integer video frames.

Preserve these invariants:

- Discard generated-video audio from the edit and remux the original source audio at the end.
- Do not use H3 `[Shot]` timestamps or model-created transitions as final cut points.
- Treat source scene changes as exclusion information and keep a guard band around detected transitions.
- Do not force every beat into a cut; choose strong beats/onsets with roughly 2–3 second spacing.
- Do not create one generation workflow per short shot. Reuse existing renders as a redundant pool.
- Do not claim exact timing until per-segment frame counts and final `ffprobe` output pass.

## Workflow

### 1. Inspect and scope

Identify the source audio, all generated MP4 candidates, verified FPS, dimensions, and duration. Exclude derived final videos, QA transcodes, and duplicate outputs from the source pool unless explicitly requested. Group primary renders and legacy/backup renders so fallback assets remain traceable.

Keep the source audio as the only master clock. If the project uses `lock_source`, retain that mode in timeline metadata.

### 2. Detect source scenes and create the asset manifest

Prefer FFmpeg's `scdet` filter when OpenCV/PySceneDetect is unavailable:

```bash
ffmpeg -hide_banner -loglevel error -i input.mp4 \
  -vf "scdet=threshold=0,metadata=print:key=lavfi.scd.score:file=scores.txt" \
  -an -f null -
```

Parse per-frame scores, find local maxima, and use a robust threshold such as:

```text
threshold = max(2.5, median + 8 × MAD, 98th percentile)
```

Merge peaks closer than 0.8 seconds, reject fragments shorter than 0.8 seconds, and record both raw and safe ranges. Treat a peak as a transition start, not as a perfect semantic boundary. Remove a small guard band around it (normally 6 frames at 24fps; increase for visibly gradual transitions).

Write `asset_manifest.csv` with at least:

- asset ID and source group
- absolute source path and prompt/reference path when available
- source FPS, dimensions, total frames, duration
- raw start/end frames and safe start/end frames
- safe duration, detector score/threshold, usability flag

Inspect a labeled contact sheet when the detector may have confused camera motion, lighting, or a gradual transition with a scene cut.

### 3. Build the beat master timeline

Use existing `opc audio librosa` output when present; otherwise run the project's approved audio analysis first. Select stronger beat/onset candidates and preserve natural paragraph endings. A workflow or generation-segment boundary is itself a visual cut, so it must land on an approved internal cut, not automatically at 15 seconds.

Convert every target boundary to the verified FPS before rendering:

```text
target_frame = round(target_time_seconds × fps)
actual_time = target_frame / fps
```

Use the same integer boundary for the end of one interval and the start of the next. This keeps the timeline gap-free and limits time quantization to at most half a frame.

### 4. Match redundant assets to target intervals

For each interval `[target_start_frame, target_end_frame)` choose a safe asset window with at least the required number of frames. Prefer coherent visual progression, avoid repeating the same source window back-to-back, and use legacy renders only as deliberate fallbacks. Reuse a long asset with a different safe source window when the pool has fewer unique long clips than target intervals.

Write `beat_locked_timeline.csv` containing target frame boundaries, requested and quantized times, asset ID, source frame window, reuse index, anchor type, and `audio_mode: lock_source`.

### 5. Render and remux

For each interval, use frame-based trimming rather than approximate timestamp seeking:

```text
trim=start_frame=SOURCE_IN:end_frame=SOURCE_OUT
setpts=PTS-STARTPTS
```

Normalize all segments to one verified format (for this project: 1280×720, 24fps, H.264, yuv420p), concatenate video-only segments, then remux the original audio. If source renders are 1280×736, center-crop to 1280×720 consistently before concatenation.

### 6. Verify before handoff

Verify every rendered interval has exactly the expected frame count. Verify the final file with `ffprobe`:

- video FPS equals the project FPS
- `nb_frames == round(duration × fps)`
- final duration equals the requested duration
- dimensions and pixel format are consistent
- audio comes from the locked source track
- no interval gaps, overlaps, or duplicated audio

Write a verification report and a contact sheet. Report frame-quantization error honestly; at 24fps it can be up to 20.8ms even when the edit is frame-accurate.

## Project resources

Use [manifest-and-timeline-schema.md](references/manifest-and-timeline-schema.md) when creating or reviewing CSV artifacts. Use [validate_beat_locked_timeline.py](scripts/validate_beat_locked_timeline.py) for a cheap gap/overlap/frame-count check before expensive media rendering.

For this VideoMake project, the working implementations are:

- `projects/情感失色症_60秒/analysis/detect_generated_assets.py`
- `projects/情感失色症_60秒/analysis/build_beat_locked_edit.py`

Adapt their paths and asset selection for another project; do not copy their project-specific asset IDs blindly.
