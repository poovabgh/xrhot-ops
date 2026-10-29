# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-29 01:10 PDT（例行 2026-10-29 16:00 BJT）。

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

## 本轮：2026-10-29 16:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、XREAL_Global、nathie、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+2）：** XREAL_Global AURA×Google collab video 2115692609624756310 / AURA live Best Buy 2115682560135082005。丢掉最旧 2 条。BigscreenVR `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100 不变：** nathie `exclude` 后 result_count 0；SadlyItsBradley 仅自串 Discord 回复（父帖 StrandXR 已在 feed）丢掉，且 most_recent 其余为 RT/回复已 exclude。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-29 12:00 BJT：official +9；media-kol +10（HEAD bf0dc98）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-29 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
