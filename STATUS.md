# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-11 04:06 PST（例行 20:00 BJT 2026-11-11）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 11 Nov 2026 12:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 11 Nov 2026 12:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-11 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：pimaxofficial、MetaVRDevs、VRChat、MetaVR_Official、BeatSaber、BigscreenVR、htcvive、Dilmerv、SadlyItsBradley、nathie；其余等于 watermark 跳过（PICOXR、PICOXR_Dev、XREAL_Global、RokidGlobal、getVITURE、Play_for_dream、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+1/−1 cap）：** pimaxofficial Buy early / Black Friday price protection 2120465299539361908。丢掉最旧 1 条：XREAL_Global A new chapter for Android XR 2115507076671914376。MetaVR_Official / BeatSaber / BigscreenVR / htcvive `exclude` 后 result_count 0。MetaVRDevs `exclude` 后仅返回 2120223376031764914 / 2120223484945244628 / 2120223621759349165，均为已入库 2120223311716364719（2026 VR numbers / Chris Pruett thread）的续帖，已在此前合并，skip。VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv MetaVR CLI network-impairment / Quest 150 ms delay sim 2120433962115801496。丢掉最旧 1 条：SadlyItsBradley WebXR Steam Frame Chromium 2117327521247338568。nathie `exclude` 后 result_count 0。SadlyItsBradley `exclude` 后仅返回 2120380985594503197，为已入库 2120380979940602035（Gaussian Splats floaters）的续帖（hedges），已在此前合并，skip。
- top-6 guid 抽查均在（新 official pimaxofficial Buy early 2120465299539361908；新 media-kol Dilmerv MetaVR CLI 2120433962115801496；其余 official pimaxofficial Black Friday 2120241914658308117 / pimaxofficial IAAPA 2120241367494373761 / XREAL Innervoice 2120230928467304646 / MetaVRDevs 2026 numbers 2120223311716364719 / XREAL Nutcracker 2120212983888371721；其余 media-kol Dilmerv shader 2120396165338239472 / SadlyItsBradley Gaussian Splats 2120380979940602035 / Dilmerv occlusion 2120344565781614941 / Dilmerv FOV sim 2120328228577436006 / Dilmerv SDKs + competition 2120313165699281006）。
- 上一有变更档：2026-11-11 16:00 BJT official +0 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-12 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
