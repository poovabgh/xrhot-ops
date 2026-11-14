# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-14 08:12 PST（例行 00:00 BJT 2026-11-15）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 14 Nov 2026 16:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 14 Nov 2026 16:12:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-15 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：RokidGlobal、VRChat、SadlyItsBradley、MetaVRDevs、htcvive、pimaxofficial、nathie；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、getVITURE、Play_for_dream、magicleap、BeatSaber、ARealityEvent、Dilmerv）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。MetaVRDevs most_recent 仍为已入库 2121305089449308635（Fresh release notes / v209 SDK）线程的续帖 2121306015765499936、htcvive most_recent 仍为转发 2118069208126747106、pimaxofficial most_recent 仍为已入库 2121055807618101380（G-STAR 2026 Busan）的 English 续帖 2121055811359347064、nathie most_recent 仍为转发 2121433435462070632（均与上轮相同，未再拉时间线）。SadlyItsBradley most_recent 为回复 2121633700450382211（@tfolkman / GPU），exclude 后另有 2 条原创。
- **official 100→100（+2/−2 cap）：** RokidGlobal Black Friday in 5 days 2121619174686359624；VRChat Virtual Dice Party 2121617840956719115。丢掉最旧 2 条：PICOXR The scariest part might happen before the headset even goes on 2116545840953045420；XREAL_Global Small room. Massive screen 2116500652541042983。
- **media-kol 100→100（+1/−1 cap）：** SadlyItsBradley How common is this?（引用 @martydudeVR H3VR2 / Quest games）2121618547604672746。丢掉最旧 1 条：Dilmerv Want to get some inspiration from the best of the best 2118469739966247365。丢弃非 XR：SadlyItsBradley 引用 TechPowerUp NVIDIA GPU scarcity 标题 2121601651060670878。
- top guid 抽查均在（official 现为 RokidGlobal Black Friday 2121619174686359624 / VRChat Virtual Dice Party 2121617840956719115 / XREAL AURA Founder Editions 2121472555395756506 / VRChat Osaka trophy 2121407670821261813 / BigscreenVR still flying 2121367890809229370 / getVITURE Pro 2 Amazon 2121362184106385433 / MetaVR Celtics highlights 2121347262102265922 / BeatSaber Confetti LFG 2121308812963438930；media-kol 现为 SadlyItsBradley Quest games quote 2121618547604672746 / Dilmerv Meta VR Glasses perspectives 2121499633079787732 / Dilmerv Meta VR Glasses 2121430048804585886 / Dilmerv AI XR workflows 2121419120281583758 / Dilmerv love XR MR conversions 2121416659160248770 / nathie Razer haptic chair 2121383921552416861 / Dilmerv TapeDeck Hand Skate 2121299006085091438 / nathie Gentle Monster first look 2121297122897305604）。
- 上一有变更档：2026-11-14 20:00 BJT official +1 / media-kol +0。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-15 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
