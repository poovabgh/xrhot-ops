# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-24 04:17 PST（例行 20:00 BJT 2026-11-24）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 24 Nov 2026 12:16:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 24 Nov 2026 12:16:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-24 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、SadlyItsBradley、nathie。与上轮相同、未再拉时间线的：BigscreenVR 2125012047834370488（转发 @VRChat Bigscreen Black Friday sale）、getVITURE 2124954039515234495（已入库串帖续帖 Z-Axis Awards / Win a Luma Ultra，根帖 2124954034205253744）、pimaxofficial 2124782768647475460（已入库串帖续帖 Limited passes，根帖 2124782743481356412）、Play_for_dream 2123607765969142225（回复 @CarsonBarrel）、PICOXR_Dev 2122242565194105089（已入库串帖续帖，根帖 2122242336612896857）、MetaVRDevs 2125025988690247767（回复 @GregMadison @Dilmerv Looks incredible；12:00 BJT 已拉 exclude result_count 0）、VRChat 2125008816647356765（已入库串帖续帖 Read more here，根帖 2125008814835446137）、Dilmerv 2125055023956803669（回复 @wanchuan918 @MetaVRDevs coffee cup；12:00 BJT 已拉 exclude result_count 0）。其余等于 watermark 跳过（ARealityEvent、BeatSaber、htcvive、magicleap、MetaVR_Official、PICOXR、RokidGlobal）。无 most_recent 低于 watermark，未做删帖核对。XREAL_Global most_recent 从 2125130454999146957 变为 2125182442470531128（For Nikk, "what if?" is a reason to start building.）；已拉时间线（since_id 2125130454999146957，exclude 后 result_count 1），入库 1。SadlyItsBradley most_recent 从 2124994475818643518（回复，08:00/16:00 已核）变为 2125173193891856768（I’m recording a YouTube video…）；已拉时间线（since_id 2124960075135779074，exclude 后 result_count 1），入库 1。nathie most_recent 从 2124987578176668005（回复 @MetaVR_Official；08:00 BJT 已拉）变为 2125197435186118915（回复 @MemeioYT What about the real easter egg?）；已拉时间线（since_id 2124987578176668005，exclude 后 result_count 0），不入库。
- **official 100→100（+1/−1 cap）：** XREAL_Global For Nikk, "what if?" is a reason to start building. 2125182442470531128。丢掉最旧 1 条：XREAL_Global Hear your inner voice. 2120230928467304646。
- **media-kol 100→100（+1/−1 cap）：** SadlyItsBradley I’m recording a YouTube video for a new series that I’ve been envisioning for months 2125173193891856768。丢掉最旧 1 条：Dilmerv Here’s a VR rendering technique every XR developer should know about! 👇 2120192393039184290。
- top guid 抽查均在（official 现为 XREAL_Global For Nikk 2125182442470531128 / XREAL_Global New York AURA hands-on 2125130454999146957 / VRChat Bigscreen BF 2125008814835446137 / MetaVR_Official Simple design 2124977157596381527 / MetaVRDevs Dilmerv Unity 2124954802350407798 / getVITURE Liquid Open Beta 2124954034205253744 / BigscreenVR Sale Starts NOW 2124941466510463443 / htcvive VIVE Eagle BF 2124921856587124781 / MetaVRDevs IWSDK 1.1 2124919669169754306 / magicleap waveguide partner 2124905061793030381 / RokidGlobal Welcome to Rokid City 2124880667506823225 / pimaxofficial CES 2027 free passes 2124782743481356412 / BigscreenVR Tomorrow. 2124642491962159137（已合成促销自回） / BeatSaber One of Us 2124546961587966204；media-kol 现为 SadlyItsBradley YouTube new series 2125173193891856768 / Dilmerv Meta VR Glasses Unity guide 2125010915313827884 / SadlyItsBradley Spatial Darkroom 2124960075135779074 / Dilmerv Meta VR Glasses blog + YouTube 2124883095727767763 / Dilmerv Happy Monday VR/MR 2124878993841103007 / Dilmerv Hand Skate 30 ways 2124759765721227728 / Dilmerv Unframed Meta VR Glasses 2124727300780601750 / Dilmerv MR idea 2124578623839518752 / SadlyItsBradley spatial Gaussian Splat bonsai 2124576503702946227）。
- 上一有变更档：2026-11-24 16:00 BJT official +1（XREAL_Global New York AURA hands-on）；media-kol 不变。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-25 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
