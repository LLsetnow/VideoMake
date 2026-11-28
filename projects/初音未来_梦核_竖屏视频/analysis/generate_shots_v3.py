# -*- coding: utf-8 -*-
"""v3：多场景漫游 + 每镜头约 3 秒（15s 段 = 5 镜头，7.38s 尾段 = 3 镜头）"""
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

STYLE_EN = "The target video is a 9:16 vertical dreamcore music-video segment in a cinematic mixed-media style: soft overexposure, hazy soft focus, pastel teal color grading, subtle film grain and a nostalgic 2000s digital texture, in a quietly melancholic liminal mood. The edit rhythm follows the existing pulse of <Audio 1>, with a new shot roughly every three seconds."
STYLE_ZH = "目标视频是一段 9:16 竖屏梦核音乐视频片段，采用电影感混合媒介风格：柔和过曝、朦胧柔焦、粉彩青绿色调、轻微胶片颗粒与怀旧的 2000 年代数字质感，整体是安静忧郁的阈限空间氛围。剪辑节奏跟随 <Audio 1> 的既有脉搏，大约每三秒切换一个新镜头。"

SOUNDSCAPE_EN = """overall_soundscape:
A quiet, reverberant dream-space ambience continues throughout the segment: faint distant water or air sounds, soft tonal hum, and a low room tone beneath the copied music."""
SOUNDSCAPE_ZH = """overall_soundscape（整体声景）：
整段持续着空旷、带混响的梦境空间环境声：微弱遥远的水声或风声、轻柔的嗡鸣，以及复制音乐下方的低柔空气感底噪。"""

MUSIC_EN = """non_diegetic_music:
<Audio 1> is directly reused 1:1 as the complete audience-only score. Preserve its exact timing, tempo, beat placement, dynamics, and stereo image from 00:00.000 to the end of the segment. Do not generate replacement music."""
MUSIC_ZH = """non_diegetic_music（非叙事音乐）：
<Audio 1> 被 1:1 直接复用为完整的观众专属配乐。从 00:00.000 到本段结束，保持其精确的时机、速度、节拍位置、动态与立体声像。不要生成替代音乐。"""

