# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-22**

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; preferred PRX Quantum manuscript **Rev7**.

Active branch: `agent/temporal-information-resource-law`.

Authoritative handoff: `grand_challenge/AGENTS.md`.

# Grand Challenge headline result

For exact periodic random-time encoding with sector probabilities `q_n`, define

`T_k = sum_(m>=k) q_m`.

For any finite `N` and **any joint POVM**, including entangled collective measurements,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`.

Thus

`R_N(k)=Tr F_N^(k)/N <= T_k`,

and

`sum_(k>=1)R_N(k) <= nbar`.

WP20 proves this directly by Hilbert--Schmidt Cauchy--Schwarz.

## Controlled periodic-to-continuum survival law

For a positive excess-frequency measure `mu`, controlled periodic-to-continuum limits satisfy

`R(nu) <= mu([nu,infinity)) = Pr(Omega>=nu)`.

This **survival law is the principal continuum theorem**.

`Ebar+ = hbar <Omega>` is mean excitation/excess energy above the participating lower edge, not a common optical carrier offset. The relations

`int_R R(nu)dnu <= 2Ebar+/hbar`,

`Ebar+ >= hbar nu R(nu) = h f R(2pi f)`

are first-moment corollaries of the survival law.

## Exact sharpness and realistic photon example

Geometric sectors with one canonical phase POVM give

`R(k)=T_k=r^k`

for every harmonic simultaneously. The controlled continuum equality family is exponential in excess frequency with a Cauchy canonical timestamp.

Rev7 additionally analyzes a transform-limited truncated-Gaussian single photon. Canonical covariant timing reaches about **96.6%** of the survival ceiling at `nu=0.5 sigma` and **88.5%** at `nu=sigma`, demonstrating that the bound remains restrictive away from the extremal equality family.

## Physical source-to-record scope

For independent quantum-marked Poisson events, the same normalized law survives arbitrary **parameter-independent** source-to-bosonic-field and detector processing through POVM pullback. This includes wavepacket overlap, propagation, loss, mode mixing, coherent detector memory, ancillas, and final joint readout.

The theorem does not apply merely because detector counts are Poisson, and it does not cover arbitrary parameter-dependent waveform-state synthesis. The coherent-sideband no-go remains the explicit boundary.

# Prior-art boundary

Weighted `U(1)` twirling and energy-gap modes, canonical phase measurements, energy-constrained phase estimation, generic quantum-Fisher/Holevo machinery, random-unitary estimation, waveform QFI, positive-frequency inequalities, Hardy--Hilbert constants, and generic Poisson/CPTP data processing are prior art.

The candidate contribution is narrower:

> an arbitrary-measurement **classical-Fisher population-tail/survival law** for Fourier perturbations of a latent random-time mixing distribution, including arbitrary finite-copy collective measurements, an exact all-mode budget, sharp simultaneous attainability, and source-to-record consequences.

Modes-of-asymmetry theory identifies which gap components exist; this theorem bounds how much **classical Fisher information any actual POVM can extract** about the mixing-law perturbation.

**Priority remains unverified, not certified.**

# Preferred manuscript — Rev7

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev7 was produced after an external adversarial review of Rev6. It implements the high-value recommendations without changing the finite-copy theorem:

- makes the continuum result explicitly controlled periodic-to-continuum;
- defines the resource consistently as excess energy above the participating edge;
- makes the survival law primary and `hfR` a first-moment corollary;
- sharpens the distinction from `U(1)` modes-of-asymmetry theory;
- adds one transform-limited single-photon example;
- hardens Figure 1 accordingly.

Final local Rev7 preflight:

- full LaTeX/BibTeX build: **PASS**;
- **8 pages**;
- PDF size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- all pages rendered at 200 dpi and visually inspected: **PASS**;
- photon closed forms and periodic-approximant convergence: **PASS**.

See:

1. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
2. `grand_challenge/AGENTS.md`
3. `grand_challenge/submission/PRX_QUANTUM_COVER_LETTER_DRAFT.md`
4. `grand_challenge/submission/PRX_QUANTUM_POPULAR_SUMMARY_DRAFT.md`

# Journal target

**First target:** PRX Quantum, Research Article.

**Fallback:** Physical Review A, Regular Article.

Do not force a PRL rewrite by hiding assumptions or proof structure.

# Workflow rule

Do not reintroduce “human verification” as a manuscript-completion gate. The research, validation, writing, build, and submission engineering are carried as far as possible; the finished package is handed to a human for submission. Unknown administrative facts may remain placeholders and must not be invented.

# Current work order

**Freeze Rev7.** Do not add more theorem scope, detector technologies, source classes, or examples unless a concrete defect or new referee-level objection appears.

Every material project-level change must be mirrored onto `main`.
