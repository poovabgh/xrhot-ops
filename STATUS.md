# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-06 16:14 PST（例行 08:00 BJT 2026-11-07）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 07 Nov 2026 00:13:49 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 07 Nov 2026 00:13:49 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-07 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、MetaVRDevs、BigscreenVR、XREAL_Global、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过。
- **official 100→100（+5）：** XREAL_Global Real VR Fishing 2118811392945824160 / Oh My Galaxy 2118781280980537391 / Robo Detective 2118751691512160543；VRChat Public Instance Ownership 澄清（quote Dev Update）2118772305803239922；MetaVR_Official SEC immersive 180° Quest TV 2118761763630113004；丢掉最旧 5 条。MetaVRDevs / BigscreenVR `exclude` 后 result_count 0。VRChat 2118457404153020801 Dev Update 续帖跳过（已在 2118457400784998664 合并）。
- **media-kol 100→100（+8）：** Dilmerv tabletop skating MR 2118846537744716044 / Laser Dance 周年 quote 2118815372816384206 / ISDK Multimodal 2118773045976338503 / Meta VR Start Competition 2118755343970766908；nathie Meta VR glasses light blockers 串帖 2118827306160377980 / Zelda XR glasses + Viture Pro 2 Dock Mini 串帖 2118776605954969882；SadlyItsBradley visionOS 活动 quote 2118840191947268503 / Spatial Immersive Video editing 2118766214667255991；丢掉最旧 8 条。Dilmerv 动机/闲聊×4 drop（2118716324658520069 / 2118694916117205195 / 2118653374904078474 / 2118619396365000977）；SadlyItsBradley 回复 2118767915868520862 drop。ARealityEvent 等于 watermark。
- top-6 guid 抽查均在（含新 XREAL Fishing / Dilmerv skating / nathie Meta glasses；旧 BeatSaber OST9 / Rokid Style / XREAL HoloMedicine 等仍在）。
- 上一有变更档：2026-11-07 00:00 BJT BeatSaber OST9 + Rokid Style + XREAL HoloMedicine。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-07 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
