"""Prepare the flat-hand-drawn-poster reference variant of the 15-second demo."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BASE_WORKFLOW = PROJECT / "妄想天使_前15秒Demo_workflow_api.json"
BASE_PROMPT = PROJECT / "妄想天使_前15秒Demo_prompt.txt"
POSTER_PROMPT = PROJECT / "妄想天使_前15秒Demo_poster_ref_v2_prompt.txt"
POSTER_WORKFLOW = PROJECT / "妄想天使_前15秒Demo_poster_ref_v2_workflow_api.json"


def build_prompt() -> str:
    prompt = BASE_PROMPT.read_text(encoding="utf-8")
    prompt = prompt.replace(
        "<Picture 6> is the identity reference for <Subject 3>, Airi; preserve her face, hairstyle, costume, proportions, headphones, and accessories.",
        "<Picture 6> is the identity reference for <Subject 3>, Airi; preserve her face, hairstyle, costume, proportions, headphones, and accessories.\n<Picture 7> is the generated 9:16 flat hand-drawn poster reference; it guides trio arrangement, title hierarchy, pastel palette, and graphic composition, not literal boundary frames.",
    )
    prompt = prompt.replace(
        "Preserve identity, costume construction, and 404 spatial continuity.",
        "Use <Picture 7> as the overall key visual while adapting its vertical composition to 16:9; preserve identity, costume construction, and 404 spatial continuity.",
    )
    prompt = prompt.replace(
        "<Picture 6> (Shots 4, 6): fully_preserved - Airi's identity, hair, costume, headphones, proportions, and accessories.",
        "<Picture 6> (Shots 4, 6): fully_preserved - Airi's identity, hair, costume, headphones, proportions, and accessories.\n<Picture 7> (Shots 1, 6): partially_preserved - retain trio arrangement, title hierarchy, pastel palette, and graphic balance while adapting the 9:16 image to 16:9 motion.",
    )
    prompt = prompt.replace(
        "Use clean anime rendering, stable faces and costumes, beat-synchronized cuts, 404 spatial continuity, and native stereo sound.",
        "Use <Picture 7> for overall group-poster balance. Keep clean anime rendering, stable faces and costumes, beat-synchronized cuts, 404 spatial continuity, and native stereo sound.",
    )
    prompt = prompt.replace(
        "Low-angle wide exterior based on <Picture 1>.",
        "Low-angle wide exterior combining <Picture 1> with the trio arrangement and title hierarchy from <Picture 7>.",
    )
    prompt = prompt.replace(
        "the \"妄想天使\" poster hangs by the entrance",
        "the \"妄想天使\" poster with small subtitle \"404 MUSIC LIVE\" hangs by the entrance",
    )
    prompt = prompt.replace(
        "Build with click track, control-panel sound, synchronized footsteps, fabric rustle, and breath to 00:15.",
        "Build with click track, control-panel sound, synchronized footsteps, fabric rustle, and breath to 00:15, echoing <Picture 7>'s group balance.",
    )
    # Keep the poster-reference variant under H3's 7000-byte prompt limit.
    prompt = prompt.replace(
        "Keep all six references separate: location refs <Picture 1>–<Picture 3>, identity refs <Picture 4>–<Picture 6>.",
        "Keep all six references separate.",
    )
    prompt = prompt.replace(
        "Use native diegetic sound: gentle rain, one brief CRT transition burst, rehearsal clicks, and stage-system audio.",
        "Use native diegetic rain, one brief static burst, rehearsal clicks, and stage audio.",
    )
    prompt = prompt.replace(
        "References are reusable, not literal boundary frames.",
        "Refs are reusable, not literal frames.",
    )
    prompt = prompt.replace(
        "No dialogue, singing, humming, spoken counting, subtitles, watermarks, or extra readable text beyond \"404\" and \"妄想天使\".",
        "No dialogue or singing; no subtitles, watermarks, or extra readable text beyond \"404\" and \"妄想天使\".",
    )
    prompt = prompt.replace(
        "The target is a cinematic 16:9 animated music-PV in a retro New Eridu visual language: wet neon, a single brief CRT transition artifact, practical stage lights, cool gray backstage shadows, and cyan, magenta, and amber accents.",
        "The target is a 16:9 animated music-PV with wet neon, brief CRT transition, practical stage lights, cool backstage shadows, and cyan, magenta, amber accents.",
    )
    prompt = prompt.replace("native stereo sound", "stereo sound")
    return prompt


def main() -> None:
    prompt = build_prompt()
    POSTER_PROMPT.write_text(prompt, encoding="utf-8")
    workflow = json.loads(BASE_WORKFLOW.read_text(encoding="utf-8"))
    workflow["36"]["inputs"]["prompt"] = prompt
    workflow["12"]["inputs"]["filename_prefix"] = "MiniMaxH3/wangxiang_tianshi_demo_15s_poster_ref_v2"
    workflow["59"] = {
        "inputs": {"image": "妄想天使_平面手绘海报_9x16_v2.png"},
        "class_type": "LoadImage",
        "_meta": {"title": "Load Poster Reference Image 59"},
    }
    workflow["6"]["inputs"]["ref_images.ref_image_6"] = ["59", 0]
    POSTER_WORKFLOW.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
