# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-09 20:06 PST（例行 12:00 BJT 2026-11-10）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 10 Nov 2026 00:15:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 10 Nov 2026 04:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-10 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：VRChat、RokidGlobal、BigscreenVR、htcvive、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVRDevs、XREAL_Global、PICOXR、MetaVR_Official、BeatSaber、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在上一轮合并，skip。RokidGlobal / BigscreenVR / htcvive `exclude` 后 result_count 0。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv Hand Skate environmental objects 2119988459481837926；Dilmerv HandSkate stretch effects 2119959907835290104。丢掉最旧 2 条：nathie smart glasses silent speech 2116592500471214115、Dilmerv Depth API 2116568461962862993。SadlyItsBradley most_recent 2119881196855504924、nathie most_recent 2119909376681210066 `exclude` 后 result_count 0（回复/转发）。
- top-6 guid 抽查均在（新 media-kol Dilmerv environmental objects 2119988459481837926 / Dilmerv stretch effects 2119959907835290104；official 仍为 MetaVRDevs prototype 2119909497934356661 / VRChat New Year's 2119893528847233479 / XREAL Glossa 2119868911281754378 / MetaVRDevs reviews 2119866328047890651 / MetaVRDevs competition 2119856412255981927 / XREAL Idle Hero Drummer 2119838644865302803）。
- 上一有变更档：2026-11-10 08:00 BJT official +6 / media-kol +4。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-10 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