SEGMENTS = [
    dict(scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots open her dreamlike journey at the pool's edge. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头开启她在池边的梦境旅程。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The video opens on an empty wide shot of <Subject 2>, the teal mosaic pool hall: still cyan water, haze, and overexposed window light, with no one in frame. <Audio 1> begins immediately and remains unchanged.\n"
            "[Shot 2] At 00:03.000, <Subject 1>, Hatsune Miku in her default outfit, enters from the left edge of the frame and walks to the pool edge, full body visible, her turquoise twin-tails swaying; the camera pans right gently to follow her.\n"
            "[Shot 3] At 00:06.000, cut to a medium shot of <Subject 1> standing at the pool edge with her back to the camera; she slowly turns her head back toward the camera with a calm, slightly wistful expression, blue-green eyes catching the window light; slow push in.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot as she crouches at the pool edge, fingertips hovering just above the still cyan water; soft push in, water reflections shimmering below her hand.\n"
            "[Shot 5] At 00:12.000, cut to an intimate close-up of her fingertips touching the water: concentric ripples spread and shatter the reflected window light into shimmering fragments on the teal tiles; the camera tilts up slowly from the water toward her calm face."
        ),
        shots_zh=(
            "[Shot 1] 视频开场是 <Subject 2> 蓝绿色马赛克泳池大厅的空旷全景：静止的青色水面、雾气与过曝的窗光，画面中空无一人。<Audio 1> 立即开始并保持不变。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 初音未来身着默认服装从画面左缘入画，走到池边，全身入镜，青绿色双马尾轻轻摆动；镜头轻微右摇跟随她。\n"
            "[Shot 3] 00:06.000 处，切到中景：<Subject 1> 背对镜头站在池边，缓缓回头望向镜头，神情平静而略带惆怅，蓝绿色眼眸映着窗光；镜头慢推。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她蹲在池边，指尖悬在静止的青色水面上方；镜头轻推，手下的水面倒影 shimmering（粼粼闪动）。\n"
            "[Shot 5] 00:12.000 处，切到指尖触碰水面的大特写：同心涟漪扩散，把倒映的窗光打碎成闪烁的光斑洒在蓝绿色瓷砖上；镜头从水面缓缓上摇到她平静的面容。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="corridor", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots of her walking the endless corridor as the first lo-fi beat enters. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现她走过无尽走廊，第一声 lo-fi 节拍进入。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty one-point-perspective wide shot of <Subject 2>, the endless teal corridor: fluorescent lights, half-open doors, thin mist, and the glowing vanishing point; no one in frame; slow push in.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks into frame from the foreground and continues down the center of the corridor away from the camera, full body visible; the first soft lo-fi beat of <Audio 1> enters; smooth lateral tracking shot at slow speed.\n"
            "[Shot 3] At 00:06.000, cut to a medium shot from the side: she walks with a gentle rhythm matching the beat, twin-tails, jacket, and pleated skirt swaying with each step; a few fluorescent tubes flicker softly overhead.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot as she stops and trails one hand along the teal wall, fingers brushing the painted surface; she looks down briefly; slow push in.\n"
            "[Shot 5] At 00:12.000, cut to a medium close-up as she slowly turns back to look toward the camera; the corridor stretches into deep perspective behind her, the far end dissolving into overexposed white glow; her expression is calm and slightly curious."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 无尽蓝绿色走廊的单点透视空镜：荧光灯、半开的门、薄雾与发光的消失点；画面中空无一人；镜头慢推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 从前景走入画面，沿走廊中央向远处走去，全身入镜；<Audio 1> 的第一声轻柔 lo-fi 节拍进入；镜头以慢速平滑跟拍。\n"
            "[Shot 3] 00:06.000 处，切到侧面中景：她踩着与节拍相合的轻柔节奏行走，双马尾、外套与百褶裙随每一步摆动；头顶几根荧光灯管微微闪烁。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她停下脚步，一只手沿蓝绿色墙面划过，指尖拂过漆面；她短暂低头；镜头慢推。\n"
            "[Shot 5] 00:12.000 处，切到中近景：她缓缓转身回望镜头；身后走廊延伸出深邃的透视，尽头融化在过曝的白色光晕中；她神情平静而略带好奇。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="cloudroom", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots of her crossing the cloud-filled room and climbing the white staircase. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现她穿过云海房间、踏上白色楼梯。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty wide shot of <Subject 2>, the cloud-filled room: fluffy cloud sea on the floor, floating pastel clouds, volumetric light beams, and the white staircase rising into light; no one in frame; slow push in.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks out of the mist across the cloud sea toward the white staircase, full body visible, her boots sinking slightly into the soft cloud surface and stirring wisps of mist; tracking shot from behind at slow speed.\n"
            "[Shot 3] At 00:06.000, cut to a medium shot of her standing at the foot of the staircase, looking up along its ascent toward the glowing top; light dust drifts around her; slow tilt up.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her stepping onto the first stair, one hand on the railing; she looks back down at the cloud sea below; the camera follows her motion with a gentle push in.\n"
            "[Shot 5] At 00:12.000, cut to a medium shot of her climbing higher, glancing back over her shoulder toward the room below as light dust floats around her; the camera tilts up with small amplitude at slow speed, following her ascent."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 云海房间的空旷广角画面：地面蓬松的云海、漂浮的粉彩云朵、体积光束，以及没入光中的白色楼梯；画面中空无一人；镜头慢推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 从雾气中走出，穿过云海走向白色楼梯，全身入镜，靴子微微陷入柔软的云面、带起缕缕雾气；镜头在她身后慢速跟拍。\n"
            "[Shot 3] 00:06.000 处，切到中景：她站在楼梯脚下，抬头仰望通向发光顶端的阶梯；光尘在她周围飘浮；镜头缓摇上。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她踏上第一级台阶，一只手扶着栏杆；她回头望向下方云海；镜头随她的动作轻推。\n"
            "[Shot 5] 00:12.000 处，切到中景：她继续向上攀登，回头瞥向下方房间，光尘在周围漂浮；镜头以慢速、小幅度上摇，跟随她向上。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="sky", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots of her stepping off the staircase into the open sky and floating on the clouds. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现她走下楼梯步入开阔天空、在云上漂浮。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty wide shot of <Subject 2>, the open teal-tinted dusk sky: layered clouds, volumetric light beams, and the top of the white staircase emerging from the clouds at the left edge; no one in frame.\n"
            "[Shot 2] At 00:03.000, <Subject 1> steps off the final stair onto the cloud surface and walks a few steps into the open sky, full body visible, twin-tails and skirt drifting in the wind; slow arc shot around her.\n"
            "[Shot 3] At 00:06.000, cut to a medium shot of her standing on the clouds, tilting her head up toward the light; golden-teal light dust floats around her; slow tilt up.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her gently spreading her arms, eyes half-closed, hair and skirt flowing in the breeze; slow lateral drift of the camera.\n"
            "[Shot 5] At 00:12.000, cut to a full-body wide shot of her standing small on the cloud surface with layers of cloud stretching into the distance behind her; the camera performs a slow arc shot with small amplitude, keeping her centered."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 开阔青绿色黄昏天空的空镜：层叠云海、体积光束，画面左侧云中探出白色楼梯顶端；画面中空无一人。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 走下最后一级台阶踏上云面，在开阔天空中前行几步，全身入镜，双马尾与裙摆在风中飘动；镜头缓慢环绕她。\n"
            "[Shot 3] 00:06.000 处，切到中景：她站在云上，抬头仰望光线；青金色光尘环绕着她；镜头缓摇上。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她轻轻张开双臂，双眼半阖，发丝与裙摆随风飘动；镜头缓慢横移。\n"
            "[Shot 5] 00:12.000 处，切到全身广角：她小巧地站在云面上，身后层层云海延伸向远方；镜头以慢速、小幅度环绕她，让她保持在画面中央。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots as the dream folds back to the pool room and she touches the water. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现梦境折返回泳池大厅、她触碰水面。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty wide shot of <Subject 2>, the pool hall returned to, with drifting haze and mirror-like puddles of window light on the wet floor, as if the dream has folded back to its beginning; no one in frame.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks slowly to the center of the hall, full body visible, surrounded by haze; her reflection stretches faintly across the damp tiles; the musical texture of <Audio 1> grows brighter; slow push in.\n"
            "[Shot 3] At 00:06.000, cut to a medium shot of her standing still, small in the frame, looking up toward the overexposed windows; soft halation blooms around her silhouette; slow push in.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot as she moves to the pool edge and crouches, fingertips hovering above the still water; she looks down at her faint reflection; gentle push in.\n"
            "[Shot 5] At 00:12.000, cut to an intimate close-up of her fingertips touching the water: ripples spread slowly and shatter the reflected window light into shimmering fragments; the camera tilts up slowly from the water to her calm face as she gazes into the light."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 泳池大厅的空旷广角画面，仿佛梦境折返回起点：漂浮的雾气，湿地上浅浅的镜面状窗光水洼；画面中空无一人。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 缓缓走到大厅中央，全身入镜，雾气环绕，倒影淡淡地越过潮湿瓷砖延伸；<Audio 1> 的音乐织体变得明亮；镜头慢推。\n"
            "[Shot 3] 00:06.000 处，切到中景：她静静站立，在画面中显得小巧，抬眸望向过曝的高窗；她的轮廓泛起柔和光晕；镜头慢推。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她走到池边蹲下，指尖悬在静止的水面上方，低头看着自己淡淡的倒影；镜头轻推。\n"
            "[Shot 5] 00:12.000 处，切到指尖触水的大特写：涟漪缓缓扩散，把倒映的窗光打碎成闪烁的光斑；镜头从水面缓缓上摇到她凝视着光的平静面容。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots of her slow spinning turn at the pool edge settling into a peaceful close. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现她在池边缓慢旋转并归于平静。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on a full-body wide shot of <Subject 1> standing at the pool edge in <Subject 2>, teal mosaic hall and still water around her; she begins a slow, graceful full turn in place as the steady beat of <Audio 1> plays; slow arc shot around her.\n"
            "[Shot 2] At 00:03.000, cut to a medium shot of her mid-turn: twin-tails, jacket, and pleated skirt flow with the motion while her reflection turns beneath her on the water; the arc shot continues at slow speed.\n"
            "[Shot 3] At 00:06.000, cut to a closer shot as she completes the turn and faces the camera, her eyes gently closed, a faint peaceful smile forming; soft lens flare blooms behind her from the window light.\n"
            "[Shot 4] At 00:09.000, cut to an extreme close-up of her face: eyelashes, drifting hair strands, and the soft overexposed light washing over her features; near-static camera with very subtle handheld vibration.\n"
            "[Shot 5] At 00:12.000, cut back to a full-body wide shot of her standing still, facing the camera, eyes still closed, small against the vast hall; the camera holds nearly static as the beat of <Audio 1> continues."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 1> 站在 <Subject 2> 池边的全身广角镜头，蓝绿色马赛克大厅与静止的水面环绕着她；随着 <Audio 1> 稳定节拍，她开始缓慢而优雅地原地旋转；镜头缓慢环绕。\n"
            "[Shot 2] 00:03.000 处，切到中景：她旋转至半程，双马尾、外套与百褶裙随动作飘动，水面上的倒影也随之转动；环绕运镜以慢速继续。\n"
            "[Shot 3] 00:06.000 处，切到更近的镜头：她完成旋转面向镜头，双眼轻轻闭合，嘴角浮起一丝平静的微笑；窗光在她身后绽开柔和的镜头光晕。\n"
            "[Shot 4] 00:09.000 处，切到面部大特写：睫毛、飘动的发丝与过曝柔光拂过她的面容；镜头近乎静止，只带极轻微的手持晃动。\n"
            "[Shot 5] 00:12.000 处，切回全身广角：她静静站立面向镜头，双眼依然闭合，在空旷大厅中显得渺小；<Audio 1> 节拍继续，镜头近乎静止。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="sky", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five quick shots of her sitting on the clouds and gazing into the distance as the music softens. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个短镜头展现她坐在云上眺望远方，音乐逐渐轻柔。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty wide shot of <Subject 2>, the open sky: layered cloud sea stretching to the glowing horizon, volumetric light, and drifting light dust; no one in frame; very slow push in.\n"
            "[Shot 2] At 00:03.000, cut to a medium shot of <Subject 1> sitting on the soft cloud surface, legs folded beside her, looking out over the cloud sea; twin-tails and skirt edges drift in the breeze; gentle push in.\n"
            "[Shot 3] At 00:06.000, cut to a closer shot of her looking down through a gap in the clouds at the drifting light dust below; her expression calm and nostalgic; slow tilt down following her gaze.\n"
            "[Shot 4] At 00:09.000, cut to a medium close-up as she lifts her head and looks toward the distant horizon, eyes catching the soft light; slow lateral drift of the camera.\n"
            "[Shot 5] At 00:12.000, cut to a wide shot of her sitting small on the cloud at the edge of the frame against the immense teal sky; the camera pulls out slowly, revealing the vast sky and the distant staircase remnant as the music of <Audio 1> grows softer and more spacious."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 开阔天空的空镜：层叠云海铺向发光的地平线、体积光与飘浮的光尘；画面中空无一人；镜头极慢推近。\n"
            "[Shot 2] 00:03.000 处，切到中景：<Subject 1> 坐在柔软的云面上，双腿盘在身旁，眺望云海；双马尾与裙摆边缘随风轻飘；镜头轻推。\n"
            "[Shot 3] 00:06.000 处，切到更近的镜头：她低头透过云隙看着下方飘浮的光尘，神情平静而怀旧；镜头随她的目光缓摇下。\n"
            "[Shot 4] 00:09.000 处，切到中近景：她抬起头望向远处地平线，眼眸映着柔光；镜头缓慢横移。\n"
            "[Shot 5] 00:12.000 处，切到广角：她坐在画面边缘的云上，在无垠青绿色天空的衬托下显得渺小；镜头缓缓拉远，展现广阔天空与远处楼梯残影，<Audio 1> 的音乐变得更加轻柔开阔。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="pool", duration=7.3846,
        summary_en="[reference generation + audio reuse] Create a final 7.4-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: three shots of her closing her eyes at the pool edge as the light fades like a dream ending where it began. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段收尾的 7.4 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：三个镜头展现她在池边闭眼，光线渐暗，梦境在起点结束。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The final segment opens on a wide shot of <Subject 1> sitting at the pool edge of <Subject 2> where her dream began, legs above the water, gazing quietly at the still cyan surface; the light from the windows begins to soften; slow push in.\n"
            "[Shot 2] At 00:02.500, cut to a medium close-up of her, her eyes slowly closing and her breathing calm; a faint breeze lifts the edges of her twin-tails, hair, and pleated skirt, and the still water darkens gently; very slow push in.\n"
            "[Shot 3] At 00:05.000, cut to a close-up of her peaceful face as the window light dims further like a dream fading, while <Audio 1> fades out. The video ends on the soft, held final frame exactly when the audio ends."
        ),
        shots_zh=(
            "[Shot 1] 收尾段开场是广角镜头：<Subject 1> 坐在她梦境开始的地方——<Subject 2> 的池边，双腿悬在水面上方，安静地望着静止的青色水面；窗光开始变柔；镜头慢推。\n"
            "[Shot 2] 00:02.500 处，切到中近景：她双眼缓缓闭合，呼吸平静；微风轻轻掀起她的双马尾、发丝与百褶裙边，静止的水面也随之缓缓变暗；镜头极慢推近。\n"
            "[Shot 3] 00:05.000 处，切到她平静面容的特写，窗光进一步变暗，如同梦境消退，<Audio 1> 随之淡出。视频在音频结束的瞬间，定格于柔软而安宁的最后一帧。"
        ),
        shot_labels="[Shot 1] through [Shot 3]"),
]

