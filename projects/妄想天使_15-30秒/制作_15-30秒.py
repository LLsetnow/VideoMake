"""Prepare the 15-30 second 妄想天使 Ref2VA test workflow."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
ROOT = PROJECT.parents[1]
TEMPLATE = ROOT / "projects" / "千夏_便利店取饮料_15秒_2K横屏" / "千夏_便利店取饮料_15秒_2K横屏_workflow_api.json"
PROMPT_FILE = PROJECT / "妄想天使_15-30秒_prompt.txt"
OUTPUT = PROJECT / "妄想天使_15-30秒_workflow_api.json"

REFERENCES = [
    "404舞台.png",
    "404走廊.png",
    "千夏-全身三视图-方形-v2.png",
    "南宫羽_角色三视图.png",
    "爱芮_角色三视图.png",
]


def main() -> None:
    workflow = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    conditioning = workflow["6"]["inputs"]
    conditioning["prompt"] = ["36", 0]
    conditioning["task_type"] = "Ref2VA"
    conditioning["audio_mode"] = "native"
    conditioning["audio_denoise_strength"] = 1.0
    conditioning["add_source_as_reference"] = False
    conditioning["prompt_primary_audio_ordinal"] = 0
    conditioning.pop("drive_audio", None)
    conditioning.pop("final_audio", None)
    conditioning.pop("ref_audios.ref_audio_0", None)

    workflow["14"]["inputs"]["value"] = 15
    workflow["16"]["inputs"].update({
        "aspect_ratio": "16:9 (Widescreen)",
        "megapixels": 0.9,
        "multiple": 32,
    })
    workflow["12"]["inputs"]["filename_prefix"] = "MiniMaxH3/wangxiang_tianshi_15_30s_test"
    workflow["36"]["inputs"]["prompt"] = PROMPT_FILE.read_text(encoding="utf-8")

    image_nodes = ["37", "54", "55", "56", "57"]
    for node_id, filename in zip(image_nodes, REFERENCES):
        workflow[node_id] = {
            "inputs": {"image": filename},
            "class_type": "LoadImage",
            "_meta": {"title": f"Load Reference Image {node_id}"},
        }
    for index, node_id in enumerate(image_nodes):
        conditioning[f"ref_images.ref_image_{index}"] = [node_id, 0]

    workflow["59"] = {
        "inputs": {
            "audio": "爱芮音色6秒.mp3",
            "audioUI": "",
        },
        "class_type": "LoadAudio",
        "_meta": {"title": "Load Airi Voice Timbre Reference"},
    }
    conditioning["ref_audios.ref_audio_0"] = ["59", 0]

    OUTPUT.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
