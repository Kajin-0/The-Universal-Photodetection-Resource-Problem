# Current Research State

**Last synchronized:** 2026-08-22

`main` is landing/index only.

**Active branch:** `agent/temporal-information-resource-law`

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science checkpoint: **WP24**.
- Preferred Grand Challenge manuscript: **Rev7 PRX Quantum**.

## Recovery

Switch to the active branch and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `docs/CURRENT_RESEARCH_STATE.md`
4. `ROADMAP.md`

## Theorem frontier

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`

for any finite-copy joint POVM, including arbitrary entangled collective measurements.

Controlled periodic-to-continuum limits satisfy

`R(nu) <= Pr(Omega>=nu)`.

This survival law is the principal continuum result. `Ebar+=hbar<Omega>` is excess energy above the participating lower edge; the area and `hfR` relations are first-moment corollaries.

## Rev7

Rev7 implements the latest adversarial review without changing the finite-copy theorem:

- explicit controlled continuum qualification;
- excess-energy terminology;
- survival law emphasized over `hfR`;
- sharper modes-of-asymmetry novelty boundary;
- transform-limited truncated-Gaussian single-photon example;
- revised Figure 1.

The photon example attains ~96.6% of the survival ceiling at `0.5 sigma` and ~88.5% at `sigma` under canonical timing.

Final local preflight:

- full LaTeX/BibTeX: **PASS**;
- **8 pages**;
- unresolved references/citations: **0**;
- overfull boxes: **0**;
- 200-dpi visual inspection of all pages: **PASS**;
- PDF SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`.

## Priority

The novelty candidate is the operational **classical-Fisher population-tail/survival law** for random-time mixing-law perturbations. Generic `U(1)` mode theory/twirling, canonical phase, phase estimation, QFI/Holevo machinery, waveform QFI, Hardy--Hilbert mathematics, and generic Poisson/CPTP processing are prior art.

**Priority remains unverified, not certified.**

## Target

**PRX Quantum — Research Article** first; **Physical Review A — Regular Article** fallback.

## Workflow

**Freeze Rev7** unless a concrete theorem defect, priority collision, build defect, journal-format problem, or new referee-level objection appears.

Do not reintroduce “human verification” as a research/manuscript completion gate. Unknown administrative facts remain placeholders; a human submits the finished package.

Every material project-level state change must be mirrored between the active branch and `main`.
