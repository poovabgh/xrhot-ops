# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-13 20:12 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 95 | Tue, 13 Oct 2026 04:02:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 76 | Tue, 13 Oct 2026 12:11:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-13 20:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；9 个最新 id 高于 watermark；`exclude=replies,retweets` 后有原创候选的：nathie、benz145、SadlyItsBradley、VRChat（串帖回复）；BigscreenVR / rayneo_global / Dilmerv / kentbye / Flat2VR 为 0。
- **official：** 95→**95**（不变）
- **media-kol：** 75→**76**（+1）
  - nathie `2109919763099234445`：Max Payne in VR is a wild experience
- 丢弃：VRChat Treats clarifying reply（回复不单列）；benz145 机场卫生间（非 XR）；SadlyItsBradley Halo3 scarab 桌面 fidget + 无 XR 语境短视频

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-14 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
