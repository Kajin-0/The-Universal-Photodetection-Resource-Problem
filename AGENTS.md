# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Current frontier

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science frontier: **WP27**.
- Preferred Grand Challenge manuscript: **Rev10 — Spectral Resource Laws for Temporal Fisher Information**, frozen.
- First target: **PRX Quantum — Research Article**.
- Fallback: **Physical Review A — Regular Article**.

A replacement agent must switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`
3. `grand_challenge/notes/WP27_SHARP_HIGH_RETENTION_EXPONENT_AND_REV10_REFEREE_CLOSURE.md`
4. `grand_challenge/notes/WP26_HERGLOTZ_COMMON_MEASUREMENT_RETENTION.md`
5. `grand_challenge/notes/WP25_COMPLETE_MONOTONE_SATURATION_CLASSIFICATION.md`
6. `docs/CURRENT_RESEARCH_STATE.md`
7. `ROADMAP.md`

## Theorem hierarchy

### Finite-copy modewise theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

Controlled periodic-to-continuum limits satisfy

`R(nu)<=Pr(Omega>=nu)`.

`Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge; the area law and `hfR` relation are first-moment corollaries.

### Fixed-one-copy common-measurement theorem

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Thus every finite Toeplitz matrix `[R_M(i-j)]` is PSD. Combining this with semibounded energy tails gives

`Ebar+>=hbar nu A(R)`,

`A(R)~1/sqrt(2(1-R))` as `R->1`.

This is specifically a fixed-one-copy/common-POVM result, not an arbitrary collective-`N` theorem. The continuum Herglotz extension invokes Bochner only when the controlled normalized positive-definite limit is continuous at the origin.

### Sharp divergence exponent

The finite sine-profile family under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`, `nbar_L=(L-1)/2`,

hence `nbar_L~pi/[2sqrt(1-R_L(1))]`. The inverse-square-root divergence exponent is sharp; the globally optimal prefactor is not claimed.

### Complete one-copy extremizers

On the full contiguous pure-sector chain:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential mixtures give the completely monotone continuum equality cone.

## Physical scope

Independent quantum-marked Poisson sources inherit the modewise tail law through arbitrary parameter-independent source-to-field and detector processing by POVM pullback.

Arbitrary parameter-dependent waveform-state synthesis remains outside the theorem; the coherent-sideband no-go shows that baseline mean energy alone is insufficient for that broader class.

## Priority discipline

Do not claim novelty for weighted `U(1)` twirling, Herglotz/Bochner, Hausdorff/Bernstein moment theory, canonical phase POVMs, geometric/exponential mixtures, finite sine states, generic QFI/Holevo/RLD/SLD machinery, or generic Poisson/CPTP data processing.

The candidate contribution is the operational combination: arbitrary-POVM Fisher-tail coefficients, fixed-measurement positive-definite retention geometry, semibounded near-lossless divergence with sharp exponent, complete one-copy saturation classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

## Rev10 preflight

- 11 pages;
- full LaTeX/BibTeX build: **PASS**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and inspected: **PASS**;
- sine-profile sharpness validator: **PASS**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`.

The current connector does not expose branch-push Actions runs; do not claim direct remote-run inspection. The equivalent local generation/build/render gate passed.

## Workflow rule

Do **not** reintroduce “human verification” as a research/manuscript completion gate. Carry work autonomously through hostile review, research, derivation, code checks, manuscript, figures, builds, and submission engineering. The finished package is handed to a human for submission.

Unknown administrative facts may remain placeholders; never invent affiliation, funding, conflicts, or similar metadata.

## Freeze

**Freeze Rev10** unless a concrete theorem defect, historical-priority collision, build/journal-format problem, or new referee-level objection appears.

Every material state change must be reflected on the active branch and mirrored onto `main`.
