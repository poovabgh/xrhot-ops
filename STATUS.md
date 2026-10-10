# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-10 PT 凌晨 / 北京 2026-10-10 16:00 例行（四次采集）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 52 | Sat, 10 Oct 2026 02:25:56 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 36 | Sat, 10 Oct 2026 08:05:38 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮例行刷新（2026-10-10 北京 16:00）

- 方法：`get_users_by_usernames` 廉价预检 → 仅对最新 id 更新的账号 `get_users_posts(since_id, exclude=replies,retweets)` → XR 初筛。
- 官方：**+0**（htcvive / BigscreenVR 最新为回复或转发；其余 9 账号无新 id）。
- 媒体/KOL：**+1**（nathie：The Last of Us Part II VR support 串帖合并；Dilmerv 最新为回复/转发；ARealityEvent 无新 id；kentbye 抽查近期原创无新于例行窗口、未回填历史）。
- 已 push：是（见 git log）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：按日历取下一个 08/12/16/20:00。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye 等长期无帖账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
