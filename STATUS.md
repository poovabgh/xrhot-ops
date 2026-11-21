# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-21 08:08 PST（例行 00:00 BJT 2026-11-22）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 21 Nov 2026 16:08:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 21 Nov 2026 16:08:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-22 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：RokidGlobal、nathie、Dilmerv；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev、VRChat、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、getVITURE、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为转发 2123894448018837561（@VRCharityEvent）。SadlyItsBradley most_recent 仍为转发 2123993168941375663（@1runeberg Meta jam entry Rift Repair on Vision Pro / OpenXR）。RokidGlobal most_recent 从已入库 2123431107765186977 变为原创 2124155883684859968；已拉时间线（since_id 2123431107765186977，exclude 后 result_count 1，入库 1）。nathie most_recent 从上轮回复 2124108210722193740（@DylanMcD8）变为引用 2124151464733835739（@SirDunkaREAL）；已拉时间线（since_id 2123945466383753670，exclude 后 result_count 1，入库 1）。Dilmerv most_recent 从上轮回复 2124107935924256842（@wanchuan918）变为回复 2124126338294730924（@hermes_f “I agree!”，会话 2124094675485364351）；已拉时间线（since_id 2124094675485364351，exclude 后 result_count 0，入库 0）。
- **official 100→100（+1/−1 cap）：** RokidGlobal Family wanted the TV tonight. 2124155883684859968（GTA VI on Rokid Max 2）。丢掉最旧 1 条：XREAL_Global Explore the world in 3D. 2119143981422362899。
- **media-kol 100→100（+1/−1 cap）：** nathie People already got a sneak peek at a potential first-person VR mod without even knowing it. 2124151464733835739（引用 @SirDunkaREAL 第一人称 glitch）。丢掉最旧 1 条：Dilmerv Really excited about Unity 7! 2119852941209489491。
- top guid 抽查均在（official 现为 RokidGlobal GTA VI on Rokid Max 2 2124155883684859968 / MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875 / pimaxofficial Korea exhibition day 1 2123716020217225505 / VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088；media-kol 现为 nathie first-person VR mod 2124151464733835739 / Dilmerv Meta VR Start Tejas Shroff 2124094675485364351 / nathie You agree? 2123945466383753670 / SadlyItsBradley toddler CV 2123871085892620743 / nathie vacuum VR 2123860708870021372 / SadlyItsBradley Step two 2123832203306221870 / SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852）。
- 上一有变更档：2026-11-21 20:00 BJT media-kol +1（Dilmerv Meta VR Start Tejas Shroff）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-22 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
