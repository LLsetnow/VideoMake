# -*- coding: utf-8 -*-
"""生成 8 段 H3 全参考提示词（EN/ZH）与 workflow JSON。"""
import json, pathlib

ROOT = pathlib.Path("projects/初音未来_梦核_竖屏视频")
SHOTS = ROOT / "shots"
TEMPLATE = json.load(open("workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json", encoding="utf-8"))

SUBJECTS_EN = """subject_definitions:
<Subject 1> is Hatsune Miku, the anime girl shown in <Picture 1>, with signature turquoise twin-tails, blue-green eyes, and her default outfit: a black cropped jacket, white puffy sleeves with white arm warmers, a black necktie, a dark pleated skirt, and thigh-high black boots. Preserve her exact face, hairstyle, body proportions, costume details, and colors from the reference image in every shot.
<Subject 2> is the empty indoor pool room shown in <Picture 2>: teal mosaic tiles covering the walls and floor, a perfectly still cyan water surface, tall windows with overexposed soft daylight, drifting haze, and a quiet dreamcore liminal-space atmosphere. Preserve the room layout, teal color palette, lighting direction, and mood in every shot.
<Audio 1> is the complete audio track of this segment, directly reused 1:1 as the target video's complete final audio track, including all music, rhythm, ambience, dynamics, and stereo balance."""

SUBJECTS_ZH = """subject_definitions（主体定义）：
<Subject 1> 是 <Picture 1> 中展示的动漫少女初音未来，拥有标志性的青绿色双马尾、蓝绿色眼眸，以及默认服装：黑色短款外套、带白色袖套的白色泡泡袖、黑色领带、深色百褶短裙和过膝黑色长靴。每个镜头都要保持参考图中她的精确面容、发型、身材比例、服装细节与配色。
<Subject 2> 是 <Picture 2> 中展示的空无一人的室内泳池大厅：墙面与地面铺满蓝绿色马赛克瓷砖、静止如镜的青色水面、透入柔和过曝日光的高窗、漂浮的雾气，以及安静而梦核化的阈限空间氛围。每个镜头都要保持房间布局、蓝绿色配色、光照方向与氛围。
<Audio 1> 是本段的完整音轨，将 1:1 直接复用为目标视频的完整最终音轨，包括全部音乐、节奏、环境声、动态与立体声平衡。"""

STYLE_EN = "The target video is a 9:16 vertical dreamcore music-video segment in a cinematic mixed-media style: soft overexposure, hazy soft focus, pastel teal color grading, subtle film grain and a nostalgic 2000s digital texture, in a quietly melancholic liminal mood. Camera movement and cuts stay in sync with the existing rhythm of <Audio 1>."
STYLE_ZH = "目标视频是一段 9:16 竖屏梦核音乐视频片段，采用电影感混合媒介风格：柔和过曝、朦胧柔焦、粉彩青绿色调、轻微胶片颗粒与怀旧的 2000 年代数字质感，整体是安静忧郁的阈限空间氛围。镜头运动与剪辑始终与 <Audio 1> 的既有节奏保持同步。"

SOUNDSCAPE_EN = """overall_soundscape:
A quiet, reverberant indoor pool hall ambience continues throughout the segment: faint water lapping, soft distant drips, and a low airy room tone beneath the copied music."""
SOUNDSCAPE_ZH = """overall_soundscape（整体声景）：
整段持续着空旷、带混响的室内泳池大厅环境声：微弱的池水拍打声、远处轻柔的水滴声，以及复制音乐下方的低柔空气感房间底噪。"""

MUSIC_EN = """non_diegetic_music:
<Audio 1> is directly reused 1:1 as the complete audience-only score. Preserve its exact timing, tempo, beat placement, dynamics, and stereo image from 00:00.000 to the end of the segment. Do not generate replacement music."""
MUSIC_ZH = """non_diegetic_music（非叙事音乐）：
<Audio 1> 被 1:1 直接复用为完整的观众专属配乐。从 00:00.000 到本段结束，保持其精确的时机、速度、节拍位置、动态与立体声像。不要生成替代音乐。"""

