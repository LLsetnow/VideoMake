#!/usr/bin/env python3
"""Build and render a frame-accurate beat-locked edit from the asset pool."""

from __future__ import annotations

import csv
import json
import subprocess
from collections import Counter
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ANALYSIS = PROJECT / "analysis"
ASSET_MANIFEST = ANALYSIS / "asset_manifest.csv"
CUTLIST = PROJECT / "cutlist.csv"
AUDIO = PROJECT / "audio" / "情感失色症.mp3"
SEGMENT_DIR = PROJECT / "qa" / "beat_locked_segments"
CONCAT_LIST = PROJECT / "qa" / "beat_locked_concat.txt"
VIDEO_ONLY = PROJECT / "qa" / "beat_locked_video_only.mp4"
FINAL = PROJECT / "output" / "情感失色症_60秒_beat_locked.mp4"
TIMELINE = ANALYSIS / "beat_locked_timeline.csv"
VERIFY = ANALYSIS / "beat_locked_cut_verification.txt"

FPS = 24
WIDTH = 1280
HEIGHT = 720
CROP_Y = 8

# Hand-tuned from the labeled contact sheets. The asset pool remains the
# source of truth for ranges; these IDs only choose the visual material.
SELECTION = [
    "A019", "A020", "A029", "A031", "A002", "A006",
    "A024", "A012", "A015", "A017", "A018", "A028",
    "A033", "A034", "A016", "A001", "A023", "A015",
    "A006", "A016", "A034", "A017", "A018",
]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def ffprobe_video(path: Path) -> dict[str, object]:
    data = json.loads(
        run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height,r_frame_rate,nb_frames,duration",
                "-show_entries",
                "format=duration",
                "-of",
                "json",
                str(path),
            ]
        ).stdout
    )
    stream = data["streams"][0]
    duration = float(stream.get("duration") or data.get("format", {}).get("duration") or 0.0)
    return {
        "width": int(stream.get("width", 0)),
        "height": int(stream.get("height", 0)),
        "fps": stream.get("r_frame_rate", ""),
        "frames": int(stream.get("nb_frames", 0)),
        "duration": duration,
    }


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def create_timeline() -> list[dict[str, object]]:
    assets = {row["asset_id"]: row for row in read_rows(ASSET_MANIFEST)}
    cuts = read_rows(CUTLIST)
    if len(cuts) != len(SELECTION):
        raise RuntimeError(f"selection has {len(SELECTION)} items but cutlist has {len(cuts)} rows")

    usage = Counter()
    timeline: list[dict[str, object]] = []
    for index, (cut, asset_id) in enumerate(zip(cuts, SELECTION), start=1):
        if asset_id not in assets:
            raise RuntimeError(f"missing asset {asset_id}")
        asset = assets[asset_id]
        if asset["usable_for_beat_edit"] != "yes":
            raise RuntimeError(f"asset {asset_id} is not marked usable")

        target_start = round(float(cut["global_start"]) * FPS)
        target_end = round(float(cut["global_end"]) * FPS)
        target_frames = target_end - target_start
        safe_start = int(asset["safe_start_frame"])
        safe_end = int(asset["safe_end_frame_exclusive"])
        available = safe_end - safe_start
        if available < target_frames:
            raise RuntimeError(
                f"asset {asset_id} has {available} safe frames but edit {index} needs {target_frames}"
            )

        extra = available - target_frames
        occurrence = usage[asset_id]
        # A repeated long asset gets a different window on each use. For the
        # first use use the centered window; later uses move toward the ends.
        if occurrence == 0:
            offset = extra // 2
        elif occurrence % 2 == 1:
            offset = 0
        else:
            offset = extra
        source_in = safe_start + offset
        source_out = source_in + target_frames
        usage[asset_id] += 1

        requested_start = float(cut["global_start"])
        requested_end = float(cut["global_end"])
        actual_start = target_start / FPS
        actual_end = target_end / FPS
        timeline.append(
            {
                "edit_index": index,
                "global_start_sec": f"{actual_start:.6f}",
                "global_end_sec": f"{actual_end:.6f}",
                "requested_start_sec": f"{requested_start:.6f}",
                "requested_end_sec": f"{requested_end:.6f}",
                "target_start_frame": target_start,
                "target_end_frame_exclusive": target_end,
                "target_frames": target_frames,
                "target_duration_sec": f"{target_frames / FPS:.6f}",
                "anchor": cut["anchor"],
                "asset_id": asset_id,
                "source_group": asset["source_group"],
                "source_path": asset["source_path"],
                "source_in_frame": source_in,
                "source_out_frame_exclusive": source_out,
                "source_in_sec": f"{source_in / FPS:.6f}",
                "source_out_sec": f"{source_out / FPS:.6f}",
                "source_window_sec": f"{target_frames / FPS:.6f}",
                "source_reuse_index": occurrence + 1,
                "audio_mode": "lock_source",
                "start_error_ms": f"{(actual_start - requested_start) * 1000:.3f}",
                "end_error_ms": f"{(actual_end - requested_end) * 1000:.3f}",
                "notes": "source transition guard respected; final cut is frame hard-cut",
            }
        )
    return timeline


