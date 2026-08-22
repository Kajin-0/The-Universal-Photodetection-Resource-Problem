# Manuscript Rev9 spectral-resource preflight — 2026-08-22

## Verdict

**PASS — Rev9 is the preferred PRX Quantum manuscript.**

Working title:

**Spectral Resource Laws for Temporal Fisher Information**

Rev9 is a genuine scientific revision, not a packaging/polish pass. It retains the Rev8 finite-copy survival theorem and controlled-continuum law, and adds two new theorem layers:

1. **WP26:** the retention spectrum of any one fixed one-copy POVM is a normalized positive-definite Herglotz sequence, producing cross-harmonic consistency and a divergent near-lossless energy law;
2. **WP25:** exact one-copy saturation on the full contiguous pure-sector chain is completely classified by geometric mixtures / Hausdorff moment tails, with a corresponding completely monotone continuum equality cone.

## Theorem hierarchy

### A. Arbitrary finite-copy modewise law

For any finite `N` and any joint POVM,

`Tr F_N^(k) <= N min(D_k,U_k) <= N T_k`,

`T_k=sum_(m>=k)q_m`.

Hence

`R_N(k)<=T_k`,

`sum_(k>=1)R_N(k)<=nbar`.

This is unchanged from the WP20/WP24 theorem.

### B. Controlled periodic-to-continuum survival law

For controlled periodic-to-continuum limits,

`R(nu)<=Pr(Omega>=nu)`.

The resource is mean **excess** energy above the participating lower edge,

`Ebar+=hbar <Omega>`.

The area and pointwise `hfR` inequalities remain first-moment corollaries. No unqualified theorem for every nonperiodic continuous-spectrum experiment is claimed.

### C. Fixed one-copy common-measurement Herglotz law — WP26

For any fixed one-copy POVM, after purification and harmless completion of zero-population sector labels,

`R_M(k)=int cos(k theta) J_M(dtheta)`

for a symmetric probability measure `J_M`.

Therefore every Toeplitz matrix `[R_M(i-j)]` is positive semidefinite.

For `q=R_M(k)` and `theta_q=acos(q)`, spherical-angle geometry gives

`R_M(mk)>=cos(m theta_q)`

whenever `m theta_q<=pi`. The high-retention proof uses only the positive-cosine range

`1<=m<=floor[pi/(2 theta_q)]`.

Combining this with monotonicity of the source tails over whole `k`-blocks gives

`nbar>=k A(q)`,

where

`A(q)=sum_(m=1)^M cos(m theta_q)`

and

`A(q)~1/sqrt(2(1-q))`

as `q->1`.

Thus

`Ebar+ >= hbar nu A(q)`

and asymptotically

`Ebar+ >= hbar nu / sqrt(2(1-q)) [1+o(1)]`.

Exact `q=1` at nonzero frequency is impossible for any normalized semibounded source; unit retention is an unattainable limit.

**Scope:** this cross-frequency theorem is presently one-copy/common-measurement. Do not extend it to arbitrary entangled `N>1` collective measurements without a new proof. The finite-copy *modewise* theorem remains valid.

### D. Complete one-copy extremizers — WP25

On the full contiguous pure-sector chain with `q_n>0`, the following are equivalent:

1. some POVM saturates the first-harmonic tail ceiling;
2. `q_n` is a mixture of geometric pmfs;
3. `T_k` is a Hausdorff moment sequence / completely monotone sequence;
4. one source-adapted POVM saturates every harmonic simultaneously.

The saturating infinite-dimensional POVM is defined directly through bounded matrix elements; the earlier potentially unbounded `rho^(-1/2)` shorthand is not used.

Product measurements give finite-copy sufficiency, but no entangled finite-copy converse is claimed.

### E. Completely monotone continuum equality cone

Mixtures of exponential excess-frequency densities have completely monotone survival laws and are exactly saturable in every exact lower-bin periodic approximant. Controlled continuum limits therefore satisfy `R(nu)=S(nu)` for this class.

The old exponential-energy/Cauchy-time family is the extreme-point case. Gamma mixing produces exact algebraic-tail examples.

## Hostile-audit defects found and repaired

