# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-15 00:04 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 14 Oct 2026 16:04:18 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 88 | Wed, 14 Oct 2026 16:04:18 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-15 00:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；11 个最新 id 高于 watermark：PICOXR、RokidGlobal、rayneo_global、Play_for_dream、VRChat、nathie、Dilmerv、kentbye、benz145、Flat2VR、SadlyItsBradley。
- `exclude=replies,retweets` 后有原创入库：PICOXR×1、RokidGlobal×1、SadlyItsBradley×4（Deckard-Plano 串帖合成 1 + 自引 1 + OLED 引用 1 + 短视频 1）、benz145×2（Quest 游戏引用 + SteamVR 头显龄）。Dilmerv 仅为已入库串帖续帖；rayneo_global / Play_for_dream / VRChat / nathie / kentbye / Flat2VR 为 0。
- **official：** 100→**100**（+2 PICOXR 2110385283392778519、RokidGlobal 2110385141608825040；cap 丢掉最旧 XREAL_Global 2104782937967177863、RokidGlobal 2104753034194804741）
- **media-kol：** 82→**88**（+6）
- 丢弃非 XR：benz145 TrellisWM Mac 窗口管理器引用 / 旗舰手机形态幻想 / 机场卫生间

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-15 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
