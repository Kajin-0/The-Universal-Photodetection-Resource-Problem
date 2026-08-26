from pathlib import Path
import sys

from r5_figure_blocks import FIGURE_BLOCKS, EXPECTED_FIGURE_PATHS, EXPECTED_LABELS

ROOT = Path(__file__).resolve().parent
r4 = (ROOT / "operational_temporal_information_r4.tex").read_text(encoding="utf-8")
r5 = (ROOT / "operational_temporal_information_r5.tex").read_text(encoding="utf-8")

if r4.count(r"\begin{figure") != 0:
    raise SystemExit("R4 unexpectedly contains figure environments; R5 isolation premise changed")

for marker, block in FIGURE_BLOCKS:
    if r4.count(marker) != 1:
        raise SystemExit(f"R4 marker not unique: {marker}")
    if r5.count(block) != 1:
        raise SystemExit("R5 must contain each frozen figure block exactly once")

stripped = r5
for _, block in FIGURE_BLOCKS:
    token = block + "\n\n"
    if stripped.count(token) != 1:
        raise SystemExit("R5 figure block separator changed")
    stripped = stripped.replace(token, "", 1)

if stripped != r4:
    raise SystemExit("R5 changes content beyond the four frozen figure blocks")

if r5.count(r"\begin{figure*}[t]") != 4 or r5.count(r"\end{figure*}") != 4:
    raise SystemExit("R5 must contain exactly four wide figure floats")

for path in EXPECTED_FIGURE_PATHS:
    if r5.count(path) != 1:
        raise SystemExit(f"Missing or duplicate frozen figure path: {path}")

for label in EXPECTED_LABELS:
    if r5.count(r"\label{" + label + "}") != 1:
        raise SystemExit(f"Missing or duplicate figure label: {label}")

required_caption_markers = [
    "specification-incompleteness example, not a new detector theorem",
    "imported from the companion random-time analysis",
    "theorem in the text is broader than the plotted special path",
    "not thermodynamic work and is not claimed as new beam-splitter physics",
]
for marker in required_caption_markers:
    if marker not in r5:
        raise SystemExit(f"R5 caption provenance/scope marker missing: {marker}")

for forbidden in ["first ever", "universal detector metric", "NEP is obsolete"]:
    if forbidden.lower() in r5.lower():
        raise SystemExit(f"Forbidden overclaiming phrase in R5: {forbidden}")

print("Practical manuscript R5 figure-integration isolation gate: PASS")
