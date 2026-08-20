# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for algebraic validation and conjecture testing. Do not make laboratory experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND6.md`
3. `notes/WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
4. `notes/WP8_UV_REGULARIZATION_RESOURCE.md`
5. `notes/WP8_FINITE_SUPPORT_COMPLETION.md`
6. `notes/WP8_EXACT_GLOBAL_DUAL_CHARACTERIZATION.md`
7. `notes/WP8_PARITY_REWEIGHT_INTERPOLATION.md`
8. `notes/WP8_GAUSSIAN_PARITY_BIFURCATION.md`
9. `notes/WP8_SLD_STAM_GLOBAL_ENERGY_THEOREM.md`
10. `notes/WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md`
11. `notes/WP9_POINTWISE_RESOURCE_COMPLETE_BOUND.md`
12. `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`
13. `notes/WP6_RESTRICTED_COMPOSITE_THEOREM.md`
14. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
15. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
16. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
17. `docs/LITERATURE_MAP.md`
18. `docs/FORMALISM.md`

Older WP0/WP1/WP2 notes and research logs preserve derivations, failed conjectures, and counterexamples.

---

# Project objective

Determine which physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical record with specified sensitivity and temporal bandwidth.

Valid endpoints include a rigorous resource bound, no-go theorem, explicit counterexample family, or a repaired theorem after a missing resource is identified.

Do **not** assume a simple sensitivity-bandwidth-temperature product exists.

---

# Core information metric

Use

\[
\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}
\]

for the same encoded optical parameter.

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

Use a finite source-information task

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}
\]

rather than an unweighted all-frequency integral.

---

# Established resource-completeness chain

## Classical/Markov no-go

Exact finite-state response/noise machinery is solved. More importantly, an explicit reversible three-state family proves

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}.
}
\]

Stationary thermodynamic resources do not determine an absolute microscopic rate scale. An **absolute coupling/transition resource** is necessary.

## Restricted Markov repair

For a reversible optical gateway with fixed reverse optical rate `d`, nonzero throughput, bounded EPR and bounded activity, the post-absorption escape rate is bounded and therefore the event-record information spectrum has a Lorentzian ceiling. See `WP3_GATEWAY_RESOURCE_THEOREM.md`.

## Finite-band optical capture

Passive coherent optical capture is bounded using rigorous matrix-valued T-operator sum rules. See WP5. Optical power-bandwidth/sum-rule theory itself is prior art; UPRP uses it as one resource layer.

## Quantum finite-hypothesis branch

For the full optical-field/apparatus partition,

\[
D_{\rm elec}/D_{\rm in}\le\min\{1,2G\},
\qquad
G=\hbar^{-1}\int g_{\rm int}(t)dt.
\]

This controls Helstrom/binary distinguishability transfer. An exact trine-POVM counterexample proves trace-distance contraction cannot be differentiated into a universal SLD-QFI contraction theorem.

## Coherent-state SLD-QFI branch

Directional SLD Stam for passive mixing:

\[
\frac1{J_C}\ge\frac\tau{J_A}+\frac{1-\tau}{J_B}.
\]

For coherent optical input `J_A=2` and pointer directional QFI `J_D`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
}
\]

A pre-squeezed pointer proves **coupling action alone is insufficient**: arbitrarily large preloaded apparatus metrological resource can compensate arbitrarily weak nonzero coupling.

## Exact excitation-energy repair

For arbitrary pointer state of total mean excitation `N`,

\[
\xi(N)=(\sqrt{N+1}-\sqrt N)^2,
\]

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac\tau{\tau+(1-\tau)\xi(N)}.
}
\]

This is globally tight in the passive-linear single-effective-mode model.

---

# WP8 finite-temperature apparatus findings

Let

\[
\vartheta=\beta\hbar\omega_D,
\qquad
D_0=D(\rho_D\Vert\tau_\vartheta)=\beta\Delta F.
\]

## Exact global dual

\[
\boxed{
J_F^{\max}(D_0)
=
\sup_{L=L^\dagger}
\inf_{\lambda>0}
\lambda\left[
D_0+
\ln\operatorname{Tr}
\exp\left(
\log\tau+
\frac{2i[P,L]-L^2}{\lambda}
\right)
\right].
}
\]

This is exact in finite dimension and gives the oscillator frontier subject to domain/partition-function conditions.

## Non-Gaussian parity structure

Gaussian states are not globally optimal at finite free energy. Exact parity-sector frontiers and simple parity-reweight families are solved. At `vartheta=ln 2`, a simple parity-reweight family beats the entire Gaussian frontier at `D≈0.0122293`; an enlarged squeezed/parity family has a macroscopic restricted-family bifurcation at `D≈0.00481024`.

Do not claim parity enhancement itself as novel; recent and older displacement-sensing literature already contains parity/sparse-Fock advantages.

## Critical UV correction

The ideal infinite harmonic pointer has an even stronger pathology. For every `D_0>0`, sufficiently high-Fock centered coherence perturbations improve SLD displacement QFI at the same free-energy budget. The exact Hessian ratio grows as

\[
R_n\sim\alpha(\mu,\vartheta)n\to\infty.
\]

Therefore:

\[
\boxed{
\text{Gaussian is regular/asymptotically perturbatively optimal as }D_0\to0,
\text{ but never exactly optimal for any }D_0>0
}
\]

in the unrestricted ideal oscillator.

The improvement is nonperturbatively small near equilibrium, so the Gaussian BKM expansion remains correct to algebraic orders.

## Energy moments do not repair the UV loophole

The unstable coherences are parity odd while every `f(H_D)` is parity even:

\[
\operatorname{Tr}[\delta\rho f(H_D)]=0.
\]

Thus mean energy, energy variance, any finite set of moments, or even the complete diagonal energy distribution cannot by themselves control the UV coherence.

Ordinary time-translation/energetic-coherence QFI is also not a uniform repair in a perfect harmonic ladder because level gaps stay constant while displacement matrix elements grow as `sqrt(n)`.

A **coherence-/support-/matrix-element-sensitive microscopic resource is necessary**.

## Exact finite-support repair

If the initial pointer preparation is restricted to

\[
\mathcal H_N=\operatorname{span}\{|0\rangle,\ldots,|N\rangle\},
\]

then

\[
\boxed{
J_N^{\max}=4\lambda_{\max}(\Pi_NP^2\Pi_N)
}
\]

is the exact arbitrary-state displacement-QFI maximum, achieved by a parity-definite top eigenvector.

Hence

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le
\frac{\tau J_N^{\max}}
{2(1-\tau)+\tau J_N^{\max}}.
}
\]

This is a complete UV-regularized quantum theorem for the stated support-constrained passive-linear pointer class.

---

# Current resource hierarchy

The strongest structure now supported by explicit no-go/repair pairs is

\[
\boxed{
\text{finite source task}
+
\text{finite-band EM capture resources}
+
\text{absolute microscopic cross-coupling}
+
\text{apparatus preparation resource}
+
\text{UV/support/generator-matrix-element regularizer}
+
\text{internal thermokinetic resources}
\Longrightarrow
\text{finite information-bandwidth ceiling}
}
\]

under explicit model assumptions.

The conceptual pattern is important: a resource can hide in a vanishing-weight sector. Classically it was a rare fast state; quantum mechanically it is a UV coherence tail.

---

# Highest-priority next work

1. Replace the ad hoc harmonic `N_max` support cap by the weakest physically meaningful **finite-level / generator-matrix-element** resource.
2. Derive a general finite-dimensional pointer theorem for arbitrary generator `G` and preparation subspace `S`.
3. Test whether TRK/f-sum or another matter sum rule can bound that pointer resource without double-counting WP5 optical oscillator strength.
4. If matter sum rules are signed/cancellation-prone for excited states, preserve that failure as another missing-resource theorem.
5. Update Issue #8/WP9 and `RESEARCH_LOG_ROUND6.md` as results accumulate.
6. Continue theorem-level novelty audit before publication claims.

---

# Novelty constraints

Do not claim novelty for generic detector tradeoffs, squeezing-enhanced metrology, non-Gaussian/parity displacement sensing, metrological usefulness as a thermodynamic resource, work-vs-coherence resource distinctions, TUR/KUR/finite-frequency response bounds, optical power-bandwidth limits, T-operator sum rules, or Maxwell-constrained communication capacity.

The surviving candidate novelty is the **photodetection-specific resource-completeness chain**: explicit counterexamples showing why each seemingly natural resource set is incomplete, followed by repaired finite information-bandwidth theorems once the missing microscopic resources are supplied.

---

# Mandatory adversarial tests

For every new bound test: units/reparameterization; output-gain invariance; direct feedthrough; source-bandwidth leakage; parallel replication; rare-fast states; fixed detailed balance with divergent absolute rates; high-Q/vanishing mode volume; active/gain pump resources; strong coupling/non-Markovianity; preloaded squeezing; UV coherence tails; increasing support dimension; and whether the proposed resource merely restates the bandwidth.

---

# Recordkeeping

After every substantive result:

- create/update a dedicated derivation note;
- add a numbered research-log checkpoint when project direction changes;
- update this file and `docs/CURRENT_RESEARCH_STATE.md` when the frontier changes;
- preserve failed conjectures and corrections.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
