# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-15 00:07 PST（例行 16:00 BJT 2026-11-15）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 15 Nov 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 15 Nov 2026 08:07:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-15 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：getVITURE、htcvive、MetaVRDevs、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、RokidGlobal、Play_for_dream、magicleap、VRChat、BeatSaber、pimaxofficial、BigscreenVR、XREAL_Global、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106、MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、getVITURE most_recent 仍为转发 2121752460553547905（@GJX__ Phantom Beast / Platinum）、nathie most_recent 仍为回复 2121733425681858846（@arithmoquine Incredible!）（均与上轮相同，未再拉时间线）。Dilmerv most_recent 为新原创 2121875874534318111。SadlyItsBradley most_recent 从上轮转发 2121664634549657893 变为转发 2121826216495722626（@gatring3 ハムスターシューター:Hamster Shooter）；exclude 后 result_count=0，无新原创入库。
- **official 100 不变（+0）：** 无新原创入库。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv I don’t know if I ever shared these photos… Meta Connect live demo rehearsal 2121857936418889905；Dilmerv To everyone spending countless hours… being an XR developer so special 2121854138447167780。丢掉最旧 2 条：ARealityEvent Google XR Blocks / Raven Resonance 2118630123801035214、Dilmerv Here’s how the hand interactions work so far in “Hand Skate” 2118583354283217102。丢掉 Dilmerv 新原创 There’s something I think about a lot / sharing my work 2121875874534318111（无 XR 内容，按规则作非 XR 闲聊/励志）。
- top guid 抽查均在（official 仍为 BeatSaber OST 9 Challenge 2121679904466973088 / pimaxofficial IAAPA Expo 2121669127135719497 / BigscreenVR VR Chat setups 2121664463124255159 / XREAL CHZZK XR AURA 2121650572449161274 / RokidGlobal Black Friday 2121619174686359624 / VRChat Virtual Dice Party 2121617840956719115 / XREAL AURA Founder Editions 2121472555395756506 / VRChat Osaka trophy 2121407670821261813；media-kol 现为 Dilmerv Meta Connect rehearsal 2121857936418889905 / Dilmerv XR developer unreleased devices 2121854138447167780 / Dilmerv keep going VR/MR devices 2121763034540474856 / nathie VR scene decade 2121672773257035943 / SadlyItsBradley Quest games quote 2121618547604672746 / Dilmerv Meta VR Glasses perspectives 2121499633079787732 / Dilmerv Meta VR Glasses 2121430048804585886 / Dilmerv AI XR workflows 2121419120281583758）。
- 上一有变更档：2026-11-15 12:00 BJT official +0 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-15 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
