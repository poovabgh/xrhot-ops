# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-26 17:04 PDT（例行 2026-10-27 08:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 27 Oct 2026 00:03:54 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 27 Oct 2026 00:03:54 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-27 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：htcvive、BigscreenVR、getVITURE、MetaVRDevs、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+5）：** VRChat referral 串帖合成 2114850030842761366；MetaVRDevs NordVPN Quest 成功案例 2114779978235884019 / Meta VR Start 开发者竞赛 $1M 2114770641459269855；getVITURE iPhone Duo + Beast 2114766639514423327；htcvive VIVE Eagle 15% off 2114753798807642466。丢掉最旧 5 条。BigscreenVR / BeatSaber `exclude` 后 result_count 0；VRChat Awards 续帖 2114080260677591221 已合入跳过；MetaVRDevs 最新为 RT Dilmerv 已排除。
- **media-kol 100→100（+8）：** SadlyItsBradley Alyx Foveated Rendering 2114856770480799894 / visionOS Spatial Accessories 引用 2114758759394484335；nathie Vision Pro+iPhone 2114824469566890131；Dilmerv Hand Pose Baker 2114801777832812778 / MR 原型 2114798895385698736 / YouTube 教程回归 2114790506978803856 / Meta 工具意愿投票 2114779142151721244 / hands+agents 2114769028463951906。丢掉最旧 8 条。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-27 00:00 BJT：official +3 / media-kol +3（HEAD 57496ec）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-27 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
