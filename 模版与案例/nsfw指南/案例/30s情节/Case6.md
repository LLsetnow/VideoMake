![](assets/Case6/file-20260901025912972.mp4)

![](assets/Case6/file-20260901025912994.mp4)

![](assets/Case6/file-20260901025913011.mp4)# Case6 — Yasal 30 秒横屏校园教室→天台偷情（写实 · 3 × 10s 工作流）

> **角色**：Yasal —— 写实真人风格：黑直短发（齐刘海、透明发夹）、灰蓝眼睛、校服（白衬衫+深色格纹裙+白及膝袜）
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个镜头，每个 4-6 秒（6+4 / 5+5 / 4+6）
> **场景**：白天阳光教室（上课中）→ 走廊楼梯 → 天台（午后、铁丝网围栏）（纯文字描述，不使用场景参考图，保持写实）
> **剧情**：正常上课→无脸男拍她肩膀把她叫走→天台铁丝网前快速脱衣→天台地面传教士→女上位前倾→楼梯口女声+脚步逼近→匆忙穿衣冲出、空天台收尾
> **动作**：纯文字 4 镜 + pose 深度图 2 镜（传教士侧面、女上位坐姿前倾）

## 全局约束（三个工作流共同遵守）

- **画风锁定**：电影级写实真人风格（真实皮肤质感、自然胶片颗粒、自然光、浅景深、35mm 手持感），**不是动漫、不是卡通**——每条提示词 detailed_description 开头声明
- 脸部与发型完全由 `<Picture 1>` 锁定，提示词不额外描述面部/发饰细节
- Yasal 服装：白衬衫（校服）+ 深色格纹裙 + 白及膝袜；脱衣后为裸体
- 男性**全程不露脸**（出画/阴影/只露手臂肩膀）、**全片无男性声音**（只有脚步声、衣物声、喘息等物理声）
- 同学/老师全部虚化或背对镜头、面部不清晰（避免生成多余清晰人脸）
- 她的声音：喘息、呻吟、压低的惊呼（女性声音，允许）；打断信号是**模糊不可辨的女声**（楼梯下同学）；无音乐（`non_diegetic_music: N/A`）
- 场景纯文字描述（写实风格不使用动漫场景参考图）；pose 深度图只用于有图的分镜

## 固定参考图（Picture 1，三个工作流完全相同）

- Yasal 面部参考（Picture 1）
![250](../../../../ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png)

## 分镜总表（6 shots）

| # | 工作流 | 时间（全片） | 时长 | 动作来源 | 内容（剧情节拍） |
|---|--------|--------------|------|----------|------------------|
| 1 | W1 | 0-6s | 6s | 纯文字 | 教室上课：老师背影+虚化同学，他拍她肩膀，她环视后溜出教室门 |
| 2 | W1 | 6-10s | 4s | 纯文字 | 走廊+楼梯：他搂她后腰快步上楼，推开天台门 |
| 3 | W2 | 0-5s | 5s | 纯文字 | 天台铁丝网前：衬衫被脱肩、格纹裙拉过胯、袜子脱下丢开 |
| 4 | W2 | 5-10s | 5s | 传教士式性交-侧面_横图 深度图（0.4） | 天台地面传教士（俯侧固定机位） |
| 5 | W3 | 0-4s | 4s | 女上位-坐姿前倾_正面_横图 深度图（0.4） | 铁丝网前女上位前倾骑乘 |
| 6 | W3 | 4-10s | 6s | 纯文字 | 楼梯口女声+脚步逼近→匆忙拉回衬衫冲出→空天台+风卷袜子的收尾（英雄镜头） |

---

## Workflow 1: 上课被叫走 → 楼梯（0-10s）

> **场景**：阳光教室（课桌、黑板、虚化同学）→ 走廊楼梯（午后长窗光）
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s），全部纯文字动作

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall young male student in a plain school uniform. His face is never visible in any shot — only his arm, shoulder, or back is ever in frame — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic school scene, featuring a realistic young female student (face from <Subject 1>) in a white shirt, dark plaid skirt, and white knee socks, and a male student whose face is never visible (<Subject 2>). [Shot 1] is a medium shot inside a sunlit classroom: the man taps her shoulder at her desk; she glances around the out-of-focus students, stands, and slips out through the door. [Shot 2] cuts to the stairwell: he leads her up the stairs with his hand at the small of her back and pushes open a heavy door at the top. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the male student is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a sunlit classroom and a school stairwell in the late afternoon, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] A sunlit classroom: rows of desks, a teacher at the chalkboard with her back to the camera, and out-of-focus students at their desks, their faces never clearly visible. The woman (face and hair from <Subject 1>) sits at a desk near the window in her school uniform: a white shirt, a dark plaid skirt, and white knee socks. A tall man in a plain school uniform sits beside her, only his arm and part of his shoulder visible, his face never in frame. He taps her shoulder with one finger; she glances around the classroom, stands, and slips out through the door. The camera is static throughout [Shot 1], at a medium distance, at a level angle.

