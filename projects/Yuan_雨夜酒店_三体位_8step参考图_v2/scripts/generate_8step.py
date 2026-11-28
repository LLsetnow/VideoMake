#!/usr/bin/env python3
"""Submit a Qwen-Image-Edit-2511 8-step keyframe job to the local ComfyUI and fetch the result."""

import argparse
import json
import time
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "http://127.0.0.1:8189"
TEMPLATE = ROOT.parent / "Yuan_雨夜酒店_双人关键帧_Qwen2511" / "v3_8step_workflow_api.json"
INPUT_SUBFOLDER = "videomake/yuan-rain-hotel-3pose-v2-8step"


def api(path, data=None):
    url = f"{HOST}{path}"
    body = json.dumps(data).encode() if data is not None else None
    request = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json"} if body else {}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        raw = response.read()
    return json.loads(raw) if raw else {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--prompt-file", required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--depth", required=True, help="depth image filename inside the input subfolder")
    parser.add_argument("--output-name", required=True)
    parser.add_argument(
        "--identity-only",
        action="store_true",
        help="use the identity image as the only reference (no pose map)",
    )
    args = parser.parse_args()

    workflow = json.loads(TEMPLATE.read_text())
    prompt = Path(args.prompt_file).read_text().strip()
    workflow["6"]["inputs"]["prompt"] = prompt
    workflow["7"]["inputs"]["seed"] = args.seed
    workflow["7"]["inputs"]["steps"] = 8
    workflow["7"]["inputs"]["cfg"] = 1.0
    workflow["7"]["inputs"]["sampler_name"] = "euler"
    workflow["7"]["inputs"]["scheduler"] = "simple"
    workflow["10"]["inputs"]["image"] = f"{INPUT_SUBFOLDER}/{args.depth}"
    workflow["15"]["inputs"]["image"] = f"{INPUT_SUBFOLDER}/yuan_identity.png"
    if args.identity_only:
        workflow["6"]["inputs"].pop("image2", None)
        workflow["12"]["inputs"].pop("image2", None)
        del workflow["15"]
    workflow["9"]["inputs"]["filename_prefix"] = (
        f"videomake/yuan-rain-hotel-3pose-v2-8step/{args.slug}"
    )

    workflow_path = ROOT / "workflows" / f"{args.slug}.json"
    workflow_path.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n")
    prompt_path = ROOT / "prompts" / f"{args.slug}.txt"
    if prompt_path.resolve() != Path(args.prompt_file).resolve():
        prompt_path.write_text(prompt + "\n")

    client_id = str(uuid.uuid4())
    queued = api("/prompt", {"prompt": workflow, "client_id": client_id})
    prompt_id = queued["prompt_id"]
    print(f"queued {prompt_id}")

    deadline = time.time() + 900
    entry = None
    while time.time() < deadline:
        time.sleep(3)
        history = api(f"/history/{prompt_id}")
        entry = history.get(prompt_id)
        if entry and entry.get("outputs"):
            break
    else:
        raise SystemExit(f"timeout waiting for {prompt_id}")

    image = entry["outputs"]["9"]["images"][0]
    query = urllib.parse.urlencode(
        {"filename": image["filename"], "subfolder": image["subfolder"], "type": "output"}
    )
    with urllib.request.urlopen(f"{HOST}/view?{query}", timeout=120) as response:
        payload = response.read()

    destination = ROOT / "output" / args.output_name
    destination.write_bytes(payload)

    record = {
        "slug": args.slug,
        "seed": args.seed,
        "prompt_id": prompt_id,
        "prompt_file": str(prompt_path),
        "workflow": str(workflow_path),
        "depth": args.depth,
        "path": str(destination),
        "filename": image["filename"],
        "subfolder": image["subfolder"],
        "bytes": len(payload),
    }
    print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
