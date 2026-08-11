from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEMPLATE = Path("/Users/apple/Documents/VideoMake/workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json")
REFERENCE_NAME = "短发社畜_角色参考_9x16.png"

segments = [
    ("1-15秒", "精神创伤_1-15秒_prompt.txt", "精神创伤_1-15秒_workflow_api.json", "MinimaxH3/spirit_trauma_01_15s"),
    ("16-30秒", "精神创伤_16-30秒_prompt.txt", "精神创伤_16-30秒_workflow_api.json", "MinimaxH3/spirit_trauma_16_30s"),
    ("31-45秒", "精神创伤_31-45秒_prompt.txt", "精神创伤_31-45秒_workflow_api.json", "MinimaxH3/spirit_trauma_31_45s"),
    ("46-60秒", "精神创伤_46-60秒_prompt.txt", "精神创伤_46-60秒_workflow_api.json", "MinimaxH3/spirit_trauma_46_60s"),
]

for folder, prompt_name, workflow_name, prefix in segments:
    folder_path = ROOT / folder
    workflow = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    prompt = (folder_path / prompt_name).read_text(encoding="utf-8")

    workflow["36"]["inputs"]["prompt"] = prompt
    workflow["37"]["inputs"]["image"] = REFERENCE_NAME
    workflow["14"]["inputs"]["value"] = 15
    workflow["16"]["inputs"]["aspect_ratio"] = "9:16 (Portrait Widescreen)"
    workflow["12"]["inputs"]["filename_prefix"] = prefix

    conditioning = workflow["6"]["inputs"]
    lock_source = folder == "1-15秒"
    conditioning["audio_mode"] = "lock_source" if lock_source else "native"
    conditioning["audio_denoise_strength"] = 0 if lock_source else 1.0
    conditioning["prompt_primary_audio_ordinal"] = 1 if lock_source else 0
    conditioning["ref_audios.ref_audio_0"] = ["53", 0]
    if lock_source:
        conditioning["drive_audio"] = ["53", 0]
        conditioning["final_audio"] = ["53", 0]
    else:
        conditioning.pop("drive_audio", None)
        conditioning.pop("final_audio", None)
    workflow["52"]["inputs"]["audio"] = "精神创伤（emo版）.mp3"
    workflow["53"]["inputs"]["duration"] = 15.0
    workflow["12"]["inputs"]["trim_to_audio"] = lock_source

    (folder_path / workflow_name).write_text(
        json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

print("Created", len(segments), "workflow files")
