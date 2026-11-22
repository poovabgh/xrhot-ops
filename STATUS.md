# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-21 16:08 PST（例行 08:00 BJT 2026-11-22）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 22 Nov 2026 00:09:18 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 22 Nov 2026 00:09:18 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-22 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、MetaVRDevs、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 从上轮转发 2123894448018837561（@VRCharityEvent）变为原创 2124249109003747407；已拉时间线（since_id 2123549256321781884，exclude 后 result_count 2，其中自回 2123549260000248096 已合成进 Nov 19 Dev Update 2123549256321781884，入库 1）。BeatSaber most_recent 从已入库 2123847813150691377 变为原创 2124218919296659517；已拉时间线（since_id 2123847813150691377，exclude 后 result_count 1，入库 1）。nathie most_recent 从已入库引用 2124151464733835739 变为自回 2124257850876711299（Source 链到 Reddit）；已拉时间线（since_id 2124151464733835739，exclude 后 result_count 2，合成 1：根帖 2124257333731786887 + 自回，入库 1）。Dilmerv most_recent 从上轮回复 2124126338294730924（@hermes_f）变为回复 2124269344578486386（@LordsiVR @AlienDogStudios “Thanks for sharing your submission! Looks very fun!”，会话 2124239952581919229）；已拉时间线（since_id 2124094675485364351，exclude 后 result_count 1，入库 1）。SadlyItsBradley most_recent 从上轮转发 2123993168941375663（@1runeberg）变为转发 2124288882531283034（@BlenderStudio_ DOGWALK visionOS / WWDC26 2124141948554404051）；已拉时间线（since_id 2123871085892620743，exclude 后 result_count 0，入库 0）。
- **official 100→100（+2/−2 cap）：** VRChat Early on November 21 JST, while responding to a serious policy violation… 2124249109003747407（误封账号已解禁致歉）；BeatSaber 🐈 "Purr" by @azazalmeow… 2124218919296659517（OST 9 免费）。丢掉最旧 2 条：XREAL_Global Let your sock sing its heart out 2119173637726978097；RokidGlobal Rokid glasses on, language barrier off 2119412737294164390。
- **media-kol 100→100（+2/−2 cap）：** nathie This Zelda: Ocarina of Time VR mod looks absolutely insane. 2124257333731786887（合成自回 Source Reddit）；Dilmerv XR devs, here’s a small test worth trying with your next demo! 👇 2124239952581919229。丢掉最旧 2 条：nathie Every time I put on my Apple Vision Pro it feels like stepping into a holodeck. 2119864306376589352；SadlyItsBradley This weekend I finally added an edit mode to my Splattery App with some whimsy! 2119866605794382181。
- top guid 抽查均在（official 现为 VRChat ban apology 2124249109003747407 / BeatSaber Purr OST 9 2124218919296659517 / RokidGlobal GTA VI on Rokid Max 2 2124155883684859968 / MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875 / pimaxofficial Korea exhibition day 1 2123716020217225505；media-kol 现为 nathie Zelda OoT VR mod 2124257333731786887 / Dilmerv XR demo test 2124239952581919229 / nathie first-person VR mod 2124151464733835739 / Dilmerv Meta VR Start Tejas Shroff 2124094675485364351 / nathie You agree? 2123945466383753670 / SadlyItsBradley toddler CV 2123871085892620743 / nathie vacuum VR 2123860708870021372 / SadlyItsBradley Step two 2123832203306221870）。
- 上一有变更档：2026-11-22 00:00 BJT official +1（RokidGlobal GTA VI on Rokid Max 2）+ media-kol +1（nathie first-person VR mod quote）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-22 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
