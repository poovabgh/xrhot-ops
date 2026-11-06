# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-05 20:02 PST（例行 12:00 BJT 2026-11-06）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 06 Nov 2026 04:02:36 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 06 Nov 2026 04:02:36 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-06 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、XREAL_Global、VRChat、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 MetaVRDevs / PICOXR / PICOXR_Dev / htcvive / RokidGlobal / getVITURE / pimaxofficial / Play_for_dream / magicleap / BeatSaber / ARealityEvent / nathie）。
- **official 100→100（+1）：** XREAL_Global Open Brush AURA（再发视频版）2118530694037029289；丢掉最旧 1 条。MetaVR_Official / BigscreenVR `exclude` 后 result_count 0。VRChat 2118457404153020801 为 Dev Update 串帖续帖（缩略图），已在 2118457400784998664 合并，跳过。
- **media-kol 100→100（+1）：** Dilmerv hands-first table-top 串帖合并 Stickman 2118536859144052741；丢掉最旧 1 条。SadlyItsBradley `exclude` 后 result_count 0（最新为 RT）。
- top-6 guid 抽查均在（含新 XREAL Open Brush / Dilmerv table-top；旧 XREAL Demeo / VRChat Dev Update / nathie VRChat reviews / Dilmerv Sphenomenon 等仍在）。
- 上一有变更档：2026-11-06 08:00 BJT official +8；media-kol +5。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-06 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
