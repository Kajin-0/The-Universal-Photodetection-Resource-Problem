#!/usr/bin/env python3
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
logs = [
    HERE / "dynamical_rank_boundary_implementation_cost_d2.log",
    HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.log",
]

fatal_markers = [
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
        errors.append(f"missing build log: {path.name}")
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for marker in fatal_markers:
        if marker in text:
            errors.append(f"{path.name}: found disallowed final-pass warning: {marker}")

if errors:
    print("BUILD LOG GATE FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("BUILD LOG GATE PASSED")
print("no overfull boxes, PDF-string math warnings, or unresolved final references/citations")
