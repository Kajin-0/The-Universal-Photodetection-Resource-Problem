# Journal positioning — autonomous temporal information manuscript

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Recommendation

### Primary aspirational target: PRX Quantum — Research Article

This is presently the strongest defensible first target **if the narrow priority claim survives final literature review and the paper is framed around one field-level insight rather than the WP chain**.

Current official PRX Quantum scope explicitly includes:

- fundamental concepts in quantum information;
- resource theories;
- quantum metrology and sensing;
- quantum thermodynamics;
- quantum information in fundamental physics;
- photon sources and detectors.

PRX Quantum Research Articles have no length limit. The journal is highly selective and, since its 2025 criteria clarification, asks for exceptionality through at least one of:

1. exceptional advance;
2. exceptional connection;
3. exceptional capabilities;
4. exceptional insight.

Official sources:

- https://journals.aps.org/prxquantum/scope
- https://journals.aps.org/prxquantum/about
- https://journals.aps.org/prxquantum/authors
- K. Cassemiro and S. Bartlett, PRX Quantum 6, 020001 (2025), DOI `10.1103/PRXQuantum.6.020001`.

### Best editorial case for this paper

Do **not** sell the paper as a new generic resource theory of time.

The strongest PRX Quantum case is **exceptional connection + exceptional insight**:

> Globally stationary relative temporal information exposes a resource dichotomy that is invisible to global time-translation asymmetry and to local Fisher information alone. A finite-radius temporal tangent is supported by pre-existing two-sided spectral survival; when the affine radius collapses at a rank-changing boundary, the resource changes order and becomes positive second-order two-sided endpoint synthesis action. Both regimes admit finite-copy arbitrary-POVM laws and sharp globally stationary constructions.

This connects four established areas in a way the theorem package makes operational:

- Page--Wootters / relational time;
- quantum metrology and common-record Fisher information;
- asymmetry/coherence resource theory;
- rank-changing state-space / PSD-cone geometry.

The claim is potentially field-level because it explains **what replaces global asymmetry as the necessary frequency-resolved resource when temporal information is purely relational** and why the resource itself changes at the boundary of state space.

### Evidence supporting PRX Quantum fit

Recent neighboring PRX Quantum work shows editorial interest in conceptual metrology frameworks rather than only platform-specific advances, including:

- *Quantum Metrology in the Finite-Sample Regime*, PRX Quantum 6, 030336 (2025), which demonstrates that QFI alone can be inadequate in a different operational regime;
- *Quantum Metrology through Spectral Measurements in Quantum Optics*, PRX Quantum 7, 010346 (2026), which connects spectral-mode access to Fisher information;
- *Randomized Measurements for Multiparameter Quantum Metrology*, PRX Quantum 7, 010314 (2026);
- *Interplay Between Time and Energy in Bosonic Noisy Quantum Metrology*, PRX Quantum 6, 020351 (2025).

These are not priority predecessors for the present theorem but show strong topical fit.

## Strong fallback: Physical Review A — Regular Article

PRA is the safest high-quality disciplinary fit.

Official scope includes:

- fundamental concepts;
- quantum information science;
- quantum technologies;
- quantum optics and photonics.

PRA requires a significant, high-quality contribution in a specific research area and offers Regular Articles with no length limit. Current source:

- https://journals.aps.org/pra/about
- https://journals.aps.org/pra/authors

The current M2R1 theorem package already comfortably fits PRA's topical scope even if editors/referees judge the PRX Quantum “exceptionality” case insufficient.

PRA is hybrid open access: immediate gold OA is optional rather than structurally required. PRX Quantum is fully open access and APC funded. This is a practical publication-route difference, not a scientific criterion.

## Stretch route: Physical Review Letters

PRL should **not** be the current default target.

Current PRL criteria require work that substantially advances a field, opens a significant new area, makes an essential step on a critical problem, or has unusual broad interest. A Letter has a **3750-word core limit**, approximately four published pages, plus up to two pages of End Matter.

