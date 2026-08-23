#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
MAIN = HERE / "dynamical_rank_boundary_implementation_cost_pra_r1.tex"
SUPP = HERE / "dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex"
SUPP_D2 = HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.tex"
D2 = HERE / "dynamical_rank_boundary_implementation_cost_d2.tex"
BIB = HERE / "references.bib"

errors = []
for p in (MAIN, SUPP, SUPP_D2, D2, BIB):
    if not p.exists():
        errors.append(f"missing required file: {p.name}")

if errors:
    for e in errors:
        print(e)
    sys.exit(1)

main = MAIN.read_text(encoding="utf-8")
supp = SUPP.read_text(encoding="utf-8")
supp_d2 = SUPP_D2.read_text(encoding="utf-8")
d2 = D2.read_text(encoding="utf-8")
bib = BIB.read_text(encoding="utf-8")

# Standalone/public identity lock. Match actual project/provenance identifiers,
# not generic substrings such as "repo" that occur inside ordinary words
# (for example, "Reports" in bibliography journal titles).
forbidden = [
    "GitHub", "github.com", "Kajin-0", "The-Universal-Photodetection-Resource-Problem",
    "WP21", "WP22", "WP23", "WP24", "WP25", "WP26", "WP27", "WP28", "WP29",
    "WP30", "WP31", "WP32", "WP33", "work package",
]
for name, text in [(MAIN.name, main), (SUPP.name, supp), (BIB.name, bib)]:
    lower = text.lower()
    for token in forbidden:
        if token.lower() in lower:
            errors.append(f"{name}: forbidden publication-facing token {token!r}")

# Publication titles should use the PRA-facing curvature language consistently.
title_match = re.search(r"\\title\{([^}]*)\}", main)
if not title_match:
    errors.append("PRA R1 title not found")
else:
    title = title_match.group(1)
    if "jet" in title.lower():
        errors.append("PRA R1 title still contains 'jet'")
    required_title_terms = ["minimum", "dynamical", "rank-changing", "curvature"]
    for term in required_title_terms:
        if term not in title.lower():
            errors.append(f"PRA R1 title missing term {term!r}")

supp_title_match = re.search(r"\\title\{([^}]*)\}", supp)
if not supp_title_match:
    errors.append("PRA R1 supplement title not found")
else:
    supp_title = supp_title_match.group(1)
    expected_supp_title = (
        "Supplemental Material for ``Exact minimum dynamical cost of "
        "prescribed rank-changing quantum-state curvature''"
    )
    if supp_title != expected_supp_title:
        errors.append("PRA R1 supplement title does not match main publication title")
    if "jet" in supp_title.lower():
        errors.append("PRA R1 supplement title still contains 'jet'")

# Abstract must state the exact result and principal physical scope.
abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", main, flags=re.S)
if not abstract_match:
    errors.append("abstract not found")
else:
    abstract = abstract_match.group(1)
    for marker in [
        r"V_{\min}=\tfrac12\operatorname{Tr}C",
        "exact total-energy conservation",
        "separable infinite-dimensional",
        r"\hbar\nu V_{\min}",
    ]:
        if marker not in abstract:
            errors.append(f"abstract missing scope/result marker: {marker}")

    thermodynamic_disclaimers = [
        "not a thermodynamic-work bound",
        "neither a thermodynamic-work bound",
    ]
    if not any(marker in abstract for marker in thermodynamic_disclaimers):
        errors.append(
            "abstract missing thermodynamic-work disclaimer "
            "('not a thermodynamic-work bound' or 'neither a thermodynamic-work bound')"
        )

# Publication-facing prior-art separation should explicitly distinguish the
# prescribed state-family kernel Hessian from Bures-metric Riemannian curvature.
for marker in [
    "HuangEtAl2026",
    "Riemannian curvature of the Bures metric itself",
    "That geometric curvature is distinct from the quantity prescribed here",
]:
    if marker not in main:
        errors.append(f"PRA R1 missing rank-changing Bures-geometry separation marker: {marker}")

