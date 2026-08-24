# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature publication program — frozen

The three developed temporal-information papers remain separate:

1. PRX Quantum flagship: *Two spectral-resource regimes for autonomous temporal information* — R3 frozen theorem/proof baseline, R4 journal-facing bridge revision.
2. *Spectral Resource Laws for Temporal Fisher Information* — independent broad random-time/spectral-survival paper.
3. PRA dynamical completion: *Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature* — final reviewer-repaired package.

Do not concatenate them. The prior architecture remains recorded in `manuscript/THREE_PAPER_PUBLICATION_ARCHITECTURE_2026-08-23.md`.

## New active program — Paper 4 practical/falsifiability bridge

Working title:

> **Operational benchmarks for temporal information in photodetection**

Goal: express temporal Fisher/resource results through standard photodetector measurements and state explicit falsification conditions.

## WP01 — complete: linear Gaussian Fisher/NEP bridge

For peak optical-power quadratures and a one-sided output-noise PSD,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2|R(f)|^2/S_n(f)`.

With conventional frequency-resolved `NEP(f)=sqrt(S_n(f))/|R(f)|`,

`F_xx/T = 1/NEP(f)^2`,

`Tr F/T = 2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

This establishes inverse-square NEP as the local input-waveform Fisher weighting in the linear stationary Gaussian regime and shows response bandwidth need not equal information bandwidth.

## WP02 — complete: Poisson timestamps and timing jitter

For fractional modulation of an ideal inhomogeneous Poisson rate,

**`Tr F/T=lambda_0`.**

For optical-power quadratures with `lambda_0=eta P_0/(hbar omega_opt)`,

`Tr F_P/T=eta/(hbar omega_opt P_0)`,

which exactly equals the WP01 `2/NEP_shot^2` result for ideal shot noise.

Independent timing jitter `J` attenuates the two-quadrature timestamp Fisher spectrum by

**`|Phi_J(Omega)|^2`**, where `Phi_J` is the jitter characteristic function.

For Gaussian jitter,

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`

and

`f_F,3dB=sqrt(ln 2)/(2 pi sigma_t)`.

Independent dark counts yield `Tr F/T=lambda_s^2/(lambda_s+lambda_d)` before the jitter factor.

## Planned work packages

### WP03 — dead time, recovery, and detector memory

Use standard nonparalyzable/paralyzable or generalized recovery models and connect measurable timestamp Fisher spectra to the existing random-time resource theory. The key target is information present in full timestamps but invisible in mean count-rate saturation curves.

### WP04 — sideband survival-to-synthesis crossover

Use conventional optical modulation and sideband physics. Compare a pre-seeded sideband with a baseline-empty sideband and determine the exact observable that realizes the transition from pre-existing spectral survival to second-order synthesis.

### WP05 — standard Hamiltonian implementation bridge

Translate `V_min=(1/2)Tr C` into at least one textbook resonant exchange model while preserving all scope limitations of the PRA theorem.

### WP06 — integrated falsification matrix

For every headline prediction specify measured inputs, predicted equality/inequality, nuisance/calibration assumptions, statistical test, and an observation that would contradict it.

### WP07 — prior-art/significance gate

Before drafting a manuscript, determine whether the surviving results constitute a publishable fourth paper. Do not force publication if the work is only pedagogical.

## Candidate publication-level targets

WP01–WP02 are a rigorous bridge but likely not sufficient novelty alone. The strongest prospective contributions are:

1. a full-timestamp dead-time/recovery information law that distinguishes detectors with identical conventional count-rate curves;
2. a practical detector-ranking example where responsivity bandwidth or D* mis-ranks devices for a specified temporal-information task while the Fisher/NEP spectrum gives the correct ranking;
3. a measurable survival-to-synthesis sideband crossover with explicit falsification criteria;
4. an integrated analog/event-detector benchmark based on the actual likelihood rather than incompatible technology-specific figures of merit.

## Claim discipline

No novelty claim for NEP/detectivity definitions, matched filtering, generic Fisher sensing, Poisson-process Fisher information, shot-noise formulas, or timing-jitter transfer functions. No experimental validation may be implied without data. No prize-level framing.

## Documentation cadence

Update `practical_temporal_information/notes/`, `practical_temporal_information/AGENTS.md`, and the top-level landing files after each material advance. The repository must remain sufficient for takeover without chat context.
