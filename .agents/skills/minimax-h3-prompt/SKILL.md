---
name: minimax-h3-prompt
description: |
  Write or rewrite prompts for the MiniMax H3 video model (MiniMaxAI/MiniMax-H3) using its official prompt-writing format. MiniMax H3 is a multimodal model that turns text/image/video/audio references into 5–15s video WITH native audio, so a good prompt is a timed audiovisual production brief, not a still-image caption.
  Use this skill whenever the user is:
  - Writing or improving a prompt for MiniMax H3 (Hailuo H3) video generation.
  - Filling the prompt/text node of a MiniMax H3 ComfyUI workflow (e.g. "Minimax H3 All-in-One Reference / 视频参考", "MiniMax H3 FL2VA", Ref2VA — the node 7 text).
  - Asking how to prompt MiniMax H3, which mode to use (T2VA / I2VA / FL2VA / L2VA / full-reference), how to write camera moves, dialogue, on-screen text, soundscape, or reference labels.
  All emitted prompt fields must be in English except dialogue/lyrics inside <d> and text visibly in the scene. Full official guides are bundled under reference/.
---

# MiniMax H3 Prompt Writing

MiniMax H3 reads text + up to 9 images / 3 videos / 3 audios (≤12 files) in one context and returns 5–15s of up to 2K video with native stereo audio. Picture AND sound are generated together, so prompt along a **timeline**: stable subject → timed observable action → camera path → lighting → audio. Start with one shot; add shots only once basic motion is reliable.

**Language rule:** write every field in English. Keep the original language only inside `<d>…</d>` (dialogue/lyrics) and for text physically visible in the scene (in `"double quotes"`).

## Step 1 — Pick the mode

| Mode | Input | Use when |
|---|---|---|
| **T2VA** | text only | pure text → video |
| **I2VA** | first frame image | animate forward from a given first frame |
| **FL2VA** | first + last frame | interpolate a path between two frames |
| **L2VA** | last frame | infer an opening that lands on a given last frame |
| **Full-reference** | any mix of image/video/audio references | reuse a character/scene/motion/voice via labeled references (this is the "All-in-One Reference / Ref2VA" workflow) |

T2VA/I2VA/FL2VA/L2VA use `reference/VIDEO_PROMPT_WRITING_GUIDE_base_en.md`.
Full-reference uses `reference/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`.

## Base mode (T2VA / I2VA / FL2VA / L2VA)

**Line 1 = alignment instruction** (skip for T2VA), then one blank line, then the three core fields.

- I2VA: `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`
- FL2VA: `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.`
- L2VA: `How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.`

(`N` = actual final shot index; `S.SS` = effective duration, 2 decimals.)

**Three core fields:**

```text
integrated_multimodal_description: [Shot 1] <style + composition> ... <action> ... <camera> ... <speaker/dialogue> ...
overall_soundscape: <ambience + physical/human sounds, 1–4 English sentences>
non_diegetic_music: <audience-only score: instrumentation/tempo/rhythm/dynamics, or N/A>
```

Keyframe placement patterns:
- I2VA: first-frame anchor → action onset → continuous development → result.
- FL2VA: usually one shot; first-frame state → intermediate changes → narrowing differences → last-frame state.
- L2VA: plausible earlier state → transition path → converge onto the reference in the final shot.

## Full-reference mode — six sections, in order

```text
subject_definitions: <one line per tracked reference, each label + role + key features>
summary: [<task-type prefix>] <one paragraph using the defined labels>
retention_analysis: <one line per label with a fixed relationship marker>
detailed_description: <shot-by-shot body, style stated BEFORE [Shot 1], labels inserted where they apply, ~350–500 English words>
overall_soundscape: <ambience/physical sound summary>
non_diegetic_music: <audience-only score, or N/A>
```

**Reference labels** (meaning stays fixed across all sections):

| Label | Use for |
|---|---|
| `<Subject N>` | reusable visible content: person/animal/object, scene, clothing/prop/effect, style/action/pose |
| `<Picture N>` | an image used as a concrete frame (first/key/last) or storyboard anchor |
| `<Video N>` | whole-video relationship: editing source, continuation start, or camera/cut/rhythm structure |
| `<Audio N>` | copied or referenced audio; if it maps to a speaker write `<Audio N> … (Sx)` reusing the global speaker ID |

