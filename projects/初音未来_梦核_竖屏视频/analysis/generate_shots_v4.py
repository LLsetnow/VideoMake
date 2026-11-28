# -*- coding: utf-8 -*-
"""v4：使用用户桌面参考图作为场景参考；无天堂意象；低清/噪点/手持相机质感。
场景：泳池乐园(332) → 水下光井(338L) → 地层小屋(338M) → 花野列车(338R)
     → 孤岛电话亭(335L) → 深夜环路(335M) → 色彩街区(335R) → 泳池乐园闭环(332)
分辨率：0.5MP（低清）；每镜头约 3 秒（15s 段 5 镜头，尾段 3 镜头）。
"""
import json, pathlib

ROOT = pathlib.Path("projects/初音未来_梦核_竖屏视频")
TEMPLATE = json.load(open("workflows/Minimax双时钟图生视频V1_qianxia_audio15s_api.json", encoding="utf-8"))

SCENES = {
    "pool": "the indoor public pool shown in <Picture 2>: mint-green chlorinated water, small square pale-green and white tiles, white fluorescent ceiling panels, a bright pink double water slide at the far end with a dark tunnel opening beneath it, and inflatable toys floating on the still water",
    "lightshaft": "the dark rectangular room shown in <Picture 2>: near-black matte walls, a single slanted skylight opening cutting through the ceiling, one diagonal shaft of cold white light falling onto a pale reflective floor, and dozens of small brightly colored tropical fish floating weightlessly inside the light beam",
    "stratahouse": "the artificial miniature landscape shown in <Picture 2>: perfectly smooth green domed hills, a straight concrete path leading to a small cartoon house with a purple roof and pink walls, and a red-brown geological strata cross-section cutting through the background",
    "train": "the vintage train carriage shown in <Picture 2>: cream-yellow interior walls, rows of cobalt-blue vinyl bench seats, overhead luggage racks, and a floor completely overgrown with knee-high wild grass and white daisies, with blurred countryside passing outside the windows",
    "booth": "the wild field shown in <Picture 2>: waist-high grass and wildflowers in purple, pink, and orange, a vintage translucent glass phone booth standing alone and glowing with pink-purple light, a deep blue twilight sky, and distant power lines",
    "suburb": "the empty suburban street at night shown in <Picture 2>: a curved asphalt road with white lane markings, sparse single-story ranch houses with dark windows, overly bright street lamps casting star-shaped lens flares, and a deep blue night sky",
    "street": "the pastel residential street shown in <Picture 2>: a straight cement road receding to a vanishing point, identical modular houses in saturated pink, mint green, lemon yellow, and cream on both sides, perfectly flat lawns, and a single distant street lamp",
}
SCENES_ZH = {
    "pool": "<Subject 2> 是 <Picture 2> 中展示的室内公共泳池乐园：薄荷绿色氯水、浅绿与白色小方格瓷砖、白色荧光吊顶灯板、远处一座亮粉色双道滑梯、滑梯下方有黑暗隧道口，静止水面上漂着充气玩具",
    "lightshaft": "<Subject 2> 是 <Picture 2> 中展示的黑暗矩形房间：近黑色哑光墙壁、天花板上一道斜切的天窗开口、一束冷白光柱斜落在地面浅色反光材质上，光柱中悬浮着几十条色彩鲜艳的热带小鱼",
    "stratahouse": "<Subject 2> 是 <Picture 2> 中展示的人造微缩景观：完美光滑的绿色半球山丘、一条笔直混凝土小径通向一座紫色屋顶粉色墙面的卡通小屋，背景露出红褐色地层剖面",
    "train": "<Subject 2> 是 <Picture 2> 中展示的复古火车车厢：奶油黄内壁、成排钴蓝色人造革座椅、车顶行李架，地板完全被及膝高的野草与白色雏菊覆盖，窗外是模糊的乡村风光",
    "booth": "<Subject 2> 是 <Picture 2> 中展示的荒野：齐腰高的紫色、粉色、橙色野花草甸，一座复古半透明玻璃电话亭独自矗立、内部散发粉紫色光芒，深蓝暮色天空，远处有电线杆",
    "suburb": "<Subject 2> 是 <Picture 2> 中展示的深夜空无一人的郊区街道：带白色标线的弯曲沥青路、零星单层 ranch 式住宅（窗户漆黑）、过亮的路灯投出星芒状镜头光晕、深蓝色夜空",
    "street": "<Subject 2> 是 <Picture 2> 中展示的粉彩住宅街区：笔直水泥路延伸向消失点，两侧是饱和粉、薄荷绿、柠檬黄、奶油色的相同模块化房屋，草坪平整，远处有一盏孤零零的街灯",
}
SCENE_IMG = {
    "pool": "ref/background/初音未来_梦核_参考_泳池乐园.png",
    "lightshaft": "ref/background/初音未来_梦核_参考_三联_光井地层列车.png",
    "stratahouse": "ref/background/初音未来_梦核_参考_三联_光井地层列车.png",
    "train": "ref/background/初音未来_梦核_参考_三联_光井地层列车.png",
    "booth": "ref/background/初音未来_梦核_参考_三联_电话亭郊外街区.png",
    "suburb": "ref/background/初音未来_梦核_参考_三联_电话亭郊外街区.png",
    "street": "ref/background/初音未来_梦核_参考_三联_电话亭郊外街区.png",
}

