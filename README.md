# xrhot-ops

XRHOT 的 **X（Twitter）采集运维仓库**。  
本仓库是 X 订阅内容、账号清单、采集规则与决策记录的**唯一事实来源（single source of truth）**。

> **不是什么**  
> 本仓库**不处理**其他 X 内容任务（例如非 XR 的盘点、AV 热度、通用爬虫、SocialData、站内 `POST /api/ingest/items`）。  
> 那些任务请另建目录/仓库，不要把规则混进这里。

## 公开订阅（站里直接拉）

| 订阅 | Raw URL |
|------|---------|
| X · XR 官方账号 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| X · XR 媒体和 KOL | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

接入时请打开站内「**短帖也算正文**」设置（280 字以下否则会被当成摘要）。

## 目录

```
README.md                 # 本文件
AGENT_HANDOFF.md          # Agent 一读接手
STATUS.md                 # 当前条数、上次更新、待办
docs/                     # 范围、规则、清单、决策、ingest 说明
feeds/                    # 两路 RSS（唯一对外产出）
accounts/                 # 账号 JSON（官方 / 媒体KOL / 跳过 / 拒绝）
scripts/                  # 刷新约定（北京时间每日五次）
```

## 快速规则摘要

- 只收名单账号的原创帖；**不做关键词主题检索**。
- XR = VR/MR 头显、AR/AI 眼镜及配件、XR 系统/平台、应用内容、技术零部件、业务与展会；AI 仅限用在 XR 设备上的。
- 已有网站 RSS 的媒体（UploadVR、Road to VR、映维、93913、MIXED）**不加**它们的 X。
- 正文逐字照录进 `content:encoded`；已发出条目不改字。
- 采集频次：北京时间（Asia/Shanghai）每日 **08:00 / 12:00 / 16:00 / 20:00 / 00:00（24:00）**；见 `STATUS.md`（Grok Bot routine 已建）。

接手请先读 [`AGENT_HANDOFF.md`](./AGENT_HANDOFF.md)。

## 旧仓库

旧临时仓库 `poovabgh/xrhot-feeds` 与探测仓 `poovabgh/xrhot-feeds-probe` 已于 2026-10-13 删除；请勿再引用。
