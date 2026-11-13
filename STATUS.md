# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-12 20:07 PST（例行 12:00 BJT 2026-11-13）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 13 Nov 2026 04:07:51 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 13 Nov 2026 04:07:51 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-13 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、pimaxofficial、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、XREAL_Global、RokidGlobal、getVITURE、Play_for_dream、MetaVRDevs、magicleap、VRChat、BeatSaber、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+1/−1 cap）：** pimaxofficial G-STAR 2026 Busan 2121055807618101380（续帖 English 2121055811359347064 已合并）。丢掉最旧 1 条：XREAL_Global Life doesn’t stop at the edge of a virtual screen 2115897128971042888。MetaVR_Official 2120973071490453795 为已入库 2120947398851912120（Winter’s coming）的续帖，未改已发出条目。htcvive / BigscreenVR exclude 后 result_count 0。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv Unity XR / CanvasCylinder 2121067263709020610。丢掉最旧 1 条：SadlyItsBradley Chromium Steam Frame WebXR 2118073306570007037。nathie 2120963842708762640 为已入库 2120906374301315571（Gentle Monster）的续帖，未改已发出条目。SadlyItsBradley most_recent 为转发，exclude 后 result_count 0。Dilmerv most_recent 2121079927625994495 与 nathie most_recent 2121078383358710208 均为回复。
- top guid 抽查均在（official 现为 pimaxofficial G-STAR 2121055807618101380 / VRChat Osaka Major 2121004071121305702 / BeatSaber Content ID 2120959070404305138 / XREAL Landing Party 2120955605384884580 / MetaVRDevs controller-first 2120954679425425625 / MetaVR_Official Winter’s coming 2120947398851912120 / XREAL DeoVR 2120926266681352556；media-kol 现为 Dilmerv Unity XR CanvasCylinder 2121067263709020610 / Hand Skate 2121024016471171584 / started at Meta 2121004826334986327 / Meta VR Glasses photo 2120999787629518873 / Mac Studio 2120948514062536849 / HandSkate polish 2120933406611538381 / ARealityEvent AWE PhAI 2120924636741525698）。
- 上一有变更档：2026-11-13 08:00 BJT official +7 / media-kol +7。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-13 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
