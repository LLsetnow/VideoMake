# Case2 — 30 秒横屏混合体位（3 × 10s 工作流）

> **原案例**：Case1（混合动作）扩展
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个 pose，每个 3-6 秒，加速构建节奏（6+4 / 5+5 / 4+6）
> **动作描述**：优先采用 `ref/Resources.json` 中每个 pose 的现成提示词描述
> **叙事线**：见面+脱衣+口交 → 传教士×2 → 女上位蛙式 → 后入式标准 → 坐姿面部射精（高潮收尾）

## 全局约束（三个工作流共同遵守）

- 提示词**不描述任何人物面部或发饰**：脸部与发型完全由 `<Picture 1>` 锁定，文字只写 "face and hair … exactly as shown in <Picture 1>"
- 男性**全程不露脸**（头部出画或出画外），**全片无男性声音**（只有身体物理声）
- 女孩 Shot 1 开场穿**情趣猫耳装**（black erotic cat-ear outfit），在该镜头内脱掉；其余全程裸体
- 同一间**昏暗暖光卧室**、同一张**白色床品**床贯穿全片
- 无对白、无音乐：`non_diegetic_music: N/A`，纯原生环境声（呼吸/呻吟/湿润声/床声）
- 她的声音强度曲线：轻 → 强 → 峰值 → 平复（跨工作流递进）

## 固定参考图（Picture 1-3，三个工作流完全相同）

- 面部参考（Picture 1）
![200](../../../../ref/character/幼女脸/幼女脸_正脸_无头饰.png)

- 身材参考（Picture 2）
![200](../../../../ref/character/其他/人体_室内_体型参考_竖版_v1.jpg)

- 外阴参考（Picture 3）
![200](../../../../ref/character/其他/人体_外阴特写.jpg)

## 分镜总表（6 poses）

| #   | 工作流 | 时间（全片） | 时长  | Pose（深度图）                                         | 内容                            |
| --- | --- | ------ | --- | ------------------------------------------------- | ----------------------------- |
| 1   | W1  | 0-6s   | 6s  | 跪姿口交-金发猫耳_正面（只借机位构图）                              | 见面 → 脱猫耳装 → 跪下稳定口交            |
| 2   | W1  | 6-10s  | 4s  | 传教士式性交-M字抬腿_第一人称俯视_横图                             | POV 插入 → 稳定 thrusting         |
| 3   | W2  | 0-5s   | 5s  | 传教士式性交-侧面_横图                                      | 抓手腕持续插入，身体轻颤、胸部起伏             |
| 4   | W2  | 5-10s  | 5s  | 女上位-坐姿蛙式_正面                                       | 蛙式开腿正对镜头，稳定骑乘                 |
| 5   | W3  | 0-4s   | 4s  | 后入式性交-标准（深度图=后入式性交-面部射精_正面_横图，按当前 `ref/pose/pose.json` 动作卡映射） | 俯卧后入，抓双腕后拉猛 thrust            |
| 6   | W3  | 4-10s  | 6s  | 坐姿面部射精-阴茎对准脸部_正面_横图                               | 最后深插 → 抽出 → 面部射精 → 呆滞平复（英雄镜头） |

---

## Workflow 1: 见面+脱衣+口交 → 传教士 M字POV（0-10s）

> **体位**：跪姿口交（开场连续镜头）→ 传教士式 M 字抬腿第一人称俯视
> **分镜**：2 个 — Shot 1（6s）见面/脱衣/口交 → Shot 2（4s）POV thrusting
> **pose 参考**：

- 跪姿口交（Picture 4，只借机位构图：低角度正面、她脸对镜头、男性站立且大部分身体出画；不继承其外观）
![200](../../../../ref/pose/color/跪姿口交-金发猫耳_正面_竖图.png)
![200](../../../../ref/pose/depth/跪姿口交-金发猫耳_正面_竖图_depth.png)

