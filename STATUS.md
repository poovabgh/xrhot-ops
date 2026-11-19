# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-18 20:08 PST（例行 12:00 BJT 2026-11-19）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 19 Nov 2026 04:08:11 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 19 Nov 2026 04:08:11 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-19 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、nathie、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、PICOXR_Dev、VRChat；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）（均与 08:00 BJT 轮相同，未再拉时间线）。XREAL_Global most_recent 从上轮回复 2122982235188150724（@FXG_VR @baiweiart @nikkmitchell Let's play the funny game with XREAL AURA!）变为新原创 2123260780376428872（Powered by Android XR, XREAL AURA / Gemini）；已拉时间线（since_id 2122691780453793834，exclude 后 result_count 0；不加 exclude 仅返回上轮已见回复/转发 6 条，时间线未包含该新 id）；经 get_posts_by_id 确认其为独立原创（conversation_id 即本帖、无 referenced_tweets、无附件/链接），入库全文。nathie most_recent 从上轮回复 2123188990123847683（@SadlyItsBradley）变为新原创 2123208524624966068（GTA 6 gaming family），已拉时间线（since_id 2122800548990910562，exclude 后 result_count 2：2123208524624966068 为非 VR 游戏/闲聊，丢弃；2122803465017606298 Vote here! 为已入库串帖续帖，已合成进 2122800548990910562，跳过）。Dilmerv most_recent 从上轮回复 2123188328749289840（@iBrews Let me look into this!）变为新回复 2123240343022006679（@soulblocks Are you real?），已拉时间线（since_id 2123186161002934390，exclude 后 result_count 2，全部入库：2123234841676100005 I have so much respect for developers building traditional games and apps（note_tweet 全文）；2123208850996109429 Honestly, I’m blown away by the number and quality of submissions being built for Meta VR Glasses and Quest in the Meta VR Start Dev Competition!；t.co 展开为 https://x.com/Dilmerv/status/2123208850996109429/photo/1）。SadlyItsBradley most_recent 从上轮转发 2123110652894138523（RT @SomniumSpace）变为转发 2123256706226385202（RT @SegaAmusements），已拉时间线（since_id 2122983246816325717，exclude 后 result_count 1，为引用帖 2123249192084865345 is this a sign?，引用 @socialchanger Microsoft Ignite / Moscone Center 停电，非 XR，丢弃）。
- **official 100→100（+1/−1 cap）：** XREAL_Global Powered by Android XR, XREAL AURA combines millions of your favorite apps from Google Play, over 100 experiences made for XR, and real-time help from Gemini in one portable experience. 2123260780376428872。丢掉最旧 1 条：XREAL_Global Your next canvas is the room around you. 2118419068080300536。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv I have so much respect for developers building traditional games and apps, and I’ve spent years doing exactly that! 2123234841676100005；Dilmerv Honestly, I’m blown away by the number and quality of submissions being built for Meta VR Glasses and Quest in the Meta VR Start Dev Competition! 2123208850996109429。丢掉最旧 2 条：Dilmerv When I worked on Arcade Hoops, music visualizers were a big part of the experience. 2119278281421725959；Dilmerv Added 13 animations to “Hand Skate” coming to Quest & Meta VR Glasses and have been tweaking the look and feel of the ga 2119273069147455708。
- top guid 抽查均在（official 现为 XREAL_Global AURA Android XR/Gemini 2123260780376428872 / MetaVRDevs Crafting Crimes 2123187217376174242 / getVITURE Beast Tom's Guide 2123136157890253100 / BeatSaber Play With Us live 2123099089004900650 / RokidGlobal Black Friday 2123068728716013871 / magicleap waveguide 2123040022811304411 / BigscreenVR GTA VI in VR 2122994472913150331 / getVITURE Z-Axis Award 2122956121896022457；media-kol 现为 Dilmerv VR/MR fun 2123234841676100005 / Dilmerv Meta VR Start submissions 2123208850996109429 / Dilmerv TouchSurface quote 2123186161002934390 / Dilmerv Greg Sphenomenon quote 2123167830585864380 / Dilmerv Japan trip 2123149605218975806 / ARealityEvent AWE 2026 recap 2123114149723124208 / Dilmerv Unframed quote 2123073735666385171 / SadlyItsBradley Step one is complete 2122983246816325717）。
- 上一有变更档：2026-11-19 08:00 BJT official +3 / media-kol +4。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-19 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
