# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-14 09:41 PT（账号裁剪：去掉 benz145 / rayneo_global / Flat2VR / kentbye）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 96 | Wed, 14 Oct 2026 16:41:44 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 71 | Wed, 14 Oct 2026 16:41:44 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-14 账号裁剪（非例行刷新）

- 用户决定去掉：`benz145`、`rayneo_global`、`Flat2VR`、`kentbye`；其余账号保留。
- 从 `accounts/official.json` / `media-kol.json` 移入 `accounts/rejected.json`（dropped-from-*；droppedAt=2026-10-14）。
- **official：** 100→**96**（删 rayneo_global×4）；监控账号 16→**15**
- **media-kol：** 88→**71**（删 benz145×14、kentbye×2、Flat2VR×1）；监控账号 7→**4**
- channel description 与 `docs/02-account-list.md` / ADR 已同步。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-15 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
