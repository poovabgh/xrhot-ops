# 01 — 采集规则（用户第二版，权威）

本文是 XRHOT X 订阅的完整规则。与用户 2026-10-09 第二版方案对齐；冲突时以本文 + `docs/03-decisions.md` 更新为准。

## 一、订阅结构

- **两路，仅此两路：**
  - `feeds/x-official.xml` — 标题：`X · XR 官方账号`
  - `feeds/x-media-kol.xml` — 标题：`X · XR 媒体和 KOL`
- **停掉主题检索**，不再按关键词搜帖子。
- 以后加账号：按类别写入对应 feed + `accounts/*.json`，**不新建**订阅文件。
- UploadVR、Road to VR（及映维、93913、MIXED）**不收 X**：网站 RSS 已接入站内。

## 二、收哪些帖子

流程：先按账号收 → 再做 XR 初筛 → 只把相关帖写入订阅。

**XR 范围：** VR、MR、AR 与 AI 眼镜。AI 眼镜带不带显示都算。

### 留下（主要内容直接涉及任一项）

- **XR 设备：** 头显（VR/MR）、AR 眼镜、AI 眼镜及其配件的发布、价格、开售、更新、评测、试戴
- **XR 系统与平台：** Horizon OS、visionOS、Android XR、SteamVR、PICO OS 等
- **XR 应用与内容：** VR/MR/AR 游戏与应用的发布、更新、折扣
- **XR 技术与零部件：** 光波导、显示、XR 芯片、眼动/手势追踪、空间计算开发工具
- **XR 业务：** XR 公司或 XR 部门的融资、财报、裁员、合作、收购；XR 展会与活动
- **AI：** 仅直接用在 XR 设备上的（如眼镜内 AI 助手）

### 丢弃

- 公司其他产品：iPhone、Mac、Apple Watch、Facebook/Instagram/WhatsApp、普通手机/电脑/穿戴
- 通用 AI（大模型、聊天机器人）、普通机器人、其他科技新闻
- 仅顺带提到 XR 品牌/产品名，XR 只是背景
- 以助听为主要功能的眼镜
- 博主生活、健身、闲聊，以及**不是 VR 的游戏**

### 拿不准

- **留下。** 站内还会再筛。初筛只去掉明显无关的；不判断「重不重要」；不因宣传/广告就丢掉。

### 格式上不收

- 回复别人的帖子
- 纯转发
- 只有图片或视频、没有文字的帖子
- 自己的串帖 → **合成一条**
- 引用别人：被引用文字附在后面，前缀 `引用 @账号：`

### 行为

- **只读：** 不点赞、不发帖、不关注、不回复。

## 三、每条帖子怎么写

| 字段 | 规则 |
|------|------|
| `<title>` | 帖子第一句，原文照抄，最长 120 字；不加字、不翻译 |
| `<link>` | `https://x.com/<账号>/status/<帖子ID>` |
| `<guid isPermaLink="false">` | 帖子 ID（稳定、不变） |
| `<pubDate>` | 页面 `<time datetime>` → RFC 822 GMT，如 `Wed, 07 Oct 2026 12:30:00 GMT` |
| `<dc:creator>` | 账号名，**不带** `@` |
| `<content:encoded>` | CDATA；全文逐字照录 |

正文细则：

- 「显示更多」必须展开；结尾不能是截断的 `…`
- `t.co` 换成真实地址；每个链接只写一次真实地址，不留截断展示链
- 保留换行、表情、话题标签；不翻译、不摘要、不改写
- 标题中的 `&`、`<`、`>` 要 XML 转义；文件为合法 UTF-8 XML
- 命名空间：`xmlns:content`、`xmlns:dc`（见样例）

## 四、更新规则

- **规范：** 固定北京时间（Asia/Shanghai）每日 **08:00、12:00、16:00、20:00** 共四次检查新帖；每周七天。有新帖（或作者编辑/删帖需同步）才更新文件并提交；无变化不提交。
- **实现状态：** 见 `STATUS.md` — 由 **Grok Bot 例行任务（routine）** 按上述时刻唤醒执行；勿再按「每 30 分钟」理解。
- 每个订阅保留最近约 **100** 条，**新的在前**。
- **已发出条目不改：** 同一帖子的标题、正文、时间、链接保持不变。仅当作者编辑原帖才更新该条；作者删除则从订阅去掉。
- `<lastBuildDate>` **只在内容有变化时**更新。

## 五、样例骨架

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>X · XR 官方账号</title>
    <link>https://github.com/poovabgh/xrhot-ops</link>
    <description>…账号列表…</description>
    <lastBuildDate>Fri, 09 Oct 2026 14:21:45 GMT</lastBuildDate>
    <item>
      <title>帖子的第一句</title>
      <link>https://x.com/MetaVR_Official/status/1234567890</link>
      <guid isPermaLink="false">1234567890</guid>
      <pubDate>Wed, 07 Oct 2026 17:19:00 GMT</pubDate>
      <dc:creator>MetaVR_Official</dc:creator>
      <content:encoded><![CDATA[帖子全文，短链换成真实地址]]></content:encoded>
    </item>
  </channel>
</rss>
```

## 六、做完一轮后应回复用户

- 两个订阅的 raw 地址
- 最近一次更新时间
- 每个订阅当前条数
- 本轮每账号：看了多少 / 初筛留下多少
