# 02 — 账号清单说明

机器可读清单在 `accounts/*.json`。本文是人类可读摘要。

## Official → `feeds/x-official.xml`

| Handle | 品牌 | 备注 |
|--------|------|------|
| MetaVR_Official | Meta | 首批 |
| PICOXR | PICO | 首批 |
| htcvive | HTC Vive | 首批 |
| BigscreenVR | Bigscreen | 首批 |
| XREAL_Global | XREAL | 2026-10-09 扩 |
| RokidGlobal | Rokid | 2026-10-09 扩 |
| getVITURE | VITURE | 2026-10-09 扩 |
| rayneo_global | RayNeo | 2026-10-09 扩 |
| pimaxofficial | Pimax | 2026-10-09 扩（站内另有 blog Atom） |
| Play_for_dream | Play For Dream | 2026-10-09 扩（站内另有 press Atom） |
| PICOXR_Dev | PICO | 开发者号，官方侧 |
| MetaVRDevs | Meta | 2026-10-10 扩；Meta VR Developers |
| LensStudioDev | Snap | 2026-10-10 扩；Lens Studio / Spectacles |
| magicleap | Magic Leap | 2026-10-10 扩 |
| VRChat | VRChat | 2026-10-10 扩；平台/内容 |
| BeatSaber | Beat Games | 2026-10-10 扩 |

政策（用户 2026-10-09）：**只加官方公司号**；官方人员个人号（如 `boztank`）不加。2026-10-10 扩的是公司/产品官方号（含平台与头部游戏官方号）。

## Media + KOL → `feeds/x-media-kol.xml`

| Handle | 类型 | 备注 |
|--------|------|------|
| ARealityEvent | 展会/媒体向 | AWE |
| nathie | KOL | 试戴/消费向；需 XR 初筛 |
| Dilmerv | KOL | Meta XR 开发向；需 XR 初筛 |
| kentbye | KOL | Voices of VR；可能长时间无帖 |
| benz145 | KOL | 2026-10-10；Ben Lang；需 XR 初筛 |
| CasandChary | KOL | 2026-10-10；试戴/评测 |
| SkarredGhost | KOL | 2026-10-10；AR/VR 博主；量大需初筛 |
| Flat2VR | KOL | 2026-10-10；Flat-to-VR 模组社区 |
| VRDesktop | KOL | 2026-10-10；Virtual Desktop / Guy Godin |
| SadlyItsBradley | KOL | 2026-10-10；硬件/空间计算；需初筛 |

## 有网站 RSS → 不加 X

见 `accounts/skipped-media-rss.json`：UploadVR、Road to VR、映维资讯、93913、MIXED（栏目过滤 VR/AR/AI Glasses）。

厂商官网 RSS（Pimax blog、玩出梦想 press、Meta Newsroom 等）由站内 sources 配置，**不**因此禁止对应公司 X（公司 X 仍可在 official）。

## 拒绝 / 低置信 / 未找到

见 `accounts/rejected.json`（如 HardwareSteam、阀门/大厂主号噪声、未找到的专用号等）。

## 品牌别名（站内评分，非 X 过滤）

评分 A 名单在站代码 `industry/brands.ts`。别名匹配会算到公司。本仓不复制维护全表；扩账号时可用品牌名对齐 evidence。已知品牌包括：Meta、Apple、Valve、Samsung、Google、PICO、ByteDance、Qualcomm、Pimax、Play For Dream、HTC Vive、Bigscreen、XREAL、Rokid、RayNeo、VITURE、Xiaomi、Huawei、Alibaba/Quark、Baidu 等。
