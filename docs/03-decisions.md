# 03 — 决策日志（ADR 风格）

按时间倒序追加。格式：日期 | 标题 | 背景 | 决定 | 后果。

---

## 2026-10-11 — 媒体/KOL 去掉 SkarredGhost、CasandChary、VRDesktop

- **背景：** 用户要求分析噪声；SkarredGhost 约占订阅 1/3 且多为 UploadVR/Road to VR 标题转发（站内已有 RSS）；CasandChary、VRDesktop 近窗口 0 条。
- **决定：** 从 `accounts/media-kol.json` 与 `feeds/x-media-kol.xml` 移除上述三账号；写入 `accounts/rejected.json`（dropped-from-media-kol）。其余 media-kol 与全部 official 保留。
- **后果：** media-kol 条目从 100 降至去掉三家后的剩余条数（按时间保留）；例行采集不再预检这三家。


## 2026-10-10 — 扩账号：官方 5 + 媒体/KOL 6

- **背景：** 用户要求继续找常讨论 VR/MR/AR 的账号（硬件、游戏、内容、生态、商业），并明确「加进去」。
- **决定：** official 增加 MetaVRDevs、LensStudioDev、magicleap、VRChat、BeatSaber；media-kol 增加 benz145、CasandChary、SkarredGhost、Flat2VR、VRDesktop、SadlyItsBradley。仍跳过已有站内 RSS 的媒体 X。采近约 14 天原创帖，XR 初筛后并入两路订阅；已有条目不改字；每路最多 100 条。
- **后果：** 账号清单与 channel description 更新；见本轮 STATUS。

---

## 2026-10-09 — 采集频次改为北京时间每日四次整点

- **背景：** 第二版曾写「约每 30 分钟检查」；用户要求改为固定时段，避免高频与指令漂移。
- **决定：** Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点，非 :18）检查；每周七天。由 Grok Bot routine 按此时刻唤醒。废除「每 30 分钟」规范。
- **后果：** `docs/01-collection-rules.md`、`STATUS.md`、`AGENT_HANDOFF.md`、`README.md`、`scripts/README.md` 一律以四时段为准；agent 不得再按 30 分钟调度。

---

## 2026-10-09 — 迁仓为 xrhot-ops 单一事实来源

- **背景：** 规则、订阅、清单散落在对话与临时仓 `xrhot-feeds`，易与其他 X 任务混淆、指令漂移。
- **决定：** 新建公开仓 `poovabgh/xrhot-ops`，分类存放规则/账号/feeds/决策/交接；`xrhot-feeds` 改为跳转。
- **后果：** 站与 agent 只认本仓 raw feed URL；旧 raw 路径废弃。

## 2026-10-09 — 只扩官方公司号，不加人员与噪声号

- **背景：** 按品牌表补充 X；用户要求「官方账号和官方人员尽量找到」，随后明确「只把官方订阅加进来，其他不加」。
- **决定：** 将 XREAL_Global、RokidGlobal、getVITURE、rayneo_global、pimaxofficial、Play_for_dream、PICOXR_Dev 写入 official。`boztank`、Valve/小米等大厂主号、HardwareSteam 不进 feed。
- **后果：** official 从 4 个核心扩到 11；media-kol 未扩。

## 2026-10-09 — 采集规则第二版：两路订阅 + 无关键词 + XR 初筛

- **背景：** 第一版曾做单路聚合 + 主题检索；站侧需要按信源分级（官方 vs 媒体/KOL）。
- **决定：** `x-official.xml` + `x-media-kol.xml`；停关键词；名单帖经 XR 初筛；删掉旧 `xrhot-x.xml` / 分账号 / keyword 文件。
- **后果：** 结构稳定；热度向主题帖不再进站。

## 2026-10-09 — 放弃 POST ingest 正文，改用 RSS

- **背景：** `POST /api/ingest/items` 只收 title/url/publishedAt/author；正文靠 worker 抓原页；服务器开 x.com 遇登录墙；上游 AIHOT 亦未透传 body。
- **决定：** 公网 RSS，`content:encoded` 放全文；站拉订阅；开启「短帖也算正文」。
- **后果：** 不开放 ingest 口令给采集端；时效约站内最短 15 分钟拉一次。

## 2026-10-09 — 单路聚合试过后改为两路

- **背景：** 用户先要求「只做一路，带作者」；站侧第二版要求官方与媒体/KOL 分订阅以便分级。
- **决定：** 服从第二版，拆成两路。
- **后果：** 单路 `xrhot-x.xml` 删除。

## 2026-10-09 — 「每 30 分钟检查」写入规范但未实现（已废止）

- **背景：** 第二版更新规则要求 30 分钟。
- **决定：** 文档与 STATUS 曾明确为规范；实际仍手动。
- **后果：** **已被同日「北京时间每日四次整点」决策取代**；勿再按 30 分钟调度。

## 2026-10-09 — 已有媒体网站 RSS 则不加其 X

- **背景：** UploadVR、Road to VR 等已接站内 RSS。
- **决定：** 跳过其 X，避免双通道重复与分级混乱。
- **后果：** 见 `accounts/skipped-media-rss.json`。

## ADR-008 — 刷新采用「最新帖 id 预检 + since_id」省 token（2026-10-10）

**决策：** 例行/手动刷新先批量取各账号 `most_recent_tweet_id`，与 feed 内该账号最大 guid 比较；仅对有更新者调用 `get_users_posts(since_id, exclude=replies,retweets)`，再对未入库 id 取全文。

**原因：** 全账号打开时间线并展开正文浪费配额与上下文；多数时刻无新原创帖。

**详见：** `scripts/cheap_check_plan.md`、`scripts/extract_since_ids.py`。

