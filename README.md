# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-21**

This repository contains three distinct research layers:

1. **Paper 1 / Rev11** — scientifically frozen and technically validated; only factual/personal submission metadata remain.
2. **Paper 2 / Rev7** — preferred frozen science draft, locally build-verified and visually inspected.
3. **Grand Challenge program** — active high-risk/high-ceiling theoretical research on quantum resources for temporal information transfer.

## Active branch and checkpoint

The current scientific frontier is on:

`agent/temporal-information-resource-law`

The authoritative active handoff is:

`grand_challenge/AGENTS.md`

The **theorem stack is through WP15**. The latest research checkpoint is **WP16**, a deep priority audit that identifies a classical Hardy–Hilbert collision for the analytic `pi/4` operator constant while leaving the quantum random-time priority question unresolved.

## Current grand question

> For a physically realizable measurement of temporal structure, what fundamental resources constrain source-to-record temporal Fisher-information transfer?

The program is analytical/theoretical and falsification-first. Numerical work is used only for proof checks and calibration. Experiments, fabrication, procurement, and laboratory campaigns are not active requirements.

## Strongest current result — sharp random-time quantum mode-area law

For a normalized nonnegative excitation-frequency density `q(omega)` with finite mean

`omega_bar = int_0^infinity omega q(omega) d omega`,

the maximal source-normalized quantum Fisher retention for a random-time Fourier mode `nu>0` is

`G_Q(nu) = 2 int_0^infinity q(omega) q(omega+nu) / [q(omega)+q(omega+nu)] d omega`,

with even extension to negative `nu`.

WP15 proves, for every finite-first-moment density and without smoothness assumptions,

`boxed: int_0^infinity G_Q(nu) dnu <= (pi/2) omega_bar`,

or equivalently

`boxed: int_R G_Q(nu) dnu <= pi E_bar^+ / hbar`.

For a flat guaranteed temporal-information band,

`G_Q(2*pi*f) >= q0` for `|f|<=B`,

this gives

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum; truncated critical densities proportional to `(1+omega)^(-2)` approach equality.

## WP16 priority correction

WP16 shows that the WP15 kernel

`L(s,t)=2st/(s+t)^3`

and its exact norm

`||T||=pi/4`

are an explicit specialization of established parameterized Hardy–Hilbert integral inequalities with best Beta-function constants. With `lambda=3`, `f(x)=x r(x)`, `g(y)=y r(y)`, the classical best constant is `B(3/2,3/2)=pi/8`; the factor `2` in `L` gives `pi/4`.

Therefore **do not claim mathematical novelty for the sharp operator constant, Mellin diagonalization, or Hilbert-type inequality**. The candidate novelty, if priority survives, is the quantum-statistical and physical synthesis: Fourier-mode estimation of a latent random time distribution, the exact source-normalized mode-retention formula, the `2 nbar` mode budget, the continuum temporal-information interpretation, and detector-independent inheritance.

Targeted searches still have not found an exact predecessor for

`G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

as Fisher retention of the `k`th Fourier coefficient of a random `U(1)` translation distribution, nor the sum rule

`sum_{k>=1}G_Q(k)<=2 nbar`.

**Quantum priority remains uncertified.**

## Earlier covariant-timestamp law

For the narrower class of reference-free covariant timestamp readouts, WP06-WP08 give

`int_R G_timestamp(nu) dnu <= 2 E_det^+ / hbar`,

or

`E_det^+ >= h B q`.

WP08 lifts this through arbitrary downstream classical detector memory and shows that finite-energy quantum timing regularizes the ideal infinite-frequency `1/e` plateau of Paper 2's classical deterministic Type-II model.

## Scope and important no-gos

The present strongest theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy excitation**. It is not a universal bound for arbitrary parameter-dependent state engineering.

WP14 gives a decisive no-go for the broader claim: a coherent carrier can acquire arbitrarily high-frequency infinitesimal sidebands while the additional energy enters only at second order. A broader waveform theorem therefore needs an encoding/control/action resource in addition to baseline energy.

Other discarded universal currencies include entropy production alone, ordinary dynamical activity alone, and detector thermodynamic cost inferred from `G` alone.

## Prior-art boundary

Do not claim novelty for generic SLD/QFI, waveform-QFI kernels, time-covariant POVMs, time-translation asymmetry resource theory, Hardy/Gagliardo–Nirenberg inequalities, Hardy–Hilbert best-constant inequalities, rearrangement/layer-cake/Mellin analysis, or generic time-energy uncertainty relations.

Close literature includes Tsang–Wiseman–Caves, Marvian–Spekkens, Pocovnicu, Kiukas–Ruschhaupt–Werner, Hall, Yang's Hilbert-type operator literature, WAY/asymmetry work, phase-diffusion/dephasing estimation, and random-unitary/noise-channel estimation.

## Immediate active gates

1. Search specifically for estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on compact groups.
2. Determine whether the harmonic-mean density inequality itself has appeared explicitly; its sharp operator constant is already classical.
3. Determine operational attainability of the integrated `pi` coefficient by a single measurement family; per-mode SLDs need not be jointly compatible.
4. Strengthen the independent quantum-marked Poisson-to-field mapping for realistic incoherent optical source models.
5. Explore arbitrary waveform-encoding resource laws only if the required control/action resource can be made noncircular and universal.
6. If priority and operational interpretation survive, decide whether WP10–WP15 justify a standalone foundational manuscript.

## Where to resume

Read in this order:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP16_DEEP_PRIORITY_AUDIT_RANDOM_TIME_QFI_AND_HARDY_HILBERT_COLLISION.md`
3. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
4. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
5. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
6. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
7. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
8. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
9. `paper2/AGENTS_PAPER2.md` only if Paper-2 context is needed.

## Documentation discipline

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

- create/update the relevant `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md` whenever the theorem stack or gates change;
- update top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md` whenever the project-level frontier changes;
- keep `PROBLEM.md` and `grand_challenge/README.md` current enough not to misroute a replacement agent;
- ensure `main` advertises the current active branch and current checkpoint.

The repository—not chat history—must remain sufficient for full context recovery.