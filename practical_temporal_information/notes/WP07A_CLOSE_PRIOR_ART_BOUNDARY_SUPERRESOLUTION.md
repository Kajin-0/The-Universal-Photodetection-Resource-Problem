# WP07A — Close prior art: quadratic vanishing populations and finite boundary Fisher information

**Date:** 2026-08-23

**Status:** novelty-boundary addendum to WP07. This does not collide with the selected-mode seed-regularization identity, but it rules out a broader novelty claim around second-order population generation at a rank boundary.

## Close source

T. Gefen, A. Rotem, and A. Retzker,

> **Overcoming resolution limits with quantum sensing**,
> Nature Communications 10, 4992 (2019),
> DOI `10.1038/s41467-019-12817-y`.

The paper develops a general superresolution criterion for quantum sensing near points of vanishing first-order distinguishability. In the relevant boundary mechanism, an eigenvalue/probability can vanish quadratically with a parameter while the ratio `(partial p)^2/p` remains finite, producing nonzero Fisher information even though the first derivative of the density operator vanishes at the limiting point. It also emphasizes nullification of projection noise as the physical mechanism and cites the known discontinuity/rank-change QFI literature.

## Consequence for Paper 4

Do **not** claim novelty for any of the following statements in isolation:

- a zero-probability outcome at a boundary can carry finite limiting Fisher information;
- a probability/eigenvalue generated as `theta^2` can produce finite FI;
- second-order population curvature can support finite boundary information;
- projection-noise suppression at a vanishing outcome can remove an apparent resolution singularity;
- rank-changing sensing can have finite FI despite vanishing first-order distinguishability.

Those mechanisms are established prior art.

## What remains distinct in the current program

The candidate Paper-4 result is narrower:

1. begin on the **interior** side with an experimentally controllable, nonzero spectral seed `p`;
2. compute the exact affine physical tangent radius `R_lin` controlling the finite-radius spectral-survival theorem;
3. remove the seed continuously while preserving a calibrated selected-mode coupling;
4. prove the exact regularization identity

   `lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`;

5. show that this survives arbitrary inert spectator populations, with `Delta P_s(0)=4 kappa^2 q` for selected carrier occupation `q`;
6. interpret the limit as the explicit connection between a **pre-existing spectral-survival resource** and the already-known boundary phenomenon of second-order population/Fisher information.

The novelty candidate is therefore the **survival-to-synthesis crossover and its physical-radius normalization**, not boundary Fisher information itself.

Priority for that crossover remains unverified, not certified.

## Manuscript requirement

The R2 support section should cite Gefen--Rotem--Retzker alongside the rank-change QFI literature and state explicitly that finite Fisher information from a quadratically vanishing population is known. The manuscript should then identify its added result as the finite-seed continuation and exact radius-normalized limit.
