# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-10 16:06 PST（例行 08:00 BJT 2026-11-11）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 11 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 11 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-11 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、pimaxofficial、MetaVRDevs、VRChat、BeatSaber、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、RokidGlobal、getVITURE、Play_for_dream、PICOXR_Dev、magicleap）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+6/−6 cap）：** pimaxofficial Black Friday price protection 2120241914658308117；pimaxofficial IAAPA Expo 2026 2120241367494373761；XREAL_Global Innervoice coming to AURA 2120230928467304646；MetaVRDevs 2026 VR numbers / Chris Pruett thread 合并为 2120223311716364719；XREAL_Global SF Ballet Nutcracker on AURA 2120212983888371721；XREAL_Global Fallout Factions on AURA 2120201229665984698。丢掉最旧 6 条：XREAL_Global Every new experience 2115496951621787701、MetaVRDevs Six questions 2115494685728964795、XREAL_Global AURA is officially here 2115489213281894825、Play_for_dream More power 2115488772582179178、PICOXR Headset care 2115458752539242783、magicleap Waveguide decisions 2115352876562239627。MetaVR_Official / htcvive / BigscreenVR / BeatSaber `exclude` 后 result_count 0。VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。
- **media-kol 100→100（+7/−7 cap）：** nathie Disney+ 3D movies on Quest 3/3S and Meta VR Glasses 2120302292112969841；Dilmerv XR device opportunities 2120297979521253523；Dilmerv quote MetaforDevs / Pruett Quest revenue 2120283640731214017；Dilmerv Meta XR Operator 2120237612321382423；ARealityEvent PhAI co-located with AWE USA 2027 2120230014729990421；SadlyItsBradley tray-table test 2120211061886595180；Dilmerv foveated rendering 2120192393039184290。丢掉最旧 7 条：Dilmerv pinch grab ISDK 2117232898449326584、Dilmerv ISDK tip 2117202641071542501、Dilmerv Meta VR Start Competition 2117172446688088255、Dilmerv basketball collisions 2117134666884886904、Dilmerv MR onboarding 2116945994860417425、nathie Steam Frame 2116933029021049043、Dilmerv Meta VR Glasses tip 2116902353521549532。Dilmerv 2120282894199349569（iOS/GitHub 经历）、2120267810102186325（保持学习）、2120252701367832827（不要怀疑想法）、2120215196312482025（iPhone Duo）按 XR 初筛丢弃。nathie 最新 2120304466159370453 为回复 @swight，非自串帖。
- top-6 guid 抽查均在（新 official pimaxofficial Black Friday 2120241914658308117 / pimaxofficial IAAPA 2120241367494373761 / XREAL Innervoice 2120230928467304646 / MetaVRDevs 2026 numbers 2120223311716364719 / XREAL Nutcracker 2120212983888371721 / XREAL Fallout Factions 2120201229665984698；新 media-kol nathie Disney+ 2120302292112969841 / Dilmerv opportunities 2120297979521253523 / Dilmerv Pruett quote 2120283640731214017 / Dilmerv XR Operator 2120237612321382423 / ARealityEvent PhAI 2120230014729990421 / SadlyItsBradley tray 2120211061886595180；其余 media-kol Dilmerv foveated 2120192393039184290 为第 7 条）。
- 上一有变更档：2026-11-11 00:00 BJT official +3 / media-kol +3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-11 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
