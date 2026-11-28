# Case4 — 千夏（绝区零）30 秒横屏便利店试衣间偷情（3 × 10s 工作流）

> **角色**：千夏 Chinatsu（绝区零 ZZZ）—— 灰绿波浪短发、青色星星发饰、多彩星瞳
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个 pose，每个 3-6 秒，加速构建节奏（6+4 / 5+5 / 4+6）
> **场景**：六分街 141 便利店试衣间（白天，店内），单场景内偷情递进
> **基调**：偷情/怕被发现——门闩、进店铃、店员喊话、脚步声、门把手逐级递进
> **动作描述**：优先采用 `ref/Resources.json` 中每个 pose 的现成提示词描述

## 全局约束（三个工作流共同遵守）

- 提示词**不描述任何人物面部或发饰**：脸部与发型完全由 `<Picture 1>` 锁定
- 千夏全片：**裸体 + 标志性粉白条纹袖套/腿套 + 粉色大腿绑带 + 青色松糕鞋**（按裸体三视图参考；开场穿常服，W1 内脱掉）
- 男性**全程不露脸**（头部出画或出画外）、**全片无男性声音**（只有身体物理声）
- 便利店 BGM 为**画内声音**（写在 detailed_description/overall_soundscape），`non_diegetic_music: N/A`
- 她的声音强度曲线：压低闷哼 → 接近失控 → 峰值 → 死寂屏息（跨工作流递进）
- **画风锁定**：Zenless Zone Zero 卡通渲染（cel-shaded，非写实）——每条提示词 detailed_description 开头声明
- 每个工作流参考图 6 张：Picture 1 脸 / 2 身体+配饰 / 3 外阴 / 4 场景 / 5-6 两个 pose 深度图

## 固定参考图（Picture 1-3，三个工作流完全相同）

- 面部参考（Picture 1）
![200](../../../../ref/character/千夏/千夏_正脸头像_v4.png)

- 身体+配饰参考（Picture 2，裸体三视图）
![200](../../../../ref/character/千夏/千夏-nude.png)

- 外阴参考（Picture 3）
![200](../../../../ref/character/其他/人体_外阴特写.jpg)

## 分镜总表（6 poses）

| # | 工作流 | 时间（全片） | 时长 | Pose（深度图） | 内容（偷情节拍） |
|---|--------|--------------|------|----------------|------------------|
| 1 | W1 | 0-6s | 6s | 跪姿口交-站立男性_侧面 | 门闩扣死→快脱常服→跪下克制的口交 |
| 2 | W1 | 6-10s | 4s | 女上位-坐姿蛙式_正面（0.4） | 地砖上蛙式骑乘+瞟镜子倒影；进店铃响起（她一僵） |
| 3 | W2 | 0-5s | 5s | 传教士式性交-侧面_横图（0.4） | 背靠布帘平躺，抓手腕持续插入；门外店员模糊喊话（她屏息） |
| 4 | W2 | 5-10s | 5s | 女上位-坐姿前倾_正面_横图（0.4） | 跪姿前倾手撑地砖、对镜泵动；门口脚步经过→声音放轻 |
| 5 | W3 | 0-4s | 4s | 后入式性交-标准（深度图=后入式性交-面部射精_正面_横图） | 俯卧在门口旁地砖，抓双腕后拉猛 thrust；门外 BGM 渐强 |
| 6 | W3 | 4-10s | 6s | 坐姿面部射精-阴茎对准脸部_正面_横图 | 最后深插→抽出→面部射精；门把手转动、两人定格屏息（英雄镜头） |

---

## Workflow 1: 门闩扣死 → 口交 → 地板蛙式（0-10s）

> **场景**：141 便利店试衣间 —— 米色布帘、LED 全身镜、低衣架（挂满衣物）、浅灰亮面地砖、带小玻璃窗的门+门闩；暖色 LED 灯带
> **体位**：跪姿口交（站立男性）→ 女上位坐姿蛙式
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s）

