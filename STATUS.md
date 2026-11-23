# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-23 04:05 PST（例行 20:00 BJT 2026-11-23）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 23 Nov 2026 12:05:42 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 23 Nov 2026 08:09:52 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-23 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：pimaxofficial；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、BigscreenVR、RokidGlobal、Play_for_dream、PICOXR_Dev、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVRDevs、PICOXR、XREAL_Global、getVITURE、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive 当前 100 条官源订阅中已无条目（此前被 cap 丢掉），most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker），未再拉。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。BigscreenVR most_recent 仍为对 @DShankar 的回复 2124661113187131504（12:00 BJT 档已拉，since_id 2124642491962159137，exclude 后 result_count 0）。RokidGlobal most_recent 仍为已入库串帖续帖 2124756865750082027（自回 2124518275514310957 Amazon Black Friday 美/欧链接）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为转发 2124491962199822604（@sdvx_viga37 「たのしい」が、ぜんぶある / #VRChat）。nathie most_recent 仍为回复 2124572687611945164（@PHIA_bunny @Thrilluwu @OfficialSlimeVR @TUBEVRCLUB @EXXOmixin @im_naku “What a next level way to say yes. Congrats both!”）。Dilmerv most_recent 仍为已入库串帖续帖 2124759769852551319（自回 2124759765721227728 Hand Skate Full list）。SadlyItsBradley most_recent 仍为转发 2124673939515265212（@BranVR EOZ_VR Furality Ultra straps；12:00 BJT 档已拉，无入库）。pimaxofficial most_recent 从已入库串帖续帖 2123716023920865610（自回 2123716020217225505）变为自回 2124782768647475460（CES 2027 Limited passes 续帖，根帖 2124782743481356412）；已拉时间线（since_id 2123716020217225505，exclude 后 result_count 3，含已入库旧续帖与新根帖+自回），入库 1。
- **official 100→100（+1/−1 cap）：** pimaxofficial Meet the Pimax team (and our headsets) at booth #20954, Las Vegas, Jan 6–9. / CES 2027 free passes 2124782743481356412（合成自回 2124782768647475460）。丢掉最旧 1 条：MetaVRDevs The reviews are in. 2119866328047890651。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 pimaxofficial CES 2027 free passes 2124782743481356412 / BigscreenVR Tomorrow. 2124642491962159137 / BeatSaber One of Us 2124546961587966204 / RokidGlobal Amazon Black Friday 2124518275514310957（已合成自回链接） / VRChat ban apology 2124249109003747407 / BeatSaber Purr OST 9 2124218919296659517 / RokidGlobal GTA VI on Rokid Max 2 2124155883684859968 / MetaVR_Official LSU 2123918298136158415；media-kol 仍为 Dilmerv Hand Skate 30 ways 2124759765721227728 / Dilmerv Unframed Meta VR Glasses 2124727300780601750 / Dilmerv MR idea 2124578623839518752 / SadlyItsBradley spatial Gaussian Splat bonsai 2124576503702946227 / Dilmerv Meta VR Glasses form factor 2124340557078032645 / Dilmerv Hand Skate forgiving gestures 2124300999653233099 / nathie Zelda OoT VR mod 2124257333731786887 / Dilmerv XR demo test 2124239952581919229）。
- 上一有变更档：2026-11-23 16:00 BJT official 合成 RokidGlobal Amazon BF 自回；media-kol +2（Dilmerv Hand Skate 30 ways / Dilmerv Unframed Meta VR Glasses）。12:00 BJT 档预检后拉过 BigscreenVR 与 SadlyItsBradley，无入库、无 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-24 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
