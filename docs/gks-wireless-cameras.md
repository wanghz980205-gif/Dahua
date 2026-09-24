# GKS 无线摄像机资料包 · Wireless Cameras

来源：GKS 签名链接 `Wireless_Cameras.zip`（用户 2026-09-23 贴出）  
体积 **12,080,138,082 字节（约 11.25 GB）**，108 个条目，ZIP64。  
auth_key `1790212682` = **2026-09-24 01:18 UTC 过期**。目录（中央目录）在过期前已拉到；2026-09-24 07:09 再抽 PDF 时 HTTP **403**，所以 **2026-06 英文目录 PDF 没有入库**。

这不是工程固定摄像机 datasheet 全集，而是 **无线/零售摄像机基础包**：选型和目录（Indoor / Outdoor / 4G）、命名表、MTBF、SD 卡兼容、低功耗续航表、竞品（Imou / Ezviz / Tapo / eufy）。11 GB 里绝大部分是 `.ai` / `.psd` 源文件，不需要整包下载。

已落仓库：

- 包内清单：[`data/gks-wireless-zip-inventory.csv`](../data/gks-wireless-zip-inventory.csv)
- 型号↔料号（只写 0922 有的）：[`data/gks-wireless-bom.csv`](../data/gks-wireless-bom.csv)
- 法语注意：[`cctp-module-video-sans-fil.md`](cctp-module-video-sans-fil.md)

未入库：16 MB 的 `Catalog_Dahua Wireless Camera_V1.0_EN_202606.pdf`（链接过期）、32 MB 选型表、全部 `.ai`、竞品 PPT。要目录正文请再贴一次新的签名链接。

---

## 1. 包结构（2026-06）

| 目录 | 用途 |
|---|---|
| `01. Product Selection` | 选型表 `Wireless Sereis Product Selection-202606.xlsx`（文件名 Sereis 是官方拼写） |
| `02. Product Naming Rules` | `2025无线命名规范_1203.xlsx` |
| `03. Catalog` | **2026-06** 拆成室内 / 室外 / 4G 三本 `.ai` + 合订 PDF |
| `04. SD Card Compatibility` | Wi-Fi IPC / Wi-Fi PTZ 卡兼容 |
| `05. MTBF` | 13 份报告，文件名带外部型号 |
| `Others` | 低功耗续航计算、Hero **H3JE**、**BP6X** 社媒图、磷酸铁锂电池 SDS、4G FAQ |
| `03. Competition` | 对 Imou / Ezviz / Tapo / eufy / 萤石 |

最新目录版本是 **2026-06**；更早有 202509 / 202503 / 202409 leaflet。

---

## 2. 和 0922 怎么对

无线摄像头 **没有单独料号段**。Wi-Fi / 4G 枪机、Hero、电池卡片走 **`1.0.01.04`（IPC）**；电池云台 P3AE/P5AE、部分 Wi-Fi PT 走 **`1.0.01.07`（SD 球机）**。

从 MTBF 文件名和 EUR 内部型号反推的后缀：

| 标记 | 含义（按表内证据） |
|---|---|
| **SW** | Wi-Fi |
| **SAW** | Wi-Fi 子弹机/半球常见搭配，多与 **IL** 全彩补光一起出现 |
| **4G** | 蜂窝；内部型号常带模组 `NL668` / `EAU` |
| **PV** | 声光警戒 |
| **IL** | 双光/全彩 |
| **SP** | 4G 枪机系列名（MTBF 的 HFW2441DG-4G-SP） |
| **EUR** | 欧洲订货位，内部型号末尾 |

短名（零售）：`DH-H3JE`、`DH-F5D-PV`、`DH-P3AE-PV`、`DH-BP4A-4G`。0922 外部型号就是短名，内部型号仍是 `DH-IPC-…` 或 `DH-SD-…`。

查询：

```bash
python3 -m src.dahua_identity lookup DH-H3JE
python3 -m src.dahua_identity lookup DH-P3AE-PV
python3 -m src.gks_catalog 20250121_DH3.RD009931_IPC_DH-F5D-PV_MTBF Report.pdf
```

