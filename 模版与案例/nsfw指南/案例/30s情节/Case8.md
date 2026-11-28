# Case8 — Yasal 30 秒横屏漫展后台偷情（写实 · 3 × 10s 工作流）

> **角色**：Yasal —— 写实真人风格：黑直短发（齐刘海、透明发夹）、灰蓝眼睛、白衬衫+深色裙+平底鞋，胸前挂 "STAFF" 工牌（漫展工作人员装扮）
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个镜头，每个 4-6 秒（6+4 / 5+5 / 4+6）
> **场景**：漫展主会场后台储物间（纸箱堆、气泡膜、门缝透光条）（纯文字描述，不使用场景参考图，保持写实）
> **剧情**：喧嚣的漫展后台，她被无脸男从门外拽进储物间→按在纸箱堆上脱衣→窄道女上位手捂嘴→翻倒在气泡膜上传教士→人影贴上门缝骤停→无声高潮（咬他手臂哭不出声）→门把手将转未转定格
> **动作**：纯文字 5 镜 + pose 深度图 1 镜（猫娘女上位-手捂嘴_实拍）

## 全局约束（三个工作流共同遵守）

- **画风锁定**：电影级写实真人风格（真实皮肤质感、自然胶片颗粒、自然光、浅景深、35mm 手持感），**不是动漫、不是卡通**——每条提示词 detailed_description 开头声明
- 脸部与发型完全由 `<Picture 1>` 锁定，提示词不额外描述面部/发饰细节
- Yasal 服装：白衬衫（领口解开）+ 深色裙 + 平底鞋 + 胸前 "STAFF" 工牌（挂绳）；脱衣后为裸体
- 男性**全程不露脸**（出画/阴影/背对镜头）、**全片无男性声音**（只有脚步声、纸箱声、衣物声等物理声）
- 门外的人=虚化剪影+脚步声（无词、面部不清晰）；避免生成多余清晰人脸
- 她的声音：全程**捂嘴压住**——闷哼、无声啜泣（女性声音，允许）
- 画内文字："STAFF" 工牌文字按原文保留
- 场景纯文字描述（写实风格不使用动漫场景参考图）；pose 深度图只用于有图的分镜
- 无配乐（门外场馆的闷响 EDM 是**画内声音**，写在 detailed_description/overall_soundscape；`non_diegetic_music: N/A`）

## 固定参考图（Picture 1，三个工作流完全相同）

- Yasal 面部参考（Picture 1）
![250](../../../../ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png)

## 分镜总表（6 shots）

| # | 工作流 | 时间（全片） | 时长 | 动作来源 | 内容（剧情节拍） |
|---|--------|--------------|------|----------|------------------|
| 1 | W1 | 0-6s | 6s | 纯文字 | 储物间：她喘着气靠纸箱，"STAFF" 工牌晃荡，无脸男从门外拽她进来、门砰然合上 |
| 2 | W1 | 6-10s | 4s | 纯文字 | 被按在纸箱堆上快速脱衣，她一手扶门防弹开 |
| 3 | W2 | 0-5s | 5s | 猫娘女上位-手捂嘴_竖图_实拍 深度图 | 纸箱窄道女上位前倾、手捂自己嘴，门外脚步经过→声音归零 |
| 4 | W2 | 5-10s | 5s | 纯文字 | 被翻倒在气泡膜/纸箱上，传教士压入 |
| 5 | W3 | 0-4s | 4s | 纯文字 | 剪影贴上门缝光条→两人骤停屏息→人走过、光条回来 |
| 6 | W3 | 4-10s | 6s | 纯文字 | 无声高潮（咬他手臂哭不出声）→拔出→门把手开始转动→定格（英雄镜头：门缝光条里的剪影） |

---

## Workflow 1: 被拽进储物间 → 纸箱堆脱衣（0-10s）

