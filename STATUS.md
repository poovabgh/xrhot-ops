# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-16 04:05 PST（例行 20:00 BJT 2026-11-16）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 16 Nov 2026 12:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 16 Nov 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-16 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：PICOXR_Dev、RokidGlobal、htcvive、getVITURE、MetaVRDevs、nathie、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、XREAL_Global、BeatSaber、pimaxofficial、BigscreenVR、Play_for_dream、magicleap、VRChat、ARealityEvent、Dilmerv）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、getVITURE most_recent 仍为转发 2121752460553547905（@GJX__ Phantom Beast / Platinum）、MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、nathie most_recent 仍为回复 2122083861287071918（@DennisWerth_ @RockstarGames That's so sick! How was it?）、SadlyItsBradley most_recent 仍为转发 2121826216495722626（@gatring3 ハムスターシューター:Hamster Shooter）、RokidGlobal most_recent 仍为转发 2122237244216062180（@Anezium Rokid Nexus v2.6.0）（均与上轮相同，未再拉时间线）。PICOXR_Dev 此前 feed 无条目、上轮 most_recent 为已 cap 的 2115634287437570110；本轮 most_recent 为新串帖 2122242565194105089（自回 2122242336612896857），已拉时间线。
- **official 100→100（+1/−1 cap）：** PICOXR_Dev PICO CLI 0.7.0 / Spatial SDK 6.2.8 / Spatial Toolkit 6.2.x / Unity SDK 6.2.0 / Unreal SDK 6.2.1 串帖合成 2122242336612896857（自回 2122242442355523746 / 2122242516091322462 / 2122242565194105089）。丢掉最旧 1 条：XREAL_Global XREAL 1 Pro+ Gesture Tracking+ 2116863143917899876。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 PICOXR_Dev PICO CLI 0.7.0 串帖 2122242336612896857 / XREAL Hexed Harvest 2122013034847596781 / BeatSaber OST 9 mappers 2122009491839328600 / PICOXR reinstallation 2121996714466852992 / BeatSaber OST 9 Challenge 2121679904466973088 / pimaxofficial IAAPA Expo 2121669127135719497 / BigscreenVR VR Chat setups 2121664463124255159 / XREAL CHZZK XR AURA 2121650572449161274；media-kol 现为 Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207 / nathie Apple smart glasses 2122003944838762897 / Dilmerv HandSkate 2121895188209836160 / Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780 / Dilmerv keep going VR/MR devices 2121763034540474856 / nathie VR scene decade 2121672773257035943）。
- 上一有变更档：2026-11-16 16:00 BJT official 不变 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-17 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
