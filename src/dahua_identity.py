"""Dahua identifier mapping learned from 映射关系0922.xlsx."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = ROOT / "data" / "mapping-0922.csv"

PART_NO_RE = re.compile(
    r"^\d+\.\d+\.\d+\.\d+(?:\.\d+)?(?:[-#][A-Za-z0-9]+)?$"
)
LENS_TOKEN_RE = re.compile(
    r"^(?:0?280B|0360B|0400B|0600B|0800B|1200B|1600B|0250B|0200B|0210B|"
    r"27135|2712F?|3711|0735|0856|1236|2812|0832)$",
    re.I,
)
REGION_TOKEN_RE = re.compile(
    r"^(?:EUR|US|UK|AU|CN|IN|RU|JP|DE|AL|DAE|DIP)$",
    re.I,
)
POWER_TOKEN_RE = re.compile(
    r"^(?:AC220V|DC12AC24V|DC12V|AC24V|DC)$",
    re.I,
)

PART_FAMILY = {
    "1.0.01.04": "IPC 网络摄像机",
    "1.0.01.23": "NVR 网络录像机",
    "1.0.01.01": "XVR/HCVR 同轴录像机",
    "1.0.01.12": "HAC 同轴摄像机",
    "1.0.01.07": "SD 球机",
    "1.0.01.15": "VTO/VTH 对讲",
    "1.0.01.34": "TPC 热成像",
    "1.0.01.09": "ITC 智能交通",
    "1.0.01.20": "其它成品",
    "1.0.99.44": "PFA/PFB 支架配件",
    "1.4.01.07": "Discount 折扣虚项",
}


@dataclass(frozen=True)
class MappingRow:
    part_no: str
    internal_model: str
    external_model: str

    @property
    def is_product_row(self) -> bool:
        if not self.part_no:
            return False
        if self.external_model in {"Discount", "/", ""} and not self.internal_model:
            return False
        return bool(self.internal_model or self.external_model)


@dataclass
class LookupResult:
    query: str
    identifier_kind: str
    rows: list[MappingRow] = field(default_factory=list)


def classify_identifier(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return "empty"
    if PART_NO_RE.match(text):
        return "part_no"
    tokens = [t for t in re.split(r"[-/]", text) if t]
    extra = any(
        LENS_TOKEN_RE.match(t) or REGION_TOKEN_RE.match(t) or POWER_TOKEN_RE.match(t)
        for t in tokens
    )
    if extra:
        return "internal_model"
    if re.search(r"\b(IPC|HAC|NVR|XVR|HCVR|TPC|VTO|VTH|SD)\b", text, re.I):
        return "external_or_internal_model"
    return "model_or_other"


def part_family(part_no: str) -> str:
    m = re.match(r"^(\d+\.\d+\.\d+\.\d+)", part_no or "")
    if not m:
        return "未知料号段"
    return PART_FAMILY.get(m.group(1), f"料号段 {m.group(1)}")


def load_mappings(csv_path: Path | None = None) -> list[MappingRow]:
    path = csv_path or DEFAULT_CSV
    rows: list[MappingRow] = []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for rec in reader:
            rows.append(
                MappingRow(
                    part_no=(rec.get("part_no") or "").strip(),
                    internal_model=(rec.get("internal_model") or "").strip(),
                    external_model=(rec.get("external_model") or "").strip(),
                )
            )
    return rows


class IdentityIndex:
    def __init__(self, rows: Iterable[MappingRow]):
        self.rows = list(rows)
        self.by_part: dict[str, list[MappingRow]] = defaultdict(list)
        self.by_internal: dict[str, list[MappingRow]] = defaultdict(list)
        self.by_external: dict[str, list[MappingRow]] = defaultdict(list)
        self.by_internal_cf: dict[str, list[MappingRow]] = defaultdict(list)
        self.by_external_cf: dict[str, list[MappingRow]] = defaultdict(list)
        for row in self.rows:
            if row.part_no:
                self.by_part[row.part_no].append(row)
            if row.internal_model:
                self.by_internal[row.internal_model].append(row)
                self.by_internal_cf[row.internal_model.casefold()].append(row)
            if row.external_model:
                self.by_external[row.external_model].append(row)
                self.by_external_cf[row.external_model.casefold()].append(row)

    def lookup(self, query: str, limit: int = 50) -> LookupResult:
        q = (query or "").strip()
        kind = classify_identifier(q)
        found: list[MappingRow] = []
        seen: set[tuple[str, str, str]] = set()

        def add(items: Iterable[MappingRow]) -> None:
            for row in items:
                key = (row.part_no, row.internal_model, row.external_model)
                if key in seen:
                    continue
                seen.add(key)
                found.append(row)

        add(self.by_part.get(q, []))
        add(self.by_internal.get(q, []))
        add(self.by_external.get(q, []))
        ql = q.casefold()
        add(self.by_internal_cf.get(ql, []))
        add(self.by_external_cf.get(ql, []))

        if not found:
            for row in self.rows:
                if (
                    q in row.part_no
                    or q.casefold() in row.internal_model.casefold()
                    or q.casefold() in row.external_model.casefold()
                ):
                    add([row])
                if len(found) >= limit:
                    break
        return LookupResult(query=q, identifier_kind=kind, rows=found[:limit])


def format_result(result: LookupResult) -> str:
    lines = [
        f"查询: {result.query}",
        f"识别为: {result.identifier_kind}",
        f"命中: {len(result.rows)} 条",
        "",
    ]
    if not result.rows:
        lines.append("没有匹配。可试料号、内部型号、外部型号或其中一段。")
        return "\n".join(lines)
    for i, row in enumerate(result.rows, 1):
        lines.append(f"{i}. 料号          {row.part_no or '—'}")
        lines.append(f"   内部型号      {row.internal_model or '—'}")
        lines.append(f"   外部型号      {row.external_model or '—'}")
        lines.append(f"   料号类别      {part_family(row.part_no)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="查询大华料号 / 内部型号 / 外部型号映射")
    sub = parser.add_subparsers(dest="cmd", required=True)
    look = sub.add_parser("lookup", help="按料号、内部型号或外部型号查询")
    look.add_argument("query")
    look.add_argument("--limit", type=int, default=50)
    look.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    stats = sub.add_parser("stats", help="打印映射表规模")
    stats.add_argument("--csv", type=Path, default=DEFAULT_CSV)

    args = parser.parse_args(argv)
    rows = load_mappings(args.csv)
    if args.cmd == "stats":
        parts = {r.part_no for r in rows if r.part_no}
        internals = {r.internal_model for r in rows if r.internal_model}
        externals = {r.external_model for r in rows if r.external_model}
        print(f"rows={len(rows)} parts={len(parts)} internals={len(internals)} externals={len(externals)}")
        return 0

    index = IdentityIndex(rows)
    print(format_result(index.lookup(args.query, limit=args.limit)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
