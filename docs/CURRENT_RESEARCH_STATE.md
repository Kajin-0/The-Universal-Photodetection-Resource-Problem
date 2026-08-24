# Current Research State

**Last synchronized:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Frozen upstream scientific layers

- Paper 1 Rev11;
- Paper 2 Rev7;
- random-time spectral-resource paper;
- autonomous temporal-information R3 theorem/proof baseline;
- PRX Quantum R4 publication-layer bridge;
- D2/WP32 unitary-coupling theorem/proof baseline;
- reviewer-repaired PRA R1 package.

WP31 remains superseded. WP32 is canonical; WP33 hostile audit remains PASS under stated assumptions.

## New active frontier — practical/falsifiability Paper 4

The next program is deliberately more grounded than the existing theorem papers.

Working title:

> **Operational benchmarks for temporal information in photodetection**

Objective: translate temporal Fisher/resource statements into standard detector observables and make falsifiability explicit.

Primary observables:

- frequency-dependent responsivity;
- measured output noise PSD;
- NEP/detectivity;
- response versus information bandwidth;
- raw photon/event timestamps;
- timing jitter;
- dead time/recovery/memory;
- optical carrier/sideband populations;
- standard resonant-exchange coupling parameters.

Workspace:

- `practical_temporal_information/README.md`;
- `practical_temporal_information/AGENTS.md`;
- `practical_temporal_information/notes/`.

## WP01 result — linear Gaussian detector bridge

For

`delta P(t)=x cos(2 pi f t)+y sin(2 pi f t)`

with peak optical-power quadratures `x,y`, linear small-signal responsivity `R(f)`, and one-sided additive stationary Gaussian output-noise PSD `S_n(f)`, the Fisher rates are

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`,

`F_xy -> 0`,

and

**`Tr F/T = 2|R(f)|^2/S_n(f)`.**

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

**`F_xx/T = 1/NEP(f)^2`**

and

**`Tr F/T = 2/NEP(f)^2`.**

For arbitrary weak input-waveform coordinates `q_i(t)`,

**`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.**

Thus inverse-square NEP is exactly the frequency weighting of the local input-waveform Fisher metric in the linear stationary Gaussian regime.

WP01 also shows that conventional responsivity 3-dB bandwidth is not generally an information bandwidth. The relevant narrowband information response is proportional to

`|R(f)|^2/S_n(f)=1/NEP(f)^2`.

If signal and dominant input noise are passed through the same nonzero linear transfer function, both can attenuate while their Fisher ratio remains unchanged; additive post-filter/readout noise restores a finite information rolloff. This gives a conventional signal-processing explanation for why speed-of-response alone does not determine temporal estimation performance.

Authoritative derivation:

`practical_temporal_information/notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`.

## Prior-art status for WP01

No novelty claim is made for NEP, detectivity, matched filtering, Fisher information in optical sensing, or the generic connection between detector noise and estimation precision.

A 2025 Nature Photonics consensus statement strongly supports using measured frequency-dependent responsivity, noise PSD, and frequency/bandwidth-specific NEP and warns against inappropriate white-noise bandwidth normalization under colored noise. Recent optical-sensing papers also combine Fisher information with detector NEP. Therefore the publishable novelty, if any, must come from the integrated temporal-information framework, new detector-ranking/crossover laws, and explicit survival/synthesis falsification tests rather than from `F ~ 1/NEP^2` alone.

## Immediate next work

1. WP02 — derive ideal inhomogeneous-Poisson two-quadrature timestamp Fisher rate and exact independent-jitter attenuation.
2. WP03 — add dead time/recovery/memory and connect to the random-time spectral-resource theorem.
3. WP04 — construct the optical seeded-to-empty sideband survival/synthesis crossover.
4. WP05 — standard resonant-exchange Hamiltonian interpretation of unitary coupling cost.
5. WP06 — integrated falsification matrix.
6. WP07 — prior-art/significance gate before manuscript drafting.

## Publication/claim discipline

The three mature papers remain independent. Paper 4 is not an omnibus synthesis paper and should not duplicate their proof stacks.

Priority remains unverified/not certified. Do not use Nobel/prize-level framing. Do not claim a generalized information-equivalent detector metric is new until dedicated prior-art review.

Every material Paper-4 advance must update the practical notes and top-level landing files so a future agent can continue without chat history.
