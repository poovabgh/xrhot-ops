# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-03 08:05 PST（例行 00:00 BJT 2026-11-04）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 03 Nov 2026 16:04:59 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 03 Nov 2026 16:04:59 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-04 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、BigscreenVR、XREAL_Global、RokidGlobal、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100→100（+2）：** XREAL_Global Europe Jumanji×1 Pro⁺ 媒体活动 2117633946124968444；RokidGlobal Creator Partner Program 2117632899730030748；丢掉最旧 2 条。MetaVR_Official / BigscreenVR / VRChat / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+1）：** nathie Google×Warby Parker/Gentle Monster 智能眼镜 2117637628967239874；丢掉最旧 1 条。SadlyItsBradley `exclude` 后 result_count 0；Dilmerv motivation 2117648723509440785 / fitness 2117640636648075510 drop；nathie 最新 2117640470687859145 为回复跳过。
- top-9 guid 抽查均在（含 getVITURE / MetaVRDevs / Rokid / XREAL / Dilmerv FOV / Bradley / nathie Quest EOF / AWE）。
- 上一有变更档：2026-11-03 20:00 BJT media-kol +1 Dilmerv FOV CLI tip（a940bc5）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-04 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
