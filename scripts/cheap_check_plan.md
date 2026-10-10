# 省 token 刷新：先廉价预检，再按需拉正文

## 目标

不要每次对全部账号做全量时间线对比与全文展开。先判断「有没有比 feed 里更新的帖」，只对**新 id**拉全文并初筛。

## 推荐流程（已在 2026-10-10 手动刷新中验证）

1. **读本地 guid**  
   从 `feeds/x-official.xml` / `feeds/x-media-kol.xml` 解析每个 `dc:creator` 的最大 `<guid>`（帖子 ID），得到 `since_id` 候选。

2. **批量解析 handle → user id + 最新帖 id（1 次 API）**  
   调用 X 工具 `get_users_by_usernames`（或等价），字段含 `most_recent_post_id` / `most_recent_tweet_id`。  
   - 若 `most_recent_tweet_id <= 该账号 feed 内 max guid` → **跳过**该账号。  
   - 若无 feed 记录（如长期无帖的 kentbye）→ 仍用 `get_users_posts` 抽查少量近期原创，避免漏。

3. **仅对「可能有新帖」的账号拉时间线头**  
   `get_users_posts`：`exclude=replies,retweets`，`since_id=<该账号 max guid>`，`max_results` 宜小（10–20）。  
   - `result_count=0`：最新帖只是回复/转发 → **无入库**。  
   - 返回的 id 若已在任一 feed 的 guid 集合中 → 跳过。

4. **只对未入库 id 取全文**  
   优先用时间线响应里的 `note_tweet.text`（长帖）+ `entities.urls[].expanded_url` 替换 `t.co`；不足时再 `get_posts_by_id`。  
   引用帖：附 `引用 @账号：` + 被引全文（可从 `expansions=referenced_tweets.id` 取）。

5. **XR 初筛 → 合并 XML**  
   按 `docs/01-collection-rules.md`；新帖插最前；guid 去重；≤100；**不改**已发出条目；有变化才改 `lastBuildDate` 并 push。

## 相对「全量浏览每个账号页面」的节省

| 步骤 | 全量浏览 | 廉价预检 |
|------|----------|----------|
| 账号头 / 最新 id | 15 次打开时间线 | 1 次 usernames 批量 |
| 无新帖账号 | 仍展开对比 | 直接跳过 |
| 仅有回复/转发 | 人工甄别 | `exclude` 后 result_count=0 |
| 正文 | 全账号展开「显示更多」 | 只对新 id 取 note_tweet |

例：本轮 15 账号预检后仅 9 个最新 id 更新；`exclude` 后仅 5 官方原创进入初筛并入库，媒体 0；htcvive / BigscreenVR / Dilmerv 最新为回复/转发被跳过。

## Agent 注意

- 仍须遵守只读：不点赞、不发帖、不关注、不回复。  
- 浏览器登录态仅作 API/页面不可用时的后备；优先 X MCP/`get_users_*`。  
- 写入仍只允许本仓库两路 feed。
