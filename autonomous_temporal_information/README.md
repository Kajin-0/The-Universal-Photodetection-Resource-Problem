# Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

The frozen Rev11 random-time paper remains untouched on `agent/temporal-information-resource-law`.

## Status

The PRX Quantum R3 manuscript is **science-frozen and build-verified** while new theory is developed separately. Research was explicitly reopened to address its remaining physical limitations.

**Current frontier: WP21–WP25.**

- Original publication theorem stack through WP20: hostile mathematical audit **PASS**.
- Publication significance gate: **PROVISIONAL PASS for a narrow theorem paper**.
- New dynamical implementation program: major exact results through WP23.
- Approximate-gap robustness: WP25.
- Priority for all new results: **unverified, not certified**.

Read first:

1. `notes/WP25_APPROXIMATE_BOHR_GAP_ROBUST_SURVIVAL_LAW.md`
2. `notes/WP24_INDEPENDENT_PSI_ENVELOPE_AND_CLASSICAL_NONREGULAR_AUDIT.md`
3. `notes/WP23_EXACT_PRESCRIBED_2JET_DYNAMICAL_IMPLEMENTATION_COST.md`
4. `notes/WP22_EXACT_MINIMUM_ENERGY_CONSERVING_IMPLEMENTATION_COST.md`
5. `notes/WP21_DYNAMICAL_IMPLEMENTATION_COUPLING_COST.md`
6. `AGENTS.md`
7. `ROADMAP.md`

## Frozen paper result

The existing paper establishes two complementary spectral-resource regimes for a finite autonomous clock–signal system.

### Finite-radius survival

For exact gap `nu`, finite copy number `N`, and arbitrary collective POVM,

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`.

For an autonomous exact exchange,

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

### Rank-changing synthesis

At `R_lin=0`, a nonlinear physical family may remain informative. Positive second-order endpoint synthesis replaces pre-existing survival.

Clean autonomous action laws:

- bilateral: `A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`;
- one-sided: `A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

R3 additionally proves

`A_C^(2)+A_S^(2)>=(hbar nu/4)Tr H_SLD`

for the clean pure-boundary tangent and separates this first-order quantum-statistical geometry from arbitrary spectator second-order Bures curvature.

## New result: exact dynamical meaning of the synthesis action

WP21–WP23 materially strengthen the physical interpretation.

For any smooth unitary dilation,

`Q partial_j^2 rho Q = 2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

Thus

`A_G^(2)=(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j]`.

The previously kinematic action is exactly a weighted squared coupling of the implementation generator into the empty endpoint sectors.

### Exact minimum for the first-order tangent — WP22

For a clean pure-boundary exact relational tangent,

`V_min=(1/4)Tr H_SLD`,

attained by an explicit target-only generator commuting with `H_C+H_S`.

The minimum compatible action is

`A_min=hbar nu V_min`.

### Exact minimum for a prescribed kernel 2-jet — WP23

Let

`C_min=2 sum_j QD_jP rho_0^+ P D_jQ`

and prescribe any globally stationary feasible kernel Laplacian

`C_Delta>=C_min`.

Then over **all** smooth unitary dilations,

`boxed: V_min=(1/2)Tr C_Delta`.

Equality is attained by adding the excess curvature through orthogonal ancilla flag sectors. The flags can be assigned compensating energies sector-by-sector, so the complete minimizing implementation stays in one exact global energy shell.

In the clean single-gap endpoint geometry,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

This is currently the strongest result in the new program: the spectral synthesis action is exactly `hbar nu` times the minimum quadratic energy-conserving implementation cost for the full metric-contracted local kernel 2-jet.

Validator:

`numerics/verify_wp23_prescribed_2jet_implementation_cost.py`

## External-review checks — WP24

The mixed scalar envelope `Psi_a(e;p,q)` was independently re-derived and numerically hostile-tested. No defect was found.

Classical boundary/nonregular statistics must be acknowledged explicitly in any future manuscript revision. Chernoff (1954), Shapiro (1985), and Self–Liang (1987) establish generic nonstandard boundary asymptotics. The quantum claim is not “boundaries are nonregular”; it is the operator PSD-cone/spectral/autonomous/dynamical resource theorem built on top of that fact.

Validator:

`numerics/verify_wp24_psi_envelope.py`

## New result: approximate Bohr-gap robustness — WP25

The exact commutator assumption is no longer all-or-nothing in the finite-radius stationary setting.

For

`R_nu=[H,A]-hbar nu A`,

`eta_nu^2=Tr(R_nu rho_0^+ R_nu^dagger)`,

and any detuning window `0<delta<nu`,

`boxed:
(R_lin^2/4)[Tr F_N^tan/N]
 <= T(nu-delta)
   + R_lin^2 eta_nu^2/(4 hbar^2 delta^2).`

Near-resonant tangent weight is paid by a slightly lower spectral tail; off-resonant leakage is paid by the weighted commutator residual. The exact theorem is recovered as the residual vanishes.

A locally energy-stationary autonomous pair obeys the corresponding minimum of the clock and signal leakage-corrected bounds.

Validator:

`numerics/verify_wp25_approximate_gap_robustness.py`

## Important prior-art boundary

Do not claim novelty for:

- Bures/Uhlmann horizontal lifts or `QFI/4` purification speed;
- quantum speed limits or generic integrated Hamiltonian norms;
- numerical-radius/PSD-cone/shorted-operator mathematics;
- classical nonregular boundary asymptotics;
- generic asymmetry modes or Page–Wootters relational time.

Carrasco & Spehner, arXiv:2606.06759 (2026), is an especially important current neighbor for Bures geodesics and quantum speed limits of non-faithful states.

The narrow candidate novelty of WP23 is the **prescribed second-order kernel-jet completion with an exact energy-conserving spectral endpoint-action interpretation**.

## Current work order

1. hostile-audit WP23 and search second-order constrained purification/Stinespring prior art;
2. audit WP25 against approximate-eigenoperator/Bohr-mode literature;
3. extend the **zero-radius synthesis/action law** to approximate exchange/noisy encoding if possible;
4. then attack infinite dimensions in stages: trace-class baseline + semibounded pure-point Hamiltonian + bounded relative tangent, followed only later by continuous spectra and unbounded generators;
5. decide on a manuscript R4 only after the new theorem chain passes these gates.

The repository is authoritative. Material results must be recorded here and in `AGENTS.md`, `ROADMAP.md`, and dedicated notes.