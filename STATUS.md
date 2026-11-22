# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-22 08:09 PST（例行 00:00 BJT 2026-11-23）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 22 Nov 2026 16:09:29 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 22 Nov 2026 04:03:27 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-23 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：RokidGlobal、VRChat；与上轮相同、未再拉时间线的：MetaVR_Official、htcvive、pimaxofficial、Play_for_dream、PICOXR_Dev、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、BigscreenVR、XREAL_Global、getVITURE、MetaVRDevs、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。MetaVR_Official most_recent 仍为回复 2123974636194935277（@RG2_Soldiers Best seat in the house.）。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。pimaxofficial most_recent 仍为已入库串帖续帖 2123716023920865610（自回 2123716020217225505）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。nathie most_recent 仍为已合成自回 2124257850876711299（Source 链到 Reddit，根帖 2124257333731786887）。Dilmerv most_recent 仍为回复 2124352332414800049（@motorsep “That’s just what I personally like ;)”，会话 2124340557078032645）。SadlyItsBradley most_recent 仍为转发 2124288882531283034（@BlenderStudio_ DOGWALK visionOS / WWDC26 2124141948554404051）。VRChat most_recent 从上轮原帖 2124249109003747407（ban apology）变为转发 2124491962199822604（@sdvx_viga37 「たのしい」が、ぜんぶある / #VRChat）；已拉时间线（since_id 2124249109003747407，exclude 后 result_count 0，入库 0）。RokidGlobal most_recent 从 2124155883684859968（GTA VI on Rokid Max 2）变为 2124518275514310957（Amazon Black Friday deals）；已拉时间线（since_id 2124155883684859968，exclude 后 result_count 1，入库 1）。
- **official 100→100（+1/−1 cap）：** RokidGlobal Prefer to shop on Amazon? / Black Friday deals on Amazon US and EU 2124518275514310957。丢掉最旧 1 条：PICOXR Ready to browse, but not to choose? 2119822502851473729。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 RokidGlobal Amazon Black Friday 2124518275514310957 / VRChat ban apology 2124249109003747407 / BeatSaber Purr OST 9 2124218919296659517 / RokidGlobal GTA VI on Rokid Max 2 2124155883684859968 / MetaVR_Official LSU 2123918298136158415 / MetaVRDevs Unite Tokyo 2123899966762668519 / BeatSaber Signal Jammer 2123847813150691377 / MetaVRDevs November updates 2123846165892583875；media-kol 仍为 Dilmerv Meta VR Glasses form factor 2124340557078032645 / Dilmerv Hand Skate forgiving gestures 2124300999653233099 / nathie Zelda OoT VR mod 2124257333731786887 / Dilmerv XR demo test 2124239952581919229 / nathie first-person VR mod 2124151464733835739 / Dilmerv Meta VR Start Tejas Shroff 2124094675485364351 / nathie You agree? 2123945466383753670 / SadlyItsBradley toddler CV 2123871085892620743）。
- 上一有变更档：2026-11-22 12:00 BJT media-kol +2（Dilmerv Meta VR Glasses form factor / Dilmerv Hand Skate forgiving gestures）。16:00 与 20:00 BJT 两档无变化、未 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-23 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