- 传教士 M 字抬腿 POV（Picture 5，magapixels = 1）
![200](../../../../ref/pose/color/传教士式性交-M字抬腿_第一人称俯视_横图.jpeg)
![200](../../../../ref/pose/depth/传教士式性交-M字抬腿_第一人称俯视_横图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as shown in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from <Picture 1>.
<Subject 2> is the body and figure of the female character, defined by <Picture 2>. Lock her extremely full hourglass figure, very full bust above D-cup, huge breast volume with natural droop, large breasts with prominent pink areola and obvious nipples, deep cleavage, smooth fine skin with light reflection highlights. Lock her body proportions, waist-to-hip ratio, limb length, and overall feminine curves. Preserve body consistency throughout the video; do not inherit facial features, clothing, or background from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction during intercourse; do not inherit background or pose from <Picture 3>.
<Subject 4> is the sex position and camera angle reference, defined by <Picture 4>. Use this depth map to lock the kneeling oral position body layout and the low frontal camera angle for the oral section of [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the missionary M-leg-raised body layout, the leg-raising posture, the penis insertion angle, and the first-person overhead POV camera perspective for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot bedroom scene featuring a naked young woman whose face and hair come from <Subject 1>, body from <Subject 2>, and vulva anatomy from <Subject 3>, having sex with a man whose face is never visible. [Shot 1] opens with the two meeting: the woman, wearing an erotic cat-ear outfit, undresses completely in front of the man, then kneels before him and begins steady oral sex from a low frontal angle. [Shot 2] cuts to a first-person overhead POV: the woman lies face-up on the white bed with her legs raised in an M-shape, and the man's penis enters her vagina from the bottom center of the frame and thrusts at a steady rhythm. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's hourglass figure and breast volume from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1], [Shot 2]): partially_preserved - the vulva anatomy from <Picture 3> is visible during the oral section and during penetration in [Shot 2].
<Subject 4> (appears in [Shot 1]): partially_preserved - the kneeling oral body layout and the low frontal camera angle are retained for the oral section of [Shot 1].
<Subject 5> (appears in [Shot 2]): partially_preserved - the missionary M-leg-raised layout and the first-person overhead POV angle are retained for [Shot 2].

detailed_description:
The target video is a realistic cinematic bedroom scene with warm dim indoor lighting, white bedding, soft shadows, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] A dimly lit bedroom with warm ambient lighting; a bed with white bedding occupies the center of the frame. The woman, combining <Subject 1> and <Subject 2>, stands at the foot of the bed wearing a black erotic cat-ear outfit. The man stands facing her, only his torso, arms, and legs visible, his head out of frame. The two meet, step closer, and hold a brief closeness. She then slowly undresses, pulling the cat-ear outfit off her body and letting it drop onto the white bedding, leaving her completely naked. She drops to her knees before the man. Following the posture of <Subject 4>, she is completely naked and kneeling in the center of the frame, leaning forward, her head and upper body close to the lower part of the frame, her face facing the camera. The man is standing in front of the woman, his legs at the bottom of the frame, most of his body outside the frame. Her hands are placed on the flat surface in front of her. The woman is touching the side of the man's penis with her lips from the side, beginning a steady oral stroke: her head moves back and forth in a smooth rhythm, her lips and mouth working around the side of the penis. The camera is at a low position near the bed surface, slightly in front of the woman's head, shooting her from a close frontal angle with a slight downward tilt, and stays static throughout [Shot 1].

[Shot 2] At 00:06.000, the camera cuts to a first-person overhead view. Following the posture of <Subject 5>, the woman is lying on the bed face-up, her legs raised in an M shape, her knees bent towards the ceiling, and her feet sole facing the camera. Her chest is exposed, her extremely full breasts visible against the white bedding. Her vulva between her spread legs matches <Subject 3>. The male is in the first-person perspective (POV): his hands are holding the woman's thighs on both sides, and his penis is extending from the center of the bottom of the frame to enter between her legs into her vagina. The penis slowly penetrates her vagina, the labia compressing around the entering shaft, then it begins to thrust in and out at a steady rhythm. Her eyes are half closed and her lips part, and a soft moan escapes with each thrust; her breasts shift with the movement and her body trembles slightly from the impact. The camera maintains the static first-person overhead POV throughout [Shot 2].

