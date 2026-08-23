# WP23 — Exact dynamical implementation cost for a prescribed boundary 2-jet

## Status

**Exact finite-dimensional variational theorem proved for the clean pure-boundary autonomous setting with a prescribed kernel Laplacian.**

This closes the main open problem left by WP21–WP22. WP21 gave a lower bound for a supplied implementation, and WP22 proved equality for the minimum-curvature horizontal orbit. WP23 proves equality for **every feasible prescribed kernel second-order jet** in the clean single-gap endpoint geometry.

The current PRX Quantum manuscript remains frozen. Do not insert WP23 until prior-art and hostile proof audits pass.

## 1. Setup

Let the target be `T=C⊗S`, finite dimensional, with

`[rho_0,H_T]=0`, `H_T=H_C+H_S`,

and

`P=supp(rho_0)`, `Q=I-P`.

Let two Hermitian real tangents `D_x,D_y` satisfy the pure-boundary conditions

`P D_j P=0`, `Q D_j Q=0`,

and exact relational stationarity

`[D_j,H_T]=0`.

For the temporal-mode convention one may take

`D_x=(A+A^dagger)/2`,

`D_y=(A-A^dagger)/(2i)`,

with `[A,H_T]=0` and the local exact exchange relations at gap `nu`.

Define

`K_j^red := Q D_j P`.

The universal PSD-cone minimum kernel curvature in coordinate `j` is

`C_j^min := 2 K_j^red rho_0^+ (K_j^red)^dagger`.

Hence the minimum Laplacian kernel curvature is

`boxed:
C_min := C_x^min+C_y^min
       = 2 sum_j QD_jP rho_0^+ P D_jQ.`

For a prescribed target kernel Laplacian `C_Delta`, feasibility requires

`boxed: C_Delta >= C_min.`

For an exactly globally stationary implementation we additionally require

`[C_Delta,H_T]=0`.

In the clean endpoint-only theorem below, `C_Delta` is supported in the synthesized exchange endpoint subspace on which the endpoint-incidence operator is

`G_ex=2 hbar nu Q`.

(If spectator/unpriced kernel sectors are present, the total generator variance also prices them, while `A_ex` need not. That more general weighted problem is separate.)

## 2. Implementation class and cost

Allow an arbitrary finite-dimensional ancilla/controller `E`, arbitrary global baseline `Omega_0` reducing to `rho_0`, and a smooth two-parameter unitary family

`Omega(x,y)=U(x,y) Omega_0 U(x,y)^dagger`,

`rho(x,y)=Tr_E Omega(x,y)`.

At the origin define Hermitian tangent generators

`partial_j U(0)=-i K_j`.

The implementation must reproduce

`partial_j rho(0)=D_j`

and the prescribed target kernel Laplacian

`Q(partial_x^2+partial_y^2)rho(0)Q=C_Delta`.

The quadratic implementation cost is

`V_impl := Var_Omega0(K_x)+Var_Omega0(K_y)`.

For the energy-conserving subclass require a global bare Hamiltonian

`H_tot=H_T+H_E`

such that

`[Omega_0,H_tot]=0`,

`[U(x,y),H_tot]=0`.

## 3. Universal lower bound from the exact unitary kernel identity

WP21 proves, for every smooth unitary implementation,

`Q partial_j^2 rho(0) Q
 = 2 Tr_E[(Q⊗I) K_j Omega_0 K_j (Q⊗I)].`

Taking the trace and summing,

`(1/2)Tr C_Delta
 = sum_j Tr[Omega_0 K_j(Q⊗I)K_j].`

Because the reduced baseline has no weight on `Q`, positivity implies

`Omega_0=(P⊗I)Omega_0(P⊗I)`.

For each Hermitian generator,

`Var_Omega0(K_j)
 = Var_Omega0((P⊗I)K_j(P⊗I))
   + Tr[Omega_0 K_j(Q⊗I)K_j]`

with both terms nonnegative. Therefore

`boxed:
V_impl >= (1/2)Tr C_Delta.`

This lower bound is stronger than the first-order QFI bound whenever the prescribed second-order curvature exceeds the PSD-cone minimum.

