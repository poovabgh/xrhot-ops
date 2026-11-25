# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-24 16:14 PST（例行 08:00 BJT 2026-11-25）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 25 Nov 2026 00:14:45 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 25 Nov 2026 00:14:45 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-25 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、getVITURE、VRChat、nathie、Dilmerv、SadlyItsBradley。与上轮相同、未再拉时间线的：pimaxofficial 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、PICOXR_Dev 2122242565194105089（已入库串帖续帖，根帖 2122242336612896857）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible；12:00 BJT 已拉 exclude result_count 0）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR、RokidGlobal、XREAL_Global）。无 most_recent 低于 watermark，未做删帖核对。BigscreenVR most_recent 从 2125012047834370488（转发 @VRChat Bigscreen Black Friday sale）变为 2125374346965475579（回复 @narazaka When is the last time you tried our eyetracking?）；已拉时间线（since_id 2125012047834370488，exclude 后 result_count 0），不入库。getVITURE most_recent 从 2124954039515234495（已入库串帖续帖 Z-Axis Awards / Win a Luma Ultra，根帖 2124954034205253744）变为 2125306175105433963；已拉时间线（since_id 2124954039515234495，exclude 后 result_count 2），入库 2：2125306175105433963 "No TV in your hideout? No problem."（Android Authority ultimate #GTA6 setup，The Beast & VITURE PRo 2）；2125286785030947309 Vice City, but private.（Tom's Guide 周末用 VITURE 玩 GTA 6 + Black Friday deals）。VRChat most_recent 从 2125258780325638214（转发 @skip4D plushies）变为 2125336220666663057（串帖续帖 OR watch the patch notes on YouTube）；已拉时间线（since_id 2125258780325638214，exclude 后 result_count 2），合成入库 1：根帖 2125336217155965150 Release 2026.4.2 is now LIVE on all platforms! + 自回 2125336220666663057 YouTube 补丁说明。nathie most_recent 从 2125213329761173989（回复 @plectrumxr @Naysy）变为 2125295689454526539（回复 @HeyItsNickRy They do! I recently visited Virtuix）；已拉时间线（since_id 2125213329761173989，exclude 后 result_count 1），入库 1：2125289841910813055 Here's a unique behind-the-scenes look at how the NYPD is using VR to train officers。Dilmerv most_recent 从 2125255508424786264（转发 @MetaVRDevs Unity build）变为 2125372497176711535（回复 @firegold21 Very good feedback!）；已拉时间线（since_id 2125255508424786264，exclude 后 result_count 2），入库 2：2125337486905717034 I'm writing a new guide for building VR/MR games with Muse Code + Meta VR CLI + Unity VR CLI；2125316559140700577 XR Devs Tips: Static MRUK occlusion。SadlyItsBradley most_recent 从 2125259205753840015（回复 @PSYCHOV3N0M That's just how I always look）变为 2125329975624773897（已入库 YouTube new series 根帖 2125173193891856768 的串帖续帖 The deed is done）；已拉时间线（since_id 2125259205753840015，exclude 后 result_count 2），入库 1 条新帖 2125293622560170322 My "Spatial Darkroom" app has a Live 3D View feature（引用自身 2125173193891856768）；并将自回 2125329975624773897 The deed is done 合成进已发出条目 2125173193891856768。
- **official 100→100（+3/−3 cap）：** VRChat Release 2026.4.2 2125336217155965150（已合成 YouTube 自回 2125336220666663057）；getVITURE "No TV in your hideout? No problem." 2125306175105433963；getVITURE Vice City, but private. 2125286785030947309。丢掉最旧 3 条：pimaxofficial Buy early. Stay confident. 2120465299539361908 / pimaxofficial Black Friday price protection is live. 2120241914658308117 / pimaxofficial Pimax is heading to IAAPA Expo 2026 in Orlando. 2120241367494373761。
- **media-kol 100→100（+4/−4 cap，另 1 条已发出串帖合成更新）：** Dilmerv I'm writing a new guide for building VR/MR games with Muse Code + Meta VR CLI + Unity VR CLI 2125337486905717034；Dilmerv XR Devs Tips: Static MRUK occlusion 2125316559140700577；SadlyItsBradley Spatial Darkroom Live 3D View 2125293622560170322；nathie NYPD VR training 2125289841910813055。丢掉最旧 4 条：Dilmerv I honestly believe developers have more opportunities today than ever before! 2120297979521253523 / Dilmerv Really worth a read for all VR/MR developers! 2120283640731214017 / Dilmerv One thing I love about Meta XR Operator 2120237612321382423 / ARealityEvent We have exciting news! 2120230014729990421。已发出条目 2125173193891856768（SadlyItsBradley YouTube new series）合成自回 The deed is done 2125329975624773897（标题/链接/guid/pubDate 未改）。
- top guid 抽查均在（official 现为 VRChat Release 2026.4.2 2125336217155965150 / getVITURE No TV hideout 2125306175105433963 / getVITURE Vice City 2125286785030947309 / XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957 / VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443 / htcvive VIVE Eagle BF 2124921856587124781 / MetaVRDevs IWSDK 1.1 2124919669169754306 / magicleap waveguide partner 2124905061793030381 / RokidGlobal Welcome to Rokid City 2124880667506823225；media-kol 现为 Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / Dilmerv Meta Ray-Ban Displays hand gestures quote 2125247608570679721 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done） / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007）。
- 上一有变更档：2026-11-25 00:00 BJT official +0；media-kol +1（Dilmerv Meta Ray-Ban Displays hand gestures quote）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-25 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
