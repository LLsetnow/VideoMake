#!/usr/bin/env python3
"""Prepare the four-segment original-character MiniMax H3 Ref2VA project."""

import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
TEMPLATE = PROJECT.parents[1] / "workflows" / "Minimax双时钟图生视频V1_qianxia_audio15s_api.json"
CHARACTER_IMAGE = "原创角色_平面手绘_参考图-v2.png"
PROJECT_NAME = "BV1KZuw6yE2D_原创手绘摇滚角色PV_横屏"


SEGMENTS = [
    {
        "number": "01",
        "duration": 12.0,
        "audio": "01.m4a",
        "seed": 640101,
        "en": r'''subject_definitions:
<Subject 1> is the original single female vocalist shown in the generated image asset "原创角色_平面手绘_参考图-v2.png": a young adult woman with a softly rounded cute face, large bright expressive eyes, an asymmetrical ink-black bob, one electric-pink streak, a small cyan hair clip, a playful confident half-smile, a cream cropped utility jacket with flat magenta and cyan panels, a black sleeveless top, a red-orange narrow neck scarf, a charcoal pleated skirt with a subtle waveform hem, mismatched ankle boots, over-ear headphones around her neck, a small cassette-player charm, cable-like accessories, and a wired handheld microphone. Preserve her face, hair silhouette, clothing construction, limited palette, proportions, accessories, and single-character identity. The generated image is only a character and style reference, not a literal first frame or last frame.
<Audio 1> is the first 12.000 seconds of the supplied source song, directly reused 1:1 as this segment's complete soundtrack, including the female Japanese vocal, distorted electric guitar, bass, drums, dynamics, effects, timing, and stereo balance.

summary:
[reference generation + audio reuse] Create a new 12-second 16:9 horizontal hand-drawn flat 2D character-PV segment starring <Subject 1>. Use the visual language learned from offline analysis of the source PV—black and warm paper-cream fields, hot magenta and cyan screen-print blocks, hard graphic cuts, oversized abstract glyph shapes, grid lines, silhouette echoes, halftone grain, and restrained RGB misregistration—but do not use any source-video frame or source-video input. Reuse <Audio 1> exactly from 00:00.000 to 00:12.000, with no generated replacement music or extra lyrics.

retention_analysis:
<Subject 1> (appears in [Shot 1] through [Shot 4]): fully_preserved - keep the original vocalist's identity, face, asymmetrical black hair with electric-pink streak, cream-magenta-cyan jacket, red-orange scarf, waveform skirt, headphones, cassette charm, microphone, proportions, and flat hand-drawn construction consistent.
<Audio 1>: fully_copy - reuse the complete supplied 12.000-second segment without time stretching, remixing, replacement vocals, or added sound effects.

detailed_description:
The target video is a 16:9 horizontal hand-drawn flat 2D music-PV with bold imperfect ink contours, limited screen-print color fills, warm paper texture, black negative space, hot magenta, cyan, red-orange, thin white rules, modular grids, halftone dots, and occasional red/cyan channel offsets. The visual rhythm is a clean graphic interpretation of high-energy Japanese rock: readable silhouette, fast planar transitions, and a small number of deliberate lyric-like marks. Do not reproduce any source-video character, frame, watermark, logo, or platform interface. <Audio 1> begins at the first frame and remains uninterrupted.

[Shot 1] The video opens on a warm paper-cream field with <Subject 1> standing full body near center, microphone lowered in one hand and headphones touched with the other. A black rectangle slides behind her while cyan and magenta blocks snap into a rough poster grid. Her jacket panels, pink hair streak, scarf, headphones, and microphone remain crisp. The camera performs a slow Push In with small amplitude while her free hand lifts toward the headphones and a loose cable draws one clean curve across the lower frame.

[Shot 2] At 00:03.100, the shot cuts to a waist-up three-quarter view. The background becomes near-black with a cream grid and two offset color silhouettes of <Subject 1> trailing one frame behind her. She turns her chin toward camera, taps the headphone cup once, and brings the microphone toward her mouth without visibly singing. A hot-magenta diagonal bar sweeps behind her at fast speed; the camera Trucks Right with small amplitude and then holds for a beat.

[Shot 3] At 00:06.300, the shot cuts to a full-body side profile on a pale cream panel. The character takes two sharp performance steps from left to right; the waveform hem, scarf, hair streak, headphone cable, and jacket edges respond with simple, controlled hand-drawn motion. Cyan circles expand like audio meters while red and black paper strips cross the background. Use a fast Tracking Shot with small amplitude, then a one-beat Static Shot as she plants her feet.

[Shot 4] At 00:09.300, the shot cuts to a close-up of her eyes, pink hair streak, and microphone grille, then pulls out to a centered half-body pose by 00:10.300. Three thin white rules and a small cyan waveform flash once around her silhouette; no readable lyrics appear yet. The camera Pulls Out with small amplitude at slow speed and holds the final graphic arrangement precisely through 00:12.000.

overall_soundscape:
All vocals, guitars, bass, drums, and source effects already present in <Audio 1> are preserved exactly. Do not add dialogue, foley, crowd noise, room tone, or newly generated impacts.

non_diegetic_music:
<Audio 1> is directly reused as the complete audience-only score from 00:00.000 through 00:12.000. Preserve its Japanese vocal, distorted guitar riff, driving bass, fast kick-and-snare pattern, dynamics, effects, and stereo image without generating replacement music.''',
        "zh": r'''subject_definitions:
<Subject 1> 是生成图资产“原创角色_平面手绘_参考图-v2.png”中的原创单人女歌手：圆润可爱的脸型、明亮偏大的有表现力眼睛、黑色不对称短发、一道电光粉挑染、青色发夹、带热粉与青蓝平面拼贴色块的米白短夹克、黑色无袖上衣、红橙色窄领巾、带波形裙摆的炭灰百褶裙、不对称短靴、挂在脖子上的头戴耳机、小磁带播放器挂件、线缆装饰和有线麦克风。保持她的脸、发型轮廓、服装结构、限定配色、比例、配件和单人身份一致。生成图只作为角色与风格参考，不是字面意义上的首帧或尾帧。
<Audio 1> 是提供的源歌曲前 12.000 秒，直接 1:1 复用为本片段完整音轨，包括日语女声、失真电吉他、贝斯、鼓、动态、效果、时间和立体声平衡。

summary:
[reference generation + audio reuse] 制作一个 12 秒、16:9 横屏的手绘平面 2D 角色 PV 片段，由 <Subject 1> 主演。使用对源 PV 离线分析得到的视觉语言——黑色与暖纸张米白底、热粉和青蓝丝网印刷色块、硬切、超大抽象字形、网格线、剪影残影、网点颗粒和克制的 RGB 错位——但不使用任何源视频画面或源视频输入。完整、准确地复用 <Audio 1> 的 00:00.000–00:12.000，不生成替代音乐或额外歌词。

retention_analysis:
<Subject 1>（出现在 [Shot 1] 至 [Shot 4]）：fully_preserved - 保持原创歌手的身份、脸、带电光粉挑染的不对称黑发、米白/热粉/青蓝夹克、红橙领巾、波形裙、耳机、磁带挂件、麦克风、比例和平面手绘结构一致。
<Audio 1>：fully_copy - 完整复用提供的 12.000 秒音频片段，不变速、不混音、不替换人声、不添加音效。

detailed_description:
成片是 16:9 横屏手绘平面 2D 音乐 PV：粗粝但清晰的墨线、限定丝网印刷色块、暖纸张纹理、黑色负空间、热粉、青蓝、红橙、细白线、模块化网格、半调网点和偶发的红/青通道错位。视觉节奏是对高能日系摇滚的平面化诠释：轮廓清楚、平面转场快速、歌词感图形少而有意。不得复刻源视频角色、画面、水印、Logo 或平台界面。<Audio 1> 从第一帧开始并保持不间断。

[Shot 1] 视频从暖纸张米白底开始，<Subject 1> 全身站在画面中央附近，一只手放低麦克风，另一只手触碰耳机。黑色矩形滑入她身后，青蓝和热粉色块啪地拼成粗略海报网格。保持夹克色块、粉色挑染、领巾、耳机和麦克风清晰。镜头以小幅度慢速 Push In 推近；她抬起空着的手靠近耳机，一条松弛线缆在画面下方划出干净曲线。

[Shot 2] 在 00:03.100，镜头切到腰部以上的三分之四侧面。背景变成近黑色，米白网格和两个落后单帧的 <Subject 1> 红/青错位剪影出现在身后。她朝镜头转下巴，轻敲一次耳机杯，再把麦克风举到嘴边，但不要做明显对嘴演唱。热粉斜条以快速速度掠过身后；镜头小幅度 Truck Right 向右平移，然后停住一拍。

[Shot 3] 在 00:06.300，镜头切到浅米白面板上的全身侧影。角色从左向右做两个利落的舞台步伐；波形裙摆、领巾、粉色发束、耳机线和夹克边缘以简洁可控的手绘方式响应运动。青蓝圆环像音频电平一样扩张，红色和黑色纸条穿过背景。使用小幅度快速 Tracking Shot 跟拍，然后在她站稳时静止一拍。

[Shot 4] 在 00:09.300，镜头切到她的眼睛、粉色发束和麦克风网罩特写，随后在 00:10.300 拉回到居中的半身姿态。三条细白线和一个小青蓝波形围绕剪影闪现一次；此处还不出现可读歌词。镜头以小幅度慢速 Pull Out 拉远，并保持最终图形构图直到 00:12.000。

overall_soundscape:
<Audio 1> 中已有的全部人声、吉他、贝斯、鼓和源效果均原样保留。不要添加对白、拟音、观众声、房间底噪或新生成的撞击声。

non_diegetic_music:
<Audio 1> 作为完整的观众侧配乐从 00:00.000 直接复用到 00:12.000。保持日语人声、失真吉他 riff、推进的贝斯、快速底鼓与军鼓、动态、效果和立体声声场，不生成替代音乐。''',
    },
    {
        "number": "02",
        "duration": 12.0,
        "audio": "02.m4a",
        "seed": 640102,
        "en": r'''subject_definitions:
<Subject 1> is the original single female vocalist shown in the generated image asset "原创角色_平面手绘_参考图-v2.png": a softly rounded cute face with large bright expressive eyes, an asymmetrical ink-black bob with one electric-pink streak, cyan hair clip, cream utility jacket with magenta and cyan panels, black sleeveless top, red-orange scarf, charcoal pleated waveform skirt, mismatched ankle boots, over-ear headphones, cassette-player charm, cable accessories, and wired microphone. Preserve her identity and graphic flat-drawn costume design in every shot. The generated image is only a character/style reference, not a literal frame.
<Audio 1> is the 12.000-second source-song segment from 00:12.000 to 00:24.000, directly reused 1:1 as the complete soundtrack for this segment, with all vocals, instruments, timing, dynamics, and stereo balance unchanged.

summary:
[reference generation + audio reuse] Create a new 12-second 16:9 horizontal hand-drawn flat 2D character-PV segment starring <Subject 1>. Continue the offline-analyzed high-contrast lyric-PV language through modular grids, black panels, paper-cream fields, magenta/cyan overprint, fragmented portrait crops, and kinetic abstract glyphs. Use no source-video frames, no source-video input, and no extra character. Reuse <Audio 1> exactly from 00:00.000 through 00:12.000 of this segment.

retention_analysis:
<Subject 1> (appears in [Shot 1] through [Shot 4]): fully_preserved - preserve the vocalist's face, black-and-pink hair, cream color-block jacket, scarf, waveform skirt, headphones, cassette charm, microphone, proportions, and flat hand-drawn line quality.
<Audio 1>: fully_copy - copy the supplied 12.000-second source segment exactly with no generated replacement audio or extra effects.

detailed_description:
The target video is a 16:9 hand-drawn flat 2D music PV that treats <Subject 1> as a printed poster figure inside a moving collage. Use rough ink contours, paper fibers, black and cream geometric planes, hot magenta and cyan registration shifts, red-orange accents, photocopy grain, thin white grid lines, and hard rhythmic cuts. The design must remain clean enough to read the character silhouette. Do not add readable subtitles or logos in this segment; use only non-readable graphic glyphs and short blocks. <Audio 1> is the only audible source.

[Shot 1] The segment opens on a black rectangular panel with <Subject 1> shown as a cream-and-cyan full-body cut-paper figure standing slightly left of center. A narrow cream grid scrolls vertically behind her while magenta paper fragments assemble around her shoulders and boots. She raises the microphone, shifts her weight once, and lets the headphone cable swing a small arc. The camera is a Static Shot with a tiny Shake Slightly at each graphic hit.

[Shot 2] At 00:02.800, the shot cuts to a close-up of her hand, wired microphone, scarf knot, and waveform skirt edge. The microphone cable becomes a thick black line that traces a geometric loop across the frame. Two cyan circles and one red-orange slash appear like hand-drawn equalizer marks. The camera Pushes In with small amplitude at fast speed, then stops sharply on the beat.

[Shot 3] At 00:05.700, the shot cuts to a wide cream field with three staggered poster panels. The center panel contains <Subject 1> in a three-quarter stance; the left and right panels contain simplified black-and-magenta silhouette echoes with no facial detail. She pivots her shoulders, steps forward once, and turns the microphone toward camera. Use a fast Truck Left with small amplitude as the panels slide in opposite directions, maintaining a flat cut-paper construction.

[Shot 4] At 00:08.900, the shot cuts to a low-angle half-body view. A large black circle expands behind her head, a cyan ring rotates in the opposite direction, and small magenta rectangles flicker at the edges. She lowers the microphone and looks just past camera while the pink streak and scarf move in a short gust. The camera Tilts Up with small amplitude at slow speed, then settles into a graphic freeze. Hold the final arrangement cleanly until 00:12.000.

overall_soundscape:
Preserve all vocals, guitar, bass, drums, and source effects contained in <Audio 1>. Do not add footsteps, crowd ambience, speech, foley, or independent impacts.

non_diegetic_music:
<Audio 1> is directly reused as the complete audience-only score from 00:00.000 to 00:12.000 of this segment. Preserve its original vocal delivery, fast rock instrumentation, beat placement, dynamics, effects, and stereo image.''',
        "zh": r'''subject_definitions:
<Subject 1> 是生成图资产“原创角色_平面手绘_参考图-v2.png”中的原创单人女歌手：圆润可爱的脸型、明亮偏大的眼睛、黑色不对称短发、一道电光粉挑染、青色发夹、带热粉与青蓝色块的米白夹克、黑色无袖上衣、红橙色领巾、炭灰波形百褶裙、不对称短靴、头戴耳机、磁带播放器挂件、线缆配件和有线麦克风。每个镜头都保持她的身份和扁平手绘服装设计一致。生成图只作为角色/风格参考，不是字面意义上的画面帧。
<Audio 1> 是源歌曲 00:12.000–00:24.000 的 12.000 秒片段，直接 1:1 复用为本片段完整音轨，保持所有人声、乐器、时间、动态和立体声平衡不变。

summary:
[reference generation + audio reuse] 制作一个 12 秒、16:9 横屏的手绘平面 2D 角色 PV 片段，由 <Subject 1> 主演。通过模块网格、黑色面板、纸张米白底、热粉/青蓝套印、碎片化人物裁切和动势抽象字形，延续离线分析得到的高对比歌词 PV 语言。不得使用源视频画面或源视频输入，不添加其他角色。完整准确地复用本片段的 <Audio 1>。

retention_analysis:
<Subject 1>（出现在 [Shot 1] 至 [Shot 4]）：fully_preserved - 保持歌手的脸、黑发与粉色挑染、米白色块夹克、领巾、波形裙、耳机、磁带挂件、麦克风、比例和平面手绘线条质量。
<Audio 1>：fully_copy - 原样复制提供的 12.000 秒源片段，不生成替代音频或额外效果。

detailed_description:
成片是 16:9 手绘平面 2D 音乐 PV，把 <Subject 1> 作为印刷海报人物放在移动拼贴内部。使用粗粝墨线、纸张纤维、黑与米白几何面、热粉/青蓝套印错位、红橙色点缀、复印颗粒、细白网格线和跟随节拍的硬切。人物轮廓必须保持清楚。此片段不添加可读字幕或 Logo，只使用不可读抽象字形和短色块。唯一音源是 <Audio 1>。

[Shot 1] 片段从黑色矩形面板开始，<Subject 1> 以米白和青蓝的全身剪纸人物站在偏左位置。细米白网格在她身后垂直滚动，热粉纸片在肩膀和靴子周围组装。她抬起麦克风，移动一次重心，让耳机线小幅摆出弧线。镜头为 Static Shot，在每次图形撞击时只做轻微 Shake Slightly。

[Shot 2] 在 00:02.800，镜头切到手、带线麦克风、领巾结和波形裙摆边缘特写。麦克风线变成一条粗黑线，在画面中勾勒几何环。两个青蓝圆环和一条红橙斜线像手绘均衡器标记一样出现。镜头以小幅度快速 Push In 推近，然后在节拍上突然停住。

[Shot 3] 在 00:05.700，镜头切到宽阔米白场地和三个错位海报面板。中间面板是三分之四姿态的 <Subject 1>；左右面板是简化的黑/热粉剪影残影，不画脸部细节。她转动肩膀，向前走一步，把麦克风朝向镜头。使用小幅度快速 Truck Left 左移，面板向相反方向滑动，保持平面剪纸结构。

[Shot 4] 在 00:08.900，镜头切到低角度半身视图。一个大黑圆在头部后方扩张，青蓝圆环反向旋转，边缘闪过小热粉矩形。她放低麦克风，视线越过镜头，粉色发束和领巾被一阵短风带动。镜头以小幅度慢速 Tilt Up 向上倾斜，随后进入图形定格。保持最终构图直到 00:12.000。

overall_soundscape:
保留 <Audio 1> 中包含的全部人声、吉他、贝斯、鼓和源效果。不要添加脚步、观众环境声、对白、拟音或独立撞击声。

non_diegetic_music:
<Audio 1> 作为完整的观众侧配乐从本片段 00:00.000 直接复用到 00:12.000。保持原始人声演绎、快速摇滚乐器、节拍位置、动态、效果和立体声场。''',
    },
    {
        "number": "03",
        "duration": 12.0,
        "audio": "03.m4a",
        "seed": 640103,
        "en": r'''subject_definitions:
<Subject 1> is the original single female vocalist shown in the generated image asset "原创角色_平面手绘_参考图-v2.png": a softly rounded cute face with large bright expressive eyes, asymmetrical ink-black bob with an electric-pink streak, cyan hair clip, cream jacket with magenta and cyan panels, black top, red-orange scarf, charcoal waveform skirt, mismatched boots, headphones, cassette charm, cable accessories, and wired microphone. Preserve her identity and flat hand-drawn graphic construction. The generated image is only a character/style reference, not a literal frame.
<Audio 1> is the 12.000-second source-song segment from 00:24.000 to 00:36.000, directly reused 1:1 as this segment's complete soundtrack. It includes the dense rock section, the vocal, and the brief drop to exposed vocal and reverberant keyboard near the end.

summary:
[reference generation + audio reuse] Create a new 12-second 16:9 horizontal flat hand-drawn character-PV segment starring <Subject 1>. Build from aggressive black, cream, magenta, cyan, and red-orange collage graphics, then deliberately reduce motion when <Audio 1> drops near the final three seconds. The source video remains offline-only visual inspiration; do not upload it or use its frames. Reuse <Audio 1> exactly from 00:00.000 through 00:12.000 of this segment.

retention_analysis:
<Subject 1> (appears in [Shot 1] through [Shot 4]): fully_preserved - preserve the original vocalist's face, hair streak, jacket panels, scarf, waveform skirt, headphones, cassette charm, microphone, proportions, and hand-drawn flat style.
<Audio 1>: fully_copy - directly copy this 12.000-second source segment, including the instrumental drop, with no time stretch or generated replacement.

detailed_description:
The target video is a 16:9 hand-drawn flat 2D music PV with a controlled arc from dense visual pressure to a sparse suspended moment. Use hard-edged paper planes, black negative space, cream grid paper, hot magenta/cyan overprint, red-orange accent marks, dry ink scratches, photocopy texture, and simple radial geometry. Keep <Subject 1> as the only character. Do not add captions, logos, or source-video frames. <Audio 1> is locked and remains the only soundtrack.

[Shot 1] The video opens on a tight close-up of <Subject 1>'s eyes, pink hair streak, cyan clip, and headphone rim, printed in black with offset magenta and cyan edges. Behind her, a radial burst of cream lines expands from a dark center while small red-orange marks pulse with the rock beat. The camera Pushes In with small amplitude at fast speed, then cuts on the visual peak.

[Shot 2] At 00:03.000, the shot cuts to a wide horizontal stage-like collage. <Subject 1> stands full body on a black floor strip, microphone raised, while oversized cream paper rectangles and cyan rings rotate in layered planes. Her skirt waveform, scarf, hair, and headphone cable move in short, rhythmic gestures. Use a large-amplitude Arc Shot at fast speed with a mechanical lateral move and counter-pan; keep her silhouette readable.

[Shot 3] At 00:06.700, the shot cuts to a fragmented three-quarter portrait. Four rectangular crops of <Subject 1>'s face, microphone, hand, and skirt overlap with thin black gaps. The crops slide a few pixels out of registration, then snap together as magenta and cyan edges align. The camera performs a quick Push In followed by a short Static Shot. Keep the motion graphic and planar, never photorealistic.

[Shot 4] At 00:09.000, when <Audio 1> reaches its brief drop toward exposed vocal and reverberant keyboard, the image abruptly clears to a pale cream field with only a small centered half-body <Subject 1>, her microphone lowered and her eyes turned down. The radial lines stop, the color offsets disappear, and a single thin black line slowly draws beneath her. Use a very slow Pull Out with small amplitude and hold this quiet suspended arrangement until 00:12.000, with no new graphic after the hold begins.

overall_soundscape:
Keep every vocal, guitar, bass, drum, keyboard, and source effect in <Audio 1> unchanged. During the final drop, do not add room tone, breath, footsteps, or new foley; the visual reduction must not alter the copied audio.

non_diegetic_music:
<Audio 1> is directly reused from 00:00.000 to 00:12.000, preserving the dense distorted-guitar rock arrangement and its brief late drop to exposed female vocal with reverberant keyboard. Do not generate replacement music or a transition effect.''',
        "zh": r'''subject_definitions:
<Subject 1> 是生成图资产“原创角色_平面手绘_参考图-v2.png”中的原创单人女歌手：圆润可爱的脸型、明亮偏大的眼睛、黑色不对称短发、电光粉挑染、青色发夹、带热粉与青蓝面板的米白夹克、黑色上衣、红橙领巾、炭灰波形裙、不对称靴子、耳机、磁带挂件、线缆配件和有线麦克风。保持她的身份与平面手绘图形结构一致。生成图只作角色/风格参考，不是字面意义上的画面帧。
<Audio 1> 是源歌曲 00:24.000–00:36.000 的 12.000 秒片段，直接 1:1 复用为本片段完整音轨；其中包括密集摇滚段、人声，以及接近结尾时短暂降为裸人声与带混响键盘的段落。

summary:
[reference generation + audio reuse] 制作一个 12 秒、16:9 横屏的手绘平面角色 PV 片段，由 <Subject 1> 主演。先用黑、米白、热粉、青蓝和红橙色的激烈拼贴图形建立压力，再在 <Audio 1> 最后约三秒进入降落段时有意识地减少运动。源视频只作离线视觉灵感，不上传也不使用源视频帧。完整复用本片段的 <Audio 1>。

retention_analysis:
<Subject 1>（出现在 [Shot 1] 至 [Shot 4]）：fully_preserved - 保持原创歌手的脸、挑染、夹克面板、领巾、波形裙、耳机、磁带挂件、麦克风、比例和平面手绘风格。
<Audio 1>：fully_copy - 直接复制 12.000 秒源片段，包括器乐降落段，不变速、不生成替代音频。

detailed_description:
成片是 16:9 手绘平面 2D 音乐 PV，视觉弧线从密集压力逐步进入稀疏悬停。使用硬边纸张面、黑色负空间、米白网格纸、热粉/青蓝套印、红橙色标记、干墨划痕、复印纹理和简单放射几何。<Subject 1> 是唯一角色。不要添加字幕、Logo 或源视频画面。<Audio 1> 被锁定并保持为唯一音轨。

[Shot 1] 视频从 <Subject 1> 的眼睛、粉色发束、青色发夹和耳机边缘特写开始，用黑色印刷线条绘制，并带有错位的热粉/青蓝边缘。她身后是从暗色中心扩张的米白放射线，小红橙标记跟随摇滚节拍脉动。镜头以小幅度快速 Push In 推近，在视觉峰值处切镜。

[Shot 2] 在 00:03.000，镜头切到宽横幅舞台感拼贴。<Subject 1> 全身站在黑色地面条带上，举起麦克风；超大米白纸片和青蓝圆环在分层平面中旋转。她的波形裙、领巾、头发和耳机线做短促节奏动作。使用大幅度快速 Arc Shot，以机械横向移动配合反向摇摄，保持轮廓清楚。

[Shot 3] 在 00:06.700，镜头切到碎片化三分之四肖像。<Subject 1> 的脸、麦克风、手和裙子被裁成四个矩形，彼此叠在一起，中间留细黑缝。裁片先错开几像素，再在热粉与青蓝边缘对齐时吸附回原位。镜头快速 Push In 后短暂停住。运动保持平面图形化，不得变成写实影像。

[Shot 4] 在 00:09.000，当 <Audio 1> 进入接近裸人声与带混响键盘的短暂降落段时，画面突然清空为浅米白底，只留下居中的小半身 <Subject 1>，她放低麦克风，眼睛向下。放射线停止，色彩错位消失，一条细黑线在她脚下缓慢画出。使用小幅度极慢 Pull Out 拉远，保持安静悬停构图直到 00:12.000，定格开始后不再加入新图形。

overall_soundscape:
保持 <Audio 1> 中的全部人声、吉他、贝斯、鼓、键盘和源效果不变。最后降落段不要添加房间底噪、呼吸、脚步或新拟音；画面减少不能改变复制的音频。

non_diegetic_music:
<Audio 1> 从 00:00.000 直接复用到 00:12.000，保留密集失真吉他摇滚编曲，以及结尾短暂降为裸女声与带混响键盘的段落。不要生成替代音乐或转场音效。''',
    },
    {
        "number": "04",
        "duration": 11.856009,
        "audio": "04.m4a",
        "seed": 640104,
        "en": r'''subject_definitions:
<Subject 1> is the original single female vocalist shown in the generated image asset "原创角色_平面手绘_参考图-v2.png": a softly rounded cute face with large bright expressive eyes, asymmetrical ink-black bob with an electric-pink streak, cyan hair clip, cream utility jacket with magenta and cyan panels, black sleeveless top, red-orange scarf, charcoal pleated waveform skirt, mismatched boots, over-ear headphones, cassette charm, cable accessories, and wired microphone. Preserve her identity, silhouette, costume, and flat hand-drawn screen-print construction. The image is only a character/style reference, not a literal frame.
<Audio 1> is the final 11.856009 seconds of the supplied source song from 00:36.000 to 00:47.856009, directly reused 1:1 as the complete soundtrack for this segment. Preserve its returning full-band climax, repeated vocal phrase, abrupt source ending, and stereo balance.

summary:
[reference generation + audio reuse] Create the final 11.856-second 16:9 horizontal hand-drawn flat 2D character-PV segment starring <Subject 1>. Return from the sparse previous moment into a vivid screen-printed climax with black, cream, hot magenta, cyan, and red-orange geometry, kinetic silhouette echoes, radial lines, and a small amount of lyric art. The only readable lyric art is the exact Japanese phrase "まだ、まだ、まだやる", appearing briefly and cleanly near the middle of the segment. Do not use source-video frames or source-video input. Reuse <Audio 1> exactly through the abrupt source ending at 00:11.856.

retention_analysis:
<Subject 1> (appears in [Shot 1] through [Shot 4]): fully_preserved - preserve the vocalist's face, hair streak, cyan clip, color-block jacket, scarf, waveform skirt, headphones, cassette charm, microphone, proportions, and hand-drawn flat graphic identity.
<Audio 1>: fully_copy - copy the complete final source segment 1:1, including the returning band, vocal phrase, dynamics, abrupt cutoff, and stereo image.

detailed_description:
The target video is the climax of a 16:9 horizontal hand-drawn flat 2D music PV. Use bold ink contours, limited screen-print fills, cream paper, black panels, hot magenta and cyan offset layers, red-orange accent bars, photocopy grain, radial speed lines, and sharp collage cuts. The design should feel like a printed single cover coming alive around one original vocalist. Use very little readable lyric art: the phrase "まだ、まだ、まだやる" is the only readable text, rendered as large rough brush lettering for a short moment; no subtitles, logos, watermarks, or extra text. <Audio 1> begins immediately and ends abruptly with the source.

[Shot 1] The segment opens on a black field as <Subject 1> snaps from the previous quiet pose into a full-body performance stance, microphone raised and one boot forward. Cream radial lines burst from behind her while cyan rings and hot-magenta rectangles expand on the returning full-band hit. Her hair streak, scarf, skirt waveform, headphone cable, and jacket panels move with crisp limited animation. The camera Pushes In with large amplitude at fast speed, then counter-pans slightly to keep her centered.

[Shot 2] At 00:03.000, the shot cuts to a diagonal three-quarter view. <Subject 1> swings the microphone cable in one controlled arc, turns her shoulders toward camera, and opens her free hand. Layered black, cream, cyan, magenta, and red-orange panels slide past her like a fast print registration test. At 00:04.400, the exact lyric art "まだ、まだ、まだやる" appears once in rough white brush lettering across a black strip, holds for less than one second, then breaks into three rectangular fragments and disappears. Keep the text limited, clean, and legible.

[Shot 3] At 00:06.400, the shot cuts to a low-angle close-to-medium view. A large cyan ring and a red-orange ring rotate in opposite directions behind <Subject 1> while a black silhouette echo expands outward. She lifts the microphone toward her mouth, makes one strong head movement, and plants her feet as the headphone cable draws a loop at the bottom edge. Use a fast Tracking Shot with large amplitude and a controlled counter-pan; preserve the face and costume without deformation.

[Shot 4] At 00:09.300, the shot cuts to a final centered full-body poster composition. The cream grid, black panel, cyan ring, magenta bar, red-orange slash, and a small white waveform lock into an asymmetric frame around <Subject 1>. She holds the microphone near her chest, looks directly into camera, and freezes with the free hand open. Use a Static Shot with only a tiny paper-grain flicker. Hold this final image until exactly 00:11.856, then end with the same abrupt cutoff as <Audio 1>; do not add a fade or post-roll.

overall_soundscape:
All female vocals, distorted guitars, bass, drums, effects, and the abrupt ending contained in <Audio 1> are copied unchanged. Do not add dialogue, crowd noise, foley, or extra impact sounds.

non_diegetic_music:
<Audio 1> is directly reused as the complete audience-only score from 00:00.000 through 00:11.856.009 of this segment, preserving the returning full-band climax, repeated vocal phrase, dynamics, exact cutoff, and stereo field. Do not generate replacement music.'''.replace("00:11.856.009", "00:11.856009"),
        "zh": r'''subject_definitions:
<Subject 1> 是生成图资产“原创角色_平面手绘_参考图-v2.png”中的原创单人女歌手：圆润可爱的脸型、明亮偏大的眼睛、黑色不对称短发、电光粉挑染、青色发夹、米白色块夹克、黑色无袖上衣、红橙领巾、炭灰波形裙、不对称靴子、头戴耳机、磁带挂件、线缆配件和有线麦克风。保持她的身份、轮廓、服装和平面手绘丝网印刷结构一致。该图只作角色/风格参考，不是字面意义上的画面帧。
<Audio 1> 是提供的源歌曲最后 11.856009 秒，即 00:36.000–00:47.856009，直接 1:1 复用为本片段完整音轨。保持全乐队回归高潮、重复人声短句、突然结束和立体声平衡。

summary:
[reference generation + audio reuse] 制作最终的 11.856 秒、16:9 横屏手绘平面 2D 角色 PV 片段，由 <Subject 1> 主演。从前一段的稀疏停顿回到鲜明的丝网印刷高潮：黑、米白、热粉、青蓝和红橙几何、动势剪影残影、放射线和少量歌词艺术字。唯一可读歌词艺术字是日文短句“まだ、まだ、まだやる”，在片段中段短暂、干净地出现。不得使用源视频画面或源视频输入。完整复用 <Audio 1>，直到 00:11.856 的源音频突然结束。

retention_analysis:
<Subject 1>（出现在 [Shot 1] 至 [Shot 4]）：fully_preserved - 保持歌手的脸、挑染、青色发夹、色块夹克、领巾、波形裙、耳机、磁带挂件、麦克风、比例和平面手绘图形身份。
<Audio 1>：fully_copy - 1:1 复制最后源片段，包括乐队回归、人声短句、动态、突然截断和立体声场。

detailed_description:
成片是 16:9 横屏手绘平面 2D 音乐 PV 的高潮段。使用粗墨线、限定丝网印刷色块、米白纸张、黑色面板、热粉/青蓝错位层、红橙色条带、复印颗粒、放射速度线和锐利拼贴硬切。整体像一张围绕原创歌手活起来的实体单曲封面。可读歌词艺术字要非常少：只有“まだ、まだ、まだやる”这一句，以粗糙白色笔刷字短暂出现；不添加字幕、Logo、水印或其他文字。<Audio 1> 立即开始，并与源音频一起突然结束。

[Shot 1] 片段从黑底开始，<Subject 1> 从上一段的安静姿态突然切换为全身表演站姿，抬起麦克风，一只靴子向前。全乐队回归的瞬间，米白放射线从她身后爆开，青蓝圆环和热粉矩形扩张。她的粉色挑染、领巾、波形裙、耳机线和夹克面板做清晰的有限动画。镜头以大幅度快速 Push In 推近，再略微反向摇摄让她保持居中。

[Shot 2] 在 00:03.000，镜头切到斜向三分之四视图。<Subject 1> 用受控弧线甩动一次麦克风线，转肩朝向镜头，张开空着的手。黑、米白、青蓝、热粉和红橙面板像快速印刷套色测试一样从她身旁滑过。在 00:04.400，准确的歌词艺术字“まだ、まだ、まだやる”以粗糙白色笔刷字在黑色横条上出现一次，停留不到一秒，然后碎成三个矩形片段消失。文字要少、清晰且可读。

[Shot 3] 在 00:06.400，镜头切到低角度近中景。一个大青蓝圆环与一个红橙圆环在 <Subject 1> 身后反向旋转，黑色剪影残影向外扩张。她把麦克风抬向嘴边，做一个有力的头部动作，然后站稳，耳机线在画面底部勾出一个环。使用大幅度快速 Tracking Shot 跟拍和受控反向摇摄；保持脸和服装不变形。

[Shot 4] 在 00:09.300，镜头切到最终居中的全身海报构图。米白网格、黑色面板、青蓝圆环、热粉条、红橙斜线和一个小白色波形在 <Subject 1> 周围锁定成非对称画框。她把麦克风停在胸前，直视镜头，张开空着的手并定格。镜头为 Static Shot，只保留极轻的纸张颗粒闪烁。保持到准确的 00:11.856，然后与 <Audio 1> 一样突然结束，不加淡出或尾帧延长。

overall_soundscape:
<Audio 1> 中的全部女声、失真吉他、贝斯、鼓、效果和突然结束均原样复制。不要添加对白、观众声、拟音或额外撞击声。

non_diegetic_music:
<Audio 1> 作为完整观众侧配乐从 00:00.000 直接复用到本片段 00:11.856，保持全乐队高潮回归、重复人声短句、动态、准确截断和立体声场。不生成替代音乐。''',
    },
]


