# Case12 — Yasal 30 秒横屏婚礼夜宴会布景间（写实 · 3 × 10s 工作流）

> **角色**：Yasal —— 写实真人风格：黑直短发（齐刘海、透明发夹）、灰蓝眼睛、白纱婚纱+头纱（新娘装扮）
> **总时长**：30 秒 = 3 个 workflow × 10 秒（24fps，1280×720，16:9 横屏）
> **分镜**：6 个镜头，每个 4-6 秒（6+4 / 5+5 / 4+6）
> **场景**：宴会厅后台布景间（叠椅、铺桌布宴会桌、花拱门、门外闷响的宴会音乐）（纯文字描述，不使用场景参考图，保持写实）
> **剧情**：新娘从喧闹宴会溜进后台布景间→无脸新郎（黑西装）跟入关门→扯头纱拥吻→花拱门前传教士（白纱层叠掀起）→压上宴会桌→女伴女声"找新娘"逼近+门把晃动→头纱罩回、躲进道具阴影（女伴剪影探头离开收尾）
> **动作**：纯文字 5 镜 + pose 深度图 1 镜（传教士侧面）

## 全局约束（三个工作流共同遵守）

- **画风锁定**：电影级写实真人风格（真实皮肤质感、自然胶片颗粒、自然光、浅景深、35mm 手持感），**不是动漫、不是卡通**——每条提示词 detailed_description 开头声明
- 脸部与发型完全由 `<Picture 1>` 锁定，提示词不额外描述面部/发饰细节
- Yasal 服装：白纱婚纱（拖地长摆）+ 头纱；被脱后裸体（白纱层层堆在腰侧）
- 男性=无脸新郎（黑西装+领带），**全程不露脸**（出画/阴影/背对镜头）、**全片无男性声音**（只有衣物声、椅子声、宴会闷响等物理声）
- 女伴=虚化剪影、面部不清晰、只有**模糊不可辨的女声**（不引入说话人 ID、不用 `<d>`）；避免生成多余清晰人脸
- 她的声音：压低的呻吟、喘息、轻唤（女性声音，允许）
- 宴会音乐=**画内声音**（门外闷响，写在 detailed_description/overall_soundscape）
- 场景纯文字描述（写实风格不使用动漫场景参考图）；pose 深度图只用于有图的分镜
- 无配乐（`non_diegetic_music: N/A`）

## 固定参考图（Picture 1，三个工作流完全相同）

- Yasal 面部参考（Picture 1）
![250](../../../../ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png)

## 分镜总表（6 shots）

| # | 工作流 | 时间（全片） | 时长 | 动作来源 | 内容（剧情节拍） |
|---|--------|--------------|------|----------|------------------|
| 1 | W1 | 0-6s | 6s | 纯文字 | 布景间：白纱拖地溜进来，门外宴会音乐闷响，无脸新郎跟入关门 |
| 2 | W1 | 6-10s | 4s | 纯文字 | 扯下头纱、西装外套推落、拥吻、手攥礼服腰 |
| 3 | W2 | 0-5s | 5s | 传教士式性交-侧面_横图 深度图（0.4） | 花拱门前传教士，白纱裙摆整层掀起（俯侧机位） |
| 4 | W2 | 5-10s | 5s | 纯文字 | 压上铺桌布宴会桌，层层白纱堆腰侧、桌布垂落 |
| 5 | W3 | 0-4s | 4s | 纯文字 | 女伴女声由远及近+门把晃动→骤停、头纱罩回、躲进叠椅阴影 |
| 6 | W3 | 4-10s | 6s | 纯文字 | 门开、女伴剪影（持酒杯）探头一圈离开；道具箱缝隙里她的眼睛+头纱尖（英雄镜头，宴会掌声响起） |

---

## Workflow 1: 溜进布景间 → 扯头纱拥吻（0-10s）

> **场景**：宴会厅后台布景间（叠椅、铺桌布宴会桌、花拱门、门外闷响的宴会音乐）
> **分镜**：2 个 — Shot 1（6s）→ Shot 2（4s），全部纯文字动作

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a black suit and tie. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic wedding reception backstage scene at night, featuring a realistic young bride (face from <Subject 1>) in a white wedding dress with a long train and a veil, and a faceless groom (<Subject 2>) in a black suit. [Shot 1] is a medium shot: the bride slips into the backstage prop room, her train dragging, the muffled banquet music dropping as the groom shuts the door. [Shot 2] cuts closer: he pulls the veil off her head and her hands push his suit jacket off his shoulders, and the two of them embrace. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the groom in the black suit is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a banquet hall backstage prop room at night with stacked banquet chairs, a draped table, a floral arch, and muffled banquet music from the hall beyond the door, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The backstage prop room: stacks of banquet chairs, a table draped with a cloth, a floral arch, and the muffled sound of a string quartet and applause drifting in through the open door. The bride (face and hair from <Subject 1>) slips in in her white wedding dress, the long train dragging on the floor, her veil half on. The man in the black suit follows her in and shuts the door, and the music cuts lower. The camera is static throughout [Shot 1], at a medium distance, at a level angle.

