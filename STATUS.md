# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-04 20:09 PST（例行 12:00 BJT 2026-11-05）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 05 Nov 2026 04:09:23 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 05 Nov 2026 04:09:23 +0000 | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-05 12:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、Play_for_dream、magicleap、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（含 RokidGlobal / getVITURE / MetaVRDevs / PICOXR / PICOXR_Dev / pimaxofficial / ARealityEvent）。08:00 例程未成功，本轮自 00:00 watermark 追赶。
- **official 100→100（+6）：** BigscreenVR VR coolest experience 2118155350461518244 / XREAL_Global Pool Assist AURA 2118116775850111132 / XREAL_Global Nevatars AURA 2118056573318611406 / VRChat Hatsune Miku PLAYBACK LIVE 2118043459022152055 / magicleap waveguide manufacturing software 2118040616437186963 / Play_for_dream VRChat social 2118040585692995709；丢掉最旧 6 条（2113344845569749180、2113314422869426650、2113307002726236483、2113284379766333550、2113284242432241692、2113269330993365163）。MetaVR_Official / htcvive / BeatSaber `exclude` 后 result_count 0。
- **media-kol 100→100（+3）：** Dilmerv MRUK Spatial Testing 2118131475501420989 / SadlyItsBradley Steam Frame Chromium WebXR 2118073306570007037 / nathie SteamOS on Quest 1（串帖合并含 reddit 链）2118025614670037343；丢掉最旧 3 条（2114563928713789607、2114533728697335809、2114532245495250952）。Dilmerv motivation×4 drop（2118184047205630137 / 2118168944968089864 / 2118146295617482889 / 2118033142229422300）；SadlyItsBradley political Missouri joke 2117853126585684469 drop。
- top-6 guid 抽查均在（含新 BigscreenVR / XREAL Pool Assist / Dilmerv MRUK / Bradley Chromium / nathie SteamOS / VRChat Miku）。
- 上一有变更档：2026-11-05 00:00 BJT official +2 htcvive/Rokid、media-kol +1 Dilmerv CLI。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-05 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
