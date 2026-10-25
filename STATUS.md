# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-24 17:03 PDT（例行 2026-10-25 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 25 Oct 2026 00:02:49 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 25 Oct 2026 00:02:49 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-25 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：getVITURE、VRChat、nathie、Dilmerv、SadlyItsBradley；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+1）：** VRChat Spookality Awards Show live + 续帖合并 2114069428853965255。丢掉最旧 1 条（RokidGlobal 2108573199268987000）。
- **media-kol 100→100（+6）：** SadlyItsBradley VRChat→Splattery 2114114352035033091；Dilmerv Cubiques gaze + Meta XR Simulator 资源 2114100282154156373；nathie Duolingo XR 2114077508249256216；SadlyItsBradley Quest 2114067287770882121；SadlyItsBradley 2026 Modernized（引 VRChat Workrooms）2114053357493199030；Dilmerv Cubiques MR/MRUK+Gaze 2114037069341421726。丢掉最旧 6 条（SadlyItsBradley×2 / Dilmerv×3 / ARealityEvent）。
- exclude / 丢弃：getVITURE result_count 0；Dilmerv 通用 agentic/GitHub 非 XR 仍丢弃 2113805429042229427；SadlyItsBradley 续帖 2113732904995996109 已并入根帖 2113731023645102102（不改已发条目）；Dilmerv newer most_recent 2114107949052502084 为回复/转发已 exclude。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-25 00:00 BJT：official +4 / media +1，commit 455bcdb。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-25 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
