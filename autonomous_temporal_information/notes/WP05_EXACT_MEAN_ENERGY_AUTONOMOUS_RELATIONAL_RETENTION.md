# WP05 — Exact mean-total-energy autonomous relational Fisher-retention law

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for one fixed one-copy record in the structured globally stationary relative-time experiment; exact equality construction obtained. Targeted searches have not identified this exact squared-posterior-sharpness/Fisher-retention optimization. Mathematical phase-estimation ingredients are prior art. Priority remains **unverified, not certified**.

## 1. Problem left by WP04

WP04 solved the hard total-energy cap exactly:

`R_M(1) <= cos^2[pi/(L+2)]`

when the autonomous clock--signal apparatus has no support above total excitation `L`.

A hard cap is stronger than a mean-energy constraint. The open question was:

> At fixed mean total excitation `Lbar`, what is the exact maximum one-copy Fisher retention of one autonomous relational record?

This is not automatically the standard mean-photon-number phase-estimation problem because the retention functional is

`R_M(1)=int |Tr(V X_y)|^2 p(dy)`,

i.e. an average of **squared posterior sharpness**, and the posterior total-energy distribution may depend on the measurement outcome.

## 2. Total-energy shell decomposition

Let total-excitation shells be indexed by integers `L=0,1,2,...`.

Inside shell `L`, the exchange coordinate has basis

`|L-n>_C |n>_S`, `n=0,...,L`,

and finite shift `V_L`.

The full relative shift is the direct sum

`V = directsum_(L>=0) V_L`.

For an arbitrary posterior density operator `X_y`, pinching in total energy does not change either

`Tr(V X_y)`

or its total-energy expectation. Let

`w_(y,L)=Tr(P_L X_y)`

and, for nonzero weight, `X_(y,L)=P_L X_y P_L/w_(y,L)`.

Then

`Tr(V X_y)=sum_L w_(y,L) Tr(V_L X_(y,L))`.

## 3. Shellwise sharpness bound

WP04 / finite-shift operator theory gives

`|Tr(V_L X_(y,L))| <= c_L`,

where

`c_L=cos[pi/(L+2)]`.

Therefore

`|Tr(V X_y)| <= sum_L w_(y,L) c_L`.

Squaring and using convexity of `x^2` on nonnegative numbers gives

`|Tr(V X_y)|^2`

`<= [sum_L w_(y,L)c_L]^2`

`<= sum_L w_(y,L)c_L^2`.

Define

`g_L := c_L^2 = cos^2[pi/(L+2)]`.

Thus, pointwise in every outcome,

`|Tr(V X_y)|^2 <= sum_L w_(y,L) g_L`.

## 4. Posterior averaging collapses to the baseline energy distribution

The posterior decomposition obeys

`int X_y p(dy)=rho0`.

Hence

`int w_(y,L) p(dy)=Tr(P_L rho0)=:W_L`,

the **baseline total-energy shell probability**.

Therefore

> `R_M(1) <= sum_(L>=0) W_L g_L`.

This removes the measurement-dependent posterior energy distribution completely. The right-hand side depends only on the baseline total-energy distribution.

This step is the key distinction from ordinary point-estimation bounds: arbitrary outcome-dependent posterior reshuffling cannot beat the baseline-weighted finite-shell Fisher-retention ceilings.

## 5. Discrete concavity of the shell ceiling

The sequence

`g_L=cos^2[pi/(L+2)]`

is discretely concave.

At the boundary,

`g_0=0`, `g_1=1/4`, `g_2=1/2`,

so

`g_2-2g_1+g_0=0`.

For real `x>=1`, the continuous extension

`g(x)=cos^2[pi/(x+2)]`

has

`g''(x) = -2 pi [(x+2) sin(2pi/(x+2)) + pi cos(2pi/(x+2))]/(x+2)^4 <0`.

Hence all subsequent discrete second differences are negative. Therefore `{g_L}` is a concave sequence on the nonnegative integers.

## 6. Exact sharp mean-energy envelope

Let the mean total excitation be

`Lbar=sum_L L W_L`.

Write

`Lbar=m+lambda`,

`m=floor(Lbar)`, `0<=lambda<1`.

For a concave sequence, the maximum of

`sum_L W_L g_L`

subject to normalization and fixed mean occurs on the two neighboring integers `m,m+1`.

Define the piecewise-linear concave interpolation

`G(Lbar)=(1-lambda) g_m + lambda g_(m+1)`.

Then:

> **Exact mean-total-energy relational retention law**
>
> `R_M(1) <= G(Lbar)`
>
> for every fixed one-copy POVM in the structured globally stationary relative-time experiment.

Equivalently, with

`Ebar_tot^+=Ebar_C^+ + Ebar_S^+ = hbar nu Lbar`

