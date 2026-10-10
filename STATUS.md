# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-09（PT）/ 采集频次改为北京四时段。

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
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine 已创建**，按上述时刻唤醒执行采集 |
| 旧规范「每 30 分钟」 | **已废止**（见 `docs/03-decisions.md`） |
| 历史更新方式 | 迁仓前多为用户要求时手动采集并 push |

**说明：** 例行任务在 Grok Bot 侧；本仓库不托管 cron。唤醒后按 `AGENT_HANDOFF.md` §4 刷新 feeds，并同步本 STATUS 的条数与时间。

## 待办

- [ ] 按北京四时段例行刷新后，同步更新本 STATUS 的条数与时间
- [ ] 可选：kentbye 等长期无帖账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号（如 boztank）；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
