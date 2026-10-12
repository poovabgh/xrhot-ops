# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-11 PT — 去掉 SkarredGhost / CasandChary / VRDesktop。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 86 | Mon, 12 Oct 2026 04:07:57 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 67 | Mon, 12 Oct 2026 06:54:25 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：名单清理（2026-10-11 PT）

- 从 media-kol **去掉** SkarredGhost（噪声/与站内 RSS 重复）、CasandChary、VRDesktop（零产出）；见 `accounts/rejected.json`。
- 订阅去掉对应 `<item>`（SkarredGhost 33 条；另两家本就 0 条）→ **67** 条；official 未动（86）。
- 保留 media-kol：ARealityEvent、nathie、Dilmerv、kentbye、benz145、Flat2VR、SadlyItsBradley。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：按日历取下一个 08/12/16/20:00。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye / Flat2VR 等低产出账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
