# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-15 21:09 PDT（例行 12:00 BJT 2026-10-16 刷新）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 15 Oct 2026 16:10:45 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 81 | Fri, 16 Oct 2026 04:09:51 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-16 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：Play_for_dream、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley。
- **official 100→100 不变。**
- **media-kol 80→81（+1）：** SadlyItsBradley 引用 Somnium Connect / Social VR（2110945856589602968）。
- 高于 watermark 但 exclude 后无入库：Play_for_dream、VRChat、BeatSaber（仅回复/转发）；nathie（已入库串帖续帖）；Dilmerv（已入库串帖续帖）；SadlyItsBradley 另有媒体帖+自回丢弃。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-16 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