# (summary_en, summary_zh, shots_en, shots_zh, retention_shots, duration)
SEGMENTS = [
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, opening her slow dreamlike journey through the liminal pool hall. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>，开启她在阈限泳池大厅中的缓慢梦境旅程。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The video opens on the wide, mostly empty pool room of <Subject 2>: teal mosaic walls, a long still cyan water surface reflecting the tall windows, soft haze drifting in the air, and overexposed daylight spilling from the side windows. <Subject 1>, Hatsune Miku in her default outfit, stands at the pool edge in the lower-center of the frame, full body visible, facing the water with her back three-quarters turned toward the camera and her turquoise twin-tails hanging down her back. She slowly turns her head toward the camera with a calm, slightly wistful expression, her blue-green eyes catching the window light. The camera pushes in with small amplitude at slow speed. <Audio 1> begins immediately and remains unchanged.\n"
            "[Shot 2] At 00:08.000, the shot cuts to a medium shot of <Subject 1> from a slightly lower angle, still at the pool edge. She looks down at the mirror-still water at her feet, and a faint reflection of her face appears on the cyan surface. She takes one small step forward; the hem of her pleated skirt sways gently and her boots make no sound on the wet tiles. A soft breeze stirs her hair. The camera drifts laterally to the left with small amplitude at slow speed, keeping her centered in the frame."
        ),
        shots_zh=(
            "[Shot 1] 视频开场是 <Subject 2> 空旷的泳池大厅全景：蓝绿色马赛克墙面、映出高窗的长长静止青色水面、空气中漂浮的柔和雾气，以及侧窗倾泻的过曝日光。<Subject 1> 初音未来身着默认服装站在画面下方中央的池边，全身入镜，背对镜头约四分之三侧面朝向水面，青绿色双马尾垂在背后。她缓缓转头看向镜头，神情平静而略带惆怅，蓝绿色眼眸映着窗光。镜头以慢速、小幅度向前推近。<Audio 1> 立即开始并保持不变。\n"
            "[Shot 2] 00:08.000 处，镜头切到稍低机位的中景，<Subject 1> 仍在池边。她低头看向脚边静止如镜的水面，青色水面上浮现她面容的淡淡倒影。她向前迈出一小步，百褶裙摆轻轻晃动，靴子踩在湿瓷砖上无声无息。一阵微风拂动她的发丝。镜头以慢速、小幅度向左横移，让她保持在画面中央。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as the first lo-fi beat enters and she begins walking along the pool. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：第一声 lo-fi 节拍进入，她开始在池边行走。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on <Subject 1> kneeling at the pool edge of <Subject 2>, seen in a medium close-up from the side; the teal mosaic wall and the still cyan water fill the background. Her fingertips hover just above the water surface as the first soft lo-fi beat of <Audio 1> enters, and tiny ripples begin to spread on the water beneath her hand. Her expression is calm and attentive, her blue-green eyes fixed on the water. Soft window light glows on her face and twin-tails. The camera pushes in with small amplitude at slow speed.\n"
            "[Shot 2] At 00:07.000, as the lo-fi beat of <Audio 1> settles in, the shot cuts to a full-body side view of <Subject 1> standing up from the pool edge and walking slowly along the pool from left to right. Her twin-tails, jacket, and pleated skirt respond naturally to each gentle step, and a faint reflection of her body glides across the water beside her. The teal mosaic wall and mirror-like water slide past in the background. Use a smooth lateral tracking shot matching her slow walking speed."
        ),
        shots_zh=(
            "[Shot 1] 开场镜头是 <Subject 1> 蹲在 <Subject 2> 池边，侧面中近景；背景是蓝绿色马赛克墙与静止的青色水面。她的指尖悬在水面正上方，<Audio 1> 的第一声轻柔 lo-fi 节拍进入，她手下的水面开始泛起细小的涟漪。她神情平静专注，蓝绿色眼眸注视着水面。柔和的窗光映在她的面容与双马尾上。镜头以慢速、小幅度向前推近。\n"
            "[Shot 2] 00:07.000 处，随着 <Audio 1> 的 lo-fi 节拍稳定下来，镜头切到全身侧面：<Subject 1> 从池边站起身，沿着泳池从右向左缓缓行走。双马尾、外套与百褶裙随着每一步自然摆动，她身体的淡淡倒影在水面旁滑过。蓝绿色马赛克墙与镜面般的水面在背景中后退。使用与她缓慢步速匹配的平滑侧面跟拍。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, continuing her slow walk along the pool with the steady lo-fi beat. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：在稳定的 lo-fi 节拍中延续她沿池边的缓慢行走。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens continuing <Subject 1>'s slow walk along the pool edge in <Subject 2>, filmed in a full-body lateral tracking shot from the side. She walks with a gentle rhythm matching the steady lo-fi beat of <Audio 1>; her twin-tails sway behind her, the hem of her pleated skirt moves with each step, and the puffy sleeves of her jacket catch the soft window light. Reflections of the tall windows glide across the still cyan water beside her, and the haze drifts slowly through the teal mosaic hall. Keep the tracking shot smooth and at slow speed.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a medium shot of <Subject 1> as she stops walking and turns slightly toward the camera. She trails one hand along the teal mosaic wall behind her, her fingers brushing the tiles, then lets her arm drop and looks quietly at the water, her expression calm and dreamy. The camera pushes in with small amplitude at slow speed while the beat of <Audio 1> continues steadily."
        ),
        shots_zh=(
            "[Shot 1] 开场延续 <Subject 1> 在 <Subject 2> 中沿池边的缓慢行走，采用侧面全身跟拍。她踩着与 <Audio 1> 稳定 lo-fi 节拍相合的轻柔节奏行走；双马尾在身后摆动，百褶裙摆随每一步晃动，外套的泡泡袖接住柔和的窗光。高窗的倒影在她身旁静止的青色水面上滑过，雾气缓缓穿过蓝绿色马赛克大厅。保持跟拍平滑、速度缓慢。\n"
            "[Shot 2] 00:07.000 处，镜头切到中景：<Subject 1> 停下脚步，微微转向镜头。她一只手沿着身后的蓝绿色马赛克墙轻轻划过，指尖拂过瓷砖，然后放下手臂，安静地望向水面，神情平静而迷离。在 <Audio 1> 稳定持续的节拍中，镜头以慢速、小幅度向前推近。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she touches the still water and gazes up into the window light. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她触碰静止的水面，又抬眸望向窗光。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an intimate close-up of <Subject 1>'s hand as her fingertips touch the still water of the pool room in <Subject 2>. Concentric ripples spread slowly across the cyan surface, shattering the reflected window light into shimmering fragments that dance across the teal tiles. The camera tilts up with small amplitude at slow speed from the water to her calm face, her blue-green eyes following the ripples.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a medium shot of <Subject 1> kneeling at the pool edge, now looking up toward the tall overexposed windows; soft halation blooms around her silhouette and her twin-tails are lifted by a faint breeze. The melodic layer of <Audio 1> brightens as she gazes into the light, her expression quietly longing. The camera pushes in with small amplitude at slow speed."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 1> 指尖触碰 <Subject 2> 泳池水面的大特写。同心涟漪在青色水面上缓缓扩散，把倒映的窗光打碎成闪烁的光斑，在蓝绿色瓷砖上跃动。镜头从水面以慢速、小幅度上摇到她的面容，蓝绿色眼眸追随着涟漪。\n"
            "[Shot 2] 00:07.000 处，镜头切到中景：<Subject 1> 仍蹲在池边，此刻抬眸望向高处的过曝窗户；她的轮廓泛起柔和光晕，双马尾被一阵微风轻轻托起。<Audio 1> 的旋律层变得明亮，她凝视着光，神情安静而向往。镜头以慢速、小幅度向前推近。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as the music texture brightens and she raises one hand toward the light. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：音乐织体变得明亮，她向光抬起一只手。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a wide view of <Subject 1> walking to the center of the empty pool room of <Subject 2>, surrounded by drifting haze and shallow mirror-like puddles of window light on the wet floor. She stops and stands still, small in the frame, as the musical texture of <Audio 1> grows brighter and fuller, and her reflection stretches faintly across the damp tiles toward the camera. The camera pushes in with small amplitude at slow speed toward her.\n"
            "[Shot 2] At 00:08.000, the shot cuts to a medium close-up of <Subject 1> slowly raising one hand toward the overexposed window light, fingers slightly spread, as the intensified melody of <Audio 1> plays. Her eyes follow her raised hand; her twin-tails and the hem of her skirt drift in a slow breeze. The camera tilts up with small amplitude at slow speed, following her hand toward the bright light."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 空旷泳池大厅的广角画面：<Subject 1> 走向大厅中央，周围是漂浮的雾气与湿地上浅浅的镜面状窗光水洼。<Audio 1> 的音乐织体变得明亮而饱满，她停下脚步静静站立，在画面中显得小巧，她的倒影淡淡地越过潮湿瓷砖向镜头延伸。镜头以慢速、小幅度向她推近。\n"
            "[Shot 2] 00:08.000 处，镜头切到中近景：<Audio 1> 的旋律加强，<Subject 1> 缓缓向过曝的窗光抬起一只手，手指微微张开。她的目光追随着抬起的手，双马尾与裙摆随风轻摆。镜头以慢速、小幅度上摇，跟随她的手朝向明亮的光。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she turns slowly in place and then settles facing the camera with closed eyes. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她原地缓缓旋转，随后面向镜头闭眼安定下来。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on <Subject 1> standing at the pool edge in <Subject 2>, seen in a full-body wide shot with the teal mosaic hall and the still water around her. She begins a slow, graceful full turn in place; her twin-tails, jacket, and pleated skirt flow with the motion while the steady beat of <Audio 1> plays, and her reflection turns beneath her on the water. The camera performs a slow arc shot around her with small amplitude, keeping her centered.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a medium shot of <Subject 1> as she completes the turn and faces the camera, her eyes gently closed and a faint, peaceful smile forming on her lips. A soft lens flare blooms behind her from the window light. The camera holds nearly static with very subtle handheld vibration as the beat of <Audio 1> continues."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 1> 站在 <Subject 2> 池边，全身广角镜头，蓝绿色马赛克大厅与静止的水面环绕着她。随着 <Audio 1> 稳定节拍的推进，她开始缓慢而优雅地原地旋转一周；双马尾、外套与百褶裙随动作飘动，水面上的倒影也随之转动。镜头围绕她做慢速、小幅度的环绕运动，始终让她保持在画面中央。\n"
            "[Shot 2] 00:07.000 处，镜头切到中景：<Subject 1> 完成旋转面向镜头，双眼轻轻闭合，嘴角浮起一丝平静的微笑。窗光在她身后绽开柔和的镜头光晕。在 <Audio 1> 持续的节拍中，镜头近乎静止，只带极轻微的手持晃动。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she gazes at her reflection, reaches toward it, then sits at the pool edge. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她凝视水中倒影、伸手触碰，然后在池边坐下。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a medium close-up of <Subject 1> kneeling at the pool edge in <Subject 2>, looking down at her own reflection in the still water. She slowly reaches her hand toward the reflection, and the spreading ripples distort her mirrored face. Her expression is calm and nostalgic, her blue-green eyes half-lidded. The camera pushes in with small amplitude at slow speed toward the water.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a wide shot of <Subject 1> sitting down at the pool edge, her legs above the water, gazing quietly into the distance of the vast empty teal hall. The camera pulls out with small amplitude at slow speed, revealing more of the mosaic architecture, the haze, and the soft window light, while the music of <Audio 1> grows softer and more spacious."
        ),
        shots_zh=(
            "[Shot 1] 开场是中近景：<Subject 1> 蹲在 <Subject 2> 池边，低头看着静止水面中自己的倒影。她缓缓向倒影伸出手，扩散的涟漪扭曲了倒映的面容。她神情平静而怀旧，蓝绿色眼眸半阖。镜头以慢速、小幅度向水面推近。\n"
            "[Shot 2] 00:07.000 处，镜头切到广角：<Subject 1> 在池边坐下，双腿悬在水面上方，安静地望向空旷蓝绿色大厅的远方。<Audio 1> 的音乐变得更加轻柔开阔，镜头以慢速、小幅度拉远，展现出更多的马赛克建筑、雾气与柔和的窗光。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        duration=7.3846,
        summary_en="[reference generation + audio reuse] Create a final 7.4-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she closes her eyes and the light fades like a dream ending. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段收尾的 7.4 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她闭上双眼，光线渐暗，如同梦境结束。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The final segment is one continuous shot: <Subject 1> sits at the pool edge of <Subject 2>, her eyes slowly closing and her breathing calm, as the light from the windows gradually softens and dims like a dream fading. A faint breeze lifts the edges of her twin-tails, hair, and pleated skirt, and the still cyan water darkens gently. The camera pushes in with very small amplitude at slow speed, holding her in a gentle centered composition while <Audio 1> fades out. The video ends on the soft, held final frame exactly when the audio ends."
        ),
        shots_zh=(
            "[Shot 1] 收尾段是单个连续镜头：<Subject 1> 坐在 <Subject 2> 池边，双眼缓缓闭合，呼吸平静，窗光渐渐变柔变暗，如同梦境正在消退。微风轻轻掀起她的双马尾、发丝与百褶裙边，静止的青色水面也随之缓缓变暗。镜头以极小的幅度、缓慢推近，将她温柔地保持在居中构图，<Audio 1> 随之淡出。视频在音频结束的瞬间，定格于柔软而安宁的最后一帧。"
        ),
        retention_shots="[Shot 1]",
    ),
]

