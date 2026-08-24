# AGENTS.md

## Purpose

Durable handoff for The Universal Photodetection Resource Problem. The repository, not chat history, is authoritative.

## Active branch

`agent/practical-temporal-information-benchmarks`

The three mature temporal-information papers remain scientifically frozen. The fourth practical/falsifiability paper is now scientifically frozen at **R4** pending deterministic figure integration.

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `practical_temporal_information/AGENTS.md`
3. `practical_temporal_information/notes/WP11_R3_RENDER_AUDIT_AND_R4_PRESENTATION_FREEZE.md`
4. `practical_temporal_information/notes/WP10_R2_BUILD_AND_SECOND_HOSTILE_AUDIT.md`
5. `practical_temporal_information/notes/WP09_HOSTILE_MANUSCRIPT_AUDIT_AND_SPECTATOR_INDEPENDENT_CROSSOVER.md`
6. `practical_temporal_information/notes/WP07A_CLOSE_PRIOR_ART_BOUNDARY_SUPERRESOLUTION.md`
7. `manuscript/practical_temporal_information/README.md`
8. `manuscript/practical_temporal_information/MANUSCRIPT_ARCHITECTURE.md`

## Current Paper-4 freeze

Working title:

> **Operational temporal-information benchmarks for photodetection**

R4 final verification:

- run `32684526293` PASS;
- job `97307019940` PASS;
- artifact `9505218922`;
- archive digest `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`;
- exact PDF 8 pages / 266068 bytes;
- PDF SHA-256 `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`.

All pages rendered/inspected. R4 differs from R3 only by hidden hyperlink borders. Disposable PR #35 was closed unmerged. Zero open PRs.

## Frozen Paper-4 theorem

For stationary selected modes with `E_s-E_c=hbar Omega`,

`rho_p=a_p|c><c|+p|s><s|+sigma_p`,

where `[rho_p,H]=0`, spectators are stationary/inert, `a_p>p`, `a_p->q>0`, and `p` is an incoherent/phase-randomized sideband population seed,

`R_lin^2=a_p p/[kappa^2(a_p-p)^2]`.

The frozen flagship theorem specializes to

`(R_lin^2/4)Tr F<=p`.

At zero seed,

`Delta P_s(0)=4kappa^2 q`,

so

**`lim_(p->0+)4p/R_lin^2=4kappa^2 q=Delta P_s(0)`.**

The completed boundary POVM attains `Tr F=Delta P_s(0)`.

Do not loosen the hypotheses or expand the theorem without a concrete blocking defect.

## Novelty boundary

Finite FI from quadratically vanishing boundary probabilities/eigenvalues is prior art (Gefen--Rotem--Retzker 2019; Safranek 2017). The candidate distinct content is the finite-seed/finite-radius continuation and the independent measurement/falsification architecture.

Priority remains **unverified, not certified**.

## Provenance

- Type-II memory theorem: frozen random-time companion; operational benchmark only here.
- Exact prescribed-curvature coupling theorem: frozen PRA companion; equal-frequency resonant benchmark only here.
- NEP/FI, Poisson/jitter, colored-noise example, weak phase modulation, and beam-splitter mechanics: standard/illustrative material.

Never duplicate companion proofs or move their novelty claims into Paper 4.

## Falsification hierarchy

1. Level I — detector/state/model reduction failure.
2. Level II — resource-law challenge only after independently verifying theorem assumptions and resource quantities.
3. Level III — failure of an ideal saturating model/equality.

## Immediate work order

**WP12: publication figures.**

Create at most four deterministic scientific figures with committed generation scripts and data checks:

1. equal conventional detector specs / unequal information spectra;
2. common Type-II saturation / different timestamp information;
3. stationary support-seed survival→synthesis crossover — principal figure;
4. equal-frequency resonant implementation + calibration/falsification map.

Do not change R4 scientific text while designing figures. Integrate figures through a new isolated manuscript revision only after the figure package itself passes numerical and visual QA.

Then rebuild/render/hostile-review and proceed to publication compression / fresh APS policy checks.

## Documentation rule

Every material result or scope change must update its WP note, practical handoff, root `README.md`, this file, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
