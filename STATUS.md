# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-28 21:14 PDT（例行 2026-10-29 12:00 BJT）。

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

## 本轮：2026-10-29 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、XREAL_Global、Play_for_dream、PICOXR_Dev、MetaVRDevs、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。上一档 00:00 BJT 后、08:00 BJT 例程失败未提交，本轮一并追上。
- **official 100→100（+9）：** PICOXR_Dev time-freeze XR quote 2115634287437570110；XREAL_Global AURA apps 2115580072698462386 / ssamat quote 2115507076671914376 / What if canvas 2115496951621787701 / AURA launch 2115489213281894825；VRChat AI landing 2115542209785446488 / 2026.4.1 thread 2115512628550205783；MetaVRDevs hands-first Academy 2115494685728964795；Play_for_dream split design 2115488772582179178。丢掉最旧 9 条。BigscreenVR `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+10）：** Dilmerv Immersive Debugger float 2115636246148005981 / spooky pet MR thread 2115624302724948032 / Simulon XR-quality quote 2115611906186911782 / XREAL congrats 2115605676869431672 / FoV Simulator 2115599523791708495 / Meta VR CLI tip 2115515222660149571；SadlyItsBradley StrandXR TestFlight thread 2115599863455035570 / Valve Steam Frame 2115536547873542470 / visionOS Mac Virtual Display quote 2115514674250936756；nathie Alyx treadmill 2115511377552916534。丢掉最旧 10 条。SadlyItsBradley most_recent 为 RT/回复已 exclude。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-29 00:00 BJT：official +1；media-kol +4（HEAD e44a802）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-29 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
