# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-25 08:13 PST（例行 00:00 BJT 2026-11-26）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 25 Nov 2026 16:13:20 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 25 Nov 2026 16:13:20 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-26 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：PICOXR、XREAL_Global、getVITURE、pimaxofficial、nathie、Dilmerv、SadlyItsBradley。与上轮相同、未再拉时间线的：BigscreenVR 2125418906546290814（回复 @Hexxhorn 👋😊；根帖 2125418341259264484 已入库）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible）、VRChat 2125336220666663057（已入库串帖续帖 YouTube 补丁说明，根帖 2125336217155965150）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR_Dev、RokidGlobal）。无 most_recent 低于 watermark，未做删帖核对。PICOXR most_recent 从 2123446342504587578（已入库）变为 2125620683614892490；已拉时间线（since_id 2123446342504587578，exclude 后 result_count 1），入库 1：2125620683614892490 Which classic game style would you try in VR first?。XREAL_Global most_recent 从 2125535085260853389（已入库 Gabor）变为 2125591084340261323（AURA Micro Center）；已拉时间线（since_id 2125535085260853389，exclude 后 result_count 2），入库 2：2125591084340261323 The wait is over.；2125579410753679425 Words you can walk around。getVITURE most_recent 从 2125397654163398905（转发 @Eldonchorizo_ Viture Beast Glasses）变为 2125590821437112463；已拉时间线（since_id 2125306175105433963，exclude 后 result_count 1），入库 1：2125590821437112463 Less than one week left to enter!（引用已入库 2122721454538047499 Phantom Blade Zero giveaway）。pimaxofficial most_recent 从 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）变为 2125605552701227050；已拉时间线（since_id 2124782743481356412，exclude 后 result_count 2，其中 1 条为已入库串帖续帖 2124782768647475460），入库 1：2125605552701227050 Pimax Play 2.0.5 is live.。nathie most_recent 从 2125558013943566591（回复 @IndieGameJoe This would look so good in VR）变为 2125587579269447690（串帖续帖 Vote here，根帖 2125587072400384338）；已拉时间线（since_id 2125289841910813055，exclude 后 result_count 2），入库 1 条合成：根帖 2125587072400384338 You can officially start voting for VR Game of the Year! + 续帖 2125587579269447690 Vote here（Steam Awards）。Dilmerv most_recent 从 2125555101402075246（上轮已初筛丢弃）变为 2125605830888165521；已拉时间线（since_id 2125501625792147675，exclude 后 result_count 3，其中 2 条为上轮已丢弃的职业/社区闲聊 2125555101402075246 / 2125526202928521366），入库 1：2125605830888165521 One thing I hope every dev gets to experience… Hand Skate / hand gestures。SadlyItsBradley most_recent 从 2125329975624773897（已入库串帖续帖 The deed is done，根帖 2125173193891856768）变为 2125606051986751657（转发 @danieloquelis Mirrors / Meta VR Competition）；已拉时间线（since_id 2125293622560170322，exclude 后 result_count 1，为已入库串帖续帖 2125329975624773897），无新原创入库。
- **official 100→100（+5/−5 cap）：** PICOXR Which classic game style would you try in VR first? 2125620683614892490；pimaxofficial Pimax Play 2.0.5 is live. 2125605552701227050；XREAL_Global The wait is over. 2125591084340261323（AURA Micro Center Austin / Santa Clara）；getVITURE Less than one week left to enter! 2125590821437112463（引用已入库 2122721454538047499）；XREAL_Global Words you can walk around. 2125579410753679425（Zach Lieberman / XREAL AURA）。丢掉最旧 5 条：XREAL_Global Your favorite VR video player just leveled up. 2120926266681352556 / BeatSaber Your new playlist just dropped. 🎧 2120910336857440643 / BeatSaber OST 9️⃣ is out now! 2120880358769983705 / pimaxofficial IMSA Esports Global Championship, final round. 2120866625205240035 / MetaVR_Official 50+ courses. No tee time. 2120654742716313712。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv One thing I hope every dev gets to experience: waking up genuinely excited about what they're building. 2125605830888165521（Hand Skate / hand gestures）；nathie You can officially start voting for VR Game of the Year! 2125587072400384338 合成续帖 2125587579269447690 Vote here（Steam Awards）。丢掉最旧 2 条：Dilmerv Here’s a cool tip if you’re developing for Meta VR Glasses! 🕶️👇 2120328228577436006 / Dilmerv Honestly, if you’ve been thinking about developing for Meta VR Glasses, I really encourage you to give it a try! 2120313165699281006。
- top guid 抽查均在（official 现为 PICOXR classic game VR 2125620683614892490 / pimaxofficial Play 2.0.5 2125605552701227050 / XREAL_Global AURA Micro Center 2125591084340261323 / getVITURE giveaway reminder 2125590821437112463 / XREAL_Global Zach Lieberman 2125579410753679425 / PICOXR_Dev PICO Space Program 2125542244900032734 / XREAL_Global Gabor A Bicycle for the Mind 2125535085260853389 / XREAL_Global Gugenka Anime worlds 2125520767677014018 / XREAL_Global AURA surgery 2125487936162676954 / BigscreenVR pssst BF sale 2125418341259264484 / VRChat Release 2026.4.2 2125336217155965150 / getVITURE No TV hideout 2125306175105433963 / getVITURE Vice City 2125286785030947309 / XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957；media-kol 现为 Dilmerv Hand Skate excitement 2125605830888165521 / nathie Steam VR GOTY voting 2125587072400384338（已合成 Vote here） / Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / Dilmerv Meta Ray-Ban Displays hand gestures quote 2125247608570679721 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done） / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007）。
- 上一有变更档：2026-11-25 20:00 BJT official +3（PICOXR_Dev PICO Space Program / XREAL_Global Gabor AURA / XREAL_Global Gugenka AURA）；media-kol +0。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-26 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
