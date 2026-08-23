# WP21 — Dynamical implementation coupling cost for boundary synthesis

## Status

**New theorem candidate proved in the finite-dimensional unitary-dilation setting.**

This work package is intentionally separate from the current PRX Quantum manuscript. Do not modify the manuscript until the theorem and prior-art boundary survive a hostile audit.

The goal is to address the remaining physical limitation of the synthesis action: in the manuscript it is introduced kinematically from the Hessian of an encoded state family. Here we ask what any actual energy-conserving implementation must dynamically supply.

## 1. Implementation model

Let the target be the clock–signal system `T=C⊗S`, with an arbitrary finite-dimensional implementation ancilla/controller `E`.

Let the global baseline be `Omega_0>=0`, `Tr Omega_0=1`, with target reduction

`rho_0=Tr_E Omega_0`.

Let

`P=supp(rho_0)`, `Q=I-P`.

Because `rho_0` has no weight on `Q`, positivity of `Omega_0` implies

`Omega_0=(P⊗I_E) Omega_0 (P⊗I_E)`.

Consider a two-parameter smooth unitary implementation

`Omega(x,y)=U(x,y) Omega_0 U(x,y)^dagger`,

`rho(x,y)=Tr_E Omega(x,y)`,

with `U(0,0)=I`. Define Hermitian tangent generators by

`partial_x U(0)=-i K_x`,

`partial_y U(0)=-i K_y`.

If the implementation conserves a total bare Hamiltonian `H_tot` for all `(x,y)`,

`[U(x,y),H_tot]=0`,

then automatically

`[K_x,H_tot]=[K_y,H_tot]=0`.

No assumption is made that the ancilla is trivial.

## 2. Exact kernel-curvature identity

For either coordinate `j in {x,y}`, a general smooth unitary has a second-order expansion containing both `K_j^2` and an acceleration generator. In the target kernel block the acceleration commutator drops out because the global baseline is supported in `P⊗E`.

Therefore

`boxed:
Q partial_j^2 rho(0) Q
 = 2 Tr_E[(Q⊗I) K_j Omega_0 K_j (Q⊗I)].`

Hence for

`C_Delta=Q(partial_x^2+partial_y^2)rho(0)Q`

one has the exact dynamical representation

