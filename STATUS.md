# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-15 16:15 PST（例行 08:00 BJT 2026-11-16）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 16 Nov 2026 00:15:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 16 Nov 2026 00:15:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-16 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：XREAL_Global、BeatSaber、htcvive、getVITURE、MetaVRDevs、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、RokidGlobal、Play_for_dream、magicleap、VRChat、pimaxofficial、BigscreenVR、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、getVITURE most_recent 仍为转发 2121752460553547905（@GJX__ Phantom Beast / Platinum）、MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、SadlyItsBradley most_recent 仍为转发 2121826216495722626（@gatring3 ハムスターシューター:Hamster Shooter）（均与上轮相同，未再拉时间线）。XREAL_Global most_recent 为新原创 2122013034847596781（Hexed Harvest / AURA）。BeatSaber most_recent 为新原创 2122009491839328600（OST 9 mappers）。nathie most_recent 为回复 2122083861287071918（@DennisWerth_ @RockstarGames That's so sick! How was it?），已拉时间线。Dilmerv most_recent 为回复 2122105617741664732（@shinoblogavi See you there!），已拉时间线。
- **official 100→100（+2/−2 cap）：** XREAL_Global Hexed Harvest on AURA 2122013034847596781 / BeatSaber Dear OST 9 mappers 2122009491839328600。丢掉最旧 2 条：VRChat Thank you Spookality party 2116758934811738213 / VRChat We're live NOW Spookality Party Zone 2116712353378996648。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv You don't need VR experience to build for Meta VR Glasses 2122105069483270207 / nathie Apple smart glasses visionOS 2122003944838762897（与自我续帖 2122004562768957950 Learn more here! 合成一条，外链换成 https://www.iclarified.com/103539/apple-smart-glasses-prototypes-reportedly-run-visionos-28）。丢掉最旧 2 条：Dilmerv ISDK feature 2118773045976338503 / SadlyItsBradley RAW Framing/Color Grading 2118766214667255991。nathie 对自己已入库投票 2121246381192904761 的回复 2121975282751950856（The results are in!）按回复/串帖续帖丢掉、不改已发出条目。
- top guid 抽查均在（official 现为 XREAL Hexed Harvest 2122013034847596781 / BeatSaber OST 9 mappers 2122009491839328600 / PICOXR reinstallation 2121996714466852992 / BeatSaber OST 9 Challenge 2121679904466973088 / pimaxofficial IAAPA Expo 2121669127135719497 / BigscreenVR VR Chat setups 2121664463124255159 / XREAL CHZZK XR AURA 2121650572449161274 / RokidGlobal Black Friday 2121619174686359624；media-kol 现为 Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780 / Dilmerv keep going VR/MR devices 2121763034540474856 / nathie VR scene decade 2121672773257035943 / SadlyItsBradley Quest games quote 2121618547604672746）。
- 上一有变更档：2026-11-16 00:00 BJT official +1 / media-kol +0。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-16 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
