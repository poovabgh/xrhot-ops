# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-10 PT / 北京时间例行刷新（20:00 节点）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 83 | Sun, 11 Oct 2026 00:06:26 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sun, 11 Oct 2026 00:06:26 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：例行刷新（2026-10-10 PT ≈ 北京 20:00）

- 廉价预检：`get_users_by_usernames` → 仅对 most_recent_tweet_id > feed max guid 的账号 `get_users_posts(exclude=replies,retweets, since_id)`
- official +3：rayneo_global、pimaxofficial、RokidGlobal（feed 80→83）
- media-kol +4：SkarredGhost、nathie、Dilmerv、SadlyItsBradley（截断保持 100）
- 丢掉：SkarredGhost Anthropic/Claude 一般 AI 帖；自回帖/串帖续写不改已发布 guid；多数「有更新」实为回复/转发

### 本轮 seen / kept

| Handle | 看了 | 留下 |
|--------|-----:|-----:|
| RokidGlobal | 1 | 1 |
| rayneo_global | 1 | 1 |
| pimaxofficial | 1 | 1 |
| VRChat | 1 | 0（自回帖，不改已有项） |
| htcvive | 0 originals | 0 |
| BigscreenVR | 0 originals | 0 |
| nathie | 2 | 1 |
| Dilmerv | 1 | 1 |
| SkarredGhost | 2 | 1 |
| SadlyItsBradley | 1 | 1 |
| benz145 | 0 originals | 0 |
| CasandChary | 0 originals | 0 |
| Flat2VR | 0 originals | 0 |
| kentbye / VRDesktop | 抽样无新于 feed 窗口 | 0 |

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
