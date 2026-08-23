# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The PRX Quantum R3 manuscript is **build-verified and science-frozen** while the post-R3 dynamical/infinite-dimensional program is audited.

**Canonical frontier: WP32; hostile audit: WP33.**

**WP31 is superseded.** It correctly introduced the classical-mixture mechanism but failed for prescribed spectator curvature in an unoccupied target-energy shell.

## Current strongest result

For a stationary rank-changing temporal family with prescribed feasible metric-contracted target-kernel Hessian `C`, the exact minimum state-weighted quadratic implementation cost is

`boxed: V_min=(1/2)Tr C`.

In the clean single-gap endpoint geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

WP32 proves this even for separable infinite-dimensional targets with unbounded occupied baseline energies and **arbitrary additional stationary spectator curvature**, including curvature in target-energy shells empty at baseline, while preserving total energy exactly with a semibounded ancilla.

## How WP32 works

Strong stationarity plus trace-class compactness gives a countable joint `rho_0/H_T` eigenbasis on the occupied support.

For the required first-order tangent, the normalized support-to-kernel columns stay in the same target-energy shell. For the excess curvature

`S=(C-C_min)/2`,

strong energy preservation gives an energy-adapted trace-class spectral decomposition.

Split one occupied baseline eigenstate weight into countably many **classically incoherent ancilla-labelled copies**. Replicate its horizontal tangent across the copies. For each excess-curvature eigenmode of target energy `F_r`, assign nonnegative ancilla input/output energies

`a_r=max(0,F_r-E_*)`,

`b_r=max(0,E_*-F_r)`

so baseline, horizontal tangent, and excess flag all share one exact total energy on that branch.

The resulting global direct-sum generator can be unbounded. This is harmless because the global baseline is a trace-class classical mixture: finite quadratic implementation cost gives summable trace-norm first- and mixed-second derivative bounds. No fourth-moment condition is needed.

## Hostile audit

WP33: **PASS** under the stated finite-information assumptions.

It verifies the energy-support lemma, branch-energy compensation, flag invisibility, exact curvature reproduction, direct-sum self-adjointness, and trace-norm `C^2` differentiation. It also shows the split weights can be chosen so the baseline ancilla has finite mean energy whenever desired, without changing the implementation optimum.

Permanent repaired validator:

`numerics/verify_wp32_repaired_energy_conserving_2jet_cost.py`

It includes mixed and degenerate baseline energy sectors and random positive excess curvature placed partly in **unoccupied** target-energy shells.

## Supporting theorem chain

- WP21: exact unitary implementation-coupling identity.
- WP22: `V_min=(1/4)Tr H_SLD` for the prescribed pure-boundary tangent.
- WP23: finite-dimensional prescribed-2-jet optimum.
- WP24: independent `Psi_a` audit; no defect; classical nonregular statistics added to prior-art boundary.
- WP25: approximate-gap finite-radius robustness.
- WP27: approximate-exchange rank-boundary robustness.
- WP28: infinite-dimensional finite-radius survival.
- WP29: infinite-dimensional rank-boundary synthesis/action.
- WP30: unrestricted infinite-dimensional dilation optimum.
- WP31: superseded intermediate proof.
- WP32: repaired exactly energy-conserving infinite-dimensional optimum.
- WP33: hostile proof and priority audit.

## Prior-art boundary

Covariant/energy-conserving Stinespring dilation is prior art; Scutaru (1979) and later treatments explicitly establish covariant Stinespring structure. Bures/Uhlmann horizontal geometry, QFI convex-roof variance, non-faithful Bures geodesics, generic QSL/control costs, second-order PSD-cone tangent theory, infinite-dimensional QFI, and classical nonregular boundary statistics are also infrastructure, not novelty.

Targeted searches have not located the exact WP32 state-specific theorem

`inf V_impl=(1/2)Tr C`

for a prescribed feasible rank-changing target-kernel Hessian contraction together with the autonomous endpoint identity `V_min=A_ex/(hbar nu)`. This is **not** priority certification.

## Publication direction

Default after WP33:

**Keep R3 frozen. Build a separate follow-up paper around WP21--WP32.**

The new chain is now too large and conceptually distinct to insert wholesale into the two-regime manuscript without diluting it.

## Next work

1. freeze a follow-up-paper theorem stack;
2. run a dedicated significance/prior-art gate on that stack;
3. only then create a manuscript skeleton;
4. afterward, if more theory is valuable, prioritize noisy/CPTP implementation cost or approximate-exchange dynamical cost.

Every public-facing paper must remain scientifically standalone and contain no personal repository identifiers or dependencies.