# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-13 08:07 PST（例行 00:00 BJT 2026-11-14）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 13 Nov 2026 16:07:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 13 Nov 2026 16:07:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-14 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、PICOXR、htcvive、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、pimaxofficial、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（Play_for_dream、MetaVRDevs、magicleap、VRChat、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+3/−3 cap）：** PICOXR A new game, two ways to begin 2121272033539449042；XREAL_Global XREAL × Jumanji: Open World prize draw 2121257606937211380；RokidGlobal WebSummit 2026 AI glasses 2121256781322305736。丢掉最旧 3 条：XREAL_Global Meet XREAL 1 Pro+ 2116119650618736697 / pimaxofficial Your questions, answered 2116041443626131539 / XREAL_Global Immersive visuals deserve sound to match 2115972467353170218。MetaVR_Official 2120973071490453795 为已入库 2120947398851912120（Winter’s coming）的续帖，未改已发出条目。pimaxofficial 2121055811359347064 为已入库 2121055807618101380（G-STAR 2026 Busan）的 English 续帖，未改已发出条目。getVITURE / BeatSaber / htcvive / BigscreenVR exclude 后 result_count 0（getVITURE most_recent 2121254857134760313 与 BeatSaber most_recent 2121236436825370812 为回复；htcvive most_recent 2118069208126747106 为转发；BigscreenVR most_recent 2118484560715595978 为回复）。
- **media-kol 100→100（+2/−2 cap）：** nathie XREAL Aura vs Meta VR Glasses 2121246381192904761；Dilmerv Unite Tokyo / Meta VR Glasses 2121233793038135521。丢掉最旧 2 条：Dilmerv 💡Curious hand tracking 2118259619923378372 / Dilmerv Calling all developers Meta VR Glasses 2118219230751653981。nathie 2120963842708762640 为已入库 2120906374301315571（Gentle Monster）的续帖，未改已发出条目。Dilmerv 另 3 条初筛丢掉（非 XR）：resume / AI coding tools 2121268410646433860、50.5K followers 2121265204059377776、coding fundamentals vs AI agents 2121247813157757301。Dilmerv most_recent 2121269521499754969 为回复。SadlyItsBradley most_recent 2121108845624000546 仍为转发（与上轮相同，未再拉时间线）。
- top guid 抽查均在（official 现为 PICOXR new game 2121272033539449042 / XREAL Jumanji prize draw 2121257606937211380 / RokidGlobal WebSummit 2121256781322305736 / pimaxofficial G-STAR 2121055807618101380 / VRChat Osaka Major 2121004071121305702 / BeatSaber Content ID 2120959070404305138 / XREAL Landing Party 2120955605384884580；media-kol 现为 nathie Aura vs Meta VR Glasses 2121246381192904761 / Dilmerv Unite Tokyo 2121233793038135521 / ARealityEvent AWE launches phaiworld 2121141198962467113 / Dilmerv Unity XR CanvasCylinder 2121067263709020610 / Hand Skate 2121024016471171584 / started at Meta 2121004826334986327）。
- 上一有变更档：2026-11-13 16:00 BJT media-kol +1。20:00 BJT 一轮无新原创入库、无 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-14 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
