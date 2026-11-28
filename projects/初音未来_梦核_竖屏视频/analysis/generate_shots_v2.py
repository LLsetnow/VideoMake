# -*- coding: utf-8 -*-
"""v2：多场景梦核漫游 —— 生成 8 段 H3 全参考提示词（EN/ZH）与 workflow JSON。

场景路线：泳池(开场) → 无尽走廊 → 云海房间 → 天空云海 → 泳池(折返) → 泳池(律动) → 天空(安坐) → 泳池(梦醒闭环)
"""
import json, pathlib

ROOT = pathlib.Path("projects/初音未来_梦核_竖屏视频")
SHOTS = ROOT / "shots"
TEMPLATE = json.load(open("workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json", encoding="utf-8"))

SCENES = {
    "pool": "the empty indoor pool room shown in <Picture 2>: teal mosaic tiles covering the walls and floor, a perfectly still cyan water surface, tall windows with overexposed soft daylight, drifting haze, and a quiet dreamcore liminal-space atmosphere",
    "corridor": "the endless corridor shown in <Picture 2>: a long straight hallway with teal tiles and painted walls, rows of fluorescent ceiling light fixtures with a few flickering tubes, half-open doors along both sides, a distant vanishing point dissolving into an overexposed white glow, a slightly reflective floor, and thin drifting mist",
    "cloudroom": "the cloud-filled room shown in <Picture 2>: a vast empty cream-and-pale-teal room whose floor is a fluffy pale-teal cloud sea, a white staircase rising toward the sky and disappearing into light, a few floating pastel-teal clouds, soft volumetric light beams from tall windows, and drifting light dust",
    "sky": "the open sky shown in <Picture 2>: an expansive teal-tinted dusk sky with layered fluffy pale-cyan and blue-green clouds stretching to the horizon, soft overexposed warm-white light breaking through the clouds in volumetric beams, faint floating cloud islands and a distant white staircase remnant, and drifting light dust",
}
SCENES_ZH = {
    "pool": "<Subject 2> 是 <Picture 2> 中展示的空无一人的室内泳池大厅：墙面与地面铺满蓝绿色马赛克瓷砖、静止如镜的青色水面、透入柔和过曝日光的高窗、漂浮的雾气，以及安静而梦核化的阈限空间氛围",
    "corridor": "<Subject 2> 是 <Picture 2> 中展示的无尽走廊：一条笔直延伸的室内走廊，蓝绿色瓷砖与漆面墙，天花板上成排的荧光灯管中有几根闪烁，两侧每隔一段有半开的门，远处消失点融化在过曝的白色光晕中，地面微微反光，飘着薄雾",
    "cloudroom": "<Subject 2> 是 <Picture 2> 中展示的云海房间：一间巨大空旷的奶油白与淡青绿房间，地面是蓬松的浅青绿色云海，一道白色楼梯向天空延伸并消失在光中，天花板附近漂浮着几朵粉彩青绿云朵，高窗投下柔和的体积光，空中飘着光尘",
    "sky": "<Subject 2> 是 <Picture 2> 中展示的天空云海：开阔的青绿色黄昏天空，层层蓬松的浅青与蓝绿色云海铺向地平线，柔和的过曝暖白光线穿过云层形成体积光，远处漂浮着淡淡的云岛与一截白色楼梯残影，空中飘着光尘",
}

SUBJECTS_EN_TMPL = """subject_definitions:
<Subject 1> is Hatsune Miku, the anime girl shown in <Picture 1>, with signature turquoise twin-tails, blue-green eyes, and her default outfit: a black cropped jacket, white puffy sleeves with white arm warmers, a black necktie, a dark pleated skirt, and thigh-high black boots. Preserve her exact face, hairstyle, body proportions, costume details, and colors from the reference image in every shot.
<Subject 2> is {scene}. Preserve the scene's layout, teal color palette, lighting direction, and dreamcore mood in every shot.
<Audio 1> is the complete audio track of this segment, directly reused 1:1 as the target video's complete final audio track, including all music, rhythm, ambience, dynamics, and stereo balance."""

SUBJECTS_ZH_TMPL = """subject_definitions（主体定义）：
<Subject 1> 是 <Picture 1> 中展示的动漫少女初音未来，拥有标志性的青绿色双马尾、蓝绿色眼眸，以及默认服装：黑色短款外套、带白色袖套的白色泡泡袖、黑色领带、深色百褶短裙和过膝黑色长靴。每个镜头都要保持参考图中她的精确面容、发型、身材比例、服装细节与配色。
{scene_zh}。每个镜头都要保持该场景的布局、蓝绿色配色、光照方向与梦核氛围。
<Audio 1> 是本段的完整音轨，将 1:1 直接复用为目标视频的完整最终音轨，包括全部音乐、节奏、环境声、动态与立体声平衡。"""

