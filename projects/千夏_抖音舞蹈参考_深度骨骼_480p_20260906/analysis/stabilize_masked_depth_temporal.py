#!/usr/bin/env python3
"""Reduce frame-to-frame depth flicker without leaving background trails."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Temporally stabilize masked depth frames.")
    parser.add_argument("depth_dir", type=Path)
    parser.add_argument("mask_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--background-value", type=int, default=8)
    parser.add_argument("--mask-threshold", type=float, default=0.20)
    return parser.parse_args()


def load_depth(path: Path) -> np.ndarray:
    with Image.open(path) as opened:
        return np.asarray(opened.convert("L"), dtype=np.float32)


def load_mask(path: Path, size: tuple[int, int]) -> np.ndarray:
    with Image.open(path) as opened:
        image = opened.convert("L").resize(size, Image.Resampling.LANCZOS)
        image = image.filter(ImageFilter.GaussianBlur(radius=0.65))
        return np.asarray(image, dtype=np.float32) / 255.0


def main() -> None:
    args = parse_args()
    if not 0 <= args.background_value <= 255:
        raise SystemExit("--background-value must be between 0 and 255")
    if not 0 <= args.mask_threshold < 1:
        raise SystemExit("--mask-threshold must be in the 0..1 range")

    depth_paths = sorted(args.depth_dir.glob("frame_*_depth.png"))
    if not depth_paths:
        raise SystemExit(f"No depth frames found in {args.depth_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(depth_paths[0]) as opened:
        width, height = opened.size
    size = (width, height)
    frame_count = len(depth_paths)
    weights = np.asarray([1, 4, 6, 4, 1], dtype=np.float32)
    radius = len(weights) // 2

    depths = [load_depth(path) for path in depth_paths]
    masks = [
        load_mask(args.mask_dir / path.name.replace("_depth.png", ".png"), size)
        for path in depth_paths
    ]

    for index, source in enumerate(depth_paths):
        start = max(0, index - radius)
        stop = min(frame_count, index + radius + 1)
        local_weights = weights[radius - (index - start) : radius + (stop - index)]
        local_weights = local_weights / local_weights.sum()

        numerator = np.zeros(size[::-1], dtype=np.float32)
        denominator = np.zeros(size[::-1], dtype=np.float32)
        for weight, frame_index in zip(local_weights, range(start, stop)):
            valid = (masks[frame_index] > args.mask_threshold).astype(np.float32)
            numerator += weight * depths[frame_index] * valid
            denominator += weight * valid

        current_mask = masks[index]
        alpha = np.clip((current_mask - args.mask_threshold) / (1 - args.mask_threshold), 0.0, 1.0)
        smoothed = np.divide(
            numerator,
            np.maximum(denominator, 1e-6),
            out=np.full_like(numerator, float(args.background_value)),
            where=denominator > 1e-6,
        )
        output = np.rint(smoothed * alpha + args.background_value * (1 - alpha)).clip(0, 255).astype(np.uint8)

        destination = args.output_dir / source.name
        temporary = destination.with_name(f".{destination.name}.part")
        Image.fromarray(output).save(temporary, format="PNG")
        temporary.replace(destination)
        if index == 0 or (index + 1) % 25 == 0 or index + 1 == frame_count:
            print(f"processed={index + 1}/{frame_count} output={destination}")

    print(
        f"frames={frame_count} output_dir={args.output_dir} window=5 "
        f"weights=1,4,6,4,1 background_value={args.background_value}"
    )


if __name__ == "__main__":
    main()
