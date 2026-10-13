# Agent 接手指南（一读即可恢复工作）

## 0. 身份与边界

你接手的是 **XRHOT 的 X 采集运维**，仓库：

- Clone：`https://github.com/poovabgh/xrhot-ops.git`
- 组织/账号：`poovabgh`（用已登录的 `gh`）

**不要做：**

- 其他 X 内容任务（非 XR 盘点、AV、通用热搜等）
- 往本仓库塞无关 feed / 关键词聚合
- 给已有网站 RSS 的媒体再加 X 账号（见 `accounts/skipped-media-rss.json`）
- 发明未核实的账号、改写已发出条目的正文
- 点赞、发帖、关注、回复（只读采集）
- 假定错误的调度（例如「每 30 分钟」）——规范是北京时间每日五次整点（08/12/16/20/00），见 `STATUS.md`

**要做：** 按 `docs/01-collection-rules.md` 采 X → 初筛 → 更新 `feeds/*.xml` → 有变化才 commit/push。

## 1. 对外订阅地址（给站用）

- Official：https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml
- Media+KOL：https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml

站内需开启：**短帖也算正文**。

## 2. 必读文档顺序

1. `docs/00-scope.md` — 范围
2. `docs/01-collection-rules.md` — 完整采集与条目规则（用户第二版）
3. `docs/02-account-list.md` + `accounts/*.json` — 谁收谁不收
4. `docs/03-decisions.md` — 为什么这样设计
5. `docs/04-ingest-vs-rss.md` — 为什么不用 POST ingest
6. `STATUS.md` — 当前状态与待办

## 3. 如何新增官方账号

1. 核实公司官网页脚 / 关于页指向的 X handle（高置信才加）。
2. 用户已明确：**只加官方公司号**进 official；个人号（如 Meta CTO）默认不加，除非用户另行批准。
3. 编辑 `accounts/official.json`：`handle`、`brand`、`evidenceUrl`、`addedAt`、`notes`。
4. 更新 `feeds/x-official.xml` 的 channel `description`（账号列表文案）。
5. 更新 `docs/02-account-list.md`。
6. 采一轮该账号近期帖，按规则初筛后**追加** item（新的在前）；**不要改**已有 item 的 title/body/guid/pubDate。
7. 有内容变化时更新 `<lastBuildDate>`，commit，push `main`。
8. 在 `docs/03-decisions.md` 记一条 ADR。
9. 回复用户：账号名、放在哪个 feed、本轮看了/留下多少条。

媒体/KOL 同理，写入 `accounts/media-kol.json` 与 `feeds/x-media-kol.xml`。**不要新建第三路订阅文件。**

## 4. 如何刷新（例行唤醒或手动）

**调度：** Asia/Shanghai 每日 08:00、12:00、16:00、20:00、00:00（24:00）（由 Grok Bot routine 唤醒）。无变化不 push。

1. 用**已登录 X 的浏览器**，对每个 handle 搜：`from:<handle> -filter:replies`（Latest；可加 `since:YYYY-MM-DD`）。
2. 展开「显示更多」；记录 `status` ID、`<time datetime>`、全文。
3. 丢弃：回复、纯转发、无文字媒体帖、明显非 XR（规则见 `docs/01-collection-rules.md`）。
4. 引用帖：正文末附 `引用 @账号：` + 被引文字。
5. `t.co` 换成真实 URL（每个链接只写一次真实地址）。
6. 合并进对应 XML：按 `guid`（帖子 ID）去重；新帖插到最前；每路最多约 100 条，丢掉最旧。
7. **禁止**改写已发出条目文字（作者编辑原帖才更新该条；作者删帖则从 feed 删除）。
8. 仅当内容有变时更新 `lastBuildDate` 并 git push。
9. 更新 `STATUS.md` 条数与时间。

细节与字段格式见 `docs/01-collection-rules.md` 与 `scripts/README.md`。

**省 token：** 先跑 `scripts/extract_since_ids.py`，再用 `get_users_by_usernames` 的 `most_recent_tweet_id` 与 feed 内 max guid 比较；仅对有更新的账号拉 `get_users_posts(since_id)`。详见 `scripts/cheap_check_plan.md`。

## 5. 不要发明的东西

- 不要 invent 未在 `accounts/` 登记的 handle。
- 不要恢复关键词主题检索订阅。
- 不要把 UploadVR / RtoVR 等加回 X feed。
- 不要按「每 30 分钟」调度；以北京五时段与 `STATUS.md` 为准。不要谎报例行任务状态。
- 不要用 Grok 摘要代替帖子原文。

## 6. 当前账号快照（以 JSON 为准）

见 `accounts/official.json` 与 `accounts/media-kol.json`。截至迁仓时 official 11 个 handle，media-kol 4 个。
