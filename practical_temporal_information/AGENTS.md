# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that brings the temporal-information resource program down to standard detector physics and builds explicit falsifiability into the presentation.

Do not turn this into another general resource-theory paper. Every central result should answer: what is measured, what is predicted, and what observation would contradict it?

## Frozen upstream inputs

Do not modify the scientific theorem/proof layers of:

1. PRX Quantum flagship `Two spectral-resource regimes for autonomous temporal information`;
2. random-time paper `Spectral Resource Laws for Temporal Fisher Information`;
3. PRA R1 `Exact minimum unitary coupling cost of prescribed rank-changing quantum-state curvature`.

If Paper 4 exposes a genuine upstream defect, record it immediately and stop using the affected claim until repaired. Otherwise upstream changes should be limited to later small application/cross-reference paragraphs after Paper 4 is stable.

## Read first

1. `README.md`
2. `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
3. `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
4. root `docs/CURRENT_RESEARCH_STATE.md`

## Current frontier

### WP01 — complete: linear Gaussian detector

For peak optical-power quadratures `x,y`, one-sided output-noise PSD `S_n(f)`, and linear responsivity `R(f)`,

`F_xx/T = F_yy/T = |R(f)|^2/S_n(f)`

and

`Tr F/T = 2|R(f)|^2/S_n(f)`.

When conventional frequency-resolved NEP is valid,

`NEP(f)=sqrt(S_n(f))/|R(f)|`,

so

`F_xx/T=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij = 4 Re integral_0^infinity q_i*(f) q_j(f)/NEP(f)^2 df`.

The task-relevant information response is `|R|^2/S_n=1/NEP^2`, not responsivity alone. Therefore response 3-dB bandwidth and Fisher-information bandwidth need not coincide.

### WP02 — complete: Poisson timestamps and independent jitter

For an ideal inhomogeneous Poisson detector

`lambda(t)=lambda_0[1+x cos(Omega t)+y sin(Omega t)]`

with fractional peak quadratures,

**`Tr F/T=lambda_0`**

exactly for the continuously illuminated finite-window model. For integer-period/long observations,

`F_xx/T=F_yy/T=lambda_0/2`, `F_xy/T -> 0`.

For optical-power quadratures with `lambda_0=eta P_0/(hbar omega_opt)`,

`Tr F_P/T=eta/(hbar omega_opt P_0)`.

This exactly equals the WP01 prediction `2/NEP_shot^2` using one-sided shot-current PSD `S_I=2qI_0` and `R_I=eta q/(hbar omega_opt)`.

If each timestamp is independently displaced by jitter `J`, with characteristic function `Phi_J(Omega)`,

**`Tr F_jitter/T=lambda_0 |Phi_J(Omega)|^2`.**

For Gaussian jitter standard deviation `sigma_t`,

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`

and

`f_F,3dB=sqrt(ln 2)/(2 pi sigma_t) ~= 0.1325/sigma_t`.

Independent dark counts `lambda_d` with signal rate `lambda_s` give

`Tr F/T=lambda_s^2/(lambda_s+lambda_d)`

before the jitter factor.

These formulas give direct timestamp-record falsification tests and make analog shot-noise and event-timestamp descriptions quantitatively identical when they represent the same ideal detection process.

## Convention lock

Every Fisher/PSD statement must specify:

- one-sided versus two-sided PSD;
- peak versus RMS modulation;
- one- versus two-quadrature Fisher information;
- absolute-power versus fractional modulation coordinates;
- observation/gating assumptions;
- whether timestamps are raw, independently jittered, or memory-correlated.

## Next work packages

- **WP03:** dead time/recovery/memory and connection to the random-time spectral-resource theorem.
- **WP04:** optical sideband survival-to-synthesis crossover with seeded and empty sidebands.
- **WP05:** textbook resonant-exchange interpretation of exact unitary-coupling cost.
- **WP06:** integrated falsification matrix and minimal practical manuscript theorem stack.
- **WP07:** dedicated prior-art/significance gate before manuscript drafting.

Do not create sidequests that do not sharpen measurement accessibility, falsifiability, or standard-physics interpretation.

## Publication criterion

Paper 4 is justified only if it produces at least one result beyond a tutorial restatement. Candidate publication-level content includes a nontrivial detector-ranking law, a memory/timestamp benchmark invisible to mean count curves, a measurable survival/synthesis crossover, or an integrated falsification protocol that directly tests the upstream resource inequalities.

No novelty claim is made for standard NEP, detectivity, matched filtering, Poisson Fisher information, shot-noise formulas, or generic timing-jitter transfer functions.

## Documentation rule

After every material advance, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
