# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-20 17:05 PDT（例行 2026-10-21 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 21 Oct 2026 00:03:52 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 21 Oct 2026 00:03:52 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-21 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、getVITURE、Play_for_dream、MetaVRDevs、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；PICOXR_Dev most_recent 未变（2105447602997354733）、仍无 feed 条目，不回溯；LensStudioDev most_recent 仍为已出队旧帖。
- **official 100→100（+4）：** MetaVRDevs Unscripted ep.1 agentic VR tools 2112667703203021055；htcvive Kyle Berkshire × VIVE Eagle 2112650720465825822；BeatSaber spooky season 2112650669299478704；VRChat Thirst Killer referral（串帖续帖合并）2112597785472270406；丢掉最旧 4 条（含 XREAL_Global 2107365703363826114）。
- **media-kol 100→100（+3）：** Dilmerv Hand Skate Meta VR Glasses 2112679677718577510；Dilmerv Meta Fury sunglasses OC capture 2112663359611121756；Dilmerv quote SPECS×RDJ / Iron Man UI 2112652056679092513；丢掉最旧 3 条。
- 高于 watermark 但 exclude / 串帖续帖后无新入库：MetaVR_Official / getVITURE / Play_for_dream / SadlyItsBradley exclude 后 0；nathie SPECS 续帖 2112574076833108015 与 Dilmerv passthrough 续帖 2112568359497892225 根帖已合并，本轮无改。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-21 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
