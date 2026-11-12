# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-11 16:06 PST（例行 08:00 BJT 2026-11-12）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 12 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 12 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-12 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、XREAL_Global、Play_for_dream、MetaVRDevs、VRChat、BeatSaber、BigscreenVR、htcvive、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、RokidGlobal、getVITURE、pimaxofficial、PICOXR_Dev、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+5/−5 cap）：** MetaVR_Official GOLF+ / Meta Quest 2120654742716313712（串帖续帖仅 meta.com/quest 链已合并）；XREAL_Global Project Hail Mary / AURA 6DoF 2120593418816516440；MetaVRDevs Unite Tokyo quote 2120591346872602912；Play_for_dream Augmented Virtuality 2120577299942699387；XREAL_Global Paper Birds / AURA 2120563760267960521。丢掉最旧 5 条：XREAL_Global A new chapter 2115692609624756310 / XREAL_Global Best Buy live 2115682560135082005 / PICOXR_Dev time-freezing 2115634287437570110 / XREAL_Global favorite apps 2115580072698462386 / VRChat AI feedback 2115542209785446488。BeatSaber / BigscreenVR / htcvive `exclude` 后 result_count 0。VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。MetaVRDevs `exclude` 后另有 2120223376031764914 / 2120223484945244628 / 2120223621759349165，均为已入库 2120223311716364719（2026 VR numbers）的续帖，skip。
- **media-kol 100→100（+11/−11 cap）：** SadlyItsBradley Vision Pro cage/SharePlay 2120667515097620923（续帖 Local SharePlay 已合并）；SadlyItsBradley Spatial Audio orb 2120655657011716574；SadlyItsBradley Apple Q&A commitment 2120639294364921992；Dilmerv MetaVR CLI xrsim env 2120622649965416657；nathie Black Friday headset pick 2120616892054335974；Dilmerv VR/MR scale 2120616320957915253；SadlyItsBradley BlackMagic mic $1695 2120589411197059112；SadlyItsBradley Ambisonic mic announce 2120586432079450245；Dilmerv hands-first challenges 2120586123080577356；SadlyItsBradley Apple Developer Center live 2120568267370909746；Dilmerv MR game design rules 2120554737913192491。丢掉最旧 11 条：nathie Google smart glasses 2117637628967239874 / Dilmerv Meta VR CLI tip 2117572758464761856 / Dilmerv Cubiques submit 2117477060298080601 / SadlyItsBradley AVP Steam VR Link 2117370134788718640 / SadlyItsBradley chroma key 2117369162792136932 / Dilmerv interesting question 2117368772201742555 / SadlyItsBradley SteamVR 2.19.1 2117364399132545432 / SadlyItsBradley Lepton decode 2117354689872154824 / nathie Quest 2/Pro EoL 2117346754295423294 / Dilmerv MR level adapt 2117342264556965913 / Dilmerv Cubiques trailer 2117334958565974368。SadlyItsBradley `exclude` 后另有生活向 2120561624180506925（long sleeve / Florida）按 XR 初筛丢弃；续帖 2120380985594503197 / 2120667519430414372 / 回复 2120668184193986953 未单独入库。
- top-6 guid 抽查均在（新 official MetaVR_Official GOLF+ 2120654742716313712 / XREAL Hail Mary 2120593418816516440 / MetaVRDevs Unite Tokyo 2120591346872602912 / Play_for_dream AV 2120577299942699387 / XREAL Paper Birds 2120563760267960521 / RokidGlobal Rokid AR Spatial 2120532005356200047；新 media-kol SadlyItsBradley Vision Pro cage 2120667515097620923 / Spatial Audio orb 2120655657011716574 / Apple Q&A 2120639294364921992 / Dilmerv xrsim env 2120622649965416657 / nathie Black Friday pick 2120616892054335974 / Dilmerv scale 2120616320957915253）。
- 上一有变更档：2026-11-12 00:00 BJT official +1 / media-kol +0。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-12 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
