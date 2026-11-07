# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-07 00:08 PST（例行 16:00 BJT 2026-11-07）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 99 | Sat, 07 Nov 2026 04:09:48 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 07 Nov 2026 08:08:09 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-07 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVRDevs、htcvive、BigscreenVR、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。无 most_recent < watermark，未做删帖核对。
- **official 99→99（+0/−0）：** 无新原创入库。MetaVRDevs / htcvive / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+3）：** SadlyItsBradley SteamVR chroma key / Room View on Vision Pro / PCXR Steam VR Link quote 2118956794714411412；Dilmerv Meta VR Glasses Unity e-book / Quad Views / foveated quote 2118926207756714255；Dilmerv MKBHD Meta VR Glasses daily quote 2118919611269939252。丢掉最旧 3 条。Dilmerv Parsec/KVM 2118944109645688986 非 XR 丢弃；nathie Meta glasses 续帖 2118827795132580291 skip（已在 2118827306160377980 合并）；SadlyItsBradley Circa 2023 续帖 2118911619254329733 skip（已在 2118907013640184068 合并）。
- top-6 guid 抽查均在（含新 Bradley SteamVR Room View / Dilmerv Unity e-book / Dilmerv MKBHD；旧 Bradley Valve quote / Steam Frame / Dilmerv Hand Skate 仍在）。
- 上一有变更档：2026-11-07 12:00 BJT media-kol Bradley Steam Frame×2 + Dilmerv Hand Skate；official −1 htcvive 删帖。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-07 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
