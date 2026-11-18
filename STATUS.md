# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-17 16:08 PST（例行 08:00 BJT 2026-11-18）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 18 Nov 2026 00:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 18 Nov 2026 00:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-18 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：MetaVR_Official、MetaVRDevs、getVITURE、Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：PICOXR_Dev、htcvive；其余等于 watermark 跳过（PICOXR、XREAL_Global、pimaxofficial、RokidGlobal、BigscreenVR、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）（均与 00:00 BJT 轮相同，未再拉时间线）。MetaVR_Official most_recent 从上轮回复 2122354254937514257 变为新原创 2122828030414668144（IT'S HERE! OST 9 just landed in @BeatSaber），已拉时间线（since_id 2121347262102265922，exclude 后 1 条，入库）。MetaVRDevs most_recent 为新原创 2122806546870739142（Meta VR Glasses arrive spring 2027 / Unscripted episode 3），已拉时间线（exclude 后 1 条，入库全文 note_tweet；t.co 展开为 https://www.youtube.com/watch?v=yyqetIo41nU）。getVITURE most_recent 从上轮原帖 2122721454538047499 变为新原创 2122736019242164279（Phantom Beast unboxed / $599），已拉时间线（since_id 2122721454538047499，exclude 后 1 条，入库）。Play_for_dream most_recent 为新原创 2122751626754617775（True 8K Micro-OLED visuals），已拉时间线（since_id 2120577299942699387，exclude 后 1 条，入库）。VRChat most_recent 从上轮回复 2122386744918028710 变为新回复 2122747122567229823（@shiro_ruby sent you a DM!），已拉时间线（since_id 2122386338687095004，exclude 后 result_count 0，无入库）。nathie most_recent 从上轮原帖 2122699884767957370 变为回复 2122832091540865134（@CircuitLord），已拉时间线（since_id 2122699884767957370，exclude 后 result_count 2：新原帖 2122800548990910562 VR Game of the Year nominees 入库；自回 2122803465017606298 Vote here! 已合成进该条目）。Dilmerv most_recent 从上轮回复 2122718654886551842 变为回复 2122812600719413353（@unitygames This is great Unity! Well done and a win for developers.），已拉时间线（since_id 2122200536132821374，exclude 后 result_count 4，全部与 00:00 BJT 轮相同、作旅行/生活/生病丢弃：2122708107696775518 因病离开 Unite Tokyo、自回 2122709091772743684 Uber 买药、2122547349235065070 It was so great meeting you!、2122415118827024888 Stopped by the Unity venue yesterday…）。SadlyItsBradley most_recent 从上轮回复 2122517408854229326 变为回复 2122839824566497525（@martydudeVR Steam frame / fruit company video），已拉时间线（since_id 2122497980120850807，exclude 后 1 条：2122769069229346868 A true abomination of nature has just arrived at my door，引用已入库预告 2122497980120850807，入库）。
- **official 100→100（+4/−4 cap）：** MetaVR_Official IT'S HERE! 💥 OST 9 just landed in @BeatSaber. 2122828030414668144；MetaVRDevs Meta VR Glasses arrive spring 2027.（Unscripted episode 3）2122806546870739142；Play_for_dream True 8K Micro-OLED visuals. 2122751626754617775；getVITURE The blade is drawn. ⚔️（Phantom Beast unboxed / $599）2122736019242164279。丢掉最旧 4 条：BigscreenVR What is the coolest experience you've had in VR recently? 2118155350461518244、XREAL_Global Never miss the pocket again. 2118116775850111132、XREAL_Global Bring your avatar to life. 2118056573318611406、VRChat Come see Hatsune Miku at PLAYBACK LIVE in VRChat! 2118043459022152055。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+2/−2 cap）：** nathie These are the nominees for VR Game of the Year.（合成 Vote here! The Game Awards Best VR/AR）2122800548990910562；SadlyItsBradley A true abomination of nature has just arrived at my door 2122769069229346868。丢掉最旧 2 条：SadlyItsBradley Latest Steam Frame Beta now lets you actually keep your Room View when you’re viewing remote frames/overlays being strea 2118882146219893178、Dilmerv The more I experiment with hand interactions in my MR skating game, Hand Skate, the more I realize how important it is t 2118879326447800539。
- top guid 抽查均在（official 现为 MetaVR_Official OST 9 2122828030414668144 / MetaVRDevs Unscripted ep 3 2122806546870739142 / Play_for_dream 8K MR 2122751626754617775 / getVITURE Phantom Beast 2122736019242164279 / PICOXR recording 2122721567541010603 / getVITURE Phantom Blade giveaway 2122721454538047499 / XREAL_Global AURA tips 2122691780453793834 / BeatSaber Play With Us reminder 2122688191996260724；media-kol 现为 nathie VR GOTY nominees 2122800548990910562 / SadlyItsBradley abomination arrived 2122769069229346868 / ARealityEvent SPAI AWE 2027 2122721508086976575 / nathie Gentle Monster glasses 2122699884767957370 / SadlyItsBradley crazy teaser 2122497980120850807 / nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374 / Dilmerv Meta VR Glasses background 2122105069483270207）。
- 上一有变更档：2026-11-18 00:00 BJT official +5 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-18 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
