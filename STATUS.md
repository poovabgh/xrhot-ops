# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-05 04:06 PST（例行 20:00 BJT 2026-11-05）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 05 Nov 2026 12:06:15 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 05 Nov 2026 12:06:15 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-05 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、XREAL_Global、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 MetaVRDevs / PICOXR / PICOXR_Dev / BigscreenVR / RokidGlobal / getVITURE / pimaxofficial / Play_for_dream / magicleap / VRChat / ARealityEvent）。
- **official 100→100（+1）：** XREAL_Global Galápagos The Last Eden on AURA / Android XR 2118267924255326283；丢掉最旧 1 条（2113364266732696033）。MetaVR_Official / htcvive / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+2）：** Dilmerv AI coding agents × VR/MR 2118289756500984279 / Dilmerv hand tracking frustration 2118259619923378372；丢掉最旧 2 条（2114714454776836443 / 2114712912635863190）。nathie 2118026204456640766 为已入订阅 SteamOS 串帖续帖（已合并）skip；最新 2118094449603739818 为回复/转发预检高于 watermark 但 `exclude` 后仅见该续帖。Dilmerv motivation keep-going 2118274645333794983 drop；Dilmerv Meta VR Glasses 串帖续 2118219233004069269（已合并进 2118219230751653981）skip；SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（含新 XREAL Galápagos / Dilmerv AI agents / Dilmerv hand tracking / Dilmerv Meta VR Glasses / Bradley Chromium / nathie SteamOS）。
- 上一有变更档：2026-11-05 16:00 BJT media-kol +1 Dilmerv Meta VR Glasses。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-06 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
