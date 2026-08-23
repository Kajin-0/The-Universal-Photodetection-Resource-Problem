#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
R3 = HERE / "autonomous_temporal_resource_law_prxq_r3.tex"
R4 = HERE / "autonomous_temporal_resource_law_prxq_r4.tex"
BIB = HERE / "references.bib"

errors = []
for p in (R3, R4, BIB):
    if not p.exists():
        errors.append(f"missing required file: {p.name}")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)

r3 = R3.read_text(encoding="utf-8")
r4 = R4.read_text(encoding="utf-8")
bib = BIB.read_text(encoding="utf-8")

# R4 is deliberately a late publication-layer bridge only. Everything before
# the prior-work section, including all theorem statements/proofs/examples, is
# byte-for-byte frozen to R3. The disclosure/data/bibliography tail is also
# unchanged as source text.
prefix_anchor = r"\section{Relation to prior work and scope}"
suffix_anchor = r"\section*{AI Use Disclosure}"
for label, text in [("R3", r3), ("R4", r4)]:
    if prefix_anchor not in text:
        errors.append(f"{label}: prior-work anchor missing")
    if suffix_anchor not in text:
        errors.append(f"{label}: disclosure anchor missing")

if not errors:
    if r3[:r3.index(prefix_anchor)] != r4[:r4.index(prefix_anchor)]:
        errors.append("R4 changed the frozen R3 theorem/proof prefix")
    if r3[r3.index(suffix_anchor):] != r4[r4.index(suffix_anchor):]:
        errors.append("R4 changed the frozen R3 disclosure/data/bibliography tail")

# Title remains exactly the flagship title.
title3 = re.search(r"\\title\{([^}]*)\}", r3)
title4 = re.search(r"\\title\{([^}]*)\}", r4)
if not title3 or not title4 or title3.group(1) != title4.group(1):
    errors.append("R4 changed or lost the R3 title")

required = [
    r"\label{eq:dynamical-bridge}",
    r"V_{\min}(C)=\frac12\Tr C",
    r"\Aact_{\rm ex}^{(2)}=\hbar\nu\,V_{\min}",
    r"\cite{CompanionUnitaryCost2026}",
    "kinematic in definition",
    "not used in any proof above",
    "thermodynamic work",
    "peak or operator-norm coupling",
    "controller bandwidth",
    "ancilla dimension",
    "externally fixed controller spectrum",
]
for marker in required:
    if marker not in r4:
        errors.append(f"R4 missing bridge/scope marker: {marker}")

if "deriving a dynamical implementation cost that produces the kinematic action" in r4:
    errors.append("R4 still calls the solved dynamical implementation question open")

# Companion reference must exist, but the bridge must not import the companion
# proof or change theorem count.
bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.M))
if "CompanionUnitaryCost2026" not in bib_keys:
    errors.append("references.bib missing CompanionUnitaryCost2026")
if r3.count(r"\begin{theorem}") != r4.count(r"\begin{theorem}"):
    errors.append("R4 changed theorem count")
if r3.count(r"\begin{proposition}") != r4.count(r"\begin{proposition}"):
    errors.append("R4 changed proposition count")
if r3.count(r"\begin{corollary}") != r4.count(r"\begin{corollary}"):
    errors.append("R4 changed corollary count")

# Generic publication identity lock remains active.
for token in ["github.com", "Kajin-0", "The-Universal-Photodetection-Resource-Problem", "WP21", "WP32", "WP33"]:
    if token.lower() in r4.lower():
        errors.append(f"R4 contains forbidden publication-facing token {token!r}")

if errors:
    print("PRXQ R4 DYNAMICAL BRIDGE GATE FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("PRXQ R4 DYNAMICAL BRIDGE GATE PASSED")
print(f"title: {title4.group(1)}")
print("R3 theorem/proof prefix frozen; only late scope/discussion bridge added")