STYLE_EN = "The target video is a 9:16 vertical dreamcore music-video segment in a cinematic mixed-media style: soft overexposure, hazy soft focus, pastel teal color grading, subtle film grain and a nostalgic 2000s digital texture, in a quietly melancholic liminal mood. Camera movement and cuts stay in sync with the existing rhythm of <Audio 1>."
STYLE_ZH = "目标视频是一段 9:16 竖屏梦核音乐视频片段，采用电影感混合媒介风格：柔和过曝、朦胧柔焦、粉彩青绿色调、轻微胶片颗粒与怀旧的 2000 年代数字质感，整体是安静忧郁的阈限空间氛围。镜头运动与剪辑始终与 <Audio 1> 的既有节奏保持同步。"

SOUNDSCAPE_EN = """overall_soundscape:
A quiet, reverberant dream-space ambience continues throughout the segment: faint distant water or air sounds, soft tonal hum, and a low room tone beneath the copied music."""
SOUNDSCAPE_ZH = """overall_soundscape（整体声景）：
整段持续着空旷、带混响的梦境空间环境声：微弱遥远的水声或风声、轻柔的嗡鸣，以及复制音乐下方的低柔空气感底噪。"""

MUSIC_EN = """non_diegetic_music:
<Audio 1> is directly reused 1:1 as the complete audience-only score. Preserve its exact timing, tempo, beat placement, dynamics, and stereo image from 00:00.000 to the end of the segment. Do not generate replacement music."""
MUSIC_ZH = """non_diegetic_music（非叙事音乐）：
<Audio 1> 被 1:1 直接复用为完整的观众专属配乐。从 00:00.000 到本段结束，保持其精确的时机、速度、节拍位置、动态与立体声像。不要生成替代音乐。"""

