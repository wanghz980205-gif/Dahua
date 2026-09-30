# 大华 GKS 目录 7291

来源：https://gks1.dahuasecurity.com/zh/parcel?category_id=7291

## 这个链接是什么

这不是公开产品官网，而是大华 **GKS（Global Knowledge System，全球知识库）** 里的一个资料目录。

- 旧地址 `/zh/parcel?category_id=7291` 会跳到 `/zh/list/7291`
- 这里的 **parcel = 资料包**（规格书、手册、彩页的打包下载），不是物流包裹
- 目录里列的是 **文件/文件夹**（名称、大小、版本、上传者），型号写在文件名或文件夹名里

`gks1.dahuasecurity.com` 在本环境无法解析（DNS NXDOMAIN）。公开入口是 https://gks.dahuasecurity.com/ ，打开 7291 会进登录页，接口返回 401。没有账号就拿不到「我们公司」在该目录下的授权产品清单。

## 和料号 / 型号的关系

GKS 文件名通常带 **外部型号**，例如：

`Datasheet_DH-IPC-HDW8441X-3D_EN.pdf`

要对库存或下单，还得再用《映射关系0922》落到内部型号和料号：

```
GKS 文件名里的型号  →  外部型号  →  内部型号（镜头/区域）  →  料号
```

把 GKS 导出的文件名丢给查询工具即可匹配：

```bash
python3 -m src.dahua_identity lookup DH-IPC-HDW8441X-3D
python3 -m src.gks_catalog "Datasheet_DH-IPC-HDW8441X-3D_EN.pdf"
```

## 登录后建议导出什么

在 GKS 打开 category 7291，把该目录（含子目录）的 **文件夹名 + 文件名** 导出成文本或 CSV，放到 `data/gks-7291-export.csv`（列：`path,name`）。有清单后可以把「公司在售产品」和 0922 映射表对齐。
