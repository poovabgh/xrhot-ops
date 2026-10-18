# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-17 17:09 PDT（例行 2026-10-18 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 18 Oct 2026 00:09:24 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 91 | Sun, 18 Oct 2026 00:09:24 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-18 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、pimaxofficial、Play_for_dream、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；PICOXR_Dev most_recent 未变、仍无 feed 条目，不回溯。
- **official 100→100（+4：VRChat Spookality 邀请 2111546004361334792；BeatSaber Ghostbusters/Ghost Notes 2111533119014600775；pimaxofficial Simracing Expo 2111532720601841721；BigscreenVR Index 手柄指南 2111501740009034228；顶掉最旧 4 条）。**
- **media-kol 87→91（+4：Dilmerv Meta XR Simulator 2111570325855175084；Dilmerv Blender MCP / Hand Skate MR 2111550087809978412；nathie Real VR Fishing 串帖合成 2111507588214902900；SadlyItsBradley Vision Pro RC Scarab 2111494768840835554）。**
- 高于 watermark 但 exclude / 已入库串帖续帖后无入库：Play_for_dream（exclude 0）；VRChat Spookality 串帖续帖 2111200616886526227 / 2111200615040729239；nathie C&C VR mod 串帖续帖 2110768324309303719。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-18 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
