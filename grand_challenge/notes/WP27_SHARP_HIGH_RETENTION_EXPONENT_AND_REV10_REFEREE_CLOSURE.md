# WP27 — Sharp high-retention exponent and Rev10 referee closure

**Date:** 2026-08-22

## Status

Rev9 survived an external extreme adversarial re-review with no central mathematical failure. The review identified two narrow mandatory repairs and one optional significance opportunity:

1. state continuity at the origin before invoking Bochner in the continuum Herglotz extension;
2. keep the divergent high-retention law explicitly attached to a **fixed one-copy common POVM**;
3. test whether a finite-chain sine-profile family proves the `(1-R)^(-1/2)` divergence exponent is achievable.

All three are addressed in Rev10.

## 1. Mandatory scope/formal repairs

The continuum Herglotz sentence now assumes convergence to a normalized positive-definite function **continuous at the origin** before invoking Bochner's theorem. This is the standard regularity hypothesis needed for representation as the Fourier transform of a finite probability measure on `R`.

The Discussion now says explicitly that the second resource effect occurs when **one fixed one-copy detector POVM** is held fixed across frequencies. The finite-copy tail theorem remains more general and still covers arbitrary finite-copy entangled collective POVMs; the Herglotz/divergence theorem does not claim that level of collective-copy generality.

## 2. Sine-profile achievability family

For each integer `L>=2`, define

`theta_L = pi/(L+1)`

and amplitudes

`a_n = sqrt(2/(L+1)) sin((n+1) theta_L)`,

for `n=0,...,L-1`, with `q_n=a_n^2` and zero population above `L-1`.

The amplitudes obey the path-eigenvector recursion

`a_(n-1)+a_(n+1)=2 cos(theta_L) a_n`,

with boundary values `a_-1=a_L=0`.

Multiplying by `a_n`, summing, and using normalization gives

`sum_(n=0)^(L-2) a_n a_(n+1)=cos(theta_L)`.

For the canonical phase POVM, first-harmonic two-quadrature Fisher retention is the squared adjacent-amplitude overlap, hence

`R_L(1)=cos^2(pi/(L+1))`.

Reflection symmetry `q_n=q_(L-1-n)` gives exactly

`nbar_L=(L-1)/2`.

Eliminating `L`,

`nbar_L = pi/[2 arccos sqrt(R_L(1))] - 1`.

As `R_L(1)->1`,

`arccos sqrt(R) ~ sqrt(1-R)`,

so

`nbar_L = pi/[2 sqrt(1-R_L(1))] [1+o(1)]`.

Equivalently,

`1-R_L(1) ~ pi^2/(4 nbar_L^2)`.

Thus the Rev9 lower law

`nbar >= A(R) ~ 1/sqrt(2(1-R))`

has the correct **power-law exponent**. There are normalized semibounded sources and one fixed one-copy measurement with energetic cost `Theta((1-R)^(-1/2))`. The exponent `1/2` is therefore sharp. The lower-bound constant `1/sqrt(2)` and the sine-family achievability constant `pi/2` do not coincide; no claim of a globally optimal asymptotic constant is made.

## 3. Prior-art discipline

Finite-support sine states are established phase-estimation/interferometric constructions. In particular:

- D. W. Berry and H. M. Wiseman, *Optimal States and Almost Optimal Adaptive Measurements for Quantum Interferometry*, Phys. Rev. Lett. 85, 5098--5101 (2000), DOI `10.1103/PhysRevLett.85.5098`.

Rev10 does **not** claim novelty for the sine state, its path-eigenvector recursion, or canonical phase estimation. Its role here is as an achievability witness for the new common-measurement retention--energy divergence law.

## 4. Numerical validator

`grand_challenge/numerics/verify_sine_profile_divergence_sharpness.py`

checks:

- normalization of the finite sine profile;
- exact adjacent overlap `cos(pi/(L+1))`;
- exact mean sector index `(L-1)/2`;
- the exact retention/resource relation;
- compatibility with the Herglotz/tail lower bound `nbar>=A(R)`;
- `nbar sqrt(1-R) -> pi/2`;
- `(1-R)nbar^2 -> pi^2/4`.

## 5. Rev10 manuscript delta

`grand_challenge/manuscript/apply_rev10_referee_closure.py` generates Rev10 from the compressed Rev9 source and:

1. switches the spectral input to generated `rev10_spectral_theorems.tex`;
2. inserts the Bochner continuity-at-origin hypothesis;
3. tightens the Discussion to `one fixed one-copy detector POVM`;
4. adds the sharp-exponent proposition and proof;
5. states in the compact abstract that the `(1-q)^(-1/2)` divergence exponent is sharp.

The central Rev9 theorems are otherwise unchanged.

## 6. Interpretation

Rev10 upgrades the high-retention statement from a one-sided divergence bound to a scaling law with a **provably optimal exponent**:

`Ebar+ = Omega((1-R)^(-1/2))`

and an explicit family with

`Ebar+ = O((1-R)^(-1/2))`.

Therefore the asymptotic resource exponent is `Theta((1-R)^(-1/2))` within the stated fixed-one-copy/common-measurement periodic setting.

This is the last scientific enhancement justified by the supplied re-review. Do not start a new constant-optimization project unless a later referee specifically requires it.
