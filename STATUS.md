# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-12 00:08 PST（例行 16:00 BJT 2026-11-12）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 12 Nov 2026 00:06:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 12 Nov 2026 08:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-12 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、MetaVRDevs、VRChat、BeatSaber、nathie、Dilmerv、SadlyItsBradley；其余等于 watermark 跳过（PICOXR、XREAL_Global、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、magicleap、ARealityEvent）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。
- **official 100 不变（+0）：** MetaVR_Official 2120654800828420258 为已入库 2120654742716313712（GOLF+）的续帖；VRChat 2119893530722140614 为已入库 2119893528847233479（New Year's Entertainment Network）的续帖；htcvive / BigscreenVR / MetaVRDevs / BeatSaber most_recent 仍为回复或转发，与 12:00 BJT 预检相同，未拉到新原创。
- **media-kol 100→100（+3/−3 cap）：** SadlyItsBradley Apple Immersive event 2120785521983246782；Dilmerv Meta VR Glasses live demos / iteration tools 2120759750212067586；Dilmerv OVR Metrics Tool custom metrics / Hand Skate 2120735420891717650。丢掉最旧 3 条：nathie helium balloon AVP 2117696562482823659 / SadlyItsBradley I’ve been working really hard 2117690988823027712 / Dilmerv VR is not dead 2117651887616856389。nathie most_recent 2120701211636806141 为对已入库 Vision Pro cage 的回复，exclude 后无新原创。SadlyItsBradley `exclude` 后另有 2120667519430414372，为已入库 2120667515097620923（Vision Pro cage / Local SharePlay）的续帖，此前已合并，skip。
- top-6 guid 抽查均在（official 仍为 MetaVR_Official GOLF+ 2120654742716313712 / XREAL Hail Mary 2120593418816516440 / MetaVRDevs Unite Tokyo 2120591346872602912 / Play_for_dream AV 2120577299942699387 / XREAL Paper Birds 2120563760267960521 / RokidGlobal Rokid AR Spatial 2120532005356200047；新 media-kol SadlyItsBradley Apple Immersive 2120785521983246782 / Dilmerv live demos 2120759750212067586 / Dilmerv OVR Metrics 2120735420891717650 / SadlyItsBradley Vision Pro cage 2120667515097620923 / Spatial Audio orb 2120655657011716574 / Apple Q&A 2120639294364921992）。
- 上一有变更档：2026-11-12 08:00 BJT official +5 / media-kol +11。12:00 BJT 一轮无新原创、无 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-12 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