for the fundamental exchange quantum `nu`,

`R_M(nu) <= G(Ebar_tot^+/(hbar nu))`.

This is an exact finite-resource law for arbitrary real mean energy, not only integer hard caps.

## 7. Exact equality construction

Let

`Lbar=m+lambda`.

Prepare a baseline classical mixture of two orthogonal total-energy shells:

- shell `m` with weight `1-lambda`;
- shell `m+1` with weight `lambda`.

Within each shell use the sine-chain relative-time seed

`|Psi_L>=sum_(n=0)^L sqrt[2/(L+2)] sin[(n+1)pi/(L+2)] |L-n>_C|n>_S`.

Uniform relative-phase twirling gives the separately stationary baseline required by the local experiment.

Use one fixed globally time-translation-invariant POVM that first resolves the total-energy shell and then performs the canonical relative-phase POVM inside that shell.

The shellwise retentions are exactly `g_m` and `g_(m+1)`, so the total retention is

`R=(1-lambda)g_m + lambda g_(m+1)=G(Lbar)`.

Thus the bound is **globally sharp for every mean total energy**.

No unproved optimality conjecture remains in this one-copy structured setting.

## 8. Near-lossless asymptotic constant

For large `L`,

`g_L = 1 - pi^2/(L+2)^2 + O(L^-4)`.

The piecewise-linear interpolation has the same leading asymptotic behavior. Hence

`1-R >= pi^2/Lbar^2 [1+o(1)]`,

or

> `Ebar_tot^+ >= pi hbar nu / sqrt(1-R) [1+o(1)]`.

The adjacent-shell sine mixture attains this same coefficient.

Therefore the inverse-square-root divergence and leading constant `pi` are both **sharp under a mean total-energy constraint** for the one-copy structured autonomous relative-time experiment.

## 9. Comparison with WP03

WP03's generic arbitrary-tangent theorem gives

`Ebar_tot^+ >= 2 hbar nu K_N(nu)`

and, with additional Herglotz structure, a weaker first-moment near-lossless coefficient based only on local survival tails.

WP05 is stronger because it uses the full structured relative-time experiment and the exact finite-shell exchange geometry.

The hierarchy is therefore:

- arbitrary robust exact exchange tangent, arbitrary finite N: dual survival / factor-2 mean-energy law;
- structured one-copy relative-time hierarchy, mean total energy fixed: exact piecewise-linear cosine-squared law with sharp asymptotic constant `pi`.

Do not apply the WP05 constant to arbitrary tangents or arbitrary collective-N measurements without a separate proof.

## 10. Prior-art boundary

The ingredients

- finite unilateral-shift numerical radius;
- sine states;
- canonical phase measurements;
- Heisenberg-style phase estimation under generator constraints

are established mathematics/physics. Berry, Hall, Zwierz, and Wiseman, Phys. Rev. A 86, 053813 (2012), DOI `10.1103/PhysRevA.86.053813`, prove strong average phase-estimation bounds and asymptotic constants for phase-error metrics.

Adaptive phase-estimation literature also uses expected posterior sharpness as an optimization criterion.

Targeted searches did **not** identify the exact theorem derived here for

`average squared posterior shift expectation = temporal Fisher retention`

under a mean **total clock+signal energy** constraint in a globally stationary relational experiment.

Accordingly, the phase-estimation mathematics must be cited as prior art, while the autonomous Fisher-retention optimization is the candidate contribution. Priority remains **unverified, not certified**.

## 11. Consequence for the grand program

The resource hierarchy now has an unexpectedly clean autonomous interpretation:

1. local Fisher alone can evade energy constraints by shrinking its physical tangent radius (WP02);
2. genuinely relational information requires matched energy survival in clock and signal (WP03);
3. for a structured autonomous relative-time record, finite total energy imposes an exact information-retention ceiling (WP04);
4. that ceiling remains exactly solvable under **mean**, not merely maximum, total energy (WP05).

This is the first point at which the new program has a fully sharp finite-resource law not present in the frozen Rev11 formulation.

## 12. Next frontier

The next work should not further optimize the solved one-copy mean-energy problem. Highest-value unresolved targets are:

1. **collective-N mean-energy law:** determine whether entangled collective measurements can beat `G(Lbar)` per copy and find the asymptotic limit;
2. **pre-existing Page--Wootters coherence:** remove separate stationarity of the baseline and bound parameter information added to an already relationally coherent history state;
3. **nonlinear `R_lin=0` families:** formulate a finite-amplitude or curvature-aware law that covers coherent-sideband synthesis;
4. **many-body cut theorem:** generalize dual survival to arbitrary bipartitions/networks;
5. **control/action accounting:** allow non-energy-conserving effective controls only when their autonomous generator resource is explicitly charged.
