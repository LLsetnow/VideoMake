#!/usr/bin/env python3
"""Generate globally normalized, temporally stabilized foreground depth frames."""

from __future__ import annotations

import argparse
from pathlib import Path

import coremltools as ct
import numpy as np
from PIL import Image, ImageFilter, ImageOps


MODEL_PATH = Path("/Users/apple/Documents/VideoMake/.runtime/depth_anything_v2_small_f16/DepthAnythingV2SmallF16.mlpackage")
MODEL_SIZE = (518, 392)


def prepare_image(image: Image.Image) -> tuple[Image.Image, tuple[int, int, int, int]]:
    image = image.convert("RGB")
    fitted = ImageOps.contain(image, MODEL_SIZE, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", MODEL_SIZE, (0, 0, 0))
    left = (MODEL_SIZE[0] - fitted.width) // 2
    top = (MODEL_SIZE[1] - fitted.height) // 2
    canvas.paste(fitted, (left, top))
    return canvas, (left, top, left + fitted.width, top + fitted.height)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Regenerate stable foreground depth frames.")
    parser.add_argument("frames_dir", type=Path)
    parser.add_argument("masks_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--background-value", type=int, default=8)
    parser.add_argument("--mask-threshold", type=float, default=0.20)
    parser.add_argument("--mask-current-weight", type=float, default=0.65)
    parser.add_argument("--depth-current-weight", type=float, default=0.65)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not MODEL_PATH.is_dir():
        raise SystemExit(f"Depth model not found: {MODEL_PATH}")
    if not 0 <= args.background_value <= 255:
        raise SystemExit("--background-value must be between 0 and 255")
    if not 0 <= args.mask_threshold < 1:
        raise SystemExit("--mask-threshold must be in the 0..1 range")
    if not 0 < args.mask_current_weight <= 1 or not 0 < args.depth_current_weight <= 1:
        raise SystemExit("temporal weights must be in the (0..1] range")

    frame_paths = sorted(args.frames_dir.glob("frame_*.png"))
    if not frame_paths:
        raise SystemExit(f"No source frames found in {args.frames_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    model = ct.models.MLModel(str(MODEL_PATH), compute_units=ct.ComputeUnit.ALL)
    raw_crops: list[np.ndarray] = []
    output_sizes: list[tuple[int, int]] = []
    samples: list[np.ndarray] = []

    for index, source in enumerate(frame_paths, start=1):
        with Image.open(source) as opened:
            original_size = opened.size
            prepared, crop = prepare_image(opened)
        result = model.predict({"image": prepared})
        raw = np.asarray(result["depth"], dtype=np.float32)
        left, top, right, bottom = crop
        raw_crop = raw[top:bottom, left:right]
        raw_crops.append(raw_crop)
        output_sizes.append(original_size)
        # A spatial sample is enough for a stable sequence-wide 1st/99th scale.
        samples.append(raw_crop[::4, ::4].reshape(-1))
        if index == 1 or index % 25 == 0 or index == len(frame_paths):
            print(f"inferred={index}/{len(frame_paths)}")

    sampled_values = np.concatenate(samples)
    low, high = np.percentile(sampled_values, (1, 99))
    if high <= low:
        low, high = float(sampled_values.min()), float(sampled_values.max())
    if high <= low:
        raise SystemExit("Global depth scale is degenerate")
    print(f"global_depth_scale low={low:.6f} high={high:.6f}")

    previous_mask: np.ndarray | None = None
    previous_depth: np.ndarray | None = None
    for index, (source, raw_crop, output_size) in enumerate(
        zip(frame_paths, raw_crops, output_sizes), start=1
    ):
        normalized = np.clip((raw_crop - low) / (high - low), 0.0, 1.0)
        depth_image = Image.fromarray(np.rint(normalized * 255).astype(np.uint8), mode="L").resize(
            output_size, Image.Resampling.BICUBIC
        )
        depth = np.asarray(depth_image, dtype=np.float32)

        mask_path = args.masks_dir / source.name
        if not mask_path.is_file():
            raise SystemExit(f"Mask frame not found: {mask_path}")
        with Image.open(mask_path) as opened_mask:
            mask_image = opened_mask.convert("L").resize(output_size, Image.Resampling.LANCZOS)
            mask_image = mask_image.filter(ImageFilter.GaussianBlur(radius=0.65))
            current_mask = np.asarray(mask_image, dtype=np.float32) / 255.0
        if previous_mask is None:
            smoothed_mask = current_mask
        else:
            smoothed_mask = args.mask_current_weight * current_mask + (1 - args.mask_current_weight) * previous_mask
        previous_mask = smoothed_mask

        alpha = np.clip((smoothed_mask - args.mask_threshold) / (1 - args.mask_threshold), 0.0, 1.0)
        masked_depth = depth * alpha + args.background_value * (1 - alpha)
        if previous_depth is not None:
            subject = (alpha > 0.5) & (previous_mask > 0.5)
            masked_depth[subject] = (
                args.depth_current_weight * masked_depth[subject]
                + (1 - args.depth_current_weight) * previous_depth[subject]
            )
        previous_depth = masked_depth.copy()

        destination = args.output_dir / source.name.replace(".png", "_depth.png")
        temporary = destination.with_name(f".{destination.name}.part")
        Image.fromarray(np.rint(masked_depth).clip(0, 255).astype(np.uint8), mode="L").save(
            temporary, format="PNG"
        )
        temporary.replace(destination)
        if index == 1 or index % 25 == 0 or index == len(frame_paths):
            print(f"written={index}/{len(frame_paths)} output={destination}")

    print(
        f"frames={len(frame_paths)} output_dir={args.output_dir} "
        f"background_value={args.background_value} mask_threshold={args.mask_threshold} "
        f"mask_current_weight={args.mask_current_weight} depth_current_weight={args.depth_current_weight}"
    )


if __name__ == "__main__":
    main()
