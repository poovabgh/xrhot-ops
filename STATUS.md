# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-25 20:08 PST（例行 12:00 BJT 2026-11-26）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 26 Nov 2026 04:08:05 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 26 Nov 2026 04:08:05 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-26 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、Dilmerv、SadlyItsBradley、VRChat、XREAL_Global。与上一轮 most_recent 相同、未重拉：MetaVRDevs（仍为转发 2125694388110242184 @8bitbob_dev mixed reality Koi pond / Meta VR Start）、Play_for_dream（仍为回复 2123607765969142225 @CarsonBarrel）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、getVITURE、htcvive、magicleap、MetaVR_Official、nathie、PICOXR、PICOXR_Dev、pimaxofficial、RokidGlobal）。无 most_recent 低于 watermark，未做删帖核对。BigscreenVR most_recent 从 2125418906546290814（回复 @Hexxhorn；根帖 2125418341259264484 已入库）变为 2125772610130829398；已拉时间线（since_id 2125418341259264484，exclude 后 result_count 4），入库 1：2125772610130829398 Our Black Friday sale isn't the only cool announcement this week.（Halo Mount / YouTube）。其余 3 条未入库：2125755015721812003 博客链接自回与 2125754737765306387 or check out the post on our blog 同属根帖 2125754736628711926，根帖已删除/Not Found，不虚构根帖、不单独收续帖；2125418529327403505 为已入库串帖续帖 our black friday sale is on right now。Dilmerv most_recent 从 2125742449230598146（回复 @teawa_）变为 2125794214789222426；已拉时间线（since_id 2125733794116186138，exclude 后 result_count 3），入库 1：2125767482640076866 Added an optional Comic Look to Hand Skate 🛹；丢掉非 XR/仅顺带提及：2125794214789222426 Here’s a question for developers using AI agents（通用 AI agent 体验，未涉及 XR）/ 2125756442883883212 I want to see something cool today（征集 AI、XR、游戏或任何技术截图，XR 仅顺带）。SadlyItsBradley most_recent 从 2125634428458430834（转发 @xbh_artist）变为 2125787243486806311（转发 @EOZ_VR Our 2nd batch of pre-orders are live and on sale now）；已拉时间线（since_id 2125293622560170322，exclude 后 result_count 1，为已入库串帖续帖 2125329975624773897 The deed is done），无新原创入库。VRChat most_recent 从 2125711959081529359（已入库串帖续帖 Watch the YouTube video here，根帖 2125711956757655999）变为 2125765152897405127（转发 @SANCTUMVR YOU ARE INVITED TO SANCTUM）；已拉时间线（since_id 2125711956757655999，exclude 后 result_count 1，为已入库串帖续帖 2125711959081529359），无新原创入库。XREAL_Global most_recent 从 2125591084340261323（已入库 AURA Micro Center）变为 2125800881421697049；已拉时间线（since_id 2125591084340261323，exclude 后 result_count 1），入库 1：2125800881421697049 A better view shouldn’t mean taking your eyes off the patient.（XREAL AURA / apoQlar HoloMedicine / Emily Cain；同题较早帖 2125487936162676954 Emily Kane 已在 feed，本条为新 id，照收）。
- **official 100→100（+2/−2 cap）：** XREAL_Global A better view shouldn’t mean taking your eyes off the patient. 2125800881421697049（AURA / apoQlar / Emily Cain）；BigscreenVR Our Black Friday sale isn't the only cool announcement this week. 2125772610130829398（Halo Mount）。丢掉最旧 2 条：VRChat The Rainbow Six Osaka Major is coming to VRChat! 2121004071121305702 / BeatSaber Creators, this one's for you. 📹 2120959070404305138。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv Added an optional Comic Look to Hand Skate 🛹 2125767482640076866。丢掉最旧 1 条：Dilmerv 💡Curious, for those building hands-first VR/MR games, what’s been your biggest challenge? 2120586123080577356。
- top guid 抽查均在（official 现为 XREAL_Global AURA apoQlar surgery Cain 2125800881421697049 / BigscreenVR Halo Mount 2125772610130829398 / VRChat Holiday Gifting / Hype Train 2125711956757655999（已合成 YouTube） / MetaVR_Official Courtside Spring 2027 2125674090594029966 / BeatSaber Memory Marker 2125641068486041632 / PICOXR classic game VR 2125620683614892490 / pimaxofficial Play 2.0.5 2125605552701227050 / XREAL_Global AURA Micro Center 2125591084340261323 / getVITURE giveaway reminder 2125590821437112463 / XREAL_Global Zach Lieberman 2125579410753679425 / PICOXR_Dev PICO Space Program 2125542244900032734 / XREAL_Global Gabor A Bicycle for the Mind 2125535085260853389 / XREAL_Global Gugenka Anime worlds 2125520767677014018 / XREAL_Global AURA surgery Kane 2125487936162676954 / BigscreenVR pssst BF sale 2125418341259264484 / VRChat Release 2026.4.2 2125336217155965150；media-kol 现为 Dilmerv Hand Skate Comic Look 2125767482640076866 / Dilmerv lightweight VR glasses devs 2125733794116186138 / Dilmerv Muse Code guide finished 2125723311925604424 / Dilmerv busy weeks VR Level Up / Hand Skate / Valem 2125685976349421768 / nathie Batman Arkham Shadow VR hands 2125682080684134443 / ARealityEvent Physical AI World 2027 2125650804950626629 / Dilmerv Meta VR CLI docs search 2125649965460414943 / Dilmerv Hand Skate excitement 2125605830888165521 / nathie Steam VR GOTY voting 2125587072400384338（已合成 Vote here） / Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322 / nathie NYPD VR training 2125289841910813055 / SadlyItsBradley YouTube new series 2125173193891856768（已合成 The deed is done））。
- 上一有变更档：2026-11-26 08:00 BJT official +3（VRChat Holiday Gifting / MetaVR_Official Courtside Spring 2027 / BeatSaber Memory Marker）；media-kol +6（Dilmerv lightweight VR glasses / Dilmerv Muse guide finished / Dilmerv busy weeks / nathie Batman VR hands / ARealityEvent Physical AI World 2027 / Dilmerv Meta VR CLI docs）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-26 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
