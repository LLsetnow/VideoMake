# Case3 — 蕾米埃尔（绝区零）30 秒横屏户外野战（3 × 10s 工作流）

> **角色**：蕾米埃尔 Remiel（绝区零 ZZZ）—— 粉色短发、白羽天使翅膀
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个 pose，每个 3-6 秒，加速构建节奏（6+4 / 5+5 / 4+6）
> **场景线**：Day → Dusk → Night（厄匹斯港白天码头 → Random Play 门口黄昏 → 404 门口雨夜），场景切换硬切（时间跳变显性化）
> **动作描述**：优先采用 `ref/Resources.json` 中每个 pose 的现成提示词描述

## 全局约束（三个工作流共同遵守）

- 提示词**不描述任何人物面部或发饰**：脸部与发型完全由 `<Picture 1>` 锁定
- 蕾米埃尔全片：**裸体 + 白色过膝袜 + 银色高跟鞋 + 白羽天使翅膀**（按裸体三视图参考）
- 男性**全程不露脸**（头部出画或出画外）、**全片无男性声音**（只有身体物理声）
- 无对白、无音乐：`non_diegetic_music: N/A`，纯原生环境声（海浪/城市底噪/雨声 + 呼吸/呻吟/湿润声）
- 她的声音强度曲线：轻 → 强 → 峰值 → 平复（跨工作流递进）
- **画风锁定**：Zenless Zone Zero 卡通渲染（cel-shaded，非写实）——每条提示词 detailed_description 开头声明
- 每个工作流参考图 6 张：Picture 1 脸 / 2 身体+翅膀 / 3 外阴 / 4 场景 / 5-6 两个 pose 深度图

## 固定参考图（Picture 1-3，三个工作流完全相同）

- 面部参考（Picture 1）
![200](../../../../ref/character/蕾米埃尔/exec-e724fa5d-a2fb-4858-b259-213277a73a94.png)

- 身体+翅膀+过膝袜参考（Picture 2，裸体三视图）
![200](../../../../ref/character/蕾米埃尔/蕾米埃尔.png)

- 外阴参考（Picture 3）
![200](../../../../ref/character/其他/人体_外阴特写.jpg)

## 分镜总表（6 poses）

| # | 工作流·场景 | 时间（全片） | 时长 | Pose（深度图） | 内容 |
|---|-------------|--------------|------|----------------|------|
| 1 | W1 白天·厄匹斯港 | 0-6s | 6s | 跪姿口交-站立男性_侧面 | 靠近→跪下→稳定口交（他站立不露脸） |
| 2 | W1 白天·厄匹斯港 | 6-10s | 4s | 女上位-坐姿蛙式_正面 | 码头木板蛙式骑乘，他手扶她腰 |
| 3 | W2 黄昏·Random Play 门口 | 0-5s | 5s | 女上位-坐姿前倾_正面_横图 | 砖路跪姿前倾、手撑地、髋部泵动 |
| 4 | W2 黄昏·Random Play 门口 | 5-10s | 5s | 传教士式性交-侧面_横图（magapixels=0.4） | 砖路平躺，抓手腕持续插入，全身轻颤 |
| 5 | W3 雨夜·404 门口 | 0-4s | 4s | 后入式性交-标准（深度图=后入式性交-面部射精_正面_横图） | 湿沥青俯卧后入，抓双腕后拉猛 thrust |
| 6 | W3 雨夜·404 门口 | 4-10s | 6s | 坐姿面部射精-阴茎对准脸部_正面_横图 | 最后深插→抽出→面部射精→呆滞平复（英雄镜头） |

---

## Workflow 1: 白天 · 厄匹斯港码头（0-10s）

> **场景**：厄匹斯港 —— 晴天海港，开阔海面、帆船、码头护栏、浅色滨海步道、远处城市天际线
> **体位**：跪姿口交（站立男性）→ 女上位坐姿蛙式
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s）

- 场景参考（Picture 4）
![200](../../../../ref/background/绝区零/厄匹斯港.png)

