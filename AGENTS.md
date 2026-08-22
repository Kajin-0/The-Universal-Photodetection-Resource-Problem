# AGENTS.md

## Purpose

Durable repository handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

`main` is the landing/index branch. Active derivations and manuscript generation live on `agent/temporal-information-resource-law`.

## Current frontier

- Paper 1 Rev11: frozen.
- Paper 2 Rev7: frozen.
- Grand Challenge science checkpoint: **WP24**.
- Preferred Grand Challenge manuscript: **Rev7 PRX Quantum**.
- First target: **PRX Quantum — Research Article**.
- Fallback: **Physical Review A — Regular Article**.

A replacement agent must switch to `agent/temporal-information-resource-law` and read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV7_REFEREE_HARDENING_2026-08-22.md`
3. `docs/CURRENT_RESEARCH_STATE.md`
4. `ROADMAP.md`

## Theorem

For exact periodic random-time encoding,

`Tr F_N^(k)/N <= min(D_k,U_k) <= T_k`,

for any finite number of independently encoded copies and any joint POVM, including arbitrary entangled collective measurements.

Controlled periodic-to-continuum limits satisfy

`R(nu) <= Pr(Omega>=nu)`.

This survival law is the principal continuum statement. `Ebar+=hbar<Omega>` is mean excess energy above the participating lower edge; the area and `hfR` relations are first-moment corollaries.

## Rev7 significance hardening

Rev7 responds directly to an external adversarial review:

- continuum scope explicitly labeled controlled periodic-to-continuum;
- excess-energy meaning explicit;
- survival law promoted above `hfR`;
- distinction from `U(1)` modes-of-asymmetry theory sharpened;
- one transform-limited truncated-Gaussian single-photon example added;
- Figure 1 revised consistently.

The photon example reaches about 96.6% of the survival ceiling at half a Gaussian width and 88.5% at one width under canonical covariant timing.

Final local Rev7 preflight: **8 pages, complete LaTeX/BibTeX PASS, zero unresolved citations/references, zero overfull boxes, full 200-dpi visual inspection PASS**.

## Priority discipline

Do not claim novelty for weighted `U(1)` twirling, energy-gap modes, canonical phase POVMs, number/energy-constrained phase estimation, generic QFI/Holevo/RLD/SLD bounds, random-unitary estimation, waveform QFI, Hardy--Hilbert/positive-frequency mathematics, or generic Poisson/CPTP data processing.

The candidate contribution is the operational **classical-Fisher population-tail/survival law** for perturbations of a random-time mixing distribution, including arbitrary finite-copy collective measurements, an exact all-mode budget, sharp simultaneous attainability, and source-to-record consequences.

**Priority remains unverified, not certified.**

## Workflow rule

Do **not** reintroduce “human verification” as a research/manuscript completion gate. Carry the work autonomously through hostile review, research, derivation, code checks, manuscript, figures, builds, and submission engineering. The finished package is handed to a human for submission.

Unknown administrative facts may remain placeholders; never invent affiliation, funding, conflicts, or similar metadata.

## Freeze

**Freeze Rev7** unless a concrete theorem defect, historical-priority collision, build defect, unavoidable journal-format problem, or new referee-level objection appears.

Every material state change must be reflected on the active branch and mirrored onto `main`.
