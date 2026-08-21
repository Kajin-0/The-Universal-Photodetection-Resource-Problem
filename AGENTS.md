# AGENTS.md

## Purpose

Durable project handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Active branch: `agent/uprp-core-theorem-round10`.

Research is analytical/theoretical. Numerical analysis is used for validation, calibration, and published-data analysis. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Critical project split

There are now two publication tracks:

1. **Paper 1 / Rev11** — scientifically frozen, technically validated, awaiting factual/personal submission metadata.
2. **Paper 2** — active research frontier: arbitrary autonomous detector channels, high-flux hidden memory, Type-II information spectra, recovery-law identifiability, and resource-completeness no-go results.

Do not assume the active scientific state is contained in the Paper-1 files.

## Read first — active research

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
4. `ROADMAP.md`
5. `paper2/notes/WP20_CESARO_VISIBLE_EVENT_RESIDUE.md`
6. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
7. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
8. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
9. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
10. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

## Paper 1 / Rev11 — frozen publication state

Preferred first-paper submission candidate: **Rev11**.

The theorem class is autonomous/time-translation-invariant, independent-event/low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining complete accessible primary-event marks.

Core exact transfer:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Phi0/(2*pi) int G(omega)S_a*(omega)S_b(omega)domega`.

For square-integrable timing densities:

`R2=2 int kappa(dm) int f_m(t)^2 dt`,

`B_FI=R2/(4 eta)<=H/(4 eta)`.

For one unresolved mark,

`B_FI=int_0^infty |H(2*pi*f)|^2 df=B_ENBW`.

Do not claim novelty for that scalar ENBW integral or the familiar first-order `pi/2` ratio.

Canonical Rev11:

- 33 pages;
- source SHA-256 `fe966f4ab3fa067bb94d200ed09605a1ed3a2cdef9b4488fd0d18a55e95ccb6e`;
- PDF SHA-256 `9eedbf562ed5fa70b78a8c1c63627e1c578f149074f7f25f3fd3988c8668ecef`.

PRApplied Rev11:

- 33 pages;
- PDF SHA-256 `d9e4a3330543106a272d4aa7b26cf6187bbd2f6ef170db4a8927b06edb824db7`;
- package ZIP SHA-256 `b9f1abff76bbcc7a97ca8b2c3038f1e44e5adbb68f230cdb7d13c02431b6183e`.

Remaining Paper-1 blockers are human metadata/compliance only: author/order, affiliations, corresponding email, ORCID, truthful AI disclosure, funding/conflict/prior-submission declarations.

Do not add more Paper-1 science unless a concrete defect or referee request appears.

## Paper 2 — active theorem stack

### General autonomous-channel theorem — WP10/WP17

For homogeneous Poisson baseline flux `Phi0`, any parameter-independent stochastic detector channel gives output score

`S_u^out=E[S_u|Y]`.

This defines a positive contraction on scalar `L2(R)`. Autonomy/time-translation covariance forces exact Fourier diagonalization:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.

WP17 closes the main formal proof gaps through standard-Borel trajectory spaces, stochastic-kernel randomization, DQM under statistics, the classical `L2` multiplier theorem, and narrowband wavepacket limits.

Candidate message: **spectral completeness is symmetry-driven, not independent-event-driven.**

All abstract statistical/harmonic-analysis ingredients are prior art.

### Continuous Type-II spectral escape — WP07

For deterministic paralyzable dead time at `lambda*tau=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero frequency,

`G_1(infty)=1/e`.

At `omega=pi/tau`, rigorous lower bound `0.516975...`; independent complete-record Volterra value about `0.52814`.

### General iid-recovery Fisher singularity — WP18

For iid recovery `T` of fixed mean `m`, every law has the same conventional curve

`r(lambda)=lambda exp(-lambda m)`.

The renewal density `U_lambda(t)=lambda F(t)exp[-lambda A(t)]` is classical prior art.

For the homogeneous static experiment use `G_DC`, not an unjustified point value of the a.e. WP10 multiplier.

Under renewal DQM/window regularity, WP18's bounded-Laplace-statistic proof yields at `lambda*m=1`:

`G_DC=0 iff T=m almost surely`.

This is currently a serious novelty candidate but priority is not certified.

### Recovery moment insufficiency — WP19

Two exact recovery laws have identical `E[T]=1`, `Var(T)=1/4`, `CV=0.5`, and identical entire conventional saturation curve but different timestamp information channels.

A common coarse-graining has zero FI for one and normalized FI `~0.00443520488427` for the other. Converged full static FI differs by about `8.78%`.

Conclusion: mean and variance/CV are not resource-complete.

### Visible-event residue — WP20

WP20 supersedes the original WP08 as the robust theorem.

If an exact-timestamp selector has conditional-score covariance measure

`Gamma_M=r delta_0+nu`,

with finite-total-variation `nu` and no zero atom, then for every fixed `0<a<b`:

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega}G(omega)domega=r/lambda`.

Atomless `nu` gives mean-square/Cesaro convergence; Rajchman/L1 `nu` gives the pointwise limit.

Interpretation: exact visible timestamps produce a zero-lag Fisher covariance atom whose coefficient fixes the high-frequency averaged residue.

## Mandatory Paper-2 novelty boundaries

Do not claim novelty for:

- random Type-II/paralyzable recovery or `M/G/infinity` modeling;
- busy-period/busy-cycle renewal theory;
- the classical generalized renewal density;
- random-paralyzable pair-correlation formulas;
- `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- pair-correlation dead-time inversion generally;
- infinite-server service/recovery inference generally;
- renewal-process FI or generic timing-vs-rate FI;
- conditional-score projection / Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory / Wiener atom results;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

WP15 is supporting/operational only after the Apanasovich–Paltsev 1995 prior-art correction.

## Historical blocker

Afanaseva & Mikhailova (1973), approximately `On recovering characteristics of some queueing systems from the output flow`, is cited in the direct Type-II lineage but a readable theorem text has not yet been obtained. Older infinite-server output-identifiability literature also exists.

Absence of accessible full text is not evidence of novelty.

## Immediate active work

1. Finish the historical inverse-output audit.
2. Audit WP20's detector-specific covariance-atom/Cesaro formulation against dependent-thinning, missing-event, stationary-score, and information-spectrum literature.
3. Recheck WP18 renewal-DQM/window-censoring assumptions for atomic and heavy-tailed recovery.
4. Decide on Paper-2 manuscript drafting only after those gates.

## Documentation discipline — mandatory

Do not allow material research state to exist only in chat.

After every material theorem, proof repair, prior-art collision, numerical result used in an argument, or change in next-gate decision:

- commit/update the relevant work package or dated research log;
- update `paper2/AGENTS_PAPER2.md` when the active recovery order, novelty hierarchy, or gates change;
- update `docs/CURRENT_RESEARCH_STATE.md` and `ROADMAP.md` when project-level status changes.

A new agent must be able to recover the full active state from the repository alone.