`boxed:
C_Delta
 = 2 sum_(j=x,y) Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

This is stronger than the generic PSD-cone inequality because it uses an explicit unitary implementation.

## 3. Exact dynamical representation of a positive endpoint action

Let `G>=0` be any target operator supported on `Q`. Define the same kinematic action used in WP13/WP19,

`A_G^(2)=(1/4)Tr_T(G C_Delta).`

The unitary-dilation identity gives

`boxed:
A_G^(2)
 = (1/2) sum_j Tr_TE[(G⊗I_E) K_j Omega_0 K_j].`

Thus the state-family Hessian action is exactly an initial-state-weighted squared **implementation coupling into the priced empty sectors**.

This supplies a direct dynamical interpretation without identifying the action with net work or total protocol energy.

## 4. Clean exact-exchange generator-variance lower bound

For the clean pure-boundary single-gap autonomous exchange used in WP18, the information-bearing kernel sectors each carry one endpoint role, so on the relevant kernel

`G_ex=2 hbar nu R`,

where `R<=Q` is the projector onto the synthesized exchange endpoints. Therefore

`A_ex^(2)
 = hbar nu sum_j Tr[(R⊗I)K_j Omega_0 K_j].`

For each Hermitian `K_j`, decompose its variance relative to the target support `P/Q`. Since `Omega_0` is supported in `P⊗E`,

`Var_Omega(K_j)
 = Var_Omega(P K_j P) + Tr[Omega_0 K_j(Q⊗I)K_j]`

(with the first term understood as the variance of the support block), hence

`Tr[(R⊗I)K_j Omega_0 K_j] <= Var_Omega(K_j)`.

Thus

`boxed:
A_ex^(2)
 <= hbar nu [Var_Omega(K_x)+Var_Omega(K_y)].`

Define the dimensionless quadratic implementation-coupling cost

`V_impl := Var_Omega(K_x)+Var_Omega(K_y)`.

Every such implementation obeys

`boxed:
V_impl >= A_ex^(2)/(hbar nu).`

This is the first direct lower bound connecting the manuscript's kinematic synthesis action to a dynamical implementation quantity.

## 5. Consequences for temporal information

Using the clean bilateral WP18/R3 laws,

`A_ex^(2) >= (hbar nu/4) Tr F_N^tan/N`,

and, for the baseline SLD-QFI tangent block,

`A_ex^(2) >= (hbar nu/4) Tr H_SLD`,

one obtains

`boxed:
V_impl >= (1/4) Tr F_N^tan/N,`

and

`boxed:
V_impl >= (1/4) Tr H_SLD.`

For clean one-sided synthesis the common-record coefficient is stronger:

`A_ex^(2) >= (hbar nu/2) Tr F_N^tan/N`,

so

`boxed:
V_impl >= (1/2) Tr F_N^tan/N.`

The SLD-QFI coefficient remains `1/4`.

The `Tr H_SLD/4` inequality is consistent with the standard global-QFI/data-processing geometry; the new content is the exact spectral endpoint-action representation and its equality with a priced implementation-transition strength.

## 6. Sharpness in the existing fixed-total-energy extremizers

### Bilateral shell

Use

`|L>=|2_C,0_S>`, `|M>=|1_C,1_S>`, `|U>=|0_C,2_S>`

inside one total-energy eigenspace, baseline `|M>` and the WP18 exact family.

Choose Hermitian tangent generators such that

`-i K_x|M> = (c/2)(|L>+|U>)`,

`-i K_y|M> = (ic/2)(|L>-|U>)`.

Then

`Var(K_x)=c^2/2`,

`Var(K_y)=c^2/2`,

so

`V_impl=c^2`.

WP18 gives

`A_ex^(2)=hbar nu c^2`.

Therefore

`boxed: A_ex^(2)=hbar nu V_impl`

exactly.

Because the generators act entirely inside one degenerate total-energy shell,

`[K_x,H_C+H_S]=[K_y,H_C+H_S]=0`.

### One-sided shell

For the fixed-total-excitation-1 extremizer,

`|D>=|1_C,0_S>`, `|U>=|0_C,1_S>`,

choose generators realizing

`partial_x|psi>=c|U>`, `partial_y|psi>=-ic|U>`.

Then

`Var(K_x)=Var(K_y)=c^2`,

`V_impl=2c^2`,

while

`A_ex^(2)=2 hbar nu c^2`.

Again

`A_ex^(2)=hbar nu V_impl`

exactly.

Thus the generator-variance coefficient is sharp.

## 7. Net-energy/work no-go

The same sharp constructions prove that **net bare-energy change is not the dynamical resource**.

If

`[U(x,y),H_tot]=0`,

then the entire distribution of `H_tot` is invariant under the implementation. In the fixed-shell extremizers it is concentrated on a single energy eigenvalue for every `(x,y)`.

Therefore

`Delta <H_tot>=0`

and even the total-energy variance remains zero, while

`A_ex^(2)>0`, `V_impl>0`, and the temporal Fisher information is nonzero.

Hence no universal inequality of the form

`A_ex^(2) <= f(net bare-energy change)`

with `f(0)=0` can hold.

A meaningful dynamical cost must price the interaction/control that moves amplitude inside the conserved shell, not merely net energy consumption.

This also separates the present problem from Tajima–Shiraishi–Saito coherence cost for implementing a unitary that violates a subsystem conservation law. Their external asymmetry-battery cost can vanish for a desired **globally conserving** exchange, while the present coupling cost remains nonzero.

## 8. Time-dependent control-action corollary

Suppose a physical implementation over laboratory time `t in [0,tau]` has a parameter-linear control Hamiltonian in the baseline interaction picture,

`H(theta,t)=H_0(t)+x V_x(t)+y V_y(t)+O(theta^2)`.

The final tangent generators are

`K_j=(1/hbar) int_0^tau V_j^I(t) dt`.

Define the integrated RMS control-fluctuation lengths

`L_j := int_0^tau sqrt(Var_Omega[V_j^I(t)]) dt`.

The state-weighted centered-operator seminorm obeys Minkowski, so

`sqrt(Var(K_j)) <= L_j/hbar`.

Therefore

`boxed:
L_x^2+L_y^2
 >= hbar^2 V_impl
 >= (hbar/nu) A_ex^(2).`

For bilateral common-record information,

`boxed:
L_x^2+L_y^2 >= (hbar^2/4) Tr F_N^tan/N.`

For one-sided common-record information,

`boxed:
L_x^2+L_y^2 >= (hbar^2/2) Tr F_N^tan/N.`

For the SLD-QFI tangent block in either clean orientation class,

`boxed:
L_x^2+L_y^2 >= (hbar^2/4) Tr H_SLD.`

These are control-action / quantum-speed-limit-type quantities; generic integrated-Hamiltonian-norm cost is established prior art. Novelty must therefore be claimed, if at all, only for the exact connection to the spectral endpoint synthesis action in a globally conserving relational exchange.

## 9. Prior-art boundary

Mandatory comparisons:

- Tajima, Shiraishi, Saito, Phys. Rev. Research 2, 043374 (2020): external coherence/QFI cost required to implement operations that violate a subsystem conserved quantity under globally conserving dynamics. Different cost and different target operation class.
- Marvian, Phys. Rev. Lett. 129, 190502 (2022): QFI as asymptotic energetic-coherence formation cost for states. Does not give the endpoint-incidence coupling identity above.
- quantum speed-limit / optimal-control literature: integrated Hamiltonian norms or energy uncertainty bound state-motion speed. Do not claim generic novelty for `integral Delta H dt` or geodesic control cost.

Current targeted search has not found the exact identity

`A_G^(2)=(1/2) sum_j Tr[(G⊗I)K_j Omega_0 K_j]`

interpreted as the dynamical implementation of a rank-changing frequency-resolved endpoint action, nor the exact fixed-shell equality `A_ex=hbar nu V_impl`. Priority remains unverified.

## 10. What is and is not solved

### Solved in this work package

- The kinematic boundary action has an exact unitary-dilation coupling interpretation.
- Clean single-gap action lower-bounds a sharp generator-variance implementation cost.
- The same fixed-shell models saturate the dynamical coefficient.
- Net bare-energy change/work cannot be the universal resource.
- A time-dependent integrated RMS control-action lower bound follows.

### Not solved yet

1. General WP19 coherent-support geometry with overlapping endpoint roles and the optimal dynamical scalar cost.
2. Minimal implementation cost over all Stinespring dilations/CPTP encoders, not only smooth unitary dilations of a supplied global baseline.
3. A thermodynamic work cost for a fully autonomous controller including switching, battery, and reset.
4. Infinite-dimensional/continuous-variable extension.
5. Prior-art priority certification.

## 11. Immediate next attacks

1. Prove the exact identity for arbitrary mixed global baselines and arbitrary smooth two-parameter unitary curves in a basis-free way.
2. Determine whether minimizing `V_impl` over all unitary dilations equals a closed expression in the reduced tangent/action; candidate connection to SLD/Bures purification geometry.
3. Extend from time-independent tangent generators to arbitrary time-dependent controls with a rigorous interaction-picture seminorm proof.
4. Search specifically for endpoint-weighted Stinespring/QFI control-cost theorems.
5. Only after these pass, decide whether this belongs in the current paper or a follow-up.