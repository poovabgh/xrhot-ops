# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-26 21:04 PDT（例行 2026-10-27 12:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Tue, 27 Oct 2026 04:03:07 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Tue, 27 Oct 2026 00:03:54 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-27 12:00 BJT

- 预检 19 账号；最新 id 高于 watermark：BigscreenVR、XREAL_Global、MetaVRDevs、VRChat、BeatSaber、nathie、Dilmerv；LensStudioDev 无 watermark、most_recent 已出队旧帖（不回溯）；其余等于 watermark 跳过。
- **official 100→100（+1）：** XREAL_Global AURA @ Android Dev Summit / Gemini / Circle to Search 2114929301741093209。丢掉最旧 1 条（2109612121134698697）。BigscreenVR / MetaVRDevs / BeatSaber `exclude` 后 result_count 0；VRChat 续帖 2114864639615852590 等（referral 串已合入 2114850030842761366）跳过。
- **media-kol 100 不变：** nathie / Dilmerv `exclude` 后 result_count 0。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-27 08:00 BJT：official +5 / media-kol +8（HEAD 11fb476）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-27 **16:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