SUBJECTS_EN_TMPL = """subject_definitions:
<Subject 1> is Hatsune Miku, the anime girl shown in <Picture 1>, with signature turquoise twin-tails, blue-green eyes, and her default outfit: a black cropped jacket, white puffy sleeves with white arm warmers, a black necktie, a dark pleated skirt, and thigh-high black boots. Preserve her exact face, hairstyle, body proportions, costume details, and colors from the reference image in every shot.
<Subject 2> is {scene}. Preserve the scene's layout, colors, lighting, and uncanny dreamcore mood in every shot.
<Audio 1> is the complete audio track of this segment, directly reused 1:1 as the target video's complete final audio track, including all music, rhythm, ambience, dynamics, and stereo balance."""

SUBJECTS_ZH_TMPL = """subject_definitions（主体定义）：
<Subject 1> 是 <Picture 1> 中展示的动漫少女初音未来，拥有标志性的青绿色双马尾、蓝绿色眼眸，以及默认服装：黑色短款外套、带白色袖套的白色泡泡袖、黑色领带、深色百褶短裙和过膝黑色长靴。每个镜头都要保持参考图中她的精确面容、发型、身材比例、服装细节与配色。
{scene_zh}。每个镜头都要保持该场景的布局、配色、光照与怪核梦核氛围。
<Audio 1> 是本段的完整音轨，将 1:1 直接复用为目标视频的完整最终音轨，包括全部音乐、节奏、环境声、动态与立体声平衡。"""

STYLE_EN = ("The target video is a 9:16 vertical dreamcore music-video segment shot on a low-fidelity handheld camera: heavy film grain and digital noise, soft focus, slight motion blur, natural handheld shake with breathing movement, and a nostalgic early-2000s digital camcorder look. "
            "The atmosphere stays grounded, liminal, and slightly uncanny - do not make the scene heavenly, divine, or paradise-like, and no glowing clouds or sacred light. "
            "The edit rhythm follows the existing pulse of <Audio 1>, with a new shot roughly every three seconds.")
STYLE_ZH = ("目标视频是一段 9:16 竖屏梦核音乐视频片段，用低保真手持相机拍摄：厚重的胶片颗粒与数码噪点、柔焦、轻微动态模糊、自然的呼吸感手持晃动，以及怀旧的 2000 年代初期数码摄像机质感。"
            "氛围保持接地、阈限与轻微不安——不要把场景做成天堂、神圣或乐园式意象，不要发光的云朵或圣光。"
            "剪辑节奏跟随 <Audio 1> 的既有脉搏，大约每三秒切换一个新镜头。")

