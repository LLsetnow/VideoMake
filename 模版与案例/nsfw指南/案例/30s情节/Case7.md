# Case7 — Yasal 30 秒横屏夜间停车场车内偷情（写实 · 3 × 10s 工作流）

> **角色**：Yasal —— 写实真人风格：黑直短发（齐刘海、透明发夹）、灰蓝眼睛、白衬衫+深色裙（夜出装扮）
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个镜头，每个 4-6 秒（6+4 / 5+5 / 4+6）
> **场景**：夜间露天停车场 → 深色轿车（车头灯亮着）后排座舱（纯文字描述，不使用场景参考图，保持写实）
> **剧情**：停车场里她滑进亮着车头灯的轿车后排→无脸男跟上→后排女上位前倾骑乘→翻倒座椅传教士→保安手电扫过挡风玻璃+脚步逼近（无词）→停止、外套罩身、两人溜进黑暗、空车+阴影里凌乱的她收尾
> **动作**：纯文字 5 镜 + pose 深度图 1 镜（女上位坐姿前倾）

## 全局约束（三个工作流共同遵守）

- **画风锁定**：电影级写实真人风格（真实皮肤质感、自然胶片颗粒、自然光、浅景深、35mm 手持感），**不是动漫、不是卡通**——每条提示词 detailed_description 开头声明
- 脸部与发型完全由 `<Picture 1>` 锁定，提示词不额外描述面部/发饰细节
- Yasal 服装：白衬衫（领口已解开）+ 深色裙；脱衣后为裸体
- 男性**全程不露脸**（背对镜头/阴影/出画）、**全片无男性声音**（只有脚步声、衣物声、车声等物理声）
- 保安**全程无词**（只有脚步声、手电咔哒声、呼吸声），面部被帽檐/逆光挡住或只出现在车窗外
- 她的声音：呻吟、压低的惊呼（女性声音，允许）；无音乐（`non_diegetic_music: N/A`）
- 场景纯文字描述（写实风格不使用动漫场景参考图）；pose 深度图只用于有图的分镜

## 固定参考图（Picture 1，三个工作流完全相同）

- Yasal 面部参考（Picture 1）
![250](../../../../ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png)

## 分镜总表（6 shots）

| # | 工作流 | 时间（全片） | 时长 | 动作来源 | 内容（剧情节拍） |
|---|--------|--------------|------|----------|------------------|
| 1 | W1 | 0-6s | 6s | 纯文字 | 停车场：她从前排副驾滑进亮着车头灯的车后排 |
| 2 | W1 | 6-10s | 4s | 纯文字 | 后排座舱：她跪在他两腿间、手探进他裤腰，他跨坐她 |
| 3 | W2 | 0-5s | 5s | 女上位-坐姿前倾_正面_横图 深度图（0.4） | 后排女上位前倾骑乘（手撑座椅靠背、车窗外车灯光带流动） |
| 4 | W2 | 5-10s | 5s | 纯文字 | 他把她翻倒在座椅上、腿缠髋、安全带松垂的传教士 |
| 5 | W3 | 0-4s | 4s | 纯文字 | 保安手电光斑扫过挡风玻璃、脚步停在车门→两人定格屏息 |
| 6 | W3 | 4-10s | 6s | 纯文字 | 外套罩头、衬衫拉好、两人滚出车门进黑暗；手电扫过空座椅；阴影里凌乱的她（英雄镜头） |

---

## Workflow 1: 停车场上车 → 后排（0-10s）

> **场景**：夜间停车场（一排排车、深色轿车车头灯亮、光池）
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s），全部纯文字动作

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark jacket. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic night parking lot scene, featuring a realistic young woman (face from <Subject 1>) in a white shirt with an unbuttoned top and a dark skirt, and a man whose face is never visible (<Subject 2>). [Shot 1] is a medium exterior shot: the woman slides from the front passenger seat into the back seat of a dark sedan with its headlights on. [Shot 2] cuts inside the car: she kneels between the man's legs in the dark back seat, her hands moving into his waistband, while he straddles her. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark jacket is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is an empty parking lot at night with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] An empty parking lot at night: rows of parked cars, a dark sedan with its headlights on, the pale pool of light on the asphalt. The woman (face and hair from <Subject 1>) in her white shirt with the top unbuttoned and her dark skirt slides from the front passenger seat into the back seat. The man follows her in, turning so that his back is to the camera, his face never visible. The camera is static throughout [Shot 1], outside the car at a medium distance, at a level angle.

[Shot 2] At 00:06.000, inside the dark back seat, lit by the faint streetlight through the window: the woman kneels between the man's legs, her dark skirt hiked up over her hips, her hands moving into his waistband; he straddles her, his face staying out of frame. The camera is static throughout [Shot 2], inside the car at a close range, through the window.

overall_soundscape:
A night parking-lot ambience continues throughout the video: a distant traffic hum, the low idle of the car's engine, and the faint buzz of the car's interior light. In [Shot 1], the leather seat creaking as she slides into the back, the car door closing, and her quickened breathing. In [Shot 2], the soft creak of the seat, the rustle of fabric, and her low moans over the parking-lot hum. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 后排女上位 → 翻倒传教士（10-20s）

> **场景**：轿车后排座舱（窗外停车场灯光带、车灯光带流动）
> **分镜**：2 个 — Shot 1（5s，女上位坐姿前倾 深度图）→ Shot 2（5s，纯文字）

