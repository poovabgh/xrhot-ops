# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-07 16:15 PST（例行 08:00 BJT 2026-11-08）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 08 Nov 2026 00:15:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 08 Nov 2026 00:15:46 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-08 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：XREAL_Global、BigscreenVR、htcvive、MetaVRDevs、Dilmerv、SadlyItsBradley、nathie；其余等于 watermark 跳过（VRChat、MetaVR_Official、BeatSaber、RokidGlobal、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR_Dev、ARealityEvent）。PICOXR most_recent（2118372937203884362）低于 watermark（2119097674494349523），核对后 Wish List 2119097674494349523 API Not Found，从 official 删除。
- **official 100→100（+3/−1 delete/−2 cap）：** XREAL_Global Sock Puppet Superstar / AURA hand tracking 2119173637726978097；XREAL_Global BRINK Traveler / AURA 2119143981422362899；XREAL_Global AMAZE VR Concerts / AURA 2119113739777487009。删除已删帖 PICOXR Wish List 2119097674494349523。丢掉最旧 2 条：VRChat referral program 2114850030842761366、MetaVRDevs NordVPN on Meta Quest 2114779978235884019。BigscreenVR / htcvive / MetaVRDevs `exclude` 后 result_count 0。
- **media-kol 100→100（+4/−4 cap）：** Dilmerv Unity gaze+pinch / Meta ISDK 2119195793881981396；Dilmerv Quest 3 vital demo / Mario64 MR quote 2119156585301983395；nathie Meta Quest Hole Wall 2119132001953325177（续帖 Wishlist 2119132199270166781 合成一条）；Dilmerv Meta VR Glasses 现有 Quest 应用 / Horizon OS v207 SDK 2119105199612584096。丢掉最旧 4 条：Dilmerv XR quality 2115611906186911782、Dilmerv XREAL/Android XR congrats 2115605676869431672、SadlyItsBradley PCVR Streamer Vision Pro TestFlight 2115599863455035570、Dilmerv Meta VR Glasses FoV Simulator 2115599523791708495。Dilmerv 丢弃：健身 2119174304558444609、泛 AI 2119165573460353378、泛科技 2119151660110877091、泛想象力/AI 工具 2119127795217379792、健身 2119127561112260982。nathie 2118827795132580291 为已入库 2118827306160377980 的续帖，skip。SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（新 XREAL Sock/BRINK/AMAZE + 旧 VRChat Dice Party / XREAL Fishing / XREAL board；新媒体 Dilmerv ISDK / Quest3 quote / nathie Hole Wall / Dilmerv Glasses SDK + 旧 Dilmerv 100g×2）。
- 上一有变更档：2026-11-08 00:00 BJT official PICOXR wishlist + VRChat Dice Party，media-kol Dilmerv Meta VR Glasses×3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-08 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
