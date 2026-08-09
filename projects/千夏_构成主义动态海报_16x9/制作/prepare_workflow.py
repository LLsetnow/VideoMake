#!/usr/bin/env python3
"""Prepare the 16:9 MiniMax H3 Ref2VA workflow and its prompt."""

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).resolve().parents[3] / "projects" / "千夏_复合构成主义_15秒" / "千夏_复合构成主义_15秒_workflow_api.json"
WORKFLOW = PROJECT / "千夏_构成主义动态海报_16x9_workflow_api.json"
PROMPT_FILE = PROJECT / "千夏_构成主义动态海报_16x9_prompt.txt"


PROMPT = r'''subject_definitions:
<Subject 1> is the single anime girl and static flat poster design shown in <Picture 1>, with short wavy ash-gray hair, a large turquoise bow, pale pink eyes, a white short-sleeve blouse, a red necktie with small white star details, a pink backpack, white wing-like side accessories, a black layered skirt, pink-and-white striped arm warmers and leg warmers, pale skin, and pink-and-white platform shoes. Preserve her exact face, hairstyle, body proportions, costume construction, accessory placement, colors, recognizable identity, and the poster's thick dark contour lines.
<Picture 1> is the provided 2:3 flat 2D constructivist character poster used as the opening frame and the central composition anchor for the target video. It defines the character's pose, poster crop, pink-white-mint graphic language, and full-body framing.
<Audio 1> is the first 15 seconds of the supplied Hypervoid music track, directly reused 1:1 as the target video's complete final audio track, including its original timing, musical content, vocals if present, dynamics, effects, and stereo balance.

summary:
[reference generation + keyframe completion + audio reuse] Create a new 15-second 16:9 horizontal experimental motion poster starring <Subject 1>. Start from <Picture 1> as the centered static poster card, then animate only the surrounding 2D graphic system: warm-white negative space, deep crimson blocks, blue-green blocks, thin black rules, circular frames, diagonal perspective lines, and exact narrow English typography reading "ZENLESS ZONE ZERO", "CHINATSU", and "00". Reuse <Audio 1> exactly from 00:00.000 through 00:15.000. Keep the design flat, screen-printed, editorial, and controlled; do not create additional characters, logos, watermarks, subtitles, or platform UI.

retention_analysis:
<Subject 1> (appears in [Shot 1] through [Shot 5]): fully_preserved - preserve the girl's identity, face, hairstyle, turquoise bow, wings, backpack, red star-detail necktie, layered skirt, striped warmers, platform shoes, pose, and complete poster-panel silhouette.
<Picture 1> ([Shot 1] opening frame and central composition anchor): fully_preserved - keep the supplied poster crop, full-body framing, flat color fills, pink-white-mint palette, and thick contour-line language while adding only external animated graphic layers.
<Audio 1>: fully_copy - <Audio 1> is reused 1:1 as the complete final soundtrack with no generated replacement music or extra sound effects.

detailed_description:
The target video is a 16:9 horizontal flat 2D constructivist motion poster with a warm-white field, deep crimson and blue-green geometric planes, thin black rules, modular grid alignments, circular frames, diagonal perspective bars, subtle paper grain, and narrow sans-serif typography. The central <Subject 1> remains a static vertical poster card based on <Picture 1>; only the surrounding graphic elements move. Preserve all visible text exactly as "ZENLESS ZONE ZERO", "CHINATSU", and "00". Use crisp hard-edged shapes, restrained easing, and short holds; do not use 3D rendering, photorealism, soft airbrush, character deformation, extra people, logos, watermarks, or unreadable replacement text. <Audio 1> begins at the first frame and remains uninterrupted.

[Shot 1] The video opens on <Picture 1> as a centered full-body vertical poster card inside a wide horizontal field. The card is bordered by a thin black frame, with a large black circular outline behind it. A deep crimson wedge occupies the upper-left corner, a blue-green diagonal plane enters from the upper-right, and the large red "00" is parked on the left. The camera is nearly a Static Shot with a very small Push In at slow speed. Hold the opening graphic for a clean beat while the poster card slides down from slightly above frame and settles without changing <Subject 1>.

[Shot 2] At 00:03.000, the camera cuts to the same horizontal poster system with a new geometric arrangement. A deep crimson diagonal bar slides from left to right, a blue-green bar cuts upward from the lower-left, and the exact title "ZENLESS ZONE ZERO" enters from the right with tight tracking. The vertical word "CHINATSU" rises along the left side of the card. Use a smooth Truck Right with small amplitude at slow speed; keep the central poster stable and fully readable.

[Shot 3] At 00:06.300, the shot cuts to a slightly wider graphic view. A second blue-green circular ring expands and drifts in the lower-right quadrant while the black ring behind the card rotates slowly. Thin horizontal and vertical rules slide a few pixels out of alignment, then snap back to the modular grid. Use a restrained Arc Shot with small amplitude at normal speed, but keep <Subject 1> static and sharp inside the card.

[Shot 4] At 00:09.500, the shot cuts to a denser composition. Two fine rules and a short crimson line assemble on the right, while the red "CHINATSU" title slides in low across the right field and briefly intersects the circular frame. The large "00" on the left holds as an anchor. Use a quick Push In with small amplitude followed by a short Pull Out; all movement is planar, graphic, and clean, with no motion blur over the character.

[Shot 5] At 00:12.400, the shot cuts to the final locked poster arrangement. The rings, diagonal planes, thin rules, "ZENLESS ZONE ZERO", "CHINATSU", and "00" settle into a balanced asymmetric grid around the centered <Subject 1>. The camera becomes a Static Shot. Hold the final poster-like tableau precisely until 00:15.000, with one restrained blue-green line gliding to a stop and no new visual elements after the hold begins.

overall_soundscape:
No diegetic ambience, dialogue, voiceover, or independently generated sound effects are required. Do not add foley or impacts; the only audible track is the copied <Audio 1>.

non_diegetic_music:
<Audio 1> is directly reused as the complete audience-only score from 00:00.000 through 00:15.000. Preserve its exact timing, musical content, dynamics, effects, and stereo image, and do not generate replacement music.
'''


def main() -> None:
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    data["16"]["inputs"]["aspect_ratio"] = "16:9 (Widescreen)"
    # The connected 24 GB instance reliably handles the verified 1.0 MP
    # landscape preset; 2.0 MP reaches the sampler's GPU memory limit.
    data["16"]["inputs"]["megapixels"] = 1.0
    data["36"]["inputs"]["prompt"] = PROMPT
    data["37"]["inputs"]["image"] = "chinatsu-constructivist-poster-v2.png"
    data["52"]["inputs"]["audio"] = "Hypervoid.m4a"
    data["12"]["inputs"]["filename_prefix"] = "MiniMaxH3/chinatsu_constructivist_16x9_15s"
    WORKFLOW.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    PROMPT_FILE.write_text(PROMPT, encoding="utf-8")
    print(WORKFLOW)
    print(PROMPT_FILE)


if __name__ == "__main__":
    main()
