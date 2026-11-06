# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-06 08:12 PST（例行 00:00 BJT 2026-11-07）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 06 Nov 2026 16:12:06 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 06 Nov 2026 12:08:59 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-07 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、XREAL_Global、RokidGlobal、VRChat、BeatSaber、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100→100（+3）：** BeatSaber OST 9 Nov12 2118735513335087481；RokidGlobal AI Glasses Style review 2118720067617583153；XREAL_Global AURA HoloMedicine surgical 2118706620293120077；丢掉最旧 3 条。MetaVR_Official / BigscreenVR `exclude` 后 result_count 0。VRChat 2118457404153020801 为 Dev Update 串帖续帖（缩略图），已在 2118457400784998664 合并，跳过。
- **media-kol 100 不变：** Dilmerv 4 条动机/闲聊 drop（含此前已 drop 的 2118653374904078474 / 2118619396365000977；另 2118716324658520069 早起例行、2118694916117205195 泛 XR 励志）；SadlyItsBradley `exclude` 后 result_count 0（最新为 RT）；ARealityEvent / nathie 等于 watermark。
- top-6 guid 抽查均在（含新 BeatSaber OST9 / Rokid Style / XREAL HoloMedicine；旧 XREAL Plynk / Open Brush / Dilmerv Hand Skate 等仍在）。
- 上一有变更档：2026-11-06 20:00 BJT XREAL Plynk + ARealityEvent Weekly Spatial。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-07 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
