# Research Roadmap

**Updated:** 2026-08-22

**Active branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

**Grand Challenge science frontier:** **WP27**.

**Preferred manuscript:** **Rev10 — Spectral Resource Laws for Temporal Fisher Information**, frozen after full local preflight.

# Established hierarchy

## G1 — finite-copy operational Fisher-tail law

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite `N` and any joint POVM, including arbitrary entangled collective measurements. Summing gives `sum_(k>=1)R_N(k)<=nbar`.

## G2 — controlled continuum survival law

`R(nu)<=Pr(Omega>=nu)`.

`Ebar+=hbar<Omega>` is excess energy above the participating lower edge. The area law and pointwise `hfR` relation are first-moment corollaries.

## G3 — common-measurement Herglotz geometry

For one fixed one-copy POVM,

`R_M(k)=int cos(k theta)J_M(dtheta)`.

Every finite Toeplitz matrix `[R_M(i-j)]` is PSD. This is an additional global constraint across harmonics, not a replacement for the finite-copy modewise theorem.

## G4 — near-lossless divergence and sharp exponent

With `q=R_M(nu)`,

`Ebar+>=hbar nu A(q)`,

`A(q)~1/sqrt(2(1-q))` as `q->1`.

Exact unit retention at nonzero frequency is impossible for a normalized semibounded source.

The finite-chain sine-profile family under canonical phase measurement has

`R_L(1)=cos^2(pi/(L+1))`, `nbar_L=(L-1)/2`,

so `nbar_L~pi/[2sqrt(1-R_L(1))]`. Therefore the inverse-square-root exponent is sharp. Do not claim the optimal prefactor.

## G5 — complete one-copy extremizer classification

On the full contiguous pure-sector one-copy chain:

`first-harmonic saturation`

`<=> geometric-mixture populations`

`<=> Hausdorff-moment tails`

`<=> one common source-adapted POVM saturates every harmonic simultaneously`.

Controlled exponential-mixture limits give the completely monotone continuum equality cone.

## G6 — nonextremal photon relevance

A transform-limited truncated-Gaussian single photon reaches about 96.6% of the survival ceiling at `0.5 sigma` and 88.5% at `sigma` under canonical covariant timing.

## G7 — independent Poisson source to field

For an independent quantum-marked Poisson source, arbitrary parameter-independent field formation and detector processing cannot evade the normalized modewise bound because final POVMs pull back to the upstream event register.

## G8 — secondary QFI envelope

WP10/WP12/WP15 remain valid but secondary. If journal length pressure appears, move the separately optimized SLD-QFI comparison before cutting the Herglotz theorem, extremizer theorem, or photon example.

## G9 — arbitrary waveform synthesis boundary

The coherent-sideband no-go remains: baseline mean energy alone cannot constrain arbitrary parameter-dependent waveform-state synthesis. Broader laws require explicit encoding/control/action resource accounting.

# Prior-art discipline

Do not claim novelty for weighted `U(1)` twirling, Herglotz/Bochner theory, Hausdorff/Bernstein moment theory, canonical phase POVMs, geometric/exponential mixtures, finite sine states, generic QFI/Holevo machinery, or generic Poisson/CPTP data processing.

The candidate contribution is the operational synthesis: arbitrary-POVM Fisher-tail coefficients, fixed-measurement spectral consistency, semibounded near-lossless divergence with a sharp exponent, complete one-copy equality classification, and source-to-record inheritance.

**Priority remains unverified, not certified.**

# Rev10 gate — PASSED locally

The extreme Rev9 re-review found no central mathematical failure and requested two narrow formal/scope fixes. It also proposed the sine-profile family as the one optional result capable of materially strengthening the divergence theorem. Rev10 closes all three points.

Final local preflight:

- full LaTeX/BibTeX build: **PASS**;
- **11 pages**;
- PDF size: **444,063 bytes**;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- all 11 pages rendered at 200 dpi and visually inspected: **PASS**;
- sharpness validator: **PASS**;
- PDF SHA-256: `a5c2d9e12bba045b76bbfb710428e5424e2c5cb5eb83d6aec6215a5996dbc6fb`;
- source ZIP SHA-256: `cfa2452f9ce4e99d0cd56f931151f6bb166fd90d4332d86faf3ea2485dec1db9`.

Detailed record:
`grand_challenge/notes/MANUSCRIPT_REV10_REFEREE_CLOSURE_PREFLIGHT_2026-08-22.md`.

# Journal ladder

1. **PRX Quantum — Research Article**.
2. **Physical Review A — Regular Article**.
3. Physical Review Research — secondary alternative.
4. PRL — only after a deliberate Letter rewrite; do not hide hypotheses/proofs to force format.

# Current work order

**Freeze Rev10.** Do not optimize the asymptotic prefactor, add more examples, or broaden the source class by default. Reopen only for:

- a concrete theorem defect;
- historical-priority collision;
- build/rendering or journal-format defect;
- a new referee-level objection.

The paper and submission package are to be completed as far as possible autonomously. Do not introduce “human verification” as a research/manuscript gate.

# Documentation discipline

Every material theorem, prior-art collision, manuscript defect, or publication-status change must update the detailed notes, active landing/handoff files, and `main`.
