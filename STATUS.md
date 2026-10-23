# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-22 17:10 PDT（例行 2026-10-23 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 23 Oct 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 23 Oct 2026 00:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-23 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、PICOXR、htcvive、getVITURE、Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley；LensStudioDev most_recent 仍为已出队旧帖，不回溯；其余等于 watermark 跳过。
- **official 100→100（+5）：** VRChat Oct 22 Dev Update 2113383235598110724；getVITURE SpaceWalker 3.0 Beta 2113364266732696033；VRChat Spookality livestream reminder 2113344845569749180；htcvive VIVE Eagle 15% off 2113314422869426650；PICOXR Fixer Undercover 2113307002726236483。丢掉最旧 5 条。
- **media-kol 100→100（+6）：** SadlyItsBradley HLX queue 2113389888498229459；Dilmerv Fuse Balls Meta Store submit skill 2113361945302913391；SadlyItsBradley HLX quote Tyler_McV 2113333764168569138；SadlyItsBradley PCVR Streamer passthrough recolor 2113318461971828770；nathie VR podracing（含续帖）2113315308299513970；SadlyItsBradley Vision Pro PCVR streaming 2113302629606461583。丢掉最旧 6 条。
- exclude / 丢弃 / 已合并：MetaVR_Official / Play_for_dream exclude 后 result_count 0；nathie SPECS 续帖 2112574076833108015 已合并；nathie「Happy Back to the Future Day!」2112979617707336165 非 XR 丢弃；nathie podracing 续帖 2113315923025379458 合并入根帖。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-23 00:00 BJT：official +3、media-kol +1，commit b998d04。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-23 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
