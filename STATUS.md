# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-31 21:05 PDT（例行 2026-11-01 12:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | 见文件 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-01 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：VRChat、getVITURE、RokidGlobal、BigscreenVR、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+1）：** VRChat Spookality Party Zone live NOW 2116712353378996648。丢掉最旧 1 条。getVITURE / RokidGlobal / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+2）：** Dilmerv Meta Connect sunglasses / charger 2116723423694950836；Dilmerv Cubiques VR/MR trailer 2116686712533385363。丢掉最旧 2 条。nathie 自串回复 2116648104304824524（Hauntify 根帖已合成入库）drop；SadlyItsBradley `exclude` 后 result_count 0。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-11-01 08:00 BJT：official +5 / media +8（HEAD d347d1b）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-01 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
