from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev2.tex")
dst = Path("energy_survival_temporal_fisher_rev3.tex")

text = src.read_text(encoding="utf-8")


def replace_once(old: str, new: str):
    global text
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old[:100]!r}"
    text = text.replace(old, new, 1)


# 0. Short theorem subtitles so REVTeX two-column theorem headings do not
# create overfull boxes.  This is layout-only; theorem content is unchanged.
replace_once(
    r"\begin{theorem}[Collective temporal-harmonic Fisher bound]",
    r"\begin{theorem}[Finite-copy Fisher bound]",
)
replace_once(
    r"\begin{theorem}[Continuum operational survival bound]",
    r"\begin{theorem}[Continuum survival bound]",
)

# 1. Abstract: define R operationally and retain the two-quadrature scope.
replace_once(
    "where $F_N^{(k)}$ is the classical Fisher-information block and $N_E$ is the excitation-sector index above the participating lower energy edge.  The result follows directly",
    "where $F_N^{(k)}$ is the classical Fisher-information block, $N_E$ is the excitation-sector index above the participating lower energy edge, and the continuum quantity $R$ below denotes the source-normalized trace of this two-quadrature block (equivalently, the phase-averaged scalar retention).  The result follows directly",
)

# 2. Introduction: avoid implying the same coefficient for a known scalar quadrature.
replace_once(
    "Summing the harmonic tails gives the mean excitation exactly, while a periodic-to-continuum construction produces a pointwise survival-function law and a sharp Planck-scale energy--frequency relation.",
    "Summing the harmonic tails gives the mean excitation exactly, while a periodic-to-continuum construction produces a pointwise survival-function law for the phase-averaged two-quadrature retention and a Planck-scale energy--frequency constraint.",
)

# 3. Add the phase-average and uniform-phase-guarantee interpretation directly after R_N is defined.
replace_once(
    "R_N(k)=\\frac1N\\Tr F_N^{(k)}.\n\\end{equation}\nThen",
    "R_N(k)=\\frac1N\\Tr F_N^{(k)}.\n\\end{equation}\nBecause the latent input block is $(1/2)I_2$, $R_N(k)$ is also the average, over sinusoidal phase, of the scalar Fisher-retention fraction relative to the latent source.  If a detector retains at least a fraction $q$ for every unit direction in the cosine--sine plane, then both eigenvalues of $F_N^{(k)}/N$ are at least $q/2$, and therefore $R_N(k)\\geq q$.\n\nThen",
)

# 4. Continuum proof: make convergence at atoms rigorous for a general lattice sequence.
replace_once(
    "Continuity from above of a finite measure yields convergence of the right-hand side to $\\mu([\\nu,\\infty))$, including at atoms because the closed-tail convention is used.",
    "For every $\\varepsilon>0$, sufficiently small $\\delta$ gives $\\nu-\\varepsilon\\leq k_\\delta\\delta\\leq\\nu$, hence $\\mu([\\nu,\\infty))\\leq\\mu([k_\\delta\\delta,\\infty))\\leq\\mu([\\nu-\\varepsilon,\\infty))$.  Letting $\\varepsilon\\downarrow0$ and using continuity from above of the finite measure proves convergence to $\\mu([\\nu,\\infty))$, including at atoms because the closed-tail convention is used.",
)

# 5. Clarify the flat-band implication as a phase-uniform guarantee.
replace_once(
    "Thus a guaranteed retention $R(2\\pi B)\\geq q_0$ requires $\\bar E^+\\geq hBq_0$.",
    "Thus $\\bar E^+\\geq hBq_0$ whenever the phase-averaged retention at $B$ is at least $q_0$.  In particular, the same condition is necessary if the detector is required to retain at least $q_0$ of the scalar Fisher information for every sinusoidal phase at frequency $B$.",
)

# 6. Remove the spectral-measure / Poisson-mean notation collision by changing
# only the Poisson section from mu to Lambda.
poisson_start = text.index(r"\section{Independent Poisson events and a physical bosonic field}")
poisson_end = text.index(r"\section{Separately optimized quantum Fisher envelope}")
poisson = text[poisson_start:poisson_end]
assert r"\mu" in poisson
poisson = poisson.replace(r"\mu", r"\Lambda")
text = text[:poisson_start] + poisson + text[poisson_end:]

# 7. QFI section: distinguish the quantum metric trace from an attainable
# common-POVM Fisher trace, and cite the exact Hardy--Hilbert provenance.
replace_once(
    "For comparison, optimizing the SLD measurement separately for a scalar quadrature of harmonic $k$ gives, for a pure excitation,\n\\begin{equation}\n G_Q(k)=2\\sum_n\\frac{q_nq_{n+k}}{q_n+q_{n+k}},\n \\label{eq:QFI-mode}\n\\end{equation}\nwhere zero denominators contribute zero.",
    "For comparison, for a pure excitation each scalar quadrature of harmonic $k$ has SLD quantum Fisher information $Q_k=\\sum_n q_nq_{n+k}/(q_n+q_{n+k})$, with zero denominators contributing zero.  Summing the two equal scalar values gives the SLD-QFIM trace; because the latent two-quadrature input trace is unity, its source-normalized trace is\n\\begin{equation}\n G_Q(k)=2\\sum_n\\frac{q_nq_{n+k}}{q_n+q_{n+k}}.\n \\label{eq:QFI-mode}\n\\end{equation}",
)

