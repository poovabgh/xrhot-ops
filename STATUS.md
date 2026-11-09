# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-09 00:08 PST（例行 16:00 BJT 2026-11-09）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 08 Nov 2026 16:06:14 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 09 Nov 2026 08:08:22 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-09 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：htcvive、BigscreenVR、MetaVRDevs、RokidGlobal、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（XREAL_Global、VRChat、MetaVR_Official、BeatSaber、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** htcvive / BigscreenVR / MetaVRDevs / RokidGlobal `exclude` 后 result_count 0。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv Meta VR Glasses creative experiences 2119678920916160897。丢掉最旧 1 条：Dilmerv Hand Pose Baker spooky pet MR 2116227340229660770。nathie 2119391299308577274 为已入库 2118316089738469467（Zelda first-person VR）的续帖，skip。nathie 2119132199270166781 为已入库 2119132001953325177（Hole Wall）的续帖，skip。nathie most_recent 2119532290501968233 `exclude` 后未返回（回复/转发）。SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（新媒体 Dilmerv Meta VR Glasses creative experiences + 旧 Hand Skate progress / Meta VR Glasses lightness / ISDK Distance Grab / Meta VR Glasses excitement / Hand Skate decorations）。
- 上一有变更档：2026-11-09 12:00 BJT media-kol Dilmerv Hand Skate progress / Meta VR Glasses lightness / ISDK Distance Grab。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-09 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
