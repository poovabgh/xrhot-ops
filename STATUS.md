# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-16 21:10 PDT（例行 12:00 BJT 2026-10-17 刷新）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 17 Oct 2026 04:09:38 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 87 | Sat, 17 Oct 2026 00:10:22 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-17 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：PICOXR、XREAL_Global、Play_for_dream、VRChat、nathie、Dilmerv；PICOXR_Dev 无 feed 记录抽查。
- **official 100→100（+1 XREAL_Global Founder Priority Pass / AURA 终呼 2111273654176936209；顶掉最旧 1 条）。**
- **media-kol 87 不变。**
- 高于 watermark 但 exclude / 初筛后无入库：PICOXR（已入库 Project Hail Mary 串帖续帖）；Play_for_dream（仅回复/转发）；VRChat（已入库 Spookality 串帖续帖）；nathie（已入库 C&C VR mod 串帖续帖）；Dilmerv（exclude 后 0）；PICOXR_Dev（most_recent 未变、仍无 feed 条目，本轮不回溯入库）。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-17 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