- 场景参考（Picture 4，141 便利店门店+街区）
![200](../../../../ref/background/绝区零/六分街141便利店.png)

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
<Subject 2> is the body and accessories of the female character, defined by <Picture 2>. Lock her petite slender figure, her pink-and-white striped elbow-length arm sleeves, her pink-and-white striped leg warmers, her pink thigh strap, and her teal platform shoes, exactly as in <Picture 2>. Preserve body and accessory consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the convenience-store location identity: the blue and gold storefront with the "141 / ONE FOUR ONE" sign, the street-front glass doors, and the daytime city-block surroundings; the video takes place in a small fitting room inside this store. Do not inherit characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the kneeling oral body layout and the side camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the cowgirl seated frog position body layout, the vulva-facing-the-camera composition, and the frontal camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot scene in the 141 convenience-store fitting room during the day, featuring a naked anime girl (face <Subject 1>, body <Subject 2>, vulva <Subject 3>) having secret sex with a man whose face is never visible. [Shot 1] opens with the door latch clicking shut, then she strips off her everyday shirt and kneels on the tile floor to perform restrained oral sex on his standing body from a side angle. [Shot 2] cuts to a frontal view: she sits on the floor in a frog position with her knees apart and bent downward, her vulva facing the camera, riding steadily over his inserted penis while glancing at her mirror reflection. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body and striped accessories from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1], [Shot 2]): partially_preserved - the vulva anatomy from <Picture 3> is visible during the oral section and faces the camera in [Shot 2].
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the 141 convenience-store fitting room is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the kneeling oral body layout and the side camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the cowgirl seated frog layout, the vulva-facing-the-camera composition, and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an indoor scene in a small convenience-store fitting room with warm LED strip lighting, a beige fabric folding screen, a full-length mirror, a low clothing rack with hangers, a glossy light-gray tile floor, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The small fitting room of <Subject 4>: the beige folding screen, the full-length mirror with LED strip lighting, the low clothing rack, and the glossy light-gray tile floor. The woman, combining <Subject 1>, <Subject 2>, and <Subject 3>, stands in her everyday outfit of a white shirt with pink straps and a black studded choker. The man stands facing her, only his torso, arms, and legs visible, his head out of frame. The latch of the door clicks shut behind them. She quickly strips off the shirt, leaving herself naked but for her pink-and-white striped arm sleeves, leg warmers, and thigh strap. She drops to her knees on the tile floor. Following the posture of <Subject 5>, the woman is in a kneeling position and the man is standing, his legs on the left side of the frame. Her mouth slightly holds the head of the man's penis and her hand grips his thigh; she performs a restrained oral stroke, her head moving back and forth in a smooth rhythm, keeping her moans low. The camera stays static throughout [Shot 1], shooting from a side angle at a close range.

[Shot 2] At 00:06.000, the camera cuts to a frontal view. Following the posture of <Subject 6>, the woman is sitting on the glossy tile floor in a frog position, naked but for her pink-and-white striped arm sleeves, leg warmers, and thigh strap. Her legs are spread out in a frog-like position, her knees are apart and bent downward, and her vulva is facing the camera, matching <Subject 3>. Her upper body is reclined backward against the folding screen, her elbows pressing against her waist, her forearms raised and slightly extended outward, the lines connecting her shoulders, elbows and wrists forming a symmetrical W shape. The man's penis is thrusting into the vagina, and the man's hands are holding the woman's waist. She rides steadily, her hips moving up and down over the inserted penis in a smooth vertical rhythm, glancing sideways at her own reflection in the full-length mirror, keeping her soft moans low. The camera maintains a static frontal position throughout [Shot 2].

overall_soundscape:
A quiet indoor ambience continues throughout the video: the faint hum of fluorescent light and soft convenience-store background music muffled through the fitting room door. In [Shot 1], the latch of the door clicks shut, the rustle of fabric as the shirt is stripped off, the wet friction and soft slurping sounds of her mouth over the penis, and her low muffled moans layer over the ambience. In [Shot 2], wet rhythmic thrusting sounds, the soft scrape of her back against the folding screen, and her suppressed moans layer over the muffled store music; near the end, a distant store entrance chime makes her flinch and hold her breath. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 布帘前传教士 → 对镜前倾骑乘（10-20s）

