# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-17 20:09 PST（例行 12:00 BJT 2026-11-18）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 18 Nov 2026 00:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 18 Nov 2026 04:09:28 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-18 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：Dilmerv、SadlyItsBradley；与上轮相同、未再拉时间线的：PICOXR_Dev、htcvive、VRChat、nathie；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）、htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）、VRChat most_recent 仍为回复 2122747122567229823（@shiro_ruby sent you a DM!）、nathie most_recent 仍为回复 2122832091540865134（@CircuitLord）（均与 08:00 BJT 轮相同，未再拉时间线）。Dilmerv most_recent 从上轮回复 2122812600719413353 变为新原创 2122880029013004659（Unite Tokyo 采访试戴 Meta VR Glasses），已拉时间线（since_id 2122200536132821374，exclude 后 result_count 5：新原帖 2122880029013004659 入库全文 note tweet，媒体 t.co 展开为 https://x.com/Dilmerv/status/2122880029013004659/photo/1；其余 4 条与上轮相同、作旅行/生活/生病丢弃：2122708107696775518 因病离开 Unite Tokyo、自回 2122709091772743684 Uber 买药、2122547349235065070 It was so great meeting you!、2122415118827024888 Stopped by the Unity venue yesterday…）。SadlyItsBradley most_recent 从上轮回复 2122839824566497525 变为新回复 2122854865013793110（@ChickTech Yeah! First time I did this lol / Christmas trees），已拉时间线（since_id 2122769069229346868，exclude 后 result_count 0，无入库）。
- **official 100 不变（+0）：** 无新原创入库。htcvive 在 official feed 仍无剩余条目（下一轮仍按 accounts 名单预检）。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv I interviewed a couple of people yesterday at Unity Unite Tokyo 🇯🇵 after they tried Meta VR Glasses for the first time,  2122880029013004659。丢掉最旧 1 条：SadlyItsBradley Oh so THAT’S what Valve is doing to enable this!? 😵 2118907013640184068。
- top guid 抽查均在（official 仍为 MetaVR_Official OST 9 2122828030414668144 / MetaVRDevs Unscripted ep 3 2122806546870739142 / Play_for_dream 8K MR 2122751626754617775 / getVITURE Phantom Beast 2122736019242164279 / PICOXR recording 2122721567541010603 / getVITURE Phantom Blade giveaway 2122721454538047499 / XREAL_Global AURA tips 2122691780453793834 / BeatSaber Play With Us reminder 2122688191996260724；media-kol 现为 Dilmerv Unite Tokyo Meta VR Glasses interviews 2122880029013004659 / nathie VR GOTY nominees 2122800548990910562 / SadlyItsBradley abomination arrived 2122769069229346868 / ARealityEvent SPAI AWE 2027 2122721508086976575 / nathie Gentle Monster glasses 2122699884767957370 / SadlyItsBradley crazy teaser 2122497980120850807 / nathie Zelda Ocarina VR 2122377254613434769 / Dilmerv Meta VR Glasses redesign 2122200536132821374）。
- 上一有变更档：2026-11-18 08:00 BJT official +4 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-18 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
