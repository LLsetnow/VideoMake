#!/usr/bin/env python3
"""Run the project Depth Anything wrapper once for a whole frame sequence."""

from pathlib import Path
import sys

import coremltools as ct
from PIL import Image

TOOLS = Path(__file__).resolve().parents[4] / "tools"
sys.path.insert(0, str(TOOLS))
from depth_anything_macos import MODEL_PATH, MODEL_SIZE, normalize_depth, prepare_image  # noqa: E402


def main() -> None:
    root = Path(__file__).resolve().parent
    frames = root / "source_24fps_frames"
    output = root / "depth"
    files = sorted(frames.glob("frame_*.png"))
    if not files:
        raise SystemExit(f"No input frames found in {frames}")
    if not MODEL_PATH.is_dir():
        raise SystemExit(f"Core ML model not found: {MODEL_PATH}")

    model = ct.models.MLModel(str(MODEL_PATH), compute_units=ct.ComputeUnit.ALL)
    output.mkdir(parents=True, exist_ok=True)
    for index, source_path in enumerate(files, 1):
        target_path = output / f"{source_path.stem}_depth.png"
        source = Image.open(source_path)
        prepared, crop = prepare_image(source)
        result = model.predict({"image": prepared})
        depth = normalize_depth(result["depth"])
        depth = depth.crop(crop).resize(source.size, Image.Resampling.BICUBIC)
        depth.save(target_path)
        print(f"{index}/{len(files)} {target_path}", flush=True)


if __name__ == "__main__":
    main()
