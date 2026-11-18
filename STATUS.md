# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-18 04:08 PST（例行 20:00 BJT 2026-11-18）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 18 Nov 2026 12:07:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 18 Nov 2026 12:07:33 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-18 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、XREAL_Global、SadlyItsBradley；与上轮相同、未再拉时间线的：PICOXR_Dev、htcvive、VRChat、nathie、Dilmerv；其余等于 watermark 跳过（MetaVR_Official、PICOXR、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、nathie most_recent 仍为回复 2122832091540865134（@CircuitLord）、Dilmerv most_recent 仍为回复 2122945920975483197（@HeionLabs That’s very cool! Is that Google map data?）（均与 16:00 BJT 轮相同，未再拉时间线）。BigscreenVR most_recent 从上轮等于 watermark 的入库原帖 2121664463124255159 变为新原创 2122994472913150331（You can play GTA VI in VR (technically)），已拉时间线（since_id 2121664463124255159，exclude 后 result_count 1，入库全文；t.co 展开为 https://store.bigscreenvr.com/blogs/beyond/play-gta-6-in-vr 与 https://x.com/BigscreenVR/status/2122994472913150331/photo/1）。XREAL_Global most_recent 从上轮转发 2122954257309815020 变为回复 2122982235188150724（@FXG_VR @baiweiart @nikkmitchell Let's play the funny game with XREAL AURA!），已拉时间线（since_id 2122691780453793834，exclude 后 result_count 0，无入库）。SadlyItsBradley most_recent 从上轮回复 2122949088245096587 变为新回复 2122986556377977274（@maxym3D I have two trips before Christmas），已拉时间线（since_id 2122912338483257751，exclude 后 result_count 1，入库 2122983246816325717 Step one is complete，引用自己 2122912338483257751 stereo view CV；t.co 展开为 https://x.com/SadlyItsBradley/status/2122983246816325717/video/1、https://x.com/SadlyItsBradley/status/2122912338483257751 与引用视频 https://x.com/SadlyItsBradley/status/2122912338483257751/video/1）。
- **official 100→100（+1/−1 cap）：** BigscreenVR You can play GTA VI in VR (technically), 2122994472913150331。丢掉最旧 1 条：RokidGlobal One gesture can now run a full AI workflow. 2118357678519165323。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+1/−1 cap）：** SadlyItsBradley Step one is complete 2122983246816325717。丢掉最旧 1 条：Dilmerv One thing that still amazes me about Meta VR Glasses is how much technology we’ve managed to fit into such a small form  2119085860763381791。
- top guid 抽查均在（official 现为 BigscreenVR GTA VI in VR 2122994472913150331 / getVITURE Z-Axis Award 2122956121896022457 / MetaVR_Official OST 9 2122828030414668144 / MetaVRDevs Unscripted ep 3 2122806546870739142 / Play_for_dream 8K MR 2122751626754617775 / getVITURE Phantom Beast 2122736019242164279 / PICOXR recording 2122721567541010603 / getVITURE Phantom Blade giveaway 2122721454538047499；media-kol 现为 SadlyItsBradley Step one is complete 2122983246816325717 / Dilmerv competition submissions 2122937962174575027 / Dilmerv Puzzleform 2122930855438057722 / SadlyItsBradley stereo view CV 2122912338483257751 / Dilmerv Unite Tokyo booth 2122910259853594833 / Dilmerv Unite Tokyo Meta VR Glasses interviews 2122880029013004659 / nathie VR GOTY nominees 2122800548990910562 / SadlyItsBradley abomination arrived 2122769069229346868）。
- 上一有变更档：2026-11-18 16:00 BJT official +1 / media-kol +4。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-19 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
