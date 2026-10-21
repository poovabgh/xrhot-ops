# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-21 09:08 PDT（例行 2026-10-22 00:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 21 Oct 2026 16:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Wed, 21 Oct 2026 16:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-22 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：RokidGlobal、XREAL_Global、pimaxofficial、BeatSaber、Dilmerv、nathie、htcvive、getVITURE、Play_for_dream、MetaVR_Official、VRChat、SadlyItsBradley；LensStudioDev most_recent 仍为已出队旧帖，不回溯。
- **official 100→100（+4）：** BeatSaber Halloween history 2112930484812714237；RokidGlobal AI glasses walking POV 2112921856239890773；pimaxofficial Dream Air Sim Racing Expo 2112906905173508250；XREAL_Global 1 Pro+ BRIGHTNESS+ 2112877472588996639；丢掉最旧 4 条（VRChat 2107597243897557143 / pimaxofficial 2107561657073549690 / htcvive 2107523861122101487 / getVITURE 2107515729197306165）。
- exclude / 无新原创入库：MetaVR_Official / htcvive / getVITURE / Play_for_dream / SadlyItsBradley result_count 0；VRChat 仅 Thirst Killer 续帖（根帖已入库）；nathie iPhone Duo 非 XR 丢弃 + SPECS 续帖已合并。
- **media-kol 100→100（+1）：** Dilmerv Fuse Balls Meta Store MR 串帖合并 2112934213028880678；丢掉最旧 Dilmerv 2107546954586808387。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-21 20:00 BJT：两路均无变化、无 commit（仍 ecbadfb）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-22 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