SEEDS = [594001 + i for i in range(8)]
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
        f"<Subject 1> (appears in {seg['shot_labels']}): fully_preserved - the character's identity and all defining visual features from <Picture 1> remain consistent throughout the entire segment.\n"
        f"<Subject 2> (appears in {seg['shot_labels']}): fully_preserved - the scene's architecture, teal palette, lighting, and dreamcore atmosphere from <Picture 2> remain consistent throughout the entire segment.\n"
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
        f"<Subject 1>（出现在 {seg['shot_labels']}）：fully_preserved - 角色身份及 <Picture 1> 中所有标志性视觉特征在整个片段中保持一致。\n"
        f"<Subject 2>（出现在 {seg['shot_labels']}）：fully_preserved - <Picture 2> 中场景的建筑、蓝绿色配色、光照与梦核氛围在整个片段中保持一致。\n"
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
    wf["12"]["inputs"]["filename_prefix"] = f"MiniMaxH3/menghe_miku_v3_S{n}"
    wf["9"]["inputs"]["noise_seed"] = SEEDS[n - 1]
    wf["60"] = {"inputs": {"image": ""}, "class_type": "LoadImage", "_meta": {"title": "Load Image (background)"}}
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
    nshots = en.count("[Shot ")
    manifest.append({"segment": i, "scene": seg["scene"], "bg": SCENE_BG[seg["scene"]],
                     "duration": seg["duration"], "seed": SEEDS[i - 1], "shots": nshots})
    print(f"S{i}: scene={seg['scene']}, shots={nshots}, prompt {len(en)} chars, duration {seg['duration']}, seed {SEEDS[i-1]}, JSON OK")

pathlib.Path("projects/初音未来_梦核_竖屏视频/shots/manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("ALL OK")
