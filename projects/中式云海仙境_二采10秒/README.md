# 中式云海仙境｜二采 10 秒

## 项目目标

参考抖音教程“先锁定高质量静态图、再设计运镜”的方法，制作一条原创中式云海宫殿视频。只借鉴工作流、构图和镜头语言，不复制原视频画面或音频。

## 项目规格

- 工作流：`H3 极速二采高质量图_文生视频_Ref2VA双图_16x9_10s_api.json`
- 模式：Ref2VA / Full-reference
- 时长：10 秒
- 画幅：16:9
- 帧率：24 fps
- 音频：H3 原生生成
- 镜头：单镜头、无对白、无剧情演绎
- 视觉策略：白衣旅人身份参考 + 云上海宫环境参考；缓慢背后跟拍推进，长焦压缩空间纵深

## 素材

- `01_素材/white_robe_traveler_reference.png`：旅人身份、服装和轮廓参考。
- `01_素材/sky_palace_corridor_reference.png`：云上海宫、建筑材质、云海和光线参考。
- 参考教程：[抖音视频](https://www.douyin.com/video/7672446890218179883)

## 复现

1. 将 `01_素材/` 中两张图片按顺序上传到工作流的两个 `LoadImage` 节点。
2. 提交 `中式云海仙境_二采10秒_workflow_api.json`。
3. 生成后将结果放入 `output/`，并在 `qa/` 保存 ffprobe、帧数、音轨和接触表核验资料。

## 本次生成记录

- 镜像：`comfypsV5`（华东二区个人镜像 `1141060360767930368`）
- GPU：`4090D-48G`
- AIGate 实例：`1141061428776148992`
- 任务：`3adc2ac9-3850-4ff4-a0e6-c3300eb3e02d`
- 最终成品：`output/zhongshi_sky_palace_2pass_00001-audio.mp4`
- 首轮草稿：`output/zhongshi_sky_palace_2pass_draft_00001-audio.mp4`
- 核验：最终视频 1376×768、24 fps、243 帧、10.125 秒，包含 H.264 视频和 AAC 双声道音轨；`qa/final_ffprobe.json` 为原始核验记录。
- 统一入口：`../../videoOutput/中式云海仙境_二采10秒.mp4`
