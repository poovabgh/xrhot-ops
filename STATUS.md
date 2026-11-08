# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-07 20:12 PST（例行 12:00 BJT 2026-11-08）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 08 Nov 2026 00:15:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 08 Nov 2026 04:11:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-08 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：htcvive、BigscreenVR、MetaVRDevs、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（XREAL_Global、VRChat、MetaVR_Official、BeatSaber、RokidGlobal、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** htcvive / BigscreenVR / MetaVRDevs `exclude` 后 result_count 0。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv Hand Skate music visualizers / Mixed Reality walls 2119278281421725959（续帖 boombox visualizer 2119278282386378861 合成一条）；Dilmerv Hand Skate 13 animations / Quest & Meta VR Glasses 2119273069147455708。丢掉最旧 2 条：Dilmerv FAST dev iteration tip 2115636246148005981、Dilmerv spooky pet 2115624302724948032。nathie 2119132199270166781 为已入库 2119132001953325177 的续帖，skip。SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（官方不变 XREAL Sock/BRINK/AMAZE + VRChat Dice Party / XREAL Fishing / XREAL board；新媒体 Dilmerv visualizer / animations + 旧 Dilmerv ISDK / Quest3 quote / nathie Hole Wall / Dilmerv Glasses SDK）。
- 上一有变更档：2026-11-08 08:00 BJT official XREAL AURA×3 / −1 PICOXR deleted wishlist，media-kol Dilmerv ISDK/Quest3/Glasses + nathie Hole Wall。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-08 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
