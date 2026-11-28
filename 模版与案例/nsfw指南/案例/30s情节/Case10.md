# Case10 — Yasal 30 秒横屏剧院催眠失神（写实 · 3 × 10s 工作流）

> **角色**：Yasal —— 写实真人风格：黑直短发（齐刘海、透明发夹）、灰蓝眼睛、白衬衫+深色裙（夜间外出装扮）
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个镜头，每个 4-6 秒（6+4 / 5+5 / 4+6）
> **场景**：昏暗剧院观众席（远处舞台有演出、观众全是剪影、过道）（纯文字描述，不使用场景参考图，保持写实）
> **剧情**：她被催眠失神坐在观众席（眼神空洞、头轻晃）→无脸男沿过道走来、手搭她膝盖，她进一步瘫软→他跨坐座位上俯压她（她如木偶无反应）→检票员手电扫过（两人不动）→舞台掌声炸响，她猛地惊醒（惊醒=高潮，英雄镜头：光束里惊恐的脸）
> **动作**：纯文字 5 镜 + pose 深度图 1 镜（传教士-俯视_竖图）

## 全局约束（三个工作流共同遵守）

- **画风锁定**：电影级写实真人风格（真实皮肤质感、自然胶片颗粒、自然光、浅景深、35mm 手持感），**不是动漫、不是卡通**——每条提示词 detailed_description 开头声明
- 脸部与发型完全由 `<Picture 1>` 锁定，提示词不额外描述面部/发饰细节
- Yasal 服装：白衬衫 + 深色裙；失神状态下眼神空洞、身体松弛
- 男性**全程不露脸**（出画/阴影/背对镜头）、**全片无男性声音**（只有脚步、座椅声、衣物声等物理声）
- 检票员**全程无词**（只有手电咔哒声+脚步）、面部被帽檐/阴影挡住
- 观众=全部剪影、面部不清晰（避免生成多余清晰人脸）
- 她的声音：失神时完全无声 → 惊醒后倒抽气/颤抖呼吸（女性声音，允许）
- 舞台演出声=**画内声音**（远处、闷声，写在 detailed_description/overall_soundscape）
- 场景纯文字描述（写实风格不使用动漫场景参考图）；pose 深度图只用于有图的分镜
- 无配乐（`non_diegetic_music: N/A`）

## 固定参考图（Picture 1，三个工作流完全相同）

- Yasal 面部参考（Picture 1）
![250](../../../../ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png)

## 分镜总表（6 shots）

| # | 工作流 | 时间（全片） | 时长 | 动作来源 | 内容（剧情节拍） |
|---|--------|--------------|------|----------|------------------|
| 1 | W1 | 0-6s | 6s | 纯文字 | 昏暗剧院：舞台演出（虚化）、观众剪影；她坐 B 排失神（眼神空洞、头轻晃），无脸男沿过道走来 |
| 2 | W1 | 6-10s | 4s | 纯文字 | 他坐她前排（背对镜头）、手搭她膝盖，她进一步瘫软、下颌松弛、头微倾 |
| 3 | W2 | 0-5s | 5s | 传教士式性交-俯视_竖图 深度图 | 他跨坐座位上俯压她（俯视机位），她如木偶毫无反应 |
| 4 | W2 | 5-10s | 5s | 纯文字 | 座椅吱呀、她的头后仰垂落、眼睛半睁却空洞，全场只有他在动 |
| 5 | W3 | 0-4s | 4s | 纯文字 | 检票员手电沿过道扫过（无词），光束落在她玻璃样的眼睛上，两人不动 |
| 6 | W3 | 4-10s | 6s | 纯文字 | 舞台掌声炸响（演出结束）→她猛地惊醒：瞳孔收缩、手摸向大腿、倒抽气（英雄镜头：光束里惊恐的脸+空过道） |

---

## Workflow 1: 失神观众席 → 手搭膝盖（0-10s）