- 跪姿口交（Picture 5）
![200](../../../../ref/pose/color/跪姿口交-站立男性_侧面_竖图.png)
![200](../../../../ref/pose/depth/跪姿口交-站立男性_侧面_竖图_depth.png)

- 女上位坐姿蛙式（Picture 6，magapixels = 0.4）
![200](../../../../ref/pose/color/女上位-坐姿蛙式_正面_竖图.png)
![200](../../../../ref/pose/depth/女上位-坐姿蛙式_正面_竖图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the body, wings, and stockings of the female character, defined by <Picture 2>. Lock her slender feminine figure, her large white feathered angel wings with long trailing feathers, her white thigh-high stockings with garter straps, and her silver high heels, exactly as in <Picture 2>. Preserve body, wing, and stocking consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the sunny daytime seaside harbor location: open sea, sailboats, pier railings, bright seaside boardwalk, and the distant city skyline. Do not inherit any characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the kneeling oral body layout and the side camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the cowgirl seated frog position body layout, the vulva-facing-the-camera composition, and the frontal camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot outdoor scene on a sunny seaside pier, featuring a naked anime angel girl (face from <Subject 1>, body and wings from <Subject 2>, vulva from <Subject 3>), having sex with a man whose face is never visible. [Shot 1] opens with the two approaching, then she kneels on the pier planks and performs steady oral sex on his standing body from a side angle. [Shot 2] cuts to a frontal view: she sits on the deck in a frog position with her knees apart and bent downward, her vulva facing the camera, and rides steadily over his inserted penis while his hands hold her waist. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body, white feathered angel wings, white thigh-high stockings, and silver high heels from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1], [Shot 2]): partially_preserved - the vulva anatomy from <Picture 3> is visible during the oral section and faces the camera in [Shot 2].
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the sunny daytime seaside harbor location is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the kneeling oral body layout and the side camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the cowgirl seated frog layout, the vulva-facing-the-camera composition, and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an outdoor scene on a sunny seaside pier with bright daylight, hard shadows, an open blue sea, white clouds, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] A sunny seaside pier with wooden planks and white railings, the open sea and sailboats behind, and the distant city skyline, matching the scene of <Subject 4>. The woman, combining <Subject 1>, <Subject 2>, and <Subject 3>, stands at the edge of the pier wearing only her white thigh-high stockings and silver high heels, her large white feathered angel wings spread behind her, her body otherwise completely naked. The man stands facing her, only his torso, arms, and legs visible, his head out of frame. The two step closer, and she drops to her knees on the pier planks. Following the posture of <Subject 5>, the woman is in a kneeling position and the man is standing, his legs on the left side of the frame. Her mouth is open, slightly holding the head of the man's penis, and her hand is gripping the man's thigh, stroking around the base. She performs a steady oral stroke, her head moving back and forth in a smooth rhythm, her lips and mouth working around the side of the penis. Her white wings tremble slightly with her movements. The camera stays static throughout [Shot 1], shooting from a side angle at a close range.

[Shot 2] At 00:06.000, the camera cuts to a frontal view. Following the posture of <Subject 6>, the woman is sitting on the pier deck in a frog position, completely naked but for her white thigh-high stockings. Her legs are spread out in a frog-like position, her knees are apart and bent downward, and her vulva is facing the camera, matching <Subject 3>. Her upper body is reclined backward, her arms are bent and placed on both sides of her body, her left and right elbows are pressing against her waist, her forearms are raised and slightly extended outward, and the lines connecting her shoulders, elbows and wrists form a symmetrical W shape as a whole. The man's penis is thrusting into the vagina, and the man's hands are holding the woman's waist. She rides steadily, her hips moving up and down over the inserted penis in a smooth vertical rhythm, her eyes half closed, soft moans escaping with each movement, her white wings swaying gently behind her. The bright daylight catches the sheen on her skin and the white feathers of her wings. The camera maintains a static frontal position throughout [Shot 2].

