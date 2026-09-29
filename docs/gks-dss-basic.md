# GKS DSS 基础资料包 · Basic Information

来源：GKS 签名链接 `01.Basic_Infomation.zip`（官方拼写 Infomation；用户 2026-09-29 贴出）  
体积 **1,945,395,477 字节（约 1.81 GB）**，92 个条目。  
auth_key `1790714642` = **2026-09-29 20:44 UTC 过期**。HEAD 403，Range GET 通。

这是 **DSS 平台基础包**（策略、系统需求、兼容、认证、选型、图标、第三方），不是入侵 datasheet。和先前的 `01-Product_Selection.zip` 互补：那边 Alarm/IVS 选型，这边 DSS 容量和许可说明。

已落仓库：

- 包内清单：[`data/gks-dss-basic-zip-inventory.csv`](../data/gks-dss-basic-zip-inventory.csv)
- V8.5 对比要点：[`data/dss-v85-comparison-key.csv`](../data/dss-v85-comparison-key.csv)
- V8.6 兼容（门禁/报警/IVSS/对讲测试型号）：[`data/dss-v86-device-compat-key.csv`](../data/dss-v86-device-compat-key.csv)
- 对比表原文：[`data/solutions/dss/DSS_Products_Comparison_List_V8.5.0.xlsx`](../data/solutions/dss/DSS_Products_Comparison_List_V8.5.0.xlsx)（zip 里误标成 V8.8 compatibility，正文写 **V8.5.0 / 7016-S2 = V8.5.1**）
- 许可速查：[`data/solutions/dss/DSS_License_Quick_Guide_V8.6.pdf`](../data/solutions/dss/DSS_License_Quick_Guide_V8.6.pdf)
- LCIE ETSI EN 303 645：[`data/solutions/dss/ETSI_EN_303645_DSS_Professional_Express_LCIE_20230525.pdf`](../data/solutions/dss/ETSI_EN_303645_DSS_Professional_Express_LCIE_20230525.pdf)

未入库：1.1 GB `Test SIA&Paxton.rar`、策略 PPT/MP4、IRM 选型表、内部维保/OEM 文档、50 MB 的完整 V8.6 兼容表（只抽了关键行）。

料号仍以 0922 为准。选型 Excel V8.8 **依旧打不开**（IRM）。容量改从 **V8.5 对比表** 引用，不要再用门禁彩页的「500 终端 / 1000 门」当 Pro 软件上限。

---

## 0. 哪些文件能读

zip 里大量「不同文件名、同一 md5」：

| 现象 | 结论 |
|---|---|
| V8.8 选型 xlsx、Pro/Ultimate License Guide PDF、Ecosystem List xlsx **同一 IRM 壳** | 路数表仍读不出 |
| 11 个认证 PDF（ISO 27001/27701、若干 GDPR-2026 文件名）**同一页 LCIE 证书** | **不能**把 ISO 27001 当已入库 |
| 旧版「Selection xlsx」其实是 V8.6 许可 PDF 的副本 | 以 V8.6 Quick Guide 为准 |
| zip 名 `…V8.8.0_EN…compatibility.xlsx` = V8.5 **产品对比表** | 下面容量都来自这张表 |
| 真实兼容表是 **V8.6.0（2025-03-04）** 50 MB xlsx | 已抽门禁/报警/IVSS 行 |

TÜV Rheinland「Protected Privacy IoT」证书（DSS Express/Pro **V7**，DSS4004 / 7016D/DR）有效期到 **2022-02-25，已过期**，不要给设计院当现行 GDPR 证明。

现行可用：Bureau Veritas **LCIE**（Fontenay-aux-Roses）**ETSI EN 303 645 v2.1.1**，证书 CN788980，签发 **2023-05-25**，产品 **DSS Professional / DSS Express**，Security Baseline 3.0。这是软件认证，不是 CNPP 入侵认证。

---

## 1. 四档产品（V8.5 对比表）

| | Express 免费 | Express 许可 | Professional | 一体机 `DSS7116D/DR` + `DSS7016D/DR-S2` |
|---|---|---|---|---|
| 系统 | Windows 软件 | Windows 软件 | Windows 软件 | **Linux** 一体机 |
| 部署 | 单机 | 单机 | 分布式 / 级联 / 热备 / N+M | 分布式 / 热备 / N+M（**不能**当多站点当前站点） |
| 在线用户 | 10 / 共 50 | 同左 | 200 / 共 2 500 | 50 / 共 200 |
| 角色 | 20 | 20 | 500 | 100 |
| 视频（单机） | 64 设备 / 64 路 | 256 / 256 | 1 000 / 2 000 | **500 / 1 000** |
| 视频（多机） | — | — | 10 000 / 20 000 | 2 500 / 5 000 |
| 门禁（多机） | — | — | **1 500 设备 / 3 000 门** | **600 / 1 500** |
| 报警（多机） | — | — | 500 主机 / 5 000 防区 | 320 / 1 600 |
| 人员库 | 5 000 | 5 000 | 300 000 | 100 000 |
| ONVIF | √ | √ | √ | √ |
| 海康协议 | × | × | √ | × |
| **SIA ADM-CID / DCS** | × | × | **√** | **×** |

