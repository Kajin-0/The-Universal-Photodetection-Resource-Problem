# WP22 — Exact minimum energy-conserving implementation cost for a pure-boundary temporal tangent

## Status

**Exact variational theorem proved for the clean finite-dimensional pure-boundary autonomous tangent.**

This sharpens WP21 from a lower bound for a supplied implementation to a minimum over all energy-conserving unitary realizations of the prescribed first-order tangent.

The generic identity `QFI/4 = minimum horizontal purification/Fubini–Study metric` is established Bures/Uhlmann geometry and is not claimed as new. The candidate new content is the constructive **target-only energy-conserving horizontal lift for an exact relational exchange**, together with its equality to the minimum spectral endpoint synthesis action.

Do not insert this into the current manuscript until the theorem survives a dedicated prior-art and hostile proof audit.

## 1. Setup

Let `rho_0` be a finite-dimensional target state on `T=C⊗S` satisfying global stationarity

`[rho_0,H_T]=0`, `H_T=H_C+H_S`.

Let

`P=supp(rho_0)`, `Q=I-P`.

Consider a pure-boundary two-quadrature tangent

`D_x=(A+A^dagger)/2`,

`D_y=(A-A^dagger)/(2i)`,

with

`PAP=0`, `QAQ=0`.

For an exact autonomous exchange,

`[H_S,A]=+hbar nu A`,

`[H_C,A]=-hbar nu A`,

so

`[H_T,A]=0`,

and therefore

`[H_T,D_x]=[H_T,D_y]=0`.

Because `rho_0` commutes with `H_T`, its support projector `P`, kernel projector `Q`, and pseudoinverse `rho_0^+` also commute with `H_T`.

## 2. Canonical horizontal generators

For either real tangent `D_j`, define

`C_j := Q D_j P rho_0^+`

and

`boxed:
K_j^hor := i(C_j-C_j^dagger).`

Then `K_j^hor` is Hermitian and has no support-support or kernel-kernel block.

A direct block calculation gives

`boxed:
-i[K_j^hor,rho_0]=D_j.`

Thus the unitary family

`rho_j(theta)=exp(-i theta K_j^hor) rho_0 exp(+i theta K_j^hor)`

realizes the desired first derivative.

Moreover every factor in `C_j` commutes with `H_T`, hence

`boxed:
[K_j^hor,H_T]=0.`

Therefore the horizontal lift is not merely a mathematical purification gauge: it is an **exact total-energy-conserving target-only implementation** of the relational tangent.

No external coherence battery is needed.

## 3. Exact variance of the horizontal lift

Since `P K_j^hor P=0`,

`Tr(rho_0 K_j^hor)=0`.

Therefore

`Var_rho(K_j^hor)=Tr(rho_0 (K_j^hor)^2)`.

Using the support/kernel blocks,

`Var_rho(K_j^hor)
 = Tr(Q D_j P rho_0^+ P D_j Q).`

For a pure-boundary Hermitian tangent, the standard SLD-QFI is

`H_jj^SLD
 = 4 Tr(Q D_j P rho_0^+ P D_j Q).`

Hence

`boxed:
Var_rho(K_j^hor)=H_jj^SLD/4.`

Summing the physical cosine/sine coordinates,

`boxed:
V_hor := Var(K_x^hor)+Var(K_y^hor)
 = (1/4)Tr H^SLD.`

Using the WP09/R3 invariants,

`Tr H^SLD=2(J_++J_-)`,

so

`boxed:
V_hor=(J_++J_-)/2.`

## 4. Variational minimum over all unitary implementations

Consider any smooth global unitary implementation, possibly with an ancilla `E`, whose reduced target derivatives equal `D_x,D_y`. Let its baseline tangent generators be `K_x,K_y` and define

`V_impl=Var_Omega(K_x)+Var_Omega(K_y)`.

By monotonicity of SLD-QFI under partial trace, or equivalently the Bures/Uhlmann horizontal-lift variational principle,

`Tr H_target^SLD <= 4 V_impl`.

Therefore

`V_impl >= (1/4)Tr H_target^SLD.`

The target-only horizontal generators above attain equality while also commuting with `H_T`.

Thus

`boxed:
inf_(all smooth unitary implementations of D_x,D_y)
V_impl
 = (1/4)Tr H^SLD.`

The same infimum is achieved within the stricter class of exact total-energy-conserving target-only implementations:

`boxed:
inf_([K_j,H_T]=0)
[Var(K_x)+Var(K_y)]
 = (1/4)Tr H^SLD.`

This is the exact minimum quadratic dynamical implementation-coupling cost for the prescribed first-order pure-boundary relational tangent.

## 5. Minimum spectral synthesis action

For any two-sided `C^2` physical family with this tangent, second-order positivity gives

`C_Delta >= Z_+ + Z_-`.

In the clean exact-exchange geometry the endpoint-incidence operator on the information-bearing kernel is

`G_ex=2 hbar nu Q`.