overall_soundscape:
A bright daytime seaside ambience continues throughout the video: distant gulls, waves lapping against the pier, and a light sea breeze. In [Shot 1], the creak of the wooden planks under her knees, the wet friction and soft slurping sounds of her mouth over the penis, her soft gasps, and her deepening breathing layer over the seaside ambience. In [Shot 2], wet rhythmic thrusting sounds and the rhythmic slapping of skin as she rides layer with her soft moans and heavy continuous breathing. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 黄昏 · Random Play 门口砖街（10-20s）

> **场景**：Random Play 门口 —— 黄昏暖光，复古录像带/唱片店：红砖墙+黄色店面、黑底招牌白色手写字 "Random Play"、橱窗录像带海报+旧电视、左侧海报墙与禁停标志、右侧铁楼梯/绿色集装箱/堆叠轮胎、方砖地面、背景起重机与楼宇剪影
> **体位**：女上位坐姿前倾 → 传教士侧面俯视
> **分镜**：2 个 — Shot 1（5s）→ Shot 2（5s）

- 场景参考（Picture 4）
![200](../../../../ref/background/绝区零/RandomPlay门口.png)

- 女上位坐姿前倾（Picture 5，magapixels = 0.4）
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
- 传教士侧面俯视（Picture 6，magapixels = 0.4 时才正确实现）
> ⚠️ 历史动作卡「传教士式性交-侧面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt
Zenless Zone Zero Cartoon rendering style
```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the body, wings, and stockings of the female character, defined by <Picture 2>. Lock her slender feminine figure, her large white feathered angel wings with long trailing feathers, her white thigh-high stockings with garter straps, and her silver high heels, exactly as in <Picture 2>. Preserve body, wing, and stocking consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the dusk storefront street location: a vintage video rental shop with a red brick wall, yellow storefront, the black hand-lettered sign "Random Play", the poster wall, bicycles, the green container, and the square-brick pavement under warm dusk light. Do not inherit any characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the cowgirl seated forward-lean body layout and the frontal camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the missionary side body layout and the fixed overhead side camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot outdoor scene on a brick storefront street at dusk, featuring a naked anime angel girl (face from <Subject 1>, body and wings from <Subject 2>, vulva from <Subject 3>), having sex with a man whose face is never visible. [Shot 1] is a frontal view: she kneels on the square-brick pavement leaning forward with her hands on the ground, the man pressing down on her from behind as his penis enters her from behind, and she pumps her hips to control the rhythm. [Shot 2] cuts to a fixed overhead side view of missionary intercourse on the brick pavement: the woman's entire body is visible, the man shows only his lower body and part of his arms, his hand grasps her wrist while his penis continuously inserts into her vagina, her body trembles, her chest rises and falls violently, and she gasps. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body, white feathered angel wings, white thigh-high stockings, and silver high heels from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1], [Shot 2]): partially_preserved - the vulva anatomy from <Picture 3> is visible during penetration in both shots.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the dusk storefront street location with the "Random Play" sign is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the cowgirl seated forward-lean body layout and the frontal camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the missionary side body layout and the fixed overhead side camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an outdoor scene on a brick storefront street at dusk with warm orange light, long shadows, neon and shop glow beginning to appear, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The square-brick pavement in front of the vintage video rental shop with the hand-lettered sign "Random Play", matching the scene of <Subject 4>. Following the posture of <Subject 5>, the woman leans forward with her upper body, her head lowered facing downwards and then raised facing the camera, her chest tilted downwards. Her legs are spread and she is kneeling on the brick pavement, completely naked but for her white thigh-high stockings, her large white wings spread wide behind her. The man is behind the woman, his upper body slightly pressing down on her, his head out of frame. The man's penis extends from behind the woman and has already entered her vagina. The woman's hands are lying on the ground and she controls the thrusting rhythm by moving her hips back and forth, her wings fluttering with each pump, soft moans escaping between breaths. The camera stays static throughout [Shot 1], shooting from a frontal angle at a close range.

[Shot 2] At 00:05.000, the camera cuts to a fixed overhead side view. Following the posture of <Subject 6>, the woman is lying on the brick pavement in a missionary position, completely naked but for her white thigh-high stockings, and her entire body can be seen in the picture, her white wings spread out around her on the bricks. The man is positioned above her, only his lower body and part of his arms visible, his head out of frame. The man's hand is grasping the woman's wrist, and his penis is continuously inserting into her vagina. His lower body is constantly slapping the woman's buttocks. Due to the intense impact, the woman's body trembles slightly, her chest rises and falls violently, and from time to time she slightly opens her mouth and lets out a gasping sound. Her vulva matches <Subject 3> as the penis slides in and out. The picture is shot from a fixed overhead perspective to fully present the scene. The camera stays static throughout [Shot 2].

overall_soundscape:
A quiet dusk street ambience continues throughout the video: a low distant city hum, faint traffic, and a soft evening breeze. In [Shot 1], the soft thuds of her hands and knees on the brick pavement, wet thrusting sounds, and her rhythmic moans layer over the dusk ambience. In [Shot 2], the creak and scrape of their bodies shifting on the bricks, wet rhythmic thrusting sounds, the slapping of his lower body against her buttocks, her moans growing louder, and her heavy continuous breathing dominate. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 雨夜 · 404 门口（20-30s）

> **场景**：404 门口夜景 —— 弧形 404ERROR 霓虹招牌、玻璃入口与墙面海报、涂鸦墙、城市建筑、地铁入口指示、斜坡道路、路边积水，蓝色夜景主调，霓虹青白光映在湿润街面
> **体位**：后入式标准（低侧机位）→ 坐姿面部射精（高潮收尾）
> **分镜**：2 个 — Shot 1（4s）→ Shot 2（6s）

- 场景参考（Picture 4）
![200](../../../../ref/background/绝区零/404门口-夜景.png)

- 后入式标准（Picture 5；按当前 `ref/pose/pose.json` 动作卡映射，该 pose 深度图为「后入式性交-面部射精_正面_横图」）
![200](../../../../ref/pose/color/后入式性交-面部射精_正面_横图.png)
![200](../../../../ref/pose/depth/后入式性交-面部射精_正面_横图_depth.png)

- 坐姿面部射精（Picture 6）
![200](../../../../ref/pose/color/坐姿面部射精-阴茎对准脸部_正面_横图.png)
![200](../../../../ref/pose/depth/坐姿面部射精-阴茎对准脸部_正面_横图_depth.png)

##### English Prompt
Zenless Zone Zero Cartoon rendering style
```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the body, wings, and stockings of the female character, defined by <Picture 2>. Lock her slender feminine figure, her large white feathered angel wings with long trailing feathers, her white thigh-high stockings with garter straps, and her silver high heels, exactly as in <Picture 2>. Preserve body, wing, and stocking consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the rainy night entrance location: the arched neon sign "404ERROR", the glass entrance, the graffiti wall, the sloped wet road, and neon reflections in puddles, in a blue night palette. Do not inherit any characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the doggy-style rear entry body layout and the low side-front camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the lying face-up body layout with the head at the bottom of the frame and the frontal camera angle for the facial ejaculation of [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot scene on a wet sloped street at a rainy neon entrance, featuring a naked anime angel girl (face from <Subject 1>, body and wings from <Subject 2>, vulva from <Subject 3>), having sex with a man whose face is never visible. [Shot 1] is a doggy-style rear entry from a low side-front angle: the woman lies prone on the wet asphalt, the man kneels behind her holding her wrists, pulling them back while thrusting into her in the rain. [Shot 2] cuts to a frontal low view: the woman lies on her back with her head at the bottom of the frame, takes a few final deep thrusts, and the man's penis aims at her face and ejaculates onto it, ending on her dazed, settling final state. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body, white feathered angel wings, white thigh-high stockings, and silver high heels from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1]): partially_preserved - the vulva anatomy from <Picture 3> is visible during penetration in [Shot 1].
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the rainy night neon entrance street is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the doggy-style rear entry body layout and the low side-front camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the lying face-up layout with the head at the bottom of the frame and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an outdoor scene on a wet sloped street at a rainy night with a blue palette, neon reflections in puddles, continuous rain, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The sloped wet asphalt road near the neon entrance, matching the scene of <Subject 4>. Following the posture of <Subject 5>, the woman is lying on the wet asphalt in a lateral prone position, completely naked but for her white thigh-high stockings, with her head in the lower left corner and her side face floating above the ground. Her torso extends to the right in the lower half of the picture, and her legs and buttocks are near the center on the right side, her large white wings spread over the wet pavement, glistening with rain. The man is on the right side of the picture, kneeling and bending over the woman, holding her wrists with both hands and repeatedly pulling them backward, his head and face staying above the frame. The man's penis is thrusting into the woman's pussy, and they are having sex in the doggy style; his hips drive hard so his lower body slaps her buttocks with each thrust, and rain splashes around them. Her body arches and trembles from the impact, and her moans grow louder and more urgent. The camera is at a low position near the ground, shooting from the side front at close range, near a level view slightly angled upward; the woman in the left foreground, the man's body occupying the right upper background. The camera stays static throughout [Shot 1].

[Shot 2] At 00:04.000, the camera cuts to a frontal low view. Following the posture of <Subject 6>, the woman is in a lying position on the wet asphalt, completely naked but for her white thigh-high stockings, with her head at the bottom of the frame and her body at the top, her white wings around her on the rain-slicked ground, the neon "404ERROR" sign glowing in the background. She takes a few final deep thrusts, her body trembling and her mouth opening in sharp gasps. The man's penis then withdraws from her vagina and extends from the upper right corner of the frame, directly aimed at the woman's face, and ejaculates: a stream of semen shoots out and splashes onto her face, covering her cheeks and forehead as the rain washes over it. She lies back dazed, her chest heaving, a final shudder running through her body, her breathing gradually settling. The camera maintains a static low frontal position throughout [Shot 2].

overall_soundscape:
Continuous rain dominates the ambience throughout the video: rain on the pavement, dripping off surfaces, and the hush of the night street. In [Shot 1], the slapping of his lower body against her buttocks and wet thrusting sounds cut through the rain with splash sounds, her loud moans rising, and her heavy breathing. In [Shot 2], the final thrusts give way to the wet spray of ejaculation, her peak moan and gasp, then quiet settling: slow heavy breathing, rain dripping off her wings, and the hush of the night. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）或按 Duration Planner 配置
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  1. `ref/character/蕾米埃尔/exec-e724fa5d-a2fb-4858-b259-213277a73a94.png` → `<Picture 1>`（脸）
  2. `ref/character/蕾米埃尔/蕾米埃尔.png` → `<Picture 2>`（身体+翅膀+过膝袜）
  3. `ref/character/其他/人体_外阴特写.jpg` → `<Picture 3>`（外阴）
  4. 本工作流场景图 → `<Picture 4>`（W1 厄匹斯港 / W2 RandomPlay门口 / W3 404门口-夜景）
  5. 本工作流 pose 1 深度图 → `<Picture 5>`
  6. 本工作流 pose 2 深度图 → `<Picture 6>`
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W1 蛙式 = 0.4；W2 前倾 = 0.4、传教士侧面 = 0.4；其余未标注用默认值
- **跨工作流一致性**：`<Subject 1/2/3>` 的锁定文字与 "the man's face is never visible" 约束在三个提示词中保持完全一致；她的裸体+过膝袜+翅膀外观三个场景一致
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接（白天→黄昏→雨夜时间跳变显性化）；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）落在动作进行中
- **场景图文字**：W2 提示词中 "Random Play"、W3 提示词中 "404ERROR" 为画面内实际出现的招牌文字，按原文保留
- **后入式标准的深度图映射**：当前 `ref/pose/pose.json` 使用「后入式性交-面部射精_正面_横图」动作卡（该图内容为标准后入式构图），提交时按此引用

## 成片

![](assets/Case3/file-20260831043058599.mp4)

## 素材

![](assets/Case3/file-20260831043102985.mp4)

![](assets/Case3/file-20260831043103060.mp4)

![](assets/Case3/file-20260831043103122.mp4)
