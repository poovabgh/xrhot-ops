# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-22 01:07 PDT（例行 2026-10-22 16:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 21 Oct 2026 16:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 22 Oct 2026 08:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-22 16:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、getVITURE、Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley；LensStudioDev most_recent 仍为已出队旧帖，不回溯；其余等于 watermark 跳过。
- **official 100 不变：** MetaVR_Official / htcvive / getVITURE / Play_for_dream exclude 后 result_count 0；VRChat 仅 Thirst Killer 续帖（根帖已合并入库）。
- **media-kol 100→100（+1）：** Dilmerv Hand Grab Pose Baker IK 演示 2113140426890993809；丢掉最旧 Dilmerv Unity 7 alpha 2107592317146472870。
- exclude / 丢弃 / 已合并：SadlyItsBradley 最新为回复/转发 exclude 0；Dilmerv Fuse Balls 续帖已合并；nathie SPECS 续帖已合并；nathie「Happy Back to the Future Day!」2112979617707336165 非 XR 丢弃。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-22 12:00 BJT：official / media-kol 均无入库变化（仍 62ef48c）。
- 再上一档 2026-10-22 08:00 BJT：media-kol +1（SadlyItsBradley Gaussian Splat），commit 62ef48c。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-22 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