[Shot 2] At 00:06.000, the corridor outside, late-afternoon light through tall windows. He leads her along the corridor and up the stairwell, his hand at the small of her back, their steps quick. They reach a heavy door at the top of the stairs, and he pushes it open. The camera is fixed at the top of the stairwell throughout [Shot 2], watching them come up at a medium distance.

overall_soundscape:
A daytime classroom ambience continues throughout the video: the soft scratch of chalk on a board, the low murmur of students, and the creak of chairs. In [Shot 1], the tap of his finger on her shoulder, the chair leg scuffing the floor as she stands, and the murmur continuing as she slips out the door. In [Shot 2], their footsteps on the corridor tiles and the stairwell, a gust of wind at the open top door, and her quickened breathing. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 天台脱衣 → 地面传教士（10-20s）

> **场景**：天台（铁丝网围栏、午后开阔天空、风）
> **分镜**：2 个 — Shot 1（5s，纯文字）→ Shot 2（5s，传教士侧面 深度图）

- 传教士侧面俯视（Picture 2，magapixels = 0.4 时才正确实现）
> ⚠️ 历史动作卡「传教士式性交-侧面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall young male student in a plain school uniform. His face is never visible in any shot — only his arm, shoulder, or back is ever in frame — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the missionary side body layout (woman on the rooftop floor, man above her) and the fixed overhead side camera angle for [Shot 2]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic school rooftop scene in the late afternoon, featuring a realistic young female student (face from <Subject 1>) and a male student whose face is never visible (<Subject 2>). [Shot 1] is a medium shot: the man pushes the woman up against the chain-link fence, unbuttons and pulls her white shirt off her shoulders, hikes the dark plaid skirt up over her hips, and tosses her white knee socks aside. [Shot 2] cuts to a fixed overhead side view: the woman lies on the concrete rooftop floor while the man shows only his lower body and part of his arms, his hand grasping her wrist while his penis continuously inserts into her vagina. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the male student is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 2]): partially_preserved - the missionary side body layout and the fixed overhead side camera angle are retained for [Shot 2].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a school rooftop with a chain-link fence, an open late-afternoon sky, and wind, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The school rooftop: a chain-link fence, an open late-afternoon sky, wind moving through the woman's hair. The man pushes the woman (face and hair from <Subject 1>) up against the chain-link fence, unbuttons the white shirt and pulls it off her shoulders, hikes the dark plaid skirt up over her hips, and pulls off her white knee socks, tossing them aside. Her bare chest rises and falls in the wind, her eyes darting toward the stairwell door. The camera is static throughout [Shot 1], at a medium distance, at a level angle.

[Shot 2] At 00:05.000, the camera cuts to a fixed overhead side view. Following the posture of <Subject 3>, the woman is lying on the concrete rooftop floor in a missionary position, and her entire body can be seen in the picture. The man is positioned above her, only his lower body and part of his arms visible, his head out of frame. The man's hand is grasping the woman's wrist, and his penis is continuously inserting into her vagina. His lower body is constantly slapping the woman's buttocks. Due to the intense impact, the woman's body trembles slightly, her chest rises and falls violently, and from time to time she slightly opens her mouth and lets out a gasping sound, then presses her lips together to hold the noise down. The picture is shot from a fixed overhead perspective to fully present the scene. The camera stays static throughout [Shot 2].

overall_soundscape:
An afternoon rooftop ambience continues throughout the video: an open sky, the wind moving through the chain-link fence with a low whistle, and faint distant schoolyard sounds. In [Shot 1], the rustle of fabric as the shirt is pulled off her shoulders, the soft plop of the knee socks landing on the concrete, the soft thud of her back against the fence, and her small gasp. In [Shot 2], wet thrusting sounds, his lower body slapping her buttocks, and her moans rising before she presses her lips together; the wind whistles through the fence. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 铁丝网前女上位 → 匆忙逃离（20-30s）

