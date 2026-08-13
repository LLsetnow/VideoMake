#!/usr/bin/env python3
"""Build a frame-aware asset manifest from generated H3 videos.

Uses FFmpeg's scdet filter so this script does not depend on OpenCV or
PySceneDetect. Detected boundaries are treated as transition starts; a small
guard band is removed from the usable range so a later beat-locked hard cut
does not land inside a generated transition.
"""

from __future__ import annotations

import csv
import json
import re
import statistics
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ANALYSIS = PROJECT / "analysis"
MANIFEST = ANALYSIS / "asset_manifest.csv"
SUMMARY = ANALYSIS / "scene_detection_summary.txt"

FPS_TARGET = 24.0
MIN_SCENE_SECONDS = 0.80
MIN_GAP_SECONDS = 0.80
TRANSITION_GUARD_FRAMES = 6


def run_capture(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)


def probe(path: Path) -> dict[str, object]:
    data = json.loads(
        run_capture(
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
    fps = float(Fraction(stream.get("r_frame_rate", "24/1")))
    duration_value = stream.get("duration") or data.get("format", {}).get("duration") or "0"
    duration = float(duration_value)
    frames_value = stream.get("nb_frames")
    frames = int(frames_value) if frames_value not in (None, "N/A") else round(duration * fps)
    return {
        "width": int(stream.get("width", 0)),
        "height": int(stream.get("height", 0)),
        "fps": fps,
        "duration": duration,
        "frames": frames,
    }


def scene_scores(path: Path) -> list[tuple[int, float, float]]:
    with tempfile.TemporaryDirectory(prefix="情感失色症_scd_") as temp_dir:
        score_file = Path(temp_dir) / "scores.txt"
        run_capture(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(path),
                "-vf",
                f"scdet=threshold=0,metadata=print:key=lavfi.scd.score:file={score_file}",
                "-an",
                "-f",
                "null",
                "-",
            ]
        )
        score_text = score_file.read_text(encoding="utf-8")
    rows: list[tuple[int, float, float]] = []
    frame = None
    pts_time = None
    for line in score_text.splitlines():
        match = re.search(r"frame:\s*(\d+).*pts_time:([0-9.]+)", line)
        if match:
            frame = int(match.group(1))
            pts_time = float(match.group(2))
            continue
        match = re.search(r"lavfi\.scd\.score=([0-9.]+)", line)
        if match and frame is not None and pts_time is not None:
            rows.append((frame, pts_time, float(match.group(1))))
    return rows


def quantile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    index = (len(ordered) - 1) * q
    low = int(index)
    high = min(low + 1, len(ordered) - 1)
    weight = index - low
    return ordered[low] * (1.0 - weight) + ordered[high] * weight


def find_peaks(scores: list[tuple[int, float, float]], fps: float) -> tuple[list[tuple[int, float, float]], float]:
    if len(scores) < 3:
        return [], 0.0
    values = [score for _, _, score in scores]
    median = statistics.median(values)
    mad = statistics.median(abs(value - median) for value in values)
    threshold = max(2.5, median + 8.0 * mad, quantile(values, 0.98))
    min_gap = round(MIN_GAP_SECONDS * fps)
    candidates: list[tuple[int, float, float]] = []
    for index in range(1, len(scores) - 1):
        previous = scores[index - 1]
        current = scores[index]
        following = scores[index + 1]
        if current[2] >= threshold and current[2] >= previous[2] and current[2] >= following[2]:
            candidates.append(current)

    selected: list[tuple[int, float, float]] = []
    for candidate in candidates:
        if not selected or candidate[0] - selected[-1][0] >= min_gap:
            selected.append(candidate)
        elif candidate[2] > selected[-1][2]:
            selected[-1] = candidate
    return selected, threshold


def prompt_for(source: Path) -> str:
    stem = source.stem.replace("_00001-audio", "")
    if stem in {"00-15", "15-30", "30-45", "45-60"}:
        folder = {
            "00-15": "1-15秒",
            "15-30": "15-30秒",
            "30-45": "30-45秒",
            "45-60": "45-60秒",
        }[stem]
        candidate = PROJECT / folder / f"情感失色症_{stem}_prompt.txt"
        return str(candidate) if candidate.exists() else ""
    match = re.search(r"shot_(\d+)", stem)
    if match:
        candidate = PROJECT / "shots" / f"shot_{int(match.group(1)):02d}_prompt.txt"
        return str(candidate) if candidate.exists() else ""
    return ""


def source_groups() -> list[tuple[str, list[Path]]]:
    return [
        (
            "primary_4090D-48G",
            sorted((PROJECT / "segments_4090D-48G").glob("*.mp4")),
        ),
        (
            "legacy_short_4090D-48G",
            sorted((PROJECT / "shots" / "output_4090D-48G").glob("*.mp4")),
        ),
        (
            "legacy_short_batch",
            sorted((PROJECT / "shots" / "output").glob("*.mp4")),
        ),
    ]


def main() -> None:
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "asset_id",
        "source_group",
        "source_path",
        "prompt_path",
        "width",
        "height",
        "fps",
        "source_total_frames",
        "source_duration_sec",
        "asset_index",
        "raw_start_frame",
        "raw_end_frame_exclusive",
        "raw_start_sec",
        "raw_end_sec",
        "safe_start_frame",
        "safe_end_frame_exclusive",
        "safe_start_sec",
        "safe_end_sec",
        "safe_duration_sec",
        "cut_in_score",
        "cut_out_score",
        "detector_threshold",
        "detector_confidence",
        "usable_for_beat_edit",
        "notes",
    ]
    manifest_rows: list[dict[str, object]] = []
    summary_lines = [
        "情感失色症：生成视频镜头检测摘要",
        "检测器：FFmpeg scdet + 局部峰值 + 最短镜头/最小间隔过滤",
        f"目标帧率：{FPS_TARGET:g} fps；转场保护：{TRANSITION_GUARD_FRAMES} frames；最短可用素材：{MIN_SCENE_SECONDS:g}s",
        "",
    ]
    asset_number = 1
    for group, sources in source_groups():
        for source in sources:
            meta = probe(source)
            scores = scene_scores(source)
            peaks, threshold = find_peaks(scores, float(meta["fps"]))
            total_frames = int(meta["frames"])
            boundaries = [0] + [frame for frame, _, _ in peaks] + [total_frames]
            score_by_frame = {frame: score for frame, _, score in scores}
            summary_lines.append(
                f"{group}\t{source.name}\t{meta['fps']:.6g}fps\t{total_frames} frames\t{meta['duration']:.3f}s\tthreshold={threshold:.3f}\tpeaks="
                + ",".join(f"{frame}@{time:.3f}s/{score:.3f}" for frame, time, score in peaks)
            )
            for index, (raw_start, raw_end) in enumerate(zip(boundaries, boundaries[1:]), start=1):
                safe_start = raw_start if index == 1 else min(raw_start + TRANSITION_GUARD_FRAMES, raw_end)
                safe_end = raw_end if index == len(boundaries) - 1 else max(raw_start, raw_end - TRANSITION_GUARD_FRAMES)
                safe_duration = max(0.0, (safe_end - safe_start) / float(meta["fps"]))
                previous_score = score_by_frame.get(raw_start, 0.0) if index > 1 else 0.0
                next_score = score_by_frame.get(raw_end, 0.0) if index < len(boundaries) - 1 else 0.0
                boundary_score = max(previous_score, next_score)
                confidence = min(1.0, boundary_score / 10.0) if boundary_score else 0.5
                usable = safe_duration >= MIN_SCENE_SECONDS
                notes = "transition guard applied" if index not in (1, len(boundaries) - 1) else "boundary edge"
                if not usable:
                    notes += "; too short after guard"
                manifest_rows.append(
                    {
                        "asset_id": f"A{asset_number:03d}",
                        "source_group": group,
                        "source_path": str(source.resolve()),
                        "prompt_path": prompt_for(source),
                        "width": meta["width"],
                        "height": meta["height"],
                        "fps": f"{float(meta['fps']):.6g}",
                        "source_total_frames": total_frames,
                        "source_duration_sec": f"{float(meta['duration']):.6f}",
                        "asset_index": index,
                        "raw_start_frame": raw_start,
                        "raw_end_frame_exclusive": raw_end,
                        "raw_start_sec": f"{raw_start / float(meta['fps']):.6f}",
                        "raw_end_sec": f"{raw_end / float(meta['fps']):.6f}",
                        "safe_start_frame": safe_start,
                        "safe_end_frame_exclusive": safe_end,
                        "safe_start_sec": f"{safe_start / float(meta['fps']):.6f}",
                        "safe_end_sec": f"{safe_end / float(meta['fps']):.6f}",
                        "safe_duration_sec": f"{safe_duration:.6f}",
                        "cut_in_score": f"{previous_score:.6f}",
                        "cut_out_score": f"{next_score:.6f}",
                        "detector_threshold": f"{threshold:.6f}",
                        "detector_confidence": f"{confidence:.4f}",
                        "usable_for_beat_edit": "yes" if usable else "no",
                        "notes": notes,
                    }
                )
                asset_number += 1

    with MANIFEST.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest_rows)
    summary_lines.extend(
        [
            "",
            f"视频数量：{sum(len(sources) for _, sources in source_groups())}",
            f"素材片段数量：{len(manifest_rows)}",
            f"可用于鼓点剪辑：{sum(row['usable_for_beat_edit'] == 'yes' for row in manifest_rows)}",
            f"已写入：{MANIFEST}",
        ]
    )
    SUMMARY.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST}")
    print(f"wrote {SUMMARY}")
    print(f"videos={sum(len(sources) for _, sources in source_groups())} assets={len(manifest_rows)}")


if __name__ == "__main__":
    main()
