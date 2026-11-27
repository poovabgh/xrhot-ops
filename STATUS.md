# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-26 16:07 PST（例行 08:00 BJT 2026-11-27）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 27 Nov 2026 00:07:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 27 Nov 2026 00:07:35 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-27 08:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：BigscreenVR、XREAL_Global、Play_for_dream、nathie、Dilmerv、SadlyItsBradley。与上一轮 most_recent 相同、未重拉：MetaVRDevs（仍为转发 2125694388110242184 @8bitbob_dev mixed reality Koi pond / Meta VR Start）、ARealityEvent（仍为转发 2125851316467462419 @realityhackmit Hacker Scholarships）。其余等于 watermark 跳过（MetaVR_Official、PICOXR、PICOXR_Dev、htcvive、RokidGlobal、getVITURE、pimaxofficial、magicleap、VRChat、BeatSaber）。无 most_recent 低于 watermark，未做删帖核对。BigscreenVR most_recent 从 2125772610130829398（已入库 Halo Mount）变为 2126095827294920968（自回复配件折扣）；已拉时间线（since_id 2125772610130829398，exclude 后 result_count 2），入库 1 条合成：2126093369474748569 When they had buddy playing VR in the trailer I didn't expect THIS.（Beyond 2 黑色星期五：免费 Audio Strap / Custom Fit Cushion、配件与镜片 25% off，至 11 月 30 日；已合成自回复 2126095827294920968，店链 https://store.bigscreenvr.com/blogs/beyond/beyond-2-black-friday-2026）。XREAL_Global most_recent 从 2125924529704771679（已入库 Blender AURA）变为 2125998268635115626；已拉时间线（since_id 2125924529704771679，exclude 后 result_count 1），入库 1：2125998268635115626 Grateful for every moment. 🧡（感恩节问候，含 #ARGlasses）。Play_for_dream most_recent 从 2123607765969142225（上一轮未重拉的回复 @CarsonBarrel）变为 2126013122859221062；已拉时间线（since_id 2123476410920513943，exclude 后 result_count 1），入库 1：2126013122859221062 Grateful for the worlds we explore and the people we share them with. 🧡（感恩节问候，含 #VR）。nathie most_recent 从 2125682080684134443 变为 2126087520265933157（回复 @helmetrius 💀，不入库）；已拉时间线（since_id 2125682080684134443，exclude 后 result_count 2），入库 1 条合成：2126000134173475057 VR gaming has officially peaked（Sock Puppet Superstar，已合成自回复 2126000718779765039 More here）。Dilmerv most_recent 从 2125953233524756987（上一轮已合成进桌面 MR 的 Credit 自回复）变为 2126096239372431852；已拉时间线（since_id 2125953232375570693，exclude 后 result_count 10），入库 4：2126096239372431852 If you're starting a Meta VR Glasses prototype in Unity…（coffee cup 上手指南，链 https://developers.meta.com/vr/blog/start-building-for-meta-vr-glasses-with-dilmer-valecillos/）；2126096153372701104 Hand Skate for Meta VR Glasses just got its first NPC 🛹；2126058519543546367 Using Codex, Muse, or Claude for Quest dev? Connect it to the Meta VR CLI's MCP server.（已合成 4 条自回复，Docs https://developers.meta.com/vr/essentials/metavr-overview/）；2126013737739911372 XR devs, if you're using an AI coding agent with Meta XR SDKs…（`metavr skills install --all`，Docs https://developers.meta.com/vr/essentials/agent-skills/）。丢掉 2126047132985577901 I remember a time in my career…（分享未完成作品/营销建议，无 XR 提及，按博主生活/闲聊丢弃）。跳过已入库桌面 MR 根帖的 Credit 自回复 2125953233524756987。SadlyItsBradley most_recent 从 2125787243486806311（上一轮未重拉的转发 @EOZ_VR）变为 2126008298042462505（转发 @sxpstudio Happy Thanksgiving!，纯转发不入库）；exclude 后 result_count 1 为已合成进 2125173193891856768 的自回复 2125329975624773897 The deed is done，无新入库。
- **official 100→100（+3/−3 cap）：** BigscreenVR When they had buddy playing VR in the trailer I didn't expect THIS. 2126093369474748569（已合成 BF 配件折扣自回复）；Play_for_dream Grateful for the worlds we explore and the people we share them with. 🧡 2126013122859221062；XREAL_Global Grateful for every moment. 🧡 2125998268635115626。丢掉最旧 3 条：BeatSaber Before they made "LFG", @whoisconfetti were Beat Saber players. 😎 2121308812963438930 / MetaVRDevs Fresh release notes here! 📣📰 2121305089449308635 / MetaVR_Official What’s your longest drive? 2121289448939987427。
- **media-kol 100→100（+5/−5 cap）：** Dilmerv If you're starting a Meta VR Glasses prototype in Unity, start with one tiny interaction before you build the whole game 2126096239372431852；Dilmerv Hand Skate for Meta VR Glasses just got its first NPC 🛹 2126096153372701104；Dilmerv Using Codex, Muse, or Claude for Quest dev? Connect it to the Meta VR CLI's MCP server. 2126058519543546367（已合成 4 条自回复）；Dilmerv XR devs, if you're using an AI coding agent with Meta XR SDKs, install the official Meta VR agent skills so it has real  2126013737739911372；nathie VR gaming has officially peaked 2126000134173475057（已合成 More here）。丢掉最旧 5 条：Dilmerv Guys, I found another very cool feature for Quest & Meta VR Glasses devs! 👇 2120735420891717650 / SadlyItsBradley This is how Apple records all of their first person content Vision Pro trailers/app previews on device 2120667515097620923 / SadlyItsBradley I found the magical Spatial Audio orb 2120655657011716574 / SadlyItsBradley Q&A just started, and they picked the most important question to lead with: 2120639294364921992 / Dilmerv Guys, I found another very cool feature in the Meta VR CLI! 👇 2120622649965416657。
- top guid 抽查均在（official 现为 BigscreenVR Beyond 2 BF sale 2126093369474748569 / Play_for_dream Thanksgiving 2126013122859221062 / XREAL_Global Thanksgiving 2125998268635115626 / BeatSaber Flameblade 2125978970055135606 / RokidGlobal Thanksgiving 2125972066050757017 / VRChat VRCat V2 2125953646907322831 / XREAL_Global Blender AURA 2125924529704771679 / XREAL_Global Zach Lieberman AURA 短帖 2125849255621636496 / XREAL_Global AURA apoQlar surgery Cain 2125800881421697049 / BigscreenVR Halo Mount 2125772610130829398 / VRChat Holiday Gifting / Hype Train 2125711956757655999（已合成 YouTube） / MetaVR_Official Courtside Spring 2027 2125674090594029966 / BeatSaber Memory Marker 2125641068486041632 / PICOXR classic game VR 2125620683614892490 / pimaxofficial Play 2.0.5 2125605552701227050 / XREAL_Global AURA Micro Center 2125591084340261323 / getVITURE giveaway reminder 2125590821437112463 / XREAL_Global Zach Lieberman 2125579410753679425 / PICOXR_Dev PICO Space Program 2125542244900032734；media-kol 现为 Dilmerv coffee cup Unity guide 2126096239372431852 / Dilmerv Hand Skate NPC 2126096153372701104 / Dilmerv Meta VR CLI MCP 2126058519543546367（已合成 4 条自回复） / Dilmerv metavr skills install 2126013737739911372 / nathie Sock Puppet Superstar 2126000134173475057（已合成 More here） / Dilmerv tabletop MR hands 2125953232375570693 / Dilmerv Hermes Quest quote 2125845038898843959 / Dilmerv metavr perf tip 2125836978537025765 / Dilmerv VR/MR onboarding 2125816855403073832 / Dilmerv Hand Skate Comic Look 2125767482640076866 / Dilmerv lightweight VR glasses devs 2125733794116186138 / Dilmerv Muse Code guide finished 2125723311925604424 / Dilmerv busy weeks VR Level Up / Hand Skate / Valem 2125685976349421768 / nathie Batman Arkham Shadow VR hands 2125682080684134443 / ARealityEvent Physical AI World 2027 2125650804950626629 / Dilmerv Meta VR CLI docs search 2125649965460414943 / Dilmerv Hand Skate excitement 2125605830888165521 / nathie Steam VR GOTY voting 2125587072400384338（已合成 Vote here） / Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322）。
- 上一有变更档：2026-11-27 00:00 BJT official +4（BeatSaber Flameblade / RokidGlobal Thanksgiving / VRChat VRCat V2 / XREAL_Global Blender AURA）；media-kol +1（Dilmerv tabletop MR hands）。20:00 BJT 无变更未提交。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-27 **12:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