[Shot 2] At 00:06.000, a closer view. He pulls the veil off the bride's head and lets it fall behind her; her hands push the black suit jacket off his shoulders, and the two of them embrace, his hand gripping the waist of the white dress, her head tipping back. The camera is static throughout [Shot 2], at a medium close range.

overall_soundscape:
A muffled banquet ambience continues throughout the video: the muffled string quartet through the door, the distant applause of the hall, and the hum of the corridor speakers. In [Shot 1], the swish of the wedding dress train dragging on the floor, the door closing, and the music cutting lower. In [Shot 2], the rustle of the veil falling, the rustle of the suit jacket, the creak of the embrace, and her muffled, breathy moan. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 2: 花拱门前传教士 → 压上宴会桌（10-20s）

> **场景**：同一布景间（花拱门/道具箱前 → 铺桌布宴会桌）
> **分镜**：2 个 — Shot 1（5s，传教士侧面 深度图）→ Shot 2（5s，纯文字）

- 传教士侧面俯视（Picture 2，magapixels = 0.4 时才正确实现）
> ⚠️ 历史动作卡「传教士式性交-侧面_横图」当前不在 `ref/pose/pose.json`；此处不自动替换，请提交前重新选择当前动作卡。
##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a black suit and tie. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.
<Subject 3> is the sex position and camera angle reference, defined by <Picture 2>. Use this depth map to lock the missionary side body layout (woman on the ground with her back against the floral arch, man above her) and the fixed overhead side camera angle for [Shot 1]. Do not inherit the character's face, hair, clothing, or scene from <Picture 2>.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic wedding reception backstage scene at night, featuring a realistic young bride (face from <Subject 1>) and a faceless groom (<Subject 2>). [Shot 1] is a fixed overhead side view: the bride lies on the ground with her back against the floral arch, her layers of white dress pulled up over her hips, the man above her shows only his lower body and part of his arms, his hand grasping her wrist while his penis continuously inserts into her vagina. [Shot 2] cuts to a low side view: he lifts her onto the draped banquet table, the layers of the white dress pooled around her waist, and he thrusts into her from above. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the groom in the black suit is retained in both shots, with his face never visible.
<Subject 3> (appears in [Shot 1]): partially_preserved - the missionary side body layout and the fixed overhead side camera angle are retained for [Shot 1].

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a banquet hall backstage prop room at night with stacked banquet chairs, a draped table, and a floral arch, with a horizontal 16:9 frame. The man's face is never visible in any shot.

[Shot 1] The floral arch side of the prop room. Following the posture of <Subject 3>, the bride (face and hair from <Subject 1>) is lying on the ground in a missionary position, her back against the floral arch, and her entire body can be seen in the picture. Her white wedding dress is pulled up over her hips, its layers bunched around her waist. The man is positioned above her, only his lower body and part of his arms visible, his head out of frame. The man's hand is grasping the woman's wrist, and his penis is continuously inserting into her vagina. His lower body is constantly slapping the woman's buttocks. Due to the intense impact, the woman's body trembles slightly, her chest rises and falls violently, and from time to time she slightly opens her mouth and lets out a stifled sound, then clamps her jaw to keep the noise down. The picture is shot from a fixed overhead perspective to fully present the scene. The camera stays static throughout [Shot 1].

[Shot 2] At 00:05.000, the camera cuts to a low side view. The man lifts the bride onto the draped banquet table; she lies on her back on the table, her layers of white dress pooled around her waist, the tablecloth draping down at both sides. The man leans over her and thrusts into her from above, his face never visible, his lower body filling the frame, the floral arch swaying faintly behind them. The camera stays static throughout [Shot 2].

overall_soundscape:
The muffled banquet ambience continues throughout the video: the muffled string quartet and the distant applause of the hall. In [Shot 1], the swish of the wedding dress layers, wet thrusting sounds, his lower body slapping her buttocks, and her stifled moans pressed low. In [Shot 2], the creak and strain of the tablecloth, the muffled thud of the table, wet thrusting sounds, and her muffled cries. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## Workflow 3: 女伴逼近 → 道具阴影藏身（20-30s）

> **场景**：同一布景间（宴会桌/叠椅道具阴影）
> **分镜**：2 个 — Shot 1（4s，纯文字）→ Shot 2（6s，纯文字，英雄镜头收尾）

##### English Prompt

