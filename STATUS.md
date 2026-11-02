# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-02 08:08 PST（例行 2026-11-03 00:00 BJT）。

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

## 本轮：2026-11-03 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：XREAL_Global、RokidGlobal、getVITURE、BeatSaber、BigscreenVR、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 99→100（+2）：** RokidGlobal Glasses voice/music 2117270520253095949 / XREAL_Global 1 Pro+ Amazon 2117240872991342991；丢掉最旧 1 条。getVITURE / BeatSaber / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+3）：** ARealityEvent UnitedXR Europe 2117257465423409441 / SadlyItsBradley Steam Frame survey 2117250717618483425 / Dilmerv ISDK pinch grab HandGrabExamples 2117232898449326584；丢掉最旧 3 条。Dilmerv XR-devs motivation drop；nathie `exclude` 后 result_count 0。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-11-02 20:00 BJT：media-kol +2 Dilmerv（HEAD f9f6559）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-03 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
