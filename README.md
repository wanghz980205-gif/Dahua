# Dahua September Business

大华九月业务仓库。产品标识以《映射关系0922》为准。

## 四个标识

| 名称 | 表字段 | 作用 |
|---|---|---|
| 料号 | Part No. | 库存 SKU，ERP 一物一码 |
| 内部型号 | Internal Model | 订货 SKU，含镜头/区域/电源 |
| 外部型号 | External Model | 对客户、规格书的产品族型号 |
| SKU | 无独立列 | 库存用料号，下单用内部型号 |

详细规则见 [`docs/映射关系0922分析.md`](docs/映射关系0922分析.md)。  
GKS 产品资料目录见 [`docs/gks-category-7291.md`](docs/gks-category-7291.md)（需登录，本环境拿不到清单）。

2026 交通车载方案见 [`docs/2026-DHIA-Transportation.md`](docs/2026-DHIA-Transportation.md)，BOM 对照 [`data/dhia-transportation-bom.csv`](data/dhia-transportation-bom.csv)。

法国分公司与设计院：[`docs/dahua-france-gtm.md`](docs/dahua-france-gtm.md)、[`docs/insight-ingerop-assystem.md`](docs/insight-ingerop-assystem.md)。

## 查询

```bash
python3 -m src.dahua_identity lookup 1.0.01.04.31634-0016
python3 -m src.dahua_identity lookup DH-IPC-HDW8441X-3D
python3 -m src.gks_catalog Datasheet_DH-IPC-HDW8441X-3D_EN.pdf
python3 -m src.dahua_identity stats
```

数据文件：

- `data/映射关系0922.xlsx` — 原始表
- `data/mapping-0922.csv` — 去重后的查询表

```bash
python3 -m unittest tests/test_dahua_identity.py
```