overall_soundscape:
A quiet bedroom room tone continues throughout the video. In [Shot 1], the rustling of fabric is audible as the cat-ear outfit is pulled off and drops onto the bedding, followed by the wet friction and soft slurping sounds of her mouth moving over the penis, her soft gasps, and her breathing deepening. In [Shot 2], wet rhythmic thrusting sounds as the penis slides in and out of her vagina dominate, synchronized with the thrusts, layered with her soft moans, light gasps, continuous heavy breathing, and the soft rustling of the bedding beneath their bodies. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 传教士侧面俯视 → 女上位蛙式（10-20s）

> **体位**：传教士式侧面俯视 → 女上位坐姿蛙式正面
> **分镜**：2 个 — Shot 1（5s）全身 thrusting → Shot 2（5s）蛙式骑乘
> **pose 参考**：

- 传教士侧面俯视（Picture 4，magapixels = 0.4 时才正确实现）
> ⚠️ 历史动作卡「传教士式性交-侧面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
- 女上位坐姿蛙式（Picture 5，magapixels = 0.4）
![200](../../../../ref/pose/color/女上位-坐姿蛙式_正面_竖图.png)
![200](../../../../ref/pose/depth/女上位-坐姿蛙式_正面_竖图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as shown in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from <Picture 1>.
<Subject 2> is the body and figure of the female character, defined by <Picture 2>. Lock her extremely full hourglass figure, very full bust above D-cup, huge breast volume with natural droop, large breasts with prominent pink areola and obvious nipples, deep cleavage, smooth fine skin with light reflection highlights. Lock her body proportions, waist-to-hip ratio, limb length, and overall feminine curves. Preserve body consistency throughout the video; do not inherit facial features, clothing, or background from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction during intercourse; do not inherit background or pose from <Picture 3>.
<Subject 4> is the sex position and camera angle reference, defined by <Picture 4>. Use this depth map to lock the missionary side body layout and the fixed overhead side camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the cowgirl seated frog position body layout, the vulva-facing-the-camera composition, and the frontal camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot bedroom scene featuring a naked young woman whose face and hair come from <Subject 1>, body from <Subject 2>, and vulva anatomy from <Subject 3>, having sex with a man whose face is never visible. [Shot 1] is a fixed overhead side view of missionary intercourse: the woman's entire body is visible, the man shows only his lower body and part of his arms, his hand grasps her wrist while his penis continuously inserts into her vagina, her body trembles, her chest rises and falls violently, and she gasps. [Shot 2] cuts to a frontal view: the woman is in a seated frog position with her knees apart and bent downward, her vulva facing the camera, her upper body reclined with her arms forming a symmetrical W shape, the man's hands holding her waist, and she rides steadily over his inserted penis. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's hourglass figure and breast volume from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1], [Shot 2]): partially_preserved - the vulva anatomy from <Picture 3> is visible as the penis slides in and out in [Shot 1] and is facing the camera in [Shot 2].
<Subject 4> (appears in [Shot 1]): partially_preserved - the missionary side body layout and the fixed overhead side camera angle are retained for [Shot 1].
<Subject 5> (appears in [Shot 2]): partially_preserved - the cowgirl seated frog body layout, the vulva-facing-the-camera composition, and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is a realistic cinematic bedroom scene with warm dim indoor lighting, white bedding, soft shadows, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] Following the posture of <Subject 4>, the woman is lying on the bed in a missionary position, completely naked, and her entire body can be seen in the picture. The man is positioned above her, only his lower body and part of his arms visible, his head out of frame. The man's hand is grasping the woman's wrist, and his penis is continuously inserting into her vagina. His lower body is constantly slapping the woman's buttocks. Due to the intense impact, the woman's body trembles slightly, her chest rises and falls violently, and from time to time she slightly opens her mouth and lets out a gasping sound. Her vulva matches <Subject 3> as the penis slides in and out. The picture is shot from a fixed overhead perspective to fully present the scene. The camera stays static throughout [Shot 1].

