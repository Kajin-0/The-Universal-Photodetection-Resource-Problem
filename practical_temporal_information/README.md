# Practical temporal-information benchmarks

**Branch:** `agent/practical-temporal-information-benchmarks`

## Purpose

Develop a fourth, deliberately grounded paper that translates the existing temporal-information resource program into standard detector physics and explicit falsification tests. This is not another abstraction layer and does not alter the frozen theorem/proof stacks of the three mature papers.

Working title:

> **Operational benchmarks for temporal information in photodetection**

## Publication gate after WP07

**PASS WITH NARROWED CLAIMS.**

The practical paper remains justified in principle, but not because Fisher information, detector dead time, inter-arrival statistics, optical sidebands, seeded/vacuum interferometry, or rank-changing QFI are individually new. Those ingredients have substantial prior art.

The strongest candidate new Paper-4 result is the **support-controlled optical survival-to-synthesis crossover** of WP04. The exact Type-II information theorem of WP03 is scientifically important but belongs to the already-frozen random-time paper and must be treated here as a cited practical benchmark, not republished as a new theorem.

Authoritative gate:

`notes/WP07_PRIOR_ART_AND_SIGNIFICANCE_GATE.md`.

## Current minimum paper architecture

1. **measurement bridge** — analog NEP and timestamp likelihoods map ordinary detector records to temporal Fisher information;
2. **memory benchmark** — use the frozen Paper-2 Type-II theorem to show concretely why saturation curves can be information-incomplete;
3. **new candidate theorem: spectral support crossover** — seeded versus empty optical sidebands realize the survival-to-synthesis transition with an exact measurable crossover;
4. **compact Hamiltonian benchmark** — a standard fixed-energy resonant beam splitter realizes the exact unitary-coupling identity;
5. **integrated falsification matrix** — every result states measured quantities, assumptions, prediction, and what a failure means.

## Result summary

### WP01 — analog bridge

`F_xx/T=F_yy/T=1/NEP(f)^2`, `Tr F/T=2/NEP(f)^2` under the locked convention.

This is background/translation, not a novelty claim.

### WP02 — timestamp bridge

Ideal fractional Poisson modulation gives `Tr F/T=lambda_0`; independent timing jitter gives factor `|Phi_J(Omega)|^2`. The optical-power form exactly matches ideal shot-noise NEP.

This is background/translation, not a novelty claim.

### WP03 — memory benchmark from frozen Paper 2

For fixed mean recovery `m`, every iid Type-II recovery law shares `r=lambda exp(-lambda m)`. At the common maximum, `G_DC=0` iff recovery is deterministic. Exact equal-mean/equal-variance/equal-saturation laws have different timestamp information and accessible separating statistics.

Paper 4 should turn this into a falsifiable detector-characterization protocol while citing the random-time paper. It must not claim the theorem as new Paper-4 content.

### WP04 — primary candidate new science

Seeded sideband:

`(R_lin^2/4)Tr F<=p`.

Empty-sideband boundary:

`Tr F<=Delta P_s`,

with exact crossover

`lim_(p->0+)4p/R_lin^2=Delta P_s`.

Ordinary ideal weak phase modulation saturates the bilateral boundary-curvature law under the locked convention.

The targeted WP07 search found no direct prior-art collision for this exact support-controlled crossover identity / survival-synthesis interpretation. Priority remains unverified, not certified.

### WP05 — Hamiltonian completion

Standard resonant two-boson beam-splitter benchmark:

`V_min=8(g t)^2=(1/2)Tr C`,

`A_ex=hbar nu V_min`,

while the total bare-energy distribution remains exactly fixed.

For fixed duration,

`V_impl=(t^2/hbar^2)sum_j Var(H_j)`.

The Hamiltonian is standard; the contribution here is its use as an independently calibratable implementation benchmark for the companion theorem.

## Falsification hierarchy

### Level I — detector-model/reduction failure

Examples: `R^2/S_n` does not match empirical FI, independent-jitter law fails, ideal modulation/beam-splitter curvature misses calibration.

First interpretation: model, calibration, stationarity, or independence assumptions are wrong.

### Level II — resource-law challenge under verified assumptions

Examples: a calibrated finite-radius experiment violates `(R_lin^2/4)Tr F<=p`, or a verified rank-boundary family violates its curvature FI bound.

Only after theorem hypotheses are independently established should such a violation be described as challenging the resource law.

### Level III — saturating-model equality failure

Failure of ideal phase-modulation or beam-splitter equality normally falsifies the specific saturating model, not the general theorem.

## Prior-art exclusions after WP07

Do not claim novelty for generic dead-time information theory, variable/random dead time, interval-based dead-time characterization, paralyzable correlation distortion, sideband Fisher metrology, seeded/vacuum interferometry, generic rank-boundary QFI curvature, or standard beam-splitter metrology.

## Scope removals

Do not add dedicated main-text sections for a separate photoconductor pole model, RC photodiode example, generalized `NEP_F` terminology, many recovery families, extra modulation technologies, unequal-frequency pumped converters, or infinite-dimensional PRA machinery unless a concrete need appears.

## Proposed main-text structure

I. Motivation: sensitivity/saturation are not information-transfer laws.

II. Detector-language Fisher bridge.

III. Memory benchmark: same saturation, different information.

IV. New support theorem: survival -> sideband synthesis.

V. Standard Hamiltonian implementation benchmark.

VI. Integrated falsification table/discussion.

Target main-text length: roughly 10–14 journal pages before references; maximum four figures.

## Immediate work

**WP08 — final pre-manuscript stack.** Derive one explicit conventional-detector misranking example, lock exact assumptions/units and decide which statements are new Paper-4 theorems versus cited upstream benchmarks. Create the manuscript workspace only after WP08 passes.

## Documentation rule

Every material advance must update the corresponding note, this handoff, root `README.md`, root `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
