# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-28 09:04 PDT（例行 2026-10-29 00:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-29 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：PICOXR、XREAL_Global、MetaVRDevs、VRChat、ARealityEvent、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+1）：** PICOXR headset care tips 2115458752539242783。丢掉最旧 1 条（2110046191442428387 htcvive）。XREAL_Global / MetaVRDevs / VRChat `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+4）：** ARealityEvent UnitedXR Europe Enterprise VIP 2115458570737385579；SadlyItsBradley 4DGS workflow quote 2115451725603885397；Dilmerv SDK/AI walkthrough 串帖合成 2115444591390507201；Dilmerv unfinished XR projects 2115437691823067382。丢掉最旧 4 条（2110232719900708875 Dilmerv / 2110140656509161814 SadlyItsBradley / 2110099934250971300 nathie / 2110022104569557172 SadlyItsBradley）。SadlyItsBradley Deadlock map 2115229006073078194 非 XR 游戏丢弃（同前轮）。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-28 16:00 BJT：official +2；media-kol +1（HEAD 3964f57）；20:00 BJT 静默无提交。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-29 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
