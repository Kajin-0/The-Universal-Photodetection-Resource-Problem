# Grand Challenge Manuscript Rev4 — Local Build and Hostile Review

**Date:** 2026-08-22

**Scientific checkpoint:** WP24 integrated hostile review PASS

**Preferred manuscript science draft:** Rev4

**Status:** **Locally build-verified, bibliography-resolved, visually inspected, and manuscript-level hostile-read passed.** The available GitHub connector still does not expose the relevant branch-push workflow run, so this note does not claim that the remote GitHub Actions job was directly inspected.

---

## 1. Canonical generation chain

The manuscript remains reproducible from the committed science source:

1. `energy_survival_temporal_fisher_rev1.tex`
2. `apply_rev2_mechanical.py` -> Rev2
3. `apply_rev3_hostile_review.py` -> Rev3
4. `apply_rev4_final_polish.py` -> Rev4

The CI workflow is:

`.github/workflows/grand-challenge-manuscript-check.yml`

and now targets Rev4.

Rev4 is not a theorem-development revision. It changes no theorem inequality, proof constant, physical source class, or numerical result relative to the WP24 science state.

---

## 2. Full local build verification

The committed generation chain was reconstructed locally from repository source and executed in order.

Final build sequence:

`pdflatex -> BibTeX -> pdflatex -> pdflatex`

The container's `/usr/bin/bibtex` alternative link is broken, so the actual TeX binary `/usr/bin/bibtex.original` was used for the equivalent local BibTeX pass. This is an environment issue, not a manuscript issue.

Final Rev4 output:

- pages: **7**;
- media: US Letter, `612 x 792 pt`;
- final local PDF size: approximately **326 kB**;
- unresolved citations: **0**;
- unresolved references: **0**;
- overfull `hbox`: **0**;
- overfull `vbox`: **0**;
- undefined control sequences: **0**;
- fatal TeX errors: **0**;
- APS-incompatible `boxed{...}` markup in generated Rev4: **0**.

The PDF was rendered at 160 dpi with the repository PDF verification tooling and all seven page images were visually inspected. No clipping, overlap, broken glyph, equation collision, or bibliography-layout defect was found.

---

## 3. Concrete build defects found and repaired during Rev2–Rev4

The build audit found actual defects rather than only style issues.

### 3.1 REVTeX theorem/proof machinery

Rev1 used theorem/proof environments without a self-contained declaration. A REVTeX 4.2 micro-test established:

- `theorem` is not predefined;
- the opening `proof` command is not predefined;
- `endproof` is already supplied by REVTeX.

Rev2 now declares theorem/corollary and supplies only the missing opening proof command. It does not load `amsthm`.

### 3.2 APS `boxed` markup

Rev1 used `boxed{...}` as visual emphasis. Rev2 removes the wrapper while preserving its mathematical contents.

The first unboxing implementation retained wrapper-only line breaks and produced a blank paragraph inside display math, causing a fatal `Missing $ inserted` error. The generator now trims those wrapper-only line breaks.

### 3.3 Missing `cK` macro

The compound-Poisson event-register section used `cK` without defining it. Rev2 now declares the macro mechanically.

### 3.4 BibTeX case corruption of Szegő

APS BibTeX lowercased the unprotected title token `Szeg\H{o}` into invalid `\h{o}`, causing the post-BibTeX LaTeX pass to fail. The bibliography now protects the proper name as `{Szeg\H{o}}`.

### 3.5 Two-column theorem-heading overflow

The original long optional theorem subtitles generated overfull boxes of approximately 45 pt and 20 pt. Rev3 shortens only those subtitles to `Finite-copy Fisher bound` and `Continuum survival bound`. No theorem content changed.

---

## 4. Scientific/interpretive defects or ambiguities repaired in Rev3

### 4.1 Two-quadrature normalization made explicit

The principal operational quantity is

`R_N(k) = Tr F_N^(k) / N`.

Since the latent source Fisher block is `(1/2) I_2`, this equals the phase-average of the source-normalized scalar Fisher retention over sinusoidal phase.

If a detector guarantees scalar retention at least `q` for **every** sinusoidal phase, then both eigenvalues of `F_N^(k)/N` are at least `q/2`, hence `R_N(k)>=q`. Therefore the survival/energy theorem applies directly to a uniform phase-agnostic guarantee.

A pre-known single scalar quadrature is a different statistical task and is not assigned the same coefficient by the manuscript.

### 4.2 Poisson/spectral-measure notation collision removed

The continuum spectral probability measure remains `mu`; the independent Poisson mean is now `Lambda`.

### 4.3 Continuum convergence at atoms