[Shot 2] At 00:05.000, the camera cuts to a frontal view. Following the posture of <Subject 5>, the woman is lying on the bed in a seated frog position, completely naked. Her legs are spread out in a frog-like position, her knees are apart and bent downward, and her vulva is facing the camera, matching <Subject 3>. Her upper body is reclined backward, her arms are bent and placed on both sides of her body, her left and right elbows are pressing against her waist, her forearms are raised and slightly extended outward, and the lines connecting her shoulders, elbows and wrists form a symmetrical W shape as a whole. The man's penis is thrusting into the vagina, and the man's hands are holding the woman's waist. She rides steadily, her hips moving up and down over the inserted penis in a smooth vertical rhythm, her eyes half closed, soft moans escaping with each movement. The camera maintains a static frontal position throughout [Shot 2].

overall_soundscape:
A quiet bedroom room tone continues throughout the video. The creaking of the bed frame and springs under their bodies, wet rhythmic thrusting sounds, and the slapping of skin—his lower body against her buttocks in [Shot 1] and skin-on-skin movement in [Shot 2]—layer with the woman's moans growing louder and her heavy continuous breathing, plus the soft rustling of the white bedding. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 后入式标准 → 坐姿面部射精（20-30s）

> **体位**：后入式标准（低侧机位）→ 坐姿面部射精（高潮收尾）
> **分镜**：2 个 — Shot 1（4s）猛 thrust 后入 → Shot 2（6s）面部射精 + 平复
> **pose 参考**：

- 后入式标准（Picture 4；按当前 `ref/pose/pose.json` 动作卡映射，该 pose 深度图为「后入式性交-面部射精_正面_横图」）
![200](../../../../ref/pose/color/后入式性交-面部射精_正面_横图.png)
![200](../../../../ref/pose/depth/后入式性交-面部射精_正面_横图_depth.png)

- 坐姿面部射精（Picture 5）
![200](../../../../ref/pose/color/坐姿面部射精-阴茎对准脸部_正面_横图.png)
![200](../../../../ref/pose/depth/坐姿面部射精-阴茎对准脸部_正面_横图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as shown in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from <Picture 1>.
<Subject 2> is the body and figure of the female character, defined by <Picture 2>. Lock her extremely full hourglass figure, very full bust above D-cup, huge breast volume with natural droop, large breasts with prominent pink areola and obvious nipples, deep cleavage, smooth fine skin with light reflection highlights. Lock her body proportions, waist-to-hip ratio, limb length, and overall feminine curves. Preserve body consistency throughout the video; do not inherit facial features, clothing, or background from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction during intercourse; do not inherit background or pose from <Picture 3>.
<Subject 4> is the sex position and camera angle reference, defined by <Picture 4>. Use this depth map to lock the doggy-style rear entry body layout and the low side-front camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the lying face-up body layout with the head at the bottom of the frame and the frontal camera angle for the facial ejaculation of [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot bedroom scene featuring a naked young woman whose face and hair come from <Subject 1>, body from <Subject 2>, and vulva anatomy from <Subject 3>, having sex with a man whose face is never visible. [Shot 1] is a doggy-style rear entry from a low side-front angle: the woman lies in a lateral prone position on the bed, the man kneels behind her, holding her wrists and repeatedly pulling them backward while thrusting into her. [Shot 2] cuts to a frontal low view: the woman lies on her back with her head at the bottom of the frame, takes a few final deep thrusts, and the man's penis then aims at her face and ejaculates onto it, ending the video on her dazed, settling final state. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's hourglass figure and breast volume from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1]): partially_preserved - the vulva anatomy from <Picture 3> is visible during penetration in [Shot 1].
<Subject 4> (appears in [Shot 1]): partially_preserved - the doggy-style rear entry body layout and the low side-front camera angle are retained for [Shot 1].
<Subject 5> (appears in [Shot 2]): partially_preserved - the lying face-up layout with the head at the bottom of the frame and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is a realistic cinematic bedroom scene with warm dim indoor lighting, white bedding, soft shadows, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] Following the posture of <Subject 4>, the woman is lying on the bed in a lateral prone position, completely naked, with her head in the lower left corner and her side face floating above the bed. Her torso extends to the right in the lower half of the picture, and her legs and buttocks are near the center on the right side. The man is on the right side of the picture, kneeling on the bed and bending over the woman, holding her wrists with both hands and repeatedly pulling them backward, his head and face staying above the frame, never visible. The man's penis is thrusting into the woman's pussy, and they are having sex in the doggy style; his hips drive hard so that his lower body slaps her buttocks with each thrust. Her body arches and trembles from the impact, and her moans grow louder and more urgent. The camera is at a low position near the bed surface, shooting from the side front of the characters at a close range horizontally. The overall shot is close to a level view but slightly with an upward angle. The woman is in the left foreground, and the man's body occupies the right and upper background. The camera stays static throughout [Shot 1].

