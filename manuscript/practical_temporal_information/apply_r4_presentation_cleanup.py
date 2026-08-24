from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_r3.tex"
out = ROOT / "operational_temporal_information_r4.tex"

text = src.read_text(encoding="utf-8")
old = "\\usepackage{hyperref}\n"
new = "\\usepackage{hyperref}\n\\hypersetup{hidelinks}\n"

if text.count(old) != 1:
    raise SystemExit("Expected exactly one hyperref package line in R3")
if "\\hypersetup{hidelinks}" in text:
    raise SystemExit("R3 already contains the R4 presentation cleanup")

text = text.replace(old, new, 1)
out.write_text(text, encoding="utf-8")
print(f"Generated {out.name}: hid PDF link borders only")
