# WP11 — R3 render audit and R4 presentation freeze

**Date:** 2026-08-23

**Status:** **PASS — R4 exact build/render freeze closed.** Scientific content is frozen through R3; R4 changes hyperlink presentation only.

## Purpose

Close the second hostile manuscript audit at the exact built-PDF level, then remove the one remaining non-scientific presentation defect (visible hyperlink borders) without changing scientific content.

## R3 exact verification

Disposable verification PR: `#35` — never merge.

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

R3 artifact:

- ID: `9505151860`
- name: `practical-temporal-information-r3`
- archive size: `312177` bytes
- archive digest: `sha256:f6463ec3928f873acc2e5b11b964c71093337f8ca901b0eff511274bc7aa044b`

Exact built R3 PDF:

- file: `operational_temporal_information_r3.pdf`
- pages: `8`
- bytes: `266067`
- SHA-256: `b1816af4811e900f05fa56eac4141d16ed617441f52c855b94eae6b571b475af`

## R3 render audit

The exact R3 artifact PDF was rendered at 180 dpi and every page inspected.

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

The only presentation defect was default `hyperref` drawing visible colored link rectangles.

## Second hostile scientific audit — final findings

### Support theorem coefficient — PASS

Frozen flagship Theorem 1 defines `P_U,nu` and `P_D,nu` as endpoint projectors supporting the **range and domain of the particular +nu tangent**, not global energy-tail projectors. Because the practical tangent acts only from the selected carrier to the selected sideband,

`P_U,Omega = |s><s|`,

so

`U_Omega = Tr(rho_p |s><s|) = p`

exactly, regardless of population in allowed inert stationary spectator modes. Therefore

`(R_lin^2/4) Tr F <= p`

is the correct one-copy specialization.

### Spectator zero modes — PASS

The tangent is identically zero on the spectator block, so zero eigenvalues or rank deficiency inside the inert spectator sector do not reduce the affine radius. Positivity reduces to the selected carrier/sideband block plus the unchanged positive spectator block.

### Boundary POVM — PASS

The four weighted equatorial effects sum to the identity on the selected two-mode subspace; adding the spectator projector completes a valid POVM. It gives

`F_xx=F_yy=2 q kappa^2`, `F_xy=0`,

hence

`Tr F=4 q kappa^2=Delta P_s(0)`.

### Conventional detector example — PASS

The equal-DC-NEP/equal-response-bandwidth example remains algebraically correct and is presented as an illustrative specification-incompleteness example, not as a novelty theorem.

### Memory provenance — PASS

The Type-II rate/Fisher singularity theorem is explicitly introduced as a companion result; the manuscript explicitly denies novelty for generic timestamp/dead-time information theory.

### Unitary-coupling provenance — PASS

The resonant exchange section is explicitly a standard benchmark of the separate companion implementation theorem. R3 states the equal-frequency free Hamiltonian

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

No word, equation, reference target, theorem, proof, citation, disclosure, or bibliography entry changes in R4.

## R4 exact verification

Workflow run: `32684526293`

Job: `97307019940`

Every step PASS:

1. first-draft static provenance/integrity;
2. R1 mechanical generation;
3. R2 theorem generation;
4. R2 scientific-isolation gate;
5. R3 hostile-review generation;
6. R3 exact whole-file gate;
7. R4 presentation generation;
8. R4 presentation-isolation gate;
9. R4 LaTeX compile;
10. unresolved-reference/citation and overfull-box gate;
11. artifact upload.

R4 artifact:

- ID: `9505218922`
- name: `practical-temporal-information-r4`
- archive size: `322116` bytes
- archive digest: `sha256:9905a2cbd4366d57731fc8f4a99c6f72a513629a8727257a43131e02efb96cce`

Exact R4 PDF:

- file: `operational_temporal_information_r4.pdf`
- pages: `8`
- bytes: `266068`
- SHA-256: `794cb1c52326dc1965e14ea8ccd15530b41b2e523ca501e88f081cf69d741a01`

## R4 render/diff audit

The exact R4 artifact PDF was rendered at 180 dpi and all eight pages were inspected.

PASS:

- no clipping;
- no overlaps;
- no broken glyphs;
- no black squares;
- no equation overflow;
- no visual regression;
- colored hyperlink rectangles are gone.

A direct 180-dpi render comparison of R3 versus R4 changed only tiny rectangular regions at former hyperlink-border locations. Per-page changed-pixel fractions were approximately `0.00027%` to `0.00511%`; the changed regions coincide with reference/citation/DOI link rectangles. This is consistent with the R4 byte-isolation gate and confirms presentation-only change.

## Freeze decision

**R4 is the current practical-manuscript freeze.**

Do not reopen theorem expansion. The next work is publication figures and later publication-style compression/packaging. Any scientific change after R4 requires a new explicit revision layer and a concrete blocking reason.

## Immediate work order

1. close disposable PR #35 unmerged;
2. synchronize all practical/root landing files to this R4 freeze;
3. produce the four planned publication figures with deterministic sources;
4. integrate figures through an isolated manuscript revision;
5. recompile/render/hostile-review the figure-integrated manuscript;
6. then do journal/submission compression and current-policy checks.
