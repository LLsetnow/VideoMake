"""Prepare the 15-second 妄想天使 demo Ref2VA workflow."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
TEMPLATE = ROOT / "projects" / "千夏_便利店取饮料_15秒_2K横屏" / "千夏_便利店取饮料_15秒_2K横屏_workflow_api.json"
PROMPT_FILE = PROJECT / "妄想天使_前15秒Demo_prompt.txt"
OUTPUT = PROJECT / "妄想天使_前15秒Demo_workflow_api.json"


REFERENCES = [
    "404门口-夜景.png",
    "404舞台.png",
    "404走廊.png",
    "千夏-全身三视图-方形-v2.png",
    "南宫羽_角色三视图.png",
    "爱芮_角色三视图.png",
]


def main() -> None:
    workflow = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    workflow["6"]["inputs"]["prompt"] = ["36", 0]
    workflow["6"]["inputs"]["task_type"] = "Ref2VA"
    workflow["6"]["inputs"]["audio_mode"] = "native"
    workflow["6"]["inputs"]["audio_denoise_strength"] = 1.0
    workflow["6"]["inputs"]["add_source_as_reference"] = False
    workflow["6"]["inputs"]["prompt_primary_audio_ordinal"] = 0
    workflow["6"]["inputs"].pop("drive_audio", None)
    workflow["6"]["inputs"].pop("final_audio", None)
    workflow["6"]["inputs"].pop("ref_audios.ref_audio_0", None)
    workflow["14"]["inputs"]["value"] = 15
    workflow["16"]["inputs"].update({
        "aspect_ratio": "16:9 (Widescreen)",
        # Six reference images exceed 48 GB at 2.0 MP on the 4090D; keep the
        # 16:9 composition while using the safer 0.9 MP conditioning size.
        "megapixels": 0.9,
        "multiple": 32,
    })
    workflow["12"]["inputs"]["filename_prefix"] = "MiniMaxH3/wangxiang_tianshi_demo_15s"
    workflow["36"]["inputs"]["prompt"] = PROMPT_FILE.read_text(encoding="utf-8")

    # Keep every character and scene reference as a separate LoadImage node.
    load_nodes = ["37", "54", "55", "56", "57", "58"]
    for node_id, filename in zip(load_nodes, REFERENCES):
        if node_id not in workflow:
            workflow[node_id] = {
                "inputs": {"image": filename},
                "class_type": "LoadImage",
                "_meta": {"title": f"Load Reference Image {node_id}"},
            }
        else:
            workflow[node_id]["inputs"]["image"] = filename
    for index, node_id in enumerate(load_nodes):
        workflow["6"]["inputs"][f"ref_images.ref_image_{index}"] = [node_id, 0]

    OUTPUT.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
