# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-16 16:06 PST（例行 08:00 BJT 2026-11-17）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 17 Nov 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 17 Nov 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-17 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、MetaVRDevs、PICOXR_Dev、htcvive、getVITURE、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、pimaxofficial、Play_for_dream、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2122354254937514257（@officialnucky ok you win this one）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、SadlyItsBradley most_recent 仍为转发 2121826216495722626（@gatring3 ハムスターシューター:Hamster Shooter）（均与上轮相同，未再拉时间线）。MetaVRDevs most_recent 为新原创 2122415013310943450（hand controls onboarding guide），已拉时间线（另有 Start Developer Competition 2122390890492944416；排除里还带回已入库 v209 串帖续帖，未再入）。getVITURE most_recent 上轮为转发 2121752460553547905，本轮为新回复 2122372163193725429（@MichaelTheGrey_ Thanks for choosing VITURE Pro 2!），exclude 后 result_count 0。VRChat most_recent 为回复 2122386744918028710（@VRChatDropsHub We're checking with Makeship now!），已拉时间线（原创 Guilty Kiss bundle 2122386338687095004）。nathie most_recent 为回复 2122427548474691773（@GAMERTAGVR irl superhero），已拉时间线。Dilmerv most_recent 为转发 2122432309513335022（转发已入库 2122105069483270207 You don't need VR experience…），已拉时间线。
- **official 100→100（+3/−3 cap）：** MetaVRDevs hand controls onboarding guide 2122415013310943450；MetaVRDevs Meta VR Start Developer Competition 2122390890492944416；VRChat Guilty Kiss Musical Performance bundle 2122386338687095004。丢掉最旧 3 条：XREAL_Global Beyond the screen 2117633946124968444 / RokidGlobal Creator Partner Program 2117632899730030748 / getVITURE PCMag Best Smart Glasses 2117343081527988417。
- **media-kol 100→100（+1/−1 cap）：** nathie Zelda: Ocarina of Time in VR 2122377254613434769（与自回 Source 2122377684080787500 合成）。丢掉最旧 1 条：Dilmerv Congrats to @tovanbo 2118815372816384206。丢掉 Dilmerv Unity venue prep 2122415118827024888（travel/life，同上轮 Tokyo walk / Made it to Japan）。nathie 排除结果里还有已合成进 2122003944838762897 的 Learn more here! 2122004562768957950，未再入。
- top guid 抽查均在（official 现为 MetaVRDevs hand onboarding 2122415013310943450 / MetaVRDevs Start Competition 2122390890492944416 / VRChat Guilty Kiss 2122386338687095004 / XREAL_Global New York AURA 2122360095136768057 / RokidGlobal gift book 2122343943870296403 / BeatSaber Play With Us 2122339291300757722 / BeatSaber Flameblade 2122329146915205519 / PICOXR_Dev PICO CLI 0.7.0 串帖 2122242336612896857；media-kol 现为 nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780 / Dilmerv keep going VR/MR devices 2121763034540474856）。
- 上一有变更档：2026-11-17 00:00 BJT official +4 / media-kol 不变。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-17 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
