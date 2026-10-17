# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-17 08:23 PDT（例行补刷：漏掉的 16:00/20:00 BJT 节点，于 23:23 BJT 附近完成）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 17 Oct 2026 15:23:58 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 87 | Sat, 17 Oct 2026 00:10:22 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-17 补刷（覆盖漏掉的 16:00/20:00 BJT）

- 预检 19 账号；最新 id 高于 watermark：PICOXR、RokidGlobal、Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley；PICOXR_Dev most_recent 未变、仍无 feed 条目，不回溯。
- **official 100→100（+2：PICOXR 多人联机宣传 2111472393231216688；RokidGlobal 香港旗舰店体验 2111472306782445709；顶掉最旧 2 条）。**
- **media-kol 87 不变**（SadlyItsBradley / Dilmerv / nathie 高于 watermark 但 exclude 后为 0 或仅串帖续帖）。
- 高于 watermark 但 exclude / 初筛后无入库：Play_for_dream（仅回复/转发）；VRChat（已入库 Spookality 串帖续帖）；nathie（已入库 C&C VR mod 串帖续帖）；Dilmerv（exclude 后 0）；SadlyItsBradley（exclude 后 0）。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-18 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
