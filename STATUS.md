# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-29 21:07 PDT（例行 2026-10-30 12:00 BJT；08:00 例程失败，本轮自 00:00 watermark 补采）。

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

## 本轮：2026-10-30 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVRDevs、BigscreenVR、XREAL_Global、getVITURE、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+7）：** XREAL_Global AURA Bose audio 2115972467353170218 / AURA OST vs VST TÜV 2115897128971042888 / VRChat Spookality DJ 2115896453268742615 / getVITURE HDMI→USB-C adapter 2115864882193027520 / MetaVRDevs hands-only guide 2115856631544295764 / VRChat Treats Makeship extend 2115854632425488489 / XREAL_Global AURA 95g spatial 2115851863253746133。丢掉最旧 7 条。BigscreenVR `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+5）：** SadlyItsBradley AIVU Vision Pro export 2115980670640259525 / Dilmerv MR Halloween prototype 2115895791562940774 / nathie Spider-Man VR mod 2115879127286706573 / Dilmerv Meta VR Glasses Connect videos 2115877665555014044 / SadlyItsBradley VRChat laser-tag recreation 2115855071036543167。丢掉最旧 5 条。Dilmerv 自串回复 2115896880756625845（父帖同轮入库）丢掉；SadlyItsBradley Discord 回复 2115599868659904966（父帖 StrandXR 已在 feed）丢掉；Dilmerv most_recent 为自 RT。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-30 00:00 BJT：official +4 / media-kol +3（HEAD ecde441）；中间 08:00 BJT 例程失败未跑，本轮补采覆盖自 00:00 watermark。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-30 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
