# 00 — 范围（Scope）

## 本仓库负责什么

- XRHOT 项目里，**X 平台**上 XR 相关账号的采集、初筛、RSS 产出与账号治理。
- 对外只维护两路订阅：`feeds/x-official.xml`、`feeds/x-media-kol.xml`。
- 规则、决策、账号清单与 Agent 交接文档，保证任意 agent 可接手。

## 明确不在范围内（Out of scope）

| 事项 | 说明 |
|------|------|
| 其他 X 内容任务 | 非 XR 的热度盘点、娱乐/AV、通用舆情等 — **另建仓库或目录** |
| 网站 RSS 抓取 | UploadVR、Road to VR、映维、93913、MIXED、厂商官网 Atom 等由**站内 sources** 配置，不在本仓维护 feed 文件 |
| SocialData / `x_search` | 不订付费 SocialData；不做站内 `x_search` 信源 |
| `POST /api/ingest/items` 推送正文 | 已弃用该路径承载 X 正文（见 `04-ingest-vs-rss.md`） |
| 关键词全站主题检索 | 第二版已停掉；不要恢复 `x-keyword` |
| 点赞/发帖/关注/回复 | 采集只读 |
| 品牌评分别名表 | `industry/brands.ts` 在站代码侧；本仓可引用说明但不维护评分逻辑 |

## 与「其他 X 任务」如何隔离

- 本仓库目录与 GitHub repo **专用于 XRHOT-X**。
- Agent 收到混杂指令时：只执行与本仓 `docs/` + `accounts/` 一致的部分；其余拒绝或请用户开新任务。
- 禁止把本仓 `feeds/` 当成通用聚合垃圾桶。

## XR 含义（摘要）

- **头显** = VR 头显 + MR 头显（一体机、PCVR 等）。
- **眼镜** = AR 眼镜、AI 眼镜（有无显示都算）及配件。
- 另含 XR 系统/平台、应用内容、技术零部件、业务与展会。
- 完整过滤见 `01-collection-rules.md`。
