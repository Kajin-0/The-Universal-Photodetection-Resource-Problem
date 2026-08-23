#!/usr/bin/env python3
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
logs = [
    HERE / "dynamical_rank_boundary_implementation_cost_pra_r1.log",
    HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.log",
]

forbidden = [
    "Overfull \\hbox",
    "Overfull \\vbox",
    "Token not allowed in a PDF string",
    "There were undefined references",
    "There were undefined citations",
    "multiply defined",
]

errors = []
for path in logs:
    if not path.exists():
        errors.append(f"missing final build log: {path.name}")
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for marker in forbidden:
        if marker in text:
            errors.append(f"{path.name}: disallowed final-pass warning: {marker}")

if errors:
    print("PRA R1 BUILD LOG GATE FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("PRA R1 BUILD LOG GATE PASSED")
print("no overfull boxes, PDF-string math warnings, unresolved final references/citations, or duplicate-label warnings")