# scene, duration, summary_en, summary_zh, shots_en, shots_zh, retention_shots
SEGMENTS = [
    dict(
        scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, opening her dreamlike journey at the pool's edge. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>，在泳池边开启她的梦境旅程。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The video opens on the wide, mostly empty pool room of <Subject 2>: teal mosaic walls, a long still cyan water surface reflecting the tall windows, soft haze drifting in the air, and overexposed daylight spilling from the side windows. <Subject 1>, Hatsune Miku in her default outfit, stands at the pool edge in the lower-center of the frame, full body visible, facing the water with her back to the camera and her turquoise twin-tails hanging down her back. She slowly turns her head back toward the camera with a calm, slightly wistful expression, her blue-green eyes catching the window light. The camera pushes in with small amplitude at slow speed. <Audio 1> begins immediately and remains unchanged.\n"
            "[Shot 2] At 00:08.000, the shot cuts to a medium shot of <Subject 1> now crouching at the pool edge. She trails one hand through the still cyan water; concentric ripples spread across the surface and shatter the reflected window light into shimmering fragments on the teal tiles. Her reflection bends and ripples beneath her fingers. A soft breeze stirs her hair. The camera drifts laterally to the left with small amplitude at slow speed, keeping her centered in the frame."
        ),
        shots_zh=(
            "[Shot 1] 视频开场是 <Subject 2> 空旷的泳池大厅全景：蓝绿色马赛克墙面、映出高窗的长长静止青色水面、空气中漂浮的柔和雾气，以及侧窗倾泻的过曝日光。<Subject 1> 初音未来身着默认服装站在画面下方中央的池边，全身入镜，背对镜头面向水面，青绿色双马尾垂在背后。她缓缓回头望向镜头，神情平静而略带惆怅，蓝绿色眼眸映着窗光。镜头以慢速、小幅度向前推近。<Audio 1> 立即开始并保持不变。\n"
            "[Shot 2] 00:08.000 处，镜头切到中景：<Subject 1> 蹲在池边，一只手划过静止的青色水面，同心涟漪在水面扩散，把倒映的窗光打碎成闪烁的光斑洒在蓝绿色瓷砖上。她的倒影在指下弯曲、波动。一阵微风拂动她的发丝。镜头以慢速、小幅度向左横移，让她保持在画面中央。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="corridor", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as the first lo-fi beat enters and she walks through the endless corridor, then stops and looks back. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：第一声 lo-fi 节拍进入，她走过无尽走廊，随后停下回头。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on <Subject 2>, the endless teal corridor, seen in a full-body wide shot with a strong one-point perspective toward the glowing vanishing point. <Subject 1> walks slowly away from the camera down the center of the corridor, her twin-tails, jacket, and pleated skirt swaying with each gentle step as the first soft lo-fi beat of <Audio 1> enters; a few fluorescent tubes flicker softly overhead and thin mist drifts along the floor. The camera follows her with a smooth lateral tracking shot at slow speed, keeping her small in the frame.\n"
            "[Shot 2] At 00:07.000, as the lo-fi beat of <Audio 1> settles in, the shot cuts to a medium close-up of <Subject 1> as she stops walking and slowly turns back to look toward the camera. The corridor stretches into deep perspective behind her, its far end dissolving into the overexposed white glow. Her expression is calm and slightly curious. The camera pushes in with small amplitude at slow speed."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 无尽蓝绿色走廊的全景：强烈的单点透视通向发光的消失点。<Subject 1> 在 <Audio 1> 第一声轻柔 lo-fi 节拍进入时，沿着走廊中央缓缓向远处走去，双马尾、外套与百褶裙随每一步轻轻摆动；头顶几根荧光灯管微微闪烁，薄雾沿地面飘动。镜头以缓慢的平滑跟拍跟随她，让她在画面中保持小巧。\n"
            "[Shot 2] 00:07.000 处，随着 <Audio 1> 的 lo-fi 节拍稳定，镜头切到中近景：<Subject 1> 停下脚步，缓缓转身回望镜头。她身后走廊延伸出深邃的透视，尽头融化在过曝的白色光晕中。她神情平静而略带好奇。镜头以慢速、小幅度向前推近。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="cloudroom", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she crosses the cloud-filled room and climbs the white staircase toward the sky. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她穿过云海房间，踏上白色楼梯向天空走去。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a wide view of <Subject 2>, the vast cream-and-pale-teal room filled with a fluffy cloud sea on the floor and floating pastel clouds near the ceiling; volumetric light beams fall from the tall windows. <Subject 1> walks across the cloud sea toward the white staircase that rises into the light, her boots sinking slightly into the soft cloud surface and stirring wisps of mist. The camera pushes in with small amplitude at slow speed behind her.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a medium shot of <Subject 1> stepping onto the white staircase, one hand resting on the railing. She looks back down over her shoulder at the cloud sea below, and drifting light dust floats around her. The camera tilts up with small amplitude at slow speed, following her ascent while the melody of <Audio 1> continues."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 云海房间的广角画面：巨大的奶油白与淡青绿房间，地面是蓬松的云海，天花板附近漂浮着粉彩云朵，高窗投下体积光束。<Subject 1> 穿过云海走向那道没入光中的白色楼梯，靴子微微陷入柔软的云面，带起缕缕雾气。镜头在她身后以慢速、小幅度向前推近。\n"
            "[Shot 2] 00:07.000 处，镜头切到中景：<Subject 1> 踏上白色楼梯，一只手搭在扶手上。她回头向下方云海望去，周围漂浮着细小的光尘。<Audio 1> 旋律继续，镜头以慢速、小幅度上摇，跟随她向上攀登。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="sky", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as the staircase ends in the open sky and she steps into the cloud sea and floats. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：楼梯在开阔天空中结束，她步入云海漂浮。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on <Subject 2>, the open teal-tinted dusk sky with layered clouds and volumetric light; the top of a white staircase emerges from the clouds at the left edge of the frame. <Subject 1> steps off the final stair onto the cloud surface and walks a few steps into the open sky, her twin-tails and skirt drifting in the wind while golden-teal light dust floats around her. The camera performs a slow arc shot around her with small amplitude.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a medium close-up of <Subject 1> standing on the clouds with her arms gently spread, eyes half-closed, hair and skirt flowing in the breeze as the brightened melody of <Audio 1> plays. Layers of cloud stretch into the distance behind her. The camera drifts laterally with small amplitude at slow speed, keeping her centered."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 开阔的青绿色黄昏天空：层叠的云海与体积光，画面左侧一道白色楼梯顶端从云中探出。<Subject 1> 走下最后一级台阶踏上云面，在开阔天空中前行几步，双马尾与裙摆在风中飘动，青金色光尘环绕着她。镜头以慢速、小幅度环绕她运镜。\n"
            "[Shot 2] 00:07.000 处，镜头切到中近景：<Subject 1> 站在云上，双臂轻轻张开，双眼半阖，发丝与裙摆随风飘动，<Audio 1> 的旋律变得明亮。层层云海在她身后延伸向远方。镜头以慢速、小幅度横移，让她保持在画面中央。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as the dream circles back to the pool room, the light texture brightens, and she touches the water. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：梦境折返回泳池大厅，音乐织体变得明亮，她触碰水面。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a wide view of <Subject 1> walking to the center of the empty pool room of <Subject 2>, surrounded by drifting haze and shallow mirror-like puddles of window light on the wet floor, as if the dream has folded back to its beginning. She stops and stands still, small in the frame, while the musical texture of <Audio 1> grows brighter and fuller; her reflection stretches faintly across the damp tiles. The camera pushes in with small amplitude at slow speed toward her.\n"
            "[Shot 2] At 00:08.000, the shot cuts to an intimate close-up of <Subject 1>'s hand as her fingertips touch the still water. Concentric ripples spread slowly across the cyan surface, shattering the reflected window light into shimmering fragments that dance across the teal tiles. The camera tilts up with small amplitude at slow speed from the water to her calm face as she looks up toward the overexposed windows, her blue-green eyes catching the light."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 1> 走向 <Subject 2> 空旷泳池大厅中央的广角画面：周围漂浮着雾气，湿地上有浅浅的镜面状窗光水洼，仿佛梦境折返回起点。<Audio 1> 的音乐织体变得明亮而饱满，她停下脚步静静站立，在画面中显得小巧，倒影淡淡地越过潮湿瓷砖向镜头延伸。镜头以慢速、小幅度向她推近。\n"
            "[Shot 2] 00:08.000 处，镜头切到指尖触碰静止水面的大特写。同心涟漪在青色水面上缓缓扩散，把倒映的窗光打碎成闪烁的光斑在蓝绿色瓷砖上跃动。镜头从水面以慢速、小幅度上摇到她平静的面容，她抬眸望向过曝的高窗，蓝绿色眼眸映着光。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she turns slowly in place at the pool edge and then settles facing the camera with closed eyes. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她在池边原地缓缓旋转，随后面向镜头闭眼安定下来。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
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
        scene="sky", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she sits on the clouds and gazes into the distance, and the music grows softer. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她坐在云上眺望远方，音乐变得轻柔。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a medium close-up of <Subject 1> sitting on the soft cloud surface of <Subject 2>, her legs folded beside her, looking out over the layered cloud sea toward the glowing horizon; her twin-tails and skirt edges drift in the breeze and light dust floats in the air. The camera pushes in with small amplitude at slow speed.\n"
            "[Shot 2] At 00:07.000, the shot cuts to a wide shot of <Subject 1> sitting on the cloud at the edge of the frame, small against the vast open teal sky, gazing into the distance as the music of <Audio 1> grows softer and more spacious. The camera pulls out with small amplitude at slow speed, revealing the immense sky and the distant staircase remnant."
        ),
        shots_zh=(
            "[Shot 1] 开场是中近景：<Subject 1> 坐在 <Subject 2> 柔软的云面上，双腿盘在身旁，眺望层叠云海尽头的发光地平线；双马尾与裙摆边缘随风轻飘，光尘在空气中漂浮。镜头以慢速、小幅度向前推近。\n"
            "[Shot 2] 00:07.000 处，镜头切到广角：<Subject 1> 坐在画面边缘的云上，在开阔的青绿色天空衬托下显得渺小，静静望向远方，<Audio 1> 的音乐变得更加轻柔开阔。镜头以慢速、小幅度拉远，展现出无垠的天空与远处那道楼梯残影。"
        ),
        retention_shots="[Shot 1], [Shot 2]",
    ),
    dict(
        scene="pool", duration=7.3846,
        summary_en="[reference generation + audio reuse] Create a final 7.4-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>, as she closes her eyes at the pool edge and the light fades like a dream ending where it began. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段收尾的 7.4 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：她在池边闭上双眼，光线渐暗，如同梦境在起点结束。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The final segment is one continuous shot: <Subject 1> sits at the pool edge of <Subject 2> where her dream began, her eyes slowly closing and her breathing calm, as the light from the windows gradually softens and dims like a dream fading. A faint breeze lifts the edges of her twin-tails, hair, and pleated skirt, and the still cyan water darkens gently. The camera pushes in with very small amplitude at slow speed, holding her in a gentle centered composition while <Audio 1> fades out. The video ends on the soft, held final frame exactly when the audio ends."
        ),
        shots_zh=(
            "[Shot 1] 收尾段是单个连续镜头：<Subject 1> 坐在她梦境开始的地方——<Subject 2> 的池边，双眼缓缓闭合，呼吸平静，窗光渐渐变柔变暗，如同梦境正在消退。微风轻轻掀起她的双马尾、发丝与百褶裙边，静止的青色水面也随之缓缓变暗。镜头以极小的幅度、缓慢推近，将她温柔地保持在居中构图，<Audio 1> 随之淡出。视频在音频结束的瞬间，定格于柔软而安宁的最后一帧。"
        ),
        retention_shots="[Shot 1]",
    ),
]

