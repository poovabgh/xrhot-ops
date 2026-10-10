# scripts — 刷新约定

## 现状

- **调度：** Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天。
- **机制：** Grok Bot routine 按上述时刻唤醒；本目录不托管系统 cron。
- 刷新步骤：**登录 X 的浏览器只读采集 → 改 XML → 有变化才 git push**。
- 规范全文见 `docs/01-collection-rules.md` 第四节。
- 旧规范「每 30 分钟」**已废止**。

## 期望行为（例行或手动均遵守）

1. 在四个北京时刻（或用户手动要求时）：对 `accounts/official.json` + `media-kol.json` 全量检查新帖。
2. 无新帖、无删帖、无作者编辑 → **不 commit**。
3. 有变化 → 更新对应 `feeds/*.xml`（新帖在前，guid 去重，≤100 条）→ 更新 `lastBuildDate` → 更新根目录 `STATUS.md` → push `main`。
4. 凭证：使用用户授权的已登录浏览器会话；禁止点赞/发帖/关注/回复。
5. 失败：在 `STATUS.md` 或 issue 记录，不要静默跳过超过两轮（两次例行唤醒）。

## 建议后续脚本（未实现，名称占位）

| 脚本 | 职责 |
|------|------|
| `refresh_feeds.py`（待写） | 读 accounts JSON，合并新 item，写 XML，打印看了/留下统计 |
| `validate_feeds.py`（待写） | 检查 XML 合法、guid 唯一、必填字段、item 数 |

在脚本实现前，agent 按 `AGENT_HANDOFF.md` §4 手动执行等价步骤即可。

## 本地校验示例

```bash
# 条数
grep -c '<item>' feeds/x-official.xml feeds/x-media-kol.xml

# 简单 XML 井号（需 xmllint）
xmllint --noout feeds/x-official.xml feeds/x-media-kol.xml
```
