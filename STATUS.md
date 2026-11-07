# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-06 20:10 PST（例行 12:00 BJT 2026-11-07）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 99 | Sat, 07 Nov 2026 04:09:48 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 07 Nov 2026 04:09:48 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-07 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVRDevs、BigscreenVR、nathie、Dilmerv、SadlyItsBradley；其余等于或低于 watermark 跳过。htcvive most_recent < watermark → 核对删帖。
- **official 100→99（+0/−1）：** 无新原创入库。MetaVRDevs / BigscreenVR `exclude` 后 result_count 0。删除已失效 htcvive VIVE Eagle DITL 2118436082706485482（API Not Found）。
- **media-kol 100→100（+3）：** SadlyItsBradley Steam Frame Beta Room View/MR/Chroma Key 2118882146219893178 / Valve 启用说明 quote 串帖（含 Circa 2023 续帖）2118907013640184068；Dilmerv Hand Skate 手势容错 2118879326447800539；丢掉最旧 3 条。nathie Meta glasses 续帖 2118827795132580291 skip（已在 2118827306160377980 合并）；ARealityEvent 等于 watermark。
- top-6 guid 抽查均在（含新 Bradley Steam Frame / Valve quote / Dilmerv Hand Skate；旧 XREAL Fishing / VRChat Ownership / MetaVR SEC 等仍在）。
- 上一有变更档：2026-11-07 08:00 BJT XREAL×3 + VRChat + MetaVR；Dilmerv×4 + nathie×2 + Bradley×2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-07 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
