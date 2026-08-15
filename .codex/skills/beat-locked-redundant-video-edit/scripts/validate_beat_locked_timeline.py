#!/usr/bin/env python3
"""Validate a beat-locked timeline's contiguous integer-frame boundaries."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("timeline", type=Path)
    parser.add_argument("--fps", type=int, required=True)
    parser.add_argument("--expected-frames", type=int, required=True)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.timeline.open(encoding="utf-8")))
    if not rows:
        raise SystemExit("timeline is empty")

    previous_end = None
    total = 0
    for index, row in enumerate(rows, start=1):
        start = int(row["target_start_frame"])
        end = int(row["target_end_frame_exclusive"])
        if end <= start:
            raise SystemExit(f"row {index}: non-positive frame range {start}:{end}")
        if previous_end is not None and start != previous_end:
            raise SystemExit(f"row {index}: gap or overlap; expected start {previous_end}, got {start}")
        expected_count = end - start
        if int(row["target_frames"]) != expected_count:
            raise SystemExit(f"row {index}: target_frames does not match range")
        total += expected_count
        previous_end = end

    if int(rows[0]["target_start_frame"]) != 0:
        raise SystemExit("timeline does not start at frame 0")
    if total != args.expected_frames:
        raise SystemExit(f"timeline has {total} frames; expected {args.expected_frames}")
    print(f"OK: {len(rows)} intervals, {total} frames, {total / args.fps:.6f}s at {args.fps}fps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
