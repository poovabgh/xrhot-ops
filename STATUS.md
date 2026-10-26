# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-26 05:15 PDT（例行 2026-10-26 20:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Mon, 26 Oct 2026 04:06:07 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Mon, 26 Oct 2026 12:14:55 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-26 20:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、RokidGlobal、getVITURE、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100 不变：** BigscreenVR / RokidGlobal / getVITURE / BeatSaber `exclude` 后 result_count 0；VRChat 续帖 2114080260677591221（Awards live 根帖已合入，不改写）。
- **media-kol 100→100（+1 Dilmerv）：** YouTube 选题投票（gaze / spatial anchors / hand grab / MR↔VR）2114687508659249594；丢掉最旧 SadlyItsBradley 2108657026259947842。nathie / SadlyItsBradley `exclude` 后 result_count 0。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-26 12:00 BJT：official +1 Rokid；media-kol +5 Dilmerv。中间 16:00 BJT 预检无入库（静默，HEAD 仍 767cf1e）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-27 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
