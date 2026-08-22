# The Universal Photodetection Resource Problem

**Current status: 2026-08-22**

`main` is the repository landing/index branch. Detailed Grand Challenge derivations live on `agent/temporal-information-resource-law`.

## Project split

1. **Paper 1 / Rev11** — frozen and technically validated.
2. **Paper 2 / Rev7** — frozen preferred science draft.
3. **Grand Challenge** — science checkpoint **WP24**; preferred manuscript **Rev4**, locally build-verified and frozen unless a concrete defect appears.

Authoritative active handoff: `grand_challenge/AGENTS.md` on `agent/temporal-information-resource-law`.

# Strongest current theorem

For the exact periodic random-time experiment with sector probabilities `q_n`, define

`T_k=sum_(m>=k)q_m`.

For **any finite number N of independently encoded excitations and any joint POVM**, including arbitrary entangled collective measurements,

`Tr F_N^(k)<=N T_k`.

More sharply,

`R_N(k):=Tr F_N^(k)/N<=min(D_k,U_k)<=T_k`,

and

`sum_(k>=1)R_N(k)<=nbar`.

The quantity `R_N(k)` is the two-quadrature / phase-averaged source-normalized Fisher retention. A scalar-retention guarantee that must hold for every sinusoidal phase obeys the same ceiling.

WP20 proves the theorem directly by Hilbert--Schmidt Cauchy--Schwarz, including arbitrary finite-copy collective readout.

## Controlled continuum form

For a positive excitation-frequency spectral probability measure `mu` with finite mean, controlled large-period limits of exact periodic approximants satisfy

`R(nu)<=mu([nu,infinity))=P(Omega>=nu)`.

Hence

`int_R R(nu)dnu<=2Ebar^+/hbar`,

and

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

The geometric-sector / exponential-spectrum canonical phase-time family attains the operational coefficient exactly.

## Physical source-to-record scope

WP23 proves the same normalized law for an independent quantum-marked compound-Poisson source followed by arbitrary parameter-independent source-to-bosonic-field formation, wavepacket overlap, coherent detector memory, ancillas, and final measurement.

This is an independent-event source theorem, not a theorem for every field with Poisson photocount statistics.

# Secondary QFI envelope and scope boundary

WP10/WP12/WP15 remain correct as separately optimized SLD-QFI metric bounds,

`sum_(k>=1)G_Q(k)<=2nbar`,

`int_R G_Q(nu)dnu<=pi Ebar^+/hbar`,

but they are secondary to the sharp operational `2E/hbar` law. WP16 identifies the `pi/4` analytic operator norm as established Hardy--Hilbert mathematics.

WP14 proves baseline mean energy does not constrain arbitrary parameter-dependent coherent waveform synthesis. Broader waveform-state theorems require explicit encoding/control/action resource accounting.

# Prior-art boundary

Weighted `U(1)` twirling/energy-gap modes, canonical phase measurements, phase estimation under photon-number constraints, arbitrary-measurement quantum-information bounds, random-unitary probability estimation, waveform QFI, and the sharp mathematical inequalities used in earlier WPs are prior art.

The candidate contribution is narrowly the arbitrary-measurement **classical-Fisher tail law** for Fourier perturbations of a latent random-time distribution, its paired-population/mean-energy resource interpretation, and source-to-record consequences.

Targeted searches have not located an exact predecessor. **Priority remains unverified, not certified.**

# Preferred Grand Challenge manuscript — Rev4

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

On the active branch, Rev4 is generated deterministically by

`Rev1 -> Rev2 mechanical -> Rev3 hostile-review repair -> Rev4 final polish`.

Verified status:

- full local LaTeX/BibTeX build: PASS;
- 7 pages;
- unresolved citations/references: 0;
- overfull boxes: 0;
- undefined controls/fatal TeX errors: 0;
- seven-page visual inspection: PASS;
- deterministic random-POVM theorem validation committed;
- DOI/title/provenance bibliography audit completed.

The bibliography audit corrected one real metadata defect: DOI `10.2140/apde.2011.4.379` is Oana Pocovnicu's *Traveling waves for the cubic Szegő equation on the real line*, which is also the correct source for the sharp positive-frequency Gagliardo--Nirenberg inequality used as mathematical prior art.

The current connector does not expose the relevant branch-push GitHub Actions run, so direct remote-job inspection is not claimed. Equivalent full local build verification is complete.

**Rev4 is frozen unless a concrete theorem, priority, build, or referee-level defect is found.**

## Replacement-agent recovery

Switch to `agent/temporal-information-resource-law`, then read:

1. `grand_challenge/AGENTS.md`
2. `grand_challenge/notes/MANUSCRIPT_REV4_LOCAL_BUILD_AND_HOSTILE_REVIEW_2026-08-22.md`
3. `grand_challenge/notes/MANUSCRIPT_REV4_BIBLIOGRAPHY_PROVENANCE_AUDIT_2026-08-22.md`
4. `grand_challenge/notes/WP24_INTEGRATED_HOSTILE_REVIEW_AND_SYMMETRY_PRIOR_ART_BOUNDARY.md`
5. `docs/CURRENT_RESEARCH_STATE.md`
6. `ROADMAP.md`

## Current work order

Do not accumulate another theorem by default. Continue with publication engineering only: remote CI inspection if accessible, a figure only if it materially improves comprehension, conservative priority language, and factual submission metadata when supplied.

## Documentation policy

`main` must always advertise the active branch and latest checkpoint. Detailed derivations may remain on the active branch, but project-level state must not be hidden from the default view.
