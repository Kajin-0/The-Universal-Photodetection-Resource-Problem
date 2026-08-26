from pathlib import Path

from r6_compression_map import EDITS

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_r5.tex"
out = ROOT / "operational_temporal_information_r6.tex"

text = src.read_text(encoding="utf-8")

for name, old, new in EDITS:
    if text.count(old) != 1:
        raise SystemExit(f"R6 edit source not unique for {name}: found {text.count(old)}")
    text = text.replace(old, new, 1)

out.write_text(text, encoding="utf-8")
print(f"Generated {out.name}: applied {len(EDITS)} audited prose-only compression edits")
