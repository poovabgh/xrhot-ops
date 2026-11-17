# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-17 08:05 PST（例行 00:00 BJT 2026-11-18）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 17 Nov 2026 16:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 17 Nov 2026 16:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-18 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：PICOXR、XREAL_Global、getVITURE、pimaxofficial、BeatSaber、ARealityEvent、nathie、Dilmerv；与上轮相同、未再拉时间线的：MetaVR_Official、PICOXR_Dev、htcvive、VRChat、SadlyItsBradley；其余等于 watermark 跳过（MetaVRDevs、BigscreenVR、RokidGlobal、Play_for_dream、magicleap）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2122354254937514257（@officialnucky ok you win this one）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、VRChat most_recent 仍为回复 2122386744918028710（@VRChatDropsHub We're checking with Makeship now!）、SadlyItsBradley most_recent 仍为回复 2122517408854229326（@hakimedes HOW DID YOU KNOW）（均与 20:00 BJT 轮相同，未再拉时间线）。PICOXR most_recent 为新原创 2122721567541010603（Start the recording, make your move, save the moment），已拉时间线（exclude 后 1 条，入库）。XREAL_Global most_recent 为新原创 2122691780453793834（Get More Out of XREAL AURA with These Power User Tips），已拉时间线（exclude 后 1 条，入库全文 note_tweet）。getVITURE most_recent 从上轮回复 2122372163193725429 变为新原创 2122721454538047499（VITURE x @mygamesir #PhantomBladeZero giveaway），已拉时间线（since_id 2121362184106385433，exclude 后 1 条，入库全文 note_tweet；most_recent 仍为该原帖，1 条回复非本人串帖）。pimaxofficial most_recent 为新原创 2122677383610442099（Progress Update November 17th），已拉时间线（exclude 后 1 条，入库）。BeatSaber most_recent 为新原创 2122688191996260724（REMINDER: Play With Us TOMORROW），已拉时间线（exclude 后 1 条，入库；与已入库公告 2122339291300757722 非同一帖）。ARealityEvent most_recent 为新原创 2122721508086976575（Ori Inbar SPAI / AWE 2027），已拉时间线（exclude 后 1 条，入库）。nathie most_recent 从上轮回复 2122491224393413090 变为新原创 2122699884767957370（Gentle Monster smart glasses short film），已拉时间线（exclude 后 result_count 2：该新帖入库；2122377684080787500 Source 已合成进 Zelda 条目 2122377254613434769，不重加）。Dilmerv most_recent 从 20:00 BJT 轮的自转 2122623875272085640 变为回复 2122718654886551842（@uralstechCTO Thank you 🤗），已拉时间线（since_id 2122200536132821374，exclude 后 result_count 4，全部作旅行/生活/生病丢弃：新帖 2122708107696775518 因病离开 Unite Tokyo、自回 2122709091772743684 Uber 买药；以及与上轮相同的 2122547349235065070 It was so great meeting you!、2122415118827024888 Stopped by the Unity venue yesterday…）。
- **official 100→100（+5/−5 cap）：** PICOXR Start the recording, make your move, save the moment. ✨ 2122721567541010603；getVITURE Every great fight needs the right gear.（VITURE x GameSir Phantom Blade Zero giveaway）2122721454538047499；XREAL_Global Get More Out of XREAL AURA with These Power User Tips 👓 2122691780453793834；BeatSaber REMINDER: Play With Us TOMORROW! 🎮 2122688191996260724；pimaxofficial Progress Update November 17th: IAAPA Expo 2026, CES 2027, Black Friday Deal, and more. 2122677383610442099。丢掉最旧 5 条：magicleap Strong software plays a key role in great AR hardware. 2118040616437186963、Play_for_dream VR brings people into virtual worlds. 2118040585692995709、htcvive At the TTSWTRS SS27 show… 2118007232801526009、RokidGlobal You know it’s a good song… 2117995284945158270、VRChat #ICYMI - The Winners Showcase… 2117754653060334010。其中 htcvive 在 official feed 已无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+2/−2 cap）：** ARealityEvent In 2020, Ori Inbar “traveled back from 2030”… SPAI / AWE 2027 2122721508086976575；nathie Gentle Monster just dropped a short film starring Joaquin Phoenix to show off its new smart glasses. 2122699884767957370。丢掉最旧 2 条：Dilmerv Excited to keep working on my new tabletop skating game in MR this weekend! 2118846537744716044、SadlyItsBradley Uhhhh turns out that I’m going to be in town for this 2118840191947268503。
- top guid 抽查均在（official 现为 PICOXR recording 2122721567541010603 / getVITURE Phantom Blade giveaway 2122721454538047499 / XREAL_Global AURA tips 2122691780453793834 / BeatSaber Play With Us reminder 2122688191996260724 / pimaxofficial Nov 17 update 2122677383610442099 / XREAL_Global AURA Founder’s Edition shipping 2122661911804129485 / RokidGlobal Glasses 2 statement 2122526110198223031 / MetaVRDevs hand onboarding 2122415013310943450；media-kol 现为 ARealityEvent SPAI AWE 2027 2122721508086976575 / nathie Gentle Monster glasses 2122699884767957370 / SadlyItsBradley crazy teaser 2122497980120850807 / nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160）。
- 上一有变更档：2026-11-17 20:00 BJT official +1 / media-kol 不变。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-18 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
