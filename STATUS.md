# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-09 16:15 PST（例行 08:00 BJT 2026-11-10）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 10 Nov 2026 00:15:00 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 10 Nov 2026 00:15:00 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-10 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVRDevs、htcvive、BigscreenVR、XREAL_Global、RokidGlobal、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（MetaVR_Official、PICOXR、PICOXR_Dev、getVITURE、pimaxofficial、Play_for_dream、magicleap、BeatSaber、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+6/−6 cap）：** MetaVRDevs Meta VR Glasses prototype 2119909497934356661；VRChat New Year's Entertainment Network 2119893528847233479（合并续帖 2119893530722140614）；XREAL_Global Glossa language case 2119868911281754378；MetaVRDevs reviews/build 2119866328047890651；MetaVRDevs Developer Competition 2119856412255981927；XREAL_Global Idle Hero Drummer 2119838644865302803。丢掉最旧 6 条：BigscreenVR No Base Stations 2115219525843247443、htcvive Pick your color 2115155446482817172、pimaxofficial Built for long sessions 2115145755203715515、VRChat Ready to party this Halloween 2115137647970800092、VRChat For the VRChat Collectors 2115079649050906798、pimaxofficial Comfort Kit 2114974709129650285。RokidGlobal / BigscreenVR / htcvive `exclude` 后 result_count 0。
- **media-kol 100→100（+4/−4 cap）：** SadlyItsBradley Splattery edit mode / Logitech Muse 2119866605794382181；nathie Apple Vision Pro holodeck 2119864306376589352；Dilmerv Unity 7 VR/MR workflows 2119852941209489491；Dilmerv Meta VR Glasses ISDK tip 2119833998067163309。丢掉最旧 4 条：Dilmerv XR devs quick tip 2116542778184479108、Dilmerv prototyping 2116363312963194911、Dilmerv Spider Web 2116315964350591037、Dilmerv Cubiques iOS to VR 2116239926434140561。nathie 2119391299308577274 为已入库 2118316089738469467（Zelda first-person VR）的续帖，skip。nathie 2119132199270166781 为已入库 2119132001953325177（Hole Wall）的续帖，skip。nathie most_recent 2119909376681210066、Dilmerv most_recent 2119881649055990204、SadlyItsBradley most_recent 2119881196855504924 `exclude` 后未作为独立原创返回（回复/转发）。
- top-6 guid 抽查均在（新 official MetaVRDevs prototype 2119909497934356661 / VRChat New Year's 2119893528847233479 / XREAL Glossa 2119868911281754378 / MetaVRDevs reviews 2119866328047890651 / MetaVRDevs competition 2119856412255981927 / XREAL Idle Hero Drummer 2119838644865302803）。
- 上一有变更档：2026-11-10 00:00 BJT official PICOXR PICO Store Wish List。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-10 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
