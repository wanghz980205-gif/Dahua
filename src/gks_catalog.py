"""Match GKS document filenames to Dahua external/internal models."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from src.dahua_identity import (
    DEFAULT_CSV,
    IdentityIndex,
    LookupResult,
    format_result,
    load_mappings,
)

MODEL_RE = re.compile(
    r"(?:DH[I]?-)?(?:IPC|HAC|NVR|XVR|HCVR|TPC|VTO|VTH|ITC|SD|ASI|ASC|ASR|ASA|ASM|ASG|ASF|DSS|IVSS|IVS|ARC|ARD|ARM|ARA|ARK|ART)[A-Z0-9\-]+",
    re.I,
)
# Retail wireless short names in GKS MTBF / catalog filenames (Hero, cubes, battery PTZ).
WIRELESS_SHORT_RE = re.compile(
    r"(?:DH-)?(?:F5D|F4C|H3JE|H5A|H3A|H3B|H2A|P3AE|P5AE|P5AS|BP4A|BP3EW|BF4C|WL46A)(?:-[A-Z0-9]+)*",
    re.I,
)


def extract_models(filename: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for rex in (MODEL_RE, WIRELESS_SHORT_RE):
        for m in rex.finditer(filename or ""):
            token = m.group(0).rstrip("-_")
            if token.upper() in {
                "IPC",
                "HAC",
                "NVR",
                "XVR",
                "DSS",
                "IVS",
                "IVSS",
                "ARC",
                "ARD",
                "ARM",
                "ARA",
                "ARK",
                "ART",
            }:
                continue
            key = token.casefold()
            if key in seen:
                continue
            seen.add(key)
            found.append(token)
    return found


def match_filename(index: IdentityIndex, filename: str, limit: int = 20):
    models = extract_models(filename)
    rows = []
    seen: set[tuple[str, str, str]] = set()
    for model in models:
        for row in index.lookup(model, limit=limit).rows:
            key = (row.part_no, row.internal_model, row.external_model)
            if key in seen:
                continue
            seen.add(key)
            rows.append(row)
    return models, rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="从 GKS 文件名反查料号/内部型号/外部型号")
    parser.add_argument("filename")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args(argv)

    index = IdentityIndex(load_mappings(args.csv))
    models, rows = match_filename(index, args.filename, limit=args.limit)
    print(f"文件: {args.filename}")
    print(f"解析到的型号: {', '.join(models) if models else '无'}")
    print()
    if not rows:
        print("映射表中没有命中。可先确认文件名是否含外部型号。")
        return 0
    print(
        format_result(
            LookupResult(query=args.filename, identifier_kind="gks_filename", rows=rows)
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
