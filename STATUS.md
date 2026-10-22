# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-22 09:15 PDT（例行 2026-10-23 00:00 BJT）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 22 Oct 2026 16:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 22 Oct 2026 16:10:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-23 00:00 BJT

- 预检 19 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、VRChat、ARealityEvent、nathie、Dilmerv、SadlyItsBradley；LensStudioDev most_recent 仍为已出队旧帖，不回溯；其余等于 watermark 跳过。
- **official 100→100（+3）：** RokidGlobal AI Glasses Style 日常步行 2113284242432241692；pimaxofficial Dream Air + DOF Reality Sim Racing Expo 2113269330993365163；VRChat avatar six seven 2113284379766333550。丢掉最旧 3 条。
- **media-kol 100→100（+1）：** ARealityEvent UnitedXR Europe 1-Day Pass 2113254045658099848；丢掉最旧 1 条。
- exclude / 丢弃 / 已合并：MetaVR_Official / htcvive / getVITURE / Play_for_dream / Dilmerv / SadlyItsBradley exclude 后 result_count 0；VRChat Thirst Killer 续帖已合并；nathie SPECS 续帖已合并；nathie「Happy Back to the Future Day!」2112979617707336165 非 XR 丢弃。
- 监控名单未变（official 15 / media-kol 4）。
- 上一档 2026-10-22 20:00 BJT：official / media-kol 均无入库变化（仍 8d08ad2）。
- 再上一档 2026-10-22 16:00 BJT：media-kol +1（Dilmerv Hand Grab Pose Baker IK），commit 8d08ad2。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-23 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
