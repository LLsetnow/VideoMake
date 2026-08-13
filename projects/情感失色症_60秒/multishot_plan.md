# 《情感失色症》60 秒多镜头方案

multishot_plan_status: confirmed
total_duration: 60.00s
shot_count: 23
edit_rhythm: 23 shots, 22 internal cuts plus 3 segment boundaries; average shot duration 2.61s. Internal cuts are snapped to Librosa beat/onset candidates listed in `cutlist.csv`.
continuity_strategy: One androgynous figure in a fully covered white jumpsuit remains the visual anchor. The same white grid laboratory, circular aperture, transparent blocks, cyan/magenta pulse markers, scanlines, and restrained chromatic aberration recur across all four 15-second generations. Segment boundaries are visual state changes only; the source audio continues from the exact corresponding timecode.

## Story arc

1. 00:00-15.00 — Emotionless baseline: sterile white laboratory, the figure is almost colorless and only responds to the beat with small geometric pulses.
2. 15.00-30.00 — First color: pulses become spatial, leave trails, and temporarily stain the room.
3. 30.00-45.00 — Overload: the pulse system multiplies, RGB separation and geometric echoes intensify, then blow out to white.
4. 45.00-60.00 — Fade: the figure returns to stillness; nearly all color drains away except one tiny cyan trace.

## Exact cut map

`0.000 / 3.179 / 5.227 / 7.445 / 10.283 / 12.032 / 15.000 / 17.077 / 19.605 / 22.752 / 25.280 / 27.808 / 30.000 / 32.224 / 34.752 / 37.280 / 39.808 / 42.336 / 45.000 / 48.021 / 51.179 / 54.176 / 56.693 / 60.000`

## Continuity ledger

- Identity: androgynous, short silver hair, calm expressionless face, fully covered white high-neck jumpsuit; no extra people.
- Visual language: white/graphite base, cyan and magenta beat blocks, thin grids, transparent towers, circular aperture, scanlines, slight RGB offset, clean electro-pop/chiptune motion design.
- Audio: the corresponding 15-second WAV is copied 1:1 as `lock_source`; no generated music, vocals, dialogue, or extra effects.
- Delivery: four 15-second 16:9 H3 Ref2VA clips, stitched in order, then remuxed with the original first 60 seconds of the MP3 and checked at 24 fps.
