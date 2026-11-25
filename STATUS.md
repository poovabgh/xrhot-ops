# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-24 20:07 PST（例行 12:00 BJT 2026-11-25）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 25 Nov 2026 04:07:48 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 25 Nov 2026 00:14:45 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-25 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、getVITURE、Dilmerv。与上轮相同、未再拉时间线的：pimaxofficial 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、PICOXR_Dev 2122242565194105089（已入库串帖续帖，根帖 2122242336612896857）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible）、VRChat 2125336220666663057（已入库串帖续帖 YouTube 补丁说明，根帖 2125336217155965150）、nathie 2125295689454526539（回复 @HeyItsNickRy They do! I recently visited Virtuix）、SadlyItsBradley 2125329975624773897（已入库 YouTube new series 根帖 2125173193891856768 的串帖续帖 The deed is done）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR、RokidGlobal、XREAL_Global）。无 most_recent 低于 watermark，未做删帖核对。BigscreenVR most_recent 从 2125374346965475579（回复 @narazaka When is the last time you tried our eyetracking?）变为 2125418906546290814（回复 @Hexxhorn 👋😊）；已拉时间线（since_id 2125374346965475579，exclude 后 result_count 2），合成入库 1：根帖 2125418341259264484 pssst. hey come here. I gotta tell you something. + 自回 2125418529327403505 our black friday sale is on right now（Beyond 2 + Audio Strap）。getVITURE most_recent 从 2125306175105433963（已入库 "No TV in your hideout? No problem."）变为 2125397654163398905（转发 @Eldonchorizo_ Viture Beast Glasses）；已拉时间线（since_id 2125306175105433963，exclude 后 result_count 0），不入库。Dilmerv most_recent 从 2125372497176711535（回复 @firegold21 Very good feedback!）变为 2125386654991192435（转发自己 Meta VR Glasses Unity guide）；已拉时间线（since_id 2125372497176711535，exclude 后 result_count 0），不入库。
- **official 100→100（+1/−1 cap）：** BigscreenVR pssst. hey come here. I gotta tell you something. 2125418341259264484（已合成黑五自回 2125418529327403505）。丢掉最旧 1 条：RokidGlobal A good movie deserves more than a small screen. 2120532005356200047。
- **media-kol 100 unchanged（+0）。**
- top guid 抽查均在（official 现为 BigscreenVR pssst BF sale 2125418341259264484 / VRChat Release 2026.4.2 2125336217155965150 / getVITURE No TV hideout 2125306175105433963 / getVITURE Vice City 2125286785030947309 / XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957 / VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443 / htcvive VIVE Eagle BF 2124921856587124781 / MetaVRDevs IWSDK 1.1 2124919669169754306 / magicleap waveguide partner 2124905061793030381；media-kol 现为 Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / Dilmerv Meta Ray-Ban Displays hand gestures quote 2125247608570679721 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done） / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007）。
- 上一有变更档：2026-11-25 08:00 BJT official +3；media-kol +4（Dilmerv Muse guide / Dilmerv MRUK / SadlyItsBradley Spatial Darkroom Live 3D / nathie NYPD VR）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-25 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
