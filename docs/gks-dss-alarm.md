# GKS 产品选型包 · DSS / Alarm / IVS

来源：GKS 签名链接 `01-Product_Selection.zip`（用户 2026-09-24 贴出）  
体积 **149,078,646 字节（约 142 MB）**，33 个条目。  
auth_key `1790271722` = **2026-09-24 17:42 UTC 过期**。目录和最新 xlsx 在过期前已抽到。

这是 **选型表包**，不是 datasheet 全集：报警、DSS / Extreme / CyberCity 许可表、IVS 服务器清单。没有法语规格书、没有 CNPP。

已落仓库：

- 包内清单：[`data/gks-dss-alarm-zip-inventory.csv`](../data/gks-dss-alarm-zip-inventory.csv)
- 型号↔料号：[`data/gks-dss-alarm-bom.csv`](../data/gks-dss-alarm-bom.csv)（0922 有的才当库存；IVS 的 GKS P/N 标了 `in_0922=no`）
- GKS IVS 原文表：[`data/gks-ivs-selection-20230214.csv`](../data/gks-ivs-selection-20230214.csv)
- 法语 CCTP：[`cctp-module-plateforme.md`](cctp-module-plateforme.md)、[`cctp-module-anti-intrusion.md`](cctp-module-anti-intrusion.md)

未入库：历史版本选型表、IRM 加密的 Excel 正文。

---

## 0. 哪些表能读、哪些不能

| 文件（最新） | 状态 |
|---|---|
| `Alarms/【Alarm】Product Selection_20260804.xlsx`（16.4 MB） | **Microsoft IRM EncryptedPackage**，打不开 |
| `Software/DSS Selection V8.8_20260409.xlsx` | 同上 |
| `Software/DSS Selection V2.21-20251126.xlsx` | 同上 |
| Extreme V4.0 / CyberCity V1.5.0 许可表 | 与 DSS V8.8 **字节完全相同**（同一份 IRM 壳），读不出许可格 |
| `IVS/IVS Selection List_20230214.xlsx` | **可读**，42 行，有 P/N 列 |

IRM 元数据指向总部 `it-policy.dahuatech.com`，签发 `fan_ziyan@dahuatech.com`。本环境没有 RMS 密钥，**不能解密**。型号和料号以 **0922 + 可读的 IVS 表 + 门禁目录报警彩页** 为准，**不编造选型格里的路数/容量**。

查询：

```bash
python3 -m src.dahua_identity lookup DHI-DSS4004-S2
python3 -m src.dahua_identity lookup DSS8PRV
python3 -m src.dahua_identity lookup DHI-ARC3800H-W2(868)
python3 -m src.dahua_identity lookup DHI-ARC3008C
python3 -m src.gks_catalog Datasheet_DHI-DSS7016DR-S2_EN.pdf
```

---

## 1. 包结构

| 目录 | 用途 | 最新日期 |
|---|---|---|
| `Alarms/` | 入侵选型，8 个历史文件（20240205 → **20260804**） | 2026-08-04 |
| `Software/` | DSS 选型 V2.16–V2.21、**DSS V8.8**、Extreme、CyberCity | DSS 8.8 = 2026-04-09 |
| `SoftwareOld version/` | 旧 DSS / Extreme / CyberCity | — |
| `IVS/` | 智能分析服务器选型 | **2023-02-14**（另有 20220613） |

---

## 2. 料号段

| 前缀 | 产品 | 0922 |
|---|---|---|
| `1.0.01.13` | DSS 一体机 / 平台硬件 | 24 行 |
| `2.9.02.07` | **DSS8** 软件许可 | 47 行 |
| `2.9.03.01` | 更早 DSS Express/Pro 许可 + Pro8 附加模块（MultiSite、AcuPick 等） | 25 行 |
| `1.0.01.19` | 入侵报警 ARC/ARD/ARA/ARM/ARK/ART | 287 行 |
| `1.0.01.23` | NVR；**IVSS** 也在这里，不是 `1.0.01.13` | IVSS 37 行 |
| `1.0.01.18` | IVS 分析服务器 | 0922 **几乎没有**（只有旧 `IVS-B5024-A`） |
| `2.9.02.10` | IVS 纯软件路数许可 | **0922 没有** |

GKS IVS 表里的 `1.0.01.18.*` / `2.9.02.10.*` **不要当 ERP 库存料号**。下单前必须在 0922 或法国价目里出现。

---

## 3. DSS 平台（对齐 0922，不是未解密的 V8.8 表）

### 3.1 版本后缀（DSS8 外部型号）

