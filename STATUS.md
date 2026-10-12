# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-12 20:14 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 88 | Mon, 12 Oct 2026 12:14:38 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 70 | Mon, 12 Oct 2026 08:07:51 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-12 20:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；11 个最新 id 高于 watermark；`exclude=replies,retweets` 后有原创候选的：XREAL_Global、pimaxofficial、benz145、SadlyItsBradley；其余为回复/转发或 0。
- **official：** 86→**88**（+2）
  - XREAL_Global `2109615071043244250`：XREAL AURA / FXG founder vibe coding 故事
  - pimaxofficial `2109612121134698697`：2026 SimRacing Expo Frankfurt 头显展示
  - 丢弃：htcvive / BigscreenVR / rayneo_global / VRChat / Dilmerv / kentbye / Flat2VR 最新为回复或转发（拉原创 0）
- **media-kol：** **70 不变**
  - 丢弃：benz145 机场卫生间（非 XR）、SadlyItsBradley 宠物厨房（非 XR）

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-13 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye / Flat2VR 等低产出账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
