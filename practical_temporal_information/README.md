# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests. This is not another abstraction layer and does not alter the frozen theorem/proof stacks of the three mature papers.

Working title:

> **Operational benchmarks for temporal information in photodetection**

## Gate status

- WP07 prior-art/significance gate: **PASS WITH NARROWED CLAIMS**.
- WP08 final pre-manuscript gate: **PASS**.

The manuscript workspace may now be created.

## Final claim hierarchy

### Primary new candidate theorem

**Support-controlled survival-to-synthesis crossover**

For the explicit seeded carrier/sideband family,

`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`.

At `p>0` the relevant sideband lies in the baseline support and finite-radius survival applies. At `p=0` the affine radius collapses and second-order sideband population curvature becomes the synthesis resource. Ordinary ideal weak phase modulation saturates the bilateral boundary-curvature law under the locked convention.

Targeted WP07 search found no direct collision for this exact identity / interpretation. Priority remains unverified, not certified.

### Cited upstream benchmark — detector memory

The frozen random-time paper proves that for fixed mean Type-II recovery all iid recovery laws share `r=lambda exp(-lambda m)` while timestamp information is not fixed; at the common maximum deterministic recovery is uniquely information-singular. Paper 4 should make this result experimentally actionable, not republish it as a new theorem.

### Cited upstream benchmark — implementation cost

The frozen PRA companion proves `V_min=(1/2)Tr C`. WP05 gives a standard resonant beam-splitter realization with

`V_min=8(g t)^2`, `A_ex=hbar nu V_min`,

while the total bare-energy distribution remains fixed.

### Standard measurement bridge

- linear Gaussian: `Tr F/T=2/NEP(f)^2`;
- ideal Poisson fractional timestamps: `Tr F/T=lambda0`;
- independent timing jitter: multiply by `|Phi_J(Omega)|^2`.

No novelty claim is attached to these bridges.

## Conventional-specification incompleteness example — WP08

Both detectors have

`|H(f)|^2=1/[1+(f/f_c)^2]`,

the same DC output-noise PSD `S0`, the same DC NEP, and the same responsivity 3-dB frequency `f_c`.

Detector A:

`S_A(f)=S0`.

Detector B:

`S_B/S0=1/5+(4/5)/[1+25(f/f_c)^2]`.

Normalized single-quadrature FI spectra:

`J_A=1/(1+x^2)`,

`J_B=(1+25x^2)/[(1+x^2)(1+5x^2)]`, `x=f/f_c`.

At `f=f_c`,

`J_B/J_A=13/3≈4.3333`.

B does not fall to half its DC FI until

`f≈2.9703 f_c`.

Thus the pair `{DC NEP, responsivity 3-dB bandwidth}` does not determine temporal estimation performance. This is a standard-physics illustration, not a priority claim.

## Falsification hierarchy

1. detector-model/reduction failure;
2. resource-law challenge only after theorem hypotheses are independently verified;
3. failure of a model-specific saturating equality.

## Final main-text architecture

I. What conventional detector specifications do not determine.

II. Detector-language FI bridge and memory benchmark.

III. Spectral support: seeded survival -> empty-sideband synthesis.

IV. Standard Hamiltonian implementation.

V. Integrated falsification matrix.

VI. Discussion.

Target roughly 10–14 journal pages before references; maximum four figures.

## Authoritative notes

- `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
- `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
- `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
- `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
- `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
- `notes/WP06_MINIMUM_PAPER_STACK_AND_FALSIFICATION_MATRIX.md`
- `notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`
- `notes/WP08_FINAL_PREMANUSCRIPT_STACK_AND_SPEC_INCOMPLETENESS.md`

## Immediate work

Create `manuscript/practical_temporal_information/`, draft from the detector example outward, keep WP04 as the principal original theorem, cite rather than duplicate the mature papers, and run a hostile manuscript-level audit before freezing any submission package.

## Claim discipline

No novelty claim for generic dead-time information theory, variable/random dead time, interval characterization, paralyzable correlations, standard NEP/Fisher sensing, sideband generation/metrology, seeded/vacuum interferometry, generic boundary-QFI curvature, beam-splitter physics, or standard interferometry. No experimental validation is implied without data.

## Documentation rule

Every material advance must update the corresponding note, this handoff, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
