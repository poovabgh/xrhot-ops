# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-30 01:09 PDT（例行 2026-10-30 16:00 BJT）。

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

## 本轮：2026-10-30 16:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、getVITURE、pimaxofficial、nathie、Dilmerv；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+1）：** pimaxofficial Frontier FAQ Crystal Pro/ringless controllers/Spation 2116041443626131539。丢掉最旧 1 条。BigscreenVR / getVITURE `exclude` 后 result_count 0（最新为回复/RT）。
- **media-kol 100 不变：** nathie / Dilmerv `exclude` 后无新原帖（most_recent 均为回复；Dilmerv 另有自串回复 2115896880756625845 丢掉）。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-30 12:00 BJT：official +7 / media-kol +5（HEAD f2379d6）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-30 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