> **场景**：漫展后台储物间（堆满纸箱、气泡膜、门缝一道光条、门外闷响的场馆）
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s），全部纯文字动作

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark t-shirt and jeans. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic scene inside a convention backstage storage room, featuring a realistic young woman (face from <Subject 1>) in a white shirt, dark skirt, and a "STAFF" badge on a lanyard, and a man whose face is never visible (<Subject 2>). [Shot 1] is a medium shot: the woman leans against a stack of cardboard boxes, breathing hard, when the man yanks her in through the door from the bright hall and the door slams shut, cutting off the light strip on the floor. [Shot 2] cuts to the same room: he pins her against the boxes and unfastens her shirt while she holds the door edge with one hand. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark t-shirt is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a narrow convention backstage storage room stacked with cardboard boxes and bubble wrap, a strip of bright light from the door gap, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The narrow storage room: stacks of cardboard boxes, rolls of bubble wrap, and a strip of bright light from the open door gap on the floor. The woman (face and hair from <Subject 1>) leans against a stack of boxes, breathing hard, her white shirt damp, the "STAFF" badge on her lanyard swinging. A hand in a dark sleeve — the man's — closes around her arm from the doorway and yanks her in; the door slams shut behind them, and the light strip on the floor vanishes into darkness. The camera is static throughout [Shot 1], at a medium distance, at a level angle.

[Shot 2] At 00:06.000, the same storage room. The man pins the woman against the cardboard boxes, his hands quickly unfastening the white shirt at the collar; she holds the edge of the door with one hand to keep it from swinging open, her eyes darting at the gap. The camera is static throughout [Shot 2], at a medium side angle.

overall_soundscape:
A muffled festival ambience continues throughout the video: a heavy muffled bass thump from the main-hall speakers, the roar of a crowd, and muffled cheering through the storage door. In [Shot 1], her heavy breathing, the creak of the cardboard boxes, and the door slamming shut, cutting off the light strip. In [Shot 2], the rustle of fabric as the shirt is unfastened, her muffled gasps, and her fingers scraping the door edge. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 纸箱窄道手捂嘴 → 气泡膜传教士（10-20s）

> **场景**：同一储物间（纸箱窄道 → 气泡膜地面）
> **分镜**：2 个 — Shot 1（5s，猫娘女上位-手捂嘴 实拍深度图）→ Shot 2（5s，纯文字）

- 女上位手捂嘴（Picture 2，实拍）
![200](../../../../ref/pose/color/猫娘女上位-手捂嘴_竖图_实拍.png)
![200](../../../../ref/pose/depth/猫娘女上位-手捂嘴_竖图_实拍_depth.png)

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark t-shirt and jeans. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the cowgirl forward-lean body layout (kneeling, leaning forward, one hand over the mouth) and the frontal camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic scene inside a convention backstage storage room, featuring a realistic young woman (face from <Subject 1>) and a man whose face is never visible (<Subject 2>). [Shot 1] is a frontal shot: the woman kneels in the narrow aisle between cardboard boxes in a cowgirl forward-lean position, pressing her palm over her own mouth to muffle her voice while the man thrusts up into her from behind. [Shot 2] cuts to a low side view: she is flipped over onto the bubble wrap on the floor and the man thrusts into her from above. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark t-shirt is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 1]): partially_preserved - the cowgirl forward-lean body layout with the hand over the mouth and the frontal camera angle are retained for [Shot 1].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a narrow convention backstage storage room stacked with cardboard boxes and bubble wrap, a strip of bright light from the door gap, and a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The narrow aisle between two stacks of cardboard boxes. Following the posture of <Subject 3>, the woman (face and hair from <Subject 1>) is kneeling on the floor in a cowgirl forward-lean position, leaning forward with her upper body, her head lowered facing downwards and then raised facing the camera, her chest tilted downwards, her white shirt bunched at her waist. Her legs are spread and she is kneeling, her bare chest and bare thighs exposed. The man is behind the woman, his upper body slightly pressing down on her, his head out of frame. The man's penis extends from behind the woman and has already entered her vagina. The woman presses her palm over her own mouth to muffle her voice and controls the thrusting rhythm by moving her hips back and forth. The camera stays static throughout [Shot 1], shooting from a frontal angle at a close range.

