# WP09 — Hostile manuscript audit and spectator-independent support crossover

**Date:** 2026-08-23

**Status:** one substantive strengthening identified. The first Paper-4 draft is structurally sound, but its central crossover proposition is unnecessarily specialized to a normalized two-level baseline. The result extends exactly to a selected carrier/sideband pair embedded in an arbitrary spectator sector. This removes the main concern that the Paper-4 novelty rests on a toy-state normalization.

## 1. Hostile question

The draft's principal new proposition uses

`rho_p=(1-p)|c><c|+p|s><s|`.

Its identity

`lim_(p->0+)4p/R_lin^2=Delta P_s(0)`

is exact, but a hostile referee could reasonably say that it follows from an unusually narrow two-level normalization and ask whether it survives when:

- only a fraction of the optical state occupies the selected carrier mode;
- other spectral modes are populated;
- the sideband seed is compensated by an arbitrary spectator redistribution rather than entirely by depletion of the carrier.

It does.

## 2. General seeded carrier/sideband model with spectators

Let `|c>` and `|s>` be orthogonal frequency modes separated by the relevant Bohr/sideband frequency. Let `H_perp` be the orthogonal spectator subspace.

For `p>0`, take a baseline

`rho_p = a_p |c><c| + p |s><s| + sigma_p`,

where:

- `sigma_p >=0` is supported on `H_perp`;
- `Tr sigma_p = 1-a_p-p`;
- `a_p>p` in the neighborhood of interest;
- `a_p -> q>0` as `p->0+`;
- `sigma_p` may vary with `p` in any way consistent with positivity and normalization;
- the local converter acts only on the `c-s` pair, so the spectator sector is dynamically inert for this benchmark.

Apply

`U(x,y)=exp{kappa[(x-iy)|s><c|-(x+iy)|c><s|]}`.

The spectator block remains unchanged.

## 3. Exact sideband population

The `c-s` block is an ordinary two-level rotation. Therefore

**`P_s(p;r)=p+(a_p-p) sin^2(kappa r)`**,

where `r=sqrt(x^2+y^2)`.

Thus

`P_s=p+(a_p-p)kappa^2(x^2+y^2)+O(r^4)`.

At the boundary `p=0`, with `a_0=q`,

`P_s(0;r)=q sin^2(kappa r)`

and hence

**`Delta P_s(0)=4 kappa^2 q`.**

The boundary curvature automatically scales with the actual population available in the selected carrier mode.

## 4. Exact affine physical radius

The first-order affine `c-s` block is

`[[a_p, kappa(a_p-p)(x+iy)], [kappa(a_p-p)(x-iy), p]]`

up to the harmless sign convention for the sine quadrature.

Its determinant is

`a_p p - kappa^2(a_p-p)^2(x^2+y^2)`.

The spectator sector is positive and uncoupled, so the affine physical radius is exactly

**`R_lin^2 = a_p p/[kappa^2(a_p-p)^2]`.**

For `p>0`, the finite-radius upper-endpoint survival theorem gives

**`(R_lin^2/4) Tr F <= p`.**

Equivalently,

**`Tr F <= 4 kappa^2 (a_p-p)^2/a_p`.**

## 5. Spectator-independent seed-regularization theorem

Using the exact radius,

`4p/R_lin^2 = 4 kappa^2 (a_p-p)^2/a_p`.

Since `a_p->q>0`,

**`lim_(p->0+) 4p/R_lin^2 = 4 kappa^2 q`.**

But Sec. 3 gives

`Delta P_s(0)=4 kappa^2 q`.

Therefore

> **Spectator-independent seed-regularization identity.** For any baseline family of the form above, with an arbitrary positive spectator sector and any continuous seed-compensation path satisfying `a_p->q>0`,
>
> `boxed: lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`.

The original normalized two-bin model is the special case

`a_p=1-p`, `sigma_p=0`, `q=1`.

## 6. Why this is materially stronger

The identity is not tied to a pure carrier baseline or to a two-dimensional total state space.

Experimentally, a selected carrier mode can have occupancy `q<1` because of:

- other spectral bins;
- polarization/spatial spectator modes;
- incoherent background populations included in the normalized state model.

Those spectators do not alter the crossover as long as the calibrated local converter acts only on the selected carrier/sideband pair. The boundary synthesis curvature simply becomes `4 kappa^2 q`.

This gives a direct measurement prescription:

1. measure the selected carrier population `a_p` and sideband seed `p`;
2. calibrate `kappa`;
3. compute/predict `R_lin` from the measured populations;
4. reduce `p` toward zero while tracking `a_p->q`;
5. independently fit the zero-seed sideband curvature;
6. test
   `4p/R_lin^2 -> Delta P_s(0)`.

The seed may be compensated elsewhere in the spectrum; it need not be transferred solely from the carrier.

## 7. Remaining hostile findings

### 7.1 The crossover is still a model theorem, not a universal seed theorem

The result assumes a lossless SU(2)-type local converter on a selected carrier/sideband pair and an inert spectator block. Loss, parameter-dependent decoherence, seed-dependent mode coupling, or correlated spectators can alter the exact formulas.

This is acceptable for Paper 4 because the point is an explicitly falsifiable standard-physics benchmark, not a universal theorem about arbitrary optical channels.

### 7.2 The finite-radius theorem coefficient was rechecked against frozen PRXQ source

The flagship proof gives, when the positive-frequency tangent range lies in upper endpoint projector `P_U`,

`(R_lin^2/4) Tr F_1 <= Tr(P_U rho_0)`.

For the seeded sideband model `Tr(P_U rho_0)=p`, so the Paper-4 coefficient is correct.

The same frozen proof uses

`R_lin=1/w(rho_0^{-1/2} A rho_0^{-1/2})`,

with the numerical-radius inequality producing the factor 4. No factor-of-two correction is needed.

### 7.3 The conventional detector A/B example is internally physical

Detector B's PSD is a positive white floor plus positive Lorentzian excess term. Its FI spectrum can exceed its dc value because the excess noise decays faster than the single-pole signal response. This is not an inconsistency.

### 7.4 Manuscript claim hierarchy remains appropriate

- WP04/WP09 crossover: candidate original Paper-4 theorem.
- Type-II memory theorem: companion result only.
- exact implementation lower bound: PRA companion result only.
- NEP/FI and Poisson/jitter: standard bridge/background.

## 8. Required manuscript repair

Before scientific freeze:

1. replace the narrow normalized two-bin proposition by the spectator-independent statement above;
2. retain the normalized `a_p=1-p` case as the simplest plotted/example specialization;
3. state explicitly that the result is exact for the selected two-mode unitary converter with inert spectators, not for arbitrary lossy optical channels;
4. keep the same falsification hierarchy.

This is a scientific strengthening, not merely prose polish.

## 9. Gate status

**HOSTILE SCIENTIFIC AUDIT: CONDITIONAL PASS.**

No defect was found in the central coefficient or limit. The principal repair is to generalize the crossover theorem before calling R1 scientifically stable.