SOUNDSCAPE_EN = """overall_soundscape:
A quiet, roomy ambience continues throughout the segment: faint distant hum, soft water or air sounds, and a low analog hiss beneath the copied music."""
SOUNDSCAPE_ZH = """overall_soundscape（整体声景）：
整段持续着空旷的环境声：微弱遥远的声音、轻柔的水声或风声，以及复制音乐下方的低噪模拟底噪。"""

MUSIC_EN = """non_diegetic_music:
<Audio 1> is directly reused 1:1 as the complete audience-only score. Preserve its exact timing, tempo, beat placement, dynamics, and stereo image from 00:00.000 to the end of the segment. Do not generate replacement music."""
MUSIC_ZH = """non_diegetic_music（非叙事音乐）：
<Audio 1> 被 1:1 直接复用为完整的观众专属配乐。从 00:00.000 到本段结束，保持其精确的时机、速度、节拍位置、动态与立体声像。不要生成替代音乐。"""

SEGMENTS = [
    dict(scene="pool", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots open her dreamlike journey at the public pool. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头在公共泳池开启她的梦境旅程。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The video opens on an empty wide handheld shot of <Subject 2>, the indoor public pool: mint-green still water, inflatable toys floating near the frame edge, the bright pink slide and its dark tunnel opening in the distance, fluorescent light humming above. No one is in frame. <Audio 1> begins immediately and remains unchanged.\n"
            "[Shot 2] At 00:03.000, <Subject 1>, Hatsune Miku in her default outfit, walks into frame from the left and stops at the tiled pool edge, full body visible, her turquoise twin-tails swaying; the handheld camera pans right gently to follow her, with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of <Subject 1> standing at the pool edge, looking down at her faint reflection in the mint-green water; she slowly turns her head toward the camera with a calm, slightly wistful expression; soft push in with handheld wobble.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot as she crouches at the pool edge, fingertips hovering just above the water; the camera drifts down with her, grainy and slightly out of focus.\n"
            "[Shot 5] At 00:12.000, cut to an intimate close-up of her fingertips touching the water: concentric ripples spread across the surface and distort the reflected fluorescent lights; the handheld camera tilts up slowly toward her calm face."
        ),
        shots_zh=(
            "[Shot 1] 视频开场是 <Subject 2> 室内公共泳池的空旷手持全景：薄荷绿静止水面、画面边缘漂浮的充气玩具、远处亮粉色滑梯与其下的黑暗隧道口，头顶荧光灯嗡嗡作响。画面中空无一人。<Audio 1> 立即开始并保持不变。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 初音未来身着默认服装从画面左侧入画，在瓷砖池边停步，全身入镜，青绿色双马尾轻轻摆动；手持镜头带自然晃动轻微右摇跟随她。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：<Subject 1> 站在池边，低头看着薄荷绿水面中自己淡淡的倒影；她缓缓转头看向镜头，神情平静而略带惆怅；镜头带手持摆动轻推。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她蹲在池边，指尖悬在水面上方；镜头随她下移，画面颗粒感重、略微失焦。\n"
            "[Shot 5] 00:12.000 处，切到指尖触水的大特写：同心涟漪在水面扩散，扭曲了倒映的荧光灯管光；手持镜头缓缓上摇到她平静的面容。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="lightshaft", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her walking through the dark room as the first lo-fi beat enters and colorful fish drift around her. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她穿过黑暗房间，第一声 lo-fi 节拍进入，彩色游鱼绕她漂浮。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld shot of <Subject 2>, the dark room: near-black walls, the slanted skylight above, and one diagonal shaft of cold white light falling onto the pale floor, with dozens of small colorful fish floating weightlessly inside the beam; no one in frame; slow handheld push in.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks into the light beam from the dark side of the room, full body visible, her outfit suddenly lit by the cold white light; the first soft lo-fi beat of <Audio 1> enters; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her walking slowly through the beam; the small colorful fish drift around her body, some passing close to her face and twin-tails.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her reaching out one hand; a bright orange fish circles her fingers and slips past; light dust and particles float in the beam; grainy image.\n"
            "[Shot 5] At 00:12.000, cut to a medium close-up of her tilting her head up toward the light source, fish drifting past her face, the beam flaring in the handheld lens; her expression is calm and wondering."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 黑暗房间的空旷手持镜头：近黑色墙壁、头顶斜切的天窗，一束冷白光柱斜落在地面浅色反光材质上，光柱中悬浮着几十条色彩鲜艳的小鱼；画面中空无一人；镜头手持慢推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 从房间暗侧走进光柱，全身入镜，她的服装被冷白光突然照亮；<Audio 1> 的第一声轻柔 lo-fi 节拍进入；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她在光柱中缓步穿行，彩色小鱼绕着她身体漂游，有的贴近她的脸与双马尾。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她伸出一只手，一条亮橙色小鱼绕着她的手指盘旋后滑过；光柱中漂浮着光尘与微粒；画面颗粒感重。\n"
            "[Shot 5] 00:12.000 处，切到中近景：她仰头望向光源，小鱼从她脸旁漂过，光束在手持镜头中泛起光晕；她神情平静而好奇。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="stratahouse", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her walking the concrete path toward the small house and pausing at the junction. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她沿着混凝土小径走向小屋、在路口停步。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld wide shot of <Subject 2>, the miniature landscape: smooth green domed hills, the concrete path, the small purple-roofed pink house ahead, and the red-brown strata cross-section behind; no one in frame; soft handheld push in.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks along the concrete path from the foreground toward the house, full body visible, her twin-tails and pleated skirt swaying with each step; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her reaching the T-shaped junction in the path and stopping, looking at the house; she hesitates, glancing left and right.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her face, looking toward the small house, a faint puzzled expression; wind moves her hair; the image is grainy with soft focus.\n"
            "[Shot 5] At 00:12.000, cut to a full-body wide handheld shot as she turns and continues along the path away from the camera, growing small against the hills and the strata wall; the camera holds with handheld wobble."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 微缩景观的空旷手持广角：光滑的绿色半球山丘、混凝土小径、前方紫色屋顶粉色墙面小屋，背景是红褐色地层剖面；画面中空无一人；镜头手持轻推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 从前景沿混凝土小径向小屋走去，全身入镜，双马尾与百褶裙随步伐摆动；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她走到小径的 T 字路口停下，望着小屋，犹豫地左右张望。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她望着小屋，神情略带困惑；风吹动她的发丝；画面颗粒感重、柔焦。\n"
            "[Shot 5] 00:12.000 处，切到全身手持广角：她转身沿小径向远处走去，身影在山丘与地层墙前变小；镜头带着手持晃动保持。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="train", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her walking through the flower-covered carriage and sitting on a blue seat. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她穿过花草覆盖的车厢、坐到蓝色座椅上。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld one-point-perspective shot of <Subject 2>, the train carriage: cream-yellow walls, rows of cobalt-blue seats, and the floor overgrown with wild grass and white daisies; blurred countryside drifts past the windows; no one in frame.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks along the aisle, stepping carefully through the grass and flowers, full body visible; her boots part the daisies; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her stopping mid-aisle and looking down at the flowers around her ankles; she slowly bends and touches a white daisy.\n"
            "[Shot 4] At 00:09.000, cut to a close-up of her fingers gently touching the daisy petals while wildflowers frame the foreground; the camera is grainy and slightly out of focus, drifting slowly.\n"
            "[Shot 5] At 00:12.000, cut to a medium shot of her sitting on one of the cobalt-blue seats, legs together, looking out the window at the blurred landscape; the handheld camera settles with a soft wobble and slow push in."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 火车车厢的空旷手持一点透视镜头：奶油黄内壁、成排钴蓝色座椅、地板被野草与白色雏菊覆盖；窗外模糊的乡村风光缓缓掠过；画面中空无一人。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 沿过道走来，小心地踩过花草，全身入镜；她的靴子分开雏菊；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她在过道中央停下，低头看着脚踝周围的花；她缓缓弯腰，触碰一朵白色雏菊。\n"
            "[Shot 4] 00:09.000 处，切到特写：她的指尖轻轻触碰雏菊花瓣，前景野花环绕；画面颗粒感重、略微失焦，缓缓漂移。\n"
            "[Shot 5] 00:12.000 处，切到中景：她坐在一张钴蓝色座椅上，双腿并拢，望着窗外模糊的风景；手持镜头带着轻晃落定，随后缓慢推近。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="booth", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her crossing the wild field toward the glowing phone booth. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她穿过荒野走向发光的电话亭。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld shot of <Subject 2>, the wild field: tall grass and wildflowers in purple, pink, and orange, and the glowing translucent phone booth standing alone in the middle distance, its pink-purple light bleeding into the dusk; no one in frame.\n"
            "[Shot 2] At 00:03.000, <Subject 1> parts the tall grass and walks slowly toward the phone booth, full body visible, her twin-tails and skirt brushing the flowers; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her stopping in front of the booth, the pink-purple glow washing over her face and outfit; she stares at the glass.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her pressing one hand flat against the glass of the booth, peering inside; the glow flares in the grainy handheld lens.\n"
            "[Shot 5] At 00:12.000, cut to a medium close-up as she slowly turns back to look toward the camera, the glowing booth behind her, flowers moving in the wind; she holds still for a moment before the shot ends."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 荒野的空旷手持镜头：齐腰高的紫色、粉色、橙色野花草甸，中景处一座半透明玻璃电话亭独自矗立，粉紫色光芒渗入暮色；画面中空无一人。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 拨开高草缓缓走向电话亭，全身入镜，双马尾与裙摆拂过花朵；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她在电话亭前停步，粉紫色光晕洒在她脸上与衣服上；她凝视着玻璃。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她把手掌平贴在电话亭玻璃上，向内窥视；光芒在颗粒感的手持镜头中泛开。\n"
            "[Shot 5] 00:12.000 处，切到中近景：她缓缓转身回望镜头，身后是发光的电话亭，花朵在风中摇曳；她在镜头结束前静静伫立片刻。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="suburb", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her walking the empty night street under the street lamps. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她走在空无一人的深夜街道、经过路灯。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld shot of <Subject 2>, the night street: the curved asphalt road, ranch houses with dark windows, and bright street lamps casting star-shaped lens flares under the deep blue sky; no one in frame; slow handheld push in along the road.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks along the center of the road toward the camera, full body visible, her outfit lit by the cold streetlight; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her stopping under a street lamp, the star-shaped flare blooming behind her head; she looks down the empty road, then slowly looks up.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her face tilted up toward the lamp, the bright flare washing out the frame edges, heavy grain; she squints slightly.\n"
            "[Shot 5] At 00:12.000, cut to a full-body wide handheld shot of her standing at a road junction, glancing around at the empty houses, small in the frame; the camera holds with handheld wobble as the beat of <Audio 1> continues."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 深夜街道的空旷手持镜头：弯曲的沥青路、窗户漆黑的 ranch 式住宅、深蓝天空下过亮的路灯投出星芒状光晕；画面中空无一人；镜头沿道路手持慢推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 沿道路中央向镜头走来，全身入镜，冷色路灯照亮她的服装；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她在路灯下停步，星芒状光晕在她头后绽开；她望向空旷的道路，然后缓缓抬头。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她仰脸朝向路灯，明亮的眩光把画面边缘洗白，颗粒感很重；她微微眯眼。\n"
            "[Shot 5] 00:12.000 处，切到全身手持广角：她站在道路岔口，环顾四周空荡的房屋，在画面中显得渺小；<Audio 1> 节拍继续，镜头带着手持晃动保持。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="street", duration=15.0,
        summary_en="[reference generation + audio reuse] Create a new 15-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: five handheld shots of her walking the endless pastel street and pausing to look back. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段新的 15 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：五个手持镜头展现她走在无尽的粉彩街路上、停步回望。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The shot opens on an empty handheld one-point-perspective shot of <Subject 2>, the pastel street: the straight road receding to a vanishing point, identical saturated pink, mint, yellow, and cream houses on both sides, flat lawns, and the single distant street lamp; no one in frame; slow handheld push in.\n"
            "[Shot 2] At 00:03.000, <Subject 1> walks down the center of the road away from the camera, full body visible, her dark outfit standing out against the pastel houses; handheld tracking shot at slow speed with natural shake.\n"
            "[Shot 3] At 00:06.000, cut to a medium handheld shot of her stopping mid-road and slowly turning her head to look at the rows of identical houses on both sides.\n"
            "[Shot 4] At 00:09.000, cut to a closer shot of her face, a faint puzzled expression as she looks at the houses; the colors of the street are slightly overexposed and grainy.\n"
            "[Shot 5] At 00:12.000, cut to a full-body wide handheld shot of her continuing toward the vanishing point, growing small; the camera slowly pulls back, the identical houses stretching into the distance."
        ),
        shots_zh=(
            "[Shot 1] 开场是 <Subject 2> 粉彩街路的空旷手持一点透视镜头：笔直道路延伸向消失点，两侧是饱和粉、薄荷绿、柠檬黄、奶油色的相同模块化房屋，草坪平整，远处一盏孤零零的街灯；画面中空无一人；镜头手持慢推。\n"
            "[Shot 2] 00:03.000 处，<Subject 1> 沿道路中央向远处走去，全身入镜，深色服装在粉彩房屋衬托下格外显眼；手持跟拍，慢速、带自然晃动。\n"
            "[Shot 3] 00:06.000 处，切到中景手持镜头：她在路中央停步，缓缓转头看向两侧一排排相同的房屋。\n"
            "[Shot 4] 00:09.000 处，切到更近的镜头：她望着房屋，神情略带困惑；街路的色彩略微过曝、颗粒感重。\n"
            "[Shot 5] 00:12.000 处，切到全身手持广角：她继续走向消失点，身影变小；镜头缓缓拉远，相同的房屋向远处延伸。"
        ),
        shot_labels="[Shot 1] through [Shot 5]"),
    dict(scene="pool", duration=7.3846,
        summary_en="[reference generation + audio reuse] Create a final 7.4-second 9:16 vertical dreamcore music-video segment starring <Subject 1> inside <Subject 2>: three handheld shots of her closing her eyes at the pool edge as the light dims and the dream ends where it began. Reuse <Audio 1> exactly from beginning to end, without generating new dialogue, singing, music, or sound effects.",
        summary_zh="[reference generation + audio reuse] 生成一段收尾的 7.4 秒 9:16 竖屏梦核音乐视频片段，主角为 <Subject 1>，场景为 <Subject 2>：三个手持镜头展现她在池边闭眼，光线渐暗，梦境在起点结束。从头到尾原样复用 <Audio 1>，不生成新的对白、演唱、音乐或音效。",
        shots_en=(
            "[Shot 1] The final segment opens on a wide handheld shot of <Subject 1> sitting at the tiled pool edge of <Subject 2> where her dream began, legs above the water, gazing quietly at the mint-green surface; the fluorescent light above begins to soften; slow handheld push in.\n"
            "[Shot 2] At 00:02.500, cut to a medium close-up handheld shot of her, her eyes slowly closing and her breathing calm; a faint breeze moves the edges of her hair and skirt, and the water darkens gently; the grain thickens.\n"
            "[Shot 3] At 00:05.000, cut to a close-up of her peaceful face as the light dims further like a dream fading, the image growing darker and noisier, while <Audio 1> fades out. The video ends on the soft, held final frame exactly when the audio ends."
        ),
        shots_zh=(
            "[Shot 1] 收尾段开场是广角手持镜头：<Subject 1> 坐在她梦境开始的地方——<Subject 2> 的瓷砖池边，双腿悬在水面上方，安静地望着薄荷绿水面；头顶荧光灯开始变柔；镜头手持慢推。\n"
            "[Shot 2] 00:02.500 处，切到中近景手持镜头：她双眼缓缓闭合，呼吸平静；微风轻轻掀起她的发丝与裙摆，水面也随之缓缓变暗；颗粒感加重。\n"
            "[Shot 3] 00:05.000 处，切到她平静面容的特写，光线进一步变暗，如同梦境消退，画面变得更暗、噪点更重，<Audio 1> 随之淡出。视频在音频结束的瞬间，定格于柔软而安宁的最后一帧。"
        ),
        shot_labels="[Shot 1] through [Shot 3]"),
]

