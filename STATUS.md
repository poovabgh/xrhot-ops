# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-25 00:14 PST（例行 16:00 BJT 2026-11-25）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 25 Nov 2026 08:14:26 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 25 Nov 2026 08:14:26 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-25 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：Dilmerv、XREAL_Global。与上轮相同、未再拉时间线的：pimaxofficial 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、PICOXR_Dev 2122242565194105089（已入库串帖续帖，根帖 2122242336612896857）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible）、VRChat 2125336220666663057（已入库串帖续帖 YouTube 补丁说明，根帖 2125336217155965150）、nathie 2125295689454526539（回复 @HeyItsNickRy They do! I recently visited Virtuix）、SadlyItsBradley 2125329975624773897（已入库 YouTube new series 根帖 2125173193891856768 的串帖续帖 The deed is done）、BigscreenVR 2125418906546290814（回复 @Hexxhorn 👋😊；根帖 2125418341259264484 已入库）、getVITURE 2125397654163398905（转发 @Eldonchorizo_ Viture Beast Glasses）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR、RokidGlobal）。无 most_recent 低于 watermark，未做删帖核对。Dilmerv most_recent 从 2125386654991192435（转发自己 Meta VR Glasses Unity guide）变为 2125501625792147675（引用 @danieloquelis Meta VR Competition mirrors）；已拉时间线（since_id 2125386654991192435，exclude 后 result_count 1），入库 1：2125501625792147675 Daniel didn’t get enough visibility on this, but honestly, this is INSANELY good! 🤯（引用 @danieloquelis）。XREAL_Global most_recent 从 2125182442470531128（已入库 For Nikk）变为 2125487936162676954（AURA / apoQlar HoloMedicine Robotics surgery）；已拉时间线（since_id 2125182442470531128，exclude 后 result_count 1），入库 1。
- **official 100→100（+1/−1 cap）：** XREAL_Global A better view shouldn’t mean taking your eyes off the patient. 2125487936162676954。丢掉最旧 1 条：XREAL_Global Step inside an award-winning story. 2120563760267960521。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv Daniel didn’t get enough visibility on this, but honestly, this is INSANELY good! 🤯 2125501625792147675（引用 @danieloquelis Meta VR Competition mirrors）。丢掉最旧 1 条：nathie Disney+ just added 3D movies and immersive viewing environments on Meta Quest 3 and 3S. 2120302292112969841。
- top guid 抽查均在（official 现为 XREAL_Global AURA surgery 2125487936162676954 / BigscreenVR pssst BF sale 2125418341259264484 / VRChat Release 2026.4.2 2125336217155965150 / getVITURE No TV hideout 2125306175105433963 / getVITURE Vice City 2125286785030947309 / XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957 / VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443 / htcvive VIVE Eagle BF 2124921856587124781 / MetaVRDevs IWSDK 1.1 2124919669169754306 / magicleap waveguide partner 2124905061793030381；media-kol 现为 Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / Dilmerv Meta Ray-Ban Displays hand gestures quote 2125247608570679721 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done） / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007）。
- 上一有变更档：2026-11-25 12:00 BJT official +1（BigscreenVR pssst BF sale thread）；media-kol +0。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-25 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
