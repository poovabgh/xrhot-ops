# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-27 12:14 PDT（补跑 2026-10-28 00:00 BJT 窗口后）。

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

## 本轮：2026-10-28 00:00 BJT（12:14 PDT 补跑）

- 预检 19 账号；最新 id 高于 watermark：htcvive、pimaxofficial、VRChat、BigscreenVR、MetaVRDevs、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过；LensStudioDev 无新可入库。
- **official 100→100（+3）：** htcvive VIVE Eagle 2115155446482817172；pimaxofficial Comfort Kit fiber 2115145755203715515；VRChat Halloween party 2115137647970800092。丢掉最旧 3 条。BigscreenVR / MetaVRDevs / BeatSaber `exclude` 后 result_count 0（最新为 RT/回复）。
- **media-kol 100→100（+5）：** Dilmerv Hand Grab Pose Baker 2115152843816464880；SadlyItsBradley HoloPrinter rooms 2115148895357423636；Dilmerv quote Meta VR Glasses + hand tracking 2115120676051063002；nathie Quest sales / breakthroughs 2115119023348187141；SadlyItsBradley Spatial Video on headset 2115112480229712201。丢掉最旧 5 条。Dilmerv 健身闲聊丢弃。
- 监控名单未变（official 15 / media-kol 4）。
- 上一有变更档 2026-10-27 20:00 BJT：official +1 VRChat；media-kol +3（HEAD 123f8c6）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-28 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