> **场景**：同一试衣间 —— 布帘后侧（传教士）与全身镜前（前倾骑乘）
> **体位**：传教士侧面俯视 → 女上位坐姿前倾
> **分镜**：2 个 — Shot 1（5s）→ Shot 2（5s）

- 场景参考（Picture 4，141 便利店门店+街区）
![200](../../../../ref/background/绝区零/六分街141便利店.png)

- 传教士侧面俯视（Picture 5，magapixels = 0.4 时才正确实现）
> ⚠️ 历史动作卡「传教士式性交-侧面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
- 女上位坐姿前倾（Picture 6，magapixels = 0.4）
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the body and accessories of the female character, defined by <Picture 2>. Lock her petite slender figure, her pink-and-white striped elbow-length arm sleeves, her pink-and-white striped leg warmers, her pink thigh strap, and her teal platform shoes, exactly as in <Picture 2>. Preserve body and accessory consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the convenience-store location identity: the blue and gold storefront with the "141 / ONE FOUR ONE" sign, the street-front glass doors, and the daytime city-block surroundings; the video takes place in a small fitting room inside this store. Do not inherit characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the missionary side body layout and the fixed overhead side camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the cowgirl seated forward-lean body layout and the frontal camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot scene in the 141 convenience-store fitting room during the day, featuring a naked anime girl (face <Subject 1>, body <Subject 2>, vulva <Subject 3>) having secret sex with a man whose face is never visible. [Shot 1] is a fixed overhead side view of missionary intercourse on the tile floor: the woman lies with her back against the folding screen, the man shows only his lower body and part of his arms, his hand grasps her wrist while his penis continuously inserts into her vagina, her body trembles, her chest heaves violently, and she gasps while clamping her jaw to stay quiet. [Shot 2] cuts to a frontal view: she kneels on the floor leaning forward with her hands on the ground, the man pressing down on her from behind, pumping her hips toward the full-length mirror. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body and striped accessories from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1]): partially_preserved - the vulva anatomy from <Picture 3> is visible as the penis slides in and out in [Shot 1].
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the 141 convenience-store fitting room is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the missionary side body layout and the fixed overhead side camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the cowgirl seated forward-lean body layout and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an indoor scene in a small convenience-store fitting room with warm LED lighting, a beige fabric folding screen, a full-length mirror, a glossy light-gray tile floor, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The beige folding screen side of the fitting room, matching the store of <Subject 4>. Following the posture of <Subject 5>, the woman is lying on the glossy tile floor in a missionary position, her back against the folding screen, naked but for her pink-and-white striped arm sleeves, leg warmers, and thigh strap, and her entire body can be seen in the picture. The man is positioned above her, only his lower body and part of his arms visible, his head out of frame. The man's hand is grasping the woman's wrist, and his penis is continuously inserting into her vagina. His lower body is constantly slapping the woman's buttocks. Due to the intense impact, the woman's body trembles slightly, her chest rises and falls violently, and she lets out gasping sounds from time to time before clamping her jaw to keep the noise down. Her vulva matches <Subject 3> as the penis slides in and out. The picture is shot from a fixed overhead perspective to fully present the scene. The camera stays static throughout [Shot 1].

[Shot 2] At 00:05.000, the camera cuts to a frontal view. Following the posture of <Subject 6>, the woman is kneeling on the glossy tile floor in a cowgirl forward-lean position, naked but for her pink-and-white striped arm sleeves, leg warmers, and thigh strap. She leans forward with her upper body, her head lowered facing downwards and then raised facing the camera, her chest tilted downwards. Her legs are spread and she is kneeling. The man is behind the woman, his upper body slightly pressing down on her, his head out of frame. The man's penis extends from behind the woman and has already entered her vagina. The woman's hands are lying on the ground and she controls the thrusting rhythm by moving her hips back and forth, pumping toward the full-length mirror where her reflection mirrors the motion, her soft moans kept low. The camera stays static throughout [Shot 2], shooting from a frontal angle at a close range.

