# WP8 — Bosonic Stam metric audit: why it does not close the SLD-QFI problem

**Date:** 2026-08-19

## Question

Can the bosonic quantum Stam/Fisher-information inequality be used to extend the tight Gaussian WP8 displacement-QFI theorem to arbitrary non-Gaussian detector pointer states?

## Primary sources checked

- R. König and G. Smith, *The entropy power inequality for quantum systems*, IEEE Trans. Inf. Theory 60, 1536–1548 (2014), arXiv:1205.3409.
- G. De Palma and D. Trevisan, *The conditional Entropy Power Inequality for bosonic quantum systems*, Commun. Math. Phys. 360, 639–662 (2018), arXiv:1706.00440.
- F. Hiai and M. B. Ruskai, *Contraction coefficients for noisy quantum channels*, J. Math. Phys. 57, 015211 (2016), arXiv:1508.03551.

---

# 1. The Fisher information in the EPI proof is not the UPRP SLD QFI

König–Smith explicitly describe the information quantity used in their quantum de Bruijn identity and beam-splitter inequalities as a **divergence-based quantum Fisher information**. It is generated from relative-entropy curvature under phase-space translations.

The UPRP local photodetection metric is instead the **SLD/Bures quantum Fisher information**, because it equals the supremum of classical Fisher information over measurements and therefore directly bounds achievable electrical estimation precision.

These are different monotone quantum metrics in general.

Hiai–Ruskai make this distinction structural: quantum channels admit infinitely many monotone Riemannian metrics, including Bures/SLD and BKM-type metrics, with contraction behavior depending on the metric. The classical uniqueness/order relations do not transfer wholesale to the quantum setting.

Therefore no Stam inequality for a divergence/BKM Fisher information may be relabeled as an SLD-QFI inequality without an explicit comparison theorem in the required direction.

**Status:** VERIFIED from primary sources.

---

# 2. Pure-state singularity kills the direct route

The divergence-based metric has a decisive problem for photodetection.

For quantum relative entropy,

\[
D(\rho\|\sigma)=+\infty
\]

whenever the support of `rho` is not contained in the support of `sigma`.

Let

\[
\rho=|\psi\rangle\langle\psi|
\]

be a pure state and let

\[
\rho_\theta
=U_\theta\rho U_\theta^\dagger
\]

be any nontrivial infinitesimal displacement/translation such that `|psi_theta>` is not the same ray as `|psi>`.

Both states have rank one and distinct supports. Therefore for every nonzero `theta`,

\[
\boxed{D(\rho\|\rho_\theta)=+\infty.}
\]

Consequently a relative-entropy-curvature/divergence Fisher information is singular or infinite on such pure translated families.

This includes the states central to UPRP:

- coherent optical source states;
- vacuum detector pointers;
- pure squeezed-vacuum pointers.

By contrast their SLD displacement QFI is finite.

Thus the divergence-based metric is not merely numerically different; it is **qualitatively singular in exactly the pure-state limits needed for the photodetector theorem**.

**Status:** PROVED from the support condition for quantum relative entropy.

---

# 3. Why the inverse Stam form still does not rescue the UPRP bound

One might hope that an inverse-Fisher Stam inequality remains useful when one input Fisher information is infinite. Formally, the reciprocal of an infinite input information contributes zero.

But this does not provide the desired resource-complete SLD theorem:

1. coherent/vacuum and squeezed-vacuum inputs can all have divergent divergence-based translation information;
2. the resulting bound can become vacuous precisely in the low-noise limits where UPRP requires a finite SLD result;
3. even if the divergence-based output Fisher information is bounded, converting that bound to the SLD output requires a metric-ordering statement, while normalizing by the **finite SLD input QFI** introduces a mismatch that can be arbitrarily severe near rank-deficient states;
4. the exact trine-POVM result in WP7 already demonstrates that quantum information contractions depend strongly on the chosen metric.

The Stam machinery is therefore not an honest substitute for the SLD calculation.

---

# 4. Decision

\[
\boxed{
\text{Bosonic divergence-Fisher Stam inequality}
\not\Rightarrow
\text{the required UPRP SLD-QFI theorem.}
}
\]

**Status: REJECTED as the direct non-Gaussian SLD-closure route.**

The EPI/Stam literature remains relevant for entropy and divergence-based resource bounds, but it must not be used to claim the tight SLD displacement theorem has been generalized.

---

# 5. What survives

The strongest clean SLD results remain:

1. the exact single-mode Gaussian free-energy theorem in `WP8_FREE_ENERGY_GAUSSIAN_CLOSURE.md`;
2. the broader but looser arbitrary-pointer variance/energy theorem in `WP7_GENERAL_APPARATUS_QFI_BOUND.md`.

The gap between these is now a well-defined open problem:

> Find the tight maximum SLD displacement QFI after passive mixing of a coherent signal with an arbitrary non-Gaussian pointer constrained by finite nonequilibrium free energy.

Alternative routes should work directly with SLD/Bures geometry, fidelity, or the measured classical FI rather than importing divergence-based Fisher information.

---

# 6. Next candidate routes

- direct variational optimization of SLD displacement QFI under a relative-entropy/free-energy constraint;
- fidelity/Bures bounds under passive beam-splitter convolution;
- extremality theorems proving or disproving Gaussian optimality for displacement-QFI under a free-energy constraint;
- explicit non-Gaussian counterexample search (Fock superpositions, cat states, grid-like states) at matched free energy;
- mode-restricted finite-dimensional semidefinite/numerical optimization to discover the likely extremizer before attempting proof.
