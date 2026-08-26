# Research Roadmap

**Updated:** 2026-08-25

**Active branch:** `agent/practical-temporal-information-benchmarks`

## Mature papers — frozen separately

1. PRX Quantum flagship — survival/synthesis conceptual law.
2. Broad random-time/timestamp spectral-information paper.
3. PRA exact unitary-coupling completion.

## Paper 4

Working title:

> **Operational temporal-information benchmarks for photodetection**

Provisional target: Physical Review Applied.

## Completed work packages

- **WP01:** linear Gaussian detector -> `Tr F/T=2/NEP(f)^2`.
- **WP02:** ideal Poisson timestamps -> `Tr F/T=lambda0`; independent jitter -> `|Phi_J|^2`.
- **WP03:** practical translation of frozen Type-II memory theorem.
- **WP04:** seeded-to-empty sideband crossover and ideal boundary saturation.
- **WP05:** equal-frequency resonant implementation benchmark.
- **WP06:** manuscript architecture and falsification hierarchy.
- **WP07/WP07A:** prior-art/significance gate and narrowed boundary-FI novelty claim.
- **WP08:** final pre-manuscript stack.
- **WP09:** first hostile audit; theorem generalized to stationary selected pair with inert spectators.
- **WP10:** second hostile scientific/build audit; theorem hypotheses and noncircular protocol hardened.
- **WP11:** R3/R4 exact artifact/render audit — PASS.
- **WP12:** standalone deterministic four-figure package — **FROZEN PASS**.
- **WP13:** R5 figure integration, full CI, and 10-page render audit — **FROZEN PASS**.

## Current R5 freeze

- run `32915363157` PASS;
- job `98017843874` PASS;
- source commit `55ec3af3bd9d57830c03f65655180936eb85eda9`;
- artifact `9588018384`;
- digest `sha256:06e1de8d8f5e44f9d62e6ebd06362d2cfbc93132014718398e57b877c784c281`;
- PDF: 10 pages / 429432 bytes;
- PDF SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`.

All ten pages rendered/inspected at 200 dpi. R5 adds only the four frozen WP12 figure/caption blocks to R4.

## Frozen principal theorem

For stationary selected modes separated by `hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

with stationary inert spectators and an incoherent/phase-randomized population seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`,

`(R_lin^2/4)Tr F<=p`,

and at zero seed

`Delta P_s(0)=4kappa^2 q`.

Therefore

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The boundary is attainable with `Tr F=Delta P_s(0)`.

Do not reopen theorem expansion without a genuine blocking defect.

## Novelty boundary

The general mechanism of finite FI from quadratically vanishing boundary probabilities/eigenvalues is prior art. Paper 4's candidate distinct contribution is the controlled finite-seed/finite-radius continuation and independent detector-facing falsification protocol. Priority remains **unverified, not certified**.

## Frozen figures

WP12 run `32914889053`, artifact `9587797682`.

1. same conventional specs / different information spectra;
2. same Type-II saturation / different timestamp information — companion benchmark;
3. support-controlled survival→synthesis crossover — principal Paper-4 figure;
4. equal-frequency resonant implementation + failure hierarchy — companion benchmark.

Do not redesign the frozen figures during ordinary publication cleanup.

## Active work package — publication compression

The next task is not new science.

### Gate A — hostile redundancy audit

Read frozen R5 as a Physical Review Applied referee/editor. Identify only text that is:

- repeated;
- tutorial beyond what the target audience needs;
- duplicated between caption and body;
- unnecessarily defensive without adding a hypothesis or provenance boundary.

Do not delete assumptions, novelty boundaries, falsification distinctions, or companion attribution.

### Gate B — optional R6

Create R6 only if the hostile audit finds a meaningful reduction. R6 must be a deterministic text-only transform with an explicit allowed-edit map.

R6 constraints:

- preserve all four R5 figure blocks exactly;
- preserve theorem/proposition/equation/proof content unless a genuine defect is found;
- preserve Data Availability and AI-assistance disclosures;
- preserve companion provenance and the narrow novelty boundary;
- compile, warning-check, render, and adversarially review independently.

### Gate C — submission packaging

After the final text freeze:

1. fresh-check then-current APS/PRA author, AI-tool, data-availability, related-manuscript, and citation policies;
2. replace anonymous author/affiliation metadata;
3. update companion citations if public identifiers exist;
4. prepare cover letter and submission checklist;
5. do not change scientific content merely to fit a submission template.

## Claim discipline

No novelty claim for standard NEP/detectivity, generic Fisher sensing, Poisson/dead-time formulas, random dead time, interval characterization, electro-optic sidebands, seeded/vacuum interferometry, beam-splitter physics, standard interferometry, or generic boundary-QFI behavior. No implied experimental validation. No prize-level framing.
