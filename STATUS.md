# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-09（PT）/ 迁仓日。

## 订阅现状（迁入时核对）

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 47 | Fri, 09 Oct 2026 14:21:45 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 35 | Fri, 09 Oct 2026 11:00:20 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 定时更新

| 项 | 状态 |
|----|------|
| 规范「每 30 分钟检查一次」 | 已写在 `docs/01-collection-rules.md` |
| 实际 cron / 定时 agent | **未实现** |
| 历史更新方式 | 仅用户要求时手动采集并 push |

**Pending：** 实现可重复的刷新脚本或定时唤醒，并在本文件记录机制（谁跑、何处凭证、失败怎么告警）。

## 待办

- [ ] 实现每 30 分钟检查（有新帖才 commit）
- [ ] 刷新后同步更新本 STATUS 的条数与时间
- [ ] 可选：kentbye 等长期无帖账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号（如 boztank）；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
