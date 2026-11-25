# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-25 04:06 PST（例行 20:00 BJT 2026-11-25）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 25 Nov 2026 12:06:02 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 25 Nov 2026 08:14:26 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-25 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、PICOXR_Dev、nathie、Dilmerv。与上轮相同、未再拉时间线的：pimaxofficial 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible）、VRChat 2125336220666663057（已入库串帖续帖 YouTube 补丁说明，根帖 2125336217155965150）、SadlyItsBradley 2125329975624773897（已入库 YouTube new series 根帖 2125173193891856768 的串帖续帖 The deed is done）、BigscreenVR 2125418906546290814（回复 @Hexxhorn 👋😊；根帖 2125418341259264484 已入库）、getVITURE 2125397654163398905（转发 @Eldonchorizo_ Viture Beast Glasses）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR、RokidGlobal）。无 most_recent 低于 watermark，未做删帖核对。XREAL_Global most_recent 从 2125487936162676954（已入库 AURA surgery）变为 2125535085260853389（Gabor / A Bicycle for the Mind）；已拉时间线（since_id 2125487936162676954，exclude 后 result_count 2），入库 2：2125535085260853389 For Gabor, the creative process is as important as the finished work.；2125520767677014018 Anime worlds, meet everyday life. ✨（Gugenka CEO / XREAL AURA）。PICOXR_Dev most_recent 从 2122242565194105089（已入库串帖续帖，根帖 2122242336612896857）变为 2125542244900032734（PICO Space Program）；已拉时间线（since_id 2122242336612896857，exclude 后 result_count 4，其中 3 条为已入库根帖 2122242336612896857 的串帖续帖），入库 1：2125542244900032734 Already shipped an app? Bring it to PICO with your AI agent.。nathie most_recent 从 2125295689454526539（回复 @HeyItsNickRy）变为 2125558013943566591（回复 @IndieGameJoe This would look so good in VR）；已拉时间线（since_id 2125289841910813055，exclude 后 result_count 0）。Dilmerv most_recent 从 2125501625792147675（已入库 Daniel Meta VR Competition quote）变为 2125555101402075246（Not every project needs to become a successful business）；已拉时间线（since_id 2125501625792147675，exclude 后 result_count 2），初筛丢弃 2 条（无明显 XR 内容的职业/社区闲聊）：2125555101402075246 Not every project needs to become a successful business to be worth your time.；2125526202928521366 One thing I truly believe is that helping another developer succeed is just as rewarding as building something yourself.。
- **official 100→100（+3/−3 cap）：** PICOXR_Dev Already shipped an app? Bring it to PICO with your AI agent. 2125542244900032734；XREAL_Global For Gabor, the creative process is as important as the finished work. 2125535085260853389；XREAL_Global Anime worlds, meet everyday life. ✨ 2125520767677014018。丢掉最旧 3 条：XREAL_Global Your living room just became the Hail Mary. 2120593418816516440 / MetaVRDevs Make sure to visit us at Unite Tokyo! 2120591346872602912 / Play_for_dream What if your room could become a castle, or your chair a cockpit? 2120577299942699387。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 PICOXR_Dev PICO Space Program 2125542244900032734 / XREAL_Global Gabor A Bicycle for the Mind 2125535085260853389 / XREAL_Global Gugenka Anime worlds 2125520767677014018 / XREAL_Global AURA surgery 2125487936162676954 / BigscreenVR pssst BF sale 2125418341259264484 / VRChat Release 2026.4.2 2125336217155965150 / getVITURE No TV hideout 2125306175105433963 / getVITURE Vice City 2125286785030947309 / XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957 / VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443；media-kol 仍为 Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / Dilmerv Meta Ray-Ban Displays hand gestures quote 2125247608570679721 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done） / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007）。
- 上一有变更档：2026-11-25 16:00 BJT official +1（XREAL_Global AURA surgery）；media-kol +1（Dilmerv Daniel Meta VR Competition quote）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-26 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
