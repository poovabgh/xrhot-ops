# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-14 16:10 PST（例行 08:00 BJT 2026-11-15）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 15 Nov 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 15 Nov 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-15 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：BigscreenVR、XREAL_Global、getVITURE、pimaxofficial、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、RokidGlobal、Play_for_dream、magicleap、VRChat、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106、MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936（均与上轮相同，未再拉时间线）。getVITURE most_recent 为转发 2121752460553547905（@GJX__ Phantom Beast / Platinum），exclude 后 result_count 0。Dilmerv most_recent 为转发自己的 2121731583963230484（已入库 AI XR workflows poll 2121419120281583758），exclude 后 result_count 0。SadlyItsBradley most_recent 为转发 2121664634549657893（@BigscreenVR setups），exclude 后 result_count 0。nathie most_recent 为回复 2121733425681858846（@arithmoquine Incredible!），exclude 后另有 1 条原创。pimaxofficial 时间线还返回已合并进根帖 2121055807618101380 的 English 续帖 2121055811359347064，跳过。
- **official 100→100（+4/−4 cap）：** BeatSaber OST 9 Challenge 2121679904466973088；pimaxofficial IAAPA Expo 2026 Orlando 2121669127135719497；BigscreenVR Full Time VR Chat User setups 2121664463124255159；XREAL_Global CHZZK XR / AURA streams 2121650572449161274。丢掉最旧 4 条：Play_for_dream Halloween hits different in VR 2116575935931760782；XREAL_Global Words you can walk around 2116576597880746022；VRChat Spookality Party Zone 2116624232255983762；BeatSaber Happy Halloween 2116626332566032759。
- **media-kol 100→100（+1/−1 cap）：** nathie YouTube channel from 10 years ago / VR scene decade 2121672773257035943。丢掉最旧 1 条：nathie What’s going on with VRChat? Steam reviews 2118484164303605977。
- top guid 抽查均在（official 现为 BeatSaber OST 9 Challenge 2121679904466973088 / pimaxofficial IAAPA Expo 2121669127135719497 / BigscreenVR VR Chat setups 2121664463124255159 / XREAL CHZZK XR AURA 2121650572449161274 / RokidGlobal Black Friday 2121619174686359624 / VRChat Virtual Dice Party 2121617840956719115 / XREAL AURA Founder Editions 2121472555395756506 / VRChat Osaka trophy 2121407670821261813；media-kol 现为 nathie VR scene decade 2121672773257035943 / SadlyItsBradley Quest games quote 2121618547604672746 / Dilmerv Meta VR Glasses perspectives 2121499633079787732 / Dilmerv Meta VR Glasses 2121430048804585886 / Dilmerv AI XR workflows 2121419120281583758 / Dilmerv love XR MR conversions 2121416659160248770 / nathie Razer haptic chair 2121383921552416861 / Dilmerv TapeDeck Hand Skate 2121299006085091438）。
- 上一有变更档：2026-11-15 00:00 BJT official +2 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-15 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