```txt
subject_definitions:
<Subject 1> is the woman's face and hair, defined by <Picture 1>. Preserve her face and hair exactly as in <Picture 1> throughout the video; do not inherit the background, clothing, or body pose from it.
<Subject 2> is the man, defined by text only (no reference image): a tall adult male in a black suit and tie. His face is never visible in any shot — he stays out of frame, in shadow, or with his back to the camera — and his voice is never heard. Preserve his body and clothing consistency throughout the video.

summary:
[reference generation] The target video is a 10-second horizontal (16:9) two-shot cinematic photorealistic wedding reception backstage scene at night, featuring a realistic young bride (face from <Subject 1>) and a faceless groom (<Subject 2>). [Shot 1] is a medium side shot: a muffled, indistinct female voice comes closer outside the door and the door handle rattles; the two freeze, and the groom drapes the veil back over the bride's head as they slide into the shadow behind the stacked chairs. [Shot 2] cuts to the prop shadow: the door opens, a silhouetted bridesmaid holding a glass looks around the prop room and leaves; the bride and groom crouch in the gap between the stacked chairs, only her eyes and the tip of the veil visible as the banquet music swells and applause erupts from the hall. No male voice appears anywhere in the video.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2]): fully_preserved - the woman's face and hair from <Picture 1> are retained in both shots.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the groom in the black suit is retained in both shots, with his face never visible.

detailed_description:
The target video is a cinematic photorealistic live-action style scene: realistic human skin texture, natural film grain, naturalistic lighting, shallow depth of field, and a 35mm handheld camera feel — not anime, not cartoon. The setting is a banquet hall backstage prop room at night with stacked banquet chairs, a draped table, and a floral arch, with a horizontal 16:9 frame. The man's face is never visible in any shot, and the bridesmaid is only a silhouette with no clear face.

[Shot 1] The prop room, the draped table, the stacks of chairs. A muffled, indistinct female voice comes closer outside the door, and the door handle rattles. The groom and the bride (face and hair from <Subject 1>) freeze; he drapes the veil back over her head, and the two of them slide into the shadow behind the stacked chairs, her white dress pooled around her waist. The camera is static throughout [Shot 1], at a medium side angle.

[Shot 2] At 00:04.000, the door opens. The bridesmaid, a silhouette with no clear face, holding a glass in her hand, looks around the prop room, then leaves. The groom and the bride crouch in the gap between the stacked chairs and the prop crates; only her eyes and the tip of the veil are visible in the shadow. The muffled string quartet swells, and applause erupts from the hall. The camera stays static throughout [Shot 2], at a close range, at a level angle.

overall_soundscape:
The banquet ambience continues throughout the video: the muffled string quartet and the distant applause of the hall. In [Shot 1], the muffled, indistinct female voice outside the door, the rattle of the door handle, the rustle of the veil draping back over her head, and the two of them sliding into the shadow. In [Shot 2], the door creaking open, the faint clink of the glass, the footsteps leaving, the muffled music swelling, and the applause of the hall as the two of them hold their breath in the shadow. No male voice is audible at any point in the video.

non_diegetic_music:
N/A
```

---

## 提交说明

- **画布/帧**：1280×720（16:9，宽高为 32 的倍数），24fps；10 秒 ≈ 243 帧（17n+5 对齐）
- **每个工作流的 Load Image 顺序**（必须与提示词标签一致）：
  - W1：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
  - W2：Yasal 脸 → `<Picture 1>`；旧动作卡「传教士式性交-侧面_横图」（当前 `ref/pose/pose.json` 无同名条目） → `<Picture 2>`
  - W3：`ref/character/Yasal/exec-10bf9109-04b1-4aba-810b-6f89b3793cc9.png` → `<Picture 1>`（1 张图，两镜均为纯文字动作）
- **magapixels**（沿用历史工作流参数备注；当前 `ref/pose/pose.json` 不记录此字段）：W2 传教士侧面 = 0.4；其余未标注用默认值
- **跨工作流一致性**：`<Subject 1>`（脸）与 `<Subject 2>`（无脸新郎）的锁定文字在三个提示词中保持完全一致；布景间（叠椅+铺桌布宴会桌+花拱门+门外宴会闷响）在 W1-W3 保持一致；她的服装状态按剧情递进（完整白纱+头纱→头纱扯下→白纱堆腰侧+头纱罩回）
- **剪辑衔接**：三个 10 秒成片按 W1→W2→W3 顺序硬切拼接；每段内部切点（00:06.000 / 00:05.000 / 00:04.000）
- **声音设计**：宴会弦乐+掌声（画内、门外闷响）+ 白纱拖地声/椅子吱呀/头纱拂动；女伴=模糊不可辨的女声（不引入说话人 ID、不用 `<d>`）；无音乐
- **写实约束**：不使用任何动漫场景参考图（场景纯文字），女伴/宴会人员=虚化剪影、面部不清晰，避免生成多余清晰人脸
