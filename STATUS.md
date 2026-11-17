# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-16 20:05 PST（例行 12:00 BJT 2026-11-17）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 17 Nov 2026 04:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 17 Nov 2026 04:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-17 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：RokidGlobal、nathie、SadlyItsBradley，以及与上轮相同、未再拉时间线的 MetaVR_Official、PICOXR_Dev、htcvive、getVITURE、VRChat、Dilmerv；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2122354254937514257（@officialnucky ok you win this one）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、getVITURE most_recent 仍为回复 2122372163193725429（@MichaelTheGrey_ Thanks for choosing VITURE Pro 2!）、VRChat most_recent 仍为回复 2122386744918028710（@VRChatDropsHub We're checking with Makeship now!）、Dilmerv most_recent 仍为转发 2122432309513335022（转发已入库 2122105069483270207 You don't need VR experience…）（均与上轮相同，未再拉时间线）。RokidGlobal most_recent 为新原创 2122526110198223031（Official Statement: Rokid Glasses 2 Mainland China / Global Version），已拉时间线（exclude 后仅此 1 条）。nathie most_recent 为新回复 2122491224393413090（@gregcroc Would love to do coverage on these and highlight how Snapdragon makes the magic happen!），已拉时间线。SadlyItsBradley most_recent 上轮为转发 2121826216495722626，本轮为新回复 2122517408854229326（@hakimedes HOW DID YOU KNOW），已拉时间线（原创 teaser 2122497980120850807）。
- **official 100→100（+1/−1 cap）：** RokidGlobal Official Statement Rokid Glasses 2 Mainland China Version and Global Version 2122526110198223031。丢掉最旧 1 条：XREAL_Global Hatsune Miku, in your room 2117694188334514440。
- **media-kol 100→100（+1/−1 cap）：** SadlyItsBradley Working on something really crazy 2122497980120850807（teaser，拿不准留下）。丢掉最旧 1 条：nathie light blockers for upcoming Meta VR glasses 2118827306160377980。nathie 排除结果里还有已合成进 2122377254613434769 的 Source 2122377684080787500，未再入。
- top guid 抽查均在（official 现为 RokidGlobal Glasses 2 statement 2122526110198223031 / MetaVRDevs hand onboarding 2122415013310943450 / MetaVRDevs Start Competition 2122390890492944416 / VRChat Guilty Kiss 2122386338687095004 / XREAL_Global New York AURA 2122360095136768057 / RokidGlobal gift book 2122343943870296403 / BeatSaber Play With Us 2122339291300757722 / BeatSaber Flameblade 2122329146915205519；media-kol 现为 SadlyItsBradley crazy teaser 2122497980120850807 / nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780）。
- 上一有变更档：2026-11-17 08:00 BJT official +3 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-17 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
