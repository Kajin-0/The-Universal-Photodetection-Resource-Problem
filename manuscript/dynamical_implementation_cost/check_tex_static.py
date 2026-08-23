#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
TEX = [
    HERE / "dynamical_rank_boundary_implementation_cost_draft.tex",
    HERE / "dynamical_rank_boundary_implementation_cost_supplement.tex",
]
BIB = HERE / "references.bib"

errors = []
texts = {}
for path in TEX:
    if not path.exists():
        errors.append(f"missing TeX root: {path.name}")
        continue
    texts[path.name] = path.read_text(encoding="utf-8")

if not BIB.exists():
    errors.append("missing references.bib")
    bib = ""
else:
    bib = BIB.read_text(encoding="utf-8")

# Manuscript-facing identity/provenance leakage is forbidden.
forbidden = [
    "GitHub",
    "github.com",
    "Kajin-0",
    "The-Universal-Photodetection-Resource-Problem",
    "WP21", "WP22", "WP23", "WP24", "WP25", "WP26", "WP27",
    "WP28", "WP29", "WP30", "WP31", "WP32", "WP33",
    "work package",
]
for name, text in texts.items():
    lower = text.lower()
    for token in forbidden:
        if token.lower() in lower:
            errors.append(f"{name}: forbidden manuscript-facing token {token!r}")

# Prevent reintroduction of the superseded infinite-dimensional shortcut.
invalid_claims = [
    "ancilla Hamiltonian may be chosen identically zero",
    "H_E=0 is sufficient universally",
    "C_E/p_E",
]
for name, text in texts.items():
    lower = text.lower()
    for claim in invalid_claims:
        if claim.lower() in lower:
            errors.append(f"{name}: superseded energy-shell claim detected: {claim}")

# The repaired construction must remain explicit in the supplement.
supp = texts.get("dynamical_rank_boundary_implementation_cost_supplement.tex", "")
required_supp = [
    r"a_r=\max(0,F_r-E_*)",
    r"b_r=\max(0,E_*-F_r)",
    "spectator curvature can occupy a shell with zero baseline population",
    "No fourth moment",
]
for req in required_supp:
    if req not in supp:
        errors.append(f"supplement missing repaired-proof marker: {req}")

# Check labels and refs within each standalone root.
for name, text in texts.items():
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    dup = sorted({x for x in labels if labels.count(x) > 1})
    if dup:
        errors.append(f"{name}: duplicate labels: {dup}")
    label_set = set(labels)
    refs = set(re.findall(r"\\(?:eqref|ref|autoref)\{([^}]+)\}", text))
    missing = sorted(refs - label_set)
    if missing:
        errors.append(f"{name}: undefined references: {missing}")

# Check citations against the standalone bibliography.
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.M))
for name, text in texts.items():
    cited = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        cited.update(k.strip() for k in group.split(",") if k.strip())
    missing = sorted(cited - bib_keys)
    if missing:
        errors.append(f"{name}: missing bibliography keys: {missing}")

# Headline theorem and scope markers that must not silently disappear.
main = texts.get("dynamical_rank_boundary_implementation_cost_draft.tex", "")
required_main = [
    r"\Vmin(\Cker;D,\rhozero)",
    r"\frac12\Tr\Cker",
    r"\cA_{\rm ex}^{(2)}=\hbar\nu\,\Vmin",
    "not a thermodynamic-work theorem",
    "not an arbitrary full tensor of mixed second derivatives",
]
for req in required_main:
    if req not in main:
        errors.append(f"main missing theorem/scope marker: {req}")

if errors:
    print("STATIC GATE FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("STATIC GATE PASSED")
print(f"checked {len(texts)} TeX roots and {len(bib_keys)} bibliography entries")
