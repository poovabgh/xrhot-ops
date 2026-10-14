# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-14 16:12 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 14 Oct 2026 04:10:32 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 82 | Wed, 14 Oct 2026 08:11:57 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-14 16:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；9 个最新 id 高于 watermark：Play_for_dream、VRChat、rayneo_global、nathie、Dilmerv、kentbye、benz145、Flat2VR、SadlyItsBradley。
- `exclude=replies,retweets` 后有原创：Dilmerv×2（自串合成 1）；benz145×2（非 XR，丢）。Play_for_dream / VRChat / rayneo_global / nathie / kentbye / Flat2VR / SadlyItsBradley 为 0。
- **official：** 100→**100** 不变
- **media-kol：** 81→**82**（+1 Dilmerv MR 桌面游戏串帖合成 2110232719900708875）
- 丢弃：benz145 旗舰手机形态幻想 / 机场卫生间（同前几轮，仍非 XR）

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-14 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
