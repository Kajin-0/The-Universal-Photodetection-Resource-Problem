# AGENTS.md

## Purpose

Durable project handoff for **The Universal Photodetection Resource Problem**. The repository, not chat history, is authoritative.

Research is analytical/theoretical. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Current project split

1. **Paper 1 / Rev11** — frozen.
2. **Paper 2 / Rev7** — frozen.
3. **Random-time spectral-resource program** — preferred Rev11 manuscript frozen on `agent/temporal-information-resource-law`.
4. **Autonomous temporal-information program** — active scientific frontier on `agent/autonomous-temporal-information-law`; PRX Quantum R3 manuscript build-verified and science-frozen while stronger post-R3 results are audited.

**Active scientific branch:** `agent/autonomous-temporal-information-law`

**Latest research checkpoint:** **WP31**

## Mandatory first read

1. `autonomous_temporal_information/AGENTS.md`
2. `autonomous_temporal_information/notes/WP31_EXACT_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`
3. `autonomous_temporal_information/notes/WP30_INFINITE_DIMENSIONAL_DYNAMICAL_2JET_COST_AND_ENERGY_DOMAIN_BOUNDARY.md`
4. `autonomous_temporal_information/notes/WP29_INFINITE_DIMENSIONAL_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
5. `autonomous_temporal_information/notes/WP28_INFINITE_DIMENSIONAL_FINITE_RADIUS_SURVIVAL_LAW.md`
6. `autonomous_temporal_information/notes/WP27_APPROXIMATE_EXCHANGE_BOUNDARY_SYNTHESIS_ACTION_LAW.md`
7. `manuscript/autonomous_temporal_information/MANUSCRIPT_HANDOFF.md`
8. `grand_challenge/AGENTS.md` only if the frozen random-time program is needed.

## Current strongest result

For a stationary rank-changing autonomous temporal family with a prescribed feasible metric-contracted target-kernel Hessian `C`, the exact minimum state-weighted quadratic implementation cost is

`boxed: V_min=(1/2)Tr C`.

In the clean single-gap exchange geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

WP23 proves this in finite dimension with exact total-energy conservation.

WP28/WP29 extend the finite-radius and rank-boundary information-resource laws to separable infinite-dimensional systems under bounded-relative / Hilbert--Schmidt finite-information assumptions.

WP30 extends the exact prescribed-2-jet cost to arbitrary smooth infinite-dimensional unitary dilations.

WP31 removes the final exact-energy-conservation domain obstruction. A stationary trace-class state decomposes into countably many occupied target-energy eigenspaces. Implement the optimal dilation separately in each target-energy shell, use a zero-energy ancilla, and combine the shells as an incoherent trace-class mixture. Then even with unbounded occupied target energies,

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

Finite quadratic cost is enough for trace-norm `C^2` smoothness; no fourth-moment shell condition is required.

## Robustness

- WP25 gives a leakage-corrected finite-radius theorem for approximate Bohr gaps.
- WP27 gives the corresponding rank-boundary synthesis/action law with off-resonant score-amplitude penalties.

Thus exact resonance is no longer an all-or-nothing assumption in either headline regime.

## Frozen manuscript status

The autonomous PRX Quantum R3 paper remains science-frozen while WP21--WP31 are audited. It is standalone and must remain free of personal repository URLs, usernames, repository names, or dependencies on internal research history.

Do not insert the new theorem chain automatically. First decide whether it belongs in a focused R4 or a separate dynamical/infinite-dimensional follow-up.

## Prior-art discipline

Do not claim novelty for:

- Page--Wootters relational time or modes of asymmetry;
- generic QFI/Bures/Holevo theory;
- Bures/Uhlmann horizontal lifts or `QFI/4` purification speed;
- generic quantum speed limits/control norms;
- energy-conserving or covariant Stinespring dilation theory;
- infinite-dimensional QFI/Bures functional analysis;
- classical nonregular boundary statistics;
- standard numerical-radius, PSD-cone, shorted-operator, Cauchy--Schwarz, or Schur-complement mathematics.

The candidate post-R3 contribution is narrowly the **frequency-resolved endpoint synthesis action as the exact minimum state-weighted quadratic coupling cost for a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics**, plus controlled detuning and infinite-dimensional extensions.

**Priority remains unverified, not certified.**

## Current work order

1. hostile-audit WP31's stationary trace-class energy-support lemma;
2. hostile-audit the mixed-shell trace-norm `C^2` dominated-convergence step;
3. expand the WP31 validator to mixed/degenerate energy shells and random excess curvature;
4. perform a targeted priority search for state-specific prescribed-second-order-jet implementation-cost theorems;
5. decide R4 versus separate follow-up;
6. if research continues, prioritize noisy/CPTP implementation cost or unbounded-relative-tangent quadratic-form extensions.

## Mandatory documentation rule

Every material theorem, counterexample, proof repair, validator, prior-art collision, or publication-strategy change must update the dedicated research note, the active autonomous landing files, and the top-level landing files. Do not allow the authoritative state to exist only in chat.