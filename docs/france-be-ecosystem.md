# 法国安全生态与设计院合作策略（官方图）

来源：Dahua Technology France 一页纸  
《Le rôle de Dahua dans l'écosystème de la sécurité en France et stratégie de collaboration avec les bureaux d'études》

这张图是 **项目生态**，不是分销价目。代理商不在图①里，但图④D 的「经销商售前设计院」会接上零售渠道。

---

## ① 项目链条（已掌握，图更完整）

```
甲方 MOA（公共/私营）
  → 设计院 / AMO（咨询、出 CCTP）
    → 集成商 / 安装商（施工）
      → 运营方 Exploitant（CSU 监控中心、维护）
```

甲方定需求预算；设计院写 CCTP、评供应商；集成商深化与安装；CSU 运维。经验和回流贯穿全程。

比口头渠道模型多出来的：**AMO** 和 **Exploitant/CSU**。厂商既要进设计院，也要让运营方愿意用我们的平台。

## ② 厂商在图里的五块产品（部分未学透）

图上写的可写进 CCTP 的能力：

| 模块 | 现状 |
|---|---|
| Vidéoprotection 视频保护 | 有 0922 + 零售 IPC/NVR；**无线/4G/电池**见 [`gks-wireless-cameras.md`](gks-wireless-cameras.md)（目录 PDF 因链接过期未入库）。工程有线 CCTP 段仍缺 |
| Contrôle d'accès 门禁 | 已学 GKS 基础包 + 2025 目录 + 0922 `1.0.01.25`。CCTP 草稿 [`cctp-module-acces.md`](cctp-module-acces.md)。缺法国可售过滤和 DESFire |
| Anti-intrusion 入侵报警 | 目录末尾有 ARC/ARD 彩页，**不算学完**；等 Alarm zip |
| IA et analyse 智能分析 | 车载 DSM/ADAS/客流有；场站/城市 AI 未做成设计院材料 |
| Plateforme et stockage 平台与存储 | DSS Pro 在门禁目录里有容量（500 终端/1000 门），仍缺 DSS 资料包 |

设计院要的是这五块的 **法语功能描述**，不是车载 27 页 PPT。

## ③ 合作五步（已理解）

1. 接触与启动（介绍、资料包、摸清设计院习惯）  
2. 需求分析（技术文档、方案讨论、分析支持）  
3. 构思与 CCTP（方案、协助写 CCTP、参考资料）  
4. 找供应商（答疑、演示/POC、带看现场与案例）  
5. 施工与运维（给集成商培训、售后）  

我们是陪设计院走完项目，不是卖一单设备。

## ④ 四类要拜访的角色（这是新知识）

先前只深挖了 Ingérop/Assystem = 基本属于 **A**。图上还有 B/C/D，数量更大。

| 类型 | 是谁 | 法国大约 | 建议列入 Dahua 名单 | 关键职位 |
|---|---|---|---|---|
| **A** 大型工程集团 | Ingérop 这一档 | 30–50 | 15–20 | 业务总监、安防负责人、**弱电 CF**、数字/智慧城市 |
| **B** 安防专业设计院/AMO | 只做 sûreté | 80–150 | 30–50 | 老板、安防顾问、技术专家 |
| **C** 采购中心 / 公共市场 | UGAP 等 | 20–40 | 15–25 | AMO/项目负责人、协调、项目经理 |
| **D** 经销商售前 / 中小型设计院 | 代理商自有 BE | 300–600 | 80–120 | 老板、项目经理、技术顾问、销售 |

A 锁大项目 CCTP；B 锁安防专篇；C 锁框架与公共采购；D 把零售优势变成「代理商出图」。四条要并行，不能只跑 Ingérop。

## ⑤ 切入点（已掌握）

大项目（城市、地铁、CSU、集体）、协助写 CCTP、论证容量与运维、联合培训、长期伙伴（信任 + 本地支持）。

## ⑥ 图上点名的目标（除 Ingérop 外尚未逐家学）

**A 大型工程集团**  
Ingérop，Egis，Artelia，Setec，Systra，Oteis（图为 teïs/oteis）  
公开一页卡已起稿：[`target-cards-grands-groupes.md`](target-cards-grands-groupes.md)。学习顺序：[`how-we-learn.md`](how-we-learn.md)。

**B 安防专业设计院**  
Tandem Sécurité，E-Conex，Galpha，Svitec，LET Consulting，Sûreté Consulting

**C 采购中心 / 公共市场**  
UGAP，CANUT，SRC Solution，SDCT，ORIA，SETICS，Althing，BPF（及图中另一公共采购标识）  
UGAP 电子安防续框为预告程序 **26U021**（预计 2027-06 发布、2028-03 开售），不是 2027 立刻投标。现框履约仍走已入围集成商。

**D 区域设计院**  
Alternet，Amocom，SOC Ingénierie，ProConsulting，Ambre，Protek AMO

口头提到的 **Assystem 不在这张摘录图上**，仍按大型工程/工业线单独跟，不要和 A 类交通工程集团混用同一套材料。

## ⑦ 价值主张（已掌握）

可靠产品与性能；符合法国/欧洲规范；开放可互操作平台；AI；法国本地团队；长期信任。

---

## 还要不要学别的

**不必再学**：项目四角色、CCTP 五步、Ingérop 为什么重要、0922 怎么把图上的「型号」落到料号。

**还要学（按对出图的影响）**

1. **图② 门禁、入侵、平台**：没有这三块，设计院只能把我们写成「摄像机供应商」。  
2. **⑥ 除 Ingérop 外的名单**：Egis / Artelia / Setec / Systra 各做什么、弱电接口在哪；UGAP 怎么进框架。  
3. **B 类安防所**：他们写的是纯安防 CCTP，比 Ingérop 更认 APSAD/CNPP。  
4. **C 类 UGAP 等**：公共采购路径，和代理商进货不是同一套动作。  
5. **法语 CCTP 模块 + EUR 可售清单**：图③第 3 步的实际弹药。

有 1 + 5，这张图就能从「战略海报」变成可执行的拜访包。
