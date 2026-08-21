#!/usr/bin/env python3
"""Generate Rev9 translational-grounding source from generated Rev8.

Rev9 does not change the theorem class. It adds only operational translation:
canonical timing-law mappings, a direct histogram estimator, finite-support and
mark-resource clarifications, a measurement-chain caveat, a DC-normalization
note, an engineering interpretation of the rare-fast construction, and a short
empirical anchor subsection tied to established SPAD timing measurements.
"""
from pathlib import Path

src = Path("event_resource_theorem_rev8.tex")
out = Path("event_resource_theorem_rev9.tex")
section = Path("section_practical_grounding_rev9.tex")
empirical = Path("section_empirical_grounding_rev9.tex")

assert src.exists(), "Generate Rev8 first with apply_rev8_referee_surgical.py"
assert section.exists()
assert empirical.exists()
s = src.read_text(encoding="utf-8")

old = (
    r"A capture-weighted local registration-hazard budget supplies the microscopic bound "
    r"$B_{\rm FI}\le\mathfrak H/(4\eta)$ and explicit inverse resource costs. We then prove "
    r"that fixed mean and variance, a free source-synchronous clock, and stationary "
    r"thermodynamic aggregates are each insufficient timing resources in distinct senses."
)
new = (
    r"A capture-weighted local registration-hazard budget supplies the microscopic bound "
    r"$B_{\rm FI}\le\mathfrak H/(4\eta)$ and explicit inverse resource costs. For direct use "
    r"with existing timing data, we give closed-form mappings for canonical timing laws and "
    r"a fit-free estimator of $B_{\rm FI}$ from digitized impulse-response histograms. We then "
    r"prove that fixed mean and variance, a free source-synchronous clock, and stationary "
    r"thermodynamic aggregates are each insufficient timing resources in distinct senses."
)
assert s.count(old) == 1
s = s.replace(old, new, 1)

old = (
    r"For this paper we normalize every electrical-record Fisher information by "
    r"Eq.~\eqref{eq:inputFI} for nonzero modulation frequency, with the exact-DC convention "
    r"just stated. The source model is intentionally classical/direct-detection specific; "
    r"no claim is made here for arbitrary optical phase encodings or nonclassical input states."
)
new = old + r"""

\paragraph{Normalization note for DC/lock-in comparisons.}
$G$ is always a source-normalized ratio. Under the parameterization in Eq.~\eqref{eq:source}, the absolute incident FI rate is $\Phi_0/2$ for every nonzero sinusoidal frequency and $\Phi_0$ at exact DC. Therefore one should \emph{not} multiply $G(0)$ by two: $G(0)=\eta$ already uses the correct DC normalization. The factor of two enters only when converting the normalized transfer back to an absolute FI rate."""
assert s.count(old) == 1
s = s.replace(old, new, 1)

anchor = r"\input{section_operational_bandwidth_rev7}"
assert s.count(anchor) == 1
s = s.replace(
    anchor,
    anchor
    + "\n\n"
    + r"\input{section_practical_grounding_rev9}"
    + "\n\n"
    + r"\input{section_empirical_grounding_rev9}",
    1,
)

old = (
    r"For a weakly coupled thermal bosonic optical reservoir one may have "
    r"$d=\gamma(\omega_0)[n_T(\omega_0)+1]$; temperature only supplies a speed statement "
    r"after the absolute coupling spectrum $\gamma(\omega_0)$ is separately bounded."
)
new = old + r"""

\paragraph{Engineering interpretation.}
The rare-fast construction can be read as a hidden fast local mode with a vanishing stationary duty cycle: its conditional escape rate scales as $\lambda_1\sim R$ while the occupation of the fast state scales as $R^{-1}$, so their product and hence the stationary jump traffic can remain $O(1)$. A trap, avalanche substate, or other internal transient can therefore possess a very short conditional time scale without forcing a large time-averaged activity. Constraining such a mode requires an independent bound on an absolute local rate or transient pole; stationary power, traffic, or entropy production alone is insufficient."""
assert s.count(old) == 1
s = s.replace(old, new, 1)

assert s.count(r"\input{section_practical_grounding_rev9}") == 1
assert s.count(r"\input{section_empirical_grounding_rev9}") == 1
assert "fit-free estimator" in s
assert "multiply $G(0)$ by two" in s
assert "hidden fast local mode" in s
assert s.count(r"\input{appendix_rare_fast_counterexample_rev8}") == 1

out.write_text(s, encoding="utf-8")
print(f"generated {out}")
