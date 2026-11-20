# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-19 16:10 PST（例行 08:00 BJT 2026-11-20）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 20 Nov 2026 00:09:13 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 20 Nov 2026 00:09:13 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-20 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：getVITURE、Play_for_dream、VRChat、BeatSaber、Dilmerv、SadlyItsBradley、nathie；与上轮相同、未再拉时间线的：htcvive、PICOXR_Dev；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、pimaxofficial、MetaVRDevs、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。getVITURE most_recent 从上轮已入库 2123136157890253100 变为新原创 2123506093741481991（Vice City / VITURE Beast）；已拉时间线（since_id 2123136157890253100，exclude 后 result_count 3，全部入库：2123506093741481991 Vice City opens up again on VITURE Beast，t.co 展开为 https://www.viture.com/product/viture-beast-xr-glasses 与 https://x.com/getVITURE/status/2123506093741481991/video/1；2123491002904186940 TWO FLAGSHIPS Beast $489 / Luma Ultra $449，t.co 展开为 https://www.viture.com/product/viture-beast-xr-glasses、https://www.viture.com/product/viture-luma-ultra-xr-glasses 与 photo/1；2123468616641216588 13 YEARS Miami Outlaw stickers / HDMI Adapter，t.co 展开为 https://www.viture.com/product/viture-pro-2-hdmi-cable-pack 与 photo/1）。Play_for_dream most_recent 从上轮已入库 2122751626754617775 变为新原创 2123476410920513943（Hand gestures）；已拉时间线（since_id 2122751626754617775，exclude 后 result_count 1，全部入库）。VRChat most_recent 从上轮回复 2122747122567229823 变为新原创串帖 2123549260000248096（Today's thumbnail is PC Only，自回 2123549256321781884 Nov 19 Dev Update）；已拉时间线（since_id 2122386338687095004，exclude 后 result_count 2，合成 1 条入库：父帖 2123549256321781884 It's time for the Nov 19 Dev Update!，t.co 展开为 https://ask.vrchat.com/t/developer-update-19-november-2026/49409 与 photo/1；续帖 2123549260000248096 合成进父帖，world 链为 https://vrchat.com/home/world/wrld_ad8933c6-90ad-49b4-8722-fa7f649c3e18/info）。BeatSaber most_recent 从上轮转发 2123377313865933300 变为新原创 2123521746145866088（Billie Eilish concert film / Music Pack）；已拉时间线（since_id 2123099089004900650，exclude 后 result_count 2，全部入库：2123521746145866088 用 note_tweet 全文，t.co 展开为 photo/1；2123478439088844912 Nostalgia is a Curse / OST 9，t.co 展开为 video/1）。Dilmerv most_recent 从上轮已入库 2123348430684586250 变为新原创 2123512111540080852（Tokyo trip / Meta VR Glasses）；已拉时间线（since_id 2123348430684586250，exclude 后 result_count 1，全部入库，用 note_tweet 全文）。SadlyItsBradley most_recent 从上轮已入库 2123281801817051516 变为回复 2123543120763920787（@jmeyey8543540）；已拉时间线（since_id 2123281801817051516，exclude 后 result_count 2，全部入库：2123534916025511973 Meta Start Competition submissions；2123467399664107864 引用 @lucas_martinic 2123285511615946782 Guys, hear me out，t.co 展开为 https://x.com/lucas_martinic/status/2123285511615946782 与 video/1）。nathie most_recent 从上轮转发 2123411765157302419 变为新原创 2123481440104907056（spatial airdropping）；已拉时间线（since_id 2122800548990910562，exclude 后 result_count 3，入库 1：2123481440104907056 入库，媒体链为 https://x.com/xbh_artist/status/2123366946624127067/video/1；2123208524624966068 GTA 6 gaming family 仍为非 VR 游戏/闲聊丢弃；2122803465017606298 Vote here 自回已在先前轮次合成进父帖 2122800548990910562）。
- **official 100→100（+7/−7 cap）：** VRChat It's time for the Nov 19 Dev Update! 2123549256321781884（合成自回 2123549260000248096 Today's thumbnail is PC Only）；BeatSaber Billie Eilish, front row. 🕊️ 2123521746145866088；getVITURE To every player who waited for it: it's HERE! 🌴 2123506093741481991；getVITURE TWO FLAGSHIPS. LOWEST PRICES EVER. 🔥 2123491002904186940；BeatSaber "Nostalgia is a Curse" by Starslinger 2123478439088844912；Play_for_dream Select. Move. Confirm. 👆 2123476410920513943；getVITURE 13 YEARS. IT'S HERE. 🌴🔥 2123468616641216588。丢掉最旧 7 条：MetaVR_Official Two huge SEC matchups 2118761763630113004 / XREAL_Global The case is yours to crack 2118751691512160543 / BeatSaber Cancel your plans for NOVEMBER 12 2118735513335087481 / RokidGlobal 9.5/10 Editor's Choice 2118720067617583153 / XREAL_Global Why should only the surgeon have a 3D view 2118706620293120077 / XREAL_Global Watch the market unfold around you 2118675807501455801 / XREAL_Global Your next canvas is the room around you 2118530694037029289。
- **media-kol 100→100（+4/−4 cap）：** SadlyItsBradley Very impressed by all the Meta Start Competition submissions 2123534916025511973；Dilmerv Finally back home after such an inspiring trip to Tokyo 2123512111540080852；nathie You can now take a photo on your phone and instantly bring it into VR 2123481440104907056；SadlyItsBradley With the way that game decomps/recomps have been going 2123467399664107864（引用 @lucas_martinic）。丢掉最旧 4 条：Dilmerv If you've been playing with VR, check out Meta's Interaction SDK 2119585780775420250 / Dilmerv It's crazy to see how much excitement there is around Meta VR Glasses 2119558130342244796 / Dilmerv All right, this felt a bit plain 2119549129516843047 / Dilmerv I updated the stretch routine in Hand Skate 2119535907132875009。
- top guid 抽查均在（official 现为 VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088 / getVITURE Vice City 2123506093741481991 / getVITURE TWO FLAGSHIPS 2123491002904186940 / BeatSaber Nostalgia is a Curse 2123478439088844912 / Play_for_dream hand gestures 2123476410920513943 / getVITURE 13 YEARS 2123468616641216588 / PICOXR copy a pose 2123446342504587578；media-kol 现为 SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852 / nathie spatial airdrop 2123481440104907056 / SadlyItsBradley decomps quote 2123467399664107864 / Dilmerv VR/MR AI tools 2123348430684586250 / Dilmerv Meta VR Start competition 2123319106656989445 / SadlyItsBradley gaussian splat 2123281801817051516 / Dilmerv TARGO Emmy quote 2123277400771567792）。
- 上一有变更档：2026-11-20 00:00 BJT official +2 PICOXR copy a pose / RokidGlobal Black Friday is live；media-kol 不变。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-20 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
