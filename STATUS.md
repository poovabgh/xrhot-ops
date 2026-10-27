# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-27 08:26 PDT（例行补跑 2026-10-27 20:00 BJT 窗口后）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 27 Oct 2026 15:26:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 27 Oct 2026 15:26:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-27 20:00 BJT（08:26 PDT 补跑）

- 预检 19 账号；最新 id 高于 watermark：VRChat、MetaVRDevs、BeatSaber、BigscreenVR、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；LensStudioDev 无新原创可入库；其余等于 watermark 跳过。
- **official 100→100（+1）：** VRChat Spookality free hat 2115079649050906798。丢掉最旧 1 条。MetaVRDevs / BeatSaber / BigscreenVR `exclude` 后 result_count 0；VRChat 串帖回复跳过。
- **media-kol 100→100（+3）：** ARealityEvent UnitedXR papers 2115096228669366736；Dilmerv XR unfinished-projects tip 2115088728259522589；Dilmerv Meta VR Glasses Device Readiness Check 2115066911163646220。nathie / Bradley `exclude` 后 0。丢掉最旧 3 条。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-27 16:00 BJT：official +2 pimax（HEAD d9fa626）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-28 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
