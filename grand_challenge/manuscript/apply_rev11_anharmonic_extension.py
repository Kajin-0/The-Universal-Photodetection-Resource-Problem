from pathlib import Path

main_src = Path("energy_survival_temporal_fisher_rev10_prxq.tex")
main_dst = Path("energy_survival_temporal_fisher_rev11_prxq.tex")
spec_src = Path("rev10_spectral_theorems.tex")
spec_dst = Path("rev11_spectral_theorems.tex")

main = main_src.read_text(encoding="utf-8")
spec = spec_src.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    assert count == 1, f"Expected one match, found {count}: {old[:100]!r}"
    return text.replace(old, new, 1)


def replace_region(text: str, start: str, end: str, new: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[:a] + new + text[b:]

# Compact abstract with the fixed-Hamiltonian result promoted to the main hierarchy.
a = main.index(r"\begin{abstract}")
b = main.index(r"\end{abstract}", a)
abstract = r'''\begin{abstract}
Temporal resolution is usually summarized by a response time or transfer function, but those quantities do not determine how much information about a time-dependent source reaches an accessible record.  We study a fixed quantum excitation emitted at a latent random time, with weak temporal structure encoded in Fourier coefficients of that random-time distribution.  In an exact periodic formulation, every joint measurement on any finite number $N$ of independently encoded excitations obeys the operational harmonic bound $\Tr F_N^{(k)}/N\leq\sum_{m\geq k}q_m$.  We show that the underlying factorization is not restricted to a harmonic ladder: for an arbitrary semibounded pure-point Hamiltonian, long-window random-time averaging isolates exact Bohr gaps and yields the analogous arbitrary-POVM bound $\Tr F_N^{(\nu)}/N\leq\Pr(\Omega\geq\nu)$.  Controlled periodic-to-continuum limits give the same spectral-survival law without assuming a smooth spectral measure.  For one fixed one-copy POVM, the multi-harmonic retention sequence is additionally positive definite.  Combining this Herglotz consistency with semibounded energy tails yields $\bar E^+\geq\hbar\nu A(q)$, where $q=R(\nu)$ and $A(q)\sim[2(1-q)]^{-1/2}$; a finite-chain sine family attains the same exponent, making the near-lossless divergence exponent sharp.  On the full contiguous pure-sector chain, exact one-copy saturation is completely classified by geometric mixtures, equivalently Hausdorff-moment survival sequences, and one source-adapted POVM then saturates every harmonic simultaneously.  The modewise law is inherited by independent quantum-marked Poisson sources under arbitrary parameter-independent source-to-field and detector dynamics, while arbitrary parameter-dependent waveform synthesis requires additional control-resource accounting.
'''
main = main[:a] + abstract + main[b:]

main = replace_once(
    main,
    "The answer is controlled by a simple spectral survival probability.  If $q_n$ is the probability that the fixed excitation occupies total-generator sector $n$ above its participating lower edge, then the accessible two-quadrature Fisher information in temporal harmonic $k$ cannot exceed the probability mass in sectors at least $k$ quanta above that edge.  The result is finite-copy and includes arbitrary entangled collective measurements.  Summing the harmonic tails gives the mean excitation exactly, while a controlled periodic-to-continuum construction produces a pointwise survival-function law for the phase-averaged two-quadrature retention.  The associated Planck-scale energy--frequency inequality is then an immediate first-moment consequence of that stronger survival statement, not the independent source of the result.",
    "The answer is controlled by a simple spectral survival probability.  In the exact periodic formulation, if $q_n$ is the probability that the fixed excitation occupies total-generator sector $n$ above its participating lower edge, then the accessible two-quadrature Fisher information in temporal harmonic $k$ cannot exceed the probability mass in sectors at least $k$ quanta above that edge.  The result is finite-copy and includes arbitrary entangled collective measurements.  Crucially, global equal spacing is not the essential algebraic hypothesis: for an arbitrary semibounded pure-point Hamiltonian, ordinary long-window random-time averaging resolves exact Bohr gaps and the same partial-isometry factorization bounds the Fisher information at a requested gap by the physical spectral tail above that energy difference.  Summing the periodic harmonic tails gives the mean excitation exactly, while a controlled periodic-to-continuum construction produces a pointwise survival-function law.  The associated Planck-scale energy--frequency inequality is then an immediate first-moment consequence of that stronger survival statement, not the independent source of the result.",
)
main = replace_once(
    main,
    "The theorem has four useful features.  First, its proof is short and operational: no optimal quantum measurement needs to be constructed.  Second, when one fixed POVM is used to define a detector's full harmonic response, its retention sequence obeys a Herglotz/Toeplitz positivity constraint.  This forces high retention at one harmonic to propagate to higher multiples and turns the bounded pointwise energy law into a divergent near-unit-retention resource requirement.  Third, exact one-copy extremizers can be classified on the full contiguous pure-sector chain: first-harmonic saturation forces a mixture of geometric populations, equivalently a Hausdorff moment structure, and one source-adapted POVM then saturates the entire harmonic hierarchy.  Fourth, an independent compound-Poisson source representation allows the final detector measurement to be pulled back through arbitrary parameter-independent source-to-field and detector dynamics, so common-field overlap and coherent detector memory do not evade the source bound.",
    "The theorem has five useful features.  First, its proof is short and operational: no optimal quantum measurement needs to be constructed.  Second, the fixed-Hamiltonian extension shows that the modewise mechanism is a Bohr-gap statement rather than an artifact of a harmonic oscillator ladder.  Third, when one fixed one-copy POVM is used to define a detector's response across integer multiples of a chosen gap, its retention sequence obeys a Herglotz/Toeplitz positivity constraint.  This forces high retention at one gap to propagate to higher multiples and turns the bounded pointwise energy law into a divergent near-unit-retention resource requirement.  Fourth, exact one-copy extremizers can be classified on the full contiguous pure-sector chain: first-harmonic saturation forces a mixture of geometric populations, equivalently a Hausdorff moment structure, and one source-adapted POVM then saturates the entire harmonic hierarchy.  Fifth, an independent compound-Poisson source representation allows the final detector measurement to be pulled back through arbitrary parameter-independent source-to-field and detector dynamics, so common-field overlap and coherent detector memory do not evade the source bound.",
)
main = replace_once(main, r"\input{figure1_operational_architecture_body_rev9.tex}", r"\input{figure1_operational_architecture_body_rev11.tex}")
main = replace_once(
    main,
    r"\caption{Operational architecture and theorem scope.  The temporal parameter enters through the latent random-time distribution of a fixed excitation.  Arbitrary parameter-independent downstream processing is absorbed into $\Gamma$.  The modewise record obeys the energy-tail Fisher law, while one fixed one-copy record across harmonics also obeys a positive-definite Herglotz consistency law.  Arbitrary parameter-dependent waveform-state synthesis is a different resource class.}",
    r"\caption{Operational architecture and theorem scope.  The temporal parameter enters through the latent random-time distribution of a fixed excitation.  Arbitrary parameter-independent downstream processing is absorbed into $\Gamma$.  The modewise tail law is exact in the periodic model and extends, in a long-window gap-resolved experiment, to arbitrary semibounded pure-point Hamiltonians at exact Bohr gaps.  One fixed one-copy record across gap multiples additionally obeys positive-definite Herglotz consistency.  Arbitrary parameter-dependent waveform-state synthesis is a different resource class.}",
)
main = main.replace(r"\section{Controlled periodic-to-continuum survival law}", "\\input{rev11_anharmonic_extension.tex}\n\n\\section{Controlled periodic-to-continuum survival law}", 1)
main = replace_once(
    main,
    r"Let $\mu$ be a probability measure on $[0,\infty)$ with finite first moment",
    r"Let $\mu$ be an arbitrary Borel probability measure on $[0,\infty)$ with finite first moment.  No density or smoothness is assumed; atomic, absolutely continuous, and singular-continuous components are all allowed.  Write",
)
main = replace_once(main, r"\input{rev10_spectral_theorems.tex}", r"\input{rev11_spectral_theorems.tex}")
main = replace_once(main, r"\bibliography{references}", r"\bibliography{references,references_rev11}")
main = replace_region(main, r"\section{Separately optimized quantum Fisher envelope}", r"\section{Boundary: arbitrary waveform synthesis}", "")
main = replace_once(
    main,
    "This statement is related to, but distinct from, ordinary time--energy uncertainty and deterministic phase estimation.  In the present experiment, absolute temporal phase is randomized at baseline; the parameters are Fourier coefficients of the random-time \\emph{distribution}.  Established modes-of-asymmetry theory explains which energy-gap components accompany those Fourier coefficients~\\cite{MarvianSpekkens2014Modes}.  The present theorem is not a restatement of that support condition: it bounds the \\emph{classical Fisher information of any actual POVM}, including finite-copy entangled collective measurements, by a sharp coefficient determined solely by paired populations and, universally, by the upper energy tail.  The geometric family further shows that one common measurement can saturate the full harmonic hierarchy.",
    "This statement is related to, but distinct from, ordinary time--energy uncertainty and deterministic phase estimation.  In the present experiment, absolute temporal phase is randomized at baseline; the parameters are Fourier coefficients of the random-time \\emph{distribution}.  Established modes-of-asymmetry theory explains which Bohr-frequency components accompany those Fourier coefficients~\\cite{MarvianSpekkens2014Modes}.  The present theorem is not a restatement of that support condition: it bounds the \\emph{classical Fisher information of any actual POVM}, including finite-copy entangled collective measurements, by a population coefficient and semibounded energy tail.  Section~\\ref{sec:anharmonic} makes this distinction especially explicit: the Fisher-tail mechanism survives completely anharmonic pure-point spectra at exact Bohr gaps.  The geometric family further shows that one common measurement can saturate the full harmonic hierarchy in the contiguous-chain model.",
)
main = replace_once(
    main,
    "Several extensions remain open.  Correlated quantum emission processes need not factor through independent event marks.  Direct coherent or squeezed waveform synthesis requires explicit accounting of the parameter-dependent encoding resource.  It is also natural to ask whether other compact groups or other semibounded generators admit analogous survival laws for perturbations of their mixing distributions.",
    "Several extensions remain open.  A direct fixed-Hamiltonian theorem for genuinely continuous spectral subspaces, with quantitative finite-window leakage rather than a controlled discretization, would further strengthen the continuum side.  Correlated quantum emission processes need not factor through independent event marks, and direct coherent or squeezed waveform synthesis requires explicit accounting of the parameter-dependent encoding resource.",
)
main = replace_once(
    main,
    "For a fixed semibounded-energy excitation whose temporal waveform is encoded in the distribution of a random translation, we have derived a sharp operational resource law.  Every finite-copy collective measurement has a two-quadrature harmonic Fisher trace bounded by a paired spectral population and, more coarsely, by the upper energy tail.  The resulting controlled periodic-to-continuum law,",
    "For a fixed semibounded-energy excitation whose temporal waveform is encoded in the distribution of a random translation, we have derived a family of operational spectral resource laws.  In the exact periodic experiment every finite-copy collective measurement has a two-quadrature harmonic Fisher trace bounded by a paired spectral population and, more coarsely, by the upper energy tail.  The same factorization extends in a long-window limit to arbitrary semibounded pure-point Hamiltonians at exact Bohr gaps, showing that global harmonic spacing is not the physical origin of the ceiling.  The controlled periodic-to-continuum law,",
)
main = replace_once(
    main,
    "The result therefore combines a modewise resource ceiling, a global consistency law for one physical measurement, a rigidity classification of extremizers, and a precise boundary showing why arbitrary waveform-state engineering requires additional control-resource accounting.",
    "The result therefore combines an arbitrary-POVM Bohr-gap resource ceiling, a global consistency law for one physical measurement, a sharp near-lossless divergence exponent, a rigidity classification of extremizers, and a precise boundary showing why arbitrary waveform-state engineering requires additional control-resource accounting.",
)

spec = replace_once(
    spec,
    "Then, irrespective of gaps in the nonzero populations,\n$A_k=\\rho_0^{1/2}V^k\\rho_0^{1/2}$.  A POVM on the original system may be lifted trivially to the purification; the resulting outcome probabilities and Fisher information are unchanged.  Thus the following consistency law applies to every fixed one-copy POVM in the exact periodic random-time experiment, not only to an optimal measurement or to an equality family.",
    "Then, irrespective of gaps in the nonzero populations,\n$A_k=\\rho_0^{1/2}V^k\\rho_0^{1/2}$.  The appended vectors are algebraic placeholders only: $\\rho_0^{1/2}$ annihilates every zero-population sector, and positivity of the posterior operator measure therefore forces its posterior density to have zero support there almost everywhere.  The completion cannot create score or Fisher information.  A POVM on the original system may be lifted trivially to the purification; the resulting outcome probabilities and Fisher information are unchanged.  Thus the following consistency law applies to every fixed one-copy POVM in the exact periodic random-time experiment, not only to an optimal measurement or to an equality family.",
)
spec = replace_once(
    spec,
    "with the same $(1-R)^{-1/2}$ divergence.  This continuum statement retains the common-measurement and controlled-limit hypotheses explicitly.",
    "with the same $(1-R)^{-1/2}$ divergence.  This continuum statement retains the common-measurement and controlled-limit hypotheses explicitly.  Independently, Section~\\ref{sec:anharmonic} shows that the discrete Herglotz construction and the same energy-divergence law apply to exact multiples of any chosen Bohr gap for an arbitrary semibounded pure-point Hamiltonian in the long-window limiting experiment.",
)

assert r"\input{rev11_anharmonic_extension.tex}" in main
assert r"\section{Separately optimized quantum Fisher envelope}" not in main
assert "singular-continuous components are all allowed" in main
assert "The completion cannot create score or Fisher information" in spec
assert r"\bibliography{references,references_rev11}" in main

main_dst.write_text(main, encoding="utf-8")
spec_dst.write_text(spec, encoding="utf-8")
print(f"Wrote {main_dst}")
print(f"Wrote {spec_dst}")
