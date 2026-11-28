#!/usr/bin/env python3
"""Apply temporally smoothed person masks to grayscale depth frames."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mask background out of grayscale depth PNGs.")
    parser.add_argument("depth_dir", type=Path)
    parser.add_argument("mask_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--background-value", type=int, default=8, help="Uniform far-background grayscale value")
    parser.add_argument("--threshold", type=float, default=0.20, help="Soft-mask cutoff in the 0..1 range")
    parser.add_argument("--current-weight", type=float, default=0.80, help="Current-frame weight for temporal smoothing")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0 <= args.background_value <= 255:
        raise SystemExit("--background-value must be between 0 and 255")
    if not 0 <= args.threshold < 1:
        raise SystemExit("--threshold must be in the 0..1 range")
    if not 0 < args.current_weight <= 1:
        raise SystemExit("--current-weight must be in the (0..1] range")

    depth_paths = sorted(args.depth_dir.glob("frame_*_depth.png"))
    if not depth_paths:
        raise SystemExit(f"No depth frames found in {args.depth_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    previous_mask: np.ndarray | None = None
    for index, depth_path in enumerate(depth_paths, start=1):
        mask_path = args.mask_dir / depth_path.name.replace("_depth.png", ".png")
        if not mask_path.is_file():
            raise SystemExit(f"Mask frame not found: {mask_path}")

        with Image.open(depth_path) as opened_depth:
            depth = np.asarray(opened_depth.convert("L"), dtype=np.float32)
        with Image.open(mask_path) as opened_mask:
            resized_mask = opened_mask.convert("L").resize(
                (depth.shape[1], depth.shape[0]), Image.Resampling.LANCZOS
            )
            # A small blur removes single-frame Vision edge speckles before the
            # temporal blend and keeps hair/hand edges softly feathered.
            resized_mask = resized_mask.filter(ImageFilter.GaussianBlur(radius=0.65))
            current_mask = np.asarray(resized_mask, dtype=np.float32) / 255.0

        if previous_mask is None:
            smoothed_mask = current_mask
        else:
            smoothed_mask = args.current_weight * current_mask + (1 - args.current_weight) * previous_mask
        previous_mask = smoothed_mask

        alpha = np.clip((smoothed_mask - args.threshold) / (1 - args.threshold), 0.0, 1.0)
        output = np.rint(depth * alpha + args.background_value * (1 - alpha)).clip(0, 255).astype(np.uint8)
        destination = args.output_dir / depth_path.name
        temporary = destination.with_name(f".{destination.name}.part")
        Image.fromarray(output, mode="L").save(temporary, format="PNG")
        temporary.replace(destination)

        if index == 1 or index % 25 == 0 or index == len(depth_paths):
            print(
                f"processed={index}/{len(depth_paths)} output={destination} "
                f"foreground_fraction={(alpha > 0.5).mean():.3f}"
            )

    print(
        f"frames={len(depth_paths)} output_dir={args.output_dir} "
        f"background_value={args.background_value} threshold={args.threshold} "
        f"current_weight={args.current_weight}"
    )


if __name__ == "__main__":
    main()
