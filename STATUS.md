# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-10 08:10 PST（例行 00:00 BJT 2026-11-11）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 10 Nov 2026 16:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 10 Nov 2026 16:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-11 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：PICOXR、RokidGlobal、magicleap、VRChat、BigscreenVR、htcvive、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（XREAL_Global、MetaVRDevs、MetaVR_Official、BeatSaber、getVITURE、Play_for_dream、pimaxofficial、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+3/−3 cap）：** PICOXR Audio Trip major update + DLC 2120185142656340100；RokidGlobal Rokid Glasses trail POV 2120169616966332669；magicleap waveguide fabrication data 2120146962402214039。丢掉最旧 3 条：RokidGlobal CES Las Vegas 2115341770716569859、XREAL_Global Android Dev Summit AURA 2115287671849578778、BeatSaber Ghostbusters environment 2115250452988035453。VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。htcvive / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+3/−3 cap）：** nathie Combat Waffle / VR studio closures 2120186765088817533；SadlyItsBradley IR-transparent filament 2120154827783094651；Dilmerv main character tweaks 2120154603945632197。丢掉最旧 3 条：Dilmerv Meta Connect sunglasses 2116723423694950836、Dilmerv Cubiques VR/MR trailer 2116686712533385363、Dilmerv MRUK World Locking 2116675356937556345。Dilmerv 最新 2120172083619708964 为回复 @lucas_martinic，SadlyItsBradley 最新 2120180947144564755 为回复 @VitaminDeath，均非自串帖。
- top-6 guid 抽查均在（新 official PICOXR Audio Trip 2120185142656340100 / RokidGlobal trail 2120169616966332669 / magicleap waveguide 2120146962402214039；其余 official XREAL AURA 2120035136682987550 / MetaVRDevs prototype 2119909497934356661 / VRChat New Year's 2119893528847233479；新 media-kol nathie VR studio closures 2120186765088817533 / SadlyItsBradley IR filament 2120154827783094651 / Dilmerv character 2120154603945632197；其余 media-kol nathie PICO Space Pro 2120119315223679136 / Dilmerv ISDK vs XRI 2120118049395089869 / Dilmerv Meta VR Glasses interaction 2120096642191778049）。
- 上一有变更档：2026-11-10 20:00 BJT official +0 / media-kol +3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-11 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
