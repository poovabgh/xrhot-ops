# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-21 04:06 PST（例行 20:00 BJT 2026-11-21）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 21 Nov 2026 00:13:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 21 Nov 2026 12:06:06 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-21 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：nathie、Dilmerv；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev、VRChat、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为转发 2123894448018837561（@VRCharityEvent）。SadlyItsBradley most_recent 仍为转发 2123993168941375663（@1runeberg Meta jam entry Rift Repair on Vision Pro / OpenXR）。nathie most_recent 从已入库 2123945466383753670 变为回复 2124108210722193740（@DylanMcD8）；已拉时间线（since_id 2123945466383753670，exclude 后 result_count 0，入库 0）。Dilmerv most_recent 从上轮转发 2123806135396503860（@devpost）变为回复 2124107935924256842（@wanchuan918 “Wow” 😉，会话 2123512111540080852）；已拉时间线（since_id 2123512111540080852，exclude 后 result_count 1，入库 1：2124094675485364351）。
- **official 100 不变（+0）。**
- **media-kol 100→100（+1/−1 cap）：** Dilmerv I’ve been discovering so many interesting projects from devs participating in the Meta VR Start Developer Competition! 2124094675485364351（Tejas Shroff 为 Meta VR Glasses 与 Quest 做的 hands-first 交互）。丢掉最旧 1 条：Dilmerv Curious about developing for Meta VR Glasses? 2119833998067163309。
- top guid 抽查均在（official 仍为 MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875 / pimaxofficial Korea exhibition day 1 2123716020217225505 / VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088 / getVITURE Vice City 2123506093741481991；media-kol 现为 Dilmerv Meta VR Start Tejas Shroff 2124094675485364351 / nathie You agree? 2123945466383753670 / SadlyItsBradley toddler CV 2123871085892620743 / nathie vacuum VR 2123860708870021372 / SadlyItsBradley Step two 2123832203306221870 / SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852 / nathie spatial airdrop 2123481440104907056）。
- 上一有变更档：2026-11-21 12:00 BJT media-kol +1（nathie You agree? 引用 @PaulTassi Best VR Game）；16:00 BJT 无变更未提交。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-22 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
