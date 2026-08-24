# WP11 — R3 render audit and R4 presentation freeze

**Date:** 2026-08-23

**Status:** R3 SCIENTIFIC/PUBLICATION BUILD PASS; R4 presentation-only verification ACTIVE.

## Purpose

Close the second hostile manuscript audit at the exact built-PDF level, then remove one non-scientific presentation defect (visible hyperlink borders) without changing scientific content.

## R3 exact verification

Disposable verification PR: `#35` — must never be merged.

Workflow run: `32684317367`

Job: `97306449423`

All steps passed:

1. static first-draft provenance/integrity gate;
2. deterministic R1 mechanical generation;
3. deterministic R2 support-theorem generation;
4. R2 scientific-isolation gate;
5. deterministic R3 hostile-review repair generation;
6. R3 whole-file isolation gate;
7. R3 LaTeX compile;
8. unresolved-reference/citation and overfull-box gate;
9. artifact upload.

Artifact:

- ID: `9505151860`
- name: `practical-temporal-information-r3`
- archive size: `312177` bytes
- archive digest: `sha256:f6463ec3928f873acc2e5b11b964c71093337f8ca901b0eff511274bc7aa044b`

Exact built R3 PDF:

- file: `operational_temporal_information_r3.pdf`
- pages: `8`
- bytes: `266067`
- SHA-256: `b1816af4811e900f05fa56eac4141d16ed617441f52c855b94eae6b571b475af`

## Render audit

The exact artifact PDF was rendered at 180 dpi and every page inspected.

PASS:

- no clipped text;
- no overlaps;
- no broken glyphs;
- no black squares;
- no equation overflow;
- no missing references/citations;
- theorem/proof block legible;
- stationary-spectator and incoherent-seed qualifications legible;
- noncircular `R_lin` tomography protocol legible;
- equal-frequency resonant Hamiltonian clarification legible;
- Type-II and unitary-coupling results remain visibly attributed to companion manuscripts.

One non-scientific presentation issue remains: default `hyperref` draws visible red/green/cyan link rectangles around internal references, citations, and bibliography links. These are not a correctness problem but make the PDF look unfinished.

## Second hostile scientific audit — final findings

### Support theorem coefficient — PASS

Frozen flagship Theorem 1 defines `P_U,nu` and `P_D,nu` as the endpoint projectors supporting the **range and domain of the particular +nu tangent**, not global energy-tail projectors. Because the practical tangent acts only from the selected carrier to the selected sideband,

`P_U,Omega = |s><s|`,

so

`U_Omega = Tr(rho_p |s><s|) = p`

exactly, regardless of population in inert stationary spectator modes. Therefore

`(R_lin^2/4) Tr F <= p`

is the correct one-copy specialization even with arbitrary allowed spectators.

### Spectator zero modes — PASS

The tangent is identically zero on the spectator block, so zero eigenvalues or rank deficiency inside the inert spectator sector do not reduce the affine radius. Positivity of the affine family reduces to positivity of the selected carrier/sideband block plus the unchanged positive spectator block.

### Boundary POVM — PASS

The four weighted equatorial effects sum to the identity on the selected two-mode subspace; adding the spectator projector completes a valid POVM. It gives

`F_xx=F_yy=2 q kappa^2`, `F_xy=0`,

hence

`Tr F=4 q kappa^2=Delta P_s(0)`.

### Conventional detector example — PASS

The equal-DC-NEP/equal-response-bandwidth example remains algebraically correct and is presented as an illustrative specification-incompleteness example, not as a new theorem.

### Memory provenance — PASS

The Type-II rate/Fisher singularity theorem is explicitly introduced as a companion result and the manuscript explicitly denies novelty for generic timestamp/dead-time information theory.

### Unitary-coupling provenance — PASS

The resonant exchange section is explicitly a standard benchmark of the separate companion implementation theorem. R3 now states the equal-frequency free Hamiltonian

`H_0=hbar nu(N_C+N_S)`

before invoking a fixed bare-energy shell and states that unequal bare frequencies require an explicit pump/controller for global energy conservation.

### Prior-art boundary — PASS with narrow claim

The manuscript explicitly cites Gefen--Rotem--Retzker (2019) and Safranek (2017) for finite Fisher information from quadratically vanishing boundary probabilities/eigenvalues. The claimed added content is limited to the finite-seed finite-radius continuation

`4p/R_lin^2 -> Delta P_s(0)`

plus the operational/falsification architecture.

Priority remains **unverified, not certified**.

## R4 presentation-only layer

Files:

- `manuscript/practical_temporal_information/apply_r4_presentation_cleanup.py`
- `manuscript/practical_temporal_information/check_practical_r4.py`

R4 is generated from R3 by adding exactly

`\\hypersetup{hidelinks}`

after the existing `hyperref` package line. The R4 gate reconstructs the complete expected file from R3 and rejects any other byte change.

No word, equation, reference target, theorem, proof, citation, disclosure, or bibliography entry is allowed to change in R4.

## Immediate work order

1. obtain green R4 CI;
2. download exact R4 artifact;
3. record artifact/PDF hashes and page count;
4. render all pages and confirm link rectangles are gone with no visual regression;
5. close PR #35 unmerged;
6. synchronize all practical/root landing files to the R4 freeze;
7. begin figure production only after that synchronization.
