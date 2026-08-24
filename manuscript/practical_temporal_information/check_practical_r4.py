from pathlib import Path

ROOT = Path(__file__).resolve().parent
r3 = (ROOT / "operational_temporal_information_r3.tex").read_text(encoding="utf-8")
r4 = (ROOT / "operational_temporal_information_r4.tex").read_text(encoding="utf-8")

old = "\\usepackage{hyperref}\n"
new = "\\usepackage{hyperref}\n\\hypersetup{hidelinks}\n"
if r3.count(old) != 1:
    raise SystemExit("R3 hyperref package line not unique")
expected = r3.replace(old, new, 1)
if r4 != expected:
    raise SystemExit("R4 changed content beyond hiding hyperlink borders")
if r4.count("\\hypersetup{hidelinks}") != 1:
    raise SystemExit("R4 must contain exactly one hidelinks setting")
print("Practical manuscript R4 presentation-isolation gate: PASS")