SEEDS = [584001 + i for i in range(8)]
# 每段对应的背景参考图（Picture 2）
SCENE_BG = {
    "pool": "ref/background/初音未来_梦核_背景_9x16_v1.png",
    "corridor": "ref/background/初音未来_梦核_走廊_9x16_v1.png",
    "cloudroom": "ref/background/初音未来_梦核_云海房间_9x16_v1.png",
    "sky": "ref/background/初音未来_梦核_天空云海_9x16_v1.png",
}

def build_prompt_en(seg):
    return "\n\n".join([
        SUBJECTS_EN_TMPL.format(scene=SCENES[seg["scene"]]),
        seg["summary_en"],
        "retention_analysis:\n"
        f"<Subject 1> (appears in {seg['retention_shots']}): fully_preserved - the character's identity and all defining visual features from <Picture 1> remain consistent throughout the entire segment.\n"
        f"<Subject 2> (appears in {seg['retention_shots']}): fully_preserved - the scene's architecture, teal palette, lighting, and dreamcore atmosphere from <Picture 2> remain consistent throughout the entire segment.\n"
        "<Audio 1>: fully_copy - <Audio 1> is reused 1:1 as the segment's complete final audio track.",
        "detailed_description:\n" + STYLE_EN + "\n" + seg["shots_en"],
        SOUNDSCAPE_EN,
        MUSIC_EN,
    ])