> **场景**：昏暗剧院观众席（远处舞台有演出、观众剪影、过道）
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s），全部纯文字动作

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark coat. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic theater scene at night, featuring a realistic young woman (face from <Subject 1>) in a white shirt and dark skirt, and a man whose face is never visible (<Subject 2>). [Shot 1] is a wide medium shot inside a dark theater: a performance plays on the distant stage, the audience is only silhouettes, and the woman sits alone in row B in a hypnotic trance — eyes half-lidded, head swaying faintly — while the man walks down the aisle toward her. [Shot 2] cuts closer: he sits in the seat in front of her, his back to the camera, and rests his hand on the top of her thigh; her body slumps further, her jaw going slack. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark coat is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a dark theater at night with a performance playing on the distant stage, rows of seats, and a horizontal 16:9 frame. The man's face is never visible in any shot, and the audience members are only silhouettes with no clear faces.

[Shot 1] A dark theater at night: a performance plays on the distant stage, out of focus, its light spilling over the empty front rows; the few audience members are only silhouettes, their faces never clearly visible. The woman (face and hair from <Subject 1>) sits alone in row B in a white shirt and dark skirt, in a hypnotic trance: her eyes are half-lidded and empty, her head sways faintly, and her body is perfectly still. A tall man in a dark coat walks down the aisle toward her, his face in shadow, his steps unhurried. The camera is static throughout [Shot 1], at a wide medium distance, at a level angle.

[Shot 2] At 00:06.000, a closer view from the aisle. The man sits in the seat in front of the woman, his back to the camera, his face out of frame; he rests his hand on the top of her thigh. Her body slumps further, her jaw goes slack, and her head tilts to one side, utterly limp. The camera is static throughout [Shot 2], at a medium close range, from behind the man's shoulder.

overall_soundscape:
A theater ambience continues throughout the video: the muffled, distant sound of the stage performance, the soft hum of the auditorium, and the creak of old seats. In [Shot 1], the man's unhurried footsteps down the aisle and the woman's faint breathing in her trance. In [Shot 2], the creak of the seat as he sits down, the soft contact of his hand on her thigh, her breathing going shallow, and the muffled performance sound. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 跨坐俯压 → 木偶般无反应（10-20s）

> **场景**：同一剧院观众席（B 排、过道、舞台光）
> **分镜**：2 个 — Shot 1（5s，传教士-俯视_竖图 深度图）→ Shot 2（5s，纯文字）

- 传教士俯视（Picture 2）
![200](../../../../ref/pose/color/传教士式性交-俯视_竖图.png)
![200](../../../../ref/pose/depth/传教士式性交-俯视_竖图_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark coat. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the missionary body layout (woman below, man above, her legs raised) and the fixed top-down camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic theater scene at night, featuring a realistic young woman (face from <Subject 1>) in a hypnotic trance and a man whose face is never visible (<Subject 2>). [Shot 1] is a fixed top-down view: the woman lies on her theater seat in a missionary position with her legs raised between the armrests, the man straddles the seat above her and thrusts into her from above, her body a limp puppet. [Shot 2] cuts to a side close view: her head falls limply back, her eyes half-open and empty, and only the man moves in the dark row. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark coat is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 1]): partially_preserved - the missionary body layout with the legs raised and the fixed top-down camera angle are retained for [Shot 1].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a dark theater at night with a performance playing on the distant stage, rows of seats, and a horizontal 16:9 frame. The man's face is never visible in any shot, and the audience members are only silhouettes with no clear faces.

[Shot 1] Row B of the dark theater, the distant stage light spilling over the seats. Following the posture of <Subject 3>, the woman (face and hair from <Subject 1>) is lying on her theater seat in a missionary position, her legs raised between the armrests, her white shirt bunched at her waist, and the man straddles the seat in front of her above her, only his lower body and part of his arms visible, his head out of frame. His penis is continuously inserting into her vagina; her body is a limp puppet, her arms loose at her sides, her face slack in the stage light. The picture is shot from a fixed top-down perspective over the row of seats. The camera stays static throughout [Shot 1].

[Shot 2] At 00:05.000, the camera cuts to a side close view. The woman's head falls limply back against the seat, her eyes half-open and empty, her breath shallow and even; only the man moves in the dark row, his shoulders rising and falling in a steady rhythm, his face never in frame. The distant stage light flickers over the two of them, and the empty seats around them hold perfect silence. The camera is static throughout [Shot 2], at a close range, at a level angle.