# APS substantive-AI disclosure. Research-level use is placed in its own
# publication methods layer rather than only in Acknowledgments.
for marker in [
    r"\section*{AI-Assisted Research and Verification}",
    "OpenAI ChatGPT",
    "GPT-5.6",
    "derivation exploration",
    "adversarial algebra checks",
    "generation and debugging of internal numerical-validation code",
    "AI outputs were treated as provisional",
    "independently checked the resulting claims",
    "primary literature",
    "takes full responsibility",
]:
    if marker not in main:
        errors.append(f"AI disclosure missing marker: {marker}")

# Software-aware Data Availability.
for marker in [
    "No empirical data were created or analyzed in this theoretical study.",
    "Internal numerical-validation scripts were used only to cross-check analytic identities",
    "not required to reproduce the reported results",
    "The validation scripts are available from the author upon reasonable request.",
]:
    if marker not in main:
        errors.append(f"Data Availability statement missing marker: {marker}")

# Publication transform must not change the scientific theorem body after the intro.
# D2 remains frozen through its acknowledgments boundary; PRA R1 inserts only
# the publication-level AI methods/disclosure layer after that frozen body.
anchor = "We consider a real parameter vector"
d2_end_anchor = r"\begin{acknowledgments}"
pra_end_anchor = r"\section*{AI-Assisted Research and Verification}"
if anchor not in d2 or d2_end_anchor not in d2:
    errors.append("D2: theorem-body comparison anchors missing")
if anchor not in main or pra_end_anchor not in main:
    errors.append("PRA R1: theorem-body comparison anchors missing")

if not errors:
    d2_body = d2[d2.index(anchor):d2.index(d2_end_anchor)]
    pra_body = main[main.index(anchor):main.index(pra_end_anchor)]
    if d2_body != pra_body:
        errors.append("PRA R1 transform changed frozen D2 theorem body")

# Supplement publication transform is title-only. Everything from the author
# declaration onward must remain byte-for-byte identical to audited D2.
supp_anchor = r"\author{Anonymous}"
for label, text in [("D2 supplement", supp_d2), ("PRA R1 supplement", supp)]:
    if supp_anchor not in text:
        errors.append(f"{label}: supplement freeze anchor missing")
if not errors:
    if supp_d2[supp_d2.index(supp_anchor):] != supp[supp.index(supp_anchor):]:
        errors.append("PRA R1 supplement transform changed content beyond the title")

# The headline equations/scopes must still be present.
for marker in [
    r"\Vmin(\Cker;D,\rhozero)",
    r"=\frac12\Tr\Cker",
    r"\cA_{\rm ex}^{(2)}=\hbar\nu\,\Vmin",
    "strongly continuous blockwise unitary family",
    "not an arbitrary full tensor of mixed second derivatives",
]:
    if marker not in main:
        errors.append(f"PRA R1 missing frozen theorem marker: {marker}")

# Labels/refs/citations.
for name, text in [(MAIN.name, main), (SUPP.name, supp)]:
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    dup = sorted({x for x in labels if labels.count(x) > 1})
    if dup:
        errors.append(f"{name}: duplicate labels {dup}")
    refs = set(re.findall(r"\\(?:eqref|ref|autoref)\{([^}]+)\}", text))
    missing_refs = sorted(refs - set(labels))
    if missing_refs:
        errors.append(f"{name}: undefined refs {missing_refs}")

bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bib, flags=re.M))
for name, text in [(MAIN.name, main), (SUPP.name, supp)]:
    cited = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        cited.update(x.strip() for x in group.split(",") if x.strip())
    missing = sorted(cited - bib_keys)
    if missing:
        errors.append(f"{name}: missing bibliography keys {missing}")

if errors:
    print("PRA R1 STATIC GATE FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("PRA R1 STATIC GATE PASSED")
print(f"title: {title_match.group(1)}")
print(f"supplement title: {supp_title_match.group(1)}")
print(f"checked publication layer against frozen D2 theorem body and {len(bib_keys)} bibliography entries")
