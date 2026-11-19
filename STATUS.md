# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-18 16:10 PST（例行 08:00 BJT 2026-11-19）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 19 Nov 2026 00:10:03 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 19 Nov 2026 00:10:03 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-19 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：MetaVRDevs、getVITURE、BeatSaber、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、XREAL_Global、PICOXR_Dev、VRChat；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、RokidGlobal、pimaxofficial、Play_for_dream、magicleap）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、XREAL_Global most_recent 仍为回复 2122982235188150724（@FXG_VR @baiweiart @nikkmitchell Let's play the funny game with XREAL AURA!）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）（均与 00:00 BJT 轮相同，未再拉时间线）。MetaVRDevs most_recent 从上轮等于 watermark 的入库原帖 2122806546870739142（Unscripted ep 3）变为新原创 2123187217376174242（What happens after winning an Emmy? / TARGO Crafting Crimes），已拉时间线（since_id 2122806546870739142，exclude 后 result_count 1，入库全文；t.co 展开为 https://developers.meta.com/vr/discover/success-stories/targo/?utm_source=social-x&utm_medium=MVRD&utm_campaign=organic&utm_content=CraftingCrimes 与 https://x.com/MetaVRDevs/status/2123187217376174242/video/1）。getVITURE most_recent 从上轮等于 watermark 的入库原帖 2122956121896022457（Z-Axis Award）变为新原创 2123136157890253100（VITURE Beast / Tom's Guide 礼物榜），已拉时间线（since_id 2122956121896022457，exclude 后 result_count 1，入库全文；t.co 展开为 https://www.tomsguide.com/tech/9-best-tech-gifts-of-2026-gadgets-that-blew-us-away）。BeatSaber most_recent 从上轮自转 2123068050337595452 变为新原创 2123099089004900650（We're live in the lobbies! / Play With Us），已拉时间线（since_id 2122688191996260724，exclude 后 result_count 1，入库全文；t.co 展开为 https://x.com/BeatSaber/status/2123099089004900650/photo/1）。ARealityEvent most_recent 从上轮等于 watermark 的入库原帖 2122721508086976575（SPAI AWE 2027）变为新原创 2123114149723124208（That was AWE USA 2026. / 2027 回归），已拉时间线（since_id 2122721508086976575，exclude 后 result_count 1，入库全文；t.co 展开为 https://www.awexr.com/usa-2027/?utm_campaign=341551836-AWE%20USA%202027&utm_content=482055905&utm_medium=social&utm_source=twitter&hss_channel=tw-106035107 与 https://x.com/ARealityEvent/status/2123114149723124208/video/1）。nathie most_recent 从上轮回复 2123028265703260566（@ikkou @MetaforDevs）变为新回复 2123188990123847683（@SadlyItsBradley），已拉时间线（since_id 2122800548990910562，exclude 后 result_count 1，为已入库串帖续帖 2122803465017606298 Vote here!，已合成进 2122800548990910562，跳过）。Dilmerv most_recent 从上轮回复 2123074177720889839（@xrdevrob）变为新回复 2123188328749289840（@iBrews Let me look into this!），已拉时间线（since_id 2123073735666385171，exclude 后 result_count 3，全部入库：2123186161002934390 This is so cool!，引用 @ValemVR TouchSurface 2123161548051124283；2123167830585864380 Greg submitted his mind-blowing VR/MR experience，引用 @GregMadison Sphenomenon 2123165466894176548；2123149605218975806 Unfortunately, I got sick halfway through my Japan trip；t.co 展开为 https://x.com/ValemVR/status/2123161548051124283、https://x.com/ValemVR/status/2123161548051124283/video/1、https://x.com/GregMadison/status/2123165466894176548、https://www.youtube.com/watch?v=NJx843F03I8、https://x.com/Dilmerv/status/2123149605218975806/photo/1）。SadlyItsBradley most_recent 从上轮回复 2122986556377977274（@maxym3D）变为转发 2123110652894138523（RT @SomniumSpace），已拉时间线（since_id 2122983246816325717，exclude 后 result_count 0，无入库）。
- **official 100→100（+3/−3 cap）：** MetaVRDevs What happens after winning an Emmy? 2123187217376174242；getVITURE "VITURE Beast raised the bar for premium immersion…" 2123136157890253100；BeatSaber We're live in the lobbies! 2123099089004900650。丢掉最旧 3 条：VRChat 🎲 Tabletop adventures await in VRChat! 2118407700052599148；getVITURE Hum the song. Hyrule answers. On a giant screen. 🎵 2118396842463351123；XREAL_Global Your full workspace, without the setup. 2118389248499892412。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+4/−4 cap）：** Dilmerv This is so cool! 2123186161002934390；Dilmerv Greg submitted his mind-blowing VR/MR experience to the Meta VR Start Competition! 🤯 2123167830585864380；Dilmerv Unfortunately, I got sick halfway through my Japan trip 🇯🇵, but honestly, I had such an amazing time! 2123149605218975806；ARealityEvent 🎬 That was AWE USA 2026. 2123114149723124208。丢掉最旧 4 条：Dilmerv Here’s a cool Unity tip for gaze + pinch UI! 👀 2119195793881981396；Dilmerv I was about to ask Lucas about a Quest 3 version of his incredible vital demo, and look at what he did today! 🤯👇 2119156585301983395；nathie This Meta Quest game lets you teleport through your own house. 2119132001953325177；Dilmerv Something I find really exciting about Meta VR Glasses is that developers don’t have to start from scratch! 2119105199612584096。
- top guid 抽查均在（official 现为 MetaVRDevs Crafting Crimes 2123187217376174242 / getVITURE Beast Tom's Guide 2123136157890253100 / BeatSaber Play With Us live 2123099089004900650 / RokidGlobal Black Friday 2123068728716013871 / magicleap waveguide 2123040022811304411 / BigscreenVR GTA VI in VR 2122994472913150331 / getVITURE Z-Axis Award 2122956121896022457 / MetaVR_Official OST 9 2122828030414668144；media-kol 现为 Dilmerv TouchSurface quote 2123186161002934390 / Dilmerv Greg Sphenomenon quote 2123167830585864380 / Dilmerv Japan trip 2123149605218975806 / ARealityEvent AWE 2026 recap 2123114149723124208 / Dilmerv Unframed quote 2123073735666385171 / SadlyItsBradley Step one is complete 2122983246816325717 / Dilmerv competition submissions 2122937962174575027 / Dilmerv Puzzleform 2122930855438057722）。
- 上一有变更档：2026-11-19 00:00 BJT official +2 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-19 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
