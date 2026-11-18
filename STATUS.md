# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-18 08:07 PST（例行 00:00 BJT 2026-11-19）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 18 Nov 2026 16:07:25 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 18 Nov 2026 16:07:25 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-19 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：RokidGlobal、magicleap、BeatSaber、nathie、Dilmerv；与上轮相同、未再拉时间线的：htcvive、XREAL_Global、PICOXR_Dev、VRChat、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、XREAL_Global most_recent 仍为回复 2122982235188150724（@FXG_VR @baiweiart @nikkmitchell Let's play the funny game with XREAL AURA!）、PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、SadlyItsBradley most_recent 仍为回复 2122986556377977274（@maxym3D I have two trips before Christmas）（均与 20:00 BJT 轮相同，未再拉时间线）。RokidGlobal most_recent 从上轮等于 watermark 的入库原帖 2122526110198223031 变为新原创 2123068728716013871（Black Friday starts tomorrow.），已拉时间线（since_id 2122526110198223031，exclude 后 result_count 1，入库全文；t.co 展开为 https://x.com/RokidGlobal/status/2123068728716013871/photo/1）。magicleap most_recent 从上轮等于 watermark 的入库原帖 2120146962402214039 变为新原创 2123040022811304411（Different AR eyewear styles don't always need different waveguide designs.），已拉时间线（since_id 2120146962402214039，exclude 后 result_count 1，入库全文；t.co 展开为 https://www.magicleap.com/stories/one-waveguide-design-many-eyepiece-shapes 与 https://x.com/magicleap/status/2123040022811304411/photo/1）。BeatSaber most_recent 从上轮等于 watermark 的入库原帖 2122688191996260724 变为自转 2123068050337595452（RT @BeatSaber Play With Us TOMORROW 提醒），已拉时间线（since_id 2122688191996260724，exclude 后 result_count 0，无入库）。nathie most_recent 从上轮回复 2122832091540865134（@CircuitLord）变为新回复 2123028265703260566（@ikkou @MetaforDevs Welcome to the club!），已拉时间线（since_id 2122800548990910562，exclude 后 result_count 1，为已入库串帖续帖 2122803465017606298 Vote here!，已合成进 2122800548990910562，跳过）。Dilmerv most_recent 从上轮回复 2122945920975483197（@HeionLabs）变为新回复 2123074177720889839（@xrdevrob That looks amazing man!），已拉时间线（since_id 2122937962174575027，exclude 后 result_count 1，入库 2123073735666385171 Take a look at this work of art by Robi，引用 @xrdevrob Unframed / Meta VR Glasses 影院概念 2123066129052795340；t.co 展开为 https://x.com/xrdevrob/status/2123066129052795340 与引用视频 https://x.com/xrdevrob/status/2123066129052795340/video/1）。
- **official 100→100（+2/−2 cap）：** RokidGlobal Black Friday starts tomorrow. 2123068728716013871；magicleap Different AR eyewear styles don't always need different waveguide designs. 2123040022811304411。丢掉最旧 2 条：PICOXR Leave the familiar behind. 2118372937203884362；BeatSaber Help a fellow player out! 2118363087283585099。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv Take a look at this work of art by Robi 🤯 this is incredible! 2123073735666385171。丢掉最旧 1 条：Dilmerv One thing that still amazes me about Meta VR Glasses is how much technology we’ve managed to fit into such a small form  2119086815366029414。
- top guid 抽查均在（official 现为 RokidGlobal Black Friday 2123068728716013871 / magicleap waveguide 2123040022811304411 / BigscreenVR GTA VI in VR 2122994472913150331 / getVITURE Z-Axis Award 2122956121896022457 / MetaVR_Official OST 9 2122828030414668144 / MetaVRDevs Unscripted ep 3 2122806546870739142 / Play_for_dream 8K MR 2122751626754617775 / getVITURE Phantom Beast 2122736019242164279；media-kol 现为 Dilmerv Unframed quote 2123073735666385171 / SadlyItsBradley Step one is complete 2122983246816325717 / Dilmerv competition submissions 2122937962174575027 / Dilmerv Puzzleform 2122930855438057722 / SadlyItsBradley stereo view CV 2122912338483257751 / Dilmerv Unite Tokyo booth 2122910259853594833 / Dilmerv Unite Tokyo Meta VR Glasses interviews 2122880029013004659 / nathie VR GOTY nominees 2122800548990910562）。
- 上一有变更档：2026-11-18 20:00 BJT official +1 / media-kol +1。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-19 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