def main() -> None:
    for segment in SEGMENTS:
        number = segment["number"]
        folder = PROJECT / number
        folder.mkdir(parents=True, exist_ok=True)
        prompt_path = folder / f"{PROJECT_NAME}_片段{number}_prompt.txt"
        zh_path = folder / f"{PROJECT_NAME}_片段{number}_prompt_zh.txt"
        workflow_path = folder / f"{PROJECT_NAME}_片段{number}_workflow_api.json"
        prompt_path.write_text(segment["en"].strip() + "\n", encoding="utf-8")
        zh_path.write_text(segment["zh"].strip() + "\n", encoding="utf-8")

        workflow = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        workflow["14"]["inputs"]["value"] = segment["duration"]
        workflow["16"]["inputs"]["aspect_ratio"] = "16:9 (Widescreen)"
        workflow["16"]["inputs"]["megapixels"] = 1.0
        workflow["36"]["inputs"]["prompt"] = segment["en"]
        workflow["37"]["inputs"]["image"] = CHARACTER_IMAGE
        workflow["52"]["inputs"]["audio"] = segment["audio"]
        workflow["53"]["inputs"]["duration"] = segment["duration"]
        workflow["9"]["inputs"]["noise_seed"] = segment["seed"]
        workflow["12"]["inputs"]["filename_prefix"] = (
            f"MiniMaxH3/{PROJECT_NAME}_片段{number}"
        )
        conditioning = workflow["6"]["inputs"]
        conditioning["task_type"] = "Ref2VA"
        conditioning["audio_mode"] = "lock_source"
        conditioning["audio_denoise_strength"] = 0
        conditioning["add_source_as_reference"] = False
        conditioning["prompt_primary_audio_ordinal"] = 1
        workflow["12"]["inputs"]["trim_to_audio"] = True
        workflow_path.write_text(
            json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(workflow_path)


if __name__ == "__main__":
    main()
