# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-05 08:06 PST（例行 00:00 BJT 2026-11-06）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 05 Nov 2026 16:06:19 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 05 Nov 2026 16:06:19 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-06 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、PICOXR、htcvive、RokidGlobal、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 MetaVRDevs / PICOXR_Dev / BigscreenVR / XREAL_Global / getVITURE / pimaxofficial / Play_for_dream / magicleap / VRChat / ARealityEvent）。
- **official 100→100（+3）：** PICOXR Leave the familiar behind 2118372937203884362 / BeatSaber stretch before session quote 2118363087283585099 / RokidGlobal Rokid Glasses AI Shortcut calories 2118357678519165323；丢掉最旧 3 条（2113627817917182009 / 2113542566360834093 / 2113383235598110724）。MetaVR_Official / htcvive `exclude` 后 result_count 0。
- **media-kol 100→100（+4）：** nathie Ghost of Tsushima VR（串帖合并 root）2118358938009653285 / Dilmerv Cubiques Meta Store approved 2118350458204864968 / Dilmerv Meta VR Start Competition 2118335116887863461 / nathie Zelda first-person VR mod 2118316089738469467；丢掉最旧 4 条（2114779142151721244 / 2114769028463951906 / 2114758759394484335 / 2114741454429950462）。nathie 2118026204456640766 为已入订阅 SteamOS 串帖续帖 skip；SadlyItsBradley `exclude` 后 result_count 0。
- top-6 guid 抽查均在（含新 PICOXR / BeatSaber / Rokid / nathie Ghost / Dilmerv Cubiques / Dilmerv VR Start；旧 top XREAL Galápagos / Dilmerv AI agents 等仍在）。
- 上一有变更档：2026-11-05 20:00 BJT official +1 XREAL Galápagos；media-kol +2 Dilmerv。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-06 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
