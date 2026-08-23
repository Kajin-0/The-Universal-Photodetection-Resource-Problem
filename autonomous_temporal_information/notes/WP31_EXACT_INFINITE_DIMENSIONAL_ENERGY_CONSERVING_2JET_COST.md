# WP31 — Infinite-dimensional energy-conserving 2-jet cost: intermediate proof and erratum

## Status

**SUPERSEDED BY WP32.**

WP31 identified the correct mechanism for removing the WP30 fourth-moment/domain obstruction: use a **classical trace-class mixture** over energy-labelled implementation branches rather than one coherent purification vector spread across infinitely many target energies.

However, the original WP31 proof contained a hidden scope defect.

It decomposed

`rho_0=direct_sum_E rho_E`, `p_E=Tr rho_E`

and then normalized every prescribed curvature block as

`c_E=C_E/p_E`.

This silently assumed

`C_E!=0 => p_E>0`.

That implication is false. A feasible positive spectator curvature can commute with the target Hamiltonian and lie in a target-energy shell that has **zero baseline population**. Such second-order curvature is exactly the kind of spectator contribution already emphasized by the R3 boundary/Bures discussion.

Therefore the original WP31 statement that an identically zero ancilla Hamiltonian `H_E=0` suffices for **arbitrary** prescribed `C` was too strong.

## What survives

The central WP31 regularity insight is correct and is retained by WP32:

> the optimal infinite-dimensional dilation should be built from a trace-class **classical mixture of implementation branches**, not one coherent purification across infinitely many energies.

That replacement changes the relevant differentiability estimate from a vector-domain/fourth-moment problem to a trace-class dominated-convergence problem controlled by the ordinary state-weighted quadratic implementation cost.

Thus no fourth-moment condition is necessary for existence of an optimal dilation.

## Corrected theorem

The full theorem, including arbitrary stationary spectator curvature in target-energy shells unoccupied at baseline, is proved in

`WP32_REPAIRED_INFINITE_DIMENSIONAL_ENERGY_CONSERVING_2JET_COST.md`.

WP32 uses:

1. a countable joint eigenbasis of the stationary trace-class baseline and target Hamiltonian;
2. classical splitting of baseline eigenstate weights into orthogonal ancilla-labelled copies;
3. proportional replication of the horizontal tangent across those copies, which leaves the minimum horizontal cost unchanged;
4. nonnegative ancilla input/output energies that exactly compensate arbitrary target-energy differences of excess curvature flags;
5. a classical global branch mixture, which makes finite quadratic cost sufficient for trace-norm `C^2` smoothness.

The corrected result is

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C`

for every feasible positive trace-class metric-contracted kernel Hessian `C` satisfying the WP29 finite-information assumptions and strong energy covariance.

In the clean single-gap endpoint geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

## Historical lesson

A zero-energy ancilla is sufficient when all required baseline, tangent, and excess-curvature transitions remain within the same target-energy shell. It is **not** sufficient for arbitrary spectator curvature in previously unoccupied target-energy shells.

The universal construction needs only a **semibounded nonnegative ancilla Hamiltonian**, with branch energies chosen to compensate target-energy differences.

WP32 is canonical. Do not cite WP31 as the final theorem.