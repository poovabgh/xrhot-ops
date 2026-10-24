# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-23 17:03 PDT（例行 2026-10-24 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 24 Oct 2026 00:02:49 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 24 Oct 2026 00:02:49 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-24 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：VRChat、getVITURE、XREAL_Global、Play_for_dream、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；MetaVR_Official 无 feed watermark 但 most_recent 为新原创 XR（收录）；LensStudioDev 无 watermark、most_recent 为已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+3）：** MetaVR_Official Quest 沉浸式大学橄榄球 2113707284065046791；Play_for_dream VR 减重/组件 2113677078117912668；Play_for_dream 视觉/追踪/减重 2113676832780202376。丢掉最旧 3 条。
- **media-kol 100→100（+5）：** Dilmerv Meta VR Glasses 2113781442945880236；Dilmerv MRUK Passthrough Relighting 2113767854638342414（并续帖资源链）；SadlyItsBradley Steam Frame CD-ROM 2113731023645102102（并续帖）；Dilmerv OpenXR Spatial Containers 2113726842779861304（并续帖）；ARealityEvent UnitedXR Activations 2113676830779797755。丢掉最旧 5 条。
- exclude / 丢弃：VRChat / getVITURE / XREAL_Global result_count 0；nathie iPhone Duo 非 XR 丢弃 2113576600113496449，续帖 2113315923025379458 已并入根帖 2113315308299513970（不改已发条目）。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-24 00:00 BJT：official +2（PICOXR / BeatSaber），commit a148033。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-24 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