SEEDS = [574001 + i for i in range(8)]

def build_prompt_en(seg):
    return "\n\n".join([
        SUBJECTS_EN,
        seg["summary_en"],
        "retention_analysis:\n"
        f"<Subject 1> (appears in {seg['retention_shots']}): fully_preserved - the character's identity and all defining visual features from <Picture 1> remain consistent throughout the entire segment.\n"
        f"<Subject 2> (appears in {seg['retention_shots']}): fully_preserved - the pool room's teal mosaic architecture, still water, window light, haze, and dreamcore atmosphere remain consistent throughout the entire segment.\n"
        "<Audio 1>: fully_copy - <Audio 1> is reused 1:1 as the segment's complete final audio track.",
        "detailed_description:\n" + STYLE_EN + "\n" + seg["shots_en"],
        SOUNDSCAPE_EN,
        MUSIC_EN,
    ])

def build_prompt_zh(seg):
    return "\n\n".join([
        SUBJECTS_ZH,
        seg["summary_zh"],
        "retention_analysis（保留分析）：\n"
        f"<Subject 1>（出现在 {seg['retention_shots']}）：fully_preserved - 角色身份及 <Picture 1> 中所有标志性视觉特征在整个片段中保持一致。\n"
        f"<Subject 2>（出现在 {seg['retention_shots']}）：fully_preserved - 泳池大厅的蓝绿色马赛克建筑、静止水面、窗光、雾气与梦核氛围在整个片段中保持一致。\n"
        "<Audio 1>：fully_copy - <Audio 1> 被 1:1 复用为本片段完整最终音轨。",
        "detailed_description（详细描述）：\n" + STYLE_ZH + "\n" + seg["shots_zh"],
        SOUNDSCAPE_ZH,
        MUSIC_ZH,
    ])

