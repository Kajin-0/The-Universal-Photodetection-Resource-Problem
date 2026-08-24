# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests. This is not another abstraction layer and does not alter the frozen theorem/proof stacks of the three mature papers.

Working title:

> **Operational benchmarks for temporal information in photodetection**

## Current paper architecture after WP06

The minimum coherent practical paper is now fixed provisionally:

1. **measurement bridge** — analog NEP and timestamp likelihoods map ordinary detector records to temporal Fisher information;
2. **headline result 1: detector memory** — conventional dead-time/saturation summaries can fail to determine temporal-information transfer;
3. **headline result 2: spectral support** — seeded versus empty optical sidebands realize the survival-to-synthesis transition with an exact crossover;
4. **compact Hamiltonian completion** — a standard fixed-energy resonant beam-splitter realizes the exact unitary-coupling identity;
5. **integrated falsification matrix** — every result states measured quantities, assumptions, prediction, and what a failure means.

Do not expand this stack before the prior-art gate.

## Result summary

### WP01 — analog bridge

`F_xx/T=F_yy/T=1/NEP(f)^2`, `Tr F/T=2/NEP(f)^2` under the locked convention.

### WP02 — timestamp bridge

Ideal fractional Poisson modulation gives `Tr F/T=lambda_0`; independent timing jitter gives factor `|Phi_J(Omega)|^2`. The optical-power form exactly matches ideal shot-noise NEP.

### WP03 — memory result

For fixed mean recovery `m`, every iid Type-II recovery law shares `r=lambda exp(-lambda m)`. At the common maximum, `G_DC=0` iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation laws have different timestamp information and simple accessible separating statistics.

### WP04 — support crossover

Seeded sideband:

`(R_lin^2/4)Tr F<=p`.

Empty-sideband boundary:

`Tr F<=Delta P_s`,

with exact crossover

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation saturates the bilateral boundary-curvature law.

### WP05 — Hamiltonian completion

Standard resonant two-boson beam-splitter benchmark:

`V_min=8(g t)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

while the total bare-energy distribution remains exactly fixed.

For fixed duration,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

## Falsification hierarchy

### Level I — detector-model/reduction failure

Examples: `R^2/S_n` does not match empirical FI, independent-jitter law fails, ideal beam-splitter endpoint curvature misses calibrated `g t`.

First interpretation: model/calibration/stationarity/independence assumptions are wrong.

### Level II — resource-law challenge under verified assumptions

Examples: calibrated finite-radius experiment violates `(R_lin^2/4)Tr F<=p`, or a verified rank-boundary family violates its curvature FI bound.

Only after theorem hypotheses are independently established should such a violation be described as challenging the resource law.

### Level III — saturating-model equality failure

Failure of ideal phase-modulation or beam-splitter equality normally falsifies the specific saturating model, not the general theorem lower bound.

## Scope removals

Do not add dedicated main-text sections for a separate photoconductor pole model, RC photodiode example, generalized `NEP_F` terminology, many recovery families, extra modulation technologies, unequal-frequency pumped converters, or infinite-dimensional PRA machinery unless WP07/referees create a concrete need.

## Proposed main-text structure

I. Motivation: sensitivity/saturation are not information-transfer laws.

II. Detector-language Fisher bridge — approximately 1.5–2 pages.

III. Memory: same saturation, different information.

IV. Spectral support: survival -> sideband synthesis.

V. Standard Hamiltonian implementation — short benchmark.

VI. Integrated falsification table/discussion.

Target main-text length: roughly 10–14 journal pages before references.

## Figures — maximum four

1. analog/timestamp common Fisher language;
2. same saturation / different timestamp information;
3. seeded-to-empty sideband crossover;
4. fixed-energy beam-splitter implementation plus measurement map.

## Authoritative notes

- `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
- `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
- `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
- `notes/WP04_OPTICAL_SIDEBAND_SURVIVAL_SYNTHESIS_CROSSOVER.md`
- `notes/WP05_RESONANT_EXCHANGE_UNITARY_COUPLING_BRIDGE.md`
- `notes/WP06_MINIMUM_PAPER_STACK_AND_FALSIFICATION_MATRIX.md`

## Publication gate

**Do not draft Paper 4 yet.** WP07 must adversarially search prior art around the three candidate distinct claims:

1. same full Type-II saturation + matched recovery moments need not determine temporal FI and admit simple accessible separating statistics;
2. exact seeded-to-empty sideband support crossover `lim 4p/R_lin^2=Delta P_s` as an experimentally legible survival/synthesis transition;
3. integrated falsification framework linking NEP/timestamps, support curvature, and fixed-energy coupling without conflating detector-model failure with theorem failure.

## Claim discipline

No novelty claim for NEP, generic Fisher sensing, Poisson/dead-time formulas, timing-jitter transfer, sideband generation, beam-splitter physics, or standard interferometry. No experimental result is implied without data.

## Documentation rule

Every material advance must update the corresponding note, this handoff, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
