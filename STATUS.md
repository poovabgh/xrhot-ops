# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-17 04:11 PST（例行 20:00 BJT 2026-11-17）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 17 Nov 2026 12:11:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 17 Nov 2026 04:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-17 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：XREAL_Global、Dilmerv，以及与上轮相同、未再拉时间线的 MetaVR_Official、PICOXR_Dev、htcvive、getVITURE、VRChat、nathie、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、RokidGlobal、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2122354254937514257（@officialnucky ok you win this one）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、getVITURE most_recent 仍为回复 2122372163193725429（@MichaelTheGrey_ Thanks for choosing VITURE Pro 2!）、VRChat most_recent 仍为回复 2122386744918028710（@VRChatDropsHub We're checking with Makeship now!）、nathie most_recent 仍为回复 2122491224393413090（@gregcroc Would love to do coverage on these and highlight how Snapdragon makes the magic happen!）、SadlyItsBradley most_recent 仍为回复 2122517408854229326（@hakimedes HOW DID YOU KNOW）（均与 16:00 BJT 轮相同，未再拉时间线）。XREAL_Global most_recent 为新原创 2122661911804129485（XREAL AURA Founder’s Edition is officially shipping），已拉时间线（exclude 后仅此 1 条，入库）。Dilmerv most_recent 从 16:00 BJT 轮的转发 2122595385625686501 变为新转发 2122623875272085640（自转已入库 2121430048804585886 Personal take: Most XR developers…），已拉时间线（since_id 2122200536132821374，exclude 后 result_count 2，两条与 16:00 轮相同、仍作旅行/生活丢弃：2122547349235065070 It was so great meeting you!、2122415118827024888 Stopped by the Unity venue yesterday…）。16:00 BJT 轮官方/媒体均无变更、未 commit。
- **official 100→100（+1/−1 cap）：** XREAL_Global The future you saw first is now on its way. ✨（AURA Founder’s Edition officially shipping）2122661911804129485。丢掉最旧 1 条：XREAL_Global Strap in without leaving your seat. 2117724672020087075。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 XREAL_Global AURA Founder’s Edition shipping 2122661911804129485 / RokidGlobal Glasses 2 statement 2122526110198223031 / MetaVRDevs hand onboarding 2122415013310943450 / MetaVRDevs Start Competition 2122390890492944416 / VRChat Guilty Kiss 2122386338687095004 / XREAL_Global New York AURA 2122360095136768057 / RokidGlobal gift book 2122343943870296403 / BeatSaber Play With Us 2122339291300757722；media-kol 现为 SadlyItsBradley crazy teaser 2122497980120850807 / nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780）。
- 上一有变更档：2026-11-17 12:00 BJT official +1 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-18 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
