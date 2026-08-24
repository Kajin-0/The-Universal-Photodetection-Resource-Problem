# Practical temporal-information manuscript workspace

**Branch:** `agent/practical-temporal-information-benchmarks`

## Provisional journal target

**Physical Review Applied — Regular Article.**

Reason: the paper is intentionally positioned at the interface of detector/device physics, photonics, metrology, and quantum information, with explicit measurement and falsification protocols. The journal target is provisional and must not drive theorem changes.

## Working title

> **Operational temporal-information benchmarks for photodetection**

Alternative retained for later comparison:

> **Temporal-information benchmarks beyond static sensitivity and detector bandwidth**

## Scientific center

The manuscript should be understandable first as detector physics and only second as an application of the broader temporal-information resource program.

Opening problem:

> DC sensitivity, response bandwidth, saturation curves, and timing jitter are useful detector specifications, but they do not generally determine how much information a detector transfers about a time-dependent optical signal.

Principal original candidate result:

`lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`

for the explicit seeded carrier/sideband family, giving a controlled crossover from finite-radius spectral survival to rank-boundary second-order synthesis.

## Claim hierarchy

### Original Paper-4 candidate

- support-controlled sideband survival-to-synthesis crossover;
- ideal weak phase-modulation saturating corollary under the locked convention;
- integrated falsification architecture as a practical synthesis.

### Cited companion results

- random-time/Type-II information incompleteness theorem;
- exact prescribed-curvature unitary-coupling theorem.

Do not reproduce their proofs as new Paper-4 content.

### Standard bridge/background

- NEP/Fisher relation under explicit Gaussian/PSD conventions;
- ideal Poisson timestamp and independent-jitter relation;
- conventional-specification incompleteness counterexample;
- standard resonant beam-splitter Hamiltonian.

## Drafting rule

Write from standard measurements outward:

1. conventional detector example;
2. Fisher/NEP and timestamp bridge;
3. memory benchmark;
4. support crossover theorem;
5. Hamiltonian benchmark;
6. explicit falsification matrix.

Avoid opening with density-matrix geometry or resource-theory terminology.

## Current files

- `MANUSCRIPT_ARCHITECTURE.md` — section/claim/figure plan.
- `operational_temporal_information_draft.tex` — first REVTeX draft.
- `references.bib` — seed bibliography.

## Required pre-freeze work

1. compile and visually inspect the full draft;
2. run a theorem/provenance gate against WP01–WP08 and the frozen companion manuscripts;
3. hostile-review all novelty and falsification language;
4. add APS-compliant AI-use and Data Availability statements based on then-current policy;
5. replace anonymous author/citation metadata only at submission packaging stage;
6. do not call any revision submission-ready until a concrete successful CI build and PDF render audit are recorded.
