from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
r1 = (ROOT / "operational_temporal_information_r1.tex").read_text(encoding="utf-8")
r2 = (ROOT / "operational_temporal_information_r2.tex").read_text(encoding="utf-8")
sec = (ROOT / "sections" / "support_crossover_r2.tex").read_text(encoding="utf-8")

start_marker = "\\section{Spectral support: from survival to synthesis}"
end_marker = "\\section{Standard Hamiltonian implementation benchmark}"

for text, name in [(r1, "R1"), (r2, "R2")]:
    if text.count(start_marker) != 1 or text.count(end_marker) != 1:
        raise SystemExit(f"{name}: support/Hamiltonian section markers not unique")

r1_start = r1.index(start_marker)
r1_body_start = r1_start + len(start_marker)
r1_end = r1.index(end_marker, r1_body_start)

r2_start = r2.index(start_marker)
r2_body_start = r2_start + len(start_marker)
r2_end = r2.index(end_marker, r2_body_start)

if r1[:r1_body_start] != r2[:r2_body_start]:
    raise SystemExit("R2 changed text before the support-crossover section body")
if r1[r1_end:] != r2[r2_end:]:
    raise SystemExit("R2 changed text after the support-crossover section body")

expected_body = "\n\n\\input{sections/support_crossover_r2}\n\n"
if r2[r2_body_start:r2_end] != expected_body:
    raise SystemExit("R2 support section body is not the isolated audited input")

required = [
    r"\rho_p=a_p|c\rangle\langle c|+p|s\rangle\langle s|+\sigma_p",
    r"R_{\rm lin}^2=",
    r"\frac{a_pp}{\kappa^2(a_p-p)^2}",
    r"\lim_{p\to0^+}\frac{4p}{R_{\rm lin}^2}",
    r"4\kappa^2q",
    r"\Delta P_s(0)",
    "spectator populations",
    "local converter leaves the spectator sector inert",
    r"\Tr F=4q\kappa^2=\Delta P_s(0)",
]
missing = [item for item in required if item not in sec]
if missing:
    print("Missing R2 support-strengthening markers:")
    for item in missing:
        print(" -", item)
    sys.exit(1)

if sec.count("Spectator-independent seed regularization") != 1:
    raise SystemExit("Expected exactly one generalized crossover proposition")

# Prevent the R2 section from claiming universality beyond the selected-mode model.
for required_limitation in ["Loss", "spectator", "converter"]:
    if required_limitation not in sec:
        raise SystemExit(f"R2 support section missing limitation marker: {required_limitation}")

print("Practical manuscript R2 scientific-isolation gate: PASS")
