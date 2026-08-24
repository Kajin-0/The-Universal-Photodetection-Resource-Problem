from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_r1.tex"
out = ROOT / "operational_temporal_information_r2.tex"

text = src.read_text(encoding="utf-8")
start_marker = "\\section{Spectral support: from survival to synthesis}"
end_marker = "\\section{Standard Hamiltonian implementation benchmark}"

if text.count(start_marker) != 1 or text.count(end_marker) != 1:
    raise SystemExit("Expected exactly one support section and one following Hamiltonian section")

start = text.index(start_marker) + len(start_marker)
end = text.index(end_marker, start)

replacement = "\n\n\\input{sections/support_crossover_r2}\n\n"
text = text[:start] + replacement + text[end:]
out.write_text(text, encoding="utf-8")

print(f"Generated {out.name}: replaced only the support-crossover section body with the WP09 generalized version")
