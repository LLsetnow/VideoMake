# Final QC

- RH local task: `task_23bceafe17d0`
- Remote task: `2096332771729928193`
- Remote workflow: `2094755110367227906`
- Raw returned file: `output/chinatsu_bv1sc_style_480p_20260906_rh_raw.mp4`
- Delivered file: `output/chinatsu_bv1sc_style_480p_20260906.mp4`

## Delivered media

- Container: MP4
- Video: H.264, 480×864, 24 fps, 267 frames
- Audio: AAC, 32 kHz, stereo
- Duration: 11.125000 seconds
- Full decode: passed with `ffmpeg -f null -`
- Visual check: `qa/final_contact_sheet.jpg`

The remote raw file was 11.541667 seconds. It was retained for traceability, and the delivered copy was re-encoded and trimmed to the 11.125-second control-video duration requested for this project.
