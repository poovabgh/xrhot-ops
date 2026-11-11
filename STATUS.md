# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-11 00:07 PST（例行 16:00 BJT 2026-11-11）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 11 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 11 Nov 2026 08:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-11 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、MetaVRDevs、htcvive、BigscreenVR、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、PICOXR_Dev、XREAL_Global、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、magicleap、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** MetaVR_Official / htcvive / BigscreenVR / BeatSaber `exclude` 后 result_count 0。MetaVRDevs `exclude` 后仅返回 2120223376031764914 / 2120223484945244628 / 2120223621759349165，均为已入库 2120223311716364719（2026 VR numbers / Chris Pruett thread）的续帖，已在此前合并，skip。VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。
- **media-kol 100→100（+2/−2 cap）：** Dilmerv Unity XR shader Single-Pass Instanced / stereo macros 2120396165338239472；SadlyItsBradley Gaussian Splats floaters（合并续帖 2120380985594503197 hedges）2120380979940602035。丢掉最旧 2 条：SadlyItsBradley Huge / Quest 2 and Pro EoL 2117324987908440330、nathie Horizon Zero Dawn VR mod 2117323861222162626。nathie `exclude` 后 result_count 0。
- top-6 guid 抽查均在（新 media-kol Dilmerv shader 2120396165338239472 / SadlyItsBradley Gaussian Splats 2120380979940602035；其余 Dilmerv occlusion 2120344565781614941 / Dilmerv FOV sim 2120328228577436006 / Dilmerv SDKs + competition 2120313165699281006 / nathie Disney+ 2120302292112969841）。
- 上一有变更档：2026-11-11 12:00 BJT official +0 / media-kol +3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-11 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