- 女上位坐姿前倾（Picture 2，magapixels = 0.4）
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
> ⚠️ 历史动作卡「女上位-坐姿前倾_正面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark jacket. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the cowgirl seated forward-lean body layout (kneeling, leaning forward, hands braced in front) and the frontal camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic car interior scene at night, featuring a realistic young woman (face from <Subject 1>) and a man whose face is never visible (<Subject 2>). [Shot 1] is a frontal close shot through the windshield: the woman kneels in the back seat in a cowgirl forward-lean position, braced on the seat back, riding the man who thrusts up into her from behind, the window reflecting streaking headlights. [Shot 2] cuts to a low side view inside the car: the man flips the woman over onto the back seat and thrusts into her from above. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark jacket is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 1]): partially_preserved - the cowgirl seated forward-lean body layout and the frontal camera angle are retained for [Shot 1].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is the dark back seat of a sedan at night, lit by faint streetlight and passing car lights through the window, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The dark back seat of the sedan at night. Following the posture of <Subject 3>, the woman (face and hair from <Subject 1>) is kneeling in the back seat in a cowgirl forward-lean position, leaning forward with her upper body, her head lowered facing downwards and then raised facing the camera, her chest tilted downwards, her white shirt gaping open. Her legs are spread and she is kneeling. The man is behind the woman, his upper body slightly pressing down on her, his head out of frame. The man's penis extends from behind the woman and has already entered her vagina. The woman's hands are braced on the seat back and she controls the thrusting rhythm by moving her hips back and forth, the window reflecting the streaking headlights of passing cars. The camera stays static throughout [Shot 1], shooting from a frontal angle at a close range.

[Shot 2] At 00:05.000, the camera cuts to a low side view inside the car. The man flips the woman over onto the back seat; she lies on her back on the leather seat, her dark skirt hiked up over her waist, her legs hooked around his hips, the seatbelt across her chest dangling loose. The man thrusts into her from above, his face never visible, his lower body filling the frame. The window reflects the streaking headlights of passing cars. The camera stays static throughout [Shot 2].

overall_soundscape:
The car interior ambience continues throughout the video: the low engine idle, the faint hum of the cabin, and the streetlight through the window. In [Shot 1], the soft thuds of her hands on the seat back, wet thrusting sounds, and her moans growing louder before she bites back a cry. In [Shot 2], the leather seat creaking, the dangle of the seatbelt, wet thrusting sounds, and her muffled moans; outside, a car's tires hiss past on the wet asphalt. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 保安手电逼近 → 溜进黑暗（20-30s）

> **场景**：同车（后排座舱）→ 停车场车缝阴影
> **分镜**：2 个 — Shot 1（4s，纯文字）→ Shot 2（6s，纯文字，英雄镜头收尾）

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark jacket. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic car interior and parking lot scene at night, featuring a realistic young woman (face from <Subject 1>) and a man whose face is never visible (<Subject 2>). [Shot 1] is a close interior shot: a security guard's flashlight beam sweeps across the windshield, a circle of light crossing the woman's face, and heavy footsteps stop at the car door; the two freeze mid-thrust. [Shot 2] cuts to the parking lot: the man drapes his dark jacket over the woman's head and shoulders and the two roll out of the open rear door into the dark row of cars; the flashlight sweeps the empty back seat, and the woman stands in the shadow between two parked cars. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark jacket is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is the back seat of a sedan and the dark rows of an empty parking lot at night, with a horizontal 16:9 frame. The man's face is never visible in any shot, and the security guard never speaks or shows a clear face.

[Shot 1] The back seat of the sedan at night. A security guard's flashlight beam sweeps across the windshield from outside, a circle of light crossing the woman's (face and hair from <Subject 1>) face; heavy footsteps stop at the car door. The man and the woman freeze mid-thrust, their breathing held. The camera is static throughout [Shot 1], inside the car at a close range.

[Shot 2] At 00:04.000, the camera cuts to the parking lot. The man pulls his dark jacket off and drapes it over the woman's head and shoulders, yanks her white shirt closed, and the two roll out of the open rear door into the dark row of cars. The guard's flashlight sweeps the back seat — empty. In the shadow between two parked cars, the woman stands with the jacket around her shoulders, breathing hard, her white shirt twisted and half-open, her dark skirt askew. The camera stays static throughout [Shot 2], at a medium distance, at a level angle.

overall_soundscape:
The parking-lot ambience continues throughout the video: a distant traffic hum and the low engine idle. In [Shot 1], the flashlight click, the beam crossing the windshield, and heavy footsteps stopping at the car door; both of them hold their breath. In [Shot 2], the rustle of the jacket draping over her, the door creaking open, their soft footsteps on the asphalt, the flashlight beam sweeping the empty back seat, and the faint hum of the lot falling over the woman breathing hard in the shadow. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  - W1：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
  - W2：Yasal 脸 → `<Picture 1>`；旧动作卡「女上位-坐姿前倾_正面_横图」（当前 `ref/pose/pose.json` 无同名条目） → `<Picture 2>`
  - W3：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W2 女上位前倾 = 0.4；其余未标注用默认值
- **跨工作流一致性**：`<Subject 1>`（脸）与 `<Subject 2>`（无脸男）的锁定文字在三个提示词中保持完全一致；车（深色轿车+车头灯+后排座舱）在 W1-W3 保持一致；她的服装状态按剧情递进（完整→领口敞开→凌乱+外套罩身）
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）
- **声音设计**：全程环境声（停车场车声/引擎怠速/车内嗡鸣）+ 她的呻吟/惊呼；保安**全程无词**（手电咔哒声、脚步、呼吸，不引入说话人 ID、不用 `<d>`）；无音乐
- **写实约束**：不使用任何动漫场景参考图（场景纯文字），保安面部被帽檐/逆光挡住或只出现在车窗外，避免生成多余清晰人脸

## 成片

![](assets/Case7/file-20260901025537536.mp4)
## 素材

![](assets/Case7/file-20260901025541056.mp4)

![](assets/Case7/file-20260901025541088.mp4)

![](assets/Case7/file-20260901025541159.mp4)
