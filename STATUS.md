# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-18 21:05 PDT（例行 2026-10-19 12:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 19 Oct 2026 00:06:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 97 | Mon, 19 Oct 2026 04:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-19 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley；PICOXR_Dev most_recent 未变（2105447602997354733）、仍无 feed 条目，不回溯。
- **official 100 不变。**
- **media-kol 96→97（+1）：** SadlyItsBradley VRChat desk portal / spatial computing 2112008731617624085。
- 高于 watermark 但 exclude / 已入库串帖续帖后无入库：Play_for_dream / VRChat / Dilmerv exclude 后 0；nathie Real VR Fishing 串帖续帖 2111508094346002895（根帖已合并，本轮无改）；SadlyItsBradley 另有更新 id 2112015505896943976 为回复/转发被 exclude。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-19 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
