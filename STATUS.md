# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-16 08:09 PST（例行 00:00 BJT 2026-11-17）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 16 Nov 2026 16:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 16 Nov 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-17 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：XREAL_Global、BeatSaber、RokidGlobal、MetaVR_Official、Dilmerv、PICOXR_Dev、htcvive、getVITURE、MetaVRDevs、nathie、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、pimaxofficial、Play_for_dream、magicleap、VRChat、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、getVITURE most_recent 仍为转发 2121752460553547905（@GJX__ Phantom Beast / Platinum）、MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、nathie most_recent 仍为回复 2122083861287071918（@DennisWerth_ @RockstarGames That's so sick! How was it?）、SadlyItsBradley most_recent 仍为转发 2121826216495722626（@gatring3 ハムスターシューター:Hamster Shooter）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）（均与上轮相同，未再拉时间线）。XREAL_Global most_recent 为新原创 2122360095136768057（New York got hands-on with XREAL AURA），已拉时间线。BeatSaber most_recent 为新原创 2122339291300757722（Play With Us is back），已拉时间线（另有 Flameblade 2122329146915205519）。RokidGlobal most_recent 上轮为转发 2122237244216062180，本轮为新原创 2122343943870296403（Rokid AR Spatial gift book），已拉时间线。MetaVR_Official most_recent 为回复 2122354254937514257（@officialnucky ok you win this one），exclude 后 result_count 0。Dilmerv most_recent 为回复 2122325297932685598（@_JoshuaTimothy Awesome! What are you thinking of building?），exclude 后 result_count 0。
- **official 100→100（+4/−4 cap）：** XREAL_Global New York hands-on with XREAL AURA 2122360095136768057；RokidGlobal Rokid AR Spatial gift book 2122343943870296403；BeatSaber Play With Us 2122339291300757722；BeatSaber Flameblade 2122329146915205519。丢掉最旧 4 条：MetaVRDevs Quest 2/Pro final OS 2117332750395232649 / RokidGlobal Ocean below 2117270520253095949 / XREAL_Global XREAL 1 Pro+ Amazon 2117240872991342991 / PICOXR Cave Crave 2116923341713858877。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 XREAL_Global New York AURA 2122360095136768057 / RokidGlobal gift book 2122343943870296403 / BeatSaber Play With Us 2122339291300757722 / BeatSaber Flameblade 2122329146915205519 / PICOXR_Dev PICO CLI 0.7.0 串帖 2122242336612896857 / XREAL Hexed Harvest 2122013034847596781 / BeatSaber OST 9 mappers 2122009491839328600 / PICOXR reinstallation 2121996714466852992；media-kol 现为 Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780 / Dilmerv keep going VR/MR devices 2121763034540474856 / nathie VR scene decade 2121672773257035943）。
- 上一有变更档：2026-11-16 20:00 BJT official +1 / media-kol 不变。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-17 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
