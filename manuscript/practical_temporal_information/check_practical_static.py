from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
tex_path = ROOT / "operational_temporal_information_draft.tex"
bib_path = ROOT / "references.bib"

tex = tex_path.read_text(encoding="utf-8")
bib = bib_path.read_text(encoding="utf-8")

required = [
    r"\title{Operational temporal-information benchmarks for photodetection}",
    r"\frac{\Tr F}{T}=\frac{2}{\mathrm{NEP}^2(f)}",
    r"\frac{J_B(1)}{J_A(1)}=\frac{13}{3}",
    r"G_{\rm DC}=0",
    r"\lim_{p\to0^+}\frac{4p}{R_{\rm lin}^2}",
    r"\Delta P_s(0)",
    r"V_{\min}=\frac12\Tr C=8(gt)^2",
    r"\section{What would falsify the framework?}",
    r"\section*{AI-Assisted Research and Verification}",
    r"\section*{Data Availability}",
]

missing = [item for item in required if item not in tex]
if missing:
    print("Missing required manuscript markers:")
    for item in missing:
        print(" -", item)
    sys.exit(1)

# Guard the central provenance discipline.
if "established in the companion random-time analysis" not in tex:
    raise SystemExit("Type-II theorem is not explicitly attributed to the companion analysis")
if "principal original model of this paper" not in tex:
    raise SystemExit("WP04 support model is not explicitly identified as the principal original model")
if "not thermodynamic work" not in tex:
    raise SystemExit("Unitary-coupling/work distinction is missing")

# Avoid obvious overclaiming language in the publication-facing draft.
for forbidden in ["first ever", "Nobel", "revolutionary", "NEP is obsolete"]:
    if forbidden.lower() in tex.lower():
        raise SystemExit(f"Forbidden overclaiming phrase found: {forbidden}")

# Every explicit cite key in the TeX must exist in references.bib.
keys = []
for group in re.findall(r"\\cite\{([^}]*)\}", tex):
    keys.extend(k.strip() for k in group.split(",") if k.strip())

bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
missing_keys = sorted(set(keys) - bibkeys)
if missing_keys:
    raise SystemExit("Missing bibliography keys: " + ", ".join(missing_keys))

# The central crossover must appear once as a numbered proposition, not as multiple competing theorems.
if tex.count("Support-controlled survival-to-synthesis crossover") != 1:
    raise SystemExit("Expected exactly one named support-to-synthesis proposition")

print("Practical manuscript static integrity gate: PASS")
print(f"Citations checked: {len(set(keys))}")
