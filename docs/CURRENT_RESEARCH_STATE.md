# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

The repository now has two clearly separated publication tracks:

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** active theoretical research program on arbitrary autonomous detector channels, high-flux hidden memory, Type-II recovery identifiability, and information-spectral resource structure.

The active scientific frontier is Paper 2. New agents must not infer the current research state from the Paper-1 submission files alone.

## Read first

### Project routing

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`

### Current Paper-2 theorem/proof state

4. `paper2/notes/WP20_CESARO_VISIBLE_EVENT_RESIDUE.md`
5. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
6. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
7. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
8. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
9. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

### Paper-1 submission state

10. `notes/RESEARCH_LOG_ROUND21_ENBW_POSITIONING.md`
11. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV11.md`
12. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV11.md`

---

# Paper 1 — frozen Rev11

Current preferred submission candidate: **Rev11**.

The first-paper theorem class remains autonomous/time-translation-invariant, independent-event/low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core exact transfer:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Phi0/(2*pi) int G(omega)S_a*(omega)S_b(omega)domega`.

For square-integrable timing densities:

`B_FI=R2/(4 eta)<=H/(4 eta)`.

For one unresolved mark:

`B_FI=int_0^infty |H(2*pi*f)|^2 df=B_ENBW`.

The conventional ENBW identity and first-order `pi/2` ratio are explicitly acknowledged as prior art.

### Validation

Canonical Rev11:

- 33 pages;
- source SHA-256 `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

Do not add Paper-1 theory, literature, or examples without a concrete defect or referee request.

Remaining Paper-1 blockers are factual/personal only: author/order, affiliation, corresponding email, ORCID, truthful AI disclosure, funding/conflict/prior-submission declarations.

---

# Paper 2 — active frontier

## 1. General autonomous-channel Fisher spectrum — WP10/WP17

For homogeneous Poisson baseline flux `Phi0`, the source tangent score is

`S_u=int u(t)[N(dt)-Phi0 dt]`.

Any parameter-independent detector channel maps this to

`S_u^out=E[S_u|Y]`,

which defines a positive contraction `A_K` on scalar `L2(R)`.

If the detector is autonomous/time-translation covariant, `A_K` commutes with temporal translations and therefore is a Fourier multiplier:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

WP17 closes the main formal proof gaps using standard-Borel trajectory spaces, kernel randomization, DQM under statistics, the classical `L2` translation-invariant multiplier theorem, and narrowband wavepacket limits.

Paper 1 is recovered exactly as the marked-Poisson special case.

Current status: proof architecture is strong; novelty/positioning remains under hostile audit.

## 2. Continuous deterministic Type-II spectral survival — WP07

For deterministic paralyzable dead time `tau`, input rate `lambda`, `rho=lambda*tau`, output rate `r=lambda exp(-rho)`.

At the classical paralysis maximum `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`,

`G_1>=exp(-1)(1+4/pi^2)=0.516975...`.

Independent complete-record Volterra numerics give about `0.52814`.

This is the strongest current concrete physical spectral theorem.

## 3. General iid Type-II recovery singularity — WP13/WP14/WP18

For iid recovery duration `T` with mean `m`, every recovery law has the same conventional mean curve

`r(lambda)=lambda exp(-lambda m)`.

The classical busy-cycle renewal density is

`U_lambda(t)=lambda F(t)exp[-lambda A(t)]`,

`A(t)=E[min(T,t)]`.

These formulas are prior art.

Define the homogeneous static FI retention per unit time `G_DC` separately from WP10's a.e.-defined spectral multiplier.

Under renewal DQM/window regularity,

`G_DC=(r/lambda) I_D`.

At `lambda*m=1`, all rate/count FI vanishes. WP18's preferred bounded-Laplace-statistic proof yields

`G_DC=0 iff T=m almost surely`

under the stated regularity.

The recovery-shape witness uses

`W_s=int exp(-s t)U_*(t)E[(T-t)_+]/m dt`

and gives

`G_DC >= (4/e) W_s^2/(1+u_s)^4`.

Thus deterministic recovery is the unique zero/minimizer of complete static FI at the common mean-rate maximum within the regular fixed-mean iid-recovery class.

For fixed known recovery law, complete stationary Lambert-W branch aliasing occurs iff recovery is deterministic; treat this as an identifiability corollary, not new queueing theory.

## 4. Mean/variance insufficiency — WP19

Two exact recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical entire conventional saturation curve `r(lambda)=lambda exp(-lambda)`, but different registered-timestamp information channels.

A common interval coarse-graining has zero FI for one law and normalized per-time FI

`~0.00443520488427`

for the other at `lambda=1`.

Converged full static values are

`G_DC^A~0.01765400847`,

`G_DC^B~0.01920433799`,

about `8.78%` different.

Conclusion: recovery mean plus variance/CV plus the complete conventional mean curve are not resource-complete descriptors of timestamp information.

## 5. Visible-event Cesaro residue — WP20

WP20 supersedes WP08 as the preferred robust general statement.

For an exact-timestamp selector `Y<=N`, suppose the conditional-score covariance measure is

`Gamma_M=r delta_0+nu`,

where `nu` has finite total variation and no atom at zero.

Then the robust high-frequency theorem is

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega}G(omega)domega=r/lambda`