replace_once(
    "The analytic $\\pi$ coefficient can be reduced to a classical sharp Hardy--Hilbert integral inequality; it is not claimed as new mathematics.  Related sharp positive-frequency inequalities are established in analysis~\\cite{Pocovnicu2011}.",
    "The analytic $\\pi$ coefficient can be reduced to a classical sharp Hardy--Hilbert integral inequality and is not claimed as new mathematics~\\cite{Yang2001HardyHilbert}; related sharp positive-frequency inequalities are also established in analysis~\\cite{Pocovnicu2011}.",
)

replace_once(
    "Equations~\\eqref{eq:QFI-mode}--\\eqref{eq:pi-envelope} are useful as a quantum envelope, but they optimize incompatible measurements mode by mode.  Theorem~\\ref{thm:finite-copy} instead bounds the Fisher information of one actual measurement, even if that measurement is a finite-copy entangled collective POVM.",
    "Equations~\\eqref{eq:QFI-mode}--\\eqref{eq:pi-envelope} are useful as a quantum-metric envelope, but an SLD-QFIM does not by itself imply that one POVM attains both quadratures or multiple modes simultaneously.  Theorem~\\ref{thm:finite-copy} instead bounds the classical Fisher information of one actual measurement, even if that measurement is a finite-copy entangled collective POVM.",
)

# 8. Replace the verbal coherent-sideband no-go by an explicit local model.
old_nogo = """The random-time hypothesis cannot simply be removed while retaining a baseline-mean-energy-only theorem.  Consider a phase-coherent optical carrier and let the parameter generate an infinitesimal sideband at an arbitrarily large modulation frequency.  The derivative of the quantum state with respect to the sideband amplitude is first order in that amplitude, while the additional mean sideband energy is second order.  Consequently, by taking the local parameter to zero while increasing the sideband frequency, one can obtain a nonzero local waveform tangent at frequencies that are not controlled by the unperturbed mean energy alone.

This is consistent with general waveform-estimation theory~\\cite{TsangWisemanCaves2011}: a waveform can enter through a parameter-dependent Hamiltonian or source map, and its quantum Fisher kernel depends on the generator of that encoding.  A universal theorem for arbitrary state-valued waveform synthesis would therefore have to count an encoding/control/action resource---for example a suitable tangent-energy, energy-curvature, or control-Hamiltonian constraint---rather than only the baseline energy of the unmodulated state.
"""
new_nogo = """The random-time hypothesis cannot simply be removed while retaining a baseline-mean-energy-only theorem.  A minimal counterexample uses a coherent carrier mode of angular frequency $\\omega_c$ and a sideband mode at $\\omega_c+\\nu$.  Let the unmodulated state be
\\begin{equation}
 |\\psi_0\\rangle=|\\alpha\\rangle_c\\otimes|0\\rangle_s,
\\end{equation}
and encode a real local waveform parameter by a sideband displacement,
\\begin{equation}
 |\\psi_\\epsilon\\rangle
 =|\\alpha\\rangle_c\\otimes|\\epsilon\\gamma\\rangle_s .
 \\label{eq:sideband-counterexample}
\\end{equation}
At $\\epsilon=0$ the pure-state QFI for $\\epsilon$ is $4|\\gamma|^2$, independent of the sideband detuning $\\nu$.  The unmodulated mean energy is $\\hbar\\omega_c|\\alpha|^2$ (up to vacuum conventions), while the added sideband energy is
\\begin{equation}
 \\Delta E(\\epsilon)
 =\\hbar(\\omega_c+\\nu)|\\gamma|^2\\epsilon^2,
 \\label{eq:sideband-energy}
\\end{equation}
so its first derivative vanishes at the operating point.  Thus a nonzero local waveform tangent can be placed at arbitrarily large $\\nu$ without increasing the baseline mean energy.  The energetic/control cost appears in the parameter-dependent encoding map or in second-order energy curvature, not in the baseline state alone.

This is consistent with general waveform-estimation theory~\\cite{TsangWisemanCaves2011}: a waveform can enter through a parameter-dependent Hamiltonian or source map, and its quantum Fisher kernel depends on the generator of that encoding.  A theorem for arbitrary state-valued waveform synthesis must therefore count an encoding/control/action resource---for example a suitable tangent-energy, energy-curvature, or control-Hamiltonian constraint---rather than only the baseline energy of the unmodulated state.
"""
replace_once(old_nogo, new_nogo)

# 9. Discussion and conclusion: keep the two-quadrature scope visible and fix
# an equality-sounding wording that should only say "bounded by".
replace_once(
    "The central result can be read directly from Eq.~\\eqref{eq:survival-law}: retaining temporal Fisher information at angular frequency $\\nu$ requires spectral probability weight at least $\\hbar\\nu$ above the participating lower energy edge.",
    "The central result can be read directly from Eq.~\\eqref{eq:survival-law}: retaining phase-averaged two-quadrature temporal Fisher information at angular frequency $\\nu$ requires spectral probability weight at least $\\hbar\\nu$ above the participating lower energy edge.  A uniform guarantee over all sinusoidal phases is a stronger requirement and therefore obeys the same bound.",
)

replace_once(
    "Every finite-copy collective measurement obeys a harmonic Fisher ceiling equal to a paired spectral population and no larger than the upper energy tail.",
    "Every finite-copy collective measurement has a two-quadrature harmonic Fisher trace bounded by a paired spectral population and, more coarsely, by the upper energy tail.",
)

# Assertions for repaired issues.
assert r"parameter-independent Poisson mean $\mu$" not in text
assert r"p_\mu" not in text
assert r"\Lambda" in text[poisson_start:poisson_start + len(poisson) + 500]
assert "phase-averaged" in text
assert r"\Delta E(\epsilon)" in text
assert "Yang2001HardyHilbert" in text

# Rev3 is a science/interpretation hardening pass.  Core theorem equations and
# proof inequalities are unchanged.
dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
