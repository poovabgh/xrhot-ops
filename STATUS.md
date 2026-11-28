# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-28 00:15 PST（例行 16:00 BJT 2026-11-28）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Sat, 28 Nov 2026 00:14:29 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 28 Nov 2026 08:15:07 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-28 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：nathie、Dilmerv、SadlyItsBradley。与上一轮 most_recent 相同、未重拉：MetaVRDevs（仍为转发 2125694388110242184 @8bitbob_dev mixed reality Koi pond / Meta VR Start）、ARealityEvent（仍为转发 2125851316467462419 @realityhackmit Hacker Scholarships）、RokidGlobal（仍为自回复 Event details 2126342918910980525，已合成进 Glasses Hackathon 2126342685212717557）。equal-watermark 跳过：MetaVR_Official、PICOXR、PICOXR_Dev、htcvive、BigscreenVR、XREAL_Global、getVITURE、pimaxofficial、Play_for_dream、magicleap、VRChat、BeatSaber。无 most_recent 低于 watermark，未做删帖核对。
- nathie most_recent 仍为 2126461472289259772（纯转发自身旧帖 VR gaming has officially peaked）；本轮仍拉时间线确认（since_id 2126104578647290142，exclude 后 result_count 1），仅为已合成进 GTA 6 in Vice City VR 2126104578647290142 的 Source 自回复 2126106019197538715，不重复入库。
- SadlyItsBradley most_recent 从 2126137327856582932（已按博主生活/闲聊丢掉的 Thanksgiving 旅行帖）变为 2126578561351909707（纯转发 @ASychov）；已拉时间线（since_id 2125293622560170322，exclude 后 result_count 2）：2126137327856582932 Flying international on Thanksgiving night 仍按博主生活/闲聊丢掉；2125329975624773897 The deed is done 已合成进 2125173193891856768，不重复入库。无新原创入库。
- Dilmerv most_recent 从 2126451174521942146（已入库 Sphenomenon，已合成 @GregMadison submission details）变为 2126576217684140220（回复 @utsxvrai Yeap! It reminds me of the old days of manual QA，回复不入库）；已拉时间线（since_id 2126451174521942146，exclude 后 result_count 5），入库 2：2126568039466328208 The biggest speedup I've had with Codex, Muse, or Claude isn't a better prompt.（XR development / simulators / headset）；2126550410022298038 A glasses-class device at about 100 grams changes the kinds of experiences worth building.。丢掉 2126505113086734658 My best results with Codex, Muse, or Claude come from small, specific tasks（通用 AI/游戏开发任务拆分，全文未提及 XR）。另有已合成自回复 2126451175671107707，以及自串回复 @dam00n Spatial SDK 2126454440978973082（上轮已按回复他人不入库），不重复处理。其他均为回复他人，不入库。
- **official 100 不变（+0）。**
- **media-kol 100→100（+2/−2 cap）：** Dilmerv The biggest speedup I've had with Codex, Muse, or Claude isn't a better prompt. 2126568039466328208；Dilmerv A glasses-class device at about 100 grams changes the kinds of experiences worth building. 2126550410022298038。丢掉最旧 2 条：Dilmerv On my way to Japan! 🇯🇵✈️ 2121233793038135521；ARealityEvent AWE launches @phaiworld, a new event co-located with AWE USA 2027, @Meta Quest App Store revenue in 2026 steady compared 2121141198962467113。
- top guid 抽查均在（official 现为 BigscreenVR BF sale 2126409459471950110 / BeatSaber OST 9 streaming 2126378527427613042 / MetaVR_Official Lone Star Showdown 2126376646148010372 / getVITURE Beast Pro 2 Best Buy 2126367271157199084 / XREAL_Global BF deals 2126360766894809462 / PICOXR atom/physics 2126345463531966687 / RokidGlobal Glasses Hackathon 2126342685212717557（已合成 Event details） / pimaxofficial Support Center / YouTube 2126330328172388610 / XREAL_Global Aimi Sekiguchi AURA 2126285156772143410 / BigscreenVR Beyond 2 BF sale 2126093369474748569 / Play_for_dream Thanksgiving 2126013122859221062 / XREAL_Global Thanksgiving 2125998268635115626 / BeatSaber Flameblade 2125978970055135606 / RokidGlobal Thanksgiving 2125972066050757017 / VRChat VRCat V2 2125953646907322831 / XREAL_Global Blender AURA 2125924529704771679 / XREAL_Global Zach Lieberman AURA 短帖 2125849255621636496 / XREAL_Global AURA apoQlar surgery Cain 2125800881421697049 / BigscreenVR Halo Mount 2125772610130829398 / VRChat Holiday Gifting / Hype Train 2125711956757655999（已合成 YouTube） / MetaVR_Official Courtside Spring 2027 2125674090594029966；media-kol 现为 Dilmerv XR simulators 2126568039466328208 / Dilmerv glasses-class 100g 2126550410022298038 / Dilmerv Sphenomenon 2126451174521942146（已合成 @GregMadison details） / Dilmerv Hand Skate gestures 2126428408917742041 / Dilmerv next years in XR 2126383274041749975 / Dilmerv Meta VR Glasses puzzle quote 2126376893016662093 / Dilmerv XR agents examples 2126353069193490892 / Dilmerv developing inside VR 2126300464446624068 / Dilmerv Meta VR Glasses workflows 2126247190381162935 / Dilmerv Meta VR Start submissions 2126165750318571737 / Dilmerv Unite Tokyo glasses reactions 2126150066008129565 / Dilmerv Meta VR CLI checks 2126126411886805144 / nathie GTA 6 in Vice City VR 2126104578647290142（已合成 Source） / Dilmerv coffee cup Unity guide 2126096239372431852 / Dilmerv Hand Skate NPC 2126096153372701104 / Dilmerv Meta VR CLI MCP 2126058519543546367（已合成 4 条自回复） / Dilmerv metavr skills install 2126013737739911372 / nathie Sock Puppet Superstar 2126000134173475057（已合成 More here） / Dilmerv tabletop MR hands 2125953232375570693 / Dilmerv Hermes Quest quote 2125845038898843959 / Dilmerv metavr perf tip 2125836978537025765 / Dilmerv VR/MR onboarding 2125816855403073832 / Dilmerv Hand Skate Comic Look 2125767482640076866 / Dilmerv lightweight VR glasses devs 2125733794116186138 / Dilmerv Muse Code guide finished 2125723311925604424 / Dilmerv busy weeks VR Level Up / Hand Skate / Valem 2125685976349421768 / nathie Batman Arkham Shadow VR hands 2125682080684134443 / ARealityEvent Physical AI World 2027 2125650804950626629 / Dilmerv Meta VR CLI docs search 2125649965460414943）。
- 上一有变更档：2026-11-28 08:00 BJT official +5（BigscreenVR BF sale / BeatSaber OST 9 streaming / MetaVR_Official Lone Star Showdown / getVITURE Beast Pro 2 Best Buy / XREAL_Global BF deals）；media-kol +5（Dilmerv Sphenomenon / Dilmerv Hand Skate gestures / Dilmerv next years in XR / Dilmerv Meta VR Glasses puzzle quote / Dilmerv XR agents examples）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-28 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
