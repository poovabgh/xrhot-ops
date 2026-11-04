# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-03 16:05 PST（例行 08:00 BJT 2026-11-04）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 04 Nov 2026 00:05:38 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 04 Nov 2026 00:05:38 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-04 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、XREAL_Global、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100→100（+3）：** VRChat Spookality Winners Showcase YouTube 2117754653060334010；XREAL_Global Epic Roller Coasters on AURA 2117724672020087075；XREAL_Global HoloModels Hatsune Miku on AURA 2117694188334514440；丢掉最旧 3 条。MetaVR_Official / BigscreenVR / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+6）：** Dilmerv Vector Tango Meta Store quote 2117769557595320404；Dilmerv Unite Tokyo / Meta VR Glasses hackathon 2117731139238465617；Dilmerv VR/MR games YouTube learnings 2117712194200563899；nathie AVP helium balloon weight cut 2117696562482823659；SadlyItsBradley Spatial/Immersive video editor teaser 2117690988823027712；Dilmerv VR is not dead / next-wave devices 2117651887616856389；丢掉最旧 6 条。Dilmerv motivation 2117648723509440785 / fitness 2117640636648075510 drop。
- top-9 guid 抽查均在（含 VRChat / XREAL×2 / Rokid / getVITURE / MetaVRDevs / Dilmerv Vector / nathie AVP / Bradley Spatial / 旧 nathie Google glasses）。
- 上一有变更档：2026-11-04 00:00 BJT official +2 XREAL/Rokid、media-kol +1 nathie（aeb6821）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-04 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
