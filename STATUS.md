# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-19 08:08 PST（例行 00:00 BJT 2026-11-20）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 19 Nov 2026 16:08:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 19 Nov 2026 12:09:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-20 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：PICOXR、RokidGlobal、nathie；与上轮相同、未再拉时间线的：htcvive、PICOXR_Dev、VRChat、BeatSaber；其余等于 watermark 跳过（MetaVR_Official、BigscreenVR、XREAL_Global、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、ARealityEvent、Dilmerv、SadlyItsBradley）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、BeatSaber most_recent 仍为转发 2123377313865933300（RT @logung3d flameblade on Beat Saber OST 9）。PICOXR most_recent 从上轮回复 2123381365328523592 变为新原创 2123446342504587578（copy a pose）；已拉时间线（since_id 2122721567541010603，exclude 后 result_count 1，全部入库：2123446342504587578 If you can copy a pose, you already get the idea，t.co 展开为 https://x.com/PICOXR/status/2123446342504587578/video/1）。RokidGlobal most_recent 从上轮已合成进父帖的自回 2123321967533228282（Deals page）变为新原创 2123431107765186977（Black Friday is live）；已拉时间线（since_id 2123068728716013871，exclude 后 result_count 2：2123431107765186977 入库；2123321967533228282 Deals page 自回已在 16:00 轮合成进父帖 2123068728716013871，不重复入库）。nathie most_recent 从上轮已丢弃的非 VR 游戏/闲聊 2123208524624966068 变为转发 2123411765157302419（RT @nathie Zelda: Ocarina of Time in VR）；已拉时间线（since_id 2122800548990910562，exclude 后 result_count 2，入库 0：2123208524624966068 GTA 6 gaming family 仍为非 VR 游戏/闲聊丢弃；2122803465017606298 Vote here 自回已在先前轮次合成进父帖 2122800548990910562）。
- **official 100→100（+2/−2 cap）：** PICOXR If you can copy a pose, you already get the idea 🕺 2123446342504587578；RokidGlobal Black Friday is live 🖤 Our whole lineup is on sale, with up to 60% off and our lowest prices of the year. 2123431107765186977。丢掉最旧 2 条：XREAL_Global Roll for initiative on your coffee table. Demeo 2118479289142116359 / VRChat It's time for the Nov 5 Developer Update! 2118457400784998664。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 PICOXR copy a pose 2123446342504587578 / RokidGlobal Black Friday is live 2123431107765186977 / pimaxofficial Pimax Play v2.0.5 2123358118721826942 / XREAL_Global AURA Android XR/Gemini 2123260780376428872 / MetaVRDevs Crafting Crimes 2123187217376174242 / getVITURE Beast Tom's Guide 2123136157890253100 / BeatSaber Play With Us live 2123099089004900650 / RokidGlobal Black Friday starts tomorrow 2123068728716013871；media-kol 仍为 Dilmerv VR/MR AI tools 2123348430684586250 / Dilmerv Meta VR Start competition 2123319106656989445 / SadlyItsBradley gaussian splat 2123281801817051516 / Dilmerv TARGO Emmy quote 2123277400771567792 / Dilmerv VR/MR fun 2123234841676100005 / Dilmerv Meta VR Start submissions 2123208850996109429 / Dilmerv TouchSurface quote 2123186161002934390 / Dilmerv Greg Sphenomenon quote 2123167830585864380）。
- 上一有变更档：2026-11-19 20:00 BJT official +1 pimaxofficial Pimax Play v2.0.5 / media-kol +1 Dilmerv VR/MR game AI tools。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-20 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
