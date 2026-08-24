# Research Roadmap

**Updated:** 2026-08-23

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature papers — frozen separately

1. PRX Quantum flagship — survival/synthesis conceptual law.
2. Broad random-time/timestamp spectral-information paper.
3. PRA exact unitary-coupling completion.

## Paper 4

Working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional target: Physical Review Applied.

## Completed Paper-4 work packages

- **WP01:** linear Gaussian detector -> `Tr F/T=2/NEP(f)^2`.
- **WP02:** ideal Poisson timestamps -> `Tr F/T=lambda0`; independent jitter -> `|Phi_J|^2`.
- **WP03:** practical translation of frozen Type-II memory theorem.
- **WP04:** explicit seeded-to-empty sideband crossover and ideal phase-modulation boundary saturation.
- **WP05:** equal-frequency resonant exchange benchmark of the frozen implementation theorem.
- **WP06:** minimum manuscript architecture and falsification hierarchy.
- **WP07:** adversarial prior-art/significance gate — **PASS WITH NARROWED CLAIMS**.
- **WP07A:** close boundary-FI prior art identified; novelty boundary tightened.
- **WP08:** final pre-manuscript theorem/benchmark stack — **PASS**.
- **WP09:** first hostile manuscript audit; theorem generalized to stationary selected pair with inert spectators.
- **WP10:** second hostile scientific/build audit; theorem hypotheses, noncircular `R_lin` protocol, incoherent seed, reference migration, and equal-frequency resonance clarification repaired.
- **WP11:** exact R3/R4 build and render audit — **PASS**.

## Current R4 freeze

Final R4 verification:

- run `32684526293` PASS;
- job `97307019940` PASS;
- artifact `9505218922`;
- archive digest `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`;
- exact PDF: 8 pages, 266068 bytes;
- SHA-256 `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`.

All pages rendered and inspected. R4 changes only hyperlink presentation relative to R3. PR #35 closed unmerged; zero open PRs.

## Frozen principal theorem

For stationary selected modes separated by `hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with stationary inert spectators and incoherent/phase-randomized population seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

`(R_lin^2/4)Tr F<=p`,

and at zero seed

`Delta P_s(0)=4kappa^2 q`.

Therefore

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The boundary is attainable with `Tr F=Delta P_s(0)`.

Do not reopen theorem expansion without a concrete blocking defect.

## Novelty boundary

The general mechanism of finite FI from quadratically vanishing boundary probabilities/eigenvalues is prior art. Paper 4's candidate distinct contribution is the exact finite-seed/finite-radius continuation into that boundary plus a noncircular detector-facing falsification protocol.

Priority remains **unverified, not certified**.

## Active work package — WP12 publication figures

Maximum four figures:

### Figure 1 — same specifications, different information

Show common single-pole responsivity, different output-noise spectra, and normalized FI spectra. Mark `f=f_c`, where the FI ratio is `13/3`, and the detector-B half-DC-FI point `f/f_c≈2.9703`.

### Figure 2 — memory hidden by saturation

Show the common Type-II saturation curve and one compact timestamp/interval-information contrast between two recovery laws. The theorem/result must be attributed to the frozen companion paper. Avoid reproducing an entire Paper-2 figure stack.

### Figure 3 — support-controlled survival→synthesis crossover

Principal figure. Show selected carrier/sideband preparation, shrinking affine radius, finite-seed quantity `4p/R_lin^2`, and its convergence to `Delta P_s(0)=4kappa^2 q`. Make independent measurement routes for radius, curvature, and FI visually explicit.

### Figure 4 — standard resonant implementation + falsification map

Show equal-frequency fixed-energy exchange, the calibration relation `V_min=(1/2)Tr C`, and the Level-I/II/III interpretation of failures.

## WP12 gates

Each figure must:

1. be generated deterministically from committed script/source;
2. have an analytic/numerical data check;
3. use journal-readable labels and units/normalization;
4. avoid decorative or AI-generated scientific content;
5. distinguish Paper-4 original content from companion-derived benchmarks;
6. pass rendered visual QA before manuscript integration.

After all figures pass, integrate them through a new isolated manuscript revision, rebuild/render/hostile-review, then compress for publication and fresh-check APS submission policy.

## Claim discipline

No novelty claim for standard NEP/detectivity, generic Fisher sensing, Poisson/dead-time formulas, random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter physics, standard interferometry, or generic boundary-QFI behavior. No implied experimental validation. No prize-level framing.
