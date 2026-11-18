# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-18 00:05 PST（例行 16:00 BJT 2026-11-18）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 18 Nov 2026 08:04:41 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 18 Nov 2026 08:04:41 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-18 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、getVITURE、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：PICOXR_Dev、htcvive、VRChat、nathie；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、RokidGlobal、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、nathie most_recent 仍为回复 2122832091540865134（@CircuitLord）（均与 12:00 BJT 轮相同，未再拉时间线）。XREAL_Global most_recent 从上轮入库原帖 2122691780453793834 变为转发 2122954257309815020（RT @RalphJodiceJr Android XR / XREAL day one verdict），已拉时间线（since_id 2122691780453793834，exclude 后 result_count 0，无入库）。getVITURE most_recent 从上轮入库原帖 2122736019242164279 变为新原创 2122956121896022457（Z-Axis Award，奖品为 VITURE Luma Ultra），已拉时间线（since_id 2122736019242164279，exclude 后 result_count 1，入库全文；引用 @MeshyAI Z-Axis Awards，$300,000 prizes；t.co 展开为 https://x.com/MeshyAI/status/2122946850491949139 与引用视频 https://x.com/MeshyAI/status/2122946850491949139/video/1）。Dilmerv most_recent 从上轮入库原帖 2122880029013004659 变为回复 2122945920975483197（@HeionLabs That’s very cool! Is that Google map data?），已拉时间线（since_id 2122880029013004659，exclude 后 result_count 3，全部入库：2122937962174575027 Meta VR Start Developer Competition submissions，媒体展开为 https://x.com/Dilmerv/status/2122937962174575027/photo/1；2122930855438057722 Looking forward to testing Puzzleform!，引用 @dannyaroslavski Puzzleform / Meta VR Start，t.co 展开为 https://x.com/dannyaroslavski/status/2122860983307874806 与引用视频 https://x.com/dannyaroslavski/status/2122860983307874806/video/1；2122910259853594833 note tweet Unite Tokyo booth / Meta VR Glasses SDK guidance，媒体 t.co 展开为 https://x.com/Dilmerv/status/2122910259853594833/video/1）。SadlyItsBradley most_recent 从上轮回复 2122854865013793110 变为新回复 2122949088245096587（@puzzabug Woah. Rare and very welcome puzzabug sighting），已拉时间线（since_id 2122769069229346868，exclude 后 result_count 1，入库 2122912338483257751 We heckin’ love stereo view CV in this house，媒体展开为 https://x.com/SadlyItsBradley/status/2122912338483257751/video/1）。
- **official 100→100（+1/−1 cap）：** getVITURE Proud to back the first Z-Axis Award by @MeshyAI 🏆 2122956121896022457。丢掉最旧 1 条：XREAL_Global Field trip, no passport required. 2118267924255326283。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+4/−4 cap）：** Dilmerv Some of the Meta VR Start Developer Competition submissions I've seen are wild! 🕶️ 2122937962174575027；Dilmerv Looking forward to testing Puzzleform! 2122930855438057722；SadlyItsBradley We heckin’ love stereo view CV in this house 2122912338483257751；Dilmerv A couple of my coworkers at Meta, and honestly, some very inspiring friends! 2122910259853594833。丢掉最旧 4 条：Dilmerv What excites me most about Meta VR Glasses isn’t just the hardware, but what devs will create with it! 2119080565253271975；SadlyItsBradley I was able to force SteamVR to render its new chroma key pipeline so that I could activate Room View on my Vision Pro 2118956794714411412；Dilmerv One of the best “start here” resources I’ve seen for Meta VR Glasses! 2118926207756714255；Dilmerv Great video by @MKBHD! 🚀🕶️ 2118919611269939252。
- top guid 抽查均在（official 现为 getVITURE Z-Axis Award 2122956121896022457 / MetaVR_Official OST 9 2122828030414668144 / MetaVRDevs Unscripted ep 3 2122806546870739142 / Play_for_dream 8K MR 2122751626754617775 / getVITURE Phantom Beast 2122736019242164279 / PICOXR recording 2122721567541010603 / getVITURE Phantom Blade giveaway 2122721454538047499 / XREAL_Global AURA tips 2122691780453793834；media-kol 现为 Dilmerv competition submissions 2122937962174575027 / Dilmerv Puzzleform 2122930855438057722 / SadlyItsBradley stereo view CV 2122912338483257751 / Dilmerv Unite Tokyo booth 2122910259853594833 / Dilmerv Unite Tokyo Meta VR Glasses interviews 2122880029013004659 / nathie VR GOTY nominees 2122800548990910562 / SadlyItsBradley abomination arrived 2122769069229346868 / ARealityEvent SPAI AWE 2027 2122721508086976575）。
- 上一有变更档：2026-11-18 12:00 BJT official +0 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-18 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
