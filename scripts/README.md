# scripts — 刷新约定

## 现状（诚实）

- **没有**已部署的每 30 分钟 cron。
- 刷新目前是：**登录 X 的浏览器只读采集 → 改 XML → git push**。
- 规范要求见 `docs/01-collection-rules.md` 第四节。

## 期望行为（实现时应遵守）

1. 每 30 分钟：对 `accounts/official.json` + `media-kol.json` 全量检查新帖。
2. 无新帖、无删帖、无作者编辑 → **不 commit**。
3. 有变化 → 更新对应 `feeds/*.xml`（新帖在前，guid 去重，≤100 条）→ 更新 `lastBuildDate` → 更新根目录 `STATUS.md` → push `main`。
4. 凭证：使用用户授权的已登录浏览器会话；禁止点赞/发帖/关注/回复。
5. 失败：在 `STATUS.md` 或 issue 记录，不要静默跳过超过两轮。

## 建议后续脚本（未实现，名称占位）

| 脚本 | 职责 |
|------|------|
| `refresh_feeds.py`（待写） | 读 accounts JSON，合并新 item，写 XML，打印看了/留下统计 |
| `validate_feeds.py`（待写） | 检查 XML 合法、guid 唯一、必填字段、item 数 |

在实现前，agent 按 `AGENT_HANDOFF.md` §4 手动执行等价步骤即可。

## 本地校验示例

```bash
# 条数
grep -c '<item>' feeds/x-official.xml feeds/x-media-kol.xml

# 简单 XML 井号（需 xmllint）
xmllint --noout feeds/x-official.xml feeds/x-media-kol.xml
```
