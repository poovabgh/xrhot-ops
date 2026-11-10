# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-10 04:10 PST（例行 20:00 BJT 2026-11-10）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 10 Nov 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 10 Nov 2026 12:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-10 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark：RokidGlobal、VRChat、BigscreenVR、htcvive、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（XREAL_Global、MetaVRDevs、PICOXR、MetaVR_Official、BeatSaber、getVITURE、magicleap、Play_for_dream、pimaxofficial、PICOXR_Dev、ARealityEvent）。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** VRChat `exclude` 后仅返回 2119893530722140614，为已入库 2119893528847233479（New Year's Entertainment Network）的续帖，已在此前合并，skip。htcvive / BigscreenVR / RokidGlobal `exclude` 后 result_count 0。
- **media-kol 100→100（+3/−3 cap）：** nathie PICO Space Pro December 2 2120119315223679136；Dilmerv Unity ISDK vs XRI + XR Hands 2120118049395089869；Dilmerv Meta VR Glasses interaction 2120096642191778049。丢掉最旧 3 条：Dilmerv never lose curiosity 2116661499972227386、nathie Hauntify 2116647626107945201、Dilmerv inspire others 2116630042864165122。SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（新 media-kol nathie PICO Space Pro 2120119315223679136 / Dilmerv ISDK vs XRI 2120118049395089869 / Dilmerv Meta VR Glasses interaction 2120096642191778049；其余 media-kol Dilmerv Unite Tokyo 2120065176833544478 / Dilmerv competition 2120022444857561331 / Dilmerv Hand Skate environmental objects 2119988459481837926；official 未变，顶条仍为 XREAL AURA 2120035136682987550 / MetaVRDevs prototype 2119909497934356661 / VRChat New Year's 2119893528847233479）。
- 上一有变更档：2026-11-10 16:00 BJT official +1 / media-kol +2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-11 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
