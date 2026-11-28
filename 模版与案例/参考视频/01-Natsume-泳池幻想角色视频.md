# 1.Natsume 泳池幻想角色视频

## 参考视频

来源：X 帖子 [@natsume0v0](https://x.com/natsume0v0/status/2093251239664558351?s=20)

![](assets/Natsume枣糕.mp4)

- 视频规格：2160×3840，50 fps，19.551 秒，H.264 视频 + AAC 双声道音频
- 用途：研究人物特写、柔和推近、横向平移、低角度上移、环绕、前推和微手持感；不是直接复刻源视频画面、人物身份或服装。

## 视频内容与运镜分析

> 以下分析由 `opc video understand` 完成。时间段是内容观察区间，个别运动属于视觉判断，不能替代逐帧测量。

| 时间段            | 内容与景别                          | 运镜重点                  | 焦点与动作                        |
| -------------- | ------------------------------ | --------------------- | ---------------------------- |
| 00:00–00:02    | 户外泳池与绿植前的女性角色；中近景逐渐进入面部特写，主体居中 | 小幅、慢速推近，带极轻微手持呼吸感     | 焦点由环境转向人物面部；微笑凝视镜头，右手轻抚胸口    |
| 00:03–00:05    | 泳池边斜侧构图；中景进入近景                 | 横向平移叠加轻微旋转，中等幅度、平稳速度  | 焦点跟随主体；转身回眸、轻撩头发             |
| 00:06–00:09    | 棕榈树旁；中近景进入特写，低角度仰拍             | 缓慢上移，随后带轻微俯冲，幅度小、速度渐慢 | 面部持续清晰；手指点脸颊、托腮躺卧；闪光/泡泡随运动出现 |
| 00:10–00:13    | 池边石阶；中景、对角线构图                  | 顺时针小弧度环绕，中等幅度、适中速度    | 主体焦点稳定；抬手接泡泡，再展开双臂微笑         |
| 00:14–00:17    | 池边正面中近景；粉色玩具枪成为前景道具            | 小幅前推，叠加轻微摇晃，速度略快      | 焦点在手部与面部之间切换；举枪瞄准、假装射击、收枪微笑  |
| 00:18–00:19.55 | 面部与肩部极近特写，背景完全虚化               | 基本静止，仅保留接近零幅度的微颤      | 眼神和星形装饰最清晰；低头浅笑并停留           |
|                |                                |                       |                              |

### 可迁移的 H3 运镜语法

- 用“small, slow push-in”建立亲密感，再以“smooth lateral tracking”承接人物转身。
- 用“low-angle tilt/pedestal upward”强化角色的纵向空间感，但保持小幅度，避免夸张升降。
- 用“small clockwise arc shot”制造沉浸感，主体面部保持稳定清晰。
- 用“small push-in with a slight handheld sway”配合道具动作，运动略快但不抖散主体。
- 全程通过 rack focus 在环境、手部和面部之间切换；背景保持柔焦，泡泡和高光只做前后景层次。
- 运镜由动作触发：回眸→横移，点脸→上移，接泡泡→环绕，举道具→前推，收束→静止特写。

## MiniMax H3 Full-reference 提示词

### English Prompt

```text
subject_definitions:
<Picture 1> is the only supplied image reference and defines the target adult character's appearance. Preserve all clearly visible identity traits from the image: face shape, eyes, eyebrows, nose, lips, skin tone, hairstyle, hair color, hair ornaments, and other identity-defining accessories. Use the image for character appearance only; do not inherit its background, clothing, body pose, camera angle, or lighting.

summary:
[reference generation] Create a new 15.000-second 9:16 fantasy character portrait sequence using <Picture 1> only for the character's appearance. Use the following written motion and visual analysis as prompt guidance: gentle push-ins, smooth lateral tracking, a restrained low-angle rise, a small clockwise arc, a short forward push with slight handheld sway, shallow focus, a tropical pool atmosphere, and a quiet extreme-close-up ending. Show the character from <Picture 1> beside a sunlit resort pool with palms, lush greenery, floating bubbles, and soft lens highlights. Keep the target character visually consistent throughout and create all imagery and audio anew.

retention_analysis:
<Picture 1> (character appearance throughout): fully_preserved - preserve the supplied image's identity and visible facial, hair, color, skin, and accessory traits; do not import its background, pose, clothing, camera angle, lighting, text, watermark, or audio.

detailed_description:
The target video is a polished 9:16 live-action fantasy character portrait. The character from <Picture 1> is the sole visible character. Use the written motion analysis as the camera and performance blueprint, not as a source-video input: warm daylight, a turquoise swimming pool, palm leaves, dense green plants, soft creamy bokeh, subtle floating bubbles, controlled highlights, and physically plausible shallow depth of field. Maintain one coherent performance with no abrupt teleportation, identity drift, face morphing, warped hands, duplicated limbs, unreadable extra text, logos, subtitles, or watermark.

[Shot 1] From 00:00.000 to 00:02.500, begin with the character from <Picture 1> in a centered medium close-up beside the pool. Preserve the character's face, hair, hair color, and identity-defining accessories from the image. The character looks directly into the lens with a soft smile and lightly touches the chest with the right hand. The camera makes a small push-in at slow speed with an almost imperceptible handheld breathing sway. Start with the pool and foliage readable, then let focus settle gently on the character's eyes and hair ornament.

From 00:02.500 to 00:05.000, the character turns three-quarters away and looks back over the shoulder. Use a smooth lateral tracking shot moving right with small-to-medium amplitude and a very slight clockwise roll, never losing the face. The hand brushes a loose strand of hair; pool highlights and palm leaves slide laterally behind the subject with natural parallax. Keep the clothing newly designed for this target scene and do not copy clothing from the image.

From 00:05.000 to 00:08.000, move to a restrained low-angle composition near a palm tree. The camera performs a slow upward tilt and small pedestal-up movement, then eases into a tiny downward dip as the character touches one cheek and reclines into a playful pose. Keep the face sharp and the background creamy and defocused. Bubbles and tiny sparkles drift through foreground and background without covering the eyes.

From 00:08.000 to 00:11.000, reveal the character seated on the pool steps in a diagonal composition. Perform a small clockwise arc shot at smooth moderate speed around the front quarter, maintaining consistent scale, anatomy, and facial identity. The character raises one hand to catch a bubble, then opens both arms with a bright smile. Keep the motion continuous and physically grounded, with foliage creating layered parallax.

From 00:11.000 to 00:13.500, introduce a new small pastel water pistol as an original target prop. Use a short push-in with small amplitude at slightly faster speed and a restrained handheld sway as the character raises it toward the lens, pretends to fire, then lowers it while smiling. Rack focus once from the prop to the face; keep both hands anatomically correct and the prop stable.

From 00:13.500 to 00:15.000, decelerate into a centered extreme close-up of the character's face and shoulders. The camera becomes almost static, retaining only a near-zero-amplitude natural micro-tremor. The character lowers the gaze and gives a small gentle smile while a highlight glints on the hair ornament. Hold the final frame calmly; do not add a sudden zoom, flash, cut, or new object.

overall_soundscape:
Generate a continuous quiet resort-pool ambience: soft water movement, distant warm air, faint palm-leaf rustle, delicate bubble pops, and subtle cloth movement. Keep the ambience understated and synchronized with the visible actions. Create this ambience anew; include no dialogue, narration, singing, or loud impact sounds.

non_diegetic_music:
Use a light, sparse fantasy-pop score with soft plucked tones, airy pads, tiny bell accents, and a gentle mid-tempo pulse. Keep the dynamics smooth, let the rhythm support the push-ins and arc movement, and reduce the score into a delicate sustained tone during the final extreme close-up. Create original music rather than reusing any source soundtrack.
```

### 中文翻译

```text
subject_definitions:
<Picture 1> 是唯一提供的图像参考，用于定义目标成年角色的外貌。保留参考图中清晰可见的全部身份特征：脸型、眼睛、眉毛、鼻子、嘴唇、肤色、发型、发色、发饰及其他具有身份识别作用的配饰。参考图只用于角色外貌；不要继承其背景、服装、身体姿势、镜头角度或光线。

summary:
[reference generation] 仅使用 <Picture 1> 作为角色外貌参考，生成一段全新的 15.000 秒 9:16 竖屏幻想人物肖像视频。以下书面化的动作与视觉分析仅作为文字提示词依据：柔和推近、平滑横向跟拍、克制低角度上移、小幅顺时针环绕、带轻微手持感的短促前推、浅景深、热带泳池氛围和安静的结尾极近特写。展示 <Picture 1> 中的角色站在阳光下的度假泳池旁，周围有棕榈树、茂盛绿植、漂浮泡泡和柔和镜头高光。目标角色全程保持视觉一致，所有画面和音频均重新生成。

retention_analysis:
<Picture 1>（全程提供角色外貌）：fully_preserved - 保留参考图中的身份，以及面部、头发、发色、肤色和配饰特征；不要导入参考图的背景、姿势、服装、镜头角度、光线、文字、水印或音频。

detailed_description:
成片是一段精致的 9:16 竖屏真人幻想人物肖像视频。<Picture 1> 中的角色是唯一可见角色。使用书面动作分析作为运镜和表演蓝图，而不是任何视频输入：温暖日光、青绿色泳池、棕榈叶、茂密绿植、柔和奶油色散景、细小漂浮泡泡、受控高光和符合物理规律的浅景深。保持连贯表演，不要突然瞬移、身份漂移、脸部变形、手部扭曲、重复肢体、无意义文字、标志、字幕或水印。

[Shot 1] 00:00.000 至 00:02.500，<Picture 1> 中的角色在泳池旁以居中的中近景开始。保留参考图中的角色面部、头发、发色和身份识别配饰。角色直视镜头并温柔微笑，右手轻触胸口。镜头以小幅度慢速推近，并带几乎不可察觉的手持呼吸感。开始时让泳池和绿植清晰可辨，然后让焦点温柔地落到角色的眼睛和发饰上。

00:02.500 至 00:05.000，角色转身至四分之三侧面，再回眸看向镜头。镜头以小到中等幅度向右平滑横向跟拍，并加入极轻微顺时针旋转，始终保持面部清晰。角色用手拨动一缕发丝；泳池高光和棕榈叶以自然视差在主体身后横向滑过。服装应为本目标场景重新设计，不要复制参考图中的服装。

00:05.000 至 00:08.000，移动到棕榈树附近的克制低角度构图。镜头缓慢向上俯仰并小幅升起，随后在角色用手指轻触脸颊并以俏皮姿态躺靠时，缓和地向下轻俯。保持面部锐利、背景奶油般虚化。泡泡和微小闪光在前后景漂浮，但不要遮住眼睛。

00:08.000 至 00:11.000，展示角色坐在泳池台阶上的画面，采用对角线构图。镜头以平滑中速围绕主体前侧进行小幅顺时针弧线环绕，保持比例、肢体结构和面部身份一致。角色抬手接住泡泡，再张开双臂微笑。运镜必须连续且符合物理规律，让绿植形成分层视差。

00:11.000 至 00:13.500，引入一把全新设计的粉彩色玩具水枪，作为目标视频原创道具。镜头以小幅度、略快速度短促前推，并加入克制的手持摇晃；角色将水枪举向镜头，假装射击，再微笑着放下。焦点从道具切换一次到面部；保持双手结构正确，道具位置稳定。

00:13.500 至 00:15.000，减速进入角色面部与肩部的居中极近特写。镜头几乎静止，只保留接近零幅度的自然微颤。角色低下视线并露出轻柔微笑，发饰上有一处高光闪过。平静保持最后一帧，不要突然变焦、闪光、切镜或增加新物体。

overall_soundscape:
生成连续安静的度假泳池环境声：轻微水流、温暖空气、远处棕榈叶沙沙声、细小泡泡破裂声和轻微衣料运动声。环境声保持克制，并与可见动作同步。所有环境声重新生成；不要对白、旁白、歌唱或强烈撞击声。

non_diegetic_music:
使用轻盈、稀疏的幻想流行配乐：柔和拨弦、空气感铺底、细小铃音和温和中速脉冲。动态保持平滑，让节奏支撑推近和环绕，在最后的极近特写中收束为细腻的延音。配乐重新生成，不复用任何源配乐。
```

### 效果

![](assets/file-20260829013148914.mp4)
