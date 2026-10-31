# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-30 17:06 PDT（例行 2026-10-31 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-31 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、RokidGlobal、getVITURE、VRChat、BeatSaber、nathie、Dilmerv；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+4）：** getVITURE Phantom Beast XR Glasses $599 2116263369808253157；MetaVR_Official Florida vs Georgia Immersive 180° 2116231178164560223；BeatSaber Fall Sale 2116230227739181431；RokidGlobal CES 2027 / Color quote 2116201780778586270。丢掉最旧 4 条。BigscreenVR / VRChat `exclude` 后 result_count 0（最新为回复/RT）。
- **media-kol 100→100（+4）：** Dilmerv Spider Web MR 2116315964350591037；Dilmerv Cubiques iOS→VR 2116239926434140561；nathie Meta Quest guitar / Immerrock 2116229244195926044；Dilmerv Hand Pose Baker spooky pet MR 2116227340229660770。丢掉最旧 4 条。nathie 自串回复 App: Immerrock 丢掉；Dilmerv 自串回复 hand poses 丢掉。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-31 00:00 BJT：official +2 PICOXR/RokidGlobal / media-kol +1 ARealityEvent（HEAD b2850a7）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-31 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
