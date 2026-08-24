from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_r2.tex"
out = ROOT / "operational_temporal_information_r3.tex"

text = src.read_text(encoding="utf-8")

# Repair only the three stale downstream references created by the isolated R2
# section replacement.
reference_repairs = {
    r"\eqref{eq:survival_bound}": r"\eqref{eq:survival_bound_general}",
    r"\eqref{eq:boundary_bound}": r"\eqref{eq:boundary_bound_general}",
    r"\eqref{eq:main_crossover}": r"\eqref{eq:main_crossover_general}",
}
for old, new in reference_repairs.items():
    if text.count(old) != 1:
        raise SystemExit(f"Expected exactly one stale R2 reference: {old}")
    text = text.replace(old, new, 1)

old_benchmark = (
    "A textbook benchmark is resonant exchange between two bosonic modes. "
    "Restrict to the fixed-total-excitation manifold $N_{\\rm tot}=2$ and define"
)
new_benchmark = (
    "A textbook benchmark is resonant exchange between two bosonic modes of the same angular frequency $\\nu$, "
    "with free Hamiltonian $H_0=\\hbar\\nu(N_C+N_S)$. "
    "Restrict to the fixed-total-excitation manifold $N_{\\rm tot}=2$ and define"
)
if text.count(old_benchmark) != 1:
    raise SystemExit("Expected exactly one resonant-benchmark lead paragraph")
text = text.replace(old_benchmark, new_benchmark, 1)

old_shell = (
    "The usual beam-splitter exchange operators $a_C^\\dagger a_S\\pm a_Ca_S^\\dagger$ "
    "act entirely within this fixed bare-energy shell. "
)
new_shell = (
    "For these equal-frequency modes, the usual beam-splitter exchange operators "
    "$a_C^\\dagger a_S\\pm a_Ca_S^\\dagger$ commute with $H_0$ and act entirely within this fixed bare-energy shell. "
    "For unequal bare mode frequencies, the reduced two-mode exchange alone is not globally energy conserving; "
    "the pump or controller supplying the frequency difference must be included explicitly. "
)
if text.count(old_shell) != 1:
    raise SystemExit("Expected exactly one fixed-shell beam-splitter sentence")
text = text.replace(old_shell, new_shell, 1)

out.write_text(text, encoding="utf-8")
print(f"Generated {out.name}: migrated three R2 references and clarified the resonant equal-frequency energy-conservation benchmark only")
