# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-24 09:07 PDT（例行 2026-10-25 00:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 24 Oct 2026 16:07:21 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 24 Oct 2026 16:07:21 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-25 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：PICOXR、XREAL_Global、getVITURE、pimaxofficial、VRChat、nathie、Dilmerv、SadlyItsBradley；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+4）：** PICOXR 2114009111339680196；XREAL_Global AURA/Android XR 2114009019967021373；pimaxofficial Dream Air @ Sim Racing Expo 2113994061212156264；VRChat Spookality Awards Show 2113991675840249923。丢掉最旧 4 条（Play_for_dream 2108374501302181962 / MetaVRDevs×2 / VRChat 2108311655998484757）。
- **media-kol 100→100（+1）：** nathie VR mod 2114022656827650248。丢掉最旧 1 条（nathie 2107992789745295830）。
- exclude / 丢弃：getVITURE result_count 0；Dilmerv 通用 agentic/GitHub 非 XR 丢弃 2113805429042229427（newer most_recent 为回复/转发已 exclude）；SadlyItsBradley 续帖 2113732904995996109 已并入根帖 2113731023645102102（不改已发条目；newer most_recent 为回复/转发已 exclude）；VRChat 续帖 2113805497719820555 已并入根帖；nathie iPhone Duo 非 XR 丢弃 2113576600113496449，续帖 2113315923025379458 已并入根帖。
- 监控名单未变（official 15 / media-kol 4）。
- 中间档 2026-10-24 16:00 / 20:00 BJT：预检有更新账号但 exclude/已并入/非 XR 后无入库，feeds 未 commit。
- 上一有变更档 2026-10-24 12:00 BJT：official +1（VRChat Spookality winners），commit 0a7e99e。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-25 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
