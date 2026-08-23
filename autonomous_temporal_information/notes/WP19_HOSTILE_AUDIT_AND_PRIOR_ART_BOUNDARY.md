# WP19 hostile audit — proof status, physical interpretation, and prior-art boundary

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** no mathematical defect found in the WP19 inequality after independent reconstruction and randomized validation. One interpretive narrowing is required: in the noncommuting-support regime, `A_CS^(2)=(1/4)Tr(G_CS C_Delta)` is a **kernel-resolved endpoint-incidence action**, not in general the full Laplacian of ordinary local endpoint population and not signed subsystem energy curvature. Generic sharpness is not claimed.

## 1. Proof dependency audit

The WP19 proof uses only previously established inequalities:

1. exact exchange and two-sided physicality imply `QAQ=0`;
2. WP11 gives the finite-copy arbitrary-POVM score bound in terms of `J_B^+`, `J_B^-`, `J_+`, `J_-`;
3. the support-preserving norms are bounded from signal and clock endpoint compressions separately, so taking the minimum gives valid two-sided pre-existing ceilings `a_+`, `a_-`;
4. PSD-cone curvature gives `C_Delta>=Z_++Z_-`;
5. positivity of `G_CS` gives `Tr(G_CS C_Delta)>=Tr(G_CS Z_+)+Tr(G_CS Z_-)`;
6. restricted minimum eigenvalues `g_+`, `g_-` yield `g_+J_+ + g_-J_-<=4A_CS^(2)`;
7. the exact WP13 scalar allocation solves the remaining maximization of the WP11 score expression.

No independence assumption between clock and signal endpoint curvatures is used. The same global kernel curvature is priced once.

## 2. Independent benchmark reconstruction

The validator `verify_noncommuting_autonomous_mixed_resource_action_law.py` reconstructs the shared-kernel qutrit directly from matrices rather than importing inherited scalar values.

It checks:

- `[H_S,A]=+A` and `[H_C,A]=-A` in `hbar nu=1` units;
- `H_C+H_S=2I` on the fixed shell;
- `QAQ=0`;
- `J_B^+=J_B^-=5/4`;
- `J_+=7/4`, `J_-=3`;
- `G_CS=diag(2,4,2)`;
- `g_+=g_-=13/4`;
- `C_Delta=(19/4)Q`;
- `4A_CS^(2)=247/16`;
- `Psi_(5/4)(247/16;13/4,13/4)=12`.

Random rank-one POVMs remain below the resource ceiling.

## 3. Important interpretation correction

For noncommuting support,

`C_Delta=Q Delta rho Q`

contains only the kernel-resolved second-order curvature.

For a local endpoint projector `Pi`,

`Tr(Q Pi Q C_Delta)`

is therefore the endpoint incidence of the **kernel curvature**.

It is not generally equal to the full population Laplacian

`Delta Tr(Pi rho)`

because `P Delta rho P` and support/kernel cross blocks can also contribute to the latter when `[P,Pi]!=0`.

Accordingly:

> `A_CS^(2)` should be called **kernel-resolved positive endpoint-incidence action** in the general WP19 theorem.

In the clean baseline-empty endpoint limit, the distinction disappears and it reduces to the ordinary endpoint population-curvature action of WP18.

This naming restriction is substantive. Do not describe general WP19 as a theorem directly about signed total energy or the full second derivative of local mean energy.

## 4. Endpoint multiplicity is intentional

`G_CS` contains

`Pi_(S,U)+Pi_(S,D)+Pi_(C,U)+Pi_(C,D)`.

These projectors need not be mutually orthogonal. A physical sector can participate in multiple endpoint roles, and its coefficient in `G_CS` can therefore exceed one.

This is not an algebraic double count of `C_Delta`: the curvature operator is still traced only once against one positive cost operator.

It is instead **incidence multiplicity** in the chosen resource definition.

That distinction matters. A future theorem may find a smaller orientation-labelled cost, but the present WP19 law is valid for the explicitly defined incidence resource.

## 5. Existing Page--Wootters resource theory

Carmo and Soares-Pinto, *Quantifying resources for the Page-Wootters mechanism: Shared asymmetry as relative entropy of entanglement*, Phys. Rev. A **103**, 052420 (2021), DOI `10.1103/PhysRevA.103.052420`, quantify Page--Wootters clock resources using mutual/shared asymmetry and relate this to entanglement inside charge sectors.