SEEDS = [604001 + i for i in range(8)]

def build_prompt_en(seg):
    return "\n\n".join([
        SUBJECTS_EN_TMPL.format(scene=SCENES[seg["scene"]]),
        seg["summary_en"],
        "retention_analysis:\n"
        f"<Subject 1> (appears in {seg['shot_labels']}): fully_preserved - the character's identity and all defining visual features from <Picture 1> remain consistent throughout the entire segment.\n"
        f"<Subject 2> (appears in {seg['shot_labels']}): fully_preserved - the scene's layout, colors, lighting, and uncanny dreamcore mood from <Picture 2> remain consistent throughout the entire segment.\n"
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
        f"<Subject 2>（出现在 {seg['shot_labels']}）：fully_preserved - <Picture 2> 中场景的布局、配色、光照与怪核梦核氛围在整个片段中保持一致。\n"
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
    wf["12"]["inputs"]["filename_prefix"] = f"MiniMaxH3/menghe_miku_v4_S{n}"
    wf["9"]["inputs"]["noise_seed"] = SEEDS[n - 1]
    wf["16"]["inputs"]["megapixels"] = 0.5  # 低清
    wf["60"] = {"inputs": {"image": ""}, "class_type": "LoadImage", "_meta": {"title": "Load Image (scene ref)"}}
    wf["6"]["inputs"]["ref_images.ref_image_1"] = ["60", 0]
    return wf

RANGES = {1: "1-15秒", 2: "16-30秒", 3: "31-45秒", 4: "46-60秒",
          5: "61-75秒", 6: "76-90秒", 7: "91-105秒", 8: "106-112秒"}
NAME = "初音未来_梦核_竖屏视频"

manifest = []
for i, seg in enumerate(SEGMENTS, start=1):
    rng = RANGES[i]
    sub = ROOT / rng
    (sub / f"{NAME}_{rng}_prompt.txt").write_text(build_prompt_en(seg), encoding="utf-8")
    (sub / f"{NAME}_{rng}_prompt_zh.txt").write_text(build_prompt_zh(seg), encoding="utf-8")
    wf = build_workflow(seg, i)
    (sub / f"{NAME}_{rng}_workflow_api.json").write_text(json.dumps(wf, ensure_ascii=False, indent=1), encoding="utf-8")
    json.loads((sub / f"{NAME}_{rng}_workflow_api.json").read_text(encoding="utf-8"))
    en = build_prompt_en(seg)
    assert len(en) <= 7000, f"{rng} prompt too long: {len(en)}"
    manifest.append({"segment": i, "range": rng, "scene": seg["scene"],
                     "bg": SCENE_IMG[seg["scene"]], "duration": seg["duration"],
                     "seed": SEEDS[i - 1], "megapixels": 0.5})
    print(f"{rng}: scene={seg['scene']}, prompt {len(en)} chars, JSON OK")

(ROOT / "analysis" / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("ALL OK")
