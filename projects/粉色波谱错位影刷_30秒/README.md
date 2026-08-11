# 粉色波谱错位影刷｜30 秒横屏视频

## 成片

- 最终视频：`output/粉色波谱错位影刷_30秒_最终.mp4`
- 规格：16:9，1376×768，24 fps，30.000 秒
- 音频：网易云音乐专辑 `285739676` 中的《偏执 Pt.5 - SASIOVERLXRD x BOBBYNOPEACE Type Beat》前 30 秒

## 生成方式

- 参考图：`/Users/apple/Desktop/微信图片_20260811163716_103_80.png`
- H3 模式：Ref2VA，`audio_mode: lock_source`
- 两个 15 秒片段分别使用 `0-15秒/` 与 `15-30秒/` 下的 workflow、prompt 和输出
- 最终拼接后以原曲前 30 秒替换成片音轨，保证音乐连续
- Aigate GPU：`4090D-48G`；实例已在成片完成后释放

## 提示词与工作流

- `0-15秒/粉色波谱错位影刷_0-15秒_prompt.txt`
- `0-15秒/粉色波谱错位影刷_0-15秒_workflow_api.json`
- `15-30秒/粉色波谱错位影刷_15-30秒_prompt.txt`
- `15-30秒/粉色波谱错位影刷_15-30秒_workflow_api.json`
