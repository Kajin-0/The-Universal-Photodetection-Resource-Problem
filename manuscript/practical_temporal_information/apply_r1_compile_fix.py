from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_draft.tex"
out = ROOT / "operational_temporal_information_r1.tex"

text = src.read_text(encoding="utf-8")

old_begin = "\\begin{ruledtabular}\n\\begin{tabular}{p{0.19\\textwidth}p{0.22\\textwidth}p{0.24\\textwidth}p{0.25\\textwidth}}"
new_begin = "\\begin{tabular}{p{0.19\\textwidth}p{0.22\\textwidth}p{0.24\\textwidth}p{0.25\\textwidth}}"
old_end = "\\end{tabular}\n\\end{ruledtabular}"
new_end = "\\end{tabular}"

if text.count(old_begin) != 1 or text.count(old_end) != 1:
    raise SystemExit("Expected exactly one falsification-table ruledtabular wrapper")

text = text.replace(old_begin, new_begin).replace(old_end, new_end)
out.write_text(text, encoding="utf-8")

print(f"Generated {out.name}: removed incompatible ruledtabular wrapper only")
