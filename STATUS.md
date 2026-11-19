# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-19 00:06 PST（例行 16:00 BJT 2026-11-19）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 19 Nov 2026 08:06:15 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 19 Nov 2026 08:06:15 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-19 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：RokidGlobal、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、PICOXR_Dev、VRChat、nathie；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、nathie most_recent 仍为上轮已丢弃的非 VR 游戏/闲聊 2123208524624966068（GTA 6 gaming family）（均与 12:00 BJT 轮相同，未再拉时间线）。RokidGlobal most_recent 从上轮已入库原创 2123068728716013871（Black Friday starts tomorrow）变为同串自回 2123321967533228282（Deals page）；已拉时间线（since_id 2123068728716013871，exclude 后仍返回该自回 1 条，conversation_id 为已入库父帖），按串帖规则合成进 2123068728716013871（guid/title/pubDate/link 不变；t.co 展开为 https://global.rokid.com/pages/rokid-bfcm-2026?utm_source=x&utm_medium=social&utm_campaign=bf2026），不另立条目。Dilmerv most_recent 从上轮回复 2123240343022006679（@soulblocks Are you real?）变为新原创 2123319106656989445（Meta VR Start submissions / Meta VR Glasses）；已拉时间线（since_id 2123234841676100005，exclude 后 result_count 2，全部入库：2123319106656989445 Seeing all the incredible submissions…（note_post 全文；t.co 展开为 https://x.com/Dilmerv/status/2123319106656989445/video/1）；2123277400771567792 👏Huge congrats to @targostories for their well-deserved Emmy! 🏆，引用 @MetaVRDevs Crafting Crimes 2123187217376174242，t.co 展开为 https://x.com/MetaVRDevs/status/2123187217376174242）。SadlyItsBradley most_recent 从上轮转发 2123256706226385202（RT @SegaAmusements）变为引用帖 2123281801817051516（Fun to use a gaussian splat as a makeshift alignment debugger）；已拉时间线（since_id 2122983246816325717，exclude 后 result_count 2：2123281801817051516 入库，引用自身 2122983246816325717 Step one is complete，t.co 展开为 https://x.com/SadlyItsBradley/status/2123281801817051516/video/1 与 https://x.com/SadlyItsBradley/status/2122983246816325717；2123249192084865345 is this a sign? 引用 @socialchanger Microsoft Ignite / Moscone Center 停电，非 XR，与上轮相同，丢弃）。
- **official 100→100（串帖合成，无新条目/无 cap）：** 将 RokidGlobal Deals page 2123321967533228282 合成进已入库 Black Friday 2123068728716013871。
- **media-kol 100→100（+3/−3 cap）：** Dilmerv 🤯 Seeing all the incredible submissions to the Meta VR Start Developer Competition makes me even more excited about Meta VR Glasses! 2123319106656989445；SadlyItsBradley Fun to use a gaussian splat as a makeshift alignment debugger 2123281801817051516；Dilmerv 👏Huge congrats to @targostories for their well-deserved Emmy! 🏆 2123277400771567792。丢掉最旧 3 条：Dilmerv Came up with a cool idea to let players resize each skate park! 2119484628037722374；Dilmerv I’m so excited about the progress I’ve made this weekend on my new Mixed Reality game, Hand Skate! 2119376912027967953；Dilmerv Meta VR Glasses could be one of the biggest opportunities for developers, and I genuinely encourage you to start buildin 2119316526876524557。
- top guid 抽查均在（official 现为 XREAL_Global AURA Android XR/Gemini 2123260780376428872 / MetaVRDevs Crafting Crimes 2123187217376174242 / getVITURE Beast Tom's Guide 2123136157890253100 / BeatSaber Play With Us live 2123099089004900650 / RokidGlobal Black Friday 2123068728716013871 / magicleap waveguide 2123040022811304411 / BigscreenVR GTA VI in VR 2122994472913150331 / getVITURE Z-Axis Award 2122956121896022457；media-kol 现为 Dilmerv Meta VR Start competition 2123319106656989445 / SadlyItsBradley gaussian splat 2123281801817051516 / Dilmerv TARGO Emmy quote 2123277400771567792 / Dilmerv VR/MR fun 2123234841676100005 / Dilmerv Meta VR Start submissions 2123208850996109429 / Dilmerv TouchSurface quote 2123186161002934390 / Dilmerv Greg Sphenomenon quote 2123167830585864380 / Dilmerv Japan trip 2123149605218975806）。
- 上一有变更档：2026-11-19 12:00 BJT official +1 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-19 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
