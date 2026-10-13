# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-13 08:13 BJT 例行刷新。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 94 | Tue, 13 Oct 2026 00:12:58 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 75 | Tue, 13 Oct 2026 00:12:58 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-10-13 08:00 BJT

- 廉价预检：23 账号 `most_recent_tweet_id`；14 个最新 id 高于 watermark；`exclude=replies,retweets` 后有原创候选的：PICOXR、htcvive、XREAL_Global、RokidGlobal、pimaxofficial、nathie、Dilmerv、benz145、SadlyItsBradley；BigscreenVR / rayneo_global / VRChat（仅串帖回复）/ kentbye / Flat2VR 为 0 或回复/转发。
- **official：** 88→**94**（+6）
  - htcvive `2109687924065206417`：VIVE Eagle 智能眼镜多模式
  - RokidGlobal `2109667673508655591`：X Takeover 2026 / Giga Texas 展示 Rokid Glasses
  - PICOXR `2109660593309307123`：SKY LEGENDS VR 航线游戏上架
  - pimaxofficial `2109660373997723723`：Crystal Pro 光学与面板规格
  - RokidGlobal `2109660360793854153`：Cybercab POV + Rokid Glasses
  - XREAL_Global `2109630435126804605`：XREAL 1 Pro+ 倒计时（10/15）
- **media-kol：** 70→**75**（+5）
  - nathie `2109752713865261394`：Apple Vision Pro 上看 Remnants
  - Dilmerv `2109726213765988525`：Table Troopers VR 开发者 showcase
  - SadlyItsBradley `2109724676671119794`：Apple 再度营销 Vision Pro / Remnants
  - Dilmerv `2109704177329086743`：自建 MR 桌面游戏（串帖合成）
  - Dilmerv `2109695883868885498`：Muse Wonder 用于 VR 工作流（引用）
  - 丢弃：benz145 机场卫生间；SadlyItsBradley 桌面 fidget / 宠物厨房 / 无 XR 语境短视频；VRChat Treats 澄清回复（已发条目不改、回复不单列）

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-10-13 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye / Flat2VR 等低产出账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
