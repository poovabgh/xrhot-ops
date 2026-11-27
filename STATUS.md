# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-27 04:18 PST（例行 20:00 BJT 2026-11-27）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 27 Nov 2026 12:18:43 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 27 Nov 2026 12:18:43 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-27 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：XREAL_Global、BeatSaber、Dilmerv。与上一轮 most_recent 相同、未重拉：MetaVRDevs（仍为转发 2125694388110242184 @8bitbob_dev mixed reality Koi pond / Meta VR Start）、ARealityEvent（仍为转发 2125851316467462419 @realityhackmit Hacker Scholarships）、nathie（仍为自回复 Source 2126106019197538715，已合成进 GTA 6 in Vice City VR 2126104578647290142）、SadlyItsBradley（仍为 2126137327856582932 Flying international on Thanksgiving night，已按博主生活/闲聊丢掉）、BigscreenVR（仍为自回复 2126095827294920968，已合成进 Beyond 2 BF sale 2126093369474748569）。equal-watermark 跳过：MetaVR_Official、PICOXR、PICOXR_Dev、htcvive、RokidGlobal、getVITURE、pimaxofficial、Play_for_dream、magicleap、VRChat。无 most_recent 低于 watermark，未做删帖核对。XREAL_Global most_recent 从 2125998268635115626（已入库 Thanksgiving）变为 2126285156772143410；已拉时间线（since_id 2125998268635115626，exclude 后 result_count 1），入库 1：2126285156772143410 Where tradition meets another dimension. 🌿（3D artist Aimi Sekiguchi / XREAL AURA / Android XR）。BeatSaber most_recent 从 2125978970055135606（已入库 Flameblade）变为 2126266558355849694（回复 @Shorties1326 Sending hugs! ❤️ 💙，回复不入库）；已拉时间线（since_id 2125978970055135606，exclude 后 result_count 0）。Dilmerv most_recent 从 16:00 轮的回复 @williamsburg399 Well done! 变为 2126247190381162935；已拉时间线（since_id 2126165750318571737，exclude 后 result_count 2），入库 1：2126247190381162935 One thing I've really enjoyed while experimenting with Meta VR Glasses is how comfortable it feels to spend more time working directly in VR!；丢掉 2126187270084424054 career/AI developer advice（16:00 轮已按通用 AI/职业建议丢掉，全文仍无 XR 提及）。Dilmerv 其余为对他人回复（不入库）。
- **official 100→100（+1/−1 cap）：** XREAL_Global Where tradition meets another dimension. 🌿 2126285156772143410。丢掉最旧 1 条：MetaVR_Official Missed the Eastern Conference showdown between the 76ers and the Celtics? 2121347262102265922。
- **media-kol 100→100（+1/−1 cap）：** Dilmerv One thing I've really enjoyed while experimenting with Meta VR Glasses is how comfortable it feels to spend more time working directly in VR! 2126247190381162935。丢掉最旧 1 条：ARealityEvent AWE and @phaiworld come together in Long Beach to create the new epicenter of spatial intelligence. 2120924636741525698。
- top guid 抽查均在（official 现为 XREAL_Global Aimi Sekiguchi AURA 2126285156772143410 / BigscreenVR Beyond 2 BF sale 2126093369474748569 / Play_for_dream Thanksgiving 2126013122859221062 / XREAL_Global Thanksgiving 2125998268635115626 / BeatSaber Flameblade 2125978970055135606 / RokidGlobal Thanksgiving 2125972066050757017 / VRChat VRCat V2 2125953646907322831 / XREAL_Global Blender AURA 2125924529704771679 / XREAL_Global Zach Lieberman AURA 短帖 2125849255621636496 / XREAL_Global AURA apoQlar surgery Cain 2125800881421697049 / BigscreenVR Halo Mount 2125772610130829398 / VRChat Holiday Gifting / Hype Train 2125711956757655999（已合成 YouTube） / MetaVR_Official Courtside Spring 2027 2125674090594029966 / BeatSaber Memory Marker 2125641068486041632 / PICOXR classic game VR 2125620683614892490 / pimaxofficial Play 2.0.5 2125605552701227050 / XREAL_Global AURA Micro Center 2125591084340261323 / getVITURE giveaway reminder 2125590821437112463 / XREAL_Global Zach Lieberman 2125579410753679425 / PICOXR_Dev PICO Space Program 2125542244900032734；media-kol 现为 Dilmerv Meta VR Glasses workflows 2126247190381162935 / Dilmerv Meta VR Start submissions 2126165750318571737 / Dilmerv Unite Tokyo glasses reactions 2126150066008129565 / Dilmerv Meta VR CLI checks 2126126411886805144 / nathie GTA 6 in Vice City VR 2126104578647290142（已合成 Source） / Dilmerv coffee cup Unity guide 2126096239372431852 / Dilmerv Hand Skate NPC 2126096153372701104 / Dilmerv Meta VR CLI MCP 2126058519543546367（已合成 4 条自回复） / Dilmerv metavr skills install 2126013737739911372 / nathie Sock Puppet Superstar 2126000134173475057（已合成 More here） / Dilmerv tabletop MR hands 2125953232375570693 / Dilmerv Hermes Quest quote 2125845038898843959 / Dilmerv metavr perf tip 2125836978537025765 / Dilmerv VR/MR onboarding 2125816855403073832 / Dilmerv Hand Skate Comic Look 2125767482640076866 / Dilmerv lightweight VR glasses devs 2125733794116186138 / Dilmerv Muse Code guide finished 2125723311925604424 / Dilmerv busy weeks VR Level Up / Hand Skate / Valem 2125685976349421768 / nathie Batman Arkham Shadow VR hands 2125682080684134443 / ARealityEvent Physical AI World 2027 2125650804950626629 / Dilmerv Meta VR CLI docs search 2125649965460414943 / Dilmerv Hand Skate excitement 2125605830888165521 / nathie Steam VR GOTY voting 2125587072400384338（已合成 Vote here） / Dilmerv Daniel Meta VR Competition quote 2125501625792147675 / Dilmerv Muse Code + Meta VR CLI + Unity VR CLI guide 2125337486905717034 / SadlyItsBradley Spatial Darkroom Live 3D View quote 2125293622560170322）。
- 上一有变更档：2026-11-27 12:00 BJT official +0；media-kol +4（Dilmerv Meta VR Start submissions / Dilmerv Unite Tokyo glasses reactions / Dilmerv Meta VR CLI checks / nathie GTA 6 in Vice City VR）。16:00 BJT 轮无入库、无 commit。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-28 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
