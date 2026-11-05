# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-05 00:09 PST（例行 16:00 BJT 2026-11-05）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 05 Nov 2026 04:09:23 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 05 Nov 2026 08:09:35 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-05 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、XREAL_Global、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 MetaVRDevs / PICOXR / PICOXR_Dev / BigscreenVR / RokidGlobal / getVITURE / pimaxofficial / Play_for_dream / magicleap / VRChat / ARealityEvent）。
- **official 100 不变：** MetaVR_Official / htcvive / XREAL_Global / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+1）：** Dilmerv Meta VR Glasses build paths（串帖合并含 video+hackathon 链）2118219230751653981；丢掉最旧 1 条（2114687508659249594）。nathie 2118026204456640766 为已入订阅 SteamOS 串帖续帖（已合并）skip；Dilmerv motivation×3 drop（2118184047205630137 / 2118168944968089864 / 2118146295617482889）；SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（含新 Dilmerv Meta VR Glasses / Dilmerv MRUK / Bradley Chromium / nathie SteamOS / Dilmerv CLI / Dilmerv Cubiques）。
- 上一有变更档：2026-11-05 12:00 BJT official +6、media-kol +3。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-05 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
