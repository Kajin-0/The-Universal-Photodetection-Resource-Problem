# Grand Challenge Manuscript Rev7 — Referee Hardening

**Date:** 2026-08-22

**Science checkpoint:** WP24

**Target:** PRX Quantum Research Article

**Preferred manuscript after this pass:** `grand_challenge/manuscript/energy_survival_temporal_fisher_rev7_prxq.tex`

## Verdict

**REV7 REFEREE-HARDENING PASS: PASS.**

The external adversarial review found no theorem-breaking defect. It independently judged the finite-copy Cauchy--Schwarz theorem, N-copy collective extension, tail-sum budget, geometric equality family, and Poisson/CPTP inheritance sound. Its substantive concerns were editorial/positioning risks for PRX Quantum: continuum scope, excess-energy terminology, distinction from modes-of-asymmetry theory, overemphasis of the `hf` first-moment corollary, and lack of a nonextremal photon example.

Rev7 addresses those points without broadening the theorem.

---

## What changed

### 1. Continuum claim discipline strengthened

The continuum section is now titled:

`Controlled periodic-to-continuum survival law`.

The theorem is explicitly a controlled-limit statement. Abstract, introduction, Figure 1, discussion, and conclusion all preserve this qualification.

No claim is made that the paper directly proves the continuum inequality for every arbitrary fixed nonperiodic continuous-spectrum experiment.

### 2. Resource identified as excess energy

The manuscript now states repeatedly that

`Ebar+ = hbar <Omega>`

is mean excitation energy **above the participating lower translation-sector edge**.

A common optical carrier-energy offset is not counted as the temporal information resource. The new single-photon example makes this explicit by writing

`omega = omega_* + Omega`, `Omega >= 0`,

where `hbar omega_*` contributes only a global phase in the one-photon sector.

### 3. Survival law promoted over the `hf` corollary

The principal continuum statement is

`R(nu) <= Pr(Omega >= nu)`.

The pointwise inequality

`Ebar+ >= hbar nu R(nu) = h f R(2 pi f)`

is explicitly described as an elementary first-moment/tail corollary after the nontrivial operational survival theorem is established.

### 4. Modes-of-asymmetry distinction sharpened

The manuscript now states the boundary directly:

- established modes-of-asymmetry theory identifies the kinematic energy-gap components available under `U(1)` symmetry;
- Rev7 instead bounds the **classical Fisher information extractable by any actual POVM** about a perturbation of the random-time mixing law;
- the coefficient is determined by paired participating populations / the upper survival tail;
- the finite-copy result includes arbitrary entangled collective measurements;
- one common canonical phase measurement saturates the full geometric harmonic hierarchy.

This is the principal novelty distinction and must remain explicit.

### 5. Added one nonextremal single-photon example

A new section, `Nonextremal single-photon wavepacket`, considers a transform-limited one-photon state with zero spectral phase and excess-frequency density

`q_sigma(Omega) = [sqrt(2/pi)/(sigma Z)] exp[-(Omega-sigma)^2/(2 sigma^2)]`,

`Z = erfc(-1/sqrt(2))`, `Omega >= 0`.

The survival function is

`S_sigma(nu) = erfc[(nu-sigma)/(sqrt(2)sigma)] / Z`.

For canonical covariant timing, obtained as the controlled limit of the discrete canonical phase POVM,

`R_time(nu) = [int_0^infinity sqrt(q_sigma(Omega) q_sigma(Omega+nu)) dOmega]^2`

and analytically

`R_time(nu) = exp[-nu^2/(4 sigma^2)] [erfc((nu/2-sigma)/(sqrt(2)sigma))/Z]^2`.

Numerical values quoted in the manuscript:

- `nu = 0.5 sigma`: `S = 0.8218539006`, `R = 0.7937545666`, `R/S = 0.9658098185` (~96.6% of ceiling);
- `nu = sigma`: `S = 0.5942867087`, `R = 0.5260361867`, `R/S = 0.8851555639` (~88.5%);
- mean excess frequency: `<Omega> = 1.2875999709 sigma`.

This is deliberately **not** an equality construction. It shows that the survival ceiling remains quantitatively restrictive for a smooth, nonextremal single-photon spectrum.

Two current time-frequency/single-photon references were added for physical context:

- Fabre, Keller, and Milman, Phys. Rev. A 105, 052429 (2022), DOI `10.1103/PhysRevA.105.052429`;
- Folge et al., Optica 13, 548–557 (2026), DOI `10.1364/OPTICA.579459`.

### 6. Figure 1 hardened

Rev7 uses a revision-specific architecture figure that labels:

- `controlled periodic-to-continuum limit`;
- survival law first;
- `hf` as a first-moment corollary;
- `Ebar+` as mean excess energy above the participating edge.

The source-class exclusion for arbitrary parameter-dependent waveform-state synthesis remains visible.

---

## Validation

### Analytic theorem status

The finite-copy theorem and proof are unchanged from the WP24/Rev4 science checkpoint:

`Tr F_N^(k) / N <= min(D_k,U_k) <= T_k`.

The controlled-limit survival inequality is also unchanged mathematically. Rev7 changes claim discipline, interpretation, and adds a worked example.

### Photon-example validation

Committed script:

`grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`

It checks:

1. normalization and mean of the truncated Gaussian;
2. numerical quadrature versus the closed-form survival and Hellinger-affinity formulas;
3. `R_time(nu) <= S_sigma(nu)`;
4. the exact quoted numerical values;
5. convergence of exact lower-bin periodic approximants to the continuum Hellinger-retention and survival formulas.

At spacing `delta = 0.005 sigma`, discrete canonical-phase retention agrees with the closed continuum values to better than `3e-7` at `nu = 0.5 sigma` and `nu = sigma`, while the discrete tail agrees to approximately `2e-12` over the finite numerical cutoff used.

### Final local LaTeX/BibTeX build

Full cycle:

`pdflatex -> BibTeX -> pdflatex -> pdflatex`

Status: **PASS**.

Final local PDF:

- pages: **8**;
- file size: **403,102 bytes**;
- SHA-256: `d168c3901faa6f29bda0eba71abe8049cc9819d91843273beeeeffb9443818ae`;
- unresolved citations/references: **0**;
- overfull boxes: **0**;
- undefined controls/fatal errors: **0**.

The first Rev7 build exposed two layout-only defects (an overlong corollary heading and a ~1 pt overfull line in the photon-example opening). `apply_rev7_layout_repair.py` repairs both and also makes the transform-limited/zero-spectral-phase convention explicit.

### Visual verification

All 8 pages were rendered at 200 dpi and inspected.

PASS:

- Figure 1 labels and equations readable;
- no clipping or overlaps;
- new single-photon equations fit the two-column layout cleanly;
- bibliography is clean;
- no visible hyperlink boxes;
- no page-level visual regression.

---

## Editorial decision

The adversarial review's three highest-value recommendations are now implemented:

1. continuum qualification sharpened;
2. modes-of-asymmetry distinction strengthened;
3. one realistic/nonextremal single-photon example added.

The excess-energy and `hf`-corollary issues were also repaired throughout the manuscript and figure.

The secondary QFI-envelope section remains because it provides a useful contrast between modewise quantum metric optimization and the one-measurement operational theorem. It remains explicitly secondary and no further expansion is recommended.

## Freeze recommendation

**Rev7 should replace Rev6 as the preferred PRX Quantum manuscript.**

Do not add additional theory, detector technologies, correlated-source extensions, squeezed-state extensions, or more examples by default. Reopen only for a concrete theorem defect, historical-priority collision, build defect, or new referee-level objection.
