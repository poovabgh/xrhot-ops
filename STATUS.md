# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-08 16:08 PST（例行 08:00 BJT 2026-11-09）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 08 Nov 2026 16:06:14 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 09 Nov 2026 00:07:07 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-09 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：htcvive、BigscreenVR、MetaVRDevs、RokidGlobal、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（XREAL_Global、VRChat、MetaVR_Official、BeatSaber、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** htcvive / BigscreenVR / MetaVRDevs / RokidGlobal `exclude` 后 result_count 0。
- **media-kol 100→100（+5/−5 cap）：** Dilmerv Meta VR Glasses excitement / hands+gaze 2119558130342244796；Hand Skate procedural decorations 2119549129516843047；Hand Skate stretch routine 2119535907132875009；Vistathlon Meta Ray-Ban Display live cheering quote 2119534041179582591；Hand Skate skate park resize 2119484628037722374。丢掉最旧 5 条：Dilmerv MR Halloween animation 2115895791562940774 / nathie Spider-Man VR mod 2115879127286706573 / Dilmerv Meta VR Glasses getting started 2115877665555014044 / SadlyItsBradley laser tag VRChat 2115855071036543167 / Dilmerv live session Meta VR Glasses 2115821443069911406。Dilmerv 2119535068515553624 iPhone Duo drop；2119505311576826055 通用 building in public（LearnXR 仅为背景）drop；2119407117878661572 通用开发者感悟 drop（同 00:00）。nathie 2119391299308577274 为已入库 2118316089738469467（Zelda first-person VR）的续帖，skip。nathie 2119132199270166781 为已入库 2119132001953325177（Hole Wall）的续帖，skip。SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（官方不变 Rokid glasses language barrier + XREAL Sock/BRINK/AMAZE + VRChat Dice Party；新媒体 Dilmerv Meta VR Glasses excitement / Hand Skate decorations / stretch routine / Ray-Ban Display quote / skate park resize + 旧 Hand Skate weekend progress）。
- 上一有变更档：2026-11-09 00:00 BJT official Rokid glasses language barrier。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-09 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