[Shot 2] At 00:04.000, the camera cuts to a frontal low view. Following the posture of <Subject 5>, the woman is in a lying position on the bed, completely naked, with her head at the bottom of the frame and her body at the top. She takes a few final deep thrusts, her body trembling and her mouth opening in sharp gasps. The man's penis then withdraws from her vagina and extends from the upper right corner of the frame, directly aimed at the area of the woman's face, with the front end of the penis facing the woman's face, and ejaculates: a stream of semen shoots out and splashes onto her face, covering her cheeks and forehead. She lies back dazed, her chest heaving, a final shudder running through her body, her breathing gradually settling into slow, heavy breaths. The camera maintains a static low frontal position throughout [Shot 2].

overall_soundscape:
A quiet bedroom room tone continues throughout the video. In [Shot 1], strong slapping sounds of his lower body against her buttocks and wet thrusting sounds dominate, with the creaking of the bed frame, her loud moans rising in volume, and her heavy breathing. In [Shot 2], the final thrusts give way to the wet spraying sound of ejaculation, her peak moan and gasp, then quiet settling: slow, heavy breathing and the soft rustling of the bedding. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）或按 Duration Planner 配置
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  1. `ref/character/幼女脸/幼女脸_正脸_无头饰.png` → `<Picture 1>`（脸）
  2. `ref/character/其他/人体_室内_体型参考_竖版_v1.jpg` → `<Picture 2>`（身材）
  3. `ref/character/其他/人体_外阴特写.jpg` → `<Picture 3>`（外阴）
  4. 本工作流 pose 1 深度图 → `<Picture 4>`
  5. 本工作流 pose 2 深度图 → `<Picture 5>`
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W1 Shot 2 M字抬腿 = 1；W2 传教士侧面 = 0.4、W2 蛙式 = 0.4；其余 pose 未标注，用默认值
- **跨工作流一致性**：`<Subject 1/2/3>` 的锁定文字与 "the man's face is never visible" 约束在三个提示词中保持完全一致；卧室/床品/灯光描述保持一致
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）落在动作进行中，拼成 30 秒连续做爱流程
- **后入式标准的深度图映射**：当前 `ref/pose/pose.json` 使用「后入式性交-面部射精_正面_横图」动作卡（该图内容为标准后入式构图），提交时按此引用

## 成片

![](assets/Case2/file-20260831043142542.mp4)

## 素材

![](assets/Case2/file-20260831043146840.mp4)

![](assets/Case2/file-20260831043146861.mp4)

![](assets/Case2/file-20260831043146951.mp4)
