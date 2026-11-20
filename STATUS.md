# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-11-20 04:03 PST（例行 20:00 BJT 2026-11-20）。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 100 | Fri, 20 Nov 2026 12:03:51 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Fri, 20 Nov 2026 00:09:13 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：2026-11-20 20:00 BJT

- 预检 18 账号；最新 id 高于 watermark 且本轮已拉时间线：pimaxofficial、SadlyItsBradley；与上轮相同、未再拉时间线的：htcvive、Play_for_dream、PICOXR_Dev、VRChat、Dilmerv；其余等于 watermark 跳过（MetaVR_Official、PICOXR、BigscreenVR、XREAL_Global、RokidGlobal、getVITURE、MetaVRDevs、magicleap、BeatSaber、ARealityEvent、nathie）。无 most_recent 低于 watermark，未做删帖核对。htcvive most_recent 仍为转发 2118069208126747106（@XsensEnt Ultimate Tracker）。Play_for_dream most_recent 仍为对 @CarsonBarrel 的回复 2123607765969142225（16:00 BJT 已拉，exclude 后 0）。PICOXR_Dev most_recent 仍为已入库串帖续帖 2122242565194105089（自回 2122242336612896857）。VRChat most_recent 仍为已入库串帖续帖 2123549260000248096（自回 2123549256321781884）。Dilmerv most_recent 仍为转发自己的 2123579806537429181（转发 2123208850996109429；16:00 BJT 已拉，exclude 后 0）。pimaxofficial most_recent 从上轮已入库 2123358118721826942 变为新原创串帖 2123716023920865610（韩国展览 1日 차 照片，自回 2123716020217225505）；已拉时间线（since_id 2123358118721826942，exclude 后 result_count 2，合成 1 条入库：父帖 2123716020217225505 🇰🇷 한국 전시회 1일 차 성황리에 종료! ✨，t.co 展开为 https://x.com/pimaxofficial/status/2123716020217225505/photo/1；续帖 2123716023920865610 合成进父帖，t.co 展开为 https://x.com/pimaxofficial/status/2123716023920865610/photo/1）。SadlyItsBradley most_recent 仍为回复 2123543120763920787（@jmeyey8543540，08:00 BJT 已见）；本轮已拉时间线（since_id 2123534916025511973，exclude 后 result_count 0）。12:00 / 16:00 BJT 两轮无新原创，未 commit。
- **official 100→100（+1/−1 cap）：** pimaxofficial 🇰🇷 한국 전시회 1일 차 성황리에 종료! ✨ 2123716020217225505（合成自回 2123716023920865610 현장 열기가 가득했던 1일 차 모습을 사진으로 먼저 만나보세요!）。丢掉最旧 1 条：VRChat We want to clear something up about VRChat Public Instance Ownership! 2118772305803239922。
- **media-kol 100 不变（+0）。**
- top guid 抽查均在（official 现为 pimaxofficial Korea exhibition day 1 2123716020217225505 / VRChat Nov 19 Dev Update 2123549256321781884 / BeatSaber Billie Eilish 2123521746145866088 / getVITURE Vice City 2123506093741481991 / getVITURE TWO FLAGSHIPS 2123491002904186940 / BeatSaber Nostalgia is a Curse 2123478439088844912 / Play_for_dream hand gestures 2123476410920513943 / getVITURE 13 YEARS 2123468616641216588；media-kol 仍为 SadlyItsBradley Meta Start 2123534916025511973 / Dilmerv Tokyo Meta VR Glasses 2123512111540080852 / nathie spatial airdrop 2123481440104907056 / SadlyItsBradley decomps quote 2123467399664107864 / Dilmerv VR/MR AI tools 2123348430684586250 / Dilmerv Meta VR Start competition 2123319106656989445 / SadlyItsBradley gaussian splat 2123281801817051516 / Dilmerv TARGO Emmy quote 2123277400771567792）。
- 上一有变更档：2026-11-20 08:00 BJT official +7 VRChat Nov 19 Dev Update / BeatSaber Billie Eilish+OST 9 / getVITURE Vice City+BF prices+stickers / Play_for_dream hand gestures；media-kol +4 SadlyItsBradley Meta Start+Lucas quote / Dilmerv Tokyo Meta VR Glasses / nathie spatial airdrop。

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00、00:00（24:00）** 共五次（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：2026-11-21 **00:00**。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
