# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

The repository has two publication tracks:

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** active theoretical program on arbitrary autonomous detector channels, hidden-memory Fisher spectra, Type-II recovery information singularities, and temporal information resources.

The active scientific frontier is Paper 2.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/WP23_CAUSAL_SCORE_MARTINGALE_AND_ATOMIC_MEMORY_PATHS.md`
4. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
5. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
6. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
7. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
8. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
9. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

---

# Paper 1 — frozen Rev11

Preferred submission candidate: **Rev11**. Do not reopen science absent a concrete defect or referee request.

Core independent-event marked transfer:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

For one unresolved mark,

`B_FI=int_0^infty |H(2*pi*f)|^2df=B_ENBW`,

which is conventional ENBW and not claimed as new.

---

# Paper 2 — active frontier

## WP10/WP17 — general autonomous-channel Fisher spectrum

For homogeneous Poisson source baseline `Phi0`, any parameter-independent stochastic detector channel has output score

`S_u^out=E[S_u|Y]`,

where

`S_u=int u(t)[N(dt)-Phi0dt]`.

This defines a positive contraction on scalar `L2(R)`. Autonomy/time-translation covariance diagonalizes it:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

WP17 closes the main formal proof gaps. The mathematical ingredients are standard; contribution must come from detector specialization/consequences.

## WP07 — continuous deterministic Type-II spectral survival

With deterministic paralyzable dead time `tau` and `rho=lambda*tau`, at the paralysis maximum `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for all `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`, analytic lower bound is `0.516975...`; exact complete-record numerics give about `0.52814`.

This remains the strongest concrete physical spectral theorem.

## WP18 — generalized iid Type-II recovery singularity

All iid recovery laws with mean `m` share the classical mean curve

`r(lambda)=lambda exp(-lambda m)`.

Under renewal DQM/window regularity, static retention is

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, count/rate FI vanishes. WP18's bounded-Laplace-statistic proof yields

`G_DC=0 iff T=m almost surely`

under the stated regularity.

Generic output identifiability is classical and cannot be novelty framing.

## WP19 — exact mean/variance insufficiency no-go

Two explicit recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`

and identical `r(lambda)=lambda exp(-lambda)`, but different timestamp information channels.

A common interval coarse-graining has zero FI for one and normalized FI `~0.00443520488427` for the other at `lambda=1`. Full static retentions differ by about `8.78%`.

Mean + variance/CV + conventional mean saturation curve are therefore not resource-complete.

## WP21 — historical inverse-output audit

Generic queue-output identifiability was established literature by at least 1965 and textbook material by 1982. Kovalenko's `M/G/1` output-only reconstruction already exhibits a generic-identifiable / exceptional-nonrecoverable service-law structure. Afanaseva & Mikhailova (1973) remains an inaccessible direct Type-II-lineage historical blocker.

The historical gate is closed for manuscript strategy but not priority certification.

Do not claim generic identifiability, output reconstruction, or exceptional information-degenerate service laws as new.

## WP22 — abstract conditional-score covariance-atom theorem

Let the complete output score admit a centered stationary random measure `M` with covariance measure

`Gamma_M=a delta_0+nu`,

where `nu` has finite total variation and `nu({0})=0`.

Then, in this regularity class,

`lambda G(omega)=a+nu_hat(omega)`

and for every fixed `0<a0<b0`,

`lim_{Omega->infty} 1/[(b0-a0)Omega] int_{a0Omega}^{b0Omega} G(omega)domega=a/lambda`.

Thus the robust high-frequency invariant is the **zero-lag conditional-score covariance atom**, normalized by source rate.

If `nu` is atomless, Wiener gives high-frequency mean-square convergence. If `nu` is Rajchman, pointwise convergence follows.

For a regular exact-timestamp selector `Y<=N` of rate `r`, diffuse posterior hidden-event mean plus Palm/field regularity imply `a=r` and residue `r/lambda`.

Important: `Y<=N` alone does not prove `a=r`.

## WP23 — causal score martingale and atomic memory paths

Standard counting-process likelihood gives

`S_u^Y=int h_t[u](dY_t-q_tdt)`,

`F_Y[u,v]=E int q_t h_t[u]h_t[v]dt`.

For a causal exact-timestamp selector with

`q_t^epsilon=lambda_epsilon(t)alpha_t^epsilon`,

`h_t[u]=u(t)+B_t[u]`,

where `B` is the causal hidden-state/acceptance response.

A key adversarial result is that **causality alone does not imply residue `r/lambda`**. For an abstract exact delayed memory term

`B_t[u]=c u(t-tau)`,

`G(omega)` contains

`|1+c exp(-i omega tau)|^2`,

whose high-frequency band average contains `1+c^2`. The delayed atomic timing path self-correlates into an additional zero-lag Fisher covariance atom.

Therefore the preferred physical interpretation is:

> **high-frequency Cesaro Fisher retention measures total atomic timing-path energy in the conditional score.**

Immediately visible event timestamps are one atomic path. Perfectly sharp delayed timing memories can add others. Diffuse/smoothing memory averages away under the WP22 regularity.

In an idealized deterministic score impulse response

`k(dt)=sum_j c_j delta_{tau_j}(dt)+k_c(t)dt`,

with sufficiently diffuse finite-energy `k_c`,

`lim <G>_high=(r/lambda)sum_j |c_j|^2`.

For regular exact-timestamp selectors the immediate path has `c_0=1`. Additional exact delayed paths add to the residue.

Do not replace WP22's non-atomic/diffuse memory assumptions merely by “causal.”

---

# Current novelty hierarchy

1. **WP10/WP17:** general autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. **WP07:** deterministic Type-II complete static blindness with positive FI at every nonzero frequency and residue `1/e`.
3. **WP18:** deterministic recovery as the unique regular static Fisher-singular iid Type-II law at the common mean-rate maximum.
4. **WP22/WP23:** conditional-score covariance-atom theorem and atomic timing-path interpretation.
5. **WP19:** exact resource no-go showing mean and variance are insufficient.

Standard/prior art and not claimable: conditional-score projection, Fisher data processing, counting-process innovation likelihoods, martingale isometry, point-process Fisher kernels, Bartlett spectra, Campbell/Palm formulas, Fourier multipliers, Wiener/Rajchman theory, random Type-II busy-cycle formulas, pair correlations, generic dead-time FI, generic queue-output identifiability.

---

# Immediate next gates

1. Continue targeted novelty audit of WP22/WP23 against classical counting-process likelihood/innovation theory, point-process score spectra, Bartlett spectra, neural frequency-resolved information, and photodetection dead-time FI.
2. Search specifically for a predecessor connecting the **zero-lag atom of a conditional/efficient score process** to a high-frequency Fisher-information residue, or interpreting exact delayed score paths as additive atomic information resources.
3. Determine whether an ordinary event-driven selector class gives a natural microscopic condition guaranteeing non-atomic memory; do not force a theorem if the condition merely restates diffuseness.
4. Recheck WP18 renewal DQM/window-censoring assumptions for atomic and heavy-tailed recovery laws.
5. Then decide whether the WP10/WP07/WP18/WP22-WP23/WP19 stack has earned manuscript drafting.

---

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed as they occur. Keep `paper2/AGENTS_PAPER2.md` and this file synchronized with the active frontier.