> **场景**：同一天台（铁丝网前）→ 空天台收尾
> **分镜**：2 个 — Shot 1（4s，女上位坐姿前倾 深度图）→ Shot 2（6s，纯文字，英雄镜头收尾）

- 女上位坐姿前倾（Picture 2，magapixels = 0.4）
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall young male student in a plain school uniform. His face is never visible in any shot — only his arm, shoulder, or back is ever in frame — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the cowgirl seated forward-lean body layout (kneeling, leaning forward, hands braced in front) and the frontal camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic school rooftop scene in the late afternoon, featuring a realistic young female student (face from <Subject 1>) and a male student whose face is never visible (<Subject 2>). [Shot 1] is a frontal view: the woman kneels on the rooftop floor in a cowgirl forward-lean position, braced against the chain-link fence, riding the man who thrusts up into her from behind. [Shot 2] cuts to the same rooftop: a muffled, indistinct female voice and quick footsteps approach on the stairwell; the two hurry down the stairs, and the door swings open on the now-empty rooftop. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the male student is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 1]): partially_preserved - the cowgirl seated forward-lean body layout and the frontal camera angle are retained for [Shot 1].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a school rooftop with a chain-link fence, an open late-afternoon sky, and wind, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The school rooftop, the chain-link fence, the open late-afternoon sky. Following the posture of <Subject 3>, the woman (face and hair from <Subject 1>) is kneeling on the concrete rooftop floor in a cowgirl forward-lean position, leaning forward against the chain-link fence, her head lowered facing downwards and then raised facing the camera, her chest tilted downwards. Her legs are spread and she is kneeling, her bare chest and bare thighs exposed. The man is behind the woman, his upper body slightly pressing down on her, his head out of frame. The man's penis extends from behind the woman and has already entered her vagina. The woman's hands are braced on the chain-link fence and she controls the thrusting rhythm by moving her hips back and forth. The camera stays static throughout [Shot 1], shooting from a frontal angle at a medium range.

[Shot 2] At 00:04.000, the camera holds on the rooftop. Quick footsteps on the stairwell and a muffled, indistinct female voice calling from below; the man and the woman freeze. He yanks the white shirt back over the woman's shoulders, smooths the dark plaid skirt down, and grabs her wrist; the two turn and hurry down the stairs. The door swings open — the rooftop is empty, the chain-link fence rattling in the wind, only the woman's white knee socks lying crumpled on the concrete. The camera stays static throughout [Shot 2].

overall_soundscape:
The rooftop ambience continues throughout the video: the wind whistling through the chain-link fence and faint distant schoolyard sounds. In [Shot 1], the soft thuds of her hands on the fence, wet thrusting sounds, and her moans growing louder. In [Shot 2], quick footsteps on the stairwell and a muffled, indistinct female voice from below; the sudden hush of held breath, the rustle of fabric as the shirt is yanked back on, their hurried footsteps rushing down the stairs, and the door swinging open on the empty rooftop with the wind rattling the fence. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  - W1：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
  - W2：Yasal 脸 → `<Picture 1>`；旧动作卡「传教士式性交-侧面_横图」（当前 `ref/pose/pose.json` 无同名条目） → `<Picture 2>`
  - W3：Yasal 脸 → `<Picture 1>`；旧动作卡「女上位-坐姿前倾_正面_横图」（当前 `ref/pose/pose.json` 无同名条目） → `<Picture 2>`
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W2 传教士侧面 = 0.4；W3 女上位前倾 = 0.4；其余未标注用默认值
- **跨工作流一致性**：`<Subject 1>`（脸）与 `<Subject 2>`（无脸男学生）的锁定文字在三个提示词中保持完全一致；天台（铁丝网+午后天空+风）在 W2/W3 保持一致；她的服装状态按剧情递进（完整校服→脱至裸体→拉回衬衫冲出）
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）
- **声音设计**：全程环境声（教室粉笔/低语 → 天台风声）+ 她的喘息/呻吟；打断信号为**模糊不可辨的女声**（楼梯下同学，不引入说话人 ID、不用 `<d>`）；无音乐
- **写实约束**：不使用任何动漫场景参考图（场景纯文字），同学/老师虚化或背对镜头、面部不清晰，避免生成多余清晰人脸


## 成片

![](assets/Case6/file-20260901025909105.mp4)
## 素材

![](assets/Case6/file-20260901025919304.mp4)

![](assets/Case6/file-20260901025919321.mp4)

![](assets/Case6/file-20260901025919372.mp4)
