# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-13 20:03 PST（例行 12:00 BJT 2026-11-14）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 14 Nov 2026 00:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 14 Nov 2026 04:03:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-14 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVRDevs、htcvive、pimaxofficial、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、Play_for_dream、magicleap、BeatSaber、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106、pimaxofficial most_recent 仍为已入库 2121055807618101380（G-STAR 2026 Busan）的 English 续帖 2121055811359347064、SadlyItsBradley most_recent 仍为转发 2121108845624000546（均与上轮相同，未再拉时间线）。
- **official 100 不变（+0）：** MetaVRDevs most_recent 2121306015765499936 为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的 2/–5/ 续帖，未改已发出条目。VRChat most_recent 2121407670821261813（Who's lifting the trophy in Osaka? / @R6Esports）按 id 可取到且看似独立原帖，但 get_users_posts（含/不含 exclude）与 from:VRChat 搜索均未出现在用户时间线（时间线最新仍为转发 2121306236696355027），since_id exclude 后 result_count 0，未入库。
- **media-kol 100→100（+3/−3 cap）：** Dilmerv Personal take / Meta VR Glasses 2121430048804585886；Dilmerv AI tools in XR workflows 投票 2121419120281583758；Dilmerv I honestly can’t imagine doing anything else / iOS games to MR 2121416659160248770。丢掉最旧 3 条：nathie This terrifying Meta Quest app 2118443855779615149 / Dilmerv Cubiques is NOW AVAILABLE 2118384006245003336 / Dilmerv Best feeling in the world! 2118350458204864968。Dilmerv 另丢掉：旅行/FAA 2121405121452212358（非 XR），以及上轮已丢的 iPhone Duo 2121303442874564938、Mac Studio from the airplane 2121300843093971063。nathie most_recent 2121433435462070632 为转发，exclude 后 result_count 0。Dilmerv most_recent 2121446438697947327 为回复。
- top guid 抽查均在（official 仍为 BigscreenVR still flying 2121367890809229370 / getVITURE Pro 2 Amazon 2121362184106385433 / MetaVR Celtics highlights 2121347262102265922 / BeatSaber Confetti LFG 2121308812963438930 / MetaVRDevs release notes 2121305089449308635 / MetaVR longest drive 2121289448939987427 / XREAL Godot AURA 2121288436569063868；media-kol 现为 Dilmerv Meta VR Glasses 2121430048804585886 / Dilmerv AI XR workflows 2121419120281583758 / Dilmerv love XR MR conversions 2121416659160248770 / nathie Razer haptic chair 2121383921552416861 / Dilmerv TapeDeck Hand Skate 2121299006085091438 / nathie Gentle Monster first look 2121297122897305604）。
- 上一有变更档：2026-11-14 08:00 BJT official +7 / media-kol +3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-14 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