`DHI-DSS4004-S2` **不在**这张对比列里，不要把 7116/7016 的数字套到 4004 上。

门禁 2025 目录写的「DSS Pro 500 终端 / 1000 门」接近 **一体机单机视频**，不是 Pro 软件门禁上限。出图用上表，并写明来源是 V8.5 对比。

法国 CSU / 值守要收报警协议：**SIA 接入只写在 DSS Professional（Windows）**。Linux 一体机没有 ADM-CID/DCS。事件外推另订 `DSS8PRSIA`（0922 `2.9.02.07.10157`）。

---

## 2. 许可（V8.6 Quick Guide，料号对得上 0922）

底座：

| 外部型号 | 说明 | 料号 |
|---|---|---|
| `DSS8PRVB` | Pro 视频底座，**含 16 路视频**，扩路前提 | `2.9.02.07.10011` |
| `DSS8PRDB` | Pro 门禁底座，**含 16 门** | `2.9.02.07.10012` |
| `DSS8PRV` / `DSS8PRD` | 每路视频 / 每门扩容 | `2.9.02.07.10013` / `10014` |
| `DSS8PRAL` | 每台报警主机，无底座前提 | `2.9.02.07.10016` |
| `DSS8PRVDP` | 每台对讲设备 | `2.9.02.07.10015` |

热备：`DSSHOTSTANDBY` = Rose Replicator Plus（1 主 + 1 备），0922 `2.3.01.01.10131`。

指南里的别名（以 0922 外部型号下单）：

| 指南型号 | 0922 外部型号 |
|---|---|
| `DSS8PRMSITE` | `DSS8PRMS` |
| `DSS8PRDATABASE` | `DSS8PRED` |
| `DSS8PRATT` | `DSS8PRAML` |
| `DSS8PRVEM` | `DSS8PRPML` |

`DSS8PRModbus` / `2.9.02.07.10159` 在指南里有，**0922 没有**，不编库存。

---

## 3. V8.6 兼容（已测型号，不是法国可售清单）

报警（868 固件包名带 `PN_868`）：

- 无线：`ARC3000H`、`ARC3800H` 的 `W2(868)` / `FW2(868)` / `GW2(868)`
- 有线 V3 一族：`DHI-ARC2008C-V3`、`DHI-ARC2016C-V3`、`DHI-ARC9016C-V3`（0922 里 `ARC9016C` 内部是 **V2**，V3 能否订要看法单价目）

门禁测试过：`ASI3213A-W`、`ASC2204B-S`、`ASC3202B`、`ASR1200E`、`ASR2101A` 等，和门禁目录一致。

IVSS：`DHI-IVSS7108-1I` 覆盖 7112/7116/7124 带 `-nI` 的系列。

---

## 4. 设计院怎么用

| 对象 | 带 | 注意 |
|---|---|---|
| Artelia / Oteis | Express 许可 256 路，或小一体机；ETSI 303 645 证书复印件 | 过期 TÜV 2020 证不要带 |
| Ingérop / Egis / Systra | Pro **Windows**（要 SIA/级联/3000 门）或 7016/7116 一体机（Linux，无 SIA 接入） | 一体机 ≠ Pro 软件 |
| CSU / 值守 | Pro + `DSS8PRSIA`；报警主机 868 | 不要承诺一体机讲 SIA ADM-CID |
| B 类安防所 | 对比表 + ETSI 证书 | 仍缺 APSAD/CNPP |

系统需求 PDF 仍是 **V8.4.0（2024-01）**：Pro 服务器建议 Xeon Silver 级；Express 可用 i7 级 Windows 10/11。V8.8 以未解密选型表为准，不要把 V8.4 硬件写成 8.8。

---

## 5. 还缺

1. 未加密的 DSS **V8.8** 选型 / License Guide（本包里的 V8.8 PDF 是 IRM 壳）。  
2. Alarm 选型表仍加密。  
3. EUR 可售、CNPP。  
4. 不要把 zip 里 ISO 27001 文件名当成真证书（字节是 LCIE 那一页）。
