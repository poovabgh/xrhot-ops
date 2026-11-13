# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-12 16:13 PST（例行 08:00 BJT 2026-11-13）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 13 Nov 2026 00:13:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 13 Nov 2026 00:13:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-13 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、MetaVRDevs、VRChat、BeatSaber、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、magicleap）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+7/−7 cap）：** VRChat Rainbow Six Osaka Major 2121004071121305702；BeatSaber OST 9 Content ID free 2120959070404305138；XREAL_Global Landing Party 2120955605384884580；MetaVRDevs controller-first / Meta VR Glasses 2120954679425425625；MetaVR_Official Winter’s coming / GOLF+ 2120947398851912120（续帖 Plot twist 2120973071490453795 已合并）；XREAL_Global DeoVR on AURA 2120926266681352556；BeatSaber OST 9 playlist 2120910336857440643。丢掉最旧 7 条：VRChat Spookality DJ Event 2115896453268742615 / getVITURE HDMI to USB-C Adapter 2115864882193027520 / MetaVRDevs Would your title play better without controllers? 2115856631544295764 / VRChat Treats Makeship 2115854632425488489 / XREAL_Global Spatial computing without the bulk 2115851863253746133 / PICOXR Flight deck 2115836266340037093 / RokidGlobal Tesla 2115805860471726171。MetaVR_Official 2120654800828420258 为已入库 2120654742716313712（GOLF+）的续帖；VRChat 2119893530722140614 为已入库 2119893528847233479（New Year's Entertainment Network）的续帖；htcvive / BigscreenVR exclude 后 result_count 0。
- **media-kol 100→100（+7/−7 cap）：** Dilmerv Hand Skate kickflip 2121024016471171584；Dilmerv started at Meta 2121004826334986327；Dilmerv Meta VR Glasses photo 2120999787629518873；Dilmerv Mac Studio / Meta XR Simulator 2120948514062536849；Dilmerv HandSkate polish / Unite 2120933406611538381；ARealityEvent AWE / PhAI Long Beach 2120924636741525698；Dilmerv Late Latching 2120912928798859353。丢掉最旧 7 条：nathie SteamOS original Quest 2118025614670037343 / Dilmerv Meta VR CLI tip 2118003054620389681 / Dilmerv passthrough components 2117942515235963098 / Dilmerv 5,000 registered Start Competition 2117829463849537998 / SadlyItsBradley FrameOS WebXR 2117781251155464370 / Dilmerv Vector Tango 2117769557595320404 / Dilmerv Japan, here we go 2117731139238465617。nathie 2120963842708762640 为已入库 2120906374301315571（Gentle Monster）的续帖，未改已发出条目。SadlyItsBradley most_recent 为转发，exclude 后 result_count 0。Dilmerv 2120915303915729076 为生病闲聊，初筛丢弃；2121032296916787447 为回复。
- top guid 抽查均在（official 现为 VRChat Osaka Major 2121004071121305702 / BeatSaber Content ID 2120959070404305138 / XREAL Landing Party 2120955605384884580 / MetaVRDevs controller-first 2120954679425425625 / MetaVR_Official Winter’s coming 2120947398851912120 / XREAL DeoVR 2120926266681352556 / BeatSaber playlist 2120910336857440643；media-kol 现为 Dilmerv Hand Skate 2121024016471171584 / started at Meta 2121004826334986327 / Meta VR Glasses photo 2120999787629518873 / Mac Studio 2120948514062536849 / HandSkate polish 2120933406611538381 / ARealityEvent AWE PhAI 2120924636741525698 / Dilmerv Late Latching 2120912928798859353）。
- 上一有变更档：2026-11-13 00:00 BJT official +2 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-13 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
