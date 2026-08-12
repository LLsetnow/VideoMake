"""Prepare the poster-reference variant of the 15-second demo."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
BASE_WORKFLOW = PROJECT / "妄想天使_前15秒Demo_workflow_api.json"
BASE_PROMPT = PROJECT / "妄想天使_前15秒Demo_prompt.txt"
POSTER_PROMPT = PROJECT / "妄想天使_前15秒Demo_poster_ref_v1_prompt.txt"
POSTER_WORKFLOW = PROJECT / "妄想天使_前15秒Demo_poster_ref_v1_workflow_api.json"


def build_prompt() -> str:
    prompt = BASE_PROMPT.read_text(encoding="utf-8")
    prompt = prompt.replace(
        "<Picture 6> is the identity reference for <Subject 3>, preserving her face, hairstyle, costume, body proportions, headphones, and accessories.",
        "<Picture 6> is the identity reference for <Subject 3>, preserving her face, hairstyle, costume, body proportions, headphones, and accessories.\n<Picture 7> is the generated 9:16 poster reference, guiding the trio arrangement, title hierarchy, rainy neon palette, and group-poster composition; it is not a literal boundary frame.",
    )
    prompt = prompt.replace(
        "Preserve identity and costume construction while creating original beat-synchronized cuts, native stereo sound, rain, rehearsal clicks, and diegetic stage audio.",
        "Use <Picture 7> as the overall key-visual reference while adapting its vertical composition to 16:9. Preserve identity and costume construction, with native stereo rain, rehearsal clicks, and diegetic stage audio.",
    )
    prompt = prompt.replace(
        "<Picture 6> (used in [Shot 4], [Shot 6]): fully_preserved - preserve <Subject 3>'s face, hairstyle, costume, headphones, proportions, and accessories.",
        "<Picture 6> (used in [Shot 4], [Shot 6]): fully_preserved - preserve <Subject 3>'s face, hairstyle, costume, headphones, proportions, and accessories.\n<Picture 7> (used as the overall key visual in [Shot 1] and [Shot 6]): partially_preserved - retain its trio arrangement, title hierarchy, rainy neon palette, and poster balance while adapting the 9:16 image to 16:9 motion.",
    )
    prompt = prompt.replace(
        "Use clean anime rendering, stable faces and costumes, 404 spatial continuity, beat-synchronized cuts, and native stereo sound.",
        "Use <Picture 7> for the overall group-poster balance. Keep clean anime rendering, stable faces and costumes, 404 spatial continuity, beat-synchronized cuts, and native stereo sound.",
    )
    prompt = prompt.replace(
        "The video opens in a low-angle wide shot based on <Picture 1>.",
        "The video opens in a low-angle wide shot combining <Picture 1> with the trio composition and title hierarchy from <Picture 7>.",
    )
    prompt = prompt.replace(
        "A poster reading \"妄想天使\" hangs beside the entrance.",
        "A poster reading \"妄想天使\" with the small subtitle \"404 MUSIC LIVE\" hangs beside the entrance.",
    )
    prompt = prompt.replace(
        "The positions remain readable against <Picture 2>, with identities consistent with <Picture 4>, <Picture 5>, and <Picture 6>.",
        "The positions remain readable against <Picture 2> and echo the group balance from <Picture 7>, with identities consistent with <Picture 4>, <Picture 5>, and <Picture 6>.",
    )
    prompt = prompt.replace(
        "<Picture 1> (used in [Shot 1]): fully_preserved - preserve the wet 404 exterior, neon sign, rain, poster, and street-lighting relationship.",
        "<Picture 1> (used in [Shot 1]): fully_preserved - preserve the 404 exterior, rain, neon, and poster setting.",
    )
    prompt = prompt.replace(
        "<Picture 2> (used in [Shot 2], [Shot 3], [Shot 5], [Shot 6]): fully_preserved - preserve the empty stage geography, microphone, hanging lights, and venue lighting.",
        "<Picture 2> (used in [Shot 2], [Shot 3], [Shot 5], [Shot 6]): fully_preserved - preserve the empty stage, microphone, lights, and venue geography.",
    )
    prompt = prompt.replace(
        "<Picture 3> (used in [Shot 4]): fully_preserved - preserve the backstage corridor, doorway, control-room entrance, and practical-light colors.",
        "<Picture 3> (used in [Shot 4]): fully_preserved - preserve the backstage corridor, doorway, and practical lights.",
    )
    prompt = prompt.replace(
        "<Picture 4> (used in [Shot 3], [Shot 4], [Shot 5], [Shot 6]): fully_preserved - preserve <Subject 1>'s face, ash-gray hair, costume, backpack, proportions, and accessories.",
        "<Picture 4> (used in [Shot 3], [Shot 4], [Shot 5], [Shot 6]): fully_preserved - preserve <Subject 1>'s face, hair, costume, proportions, and accessories.",
    )
    prompt = prompt.replace(
        "<Picture 5> (used in [Shot 5], [Shot 6]): fully_preserved - preserve <Subject 2>'s identity, hairstyle, costume, proportions, and accessories.",
        "<Picture 5> (used in [Shot 5], [Shot 6]): fully_preserved - preserve <Subject 2>'s identity, costume, proportions, and accessories.",
    )
    prompt = prompt.replace(
        "Native diegetic sound follows the timeline: steady rain and distant New Eridu traffic, neon transformer hum, CRT static, empty-stage reverberation, light relay clicks, pencil friction, paper movement, door hinge, footsteps, headphone click, two hand claps, control-panel sounds, fabric rustle, synchronized rehearsal clicks, and quiet breathing. The low-frequency rehearsal pulse comes from the 404 stage system and is audible to the characters; generate no dialogue or crowd noise.",
        "Native diegetic sound: rain, distant traffic, neon hum, CRT static, empty-stage reverberation, relay clicks, pencil and paper, door hinge, footsteps, headphone click, claps, control-panel sounds, fabric rustle, rehearsal clicks, and quiet breathing. The stage pulse is audible to the characters; no dialogue or crowd noise.",
    )
    return prompt


def main() -> None:
    prompt = build_prompt()
    POSTER_PROMPT.write_text(prompt, encoding="utf-8")
    workflow = json.loads(BASE_WORKFLOW.read_text(encoding="utf-8"))
    workflow["36"]["inputs"]["prompt"] = prompt
    workflow["12"]["inputs"]["filename_prefix"] = "MiniMaxH3/wangxiang_tianshi_demo_15s_poster_ref_v1"
    workflow["59"] = {
        "inputs": {"image": "妄想天使_404音乐现场海报_9x16_v1.png"},
        "class_type": "LoadImage",
        "_meta": {"title": "Load Poster Reference Image 59"},
    }
    workflow["6"]["inputs"]["ref_images.ref_image_6"] = ["59", 0]
    POSTER_WORKFLOW.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
