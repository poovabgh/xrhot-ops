# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-13 12:03 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 95 | Tue, 13 Oct 2026 04:02:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 75 | Tue, 13 Oct 2026 00:12:58 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-13 12:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；9 个最新 id 高于 watermark；`exclude=replies,retweets` 后有原创候选的：XREAL_Global、benz145、SadlyItsBradley；BigscreenVR / rayneo_global / VRChat（串帖回复）/ Dilmerv / kentbye / Flat2VR 为 0 或仅回复/转发。
- **official：** 94→**95**（+1）
  - XREAL_Global `2109827138413093034`：AR glasses 工作 POV（#XREAL #ARGlasses）
- **media-kol：** 75→**75**（不变）
- 丢弃：benz145 机场卫生间（非 XR）；SadlyItsBradley Halo3 scarab 桌面 fidget / 无 XR 语境短视频；VRChat Treats 澄清回复（回复不单列）

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-13 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye / Flat2VR 等低产出账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
