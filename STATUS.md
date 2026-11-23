# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-23 08:10 PST（例行 00:00 BJT 2026-11-24）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 23 Nov 2026 16:10:29 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 23 Nov 2026 16:10:29 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-24 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：RokidGlobal、MetaVRDevs、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、BigscreenVR、Play_for_dream、PICOXR_Dev、VRChat、nathie、pimaxofficial；其余等于 watermark 跳过（PICOXR、XREAL_Global、getVITURE、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive 当前 100 条官源订阅中已无条目（此前被 cap 丢掉），most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker），未再拉。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。BigscreenVR most_recent 仍为对 @DShankar 的回复 2124661113187131504（12:00 BJT 档已拉，since_id 2124642491962159137，exclude 后 result_count 0）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为转发 2124491962199822604（@sdvx_viga37 「たのしい」が、ぜんぶある / #VRChat）。nathie most_recent 仍为回复 2124572687611945164（@PHIA_bunny @Thrilluwu @OfficialSlimeVR @TUBEVRCLUB @EXXOmixin @im_naku “What a next level way to say yes. Congrats both!”）。pimaxofficial most_recent 仍为已入库串帖续帖 2124782768647475460（自回 2124782743481356412 CES 2027 Limited passes）。RokidGlobal most_recent 从已入库串帖续帖 2124756865750082027（自回 2124518275514310957 Amazon Black Friday 美/欧链接）变为 2124880667506823225（Welcome to Rokid City）；已拉时间线（since_id 2124518275514310957，exclude 后 result_count 2，含已入库旧续帖），入库 1。MetaVRDevs most_recent 从等于 watermark 的 2123899966762668519 变为转发 2124897469255520715（@tevfikufuk Meta VR Start Developer Competition Showcase / Nov 25）；已拉时间线（since_id 2123899966762668519，exclude 后 result_count 0），入库 0。Dilmerv most_recent 从已入库串帖续帖 2124759769852551319（自回 2124759765721227728 Hand Skate Full list）变为 2124883095727767763（Meta VR Glasses blog + YouTube）；已拉时间线（since_id 2124759765721227728，exclude 后 result_count 4，含已入库旧续帖；另丢弃日本旅行生活帖 2124881442618617860），入库 2。SadlyItsBradley most_recent 从转发 2124673939515265212（@BranVR EOZ_VR Furality Ultra straps）变为回复 2124895182298431568（@luke_smith2579 a second AVP doing local SharePlay with the same app）；已拉时间线（since_id 2124576503702946227，exclude 后 result_count 0），入库 0。
- **official 100→100（+1/−1 cap）：** RokidGlobal Welcome to Rokid City 🌴 6 everyday missions, all easier with Rokid glasses. / Black Friday up to 60% off 2124880667506823225。丢掉最旧 1 条：XREAL_Global Learn a language by cracking a case. 2119868911281754378。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv I’m working on two exciting things this week! / Meta VR Glasses blog + YouTube 2124883095727767763；Dilmerv Happy Monday everyone! ☕️ / build with VR/MR 2124878993841103007。丢掉最旧 2 条：Dilmerv I made a few tweaks to the main character! 2120154603945632197 / nathie New leaks suggest the PICO Space Pro could launch on December 2. 2120119315223679136。
- top guid 抽查均在（official 现为 RokidGlobal Welcome to Rokid City 2124880667506823225 / pimaxofficial CES 2027 free passes 2124782743481356412 / BigscreenVR Tomorrow. 2124642491962159137 / BeatSaber One of Us 2124546961587966204 / RokidGlobal Amazon Black Friday 2124518275514310957（已合成自回链接） / VRChat ban apology 2124249109003747407 / BeatSaber Purr OST 9 2124218919296659517 / RokidGlobal GTA VI on Rokid Max 2 2124155883684859968；media-kol 现为 Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007 / Dilmerv Hand Skate 30 ways 2124759765721227728 / Dilmerv Unframed Meta VR Glasses 2124727300780601750 / Dilmerv MR idea 2124578623839518752 / SadlyItsBradley spatial Gaussian Splat bonsai 2124576503702946227 / Dilmerv Meta VR Glasses form factor 2124340557078032645 / Dilmerv Hand Skate forgiving gestures 2124300999653233099）。
- 上一有变更档：2026-11-23 20:00 BJT official +1（pimaxofficial CES 2027 free passes）；media-kol 不变。16:00 BJT official 合成 RokidGlobal Amazon BF 自回；media-kol +2（Dilmerv Hand Skate 30 ways / Dilmerv Unframed Meta VR Glasses）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-24 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
