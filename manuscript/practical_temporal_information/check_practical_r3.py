from pathlib import Path

ROOT = Path(__file__).resolve().parent
r2 = (ROOT / "operational_temporal_information_r2.tex").read_text(encoding="utf-8")
r3 = (ROOT / "operational_temporal_information_r3.tex").read_text(encoding="utf-8")

expected = r2

reference_repairs = {
    r"\eqref{eq:survival_bound}": r"\eqref{eq:survival_bound_general}",
    r"\eqref{eq:boundary_bound}": r"\eqref{eq:boundary_bound_general}",
    r"\eqref{eq:main_crossover}": r"\eqref{eq:main_crossover_general}",
}
for old, new in reference_repairs.items():
    if expected.count(old) != 1:
        raise SystemExit(f"R2 no longer has the expected single stale reference: {old}")
    expected = expected.replace(old, new, 1)

old_benchmark = (
    "A textbook benchmark is resonant exchange between two bosonic modes. "
    "Restrict to the fixed-total-excitation manifold $N_{\\rm tot}=2$ and define"
)
new_benchmark = (
    "A textbook benchmark is resonant exchange between two bosonic modes of the same angular frequency $\\nu$, "
    "with free Hamiltonian $H_0=\\hbar\\nu(N_C+N_S)$. "
    "Restrict to the fixed-total-excitation manifold $N_{\\rm tot}=2$ and define"
)
if expected.count(old_benchmark) != 1:
    raise SystemExit("R2 resonant benchmark lead changed unexpectedly")
expected = expected.replace(old_benchmark, new_benchmark, 1)

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
if expected.count(old_shell) != 1:
    raise SystemExit("R2 fixed-shell sentence changed unexpectedly")
expected = expected.replace(old_shell, new_shell, 1)

if r3 != expected:
    raise SystemExit("R3 contains textual changes outside the audited reference/resonance repairs")

required = [
    r"H_0=\hbar\nu(N_C+N_S)",
    "same angular frequency",
    "commute with $H_0$",
    "For unequal bare mode frequencies",
    "pump or controller supplying the frequency difference must be included explicitly",
    r"\eqref{eq:survival_bound_general}",
    r"\eqref{eq:boundary_bound_general}",
    r"\eqref{eq:main_crossover_general}",
]
for marker in required:
    if marker not in r3:
        raise SystemExit(f"R3 missing required repair marker: {marker}")

for stale in reference_repairs:
    if stale in r3:
        raise SystemExit(f"R3 retained stale reference: {stale}")

print("Practical manuscript R3 hostile-review isolation gate: PASS")
