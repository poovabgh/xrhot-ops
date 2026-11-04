# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-04 08:13 PST（例行 00:00 BJT 2026-11-05）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 04 Nov 2026 16:13:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 04 Nov 2026 16:13:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-05 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、RokidGlobal、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100→100（+2）：** htcvive VIVE Eagle Bucharest Fashion Week 2118007232801526009 / RokidGlobal Rokid Glasses afternoon music 2117995284945158270；丢掉最旧 2 条（2112930484812714237、2112921856239890773）。MetaVR_Official / BigscreenVR / XREAL_Global / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+1）：** Dilmerv Meta VR CLI Agent Skills tip 2118003054620389681；丢掉最旧 1 条（2114514870431346908）。nathie `exclude` 后 result_count 0。Dilmerv VR evolution motivation 2117961345047908442 drop；SadlyItsBradley political Missouri joke 2117853126585684469 drop。
- top-6 guid 抽查均在（含新 htcvive Eagle / Rokid Glasses / Dilmerv Agent Skills / Dilmerv Cubiques / Dilmerv Start Competition / Bradley FrameOS）。
- 上一有变更档：2026-11-04 20:00 BJT official 不变、media-kol +1 Dilmerv Cubiques。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-05 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
