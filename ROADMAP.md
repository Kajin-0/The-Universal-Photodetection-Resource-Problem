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

Goal: express the abstract temporal-information results through standard photodetector measurements and state explicit falsification conditions.

This is not a new generic resource-theory layer. It is justified only if it produces nontrivial, experimentally legible consequences beyond a tutorial restatement.

## WP01 — complete: linear Gaussian Fisher/NEP bridge

For peak optical-power quadratures and a one-sided output-noise PSD,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2|R(f)|^2/S_n(f)`.

With conventional frequency-resolved

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

this becomes

`F_xx/T = 1/NEP(f)^2`,

`Tr F/T = 2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

WP01 also establishes a standard-physics distinction between responsivity bandwidth and task-specific Fisher-information bandwidth. They agree for locally flat output noise but need not agree for colored or transfer-correlated noise.

Authoritative note:

`practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`.

## Planned work packages

### WP02 — Poisson timestamps and timing jitter

Derive from the point-process likelihood:

- ideal two-quadrature Fisher rate for weak sinusoidal fractional modulation;
- exact attenuation under independent timestamp jitter using the jitter characteristic function;
- finite-window/end-effect assumptions;
- practical extraction from timestamp records.

### WP03 — dead time, recovery, and detector memory

Use standard nonparalyzable/paralyzable or generalized recovery models and connect measurable timestamp Fisher spectra to the existing random-time resource theory. Identify predictions that differ from mean-count saturation curves.

### WP04 — sideband survival-to-synthesis crossover

Use conventional optical modulation and sideband physics. Compare a pre-seeded sideband with a baseline-empty sideband and determine the exact observable that realizes the transition from pre-existing spectral survival to second-order synthesis.

### WP05 — standard Hamiltonian implementation bridge

Translate `V_min=(1/2)Tr C` into at least one textbook resonant exchange model such as a beam-splitter/frequency-conversion Hamiltonian, while preserving all scope limitations of the PRA theorem.

### WP06 — integrated falsification matrix

For every headline prediction specify:

- measured inputs;
- predicted equality/inequality;
- nuisance/calibration assumptions;
- statistical test;
- observation that would contradict the model or resource law.

### WP07 — prior-art/significance gate

Before drafting a manuscript, determine whether the surviving results constitute a publishable fourth paper. Do not force publication if the work is only pedagogical.

## Candidate high-value practical result

A potentially important direction is a task-specific information bandwidth based on

`|R(f)|^2/S_n(f) = 1/NEP(f)^2`

rather than responsivity alone. A standard linear filter that attenuates signal and dominant pre-filter noise equally can have a finite responsivity 3-dB point while preserving narrowband Fisher information until additive readout noise becomes important. This could provide a physically transparent example of why bandwidth alone does not rank temporal sensing performance.

Novelty of this framing is not yet established.

## Claim discipline

- no novelty claim for NEP/detectivity definitions;
- no novelty claim for Fisher information as a generic sensing metric;
- no generalized `NEP_F` novelty claim before dedicated prior-art review;
- no implied experimental validation without data;
- no prize-level framing.

## Documentation cadence

Update `practical_temporal_information/notes/`, `practical_temporal_information/AGENTS.md`, and the top-level landing files after each material advance. The repository must remain sufficient for takeover without chat context.
