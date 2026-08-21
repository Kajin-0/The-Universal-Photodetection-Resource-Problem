# The Universal Photodetection Resource Problem

## Research question

**What physical resources are sufficient to bound how much temporal information a photodetector can transfer from an incident optical field into an accessible electrical/event record, and which proposed resource sets fail by explicit counterexample?**

The project began as a search for a detector-independent sensitivity–bandwidth–temperature law. The research now shows that such a scalar law is too broad unless the detector/output class and hidden dynamical resources are specified.

This repository is theoretical/analytical. Numerical calculations are used for validation and calibration; experiments, fabrication, procurement, and laboratory campaigns are not required next steps.

Active branch: `agent/uprp-core-theorem-round10`.

## Current publication split

### Paper 1 — Rev11 frozen

Paper 1 develops a temporal-information resource theory for autonomous low-overlap marked photodetection event channels.

Core transfer:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

For arbitrary finite weak temporal waveform families,

`[F_out]_{ab}=Phi0/(2*pi) int G(omega)S_a*(omega)S_b(omega)domega`.

Pointwise ordering of `G` is necessary and sufficient for local Fisher dominance over every admitted weak temporal waveform task in the theorem class.

For square-integrable timing densities,

`B_FI=R2/(4 eta)<=H/(4 eta)`.

For one unresolved mark,

`B_FI=int_0^infty |H(2*pi*f)|^2 df=B_ENBW`.

Rev11 explicitly recognizes this single-mark scalar integral as conventional one-sided equivalent noise bandwidth; the novelty claim is narrower and lies in the event-registration/Fisher interpretation, retained-mark spectrum, resource identities/bounds, and waveform ordering.

The published-IRF demonstration using Spinelli et al. 1998 gives an approximate full-shape ranking reversal:

- MCP FWHM `25 ps`, digitized `B_FI~5.977 GHz`;
- DJ-SPAD FWHM `35 ps`, digitized `B_FI~9.160 GHz`;
- ratio `B_FI(DJ)/B_FI(MCP)=1.533`.

Rev11 is technically validated and scientifically frozen by default. Remaining submission blockers are factual/personal metadata and compliance declarations.

### Paper 2 — active research frontier

Paper 2 removes the independent-event restriction and treats the detector as an arbitrary parameter-independent autonomous stochastic channel from the full incident Poisson trajectory to the complete accessible output record.

The current organizing theorem is:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

`0<=G<=1` a.e.,

where the scalar Fisher multiplier is forced by time-translation covariance of the detector channel rather than by an independent single-event delay kernel.

Candidate message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The mathematical ingredients—conditional-score projection, Fisher data processing, translation-invariant operator theory—are standard. The research question is whether their photodetection-channel synthesis and hidden-memory consequences are genuinely new and physically useful.

## Strongest active Paper-2 results

### Continuous deterministic Type-II spectral escape

For ideal deterministic paralyzable dead time at the classical paralysis maximum `lambda*tau=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every nonzero temporal frequency,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`, a rigorous complete-record lower bound is `0.516975...`; independent Volterra calculation gives about `0.52814`.

Thus the complete stationary record can be locally blind to a uniform intensity perturbation while retaining substantial information about every nonzero temporal mode.

### Deterministic recovery is an information-singular boundary

For generalized iid Type-II recovery duration `T` with mean `m`, every recovery law shares the conventional mean curve

`r(lambda)=lambda exp(-lambda m)`.

Under stated renewal-DQM/window regularity, at the common mean-rate maximum `lambda*m=1` the static complete-record Fisher retention satisfies

`G_DC=0 iff T=m almost surely`.

The preferred proof uses bounded interval Laplace statistics and the stop-loss functional `E[(T-t)_+]`, avoiding an unnecessary pointwise-density argument.

### Recovery mean and variance are not resource-complete

Two exact recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and therefore the same entire conventional saturation curve, yet different timestamp information channels. A common timestamp coarse-graining has zero FI for one law and positive normalized FI `~0.0044352` for the other. Converged full static FI differs by about `8.78%`.

Thus mean plus variance/CV are insufficient to characterize recovery information.

### Visible-event high-frequency Cesaro residue

For an exact-timestamp event selector whose conditional-score covariance measure has form

`Gamma_M=r delta_0+nu`,

with finite-total-variation `nu` and no zero atom,

`lim_{Omega->infty} 1/[(b-a)Omega] int_{aOmega}^{bOmega}G(omega)domega=r/lambda`

for every fixed `0<a<b`.

Atomless corrections give high-frequency mean-square/Cesaro convergence; Rajchman/L1 corrections give the stronger pointwise limit.

The physical interpretation is that directly visible incident timestamps contribute a zero-lag Fisher covariance atom whose coefficient fixes the high-frequency averaged residue.

## Important prior-art corrections

The following are established and must not be claimed as new:

- random Type-II/paralyzable recovery and `M/G/infinity` modeling;
- busy-cycle renewal theory and the generalized random-recovery renewal density;
- random-paralyzable pair-correlation formulas;
- `g_Y^(2)(t)=F(t)exp[lambda E[(T-t)_+]]`;
- generic pair-correlation dead-time inversion;
- infinite-server service/recovery inference;
- renewal-process FI and generic timing-vs-rate information comparisons;
- conditional-score/Fisher data processing;
- function-valued FI operators;
- translation-invariant Fourier multipliers;
- stationary random-measure spectral theory and Wiener atom theorems;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

The exact pair-correlation identity originally highlighted in WP15 is already contained in Apanasovich & Paltsev (JOSA B, 1995) after stationary specialization and is now treated as supporting material only.

Afanaseva & Mikhailova (1973) and older infinite-server output-identifiability literature remain important historical checks before any priority claim for the Type-II recovery singularity theorem.

## Current research gates

Before drafting Paper 2:

1. finish the historical inverse-output audit;
2. audit the visible-event covariance-atom/Cesaro theorem against dependent-thinning, missing-event, stationary-score, and information-spectrum literature;
3. harden the renewal-DQM/window-censoring scope for atomic and heavy-tailed recovery laws.

## Where to resume

Read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
4. `ROADMAP.md`

The repository is intended to be sufficient for context recovery without relying on prior chat history.
