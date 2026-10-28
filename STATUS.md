# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-27 21:02 PDT（例行 2026-10-28 12:00 BJT）。

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

## 本轮：2026-10-28 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：XREAL_Global、MetaVRDevs、VRChat、BeatSaber、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev 无新可入库（aged-out）。
- **official 100→100（+2）：** XREAL_Global AURA Android Dev Summit 2115287671849578778；BeatSaber Ghostbusters environment 2115250452988035453。丢掉最旧 2 条。MetaVRDevs / VRChat `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+1）：** Dilmerv Meta VR Glasses SDK / Cubiques Meta Store 2115237113113219140。丢掉最旧 1 条。Dilmerv 动机闲聊 2115273852016058663 非 XR 丢弃；SadlyItsBradley Deadlock map 2115229006073078194 非 XR 游戏丢弃。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-28 08:00 BJT：official +2；media-kol +1（HEAD 4c82390）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-28 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
