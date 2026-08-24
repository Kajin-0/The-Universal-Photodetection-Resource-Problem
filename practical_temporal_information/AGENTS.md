# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that translates the temporal-information resource program into standard detector physics and explicit falsification tests. Do not modify the frozen theorem/proof layers of the three mature papers unless a genuine defect is exposed.

## Read first

1. `README.md`
2. `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`
3. `notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
4. `notes/WP06_MINIMUM_PAPER_STACK_AND_FALSIFICATION_MATRIX.md`
5. `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
6. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
7. `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
8. `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
9. `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
10. root `docs/CURRENT_RESEARCH_STATE.md`

## Current status

WP07 prior-art gate: **PASS WITH NARROWED CLAIMS**.

WP08 final pre-manuscript gate: **PASS**.

The manuscript workspace may now be created.

## Final Paper-4 claim hierarchy

### New candidate Paper-4 science

**P4-T1 — support-seed crossover**

For the explicit positive-semidefinite carrier/sideband family of WP04,

`lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`.

This is the scientific center of Paper 4: controlled removal of baseline spectral support converts the finite-radius survival resource into the rank-boundary second-order synthesis resource.

**P4-C1 — ideal phase-modulation boundary saturator**

Ordinary weak phase modulation with the locked phase-sensitive analyzer saturates the bilateral boundary population-curvature Fisher law.

Priority remains unverified/not certified; targeted WP07 search found no direct collision.

### Cited upstream benchmarks

**P4-B1 — Type-II memory benchmark.** Use the frozen random-time paper's theorem that the entire homogeneous saturation curve can be fixed while timestamp information differs. Make it experimentally actionable; do not republish it as a new theorem.

**P4-B2 — prescribed-curvature implementation benchmark.** Use the frozen PRA theorem `V_min=(1/2)Tr C` and WP05's standard resonant beam-splitter realization.

### Standard bridge/background

- **P4-S1:** linear Gaussian `Tr F/T=2/NEP(f)^2` under the locked convention.
- **P4-S2:** ideal Poisson/jitter `Tr F/T=lambda0 |Phi_J(Omega)|^2` for fractional two-quadrature modulation.
- **P4-S3:** explicit conventional-specification incompleteness example from WP08.

## Opening detector example

Two detectors have identical responsivity

`|H|^2=1/(1+x^2)`, `x=f/f_c`,

the same DC output-noise PSD `S0`, the same DC NEP, and the same responsivity 3-dB frequency `f_c`.

Detector A: `S_A=S0`.

Detector B: `S_B/S0=1/5+(4/5)/(1+25x^2)`.

Their normalized single-quadrature FI spectra are

`J_A=1/(1+x^2)`,

`J_B=(1+25x^2)/[(1+x^2)(1+5x^2)]`.

At `f=f_c`, `J_B/J_A=13/3≈4.3333` despite identical conventional DC sensitivity and responsivity bandwidth. B remains above half its DC FI until `f≈2.9703 f_c`.

Use this as the manuscript opening. It is an explicit standard-detector illustration, not a priority claim.

## Falsification hierarchy

Always distinguish:

1. **Level I — detector-model/reduction failure.** Gaussian, Poisson, independent-jitter, ideal modulation, or ideal Hamiltonian assumptions fail.
2. **Level II — resource-law challenge.** Only after theorem hypotheses, parameter normalization, support/radius, and measured FI/curvature are independently verified.
3. **Level III — saturating-model equality failure.** Usually falsifies the selected ideal saturator, not the general theorem.

## Manuscript architecture

I. What conventional detector specifications do not determine.

II. Memory benchmark: identical saturation does not imply identical information.

III. Spectral support: seeded survival -> empty-sideband synthesis.

IV. Standard Hamiltonian implementation.

V. Falsification matrix.

VI. Discussion.

Maximum four figures. Main-text target roughly 10–14 journal pages before references.

## Immediate work order

1. create `manuscript/practical_temporal_information/` with manuscript architecture, references, and a minimal REVTeX draft;
2. write the Introduction/measurement bridge from WP08 without novelty overclaiming;
3. integrate WP04 as the principal original theorem;
4. cite rather than duplicate the Paper-2 and PRA proofs;
5. run a hostile manuscript-level audit before calling any draft submission-ready.

## Prior-art exclusions

Do not claim novelty for dead-time information theory, variable/random dead time, inter-arrival characterization, paralyzable correlation distortion, sideband Fisher metrology, seeded/vacuum interferometry, generic rank-boundary QFI curvature, beam-splitter metrology, standard NEP, or generic Fisher sensing.

## Documentation rule

After every material manuscript/science change, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
