# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-16 17:10 PDT（例行 08:00 BJT 2026-10-17 刷新）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 17 Oct 2026 00:10:22 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 87 | Sat, 17 Oct 2026 00:10:22 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-17 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：PICOXR、Play_for_dream、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley。
- **official 100→100（+2 VRChat Spookality 2026 串帖 2111200613358772644、BeatSaber Halloween 2111161123277803552；顶掉最旧 2 条）。**
- **media-kol 85→87（+2 SadlyItsBradley Halo Scarab/Hornets 2111209658635391472、Dilmerv Oculus Integration swag 2111132714288259578）。**
- 高于 watermark 但 exclude / 初筛后无入库：PICOXR（已入库 Project Hail Mary 串帖续帖）；Play_for_dream（仅回复/转发）；nathie（已入库 C&C VR mod 串帖续帖）；Dilmerv（已入库 MR 桌面游戏串帖续帖）；SadlyItsBradley RC Truck（无 XR 上下文丢弃）。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-17 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