[Shot 2] At 00:05.000, the camera cuts to a low side view. The man flips the woman over onto the bubble wrap on the floor; she lies on her back, her dark skirt hiked up over her waist, her knees drawn up, the cardboard boxes creaking around them. The man straddles her hips and thrusts into her from above, his face never visible, the strip of light from the door gap flickering over them. The camera stays static throughout [Shot 2].

overall_soundscape:
The muffled festival ambience continues throughout the video: the heavy bass thump and the crowd roar through the door. In [Shot 1], the soft creak of the boxes, the thud of her knees on the floor, wet thrusting sounds, and her muffled moans pressed into her own palm; heavy footsteps pass just outside the door and her sound drops to nothing. In [Shot 2], the bubble wrap crinkling, the boxes groaning, wet thrusting sounds, and her stifled cries. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 门缝剪影骤停 → 无声高潮·门把手定格（20-30s）

> **场景**：同一储物间（气泡膜地面、门缝光条）
> **分镜**：2 个 — Shot 1（4s，纯文字）→ Shot 2（6s，纯文字，英雄镜头收尾）

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a dark t-shirt and jeans. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic scene inside a convention backstage storage room, featuring a realistic young woman (face from <Subject 1>) and a man whose face is never visible (<Subject 2>). [Shot 1] is a medium side shot: a silhouette crosses the door gap, the light strip swallowed by a moving shadow; the two freeze mid-thrust until the person passes and the light returns. [Shot 2] cuts to a close view: the woman has a silent climax, biting the man's forearm to keep from crying out; he pulls out, and the door handle begins to turn as the two freeze, shown in silhouette through the light strip. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the man in the dark t-shirt is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a narrow convention backstage storage room stacked with cardboard boxes and bubble wrap, a strip of bright light from the door gap, and a horizontal 16:9 frame. The man's face is never visible in any shot, and the person at the door never shows a clear face.

[Shot 1] The storage room, the bubble wrap floor, the strip of bright light from the door gap. A silhouette crosses the door gap; the light strip is swallowed by a moving shadow. The man and the woman (face and hair from <Subject 1>) freeze mid-thrust, their breathing held, the boxes around them perfectly still. The shadow moves on, and the light strip returns. The camera is static throughout [Shot 1], at a medium side angle.

[Shot 2] At 00:04.000, the camera cuts to a close view. The woman rides the man harder, her palm flat over her own mouth, then her hand slides to his forearm and she bites down on it, a silent scream, her eyes wide with tears; the man's thrusts grow fast, and he pulls out, bracing against the boxes. The door handle begins to turn, slow and deliberate; both of them freeze. Through the light strip in the door gap, the two of them are silhouettes on the floor. The camera stays static throughout [Shot 2].

overall_soundscape:
The festival ambience continues throughout the video: the heavy bass thump and the crowd roar through the door. In [Shot 1], the thrusts stop abruptly, held breath, and muffled footsteps crossing the door gap, the light strip swallowed by a shadow. In [Shot 2], her hand biting into the man's forearm with a silent scream, wet thrusting sounds, his pullout against the boxes, the slow click of the door handle beginning to turn, and both of them freezing as the muffled bass keeps thumping. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  - W1：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
  - W2：Yasal 脸 → `<Picture 1>`；`ref/pose/depth/猫娘女上位-手捂嘴_竖图_实拍_depth.png` → `<Picture 2>`
  - W3：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
- **magapixels**：猫娘女上位-手捂嘴 无特殊标注，用默认值
- **跨工作流一致性**：`<Subject 1>`（脸）与 `<Subject 2>`（无脸男）的锁定文字在三个提示词中保持完全一致；储物间（纸箱堆+气泡膜+门缝光条）在 W1-W3 保持一致；她的服装状态按剧情递进（完整+工牌→衬衫扒至腰→凌乱）
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）
- **声音设计**：全程场馆闷响 EDM+人浪（画内声音）+ 纸箱/气泡膜物理声 + 她捂嘴的闷哼/无声啜泣；门外人=剪影+脚步（无词）；无音乐
- **画内文字**："STAFF" 工牌文字按原文保留
- **写实约束**：不使用任何动漫场景参考图（场景纯文字），门外的人/观众=虚化剪影、面部不清晰，避免生成多余清晰人脸
