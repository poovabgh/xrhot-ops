# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-26 00:16 PST（例行 16:00 BJT 2026-11-26）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Thu, 26 Nov 2026 08:16:59 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Thu, 26 Nov 2026 08:16:59 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-26 16:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、ARealityEvent、Dilmerv。与上一轮 most_recent 相同、未重拉：MetaVRDevs（仍为转发 2125694388110242184 @8bitbob_dev mixed reality Koi pond / Meta VR Start）、Play_for_dream（仍为回复 2123607765969142225 @CarsonBarrel）、VRChat（仍为转发 2125765152897405127 @SANCTUMVR）、SadlyItsBradley（仍为转发 2125787243486806311 @EOZ_VR）。其余等于 watermark 跳过（MetaVR_Official、PICOXR、PICOXR_Dev、htcvive、BigscreenVR、RokidGlobal、getVITURE、pimaxofficial、magicleap、BeatSaber、nathie）。无 most_recent 低于 watermark，未做删帖核对。XREAL_Global most_recent 从 2125800881421697049（已入库 AURA apoQlar surgery Cain）变为 2125849255621636496；`get_users_posts`（since_id 2125800881421697049，exclude 与不 exclude）及 `searchPostsAll from:XREAL_Global` 均 result_count 0，但 `get_posts_by_id` 与公开页确认为原创短帖，入库 1：2125849255621636496 Words you can walk around.（前两句与已入库 2125579410753679425 相同，卡片复用同一 Zach Lieberman / XREAL AURA 视频；新 id，照收）。ARealityEvent most_recent 从 2125650804950626629 变为 2125851316467462419（转发 @realityhackmit Hacker Scholarships）；已拉时间线（since_id 2125650804950626629，exclude 后 result_count 0），无新原创入库。Dilmerv most_recent 从 2125794214789222426（上一轮已丢掉的非 XR AI agents 问帖）变为 2125849117125648691（回复 @witcheer @StefanMaier It shows quite well!）；已拉时间线（since_id 2125767482640076866，exclude 后 result_count 4），入库 3：2125845038898843959 This is such a cool crossover of AI agents and Quest 👏（引用 @StefanMaier Hermes Agent Talaria 在 Quest 3 / 3S / Meta VR Glasses）；2125836978537025765 Here’s a quick Meta VR Glasses / Quest performance tip! 👇（metavr perf capture / Perfetto）；2125816855403073832 I’ve been thinking about this quite a bit while polishing my latest MR games.（VR/MR 首 60 秒 / onboarding）。丢掉已在上一轮判定非 XR 的 2125794214789222426 Here’s a question for developers using AI agents。
- **official 100→100（+1/−1 cap）：** XREAL_Global Words you can walk around. 2125849255621636496（Zach Lieberman / AURA 短帖+视频卡片）。丢掉最旧 1 条：pimaxofficial Pimax가 G-STAR 2026에 참가합니다! 2121055807618101380。
- **media-kol 100→100（+3/−3 cap）：** Dilmerv This is such a cool crossover of AI agents and Quest 👏 2125845038898843959；Dilmerv Here’s a quick Meta VR Glasses / Quest performance tip! 👇 2125836978537025765；Dilmerv I’ve been thinking about this quite a bit while polishing my latest MR games. 2125816855403073832。丢掉最旧 3 条：Dilmerv One of my favorite things about VR/MR development is how much the scale of an experience can change how it feels. 2120616320957915253 / SadlyItsBradley $1695 USD, launches in December 2120589411197059112 / SadlyItsBradley Apple and BlackMagic announced a new Ambisonic microphone designed for insanely high fidelity Spatial Audio 2120586432079450245。
- top guid 抽查均在（official 现为 XREAL_Global Zach Lieberman AURA 短帖 2125849255621636496 / XREAL_Global AURA apoQlar surgery Cain 2125800881421697049 / BigscreenVR Halo Mount 2125772610130829398 / VRChat Holiday Gifting / Hype Train 2125711956757655999（已合成 YouTube） / MetaVR_Official Courtside Spring 2027 2125674090594029966 / BeatSaber Memory Marker 2125641068486041632 / PICOXR classic game VR 2125620683614892490 / pimaxofficial Play 2.0.5 2125605552701227050 / XREAL_Global AURA Micro Center 2125591084340261323 / getVITURE giveaway reminder 2125590821437112463 / XREAL_Global Zach Lieberman 2125579410753679425 / PICOXR_Dev PICO Space Program 2125542244900032734 / XREAL_Global Gabor A Bicycle for the Mind 2125535085260853389 / XREAL_Global Gugenka Anime worlds 2125520767677014018 / XREAL_Global AURA surgery Kane 2125487936162676954 / BigscreenVR pssst BF sale 2125418341259264484；media-kol 现为 Dilmerv Hermes Quest quote 2125845038898843959 / Dilmerv metavr perf tip 2125836978537025765 / Dilmerv VR/MR onboarding 2125816855403073832 / Dilmerv Hand Skate Comic Look 2125767482640076866 / Dilmerv lightweight VR glasses devs 2125733794116186138 / Dilmerv Muse Code guide finished 2125723311925604424 / Dilmerv busy weeks VR Level Up / Hand Skate / Valem 2125685976349421768 / nathie Batman Arkham Shadow VR hands 2125682080684134443 / ARealityEvent Physical AI World 2027 2125650804950626629 / Dilmerv Meta VR CLI docs search 2125649965460414943 / Dilmerv Hand Skate excitement 2125605830888165521 / nathie Steam VR GOTY voting 2125587072400384338（已合成 Vote here） / Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / Dilmerv Static MRUK occlusion 2125316559140700577 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322）。
- 上一有变更档：2026-11-26 12:00 BJT official +2（XREAL_Global AURA apoQlar surgery Cain / BigscreenVR Halo Mount）；media-kol +1（Dilmerv Hand Skate Comic Look）。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-26 **20:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
