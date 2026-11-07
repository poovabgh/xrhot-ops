# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-07 08:05 PST（例行 00:00 BJT 2026-11-08）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 07 Nov 2026 16:05:24 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 07 Nov 2026 16:05:24 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-08 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：PICOXR、VRChat、MetaVRDevs、htcvive、BigscreenVR、nathie、Dilmerv；其余等于 watermark 跳过。无 most_recent < watermark，未做删帖核对。
- **official 99→100（+2/−1 cap）：** PICOXR PICO Store Wish List 2119097674494349523；VRChat Virtual Dice Party 2026 2119082451100205331。丢掉最旧 1 条 MetaVRDevs Meta VR Start Competition 2114770641459269855。MetaVRDevs / htcvive / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+3）：** Dilmerv Meta VR Glasses form factor / 100g 2119086815366029414；Dilmerv 同文另一视频独立原创 2119085860763381791；Dilmerv MKBHD Meta VR Glasses / Start Competition quote 2119080565253271975。丢掉最旧 3 条。Dilmerv Parsec/KVM 2118944109645688986 非 XR 丢弃；nathie Meta glasses 续帖 2118827795132580291 skip（已在 2118827306160377980 合并）。
- top-6 guid 抽查均在（含新 PICOXR Wish List / VRChat Dice Party / Dilmerv 100g×2 / Dilmerv MKBHD quote；旧 Bradley SteamVR Room View / Dilmerv Unity e-book 仍在）。
- 上一有变更档：2026-11-07 16:00 BJT media-kol Bradley SteamVR Room View + Dilmerv Meta VR Glasses×2。20:00 BJT 无变更未提交。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-08 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
