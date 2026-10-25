# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-25 09:04 PDT（例行 2026-10-26 00:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sun, 25 Oct 2026 16:04:13 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 25 Oct 2026 12:06:22 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-26 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：XREAL_Global、getVITURE、pimaxofficial、VRChat、Dilmerv、SadlyItsBradley；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+2）：** XREAL_Global AURA 2114371405743604078；pimaxofficial Dream Air SE @ Sim Racing Expo 2114356460700250347。丢掉最旧 2 条（PICOXR 2108573382174273985 / pimaxofficial 2108573200518897936）。getVITURE `exclude` 后 result_count 0；VRChat 续帖 2114080260677591221（Awards live 根帖已发，不改写）。
- **media-kol 100 不变：** SadlyItsBradley `exclude` 后 result_count 0；Dilmerv most_recent 为纯转发（RT 2114371581590081754），续帖 2114104864615907737 / 2114100284431712266（Cubiques 根帖已发，不改写）。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-25 20:00 BJT：media +1 nathie，commit 2835d54。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-26 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
