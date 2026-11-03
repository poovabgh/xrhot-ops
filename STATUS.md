# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-02 16:11 PST（例行 2026-11-03 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-03 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、MetaVRDevs、BigscreenVR、getVITURE、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+2）：** getVITURE PCMag Smart Glasses Gift 2117343081527988417 / MetaVRDevs Quest 2+Pro EOF feature 2117332750395232649；丢掉最旧 2 条。MetaVR_Official / BigscreenVR / VRChat / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+12）：** SadlyItsBradley AVP SteamVR Link 2117370134788718640 / chroma passthrough 2117369162792136932 / SteamVR 2.19.1 Beta（合串）2117364399132545432 / Frame Lepton decode 2117354689872154824 / WebXR Chromium 2117327521247338568 / Huge Quest EOF quote 2117324987908440330；Dilmerv XR feature Q 2117368772201742555 / MR room adapt 2117342264556965913 / Cubiques store 2117334958565974368 / VR-MR interaction 2117316441292652799；nathie Quest EOF quote 2117346754295423294 / HZD VR mod 2117323861222162626；丢掉最旧 12 条。nathie self-thread reply drop；Dilmerv XR-devs motivation drop；Bradley patch-notes 自回复合入 Beta 根帖。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-11-03 00:00 BJT：official +2 Rokid/XREAL；media-kol +3 AWE/Bradley/Dilmerv（HEAD 24c13f0）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-03 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
