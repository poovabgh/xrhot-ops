# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-29 09:05 PDT（例行 2026-10-30 00:00 BJT）。

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

## 本轮：2026-10-30 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+4）：** PICOXR spaces promo 2115836266340037093 / RokidGlobal Glasses×Tesla Gigafactory 2115805860471726171 / VRChat Hatsune Miku Yozora 2115805711963762827 / BeatSaber fan car 2115804629468389591。丢掉最旧 4 条。BigscreenVR / XREAL_Global / getVITURE `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+3）：** Dilmerv Meta VR Glasses live session 2115821443069911406 / Meta Ray-Ban Display Explore quote 2115810577696370722 / XR devices essay 2115800080905097270。丢掉最旧 3 条。nathie `exclude` 后 result_count 0；SadlyItsBradley 仅自串 Discord 回复 2115599868659904966（父帖 StrandXR 已在 feed）丢掉；其 most_recent 其余为 RT/回复已 exclude。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-29 16:00 BJT：official +2 XREAL AURA（HEAD b3926f5）；中间 20:00 BJT 静默无提交。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-30 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