1. **Invalid recycled cosine lobes.** An intermediate WP26 draft informally suggested `[cos(m theta_q)]_+` for all `m`. This is not justified after `m theta_q>pi`; spherical-angle geometry only yields the cosine lower bound while the angle remains within `[0,pi]`. Rev9 uses only the rigorous positive-cosine range `m theta_q<=pi/2`.
2. **Endpoint language.** `R=1` was initially described only as an infinite-energy limit. The stronger correct statement is that exact unit retention at any nonzero harmonic is impossible for a normalized semibounded source; the energy divergence concerns `R->1`.
3. **Infinite-dimensional POVM shorthand.** The formal source-adapted `rho^(-1/2)` construction can involve generalized phase vectors. Rev9 instead defines the POVM weakly by explicit matrix elements and proves positivity and normalization directly.
4. **Abstract bloat.** The first integrated Rev9 abstract was about 430 words. It was compressed to approximately 220 words to foreground the four significance-changing results rather than reciting the entire paper.

## Prior-art boundary

The following mathematics is explicitly prior art and is not claimed as new:

- Herglotz and Bochner representation theorems;
- Toeplitz positive definiteness;
- Hausdorff moment theorem;
- complete monotonicity;
- mixtures of geometric/exponential distributions;
- Bernstein--Widder representation;
- unilateral/backward-shift eigenvectors;
- trace-class Radon--Nikodym theory;
- canonical phase distributions/POVMs.

The candidate contribution is their operational quantum-statistical coupling:

- one actual POVM's classical temporal Fisher-retention spectrum is positive definite across harmonics;
- this forces cross-harmonic retention propagation;
- semibounded energy-tail monotonicity converts that into a divergent near-lossless resource law;
- equality in the modewise Fisher-tail theorem has a complete moment-theoretic rigidity classification.

Targeted literature searches through 2026-08-22 did not identify an exact predecessor. **Priority remains unverified, not certified.**

Recent adjacent work includes Nishiyama and Hasegawa, *Unified speed limits in classical and quantum dynamics via temporal Fisher information*, Phys. Rev. E 114, 014120 (2026), which concerns dynamical speed limits/costs rather than random-time source-to-record retention.

## Numerical validation

Committed validators:

- `grand_challenge/numerics/verify_operational_tail_bound.py`
- `grand_challenge/numerics/verify_truncated_gaussian_photon_example.py`
- `grand_challenge/numerics/verify_complete_monotone_saturation.py`
- `grand_challenge/numerics/verify_herglotz_high_retention.py`

The WP26 validator checks random Toeplitz PSD instances, the corrected positive-cosine angle propagation, the block-tail inequality on exact equality sources, the finite cosine-sum formula, and convergence of `sqrt(1-q) A(q)` to `1/sqrt(2)`.

Numerics are validation only; all manuscript theorem claims are analytic.

## Deterministic generation

`Rev1 -> Rev2 -> Rev3 -> Rev4 -> Rev5 -> Rev6 -> Rev7 -> Rev8 -> Rev9 spectral integration -> Rev9 abstract compression`.

Rev9-specific files:

- `grand_challenge/manuscript/apply_rev9_spectral_resource_theory.py`
- `grand_challenge/manuscript/apply_rev9_abstract_compression.py`
- `grand_challenge/manuscript/rev9_spectral_theorems.tex`
- `grand_challenge/manuscript/figure1_operational_architecture_body_rev9.tex`

Dedicated CI now regenerates Rev9, runs all four validators, compiles the PRX package, and rejects stale scope/claim defects.

## Final local build

Full build:

`pdflatex -> BibTeX -> pdflatex -> pdflatex`

Result:

- pages: **11**;
- PDF size: **439,616 bytes**;
- SHA-256: `81425f8576b47013631ece20152d1e23837fed22a62441d389f2405c5851bf13`;
- unresolved citations/references: **0**;
- overfull hbox/vbox: **0**;
- undefined controls/fatal TeX errors: **0**;
- all 11 pages rendered at 200 dpi and visually inspected: **PASS**;
- revised Figure 1: **PASS**;
- Herglotz/high-retention section: **PASS**;
- extremizer classification section: **PASS**;
- bibliography continuation page: **PASS**.

The current connector does not establish that the latest branch-push GitHub Actions run completed, so no remote-run PASS is claimed.

## Freeze recommendation

**Freeze Rev9 as the preferred PRX Quantum manuscript.**

This revision materially changes the significance case. It is no longer only a sharp modewise energy-survival inequality. It now combines:

1. an arbitrary finite-copy modewise resource ceiling;
2. a global spectral-consistency law for one physical measurement;
3. a divergent resource requirement for near-lossless temporal information transfer;
4. a complete rigidity classification of exact one-copy extremizers;
5. a continuum completely-monotone equality cone.

Do not add further theory by default. A possible Airy/Dirichlet asymptotic sharpening exists as a separate research direction, but it should not delay Rev9 and has closer overlap with established optical phase-estimation asymptotics.