for every fixed `0<a<b`.

If `nu` is atomless, Wiener's theorem gives high-frequency mean-square/Cesaro convergence. If `nu` is Rajchman, for example has an `L1` density, then the pointwise limit `G(omega)->r/lambda` follows.

Interpretation: exact visible timestamps create a zero-lag conditional-score covariance atom whose weight fixes the high-frequency averaged Fisher residue.

## 6. Numerical calibration

At mean recovery `m=1` and `lambda=1`:

- exponential recovery: converged `G_DC~0.06915579`;
- gamma-family values decrease toward the deterministic limit within that family only;
- no universal variance monotonicity is claimed.

The former chat-only gamma/lognormal comparison is superseded by WP19 and must not be used as evidence.

---

# Current novelty boundaries

Classical / must be credited:

- random Type-II/paralyzable recovery and `M/G/infinity` modeling;
- busy-period/busy-cycle renewal formulas;
- the random-recovery renewal density above;
- random-paralyzable pair-correlation formulas;
- `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- generic pair-correlation dead-time inversion;
- infinite-server recovery/service-distribution inference;
- renewal-process FI and generic rate-vs-timing distinctions;
- conditional-score projection / Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory / Wiener atom theorems;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

WP15's central pair-correlation identity is prior art through Apanasovich & Paltsev (1995); WP15 is supporting/operational only.

## Historical risk

Afanaseva & Mikhailova (1973), approximately `On recovering characteristics of some queueing systems from the output flow`, is cited in the direct Type-II lineage but its theorem text has not yet been obtained. Older infinite-server output-identifiability literature also exists.

No priority language is permitted until this history is exhausted as far as feasible.

No verified predecessor has yet been found for:

- `G_DC=0 iff T deterministic` at the universal Type-II mean-rate maximum;
- the WP07 complete-record dynamic escape from static blindness;
- the detector-specific WP20 zero-lag Fisher-covariance interpretation.

---

# Immediate next gates

1. Finish the historical inverse-output audit, especially Afanaseva–Mikhailova and old Type-II/infinite-server identifiability literature.
2. Audit WP20 specifically against dependent thinning, missing-event point-process inference, score spectra, and stationary-channel information literature.
3. Recheck WP18 renewal DQM/window-censoring assumptions for atomic and heavy-tailed recovery laws.
4. Only after those gates decide whether the WP10/WP07/WP18/WP20/WP19 stack has earned Paper-2 manuscript drafting.

---

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed as they occur. Do not allow important project state to exist only in chat.

At minimum, keep synchronized:

- the relevant `paper2/notes/WP*.md` or research log;
- `paper2/AGENTS_PAPER2.md` when recovery order/claims/gates change;
- this file when project-level status changes.
