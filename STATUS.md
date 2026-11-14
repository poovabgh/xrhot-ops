# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-14 04:12 PST（例行 20:00 BJT 2026-11-14）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 14 Nov 2026 12:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 14 Nov 2026 08:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-14 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVRDevs、htcvive、pimaxofficial、VRChat、nathie、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、Play_for_dream、magicleap、BeatSaber、ARealityEvent、Dilmerv）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、htcvive most_recent 仍为转发 2118069208126747106、pimaxofficial most_recent 仍为已入库 2121055807618101380（G-STAR 2026 Busan）的 English 续帖 2121055811359347064、nathie most_recent 仍为转发 2121433435462070632、SadlyItsBradley most_recent 仍为转发 2121108845624000546（均与上轮相同，未再拉时间线）。VRChat most_recent 仍为 2121407670821261813（Who's lifting the trophy in Osaka?）；前两轮因 get_users_posts since_id + exclude 后 result_count 0、时间线/搜索也不返回该 id 未入库。本轮按 id 复核：conversation_id 等于帖子 id、无 in_reply_to / referenced_posts，是原创而非回复或转发；公开可见（约 355 万展示、251 赞）；正文讲在 VRChat 看大阪季后赛，属 XR；唯一回复来自 chyadosensei，非官方续帖。本轮入库。时间线与 search 仍不返回该 id。
- **official 100→100（+1/−1 cap）：** VRChat Who's lifting the trophy in Osaka? 2121407670821261813。丢掉最旧 1 条：pimaxofficial The Dream Air front plates 2116435495827673341。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 XREAL AURA Founder Editions 2121472555395756506 / VRChat Osaka trophy 2121407670821261813 / BigscreenVR still flying 2121367890809229370 / getVITURE Pro 2 Amazon 2121362184106385433 / MetaVR Celtics highlights 2121347262102265922 / BeatSaber Confetti LFG 2121308812963438930 / MetaVRDevs release notes 2121305089449308635 / MetaVR longest drive 2121289448939987427；media-kol 仍为 Dilmerv Meta VR Glasses perspectives 2121499633079787732 / Dilmerv Meta VR Glasses 2121430048804585886 / Dilmerv AI XR workflows 2121419120281583758 / Dilmerv love XR MR conversions 2121416659160248770 / nathie Razer haptic chair 2121383921552416861 / Dilmerv TapeDeck Hand Skate 2121299006085091438 / nathie Gentle Monster first look 2121297122897305604）。
- 上一有变更档：2026-11-14 16:00 BJT official +1 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-15 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
