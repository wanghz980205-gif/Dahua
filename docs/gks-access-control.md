# GKS 门禁资料包 · Access Control & Time Attendance

来源：GKS 签名链接 `Access_Control___Time_Attendance.zip`（2026-09-23）  
链接有效：HTTP 200，`accept-ranges: bytes`，体积 **1,524,590,905 字节（约 1.45 GB）**，94 个条目。  
auth_key 时间戳 `1790209562` = 2026-09-24 00:26 UTC。

这不是单品 datasheet 全集，而是 **门禁基础资料包**：目录、方案海报、功能清单（Excel 被 DRM 锁）、MTBF、竞品。产品弹药够写 CCTP 架构段；法国可售过滤仍缺 EUR 价目。

整包未入库（太大，且大半是 .ai / 视频）。已抽：

- 目录 PDF：[`data/solutions/access-control/Catalog_Dahua Access Control_V1.0_EN_20251014.pdf`](../data/solutions/access-control/Catalog_Dahua%20Access%20Control_V1.0_EN_20251014.pdf)（73 页，2025-10-14；门禁 34–58 页，报警 59–63 页）
- 型号↔料号：[`data/gks-access-bom.csv`](../data/gks-access-bom.csv)
- 包内文件清单：[`data/gks-access-zip-inventory.csv`](../data/gks-access-zip-inventory.csv)
- 法语 CCTP 可抄段：[`cctp-module-acces.md`](cctp-module-acces.md)

未抽：数百 MB 的 .ai 海报源文件、竞品对比视频、测温方案（疫情期，法国设计院现在一般不写）。

Excel 功能清单 / 命名规则 PPT 是 **Microsoft IRM（EncryptedPackage）**，没有密钥读不了。型号以 2025 目录 + 0922 为准。

---

## 1. 料号段

| 前缀 | 产品 |
|---|---|
| `1.0.01.25` | 门禁/考勤：ASI 一体机、ASC 控制器、ASR 读头、ASA 考勤、ASG 闸机、ASM 发卡器 |
| `1.2.01.27` | 电锁及支架（ASF 磁力锁/电插锁/电锁口） |
| `1.0.01.15` | 对讲 VTO/VTH（同本目录前半，楼宇门口机可和门禁联动） |

0922 里 `1.0.01.25` 约 298 条。查询：

```bash
python3 -m src.dahua_identity lookup ASI6213J-MW
python3 -m src.dahua_identity lookup 1.0.01.25.11413-9001
python3 -m src.gks_catalog Datasheet_DHI-ASC2204C-S_EN.pdf
```

---

## 2. 命名（从目录型号反推，PPT 打不开）

| 前缀 | 角色 | 目录例子 |
|---|---|---|
| **ASI** | Access Standalone / 人脸或刷卡一体机 | ASI6213J-MW、ASI7213X、ASI2212H-W |
| **ASC** | Access Controller / 多门控制器 | ASC2204C-S、ASC3202B |
| **ASR** | Access Reader / 读头 | ASR2101A-ME、ASR2102A、ASR1200E |
| **ASA** | Attendance / 考勤机 | ASA1222GL-D、ASA3213GL-MW |
| **ASG** | 闸机：G 三辊、Y 拍打、B 摆闸 | ASGG520T、ASGY510C-L、ASGB810X-L |
| **ASF** | 锁具 | ASF280A（280 kg 磁力锁） |
| **ASM** | 发卡/指纹登记器 | ASM100、ASM101A、ASM202 |

后缀常见：

- **无 / `-S`**：单向（1-way）
- **`-D`**：双向或 ID（125 kHz Unique），看系列：控制器 `-D` = 双向；读头 `-D` = ID 卡
- **`-W` / `-MW`**：Wi-Fi / Mifare+Wi-Fi
- **`-ME`**：IC+ID 双频
- **IC = 13.56 MHz Mifare Classic**；**ID = 125 kHz Unique**

法国 CCTP 经常写 **MIFARE DESFire EV2/EV3**。本目录几乎全是 **Mifare Classic**，0922 里 DESFire 只有卡片料号 `MW-DESFire-4-3-2`。出图前必须和产品确认有没有 DESFire 读头/固件，**不能把 Classic 写成 DESFire**。

---

## 3. 三条方案（海报 2022 + 目录 2025）

### A. 单门一体机（SMB / 零售）

`ASI3214A-W` + 室内机 `VTH5421EW-H` + DMSS。无额外平台，可对讲访客。  
适合 Artelia / Oteis 楼宇里「一门一机」。

### B. 约 40 门 Insider（无服务器）

主/从 `ASC3202B` + `ASR1200E` / `ASR2101A-ME` / `ASR2102A`。Web 管理，PoE 给锁供电。SMB，不配 DSS。

### C. 最多 64 门 SmartPSS Lite / 最多 1000 门 DSS Pro

`ASC2204C-S` + 读头 + 可选人脸 `ASI6214J-MFW`。SmartPSS Lite：**最多 64 台设备**，免费，Windows。DSS Pro：**500 终端 / 1000 门**，视频联动、消防联动。  
Ingérop / Egis 大项目走 DSS；中小楼宇走 SmartPSS Lite。

考勤：`ASA1222GL(-D)` / `ASA3223A-W`（0922 无 ASA3223A-W）+ SmartPSS Lite。

---

## 4. 设计院该带哪套

| 对象 | 带 | 不带 |
|---|---|---|
| Artelia / Oteis 楼宇 | 方案 A 或 C（64 门）+ 法语规格；IC 读头 IP66 | 闸机整册、测温额头机 |
| Egis / Systra 车站 | 方案 C + DSS + 闸机 ASGB/ASGY；防尾随 | 零售 2.4 寸考勤机 |
| Ingérop 场站 | 门禁+视频联动 DSS；客流仍用摄像机不是闸机 | 校车 PPT |
| Assystem 工业 | 周界锁 + IP66 读头 + 角色/胁迫码；人脸要 RGPD 说明 | 测温系列 |

人脸终端目录写 **GDPR 合规、防照片/视频攻击**。法国仍须单独做 CNIL 用途说明，不能只抄彩页。

---

## 5. 同包里的报警（完整入侵见 DSS/Alarm 选型包）

目录 59–63 页有有线报警：`ARC3008C`（EN50131 Grade 2）、`ARC2008C/2016C`、`ARC9016C`，探测器 `ARD1233` 等。0922 有 `ARC3008C` / `ARC2016C` / `ARC9016C`，**没有 `ARC2008C` 行**。法国无线必须 868 MHz，见 [`gks-dss-alarm.md`](gks-dss-alarm.md)。APSAD 认证表仍缺。

---

## 6. 还缺

1. 法国/EUR 可售清单（目录型号 ≠ 法国能订）
2. DESFire / OSDP 实际可售读头
3. 未加密的功能清单，或单品法语 datasheet
4. 未加密的 DSS V8.8 / Alarm 选型表、EUR 可售、CNPP