## 4. Constructive equality for every feasible C_Delta

Write

`S := (1/2)(C_Delta-C_min) >= 0.`

The construction has two orthogonal pieces.

### 4.1 Horizontal first-order piece

Choose an energy-adapted purification of `rho_0`,

`|Omega> = sum_a sqrt(lambda_a)|a>_T |a>_E`,

where the support eigenvectors can be chosen jointly with `H_T` because `[rho_0,H_T]=0`.

For each coordinate use the WP22 target-only horizontal generator

`K_j^hor=i(QD_jP rho_0^+ - rho_0^+ P D_jQ)`.

Let

`|chi_j^hor> := -i(K_j^hor⊗I)|Omega>`.

Then

`Tr_E(|chi_j^hor><Omega|+|Omega><chi_j^hor|)=D_j`,

and

`2 Tr_E[Q|chi_j^hor><chi_j^hor|Q]=C_j^min`.

The horizontal norms satisfy

`sum_j ||chi_j^hor||^2=(1/2)Tr C_min=(1/4)Tr H_SLD.`

### 4.2 Orthogonal flag for arbitrary excess curvature

Because `S>=0`, choose any purification

`|eta> in Q⊗E_flag`

such that

`Tr_Eflag |eta><eta| = S`.

Take the flag ancilla subspace orthogonal to the baseline purification ancilla and to the horizontal ancilla support. Then

`Tr_E(|eta><Omega|)=0`,

`Tr_E(|eta><chi_j^hor|)=0`.

Assign the entire excess to one coordinate, e.g.

`|chi_x>=|chi_x^hor>+|eta>`,

`|chi_y>=|chi_y^hor>`.

Therefore the first derivatives remain exactly `D_x,D_y`, while

`2 sum_j Tr_E[Q|chi_j><chi_j|Q]
 = C_min+2S
 = C_Delta`.

The total norm is

`sum_j ||chi_j||^2
 = (1/2)Tr C_min + Tr S
 = (1/2)Tr C_Delta.`

Since each `chi_j` is orthogonal to `Omega`, define Hermitian generators on the global Hilbert space by

`K_j = i(|chi_j><Omega|-|Omega><chi_j|)`

on the span of `Omega,chi_j`, extended arbitrarily and Hermitian on the orthogonal complement. Then

`-iK_j|Omega>=|chi_j>`,

`<Omega|K_j|Omega>=0`,

and

`Var_Omega(K_j)=||chi_j||^2`.

The smooth local family

`U(x,y)=exp[-i(xK_x+yK_y)]`

therefore realizes the prescribed tangent and kernel Laplacian with

`boxed:
V_impl=(1/2)Tr C_Delta.`

Combined with the lower bound,

`boxed:
inf V_impl=(1/2)Tr C_Delta.`

## 5. Exact total-energy-conserving realization

The equality construction can be made exactly energy conserving.

Choose the purification ancilla Hamiltonian so that each baseline Schmidt term has the same global energy. If

`H_T|a>=E_a|a>`,

assign

`H_E|a>_E=(E_* - E_a)|a>_E`.

Then `|Omega>` lies entirely in the global energy-`E_*` eigenspace.

Because `[D_j,H_T]=0`, the horizontal vectors `|chi_j^hor>` lie in the same global shell.

Because `[S,H_T]=0`, decompose `S` by target-energy sectors. Purify each sector using fresh orthogonal flag states assigned ancilla energy `E_*-E`. The resulting `|eta>` also lies entirely in the same global shell.

Hence every `|chi_j>` and `|Omega>` are degenerate eigenvectors of `H_tot`. The rank-two generators above can therefore be chosen wholly inside that shell, giving

`boxed: [K_j,H_tot]=0`

and thus

`boxed: [U(x,y),H_tot]=0.`

Therefore the same minimum is achieved inside the stricter exactly conserving class:

`boxed:
inf_(energy-conserving implementations) V_impl
 = (1/2)Tr C_Delta.`

No external time-translation asymmetry is required.

## 6. Equality with the spectral synthesis action

In the clean single-gap endpoint geometry,

`G_ex=2 hbar nu Q`

on the entire prescribed kernel curvature. Therefore

