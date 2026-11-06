# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-05 16:09 PST（例行 08:00 BJT 2026-11-06）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 06 Nov 2026 00:09:39 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 06 Nov 2026 00:09:39 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-06 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、getVITURE、VRChat、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 MetaVRDevs / PICOXR / PICOXR_Dev / RokidGlobal / pimaxofficial / Play_for_dream / magicleap / BeatSaber / ARealityEvent）。
- **official 100→100（+8）：** XREAL_Global Demeo AURA 2118479289142116359 / VRChat Nov 5 Developer Update（串帖合并 thumbnail）2118457400784998664 / XREAL_Global Figmin XR AURA 2118449015306022985 / htcvive VIVE Eagle Hollywood DITL 2118436082706485482 / XREAL_Global Open Brush AURA 2118419068080300536 / VRChat Virtual Dice Party 2026 quote 2118407700052599148 / getVITURE Dock Mini Zelda 2118396842463351123 / XREAL_Global ShapesXR AURA 2118389248499892412；丢掉最旧 8 条。MetaVR_Official / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+5）：** nathie VRChat Steam reviews 2118484164303605977 / Dilmerv Greg Madison Sphenomenon MR quote 2118469739966247365 / Dilmerv HandGrabUse ISDK 2118448333538595246 / nathie Meta Quest walls app（串帖合并 reddit）2118443855779615149 / Dilmerv Cubiques Meta Store NOW AVAILABLE 2118384006245003336；丢掉最旧 5 条。nathie Ghost of Tsushima 续帖 skip；Dilmerv motivation×2 + Mac Studio unboxing + XR educator soft drop；SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（含新 XREAL Demeo / VRChat Dev Update / XREAL Figmin / htcvive Eagle / nathie VRChat reviews / Dilmerv Sphenomenon；旧 PICOXR Leave the familiar / nathie Ghost 等仍在）。
- 上一有变更档：2026-11-06 00:00 BJT official +3 PICOXR/BeatSaber/Rokid；media-kol +4 nathie/Dilmerv。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-06 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
