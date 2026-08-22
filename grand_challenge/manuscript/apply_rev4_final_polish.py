from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev3.tex")
dst = Path("energy_survival_temporal_fisher_rev4.tex")

text = src.read_text(encoding="utf-8")


def replace_once(old: str, new: str):
    global text
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old[:120]!r}"
    text = text.replace(old, new, 1)


# 1. Abstract: avoid overloading N with copy number / event number / energy index,
# and state the continuum result as the controlled periodic limit actually proved.
replace_once(
    r"\frac{1}{N}\Tr F_N^{(k)}\leq \Pr(N_E\geq k),",
    r"\frac{1}{N}\Tr F_N^{(k)}\leq \sum_{m\geq k}q_m,",
)
replace_once(
    "where $F_N^{(k)}$ is the classical Fisher-information block, $N_E$ is the excitation-sector index above the participating lower energy edge, and the continuum quantity $R$ below denotes the source-normalized trace of this two-quadrature block (equivalently, the phase-averaged scalar retention).",
    "where $F_N^{(k)}$ is the classical Fisher-information block, $q_m$ is the excitation probability in sector $m$ above the participating lower energy edge, and the continuum quantity $R$ below denotes the source-normalized trace of this two-quadrature block (equivalently, the phase-averaged scalar retention).",
)
replace_once(
    "In the continuum limit it gives the pointwise survival law",
    "For controlled large-period limits it gives the pointwise survival law",
)

# 2. Make the treatment of general POVMs precise without introducing
# unnecessary operator-valued Radon--Nikodym machinery in the main proof.
replace_once(
    "For a POVM element $M_y$, with the obvious measure-theoretic replacement for continuous outcomes, define",
    "We write the proof first for a discrete POVM with elements $M_y$.  A general outcome space follows by applying the same inequality to every finite measurable coarse graining; classical Fisher information is the supremum of the Fisher information over such finite partitions for the dominated local experiment considered here.  Define",
)

# 3. Remove a common factor-of-two ambiguity in the equality discussion.
replace_once(
    "whose characteristic-function retention is $\\e^{-2a|\\nu|}$.",
    "whose characteristic function is $\\e^{-a|\\nu|}$ and whose timestamp Fisher retention is therefore its modulus squared, $\\e^{-2a|\\nu|}$.",
)

# 4. Keep the continuum scope explicit in Discussion and Conclusion.
replace_once(
    "In the continuum, the same construction gives an exponential excitation spectrum and Cauchy timing density, providing an exact bridge between the energy survival function and a physically interpretable timestamp channel.",
    "In the controlled large-period continuum limit, the same construction gives an exponential excitation spectrum and Cauchy timing density, providing an exact bridge between the energy survival function and a physically interpretable timestamp channel.",
)
replace_once(
    "The resulting continuum law,\n\\begin{equation}",
    "The resulting controlled-limit continuum law,\n\\begin{equation}",
)

# 5. Final source assertions for the intended claim discipline.
assert "N_E" not in text
assert "controlled large-period" in text
assert r"characteristic function is $\e^{-a|\nu|}$" in text
assert "obvious measure-theoretic replacement" not in text
assert r"\boxed{" not in text

# Rev4 changes no theorem equation, proof inequality, physical source class,
# or numerical constant.  It is the final claim/notation/readability polish.
dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