`A_ex^(2)
 = (1/4)Tr(G_ex C_Delta)
 = (hbar nu/2)Tr C_Delta.`

The exact variational theorem becomes

`boxed:
V_min(full local 2-jet)
 = A_ex^(2)/(hbar nu).`

Equivalently,

`boxed:
A_ex^(2)=hbar nu V_min.`

WP22 is recovered when `C_Delta=C_min`.

Thus the manuscript's kinematic endpoint action is not only a necessary dynamical lower bound: **for every feasible clean prescribed kernel 2-jet it is exactly hbar*nu times the minimum quadratic energy-conserving unitary implementation cost.**

## 7. Relation to first-order SLD geometry

Since

`(1/2)Tr C_min=(1/4)Tr H_SLD`,

one may write

`V_min(full 2-jet)
 = (1/4)Tr H_SLD
   + (1/2)Tr(C_Delta-C_min).`

The first term is the familiar horizontal/Bures first-order cost. The second term is the exact additional implementation cost of prescribed nonminimal boundary curvature.

This cleanly separates

1. first-order statistical geometry;
2. independent second-order state-family specification.

The spectator-curvature phenomenon in R3 is therefore dynamically priced rather than ignored: if a spectator second-order population is prescribed, it adds exactly half its kernel-Laplacian trace to the minimum generator variance. It is absent only when the implementation problem prices solely the chosen temporal endpoint sectors.

## 8. Coordinate-covariant statement

For a physical parameter metric `g`, prescribe the metric-contracted kernel Hessian

`C_g := g^{ij} Q partial_i partial_j rho(0) Q`.

For linear coordinate transformations with the metric transformed covariantly, define

`V_impl[g]=g^{ij} Cov_sym(K_i,K_j)`.

The same construction gives, in the clean endpoint geometry,

`boxed:
V_min[g]=(1/2)Tr C_g`

and

`boxed:
A_ex[g]=hbar nu V_min[g].`

A complete tensor-valued prescribed Hessian, including mixed second derivatives, may impose additional compatibility conditions not needed for the scalar metric-contracted action theorem.

## 9. What this solves

WP23 solves the clean finite-dimensional **metric-contracted local 2-jet implementation problem**:

- arbitrary feasible excess positive kernel curvature;
- arbitrary finite ancilla/controller dimension;
- exact minimum generator-variance cost;
- constructive Stinespring/unitary realization;
- exact total-energy conservation;
- equality to the spectral synthesis action.

This materially resolves the criticism that the action is only kinematic, for this core setting.

## 10. What remains open

1. Full tensor-valued second-order jet, including prescribed mixed `partial_x partial_y rho` blocks.
2. General WP19 coherent-support case with simultaneous survival and synthesis.
3. Weighted/multi-gap action where `G` is not proportional to the identity on the relevant kernel.
4. Infinite-dimensional/unbounded-generator extension.
5. Thermodynamic work, switching, reset, and autonomous-controller accounting.
6. Approximate rather than exact Bohr-gap/exchange structure.
7. Dedicated prior-art audit of constrained second-order Stinespring/Bures lift results.

## 11. Prior-art boundary

The first-order identity `V_min=Tr H_SLD/4` is Bures/Uhlmann horizontal-lift geometry and is not new.

The potentially distinct content is the second-order constrained completion:

`V_min(full kernel Laplacian 2-jet)=(1/2)Tr C_Delta`,

with a constructive orthogonal-flag Stinespring realization that preserves exact global energy conservation, and therefore

`A_ex=hbar nu V_min`

for the frequency-resolved endpoint action.

Priority remains unverified.

## 12. Immediate next work

1. Build a numerical validator using random block-diagonal `rho_0`, random energy-preserving pure-boundary tangents, and random PSD excess `S`.
2. Hostile proof audit the energy-shell flag construction and the variance decomposition.
3. Search prior art for second-order constrained purification/Stinespring interpolation and quantum statistical 2-jet geometry.
4. Independently re-derive the manuscript's `Psi_a(e;p,q)` mixed-resource envelope as requested by the external critique.
5. Then choose between approximate-gap/noise robustness and infinite-dimensional extension.