**`summary` task-type prefixes** (combine with ` + `, no repeats): `keyframe completion`, `reference generation`, `video editing`, `video continuation`, `audio reuse`, `audio reference`. Presence of a video/audio file alone does NOT create a type — only its actual role does.

**`retention_analysis` markers** — visible (`<Subject/Picture/Video>`): `fully_preserved` · `partially_preserved` · `attribute_transfer` · `weak_reference`. Audio (`<Audio>`): `fully_copy` · `partially_copy` · `reference` · `weak_reference`.

## Shared building blocks (both modes)

**Shots & cuts:** `[Shot 1]` has NO timestamp. Later: `[Shot N] At MM:SS.mmm, the camera cuts to …` with strictly increasing times inside the duration. A cut must add new info (subject/space/state/viewpoint/time); for a mere distance/angle change use camera motion instead.

**Camera motion = type (+ amplitude) (+ speed)**, written as natural English inside the shot (omit medium amplitude / normal speed):

| Type | Type | Type |
|---|---|---|
| Zoom In/Out | Push In / Pull Out | Pan Left/Right |
| Truck Left/Right | Tilt Up/Down | Pedestal Up/Down |
| Arc Shot | Tracking Shot | Static Shot |
| Shake Slightly/Strongly | POV | Roll Clockwise/Counterclockwise |

Amplitude: `with small amplitude` / `with large amplitude`. Speed: `at slow speed` / `at fast speed`.
e.g. `The camera pushes in with small amplitude at slow speed toward the letter in her hands.`

**Speakers & dialogue:** stable IDs `(S1)`, `(S2)`, group `(S1,S2)`; same ID across shots; silent characters get no ID. On first appearance establish a stable voice identity (type/age/gender/on-off-screen/pitch/timbre/rate/accent) OUTSIDE `<d>`. Inside `<d>` put only `[Language]` + verbatim words (preserve punctuation, no translation):
`The quiet, breathy young woman (S1) says: <d>[English] I get off at the next station.</d>`
Voiceover: use `says in an off-screen voiceover` and add `while his lips remain completely closed.` after the block. Across a cut use `<scenetrans>` + a continuity phrase; truncated-by-end uses `<cutoff>`.

**On-screen text:** put visible signage/subtitles in English double quotes, verbatim, no translation: `A red neon sign reading "营业中" glows above the doorway.`

**overall_soundscape:** 1–4 sentences of ambience + physical + non-verbal human sounds; NOT dialogue/singing/diegetic music (those live in the description). `N/A` only for full silence.
**non_diegetic_music:** 1–3 sentences, audience-only score — instrumentation/tempo/rhythm/dynamics, no mood words; `N/A` if none. Music the characters can hear (radio, singing) is diegetic → goes in the description.

## Applying to the OPC ComfyUI workflows

The `Minimax H3 All-in-One Reference*` and `MiniMax H3 FL2VA` workflows expose the prompt in their text node (e.g. node 7). Free-form natural-language prompts work, but the structured formats above give the most control. For the All-in-One Reference (Ref2VA) graph, node 16 = the `<Subject>`/`<Picture>` character image and node 17 = the driving `<Video>` — describe both with labels in `detailed_description`, and if you keep the driving video's audio, note it as `<Audio N>` reuse.

## Quality checklist

- Correct mode chosen; alignment instruction present & first line (base I2VA/FL2VA/L2VA).
- Every claim is visible or audible — no abstract mood/emotion words.
- `[Shot 1]` timeless; later cut times strictly increasing and within duration.
- Camera moves phrased naturally in-shot, not stacked as end labels.
- Dialogue verbatim inside `<d>[Language]…</d>`; speaker IDs stable and reused.
- Full-reference: 6 sections in order; labels defined once and consistent; task-type prefix matches actual roles; retention markers from the fixed set.
- Sound split correctly: dialogue/diegetic → description; ambience → soundscape; audience-only → non_diegetic_music.

For anything ambiguous (voiceover, dialogue across cuts, multi-asset subjects, audio-speaker mapping, full worked examples), read the matching file in `reference/`.
