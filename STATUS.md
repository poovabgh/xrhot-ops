# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-14 17:07 PT（例行 08:00 BJT 刷新）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 98 | Thu, 15 Oct 2026 00:07:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 76 | Thu, 15 Oct 2026 00:07:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-15 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVRDevs、Play_for_dream、VRChat、nathie、Dilmerv、SadlyItsBradley。
- **official 96→98（+2）：** MetaVRDevs Immersive Web SDK 1.0（2110465010803605583）；Play_for_dream immersion/FOV（2110415336302391327）。
- **media-kol 71→76（+5）：** SadlyItsBradley Steam Frame OS kernel / Yippee / Deckard-Plano foveated / Making great progress（4）；nathie Steam Frame OLED 引用 FoxletFox（2110408971802865955）。
- 高于 watermark 但 exclude 后无入库：VRChat（仅回复/转发）；Dilmerv（已入库串帖续帖 + 对 Unity 回复）；nathie/SadlyItsBradley 最新为对他人回复。
- 丢弃：SadlyItsBradley 无文字媒体帖×2（211043667、211043925）。
- 监控名单未变（official 15 / media-kol 4）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-15 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