overall_soundscape:
The quiet fitting-room ambience continues throughout the video: the faint hum of fluorescent light and soft convenience-store background music muffled through the door. In [Shot 1], the creak of the folding screen, wet thrusting sounds, his lower body slapping her buttocks, and her moans growing louder before she clamps her jaw layer over the ambience; a muffled, indistinct call from outside makes her go still. In [Shot 2], the soft thuds of her hands on the tile, wet thrusting sounds, and her suppressed moans layer over the ambience; footsteps pass by just outside the door and her sound drops to a whisper. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 门口后入 → 面部射精定格（20-30s）

> **场景**：同一试衣间 —— 门口一侧（小玻璃窗透出店内灯光）
> **体位**：后入式标准（低侧机位）→ 坐姿面部射精（高潮定格收尾）
> **分镜**：2 个 — Shot 1（4s）→ Shot 2（6s）

- 场景参考（Picture 4，141 便利店门店+街区）
![200](../../../../ref/background/绝区零/六分街141便利店.png)

- 后入式标准（Picture 5；按当前 `ref/pose/pose.json` 动作卡映射，该 pose 深度图为「后入式性交-面部射精_正面_横图」）
![200](../../../../ref/pose/color/后入式性交-面部射精_正面_横图.png)
![200](../../../../ref/pose/depth/后入式性交-面部射精_正面_横图_depth.png)

