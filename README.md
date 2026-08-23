# The Universal Photodetection Resource Problem

**Status synchronized: 2026-08-23**

This repository contains several related theoretical programs. The repository is authoritative; chat history is not.

## Current project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Random-time spectral-resource program** — preferred Rev11 manuscript frozen on `agent/temporal-information-resource-law`.
4. **Autonomous temporal-information program** — active research on `agent/autonomous-temporal-information-law`; PRX Quantum R3 manuscript build-verified and science-frozen while the post-R3 theorem chain is audited.

**Active scientific branch:** `agent/autonomous-temporal-information-law`

**Current autonomous frontier:** **WP31**

Authoritative active handoff: `autonomous_temporal_information/AGENTS.md`.

## Active autonomous result

The existing R3 manuscript establishes two resource regimes for globally stationary relative temporal information:

- finite affine radius -> pre-existing spectral survival;
- rank-changing zero radius -> positive second-order endpoint synthesis action.

For clean exact autonomous exchange the boundary coefficients are

`A_C^(2)+A_S^(2) >= (hbar nu/4)[Tr F_N^tan/N]`

bilaterally and

`A_C^(2)+A_S^(2) >= (hbar nu/2)[Tr F_N^tan/N]`

one-sidedly, with exact fixed-total-energy sharpness.

R3 also contains a pure-boundary SLD-QFI action corollary, a spectator-curvature no-go, the coherent-support mixed bridge, the exact `12 > 43/4 > 55/8` qutrit hierarchy, and the multi-gap shared-Hessian law.

## Post-R3 dynamical completion

Research was reopened to address the criticism that the synthesis action was only kinematic.

### Exact implementation coupling

For a smooth unitary dilation,

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

Thus the kernel synthesis action is exactly a state-weighted squared dynamical coupling into the previously empty endpoint sectors.

### Exact prescribed-2-jet cost

For a prescribed feasible metric-contracted target-kernel Hessian `C`,

`boxed: V_min=(1/2)Tr C`.

In the clean single-gap exchange geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

WP23 proves the finite-dimensional exactly energy-conserving result.

### Infinite-dimensional energy-conserving completion

WP28 and WP29 extend the finite-radius and rank-boundary resource laws to separable infinite-dimensional systems under bounded-relative / Hilbert--Schmidt finite-information assumptions.

WP30 extends the prescribed-2-jet dynamical minimum to arbitrary smooth infinite-dimensional unitary dilations.

WP31 closes the remaining exact-energy-conservation domain problem. A stationary trace-class state decomposes into countably many occupied target-energy shells. By implementing the optimal dilation **separately inside each shell** and using an incoherent global shell mixture with zero-energy ancilla,

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C`

remains valid even when the occupied target energies are unbounded above.

The direct-sum generator may be unbounded; finite state-weighted quadratic cost nevertheless gives summable trace-norm first- and second-derivative majorants, so no fourth-moment condition is required.

## Exact-resonance robustness

The exact Bohr-gap hypothesis is no longer all-or-nothing.

- **WP25:** finite-radius survival with an explicit commutator-residual leakage penalty.
- **WP27:** rank-boundary synthesis/action with near-resonant endpoint terms plus explicit off-resonant score-amplitude penalties.

Both recover the exact-gap laws continuously as the residual vanishes.

## External-review audits

- The mixed `Psi_a(e;p,q)` envelope was independently re-derived and brute-force validated; no defect found.
- Classical nonregular boundary statistics are mandatory prior art. Boundary nonregularity itself is not a quantum novelty claim.
- Bures/Uhlmann horizontal-lift `QFI/4` geometry, generic quantum speed limits, covariant Stinespring dilation theory, and infinite-dimensional QFI/Bures analysis are prior art infrastructure.

The narrow candidate post-R3 contribution is the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic implementation-coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, together with controlled detuning and infinite-dimensional extensions.

**Priority remains unverified, not certified.**

## Current work order

1. hostile-audit WP31's stationary trace-class energy-support lemma;
2. hostile-audit its trace-norm `C^2` dominated-convergence proof;
3. expand the WP31 validator to mixed/degenerate shells and random excess curvature;
4. targeted priority search for state-specific second-order Stinespring/purification implementation-cost theorems;
5. decide deliberately whether WP21--WP31 belong in an R4 of the existing paper or in a separate dynamical follow-up article;
6. if theorem work continues, prioritize noisy/CPTP implementation cost or unbounded-relative-tangent quadratic-form extensions.

## Manuscript integrity

Every paper must be scientifically standalone. Never put personal repository URLs, usernames, repository names, development history, or dependencies on internal research files into a manuscript.

## Frozen programs

The random-time Rev11 manuscript and the other frozen papers remain untouched unless a concrete theorem defect, priority collision, substantive referee objection, or unavoidable submission requirement appears.