Therefore WP19 must **not** claim that identifying a resource inside a globally stationary Page--Wootters state is itself new.

The distinction is that WP19 concerns a frequency-resolved local Fisher inequality for an exact exchange tangent and separates pre-existing finite-radius survival from support-changing second-order synthesis.

## 6. Existing relational/reference-frame theory

Quantum-reference-frame and relational-observable formalisms already establish that physically meaningful phase/time information can be relational and symmetry invariant. Examples include:

- Loveridge, Miyadera, and Busch, *Symmetry, Reference Frames, and Relational Quantities in Quantum Mechanics*, Found. Phys. **48**, 135--198 (2018), arXiv:1703.10434;
- Giacomini, Castro-Ruiz, and Brukner, *Quantum mechanics and the covariance of physical laws in quantum reference frames*, Nat. Commun. **10**, 494 (2019);
- Höhn, Smith, and Lock, *Trinity of relational quantum dynamics*, Phys. Rev. D **104**, 066001 (2021).

No novelty is claimed for relational observables, fixed-total-energy descriptions, or the absence of global asymmetry.

## 7. Existing relative-phase / fixed-number metrology

Two-mode and fixed-number interferometry already studies metrological information encoded in relative phases under a fixed total particle or photon number. Relative phase can carry the full relevant Fisher information in standard settings.

Therefore the fixed-total-energy qutrit extremizer should be presented only as a sharp construction for the new resource inequality, not as a new interferometric principle.

## 8. 2026 energy-constrained quantum metrology

Chen and Yang, *Optimal Quantum Metrology under Energy Constraints*, Phys. Rev. Lett. **136**, 070801 (2026), DOI `10.1103/6ghs-frtx`, formulate metrology when the total energy consumption of preparation, intermediate control, and final measurement is constrained, and derive optimal phase-estimation limits.

This is a major nearby result and must be discussed in any manuscript.

WP19 is not a replacement for that framework. Its resource is different:

- local and frequency resolved;
- tied to a rank-changing exact exchange tangent;
- kinematic rather than a total protocol energy ledger;
- split into finite-radius survival and kernel-resolved second-order synthesis;
- explicitly relational across clock and signal.

Whether this distinction is sufficient for publication-level novelty still requires deeper literature review.

## 9. Nearby 2026 symmetry-metrology result

Wilson et al., *Geometric invariants of quantum metrology*, Phys. Rev. A **113**, 063725 (2026), DOI `10.1103/tmkc-dw9z`, identify invariant QFIM spectra under symmetry-preserving dynamics generated by a closed Lie algebra.

This reinforces the need to avoid broad claims such as 'a conserved symmetry creates a new metrological resource law.' WP19's candidate contribution is the support-changing endpoint-resource inequality, not generic symmetry-protected QFI geometry.

## 10. Current priority assessment

Targeted searches have not identified a predecessor with all of the following simultaneously:

- globally stationary exact clock--signal exchange;
- arbitrary coherent/non-energy-diagonal baseline support;
- finite-copy arbitrary collective POVM Fisher information;
- support-shortened two-sided pre-existing endpoint survival;
- a second-order positive kernel synthesis resource;
- one combined clock+signal endpoint-incidence cost that avoids charging the same kernel curvature independently twice;
- exact reduction to the clean sharp WP18 coefficients.

This is evidence of distinctness, not proof of priority.

## 11. Audit conclusion

**Mathematical status:** PASS.

**Interpretive correction:** call the general resource a `kernel-resolved endpoint-incidence action`, not full local energy curvature.

**Sharpness:** clean WP18 limits are exactly sharp; the generic WP19 scalar reduction is not claimed sharp.

**Novelty:** plausible but unverified. The strongest manuscript-level contrast is likely

`finite-radius dual survival  <->  zero-radius dual synthesis action`

inside globally stationary relational exchange, rather than the raw SDP/shorting machinery.

## 12. Next decision

The highest-value next mathematical target is a multi-gap autonomous sum law. If that law is only a trivial sum of WP19 modewise inequalities, stop. Proceed only if one common spectral-incidence operator yields a stronger shared budget across frequencies.