- 坐姿面部射精（Picture 6）
![200](../../../../ref/pose/color/坐姿面部射精-阴茎对准脸部_正面_横图.png)
![200](../../../../ref/pose/depth/坐姿面部射精-阴茎对准脸部_正面_横图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the face and hair of the female character, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the body and accessories of the female character, defined by <Picture 2>. Lock her petite slender figure, her pink-and-white striped elbow-length arm sleeves, her pink-and-white striped leg warmers, her pink thigh strap, and her teal platform shoes, exactly as in <Picture 2>. Preserve body and accessory consistency throughout the video; do not inherit the background or pose from <Picture 2>.
<Subject 3> is the vulva reference for the female character, defined by <Picture 3>. Lock the external genital anatomy: full symmetrical labia majora, prominently protruding pink labia minora with clear natural folds, clitoral hood covering the clitoris, narrow slit vaginal opening, fair surrounding skin, and neatly trimmed pubic area. Use this reference for consistent pussy depiction; do not inherit background or pose from <Picture 3>.
<Subject 4> is the scene reference, defined by <Picture 4>. Use this image to lock the convenience-store location identity: the blue and gold storefront with the "141 / ONE FOUR ONE" sign, the street-front glass doors, and the daytime city-block surroundings; the video takes place in a small fitting room inside this store. Do not inherit characters from <Picture 4>.
<Subject 5> is the sex position and camera angle reference, defined by <Picture 5>. Use this depth map to lock the doggy-style rear entry body layout and the low side-front camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 5>.
<Subject 6> is the sex position and camera angle reference, defined by <Picture 6>. Use this depth map to lock the lying face-up body layout with the head at the bottom of the frame and the frontal camera angle for the facial ejaculation of [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 6>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot scene in the 141 convenience-store fitting room during the day, featuring a naked anime girl (face <Subject 1>, body <Subject 2>, vulva <Subject 3>) having secret sex with a man whose face is never visible. [Shot 1] is a doggy-style rear entry from a low side-front angle: the woman lies prone on the tile floor near the door, the man kneels behind her holding her wrists, pulling them back while thrusting into her. [Shot 2] cuts to a frontal low view: the woman lies on her back with her head at the bottom of the frame, takes a few final deep thrusts, and the man's penis aims at her face and ejaculates onto it as the door handle turns; the two freeze, breath held, on her dazed final state. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's body and striped accessories from <Picture 2> are retained in both shots.
<Subject 3> (appears in [Shot 1]): partially_preserved - the vulva anatomy from <Picture 3> is visible during penetration in [Shot 1].
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the 141 convenience-store fitting room is retained in both shots.
<Subject 5> (appears in [Shot 1]): partially_preserved - the doggy-style rear entry body layout and the low side-front camera angle are retained for [Shot 1].
<Subject 6> (appears in [Shot 2]): partially_preserved - the lying face-up layout with the head at the bottom of the frame and the frontal camera angle are retained for [Shot 2].

detailed_description:
The target video is in a Zenless Zone Zero cartoon rendering style (cel-shaded, not photorealistic), showing an indoor scene in a small convenience-store fitting room with warm LED lighting, a beige fabric folding screen, a full-length mirror, a glossy light-gray tile floor, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The door side of the fitting room, the small glass window glowing with store light, matching <Subject 4>. Following the posture of <Subject 5>, the woman is lying on the glossy tile floor in a lateral prone position near the door, naked but for her striped arm sleeves, leg warmers, and thigh strap, her head in the lower left corner and her side face floating above the floor. Her torso extends to the right in the lower half of the picture, her legs and buttocks near the center right. The man is on the right, kneeling and bending over the woman, holding her wrists with both hands and repeatedly pulling them backward, his head staying above the frame. The man's penis is thrusting into the woman's pussy in the doggy style; his hips drive hard so his lower body slaps her buttocks with each thrust. Her body arches and trembles from the impact, and her moans grow louder and more urgent. The camera is low near the floor, shooting from the side front at close range, near level view slightly angled upward; the woman in the left foreground, the man's body occupying the right upper background. The camera stays static throughout [Shot 1].

[Shot 2] At 00:04.000, the camera cuts to a frontal low view. Following the posture of <Subject 6>, the woman is in a lying position on the glossy tile floor, with her head at the bottom of the frame and her body at the top, her hair spread across the tile, the small glass window glowing with store light behind her. She takes a few final deep thrusts, her body trembling and her mouth opening in sharp gasps. The man's penis then withdraws from her vagina and extends from the upper right corner of the frame, directly aimed at the woman's face, and ejaculates: a stream of semen splashes onto her face, covering her cheeks and forehead. The door handle begins to turn with a muffled, indistinct call from outside; the two freeze, breath held. She lies back dazed, her chest heaving, a final shudder through her body, her breathing gradually settling. The camera maintains a static low frontal position throughout [Shot 2].

overall_soundscape:
The fitting-room ambience continues throughout the video: a faint fluorescent hum and the convenience-store background music growing slightly louder through the door as customers pass. In [Shot 1], his lower body slapping her buttocks and wet thrusting sounds cut through the ambience, with her loud moans rising and her heavy breathing. In [Shot 2], the final thrusts give way to the wet spray of ejaculation and her peak moan and gasp, then sudden quiet: the slow turn of the door handle, a muffled indistinct call from outside, and both of them holding their breath as the hum of the fluorescent light fills the silence. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）或按 Duration Planner 配置
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  1. `ref/character/千夏/千夏_正脸头像_v4.png` → `<Picture 1>`（脸）
  2. `ref/character/千夏/千夏-nude.png` → `<Picture 2>`（身体+条纹配饰）
  3. `ref/character/其他/人体_外阴特写.jpg` → `<Picture 3>`（外阴）
  4. `ref/background/绝区零/六分街141便利店.png` → `<Picture 4>`（场景，三个工作流相同）
  5. 本工作流 pose 1 深度图 → `<Picture 5>`
  6. 本工作流 pose 2 深度图 → `<Picture 6>`
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W1 蛙式 = 0.4；W2 传教士侧面 = 0.4、前倾 = 0.4；其余未标注用默认值
- **跨工作流一致性**：`<Subject 1/2/3>` 的锁定文字与 "the man's face is never visible" 约束在三个提示词中保持完全一致；试衣间内部元素（布帘/LED 镜/地砖/门闩）三个工作流一致
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）落在动作进行中
- **画内文字**：W1-W3 提示词中 "141 / ONE FOUR ONE" 为场景参考中实际出现的招牌文字，按原文保留
- **声音设计**：便利店 BGM 为画内声音（diegetic），写在 detailed_description 与 overall_soundscape；`non_diegetic_music: N/A`；门外喊话为模糊不可辨（不引入说话人 ID、不用 `<d>`）
- **后入式标准的深度图映射**：当前 `ref/pose/pose.json` 使用「后入式性交-面部射精_正面_横图」动作卡（该图内容为标准后入式构图），提交时按此引用

## 成片

![](assets/Case4/file-20260831043005831.mp4)

## 素材

![](assets/Case4/file-20260831043015537.mp4)

![](assets/Case4/file-20260831043015581.mp4)

![](assets/Case4/file-20260831043015682.mp4)