---

## 3. 三条产品线（对齐 2026-06 目录三分法）

### 室内 Indoor（Hero / 卡片）

| 外部型号 | 内部型号（EUR） | 料号 |
|---|---|---|
| `DH-H3JE` | `DH-IPC-H3JEP-0280B-EUR` | `1.0.01.04.48317-9901` |
| `DH-H3A` | `DH-IPC-H3AP-0360B-EUR` | `1.0.01.04.43549-9001` |
| `DH-H5A` | `DH-IPC-H5ASP-0280B-EUR` | `1.0.01.04.48883-9901` |
| `DH-F5D-PV` | `DH-IPC-F5DP-PV-0280B-EUR` | `1.0.01.04.45447-9001` |
| `DH-F5D-IL` | `DH-IPC-F5DP-IL-0360B-EUR` | `1.0.01.04.45916-9001` |

GKS 另有 **BP6X** 社媒物料，**0922 没有 BP6X**，不能编料号。

### 室外 Outdoor（Wi-Fi 固定 + 云台）

| 外部型号 | 料号（优先 EUR） |
|---|---|
| `DH-IPC-HDW1339DA-SW-PV` | `1.0.01.04.45398-9001` |
| `DH-IPC-HDW1539DA-SW-PV` | `1.0.01.04.45395-9001` |
| `DH-IPC-HFW1339DTK1-SW-PV` | `1.0.01.04.45380-9001` |
| `DH-IPC-HFW1339DTK1-SAW-IL` | `1.0.01.04.45376-9002` |
| `DH-P5AS-PV`（电池枪） | `1.0.01.04.45708-9001` |
| `DH-P3AE-PV` / `DH-P5AE-PV`（电池云台） | `1.0.01.07.15562-9002` / `1.0.01.07.15563-9002` |

路灯款 `DH-IPC-WL46A` 在 0922：`1.0.01.04.40140`（内部 `WL46AP-0280B`）。

### 4G

| 外部型号 | 料号 |
|---|---|
| `DH-IPC-HFW2441DG-4G-SP-B-MAX` | `1.0.01.04.45462-9001`（EUR） |
| `DH-BP4A-4G` | `1.0.01.04.46128` |
| `DH-BP3EW-4GP` | `1.0.01.04.47885-9001` |
| `DH-BF4CP-4G-XL` | `1.0.01.04.46139` |
| `DH-P3AE-PV-4G` | `1.0.01.07.15910` |

4G 内部型号常带 `NL668EAU`：模组 + 欧洲频段，不是另一台摄像机。

---

## 4. 法国怎么用（别拿错场合）

这包是 **零售 / 中小安装商 / 经销商 BE（海报 D 类）** 弹药，不是地铁 CCTP。

| 对象 | 带 | 不带 |
|---|---|---|
| 代理商、D 类经销商 BE、中小安装 | Hero、Wi-Fi 枪球、4G 电池、DMSS | 车载 MXVR、DSS 1000 门 |
| Artelia / Oteis 小楼宇临时点 | 可提 Wi-Fi 作为过渡，须写清不替代有线 62676 | 把电池枪写成车站主系统 |
| Egis / Systra / Ingérop 大项目 | 不用这包 | 无线电池、Hero 室内机 |
| Assystem 工业 | 除非临时施工监控 | 4G 消费级 |

有包内「低功耗续航计算」Excel，链接过期没抽到；电池方案出图前要那张表，不要口头承诺续航。

锂电池 SDS 在包里（磷酸铁锂圆柱），运输/安装商需要时再下。

---

## 5. 还缺

1. **再贴一次未过期的签名链接**，抽 2026-06 目录 PDF + 命名表 + 续航表。  
2. 法国/EUR 可售过滤（BOM 里标了 EUR 的才能当法国订货候选）。  
3. BP6X 的 0922 行（现在没有）。  
4. DSS / Alarm 包仍然优先于再下无线竞品 PPT。
