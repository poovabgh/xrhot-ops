# STATUS — XRHOT X 采集状态

最后在本文件手工更新：2026-10-10 PT / 北京 扩账号并刷新 feeds。

## 订阅现状

| Feed | Items | lastBuildDate (GMT) | Raw URL |
|------|------:|---------------------|---------|
| x-official.xml | 80 | Sat, 10 Oct 2026 10:21:44 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml |
| x-media-kol.xml | 100 | Sat, 10 Oct 2026 10:21:44 GMT | https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml |

核对命令：

```bash
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-official.xml | grep -c '<item>'
curl -sL https://raw.githubusercontent.com/poovabgh/xrhot-ops/main/feeds/x-media-kol.xml | grep -c '<item>'
```

## 本轮：扩账号 + 近 14 天回填（2026-10-10）

- 新增 official：MetaVRDevs、LensStudioDev、magicleap、VRChat、BeatSaber（+28 条入库；feed 现 80）
- 新增 media-kol：benz145、CasandChary、SkarredGhost、Flat2VR、VRDesktop、SadlyItsBradley（候选 +134；feed 截断至 100）
- 方法：`get_users_posts(start_time≈2026-09-26, exclude=replies,retweets)` → XR 初筛 → 串帖合并 → t.co 展开 → 不改已有 guid

### 新账号 seen / kept

| Handle | 看了 | 留下 |
|--------|-----:|-----:|
| MetaVRDevs | 8 | 7 |
| LensStudioDev | 1 | 1 |
| magicleap | 2 | 2 |
| VRChat | 14 | 10 |
| BeatSaber | 9 | 8 |
| benz145 | 26 | 20 |
| CasandChary | 4 | 3 |
| SkarredGhost | 83 | 68 |
| Flat2VR | 5 | 3 |
| VRDesktop | 2 | 1 |
| SadlyItsBradley | 54 | 39 |

## 定时更新

| 项 | 状态 |
|----|------|
| 规范 | Asia/Shanghai 每日 **08:00、12:00、16:00、20:00**（整点），每周七天；有变化才 commit |
| 调度机制 | **Grok Bot routine** 按上述时刻唤醒；**只更新 RSS，有变化也不主动通知用户** |
| 旧规范「每 30 分钟」 | **已废止** |
| 省 token | 见 `scripts/cheap_check_plan.md` |

下一例行节点（北京时间）：按日历取下一个 08/12/16/20:00。

## 待办

- [ ] 可选：实现 `refresh_feeds.py` 自动化合并
- [ ] 可选：kentbye 等长期无帖账号的保留策略复核
- [ ] 用户若批准再考虑官方人员号；当前政策为只收公司官方号

## 旧仓库

`poovabgh/xrhot-feeds` → 仅保留指向本仓库的 README，不再更新 feeds。
