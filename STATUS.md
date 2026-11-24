# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-23 16:07 PST（例行 08:00 BJT 2026-11-24）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 24 Nov 2026 00:07:40 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 24 Nov 2026 00:07:40 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-24 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、Dilmerv、getVITURE、htcvive、magicleap、MetaVR_Official、MetaVRDevs、nathie、SadlyItsBradley、VRChat；与上轮相同、未再拉时间线的：PICOXR_Dev、pimaxofficial、Play_for_dream；其余等于 watermark 跳过（ARealityEvent、BeatSaber、PICOXR、RokidGlobal、XREAL_Global）。无 most_recent 低于 watermark，未做删帖核对。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。pimaxofficial most_recent 仍为已入库串帖续帖 2124782768647475460（自回 2124782743481356412 CES 2027 Limited passes）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。BigscreenVR most_recent 从对 @DShankar 的回复 2124661113187131504 变为转发 2125012047834370488（@VRChat Bigscreen Black Friday sale）；已拉时间线（since_id 2124642491962159137，exclude 后 result_count 2），入库 1 条独立促销帖，并将自回 2124972955503587677（Our Black Friday Sale is Live NOW）合成进已入库 Tomorrow. 2124642491962159137。Dilmerv most_recent 从已入库 2124883095727767763（Meta VR Glasses blog + YouTube）变为回复 2125015779028750649（@motorsep @MetaVRDevs Thanks for your suggestion!）；已拉时间线（since_id 2124883095727767763，exclude 后 result_count 2；丢弃 Mac/XLR/Stream Deck 设备升级生活帖 2124978778619199754），入库 1。getVITURE most_recent 从等于 watermark 的 2123506093741481991 变为已入库串帖续帖 2124954039515234495（Z-Axis Awards / Win a Luma Ultra）；已拉时间线（since_id 2123506093741481991，exclude 后 result_count 3，均为同一串），入库 1（根帖 2124954034205253744 VITURE Liquid Open Beta，已合成两则续帖）。htcvive most_recent 从转发 2118069208126747106（@XsensEnt Ultimate Tracker；官源订阅此前已无条目）变为 2124921856587124781（Black Friday 20% off VIVE Eagle AI glasses）；已拉时间线（since_id 2118069208126747106，exclude 后 result_count 1），入库 1。magicleap most_recent 从等于 watermark 的 2123040022811304411 变为 2124905061793030381（waveguide partner）；已拉时间线（since_id 2123040022811304411，exclude 后 result_count 1），入库 1。MetaVR_Official most_recent 从回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）变为 2124977157596381527（Simple design. Big impression. / Meta VR Glasses updates）；已拉时间线（since_id 2123918298136158415，exclude 后 result_count 1），入库 1。MetaVRDevs most_recent 从转发 2124897469255520715（@tevfikufuk Meta VR Start Developer Competition Showcase）变为 2124954802350407798（Follow @Dilmerv Unity build for Meta VR Glasses）；已拉时间线（since_id 2123899966762668519，exclude 后 result_count 2），入库 2。nathie most_recent 从回复 2124572687611945164（@PHIA_bunny 等）变为回复 2124987578176668005（@MetaVR_Official）；已拉时间线（since_id 2124257333731786887，exclude 后 result_count 1，为已入库 Zelda 串帖续帖 Source 2124257850876711299），入库 0。SadlyItsBradley most_recent 从回复 2124895182298431568（@luke_smith2579 a second AVP doing local SharePlay）变为回复 2124994475818643518（@Grailx3 @zmiennys natively editing splats on frame）；已拉时间线（since_id 2124576503702946227，exclude 后 result_count 1），入库 1。VRChat most_recent 从转发 2124491962199822604（@sdvx_viga37）变为已入库串帖续帖 2125008816647356765（Read more here）；已拉时间线（since_id 2124249109003747407，exclude 后 result_count 2），入库 1（根帖 2125008814835446137 Bigscreen Black Friday sale，已合成续帖链接）。
- **official 100→100（+8/−8 cap；另 1 条已发出条目合成自回）：** VRChat Bigscreen has a Black Friday sale! / code VRC2026 2125008814835446137（已合成自回 Read more）；MetaVR_Official Simple design. Big impression. / Sign up for Meta VR Glasses updates 2124977157596381527；MetaVRDevs Follow @Dilmerv through a Unity build for Meta VR Glasses 2124954802350407798；getVITURE Introducing VITURE Liquid (Open Beta) 2124954034205253744（已合成两则续帖）；BigscreenVR Our Black Friday Sale Starts NOW! 2124941466510463443；htcvive Black Friday starts now. 20% off VIVE Eagle. 2124921856587124781；MetaVRDevs What changes in VR development when eyes and hands become the primary input? / IWSDK 1.1 2124919669169754306；magicleap A waveguide may meet specifications… / waveguide partner 2124905061793030381。另将 BigscreenVR Tomorrow. 2124642491962159137 合成自回 2124972955503587677（Our Black Friday Sale is Live NOW）。丢掉最旧 8 条：XREAL_Global What if you could experience the San Francisco Ballet’s 'Nutcracker' 2120212983888371721 / XREAL_Global With XREAL AURA Fallout: Faction 2120201229665984698 / PICOXR Audio Trip is back with a major update and new DLC. 2120185142656340100 / RokidGlobal Fresh snow and a trail that kept going. 2120169616966332669 / magicleap The insights gathered by our engineers during fabrication 2120146962402214039 / XREAL_Global Your city, enhanced. 2120035136682987550 / MetaVRDevs Your first Meta VR Glasses prototype can start on your desktop. 2119909497934356661 / VRChat Want to celebrate New Year's with us? 2119893528847233479。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv XR devs, super excited to share a new guide… Meta VR Glasses development in Unity 2125010915313827884；SadlyItsBradley Turning ANY desktop surface into a “Spatial Darkroom” 2124960075135779074。丢掉最旧 2 条：nathie Scott, CEO of Combat Waffle Studios… 2120186765088817533 / SadlyItsBradley Bought some Infrared-transparent 3D printer filament 2120154827783094651。
- top guid 抽查均在（official 现为 VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443 / htcvive VIVE Eagle BF 2124921856587124781 / MetaVRDevs IWSDK 1.1 2124919669169754306 / magicleap waveguide partner 2124905061793030381 / RokidGlobal Welcome to Rokid City 2124880667506823225 / pimaxofficial CES 2027 free passes 2124782743481356412 / BigscreenVR Tomorrow. 2124642491962159137（已合成促销自回） / BeatSaber One of Us 2124546961587966204；media-kol 现为 Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007 / Dilmerv Hand Skate 30 ways 2124759765721227728 / Dilmerv Unframed Meta VR Glasses 2124727300780601750 / Dilmerv MR idea 2124578623839518752 / SadlyItsBradley spatial Gaussian Splat bonsai 2124576503702946227）。
- 上一有变更档：2026-11-24 00:00 BJT official +1（RokidGlobal Welcome to Rokid City）；media-kol +2（Dilmerv Meta VR Glasses blog+YT / Dilmerv Happy Monday VR/MR）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-24 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