overall_soundscape:
The theater ambience continues throughout the video: the muffled, distant sound of the stage performance and the creak of old seats. In [Shot 1], the creak of the seat, the soft wet sounds of the steady rhythm, and her shallow, even breathing, with no moans at all. In [Shot 2], the creaking seat, the slow rise and fall of his shoulders, the faint rustle of fabric, and the muffled performance sound filling the stillness. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 手电扫过 → 掌声惊醒（20-30s）

> **场景**：同一剧院（过道、B 排、舞台掌声）
> **分镜**：2 个 — Shot 1（4s，纯文字）→ Shot 2（6s，纯文字，英雄镜头收尾）

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark coat. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic theater scene at night, featuring a realistic young woman (face from <Subject 1>) in a hypnotic trance and a man whose face is never visible (<Subject 2>). [Shot 1] is a medium shot: an usher in a dark uniform with a flashlight walks down the aisle, the beam sweeping across the two of them; the beam catches the woman's glassy, empty eyes, and neither of them moves. [Shot 2] cuts to a close view of the woman's face: the applause on the distant stage erupts as the performance ends, and she snaps awake — her pupils contracting, her hands flying to her lap, a sharp gasp tearing out of her. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1]): fully_preserved - the man in the dark coat is retained in [Shot 1], with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a dark theater at night with a performance playing on the distant stage, rows of seats, and a horizontal 16:9 frame. The man's face is never visible in any shot, the usher never shows a clear face, and the audience members are only silhouettes.

[Shot 1] Row B of the dark theater. An usher in a dark uniform, his face hidden under the brim of his cap, walks down the aisle with a flashlight; the beam sweeps across the row and lands on the woman (face and hair from <Subject 1>) and the man above her, his face never in frame. The beam catches the woman's glassy, empty eyes; she does not react, and neither does the man — they stay perfectly still while the usher's footsteps pause just out of frame. The camera is static throughout [Shot 1], at a medium distance, at a level angle.

[Shot 2] At 00:04.000, the camera cuts to a close view of the woman's face in row B. The applause on the distant stage erupts as the performance ends; the sound snaps through the row like a crack. The woman's eyes snap wide open, her pupils contracting, her hands flying to her lap; a sharp gasp tears out of her, her head whipping up, her chest heaving. In the flashlight beam left behind in the aisle, her face is terrified and dazed, and the row of empty seats stretches out behind her. The camera stays static throughout [Shot 2], at a close range, at a slightly low angle.

overall_soundscape:
The theater ambience continues throughout the video: the muffled, distant sound of the stage performance and the creak of old seats. In [Shot 1], the click of the flashlight, the usher's measured footsteps down the aisle, the beam sweeping the row, and the held stillness of the two of them. In [Shot 2], the distant applause erupting as the performance ends, the sudden rush of air as the woman gasps awake, the creak of the seat, and her sharp, trembling breaths over the fading applause. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  - W1：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
  - W2：Yasal 脸 → `<Picture 1>`；`ref/pose/depth/传教士式性交-俯视_竖图_depth.png` → `<Picture 2>`
  - W3：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
- **magapixels**：传教士-俯视_竖图 无特殊标注，用默认值
- **跨工作流一致性**：`<Subject 1>`（脸）与 `<Subject 2>`（无脸男）的锁定文字在三个提示词中保持完全一致；剧院（昏暗观众席+远处舞台演出光+过道）在 W1-W3 保持一致；她的服装状态按剧情递进（完整→衬衫扒至腰+裙摆堆叠→凌乱）
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）
- **声音设计**：舞台演出闷声（画内）+ 座椅吱呀 + 手电咔哒/检票员脚步（无词）+ 结尾掌声炸响；她的声音只在惊醒后出现（倒抽气/颤抖呼吸）；无音乐
- **写实约束**：不使用任何动漫场景参考图（场景纯文字），观众/检票员=剪影或面部不清晰（帽檐遮脸），避免生成多余清晰人脸
- **剧情要点**：她全程无高潮、无呻吟——失神的"木偶感"与结尾"惊醒"是情绪高潮点；提交时重点核对 W2 的无反应状态与 W3 的惊醒反差
