# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-21**

This repository now contains three distinct research layers:

1. **Paper 1 / Rev11** — scientifically frozen and technically validated; only factual/personal submission metadata remain.
2. **Paper 2 / Rev7** — preferred frozen science draft, locally build-verified and visually inspected.
3. **Grand Challenge program** — active high-risk/high-ceiling theoretical research on universal quantum resources for temporal information transfer.

## Active branch

The current scientific frontier is on:

`agent/temporal-information-resource-law`

The authoritative active handoff is:

`grand_challenge/AGENTS.md`

A replacement agent should read that file before doing new research.

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

this gives the inverse Planck-scale resource law

`boxed: E_bar^+ >= (2/pi) h B q0`.

The constant is sharp as a supremum. WP15 reduces the proof to a positive Mellin-convolution operator whose exact norm is `pi/4`; truncated critical densities proportional to `(1+omega)^(-2)` approach equality.

## Earlier covariant-timestamp law

For the narrower class of reference-free covariant timestamp readouts, WP06-WP08 give the sharper measurement-class-specific law

`int_R G_timestamp(nu) dnu <= 2 E_det^+ / hbar`,

or

`E_det^+ >= h B q`.

WP08 lifts this through arbitrary downstream classical detector memory and shows that finite-energy quantum timing regularizes the ideal infinite-frequency `1/e` plateau of Paper 2's classical deterministic Type-II model.

## Scope and important no-gos

The present strongest theorem concerns **random temporal-distribution encoding of a fixed semibounded-energy excitation**. It is not a universal bound for arbitrary parameter-dependent state engineering.

WP14 gives a decisive no-go for the broader claim: a coherent carrier can acquire arbitrarily high-frequency infinitesimal sidebands while the additional energy enters only at second order. A broader waveform theorem therefore needs an encoding/control/action resource in addition to baseline energy.

Other discarded universal currencies include entropy production alone, ordinary dynamical activity alone, and detector thermodynamic cost inferred from `G` alone.

## Prior-art boundary

Do not claim novelty for generic SLD/QFI, waveform-QFI kernels, time-covariant POVMs, time-translation asymmetry resource theory, Hardy/Gagliardo-Nirenberg inequalities, rearrangement/layer-cake/Mellin analysis, or generic time-energy uncertainty relations.

Close literature includes Tsang-Wiseman-Caves, Marvian-Spekkens, Pocovnicu, Kiukas-Ruschhaupt-Werner, Hall, WAY/asymmetry work, and random-unitary/phase-noise estimation. Targeted searches have not yet found the exact WP10/WP12/WP15 random-time Fisher-mode formula or sharp `pi E/hbar` integrated-transfer law. **Priority is not certified.**

## Immediate active gates

1. Deep priority audit for an exact equivalent of WP10/WP12/WP15.
2. Determine operational attainability of the integrated `pi` coefficient by a single measurement family; per-mode SLDs need not be jointly compatible.
3. Strengthen the independent quantum-marked Poisson-to-field mapping for realistic incoherent optical source models.
4. Explore arbitrary waveform-encoding resource laws only if the required control/action resource can be made noncircular and universal.
5. If priority survives, decide whether WP10-WP15 justify a standalone foundational manuscript.

## Where to resume

Read in this order:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/WP15_GENERAL_DENSITY_PROOF_OF_SHARP_PI_AREA_INEQUALITY.md`
3. `grand_challenge/notes/WP14_COHERENT_FIELD_BASELINE_ENERGY_NO_GO.md`
4. `grand_challenge/notes/WP13_SECOND_QUANTIZED_SCOPE_AND_POISSON_EVENT_EMBEDDING.md`
5. `grand_challenge/notes/WP12_SHARP_CONTINUUM_QUANTUM_MODE_AREA_LAW.md`
6. `grand_challenge/notes/WP11_WP10_FACTOR_AUDIT_AND_PRIOR_ART.md`
7. `grand_challenge/notes/WP10_QUANTUM_RANDOM_TIME_MODE_BUDGET.md`
8. `paper2/AGENTS_PAPER2.md` only if Paper 2 context is needed.

## Documentation discipline

After every material theorem, counterexample, proof repair, prior-art collision, numerical result, or strategy change:

- create/update the relevant `grand_challenge/notes/WP*.md` immediately;
- update `grand_challenge/AGENTS.md` whenever the theorem stack or gates change;
- update top-level `README.md`, `AGENTS.md`, `docs/CURRENT_RESEARCH_STATE.md`, and `ROADMAP.md` whenever the project-level frontier changes;
- ensure `main` advertises the current active branch and current checkpoint.

The repository—not chat history—must remain sufficient for full context recovery.