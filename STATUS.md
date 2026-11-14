# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-13 16:12 PST（例行 08:00 BJT 2026-11-14）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 14 Nov 2026 00:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 14 Nov 2026 00:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-14 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、MetaVRDevs、htcvive、BigscreenVR、XREAL_Global、getVITURE、pimaxofficial、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、RokidGlobal、Play_for_dream、magicleap、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106、pimaxofficial most_recent 仍为已入库 2121055807618101380（G-STAR 2026 Busan）的 English 续帖 2121055811359347064、SadlyItsBradley most_recent 仍为转发 2121108845624000546（均与上轮相同，未再拉时间线）。
- **official 100→100（+7/−7 cap）：** BigscreenVR idk about you but we're still flying 2121367890809229370；getVITURE Sweeping #1 / VITURE Pro 2 Amazon 2121362184106385433；MetaVR_Official Celtics vs 76ers immersive highlights 2121347262102265922；BeatSaber Confetti LFG 2121308812963438930；MetaVRDevs Fresh release notes / v209 SDK 线程合并 2121305089449308635；MetaVR_Official What’s your longest drive 2121289448939987427（自回 2121289680423637189 已合成）；XREAL_Global Godot Engine 4 on XREAL AURA 2121288436569063868。丢掉最旧 7 条：MetaVR_Official Some scares end with the credits 2116330178683314619 / getVITURE A legend forged in shadow 2116263369808253157 / MetaVR_Official Front-row energy Florida vs Georgia 2116231178164560223 / BeatSaber Last call for the Fall Sale 2116230227739181431 / RokidGlobal Thanks for following along 2116201780778586270 / PICOXR How to God 2116183610386509978 / RokidGlobal Hi Rokiders 2116183344056832166。MetaVR_Official 2120973071490453795 为已入库 2120947398851912120（Winter’s coming）的续帖，未改已发出条目。VRChat exclude 后 result_count 0（most_recent 2121326804854300681 为回复）。
- **media-kol 100→100（+3/−3 cap）：** nathie Razer haptic gaming chair / VR games 2121383921552416861；Dilmerv TapeDeck in Meta VR CLI / Hand Skate 2121299006085091438；nathie Gentle Monster smart glasses first look 2121297122897305604。丢掉最旧 3 条：Dilmerv Meta VR Start Developer Competition 2118335116887863461 / nathie Zelda first-person VR 2118316089738469467 / Dilmerv AI coding agents 2118289756500984279。Dilmerv 另 5 条初筛丢掉（非 XR）：iPhone Duo 2121303442874564938、Mac Studio from the airplane 2121300843093971063，以及上轮已丢的 resume / AI coding tools 2121268410646433860、50.5K followers 2121265204059377776、coding fundamentals vs AI agents 2121247813157757301。Dilmerv most_recent 2121340842447430101 为回复。
- top guid 抽查均在（official 现为 BigscreenVR still flying 2121367890809229370 / getVITURE Pro 2 Amazon 2121362184106385433 / MetaVR Celtics highlights 2121347262102265922 / BeatSaber Confetti LFG 2121308812963438930 / MetaVRDevs release notes 2121305089449308635 / MetaVR longest drive 2121289448939987427 / XREAL Godot AURA 2121288436569063868；media-kol 现为 nathie Razer haptic chair 2121383921552416861 / Dilmerv TapeDeck Hand Skate 2121299006085091438 / nathie Gentle Monster first look 2121297122897305604 / nathie Aura vs Meta VR Glasses 2121246381192904761 / Dilmerv Unite Tokyo 2121233793038135521 / ARealityEvent AWE launches phaiworld 2121141198962467113）。
- 上一有变更档：2026-11-14 00:00 BJT official +3 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-14 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
