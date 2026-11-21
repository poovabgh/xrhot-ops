# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-20 20:04 PST（例行 12:00 BJT 2026-11-21）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 21 Nov 2026 00:13:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 21 Nov 2026 04:04:28 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-21 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：MetaVR_Official、nathie、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev、VRChat、Dilmerv；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为转发 2123894448018837561（@VRCharityEvent）。Dilmerv most_recent 仍为转发 2123806135396503860（@devpost Meta VR Start）。MetaVR_Official most_recent 从已入库 2123918298136158415 变为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）；已拉时间线（since_id 2123918298136158415，exclude 后 result_count 0，入库 0）。nathie most_recent 从上轮回复 2123930634351505524 变为 2123945466383753670（You agree? 引用 @PaulTassi）；已拉时间线（since_id 2123860708870021372，exclude 后 result_count 2，入库 1：引用帖 2123945466383753670；另一条为已入库串帖续帖 2123861323024875685，入库 0）。SadlyItsBradley most_recent 从上轮回复 2123892687623328124 变为回复 2123958214416855329（@JoeyGhost They see my avatar, yeah）；已拉时间线（since_id 2123871085892620743，exclude 后 result_count 0，入库 0）。
- **official 100 不变（+0）。**
- **media-kol 100→100（+1/−1 cap）：** nathie You agree? 2123945466383753670（引用 @PaulTassi 2122737867365536191 no offense but I'm not sure we need Best VR Game anymore）。丢掉最旧 1 条：Dilmerv I doubt there are many people out there who spend more time in Unity experimenting with XR than I do. 😆 2119720444798382280。
- top guid 抽查均在（official 仍为 MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875 / pimaxofficial Korea exhibition day 1 2123716020217225505 / VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088 / getVITURE Vice City 2123506093741481991；media-kol 现为 nathie You agree? 2123945466383753670 / SadlyItsBradley toddler CV 2123871085892620743 / nathie vacuum VR 2123860708870021372 / SadlyItsBradley Step two 2123832203306221870 / SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852 / nathie spatial airdrop 2123481440104907056 / SadlyItsBradley decomps quote 2123467399664107864）。
- 上一有变更档：2026-11-21 08:00 BJT official +4（MetaVR_Official LSU 180 / MetaVRDevs Unite Tokyo+November updates / BeatSaber Signal Jammer）；media-kol +3（SadlyItsBradley toddler CV+Step two，nathie vacuum VR）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-21 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
