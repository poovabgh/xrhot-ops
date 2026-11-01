# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-31 17:06 PDT（例行 2026-11-01 08:00 BJT）。

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

## 本轮：2026-11-01 08:00 BJT

- 预检 19 账号；最新 id 高于 watermark：XREAL_Global、getVITURE、BeatSaber、RokidGlobal、VRChat、Play_for_dream、BigscreenVR、nathie、Dilmerv；其余等于 watermark 跳过；LensStudioDev aged-out skip（most_recent 2107190748114481270）。
- **official 100→100（+5）：** VRChat Spookality schedule change 2116677818440614017；BeatSaber Halloween tracks 2116626332566032759；VRChat Spookality Party Zone 2116624232255983762；XREAL_Global Zach Lieberman / AURA 2116576597880746022；Play_for_dream Halloween VR 2116575935931760782。丢掉最旧 5 条（2112248108507619684 … 2112115140459901216）。getVITURE / RokidGlobal / BigscreenVR `exclude` 后 result_count 0。
- **media-kol 100→100（+8）：** Dilmerv MRUK World Locking 2116675356937556345 / curiosity 2116661499972227386 / inspire 2116630042864165122 / experiment 2116602463457333520 / Depth API Soft Occlusion 2116568461962862993；nathie Hauntify（串帖合成）2116647626107945201 / trick-or-treat 2116611485321638168 / Subvocal glasses（串帖合成）2116592500471214115。丢掉最旧 8 条。Dilmerv 泛开发者闲聊 2116584740484440186（无 XR）丢掉；nathie 自串回复并入根帖。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-11-01 00:00 BJT：official +1 PICOXR / media +1 Dilmerv MRUK tip（HEAD 8e30e32）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-01 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
