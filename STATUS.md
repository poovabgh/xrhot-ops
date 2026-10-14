# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-14 08:12 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Wed, 14 Oct 2026 00:12:09 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 81 | Wed, 14 Oct 2026 00:12:09 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-14 08:00 BJT

- 前一轮 00:00 BJT 未跑成；本轮为 08:00 补采。
- 廉价预检：23 账号 `most_recent_tweet_id`；18 个最新 id 高于 watermark；`exclude=replies,retweets` 后有原创：XREAL_Global、htcvive、RokidGlobal、pimaxofficial×2、getVITURE、BeatSaber、Play_for_dream、MetaVRDevs、magicleap、VRChat；nathie、Dilmerv、SadlyItsBradley、benz145。rayneo_global / BigscreenVR / Flat2VR / kentbye 为 0。
- **official：** 95→**100**（+11，cap≈100 丢最旧；BeatSaber 2110109890718953984；MetaVRDevs 2110104112406868209；getVITURE 2110084514399539515；pimaxofficial 2110068052012454104 / 2110022750995988754；magicleap 2110061296716513688；Play_for_dream 2110052949439455422；htcvive 2110046191442428387；VRChat 2110044805669527903；RokidGlobal 2110022749846450186；XREAL_Global 2110007658732495060）
- **media-kol：** 76→**81**（+5：SadlyItsBradley Index sunset 2110140656509161814 / Minecraft VR Steam Frame 2110022104569557172 / AR slasher 2110019036528697453；nathie Ray-Ban Display EU 2110099934250971300；Dilmerv GregMadison XR 2110017375630446646）
- 丢弃：VRChat Treats clarifying reply；benz145 手机形态/机场卫生间；nathie HomeView≈visionOS 顺带；SadlyItsBradley Halo3 fidget / Scarab mini-game / 无 XR 语境短视频

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-14 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
