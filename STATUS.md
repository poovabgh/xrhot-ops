# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-20 16:13 PST（例行 08:00 BJT 2026-11-21）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 21 Nov 2026 00:13:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 21 Nov 2026 00:13:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-21 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：MetaVR_Official、MetaVRDevs、VRChat、BeatSaber、nathie、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev、Dilmerv；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。Dilmerv most_recent 仍为转发 2123806135396503860（@devpost Meta VR Start；00:00 BJT 已拉，exclude 后 0）。MetaVR_Official most_recent 从上轮已入库 2122828030414668144 变为新原创 2123918298136158415（LSU Tigers vs Tennessee 180° sideline）；已拉时间线（since_id 2122828030414668144，exclude 后 result_count 1，入库 1）。MetaVRDevs most_recent 变为 2123899966762668519（Unite Tokyo Meta VR Glasses）；已拉时间线（since_id 2123187217376174242，exclude 后 result_count 5，入库 2：Unite Tokyo 原创 2123899966762668519；November updates 父帖 2123846165892583875 合成自回 2123846231290171696 / 2123846295089774970 / 2123846341390639417）。VRChat most_recent 变为转发 2123894448018837561（@VRCharityEvent）；已拉时间线（since_id 2123549256321781884，exclude 后 result_count 1，为已入库串帖续帖 2123549260000248096，入库 0）。BeatSaber most_recent 变为 2123847813150691377（Signal Jammer by @EEWK_）；已拉时间线（since_id 2123521746145866088，exclude 后 result_count 1，入库 1）。nathie most_recent 变为回复 2123930634351505524（@EinarJohnson_XR）；已拉时间线（since_id 2123481440104907056，exclude 后 result_count 2，合成 1 条入库：父帖 2123860708870021372 This VR app turns vacuuming into a video game，续帖 2123861323024875685 Check out the game here Dusty）。SadlyItsBradley most_recent 变为回复 2123892687623328124（@CyborgLavery）；已拉时间线（since_id 2123534916025511973，exclude 后 result_count 2，入库 2：toddler CV tree 2123871085892620743 / Step two 2123832203306221870 引用自己的 2122983246816325717）。
- **official 100→100（+4/−4 cap）：** MetaVR_Official LSU vs Tennessee 180° sideline 2123918298136158415；MetaVRDevs At Unite Tokyo… Meta VR Glasses 2123899966762668519；BeatSaber Signal Jammer 2123847813150691377；MetaVRDevs More November updates 🎁 2123846165892583875（合成自回 Core SDK / Interaction SDK / Meta Quest Browser）。丢掉最旧 4 条：XREAL_Global Front row, from your living room. 2119113739777487009；VRChat 🎲 Virtual Dice Party 2026 is now open in VRChat! 2119082451100205331；XREAL_Global Cast your line anywhere. 2118811392945824160；XREAL_Global Pull up a seat, the board is already on your table. 2118781280980537391。
- **media-kol 100→100（+3/−3 cap）：** SadlyItsBradley toddler CV Christmas tree lights 2123871085892620743；nathie This VR app turns vacuuming into a video game 2123860708870021372（合成自回 Dusty: Mixed Reality Cleaning）；SadlyItsBradley Step two is complete 2123832203306221870（引用自己的 Step one 2122983246816325717）。丢掉最旧 3 条：Dilmerv Something that really excites me about Meta VR Glasses is that I don’t fully know what the most creative experiences wil 2119678920916160897；Dilmerv Made a lot of progress with Hand Skate today! 2119631229108494348；Dilmerv One thing I keep thinking about with Meta VR Glasses is how much the experience changes when the hardware becomes so lig 2119612215275721005。
- top guid 抽查均在（official 现为 MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875 / pimaxofficial Korea exhibition day 1 2123716020217225505 / VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088 / getVITURE Vice City 2123506093741481991；media-kol 现为 SadlyItsBradley toddler CV 2123871085892620743 / nathie vacuum VR 2123860708870021372 / SadlyItsBradley Step two 2123832203306221870 / SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852 / nathie spatial airdrop 2123481440104907056 / SadlyItsBradley decomps quote 2123467399664107864 / Dilmerv VR/MR AI tools 2123348430684586250）。
- 上一有变更档：2026-11-20 20:00 BJT official +1 pimaxofficial Korea exhibition day 1；media-kol 不变。00:00 BJT 无新原创，未 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-21 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
