# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-23 01:10 PDT（例行 2026-10-23 16:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 23 Oct 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 23 Oct 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-23 16:00 BJT

- 预检 19 账号；最新 id 高于 watermark：XREAL_Global、RokidGlobal、Play_for_dream、ARealityEvent、nathie、Dilmerv；MetaVR_Official / LensStudioDev 无 feed watermark（most_recent 为回复或已出队旧帖，不回溯）；其余等于 watermark 跳过。
- **official 100→100（+1）：** RokidGlobal Rokid Glasses AI Agent Jam（Singapore）2113542566360834093。丢掉最旧 1 条。
- **media-kol 100→100（+1）：** ARealityEvent Weekly Spatial（SPECS / UnitedXR Europe）2113527055493304395。丢掉最旧 1 条。
- exclude / 丢弃 / 已合并：XREAL_Global / Play_for_dream / Dilmerv exclude 后 result_count 0；nathie 续帖 2113315923025379458 已并入根帖 2113315308299513970；MetaVR_Official 最新原创仍为旧档（不回溯）。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-23 12:00 BJT：无变更、无 commit（仍 3f9b6e9）；再上一档 08:00 BJT：official +5、media-kol +6，commit 3f9b6e9。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-23 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
