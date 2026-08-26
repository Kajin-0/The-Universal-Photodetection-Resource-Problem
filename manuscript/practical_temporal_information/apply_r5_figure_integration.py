from pathlib import Path

from r5_figure_blocks import FIGURE_BLOCKS

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_r4.tex"
out = ROOT / "operational_temporal_information_r5.tex"

text = src.read_text(encoding="utf-8")

for marker, block in FIGURE_BLOCKS:
    if text.count(marker) != 1:
        raise SystemExit(f"R4 marker not unique: {marker}")
    if block in text:
        raise SystemExit("R4 already contains an R5 figure block")
    text = text.replace(marker, block + "\n\n" + marker, 1)

out.write_text(text, encoding="utf-8")
print(f"Generated {out.name}: inserted four frozen WP12 figures/captions only")