Official sources:

- https://journals.aps.org/prl/about
- https://journals.aps.org/prl/authors

The present paper is theorem-rich and its strength lies partly in showing that several superficially similar resources are actually distinct. Compressing the complete story to PRL length risks either:

- hiding essential assumptions;
- suppressing the finite-radius / zero-radius transition;
- dropping the arbitrary-support bridge that protects the result from a natural referee objection;
- overstating broad significance to compensate for missing detail.

### When PRL would become justified

A PRL version becomes attractive only if one central statement can be shown to have broad consequence beyond the immediate quantum-resource/metrology community. For example, if the final narrative establishes convincingly that

> any autonomous finite quantum system carrying relative temporal information obeys a sharp two-regime spectral-resource principle even when the total state has exactly zero time-translation asymmetry,

and the result can be established cleanly in a 3750-word core without depending on the mixed shorted-operator machinery in the main text.

At present this is plausible but not sufficiently established to make PRL the primary route.

## Physical Review Research

PRResearch is fully in scope and accepts high-quality significant physics across disciplines, but it is not preferred over PRA for this manuscript unless a fully open-access general-physics route is specifically desired. The paper has a clear specialist home in quantum information/foundations/metrology, where PRA offers a sharper readership match.

Official source:

- https://journals.aps.org/prresearch/about

## Current target ranking

1. **PRX Quantum Research Article** — highest defensible target; significant desk-rejection risk; frame as exceptional connection/insight.
2. **Physical Review A Regular Article** — strongest robust fit and natural transfer/fallback.
3. **Physical Review Letters** — prestige stretch only after a successful independent compression/broad-interest gate.
4. **Physical Review Research** — scientifically valid but less targeted than PRA.

## Manuscript changes required for PRX Quantum

### Abstract

Remove most technical machinery names. Lead with the conceptual problem and the two-regime result. Keep:

- global stationarity / purely relational temporal information;
- local-Fisher high-frequency no-go;
- finite-radius survival resource;
- rank-changing synthesis action;
- arbitrary finite-copy collective measurements;
- sharp fixed-shell and multi-frequency constructions.

Move “shorted endpoint geometry,” `Psi`, and the qutrit accessibility hierarchy out of the abstract.

### Introduction

The first page should answer, in this order:

1. Why autonomous temporal information is a physical-resource problem.
2. Why global asymmetry is insufficient in a stationary relational clock.
3. Why Fisher information alone is insufficient at high frequency.
4. What resource replaces each failed quantity.
5. What is genuinely new relative to Page--Wootters, asymmetry/QFI resource theory, WAY/coherence costs, rank-changing Bures geometry, and waveform/energy-constrained metrology.

The introduction should not narrate WP01--WP20.

### Main theorem structure

For a PRX Quantum read, emphasize four conceptual results rather than eight technical statements:

1. **Local no-go + finite-radius repair.**
2. **Autonomous two-sided survival.**
3. **Boundary transition to sharp two-sided synthesis action.**
4. **Robustness/generalization: arbitrary coherent support and multi-gap sharp sum.**

The shorting and `55/8` material should stay mainly in the supplement as robustness evidence.

### Popular Summary

PRX Quantum uses a nontechnical Popular Summary. Its existence is useful as an internal significance test: if the two-regime principle cannot be explained without `R_lin`, `Psi`, QFI, or shorted operators, the framing is not yet broad enough for PRX Quantum.

## Submission decision gate

Submit first to PRX Quantum only if, after prose compression, all of the following remain true:

- the central two-regime claim fits in two sentences;
- the fixed-shell examples make the result physically intuitive rather than only algebraically sharp;
- the distinction from existing asymmetry/QFI/WAY/energy-metrology results is explicit within the first two pages;
- the paper can defend “exceptional insight” or “exceptional connection” without claiming priority for standard ingredients;
- no final priority search finds an equivalent finite-radius/zero-radius relational theorem.

Otherwise target PRA directly rather than weakening scientific precision to chase selectivity.
