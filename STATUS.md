# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-12 08:08 PST（例行 00:00 BJT 2026-11-13）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 12 Nov 2026 16:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 12 Nov 2026 16:08:00 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-13 00:00 BJT

- 预检 18 账号；最新 id 高于 watermark：MetaVR_Official、htcvive、BigscreenVR、XREAL_Global、pimaxofficial、MetaVRDevs、VRChat、BeatSaber、nathie、Dilmerv；其余等于 watermark 跳过（PICOXR、RokidGlobal、getVITURE、Play_for_dream、magicleap、ARealityEvent、SadlyItsBradley）。PICOXR_Dev 当前 feed 无条目，most_recent 仍为此前 cap 掉的 2115634287437570110，跳过。无 most_recent 低于 watermark，未做删帖核对。
- **official 100→100（+2/−2 cap）：** BeatSaber OST 9 2120880358769983705；pimaxofficial IMSA Esports / Pimax logo / iRacing VR 2120866625205240035。丢掉最旧 2 条：VRChat Hatsune Miku Yozora Program 2115805711963762827 / BeatSaber How do you know someone truly ❤️ Beat Saber? 2115804629468389591。MetaVR_Official 2120654800828420258 为已入库 2120654742716313712（GOLF+）的续帖；VRChat 2119893530722140614 为已入库 2119893528847233479（New Year's Entertainment Network）的续帖；htcvive / BigscreenVR / MetaVRDevs exclude 后 result_count 0。XREAL_Global most_recent 2120806623073763363 仍为 Twitter Ads/Amplify CPC 变体（organic timeline result_count 0，未入库）。
- **media-kol 100→100（+1/−1 cap）：** nathie Gentle Monster smart glasses（Google/Samsung，起售 $449）2120906374301315571。丢掉最旧 1 条：Dilmerv Mmm, I think I released enough VR/MR games 2117712194200563899。Dilmerv most_recent 2120893061035335707 为转发，exclude 后 result_count 0。
- top guid 抽查均在（official 现为 BeatSaber OST 9 2120880358769983705 / pimaxofficial IMSA 2120866625205240035 / MetaVR_Official GOLF+ 2120654742716313712 / XREAL Hail Mary 2120593418816516440 / MetaVRDevs Unite Tokyo 2120591346872602912 / Play_for_dream AV 2120577299942699387；media-kol 现为 nathie Gentle Monster 2120906374301315571 / SadlyItsBradley Apple Immersive 2120785521983246782 / Dilmerv live demos 2120759750212067586 / Dilmerv OVR Metrics 2120735420891717650 / SadlyItsBradley Vision Pro cage 2120667515097620923 / Spatial Audio orb 2120655657011716574）。
- 上一有变更档：2026-11-12 16:00 BJT media-kol +3。20:00 BJT 一轮无新原创入库、无 commit（XREAL_Global Ads 变体未入库）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-13 **08:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