内部型号写成 `DHI-DSSExpress8-…` / `DHI-DSSPro8-…` / `DHI-DSSUltimate8-…`，外部是短码：

| 标记 | 含义 |
|---|---|
| **EX** | Express |
| **PR** | Professional |
| **UT** | Ultimate |
| **V** | 视频通道 |
| **D** | 门 / 门禁通道 |
| **AL** | 报警主机 |
| **VDP** | 对讲设备 |
| **VB / DB** | Video / Door **Base**（底座许可，和通道许可分开订） |
| **EX-PR / PR-UT** | 版本升级许可，不是新通道 |

例：`DSS8PRV` = Pro 视频通道 `2.9.02.07.10013`；`DSS8EXAL` = Express 报警 `2.9.02.07.10009`。

门禁 2025 目录写 DSS Pro **500 终端 / 1000 门**。这是彩页数字；V8.8 选型表打不开，**不要另编 Express/Ultimate 路数**。

### 3.2 硬件（`1.0.01.13`）

新项目优先 S2 / 7116：

| 外部型号 | 料号 | 角色 |
|---|---|---|
| `DHI-DSS4004-S2` | `1.0.01.13.11908` | 小一体机（Express 档常见） |
| `DHI-DSS4004-S2-W` | `1.0.01.13.11859` | 同系列 W 订货位 |
| `DHI-DSS7016D-S2` / `DHI-DSS7016DR-S2` | `1.0.01.13.11593` / `11596` | Pro 档一体机，D 与 DR 成对 |
| `DHI-DSS7116D` / `DHI-DSS7116DR` | `1.0.01.13.12877-9001` / `12876-9001` | 更新一代 7116 |

`DHI-DSS4004`、`DHI-DSS7016D` 仍在 0922，是 S2 之前的订货位。

许可和硬件要一起报：一体机 ≠ 通道授权。大项目常见：`DSS7016DR-S2` + `DSS8PRVB` + N×`DSS8PRV` + 门禁 `DSS8PRD` + 报警 `DSS8PRAL`。

CSU / 远程值守可加 `DSS8PRSIA`（SIA 事件推送）。

### 3.3 IVSS ≠ DSS

IVSS 是 **带智能卡的 NVR**，料号在 `1.0.01.23`，例如 `DHI-IVSS5108-1I`、`DHI-IVSS7108-1I-V2`、`DHI-IVSS7116DR`。后缀 `-nI` = 智能分析卡数量。人脸/结构化在边缘做，平台仍是 DSS。

---

## 4. 入侵报警（法国用 868）

0922 里型号字符串带 **868** 的约 233 条，带 **433** 的报警几乎没有（3 条 433 还不是报警主机）。法国无线必须写 **868 MHz**，内部/外部型号带 **`W2(868)`**。不要拿 433 主机出法国图。

### 4.1 命名

| 前缀 | 角色 | 例子 |
|---|---|---|
| **ARC** | 主机 / Hub | `ARC3000H`、`ARC3800H`、有线 `ARC3008C` |
| **ART-ARC** | 套装 | `ART-ARC3800H-03-FW2(868)` |
| **ARD** | 探测器 | `ARD1233` PIR、`ARD323` 门磁 |
| **ARA** | 警号 / 中继 / 遥控器 | `ARA12` 室内警号 |
| **ARK** | 键盘 | `ARK30T` / `ARK30C` |
| **ARM** | 扩展 / 继电器 / 墙开 | `ARM310` 扩展 |

无线后缀（按 0922 成对出现 + OEM 别名）：

| 后缀 | 含义 |
|---|---|
| **W2(868)** | 868 MHz 无线 |
| **FW2(868)** | Wi-Fi + 868 |
| **GW2(868)** | 蜂窝 + 868 |
| **W2(868S)** | 同系列 S 变体（门磁加长等） |
| **W2(868V)** | 带摄像机的室外探头 |
| **W2(868D)** | 水浸等 D 变体 |
| **W(868)** | 更早一代，只有 868、没有 W2 |

0922 给同一料号配了 OEM 短名，用来确认**功能**（不是第二台机器）：

