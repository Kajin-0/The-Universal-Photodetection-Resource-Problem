#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
TEX = [
    HERE / "dynamical_rank_boundary_implementation_cost_d2.tex",
    HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.tex",
]
BIB = HERE / "references.bib"

errors = []
texts = {}
for path in TEX:
    if not path.exists():
        errors.append(f"missing generated TeX root: {path.name}")
        continue
    texts[path.name] = path.read_text(encoding="utf-8")

bib = BIB.read_text(encoding="utf-8") if BIB.exists() else ""
if not bib:
    errors.append("missing references.bib")

forbidden = [
    "GitHub", "github.com", "Kajin-0", "The-Universal-Photodetection-Resource-Problem",
    "WP21", "WP22", "WP23", "WP24", "WP25", "WP26", "WP27", "WP28", "WP29",
    "WP30", "WP31", "WP32", "WP33", "work package",
]
invalid_claims = [
    "ancilla Hamiltonian may be chosen identically zero",
    "H_E=0 is sufficient universally",
    "C_E/p_E",
]
for name, text in texts.items():
    lower = text.lower()
    for token in forbidden:
        if token.lower() in lower:
            errors.append(f"{name}: forbidden manuscript-facing token {token!r}")
    for claim in invalid_claims:
        if claim.lower() in lower:
            errors.append(f"{name}: superseded energy-shell claim detected: {claim}")

supp = texts.get("dynamical_rank_boundary_implementation_cost_supplement_d2.tex", "")
for req in [
    r"a_r=\max(0,F_r-E_*)",
    r"b_r=\max(0,E_*-F_r)",
    "spectator curvature can occupy a shell with zero baseline population",
    "No fourth moment",
    "bounded spectral truncations of $K$",
    r"\section{Trace-norm second-order control of the direct-sum family}",
]:
    if req not in supp:
        errors.append(f"supplement missing audited proof marker: {req}")

main = texts.get("dynamical_rank_boundary_implementation_cost_d2.tex", "")
for req in [
    r"\Vmin(\Cker;D,\rhozero)",
    r"\frac12\Tr\Cker",
    r"\cA_{\rm ex}^{(2)}=\hbar\nu\,\Vmin",
    "not a thermodynamic-work theorem",
    "not an arbitrary full tensor of mixed second derivatives",
    "trace-norm $C^2$ at the origin",
    "finite second moments",
    "strongly continuous blockwise unitary family",
]:
    if req not in main:
        errors.append(f"main missing audited theorem/scope marker: {req}")

for name, text in texts.items():
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    dup = sorted({x for x in labels if labels.count(x) > 1})
    if dup:
        errors.append(f"{name}: duplicate labels: {dup}")
    refs = set(re.findall(r"\\(?:eqref|ref|autoref)\{([^}]+)\}", text))
    missing_refs = sorted(refs - set(labels))
    if missing_refs:
        errors.append(f"{name}: undefined references: {missing_refs}")

bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.M))
for name, text in texts.items():
    cited = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        cited.update(x.strip() for x in group.split(",") if x.strip())
    missing = sorted(cited - bib_keys)
    if missing:
        errors.append(f"{name}: missing bibliography keys: {missing}")

if errors:
    print("D2 STATIC GATE FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("D2 STATIC GATE PASSED")
print(f"checked {len(texts)} generated TeX roots and {len(bib_keys)} bibliography entries")
