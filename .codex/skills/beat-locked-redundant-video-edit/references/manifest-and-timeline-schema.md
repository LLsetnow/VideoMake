# Manifest and timeline schema

## `asset_manifest.csv`

Keep one row per safe source fragment. Preserve both raw detector ranges and safe ranges so later edits can audit what was removed around a transition.

Required columns:

```text
asset_id
source_group
source_path
prompt_path
width,height,fps,source_total_frames,source_duration_sec
raw_start_frame,raw_end_frame_exclusive
safe_start_frame,safe_end_frame_exclusive,safe_duration_sec
cut_in_score,cut_out_score,detector_threshold,detector_confidence
usable_for_beat_edit
```

The safe range is the only range eligible for a beat-locked source window. Use half-open frame ranges: `[start_frame, end_frame_exclusive)`.

## `beat_locked_timeline.csv`

Keep one row per final visual interval:

```text
edit_index
requested_start_sec,requested_end_sec
global_start_sec,global_end_sec
target_start_frame,target_end_frame_exclusive,target_frames
anchor
asset_id,source_group,source_path
source_in_frame,source_out_frame_exclusive
source_in_sec,source_out_sec,source_window_sec
source_reuse_index
audio_mode
start_error_ms,end_error_ms
notes
```

The `global_*` fields are the quantized times derived from integer frames. The requested fields preserve the original beat/onset timestamps. Use the end frame of row `N` as the start frame of row `N+1`.

## Matching pseudocode

```text
for target in cutlist:
    start = round(target.start_seconds * fps)
    end = round(target.end_seconds * fps)
    need = end - start
    candidates = safe_assets where safe_duration_frames >= need
    asset = choose_by(coherence, unused_source_window, duration_margin)
    source_in = choose_safe_window(asset, need)
    source_out = source_in + need
    append timeline row
```

Do not use the source video's original global position as the target position. Generated videos are a redundant pool and may be reordered, cropped, or reused from different safe windows.
