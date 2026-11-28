# 2. rioko 车内自拍短视频

## 参考视频

来源：X 帖子 [@rioko041120](https://x.com/rioko041120/status/2093277648638370005?s=20)

![](assets/rioko凉凉子♡C108-车内自拍.mp4)

- 视频规格：约 5 秒，竖屏，H.264 视频
- 用途：研究自拍视角、第一人称眼神互动、手持微晃真实感、浅景深背景虚化、私密空间氛围；不是直接复刻源视频画面、人物身份或服装。

## 视频内容与运镜分析

> 以下分析由 `opc video understand` 完成。时间段是内容观察区间，个别运动属于视觉判断，不能替代逐帧测量。

| 时间段 | 内容与景别 | 运镜重点 | 焦点与动作 |
| --- | --- | --- | --- |
| 00:00–00:02 | 行驶汽车后座内的女性角色；中近景（chest-up），主体居中正面 | 基本固定，平视略偏仰角，仅因车辆颠簸和手持产生轻微晃动 | 焦点由环境转向人物面部；微笑凝视镜头，右手抬起做手势 |
| 00:02–00:04 | 同一构图，手势成为新焦点 | 保持固定，手持微晃持续 | 焦点跟随手部；右手做出"比心/指向自己"手势，眼神更显灵动 |
| 00:04–00:05 | 同一构图，手部移至胸前 | 保持固定，手持微晃持续 | 焦点回到面部与手部交汇处；手轻抚胸口衣襟，目光稍移又回望镜头 |

### 可迁移的 H3 运镜语法

- 用"front-facing selfie angle at eye level with a slight low-angle"建立第一人称亲密感，观众即"对话对象"。
- 用"static shot with handheld slight shake"模拟手机自拍的真实感，避免完美稳定带来的"影视感"。
- 用"centered composition with subject filling frame"最大化视觉焦点集中，背景虚化（车窗动态模糊）增加层次感。
- 用"slow hand gestures guiding viewer attention"引导视线流动，从面部到手部再回到面部，形成情感表达闭环。
- 用"direct eye contact with lens"建立与观众的直接情感连接，眼神变化（微笑→灵动→挑逗）驱动情绪递进。
- 用"moving vehicle background with blurred parallax"增加环境流动感和私密空间氛围。

## MiniMax H3 Full-reference 提示词

### English Prompt

```text
subject_definitions:
<Picture 1> is the only supplied image reference and defines the target adult character's appearance. Preserve all clearly visible facial identity, facial proportions, eyes, eyebrows, nose, lips, skin tone, hairstyle, hair color, and identity-defining hair accessories from the image. Use the image for appearance only; do not inherit its background, clothing, body pose, camera angle, or lighting.

summary:
[reference generation] Create a new 10.000-second 9:16 intimate character portrait sequence using <Picture 1> only for the character's appearance. Use the following written motion analysis as prompt guidance: a front-facing selfie angle at eye level with a slight low-angle, a static shot with handheld slight shake, centered composition with the subject filling the frame, slow hand gestures guiding attention, direct eye contact with the lens, shallow-focus background, and blurred moving-vehicle parallax. Show the consistent character from <Picture 1> in the backseat of a moving taxi, wearing a newly designed deep V-neck dress. Create all imagery and audio anew.

retention_analysis:
<Picture 1> (character appearance throughout): fully_preserved - preserve the supplied image's facial identity, facial proportions, hairstyle, hair color, skin tone, and identity-defining accessories; do not import its background, pose, clothing, environment, lighting, text, watermark, or audio.

detailed_description:
The target video is a polished 9:16 live-action intimate character portrait based on a written selfie-style motion analysis, not a video input. Use warm interior taxi lighting, natural daylight from the windows, blurred passing city streets, beige leather seats, and a partition between the front and back. The character from <Picture 1> is the sole target character. Use one coherent performance with no abrupt teleportation, identity drift, face morphing, warped hands, duplicated limbs, unreadable extra text, logos, subtitles, or watermark. Keep the character's appearance and newly designed costume consistent from beginning to end.

[Shot 1] From 00:00.000 to 00:03.000, begin in a front-facing selfie close-up in the backseat of a moving taxi. The character from <Picture 1> looks directly into the lens with a confident, slightly playful expression. The hand rests near the chest. The camera is held in a smartphone selfie position at eye level with a slight low-angle, maintaining a centered composition with the subject filling the frame. The background shows blurred passing city streets and the beige leather taxi interior. The camera remains static with slight handheld shake caused by the moving vehicle and phone recording.

From 00:03.000 to 00:06.000, the character slowly raises the right hand and grips the bottom edge of the newly designed deep V-neck dress. The fingers pull the fabric downward, exposing the upper chest area without explicit nudity. Continue the static shot with slight handheld shake. Eye contact with the lens remains strong, and the expression shifts from playful to sensual. Passing-window parallax reinforces the moving-vehicle atmosphere.

From 00:06.000 to 00:10.000, while the left hand holds the dress fabric in place, the character slowly rotates the smartphone clockwise. The camera angle shifts from the selfie perspective to face forward through the taxi partition. As the phone rotates, the view transitions from the character to the front of the taxi interior: the driver's head and shoulders visible from behind, hands on the steering wheel, and the windshield showing the road ahead. The driver remains unaware of the backseat interaction. Slight handheld shake continues throughout the rotation. Keep the framing non-explicit and do not expose breasts or genitals.

overall_soundscape:
Use a continuous moving-taxi ambience: low steady engine rumble, tires on asphalt, rhythmic wind through the windows, occasional distant traffic, faint city noise, and subtle dress-fabric rustle. Keep the ambience realistic and synchronized with the visible actions. Generate all sound anew; no dialogue, narration, singing, or loud impact sounds.

non_diegetic_music:
N/A
```

### 中文翻译

```text
subject_definitions:
<Picture 1> 是唯一提供的图像参考，用于定义目标成年角色的外貌。保留参考图中清晰可见的面部身份、面部比例、眼睛、眉毛、鼻子、嘴唇、肤色、发型、发色和具有身份识别作用的发饰。参考图只用于外貌；不要继承其背景、服装、身体姿势、镜头角度或光线。

summary:
[reference generation] 仅使用 <Picture 1> 作为角色外貌参考，生成一段全新的 10.000 秒 9:16 竖屏亲密人物肖像视频。以下书面化的动作分析仅作为文字提示词依据：眼部高度带轻微仰角的正面自拍视角、带手持微晃的固定镜头、主体填满画面的居中构图、缓慢手势引导视线、直视镜头、浅景深背景和行驶车辆造成的模糊背景视差。展示 <Picture 1> 中保持一致的角色坐在行驶中的出租车后座，穿着全新设计的深 V 连衣裙。所有画面和音频均重新生成。

retention_analysis:
<Picture 1>（全程提供角色外貌）：fully_preserved - 保留参考图中的面部身份、面部比例、发型、发色、肤色和身份识别配饰；不要导入参考图的背景、姿势、服装、环境、光线、文字、水印或音频。

detailed_description:
成片是一段基于书面自拍式运动分析的精致 9:16 竖屏真人亲密人物肖像视频，不使用任何视频输入。使用温暖的出租车内部照明、车窗自然光、模糊流动的城市街景、米色皮质座椅和前后排隔断。<Picture 1> 中的角色是唯一目标角色。采用连贯表演，不要突然瞬移、身份漂移、脸部变形、手部扭曲、重复肢体、无意义文字、标志、字幕或水印。角色外貌和重新设计的服装从头到尾保持一致。

[Shot 1] 00:00.000 至 00:03.000，从行驶中的出租车后座正面自拍特写开始。<Picture 1> 中的角色直视镜头，表情自信而略带俏皮。手放在胸口附近。镜头以手机自拍姿势位于眼部高度，带轻微仰角，保持居中构图，主体填满画面。背景显示窗外模糊流动的城市街景和米色出租车内饰。镜头保持固定，因车辆行驶和手机录制产生轻微手持晃动。

00:03.000 至 00:06.000，角色缓慢抬起右手，抓住全新设计的深 V 连衣裙下摆。手指向下拉，露出上胸区域，但不要表现露骨裸体。镜头继续固定并保留轻微手持晃动。角色持续直视镜头，表情从俏皮转为性感。车窗外的视差强化行驶中的氛围。

00:06.000 至 00:10.000，角色用左手固定裙料，同时缓慢顺时针旋转手机。镜头从自拍视角转向透过隔断面向前方。随着手机旋转，画面从角色过渡到出租车前方：司机的头部和肩部从背后可见，双手握着方向盘，挡风玻璃外显示前方道路。司机没有察觉后座互动。手持微晃贯穿整个旋转过程。保持非露骨构图，不要露出乳房或生殖器。

overall_soundscape:
使用连续的移动出租车环境声：低沉引擎声、轮胎与沥青摩擦声、窗外有节奏的风声、偶尔的远处交通声、微弱城市噪音和细小衣料摩擦声。环境声保持真实，并与可见动作同步。所有声音重新生成；不要对白、旁白、歌唱或强烈撞击声。

non_diegetic_music:
N/A
```

### 效果

![](assets/file-20260829013201482.mp4)
