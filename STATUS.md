# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-03 04:03 PST（例行 20:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 03 Nov 2026 12:03:11 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-03 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、XREAL_Global、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100 不变：** MetaVR_Official / BigscreenVR / XREAL_Global / VRChat / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+1）：** Dilmerv Meta VR CLI FOV sim tip 2117572758464761856；丢掉最旧 1 条（2114053357493199030）。nathie / SadlyItsBradley `exclude` 后 result_count 0；Dilmerv motivation drop（2117542439015567392）；Cubiques 串帖回复 2117480716347035823 已合入既有条目、不重复入库。
- top-9 guid 抽查均在（含 getVITURE / MetaVRDevs / Rokid / XREAL / Cubiques / Bradley / nathie / AWE）。
- 上一有变更档：同日 16:00 BJT media-kol +1 Cubiques；中间另有 411f624 去掉 LensStudioDev（名单 14/4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-04 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