def build_workflow(seg, n):
    wf = json.loads(json.dumps(TEMPLATE))
    wf["36"]["inputs"]["prompt"] = build_prompt_en(seg)
    wf["14"]["inputs"]["value"] = seg["duration"]
    wf["53"]["inputs"]["duration"] = seg["duration"]
    wf["12"]["inputs"]["filename_prefix"] = f"MiniMaxH3/menghe_miku_S{n}_v1"
    wf["9"]["inputs"]["noise_seed"] = SEEDS[n - 1]
    # 第二张参考图：背景图 LoadImage 节点
    wf["60"] = {
        "inputs": {"image": ""},
        "class_type": "LoadImage",
        "_meta": {"title": "Load Image (background)"},
    }
    wf["6"]["inputs"]["ref_images.ref_image_1"] = ["60", 0]
    return wf

for i, seg in enumerate(SEGMENTS, start=1):
    (SHOTS / f"S{i}_prompt.txt").write_text(build_prompt_en(seg), encoding="utf-8")
    (SHOTS / f"S{i}_prompt_zh.txt").write_text(build_prompt_zh(seg), encoding="utf-8")
    wf = build_workflow(seg, i)
    (SHOTS / f"S{i}_workflow_api.json").write_text(json.dumps(wf, ensure_ascii=False, indent=1), encoding="utf-8")
    # JSON 校验
    json.loads((SHOTS / f"S{i}_workflow_api.json").read_text(encoding="utf-8"))
    en = build_prompt_en(seg)
    assert len(en) <= 7000, f"S{i} prompt too long: {len(en)}"
    print(f"S{i}: prompt {len(en)} chars, duration {seg['duration']}, seed {SEEDS[i-1]}, JSON OK")

print("ALL OK")