| OEM 外部型号 | 内部型号 | 功能 |
|---|---|---|
| `WCENT` / `WCENT2` | `ARC3000H-FW2(868)` / `ARC3800H-FW2(868)` | 主机 |
| `WDCONT` | `ARD323-W2(868)` | 门磁 |
| `WPIRDET` | `ARD1233-W2(868)` | 红外 |
| `WDTDET` | `ARD2231-W2(868)` | 双鉴 |
| `WCAMDET` | `ARD1731-W2(868)` | 摄像探测器 |
| `WOUTDET` / `WOUTDETCAM` | `ARD2251E-W2(868)` / `(868V)` | 室外 / 室外+摄像 |
| `WGLASSBREAK` | `ARD512-W2(868)` | 玻璃破碎 |
| `WWATERDET` | `ARD912-W2(868D)` | 水浸 |
| `WSIREN` / `WOUTSIREN` | `ARA12` / `ARA13` | 室内 / 室外警号 |
| `WREPEATER` | `ARA43-W2(868)` | 中继 |
| `WKEYPAD` / `WKEYPAD-LCD` | `ARK30T` / `ARK30C-RW2` | 键盘 |
| `WKEYFOB-B` | `ARA24-W2(868)-B` | 遥控器 |
| `WEXPANDER` | `ARM310-W2(868)` | 扩展 |

出货仍用 **DHI-** 外部型号和料号，不要把 `WCENT` 写进 CCTP。

### 4.2 法国常用订货位（0922）

无线主机：

| 外部型号 | 料号 |
|---|---|
| `DHI-ARC3000H-W2(868)` / `-FW2(868)` / `-GW2(868)` | `1.0.01.19.10560` / `10557` / `10558` |
| `DHI-ARC3800H-W2(868)` / `-FW2(868)` | `1.0.01.19.10824-9002` / `10806-9001` |
| 套装 `DHI-ART-ARC3800H-03-FW2(868)` | `1.0.01.19.11086-0001` |

有线（门禁目录 59–63 页也有彩页）：

| 外部型号 | 料号 | 备注 |
|---|---|---|
| `DHI-ARC3008C` | `1.0.01.19.10457` | 目录写 **EN 50131 Grade 2** |
| `DHI-ARC2016C` | `1.0.01.19.10077` | 目录还写了 ARC2008C，**0922 没有 ARC2008C 行** |
| `DHI-ARC9016C` | `1.0.01.19.10243` | 内部 `…-V2` |

烟感 `DHI-HY-SA21A-W2(868)` 在 `1.0.01.36`，不是 `1.0.01.19`。

### 4.3 和 DSS 的关系

报警主机是设备，DSS 侧再订 `DSS8EXAL` / `DSS8PRAL`。不要把报警通道算进视频 `DSS8PRV`。

---

## 5. IVS（GKS 2023-02-14，0922 对不上）

可读表按类别：人脸 F7500、车辆 T8100、结构化 GS8000 / VS8000-R-PRO、交通事件 TB8000、人员行为 PB8000、**囚室 IP8000（仅 prisoner）**、视频质量 VQ8000、分析卡 T4 / AIX3200、CV 引擎 IVE-DP8000。

纯软件行是 `2.9.02.10.*` 或 `2.9.01.10.*`（VQ 的 PRO），0922 都没有。

**法国设计院**：人像 F7500 必须配 CNIL；囚室 IP8000 **不要写进民用 CCTP**；交通 TB8000 可以跟 Egis / Systra 路侧谈，但先确认法国能否订。

---

## 6. 设计院该带哪套

| 对象 | 带 | 不带 |
|---|---|---|
| Artelia / Oteis 楼宇 | DSS Express 或小 Pro + 门禁 64 门路径；无线 868 套装或有线 ARC3008C | IVS 机房服务器、囚室 IP8000、CyberCity |
| Egis / Systra / Ingérop 场站 | DSS Pro 一体机 + 视频/门/报警许可；IVSS 边缘智能 | Hero / 4G 电池枪当主系统 |
| Assystem 工业 | 周界有线 Grade 2 或 868 室外探头 + DSS；SIA 上值守 | 零售套装彩页当工业规范 |
| B 类安防所 | 868 主机+探头料号；强调 APSAD 仍缺证 | 把目录 EN50131 说成已 CNPP |
| D 类经销商 BE | ARC3800 套装 + DMSS；不必上 DSS Ultimate | 7116 + 上千路许可 |

Extreme / CyberCity 许可表打不开，城市超脑不要用本包出图。

---

## 7. 还缺

1. **未加密** 的 Alarm 20260804 和 DSS V8.8（或法国同事导出的 CSV）。  
2. 法国/EUR 可售过滤（868 型号 ≠ 法国都能订）。  
3. APSAD R82 / CNPP 认证表。  
4. Extreme / CyberCity 真表（现在是同一份 IRM 壳）。  
5. 无线摄像机 2026-06 目录 PDF（上一包链接已过期）。