def write_timeline(timeline: list[dict[str, object]]) -> None:
    fieldnames = list(timeline[0].keys())
    with TIMELINE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(timeline)


def render_segment(row: dict[str, object], output: Path) -> None:
    source = str(row["source_path"])
    start = int(row["source_in_frame"])
    end = int(row["source_out_frame_exclusive"])
    frames = int(row["target_frames"])
    filter_graph = (
        f"trim=start_frame={start}:end_frame={end},"
        "setpts=PTS-STARTPTS,"
        f"crop={WIDTH}:{HEIGHT}:0:{CROP_Y},format=yuv420p"
    )
    run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            source,
            "-vf",
            filter_graph,
            "-an",
            "-frames:v",
            str(frames),
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-video_track_timescale",
            "24000",
            str(output),
        ]
    )


def render_video(timeline: list[dict[str, object]]) -> list[dict[str, object]]:
    SEGMENT_DIR.mkdir(parents=True, exist_ok=True)
    segment_paths: list[Path] = []
    verification: list[dict[str, object]] = []
    for row in timeline:
        output = SEGMENT_DIR / f"edit_{int(row['edit_index']):02d}_{row['asset_id']}.mp4"
        render_segment(row, output)
        actual = ffprobe_video(output)
        expected = int(row["target_frames"])
        verification.append(
            {
                "edit_index": row["edit_index"],
                "asset_id": row["asset_id"],
                "expected_frames": expected,
                "actual_frames": actual["frames"],
                "expected_duration": f"{expected / FPS:.6f}",
                "actual_duration": f"{float(actual['duration']):.6f}",
                "ok": actual["frames"] == expected and actual["width"] == WIDTH and actual["height"] == HEIGHT,
            }
        )
        segment_paths.append(output)

    with CONCAT_LIST.open("w", encoding="utf-8") as handle:
        for path in segment_paths:
            handle.write(f"file '{path.resolve()}'\n")

    run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(CONCAT_LIST),
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "18",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            "-video_track_timescale",
            "24000",
            str(VIDEO_ONLY),
        ]
    )

    FINAL.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(VIDEO_ONLY),
            "-i",
            str(AUDIO),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "copy",
            "-t",
            "60",
            "-movflags",
            "+faststart",
            str(FINAL),
        ]
    )

    final_video = ffprobe_video(FINAL)
    with VERIFY.open("w", encoding="utf-8") as handle:
        handle.write("情感失色症精准卡点剪辑核验\n")
        handle.write("规则：每个鼓点区间先量化到24fps整数帧，再使用素材源帧硬切；音频直接来自原始MP3。\n\n")
        handle.write("分段核验\n")
        for item in verification:
            handle.write(
                f"edit_{int(item['edit_index']):02d} {item['asset_id']} "
                f"expected={item['expected_frames']} actual={item['actual_frames']} "
                f"expected_duration={item['expected_duration']} actual_duration={item['actual_duration']} "
                f"ok={item['ok']}\n"
            )
        handle.write("\n最终文件\n")
        handle.write(
            f"path={FINAL}\nvideo={final_video['width']}x{final_video['height']} "
            f"fps={final_video['fps']} frames={final_video['frames']} "
            f"duration={float(final_video['duration']):.6f}\n"
        )
        handle.write(f"all_segments_ok={all(bool(item['ok']) for item in verification)}\n")
    return verification


def main() -> None:
    timeline = create_timeline()
    write_timeline(timeline)
    verification = render_video(timeline)
    if not all(bool(item["ok"]) for item in verification):
        raise SystemExit("one or more rendered segments failed frame verification")
    print(f"wrote {TIMELINE}")
    print(f"wrote {FINAL}")
    print(f"wrote {VERIFY}")
    print(f"segments={len(timeline)} frames={sum(int(row['target_frames']) for row in timeline)}")


if __name__ == "__main__":
    main()