def build_prompt_zh(seg):
    return "\n\n".join([
        SUBJECTS_ZH_TMPL.format(scene_zh=SCENES_ZH[seg["scene"]]),
        seg["summary_zh"],
        "retention_analysis（保留分析）：\n"
        f"<Subject 1>（出现在 {seg['retention_shots']}）：fully_preserved - 角色身份及 <Picture 1> 中所有标志性视觉特征在整个片段中保持一致。\n"
        f"<Subject 2>（出现在 {seg['retention_shots']}）：fully_preserved - <Picture 2> 中场景的建筑、蓝绿色配色、光照与梦核氛围在整个片段中保持一致。\n"
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
    wf["12"]["inputs"]["filename_prefix"] = f"MiniMaxH3/menghe_miku_v2_S{n}"
    wf["9"]["inputs"]["noise_seed"] = SEEDS[n - 1]
    wf["60"] = {
        "inputs": {"image": ""},
        "class_type": "LoadImage",
        "_meta": {"title": "Load Image (background)"},
    }
    wf["6"]["inputs"]["ref_images.ref_image_1"] = ["60", 0]
    return wf

manifest = []
for i, seg in enumerate(SEGMENTS, start=1):
    (SHOTS / f"S{i}_prompt.txt").write_text(build_prompt_en(seg), encoding="utf-8")
    (SHOTS / f"S{i}_prompt_zh.txt").write_text(build_prompt_zh(seg), encoding="utf-8")
    wf = build_workflow(seg, i)
    (SHOTS / f"S{i}_workflow_api.json").write_text(json.dumps(wf, ensure_ascii=False, indent=1), encoding="utf-8")
    json.loads((SHOTS / f"S{i}_workflow_api.json").read_text(encoding="utf-8"))
    en = build_prompt_en(seg)
    assert len(en) <= 7000, f"S{i} prompt too long: {len(en)}"
    manifest.append({"segment": i, "scene": seg["scene"], "bg": SCENE_BG[seg["scene"]],
                     "duration": seg["duration"], "seed": SEEDS[i - 1]})
    print(f"S{i}: scene={seg['scene']}, prompt {len(en)} chars, duration {seg['duration']}, seed {SEEDS[i-1]}, JSON OK")

pathlib.Path("projects/初音未来_梦核_竖屏视频/shots/manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("MANIFEST:", json.dumps(manifest, ensure_ascii=False))
print("ALL OK")