The continuum proof now uses the explicit squeeze

`nu-epsilon <= k_delta delta <= nu`

and the corresponding closed-tail bounds before sending `epsilon -> 0`. This makes the stated closed-tail limit valid even at atoms.

### 4.4 SLD-QFI interpretation corrected

The paper now distinguishes:

- each scalar-quadrature SLD QFI;
- the SLD-QFIM trace;
- the classical Fisher trace of one actual POVM.

The `pi E/hbar` result is presented only as a separately optimized quantum-metric envelope, not as a jointly attainable broadband detector law.

### 4.5 Explicit arbitrary-waveform no-go

The source-class boundary is now shown with the explicit coherent-sideband family

`|psi_epsilon> = |alpha>_c tensor |epsilon gamma>_s`,

for which

`F_Q(0)=4|gamma|^2`

is independent of sideband detuning while

`Delta E(epsilon)=hbar(omega_c+nu)|gamma|^2 epsilon^2`.

This makes clear why baseline mean energy alone cannot control arbitrary parameter-dependent waveform-state synthesis.

---

## 5. Rev4 final claim/notation hardening

Rev4 makes only conservative scope/readability changes:

1. The abstract no longer introduces an overloaded energy-index symbol `N_E`; it writes the upper tail directly as `sum_(m>=k) q_m`.
2. The abstract explicitly says the exact finite-copy theorem is first formulated on a **periodic time coordinate with equally spaced generator sectors**.
3. The continuum statement is explicitly a **controlled large-period limit**, not an unqualified theorem for an arbitrary fixed nonperiodic detector experiment.
4. The Cauchy equality discussion now states separately:
   - characteristic function: `exp(-a|nu|)`;
   - timestamp Fisher retention: its modulus squared, `exp(-2a|nu|)`.
5. The continuous-outcome proof no longer says merely 'obvious measure-theoretic replacement'; it states the finite-measurable-coarse-graining route used to extend the discrete-outcome Cauchy--Schwarz inequality.
6. Discussion and conclusion retain the controlled-limit qualifier.

No theorem equation or numerical coefficient was changed.

---

## 6. Numerical theorem validation

The deterministic validation script

`grand_challenge/numerics/verify_operational_tail_bound.py`

uses fixed seed `20260822` and checks random rank-one frame POVMs for:

- one-copy systems with dimensions 2–5;
- global two-copy POVMs for dimensions 2–3;
- random energy-sector populations;
- support distributions with missing intermediate sectors;
- the tighter paired-support bound `Tr F_N^(k) <= N min(D_k,U_k)`;
- the coarse tail bound `<= N T_k`;
- the exact geometric/canonical-phase equality relation.

The earlier exploratory sweep reached approximately `0.934` of the tight one-copy bound and `0.849` for global two-copy random POVMs, with no violation. These maxima are validation diagnostics only, not theorem values.

CI now installs Python 3.12 and NumPy explicitly before running this script.

---

## 7. Final manuscript-level hostile review

No fatal scientific defect was found.

The manuscript's strongest claim is now kept narrow and supportable:

> For the periodic random-time statistical experiment, every finite-copy joint measurement has a two-quadrature temporal-harmonic Fisher trace bounded by paired energy-sector population and hence by the upper excitation-energy tail. Controlled large-period limits inherit the survival-function and mean-energy laws.

The manuscript does **not** claim:

- a baseline-energy theorem for arbitrary waveform-state synthesis;
- that every Poisson-counting optical field is an independent quantum-marked Poisson source;
- mathematical novelty for `U(1)` mode decomposition, weighted twirling, canonical phase POVMs, generic Fisher/QFI monotonicity, Hilbert--Schmidt Cauchy--Schwarz, or the Hardy--Hilbert `pi` constant;
- that the separately optimized SLD-QFI area is jointly attainable;
- a direct nonperiodic-continuum theorem without the stated controlled-limit construction.

Priority for the specific Fisher-tail theorem remains **unverified, not certified**, after targeted searches of phase estimation, phase diffusion/noise, random-unitary probability estimation, modes of asymmetry, and quantum statistical information inequalities.

---

## 8. Decision

**Rev4 is the preferred frozen science draft unless a concrete theorem, priority, build, or referee-level defect is found.**

The next work should not accumulate another theorem by default. High-value next tasks are publication engineering:

1. inspect the remote GitHub Actions Rev4 job if/when the connector exposes it;
2. decide whether a single conceptual figure materially improves comprehension;
3. perform journal-style bibliography/provenance verification at DOI/title level;
4. prepare submission metadata only when factual author/funding/disclosure information is supplied;
5. reopen the science only for a concrete defect or priority collision.