Hence

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)
 >= (hbar nu/2)Tr(Z_++Z_-).`

But

`Tr(Z_++Z_-)=J_++J_-=(1/2)Tr H^SLD`.

Therefore

`boxed:
A_ex^(2) >= (hbar nu/4)Tr H^SLD.`

The horizontal unitary orbit has the **minimal kernel curvature**

`C_Delta=Z_++Z_-`

and therefore attains equality:

`boxed:
A_min^(2)
 = (hbar nu/4)Tr H^SLD
 = hbar nu V_min.`

This is the key dynamical completion:

> For a clean pure-boundary exact autonomous temporal tangent, the least possible spectral synthesis action equals `hbar nu` times the least possible quadratic energy-conserving generator variance.

## 6. Relation to common-record Fisher information

The exact minimum dynamical cost is controlled by the SLD geometry,

`V_min=(1/4)Tr H^SLD`.

Measurement accessibility may be lower.

### Bilateral

WP18 gives

`A_ex >= (hbar nu/4) Tr F_N^tan/N`.

Therefore

`V_impl >= A_ex/(hbar nu) >= (1/4)Tr F_N^tan/N`.

At the symmetric fixed-shell extremizer the same Fourier measurement saturates the common-record coefficient and `F^tan=H^SLD`, so all three layers coincide after normalization.

### One-sided

The common-record law is stronger,

`A_ex >= (hbar nu/2)Tr F_N^tan/N`,

while

`A_min=(hbar nu/4)Tr H^SLD`.

The factor-two difference is measurement compatibility: the minimum dynamical coupling is still `Tr H^SLD/4`, but one common fixed measurement accesses only half of the two-quadrature SLD trace in the sharp one-sided model.

## 7. Why this is not Tajima–Shiraishi–Saito coherence cost

Tajima–Shiraishi–Saito study the external QFI/coherence resource needed to implement an operation on a subsystem that **violates that subsystem's conserved quantity**, while total dynamics remains conserving.

Here the desired clock–signal tangent itself obeys

`[A,H_C+H_S]=0`.

The horizontal generators can be chosen directly on `C⊗S` with

`[K_j,H_C+H_S]=0`.

Thus the required external asymmetry battery can be zero even though

`V_min>0`, `A_min>0`, and temporal information is nonzero.

The present cost is interaction/generator strength inside a conserved energy shell, not symmetry-breaking coherence.

## 8. Relation to Bures/Uhlmann geometry

The generic variational statement that mixed-state Bures/QFI geometry is the minimum Fubini–Study geometry over purifications/horizontal lifts is established prior art.

Do not claim novelty for

`min purification speed = QFI/4`.

The potentially distinct statement is the **spectral and autonomous specialization**:

1. the Bures-horizontal tangent admits an explicit target-only generator `K_j^hor`;
2. that generator exactly conserves the total clock–signal Hamiltonian because the temporal mode is relational;
3. the minimum generator variance is linked to the positive endpoint synthesis action by

`A_min=hbar nu V_min`;

4. the construction is sharp in the same fixed-total-energy shell models that saturate the information-resource law.

Priority is unverified.

## 9. Coordinate-covariant form

For a physical parameter metric `g_ij`, define the quadratic implementation cost

`V_impl[g]=g^{ij} Cov_sym(K_i,K_j)`.

The target SLD tensor transforms covariantly, and the horizontal-lift theorem becomes

`boxed:
V_min[g]=(1/4) tr(g^{-1}H^SLD).`

For the canonical cosine/sine quadratures used in the manuscript, `g=I_2`.

The minimum action is

`boxed:
A_min[g]=(hbar nu/4) tr(g^{-1}H^SLD).`

Thus the exact dynamical cost is not tied to an arbitrary coordinate chart.

## 10. What remains unsolved

This result is strong but deliberately narrow.

1. It solves the **pure-boundary exact-exchange tangent** implementation problem, not the full WP19 mixed survival+synthesis geometry.
2. The cost is generator variance / control action, not thermodynamic work, battery depletion, switching cost, or reset cost.
3. General CPTP implementation with prescribed full Hessian, rather than only first-order tangent, remains to be optimized.
4. Infinite-dimensional unbounded-generator domains remain open.
5. Prior-art search must target energy-conserving horizontal lifts and constrained Bures purification geometry before publication claims.

## 11. Immediate next step

The highest-value next question is now precise:

> Given both the first-order tangent and a prescribed nonminimal endpoint Hessian/action, what is the exact minimum generator/control cost over all energy-conserving Stinespring dilations?

WP21 gives the lower bound `V_impl>=A_ex/(hbar nu)`. WP22 shows equality at the minimal-curvature boundary orbit. The remaining problem is whether arbitrary excess positive curvature can be implemented at exactly the additional cost `Delta A/(hbar nu)`, which would yield the full identity

`V_min(full local 2-jet)=A_ex/(hbar nu)`

for clean pure-boundary families.

That is the next theorem target.