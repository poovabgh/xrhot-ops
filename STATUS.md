# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-21 01:05 PDT（例行 2026-10-21 16:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 21 Oct 2026 04:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 21 Oct 2026 08:05:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-21 16:00 BJT

- 预检 19 账号；最新 id 高于 watermark：RokidGlobal、htcvive、VRChat、getVITURE、Play_for_dream、MetaVR_Official、Dilmerv、nathie、SadlyItsBradley；LensStudioDev most_recent 仍为已出队旧帖，不回溯。
- **official 100 不变。** exclude / 无新原创：RokidGlobal / htcvive / getVITURE / Play_for_dream / MetaVR_Official / SadlyItsBradley result_count 0；VRChat 仅 Thirst Killer 续帖 2112597788831924697（根帖已入库）；nathie SPECS 续帖 2112574076833108015 根帖已合并。
- **media-kol 100→100（+2）：** Dilmerv Hand Pose Baking for Meta VR Glasses 2112800102712775157；Dilmerv quote MetaVRDevs Unscripted / Meta Connect agentic workflows 2112769827605828079；丢掉最旧 2 条（SadlyItsBradley 2107477263210217493 / 2107476845478207629）。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-21 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
