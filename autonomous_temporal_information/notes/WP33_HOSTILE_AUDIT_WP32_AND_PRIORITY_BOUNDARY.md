# WP33 — Hostile audit of WP32 and second-order implementation-cost priority boundary

## Status

**PASS after one explicit predecessor correction: WP31 is superseded, WP32 is canonical.**

WP32 was audited specifically against the failure mode discovered in WP31, the strong-stationarity functional analysis, trace-norm `C^2` differentiability of an unbounded direct-sum implementation, exact total-energy conservation with a semibounded ancilla, and nearby prior art in covariant Stinespring dilation, Bures/QFI horizontal geometry, and second-order PSD-cone tangent theory.

No new mathematical defect was found in WP32.

Priority remains **unverified, not certified**. The generic ingredients are heavily prior art; only the narrow state-specific prescribed-second-order-jet minimum-cost identity remains a candidate distinct contribution.

## 1. WP31 defect and WP32 repair

WP31 correctly identified that a classical energy-shell mixture removes the fourth-moment obstruction created by one coherent purification across infinitely many energies.

However, WP31 normalized every prescribed curvature block as

`C_E/p_E`.

That silently required

`C_E != 0 => p_E > 0`.

A feasible positive spectator curvature may instead lie in a target-energy shell with zero baseline population. Such curvature can strongly commute with the target Hamiltonian and still satisfy `C>=C_min`.

Therefore WP31's claim that `H_E=0` suffices for arbitrary prescribed `C` was false.

WP32 repairs this by:

1. expanding the stationary trace-class baseline in a countable joint `rho_0/H_T` eigenbasis;
2. splitting one occupied baseline eigenstate weight into countably many **classically incoherent ancilla-labelled copies**;
3. replicating the required horizontal tangent proportionally across those copies, leaving its total cost unchanged;
4. assigning every excess-curvature eigenmode its own output ancilla flag and nonnegative energy compensation;
5. forming the global encoded state as a trace-class classical branch mixture.

This handles arbitrary stationary spectator curvature, including target-energy shells unoccupied at baseline.

## 2. Strong stationarity implies countable occupied pure-point energy support

This point is subtle because the ambient target Hamiltonian may have continuous spectrum.

Assume strong stationarity

`U_t rho_0 U_t^dagger = rho_0`

for every real `t`, with

`U_t=exp(-i H_T t/hbar)`.

Because `rho_0` is positive trace class, it is compact. Its nonzero spectrum consists of countably many eigenvalues with finite multiplicity:

`rho_0=sum_a lambda_a P_a`, `lambda_a>0`.

Strong stationarity implies

`U_t P_a = P_a U_t`

for every nonzero spectral projector `P_a`. Hence each finite-dimensional subspace `Ran P_a` is invariant under the one-parameter unitary group.

On a finite-dimensional invariant subspace, the restricted strongly continuous unitary representation of `R` has the form

`U_t|_(Ran P_a)=exp(-i H_a t/hbar)`

for a finite-dimensional Hermitian matrix `H_a`, and therefore has an orthonormal basis of characters

`U_t |a,m> = exp(-i E_(a,m)t/hbar)|a,m>`.

By Stone's theorem these vectors lie in `Dom(H_T)` and satisfy

`H_T |a,m>=E_(a,m)|a,m>`.

The countable union of these finite bases spans `supp(rho_0)`.

Therefore a stationary trace-class state occupies only a **countable pure-point energy subspace**, even when the ambient Hamiltonian has additional continuous spectrum.

This is a property of the occupied state support, not a claim that the ambient Hamiltonian is pure point.

## 3. Energy covariance of the first derivative

WP32 assumes strong energy preservation of each pure-boundary derivative,

`U_t D_j U_t^dagger = D_j`.

The derivative `D_j` is trace class for a trace-norm differentiable state family and therefore bounded.

If `|n>` is an occupied target-energy eigenvector of energy `E_n`, then

`U_t D_j|n>
 =D_j U_t|n>
 =exp(-iE_n t/hbar)D_j|n>`.

Thus every nonzero vector `QD_j|n>` is itself a genuine target-energy eigenvector at the **same energy `E_n`**.

This justifies the shell-preserving horizontal part of every branch without any domain ambiguity involving an unbounded commutator `[H_T,D_j]`.

## 4. The minimum curvature also preserves energy

Let

`L_j=Q D_j P rho_0^(-1/2)`

in the WP29 Hilbert--Schmidt sense.

Because `rho_0` strongly commutes with `U_t`, all of its spectral functions, including the support-restricted inverse square root on its natural domain, are invariant under `U_t`.

The bounded Hilbert--Schmidt closure `L_j` therefore intertwines the same target-energy representation, and

`L_j L_j^dagger`

strongly commutes with `H_T`.

Hence

`C_min=2 sum_j L_j L_j^dagger`

strongly commutes with `H_T`.

Since prescribed `C` does as well,

`S=(C-C_min)/2`

is positive trace class and strongly energy preserving.

Because `S` is compact, exactly the same finite-multiplicity argument as for `rho_0` gives an energy-adapted spectral decomposition

`S=sum_r s_r |q_r><q_r|`,

`H_T|q_r>=F_r|q_r>`.

The energies `F_r` need not appear in the support of `rho_0`.

## 5. Classical splitting does not change the horizontal tangent or its cost

Choose one occupied eigenstate `|n_*>` with baseline weight `lambda_*>0`.

Split it into mutually orthogonal ancilla-labelled copies with positive weights

`w_r>0`, `sum_r w_r=lambda_*`.

For every copy use the same normalized horizontal column

`h_(j,n_*)=Q D_j|n_*>/lambda_*`.

Then the summed first derivative from the split copies is

`sum_r w_r (|h><n_*|+h.c.)
=lambda_* (|h><n_*|+h.c.)`,

exactly the original contribution.

Likewise its state-weighted quadratic cost is unchanged:

`sum_r w_r ||h_(j,n_*)||^2
=lambda_* ||h_(j,n_*)||^2`.

Thus classical splitting is cost-neutral for the required first-order tangent.

## 6. Arbitrary stationary spectator curvature can be energy matched with a semibounded ancilla

For excess eigenmode `|q_r>` with target energy `F_r`, use one split copy of `|n_*>`, target energy `E_*`.

Choose nonnegative ancilla input/output energies

`a_r=max(0,F_r-E_*)`,

`b_r=max(0,E_*-F_r)`.

Then

`E_*+a_r=F_r+b_r`.

Choose mutually orthogonal input/output ancilla vectors even if some numerical energies coincide.

The excess flag

`eta_r=sqrt(s_r/w_r)|q_r,b_r>`

has the same total energy as its baseline input branch `|n_*,a_r>`.

The horizontal tangent on that split branch uses the same input ancilla vector `|a_r>` and remains at target energy `E_*`; it therefore also has the same total energy.

Consequently the full tangent vector, horizontal plus excess flag, lies in one exact total-energy eigenspace.

The rank-two branch generator

`K=i(|chi><Omega|-|Omega><chi|)`

commutes exactly with `H_T+H_E` on that branch.

The ancilla Hamiltonian can be defined diagonally on the countable orthonormal input/output flag basis with eigenvalues `{a_r,b_r}` and zero on unused basis vectors. All eigenvalues are nonnegative, so `H_E` is self-adjoint and semibounded.

No fixed global energy shell and no negative ancilla energy are required.

## 7. First-order invisibility and exact excess curvature

Input and output ancilla labels are orthogonal. Therefore

`Tr_E(|eta_r><Omega_r|)=0`

and every horizontal--excess partial-trace cross term also vanishes.

The excess flag is therefore first-order invisible on the target.

Its contribution to the metric-contracted target kernel Hessian is

`2w_r |eta_r><eta_r|`

after partial trace, namely

`2s_r |q_r><q_r|`.

Summing all excess modes gives

`2S=C-C_min`.

Adding the horizontal minimum curvature reproduces **exactly**

`C`.

No leakage or inequality remains in the construction.

## 8. Exact cost

The horizontal branch cost is

`(1/2)Tr C_min`.

The excess cost is

`sum_r w_r ||eta_r||^2
=sum_r s_r
=Tr S
=(1/2)Tr(C-C_min)`.

Thus the construction has

`boxed: V_impl=(1/2)Tr C.`

The WP21/WP30 dimension-independent lower bound gives the reverse inequality for every smooth dilation realizing the same prescribed target kernel curvature.

Therefore

`boxed:
inf V_impl=(1/2)Tr C.`

The construction attains the infimum within the class of semibounded exactly energy-conserving dilations.

For a clean single-gap endpoint price,

`A_ex^(2)=(hbar nu/2)Tr C`,

so

`boxed: V_min=A_ex^(2)/(hbar nu).`

## 9. Direct-sum self-adjointness

Each implementation branch is placed in an orthogonal ancilla-labelled subspace.

For coordinate `j`, the branch operator `K_(j,alpha)` is bounded self-adjoint. The global operator

`K_j=direct_sum_alpha K_(j,alpha)`

is therefore self-adjoint on the standard direct-sum domain

`Dom(K_j)={psi=(psi_alpha): sum_alpha ||K_(j,alpha)psi_alpha||^2<infinity}`.

No uniform bound on the shell operator norms is required.

For a multi-parameter local family one may define the unitary **blockwise**,

`U(theta)=direct_sum_alpha exp[-i sum_j theta_j K_(j,alpha)]`,

rather than first demanding a globally bounded operator `sum_j theta_j K_j`.

Each block is finite dimensional (or finite rank on its active subspace) and energy preserving. The direct sum is unitary. Strong continuity follows from dominated convergence on the square-summable norm of an arbitrary Hilbert-space vector because every block unitary has norm one.

## 10. Trace-norm `C^2` audit

The global baseline is the classical trace-class mixture

`Omega_0=sum_alpha w_alpha omega_alpha`,

`omega_alpha=|Omega_alpha><Omega_alpha|`.

This is the decisive difference from the coherent-purification route that generated the WP30 fourth-moment concern.

For one branch, Duhamel differentiation of

`U_alpha(theta) omega_alpha U_alpha(theta)^dagger`

gives locally uniform bounds

`||partial_j omega_alpha(theta)||_1
 <=2 ||K_(j,alpha)||`,

and for mixed second derivatives

`||partial_j partial_k omega_alpha(theta)||_1
 <=4 ||K_(j,alpha)|| ||K_(k,alpha)||`.

At the origin, when the `K_j` do not commute, the exact mixed derivative is the symmetrized double-commutator expression generated by the exponential of the linear combination `sum_j theta_j K_j`; the above product bound remains valid. No claim that the unsymmetrized nested commutator is the exact mixed derivative is needed.

The optimal quadratic cost gives

`sum_alpha w_alpha sum_j ||K_(j,alpha)||^2
=(1/2)Tr C<infinity`.

Therefore

`sum_alpha w_alpha ||K_(j,alpha)||<infinity`

by Cauchy--Schwarz, and

`sum_alpha w_alpha ||K_(j,alpha)|| ||K_(k,alpha)||<infinity`

by Cauchy--Schwarz.

The branchwise first and mixed second derivatives are thus dominated by summable trace-norm majorants independent of sufficiently small `theta`.

Termwise differentiation of the trace-class series follows from dominated convergence. The global encoded state is trace-norm `C^2` locally, and partial trace preserves that regularity by contractivity.

Hence finite **quadratic** cost is sufficient. A fourth moment is not required.

## 11. Finite baseline ancilla mean energy can also be imposed

The WP32 theorem only needs a semibounded ancilla, but a useful strengthening is available.

The compensation input energies are

`a_r=max(0,F_r-E_*)`.

Choose split probabilities

`mu_r = Z^(-1) 2^(-r)/(1+a_r)`,

`w_r=lambda_* mu_r`,

where

`Z=sum_r 2^(-r)/(1+a_r)`.

Then every `w_r` is positive and `sum_r w_r=lambda_*`, while

`sum_r w_r a_r
 <=lambda_*/Z sum_r 2^(-r)<infinity`.

Thus the baseline ancilla can be chosen with finite mean energy even when the required compensation energies are unbounded.

The excess implementation cost is unchanged because

`w_r ||eta_r||^2=s_r`

independently of `w_r`.

Therefore if the target baseline itself has finite mean energy, the constructed global baseline can also be chosen with finite mean total bare energy.

This is **not** a thermodynamic-work theorem. No claim is made about switching work, thermal reset, partition-function normalizability, or battery depletion.

## 12. Numerical hostile validation

Permanent validator:

`numerics/verify_wp32_repaired_energy_conserving_2jet_cost.py`.

It explicitly includes the WP31 failure mode:

- mixed baseline;
- degenerate occupied target-energy sector;
- random complex energy-preserving support-to-kernel tangents;
- random positive excess curvature in target-energy shells **unoccupied at baseline**;
- nonnegative ancilla input/output energy compensation;
- exact first derivative;
- exact prescribed kernel curvature;
- exact cost equality;
- exact branchwise `[K,H_tot]=0`.

The random stress test passes to machine precision.

The older WP31 validator remains valid only as the special same-target-energy / zero-ancilla-energy case.

## 13. Prior-art audit

### Covariant and energy-conserving Stinespring dilation

This is established prior art and is not a novelty claim.

Scutaru, *Reports on Mathematical Physics* **16**, 79--87 (1979), proved a Stinespring-type theorem for covariant completely positive maps on `C*`-algebras, DOI `10.1016/0034-4877(79)90040-5`.

Faist, Berta, and Brandao, *Communications in Mathematical Physics* **384**, 1709--1750 (2021), explicitly use the fact that a time-covariant channel admits a Stinespring dilation with an energy-conserving unitary and an environment carrying its own Hamiltonian (their Lemma 7.2), citing Scutaru, Keyl--Werner, and Marvian's symmetry thesis.

Accordingly, WP32 must not be framed as a new covariant Stinespring theorem.

### First-order QFI / variance / horizontal geometry

Also prior art.

The relation between QFI and minimum variance/purification geometry is established through Bures/Uhlmann theory and convex-roof variance results. Yu (2013) proved QFI as four times the convex roof of variance; Toth--Petz gave the preceding extremal formulation.

Carrasco and Spehner, arXiv:2606.06759 (2026), derive Bures geodesics for non-faithful states and discuss QSL consequences. This further confirms that first-order rank-deficient Bures/QFI geometry is not the candidate novelty.

### Second-order cone geometry

Second-order tangent-set and semidefinite-cone geometry are established optimization theory. Bonnans, Cominetti, and Shapiro, *SIAM J. Optim.* **9**, 466--492 (1999), develop second-order tangent-set optimality theory and explicitly note second-order regularity for semidefinite programming.

Thus the PSD-cone curvature inequality is infrastructure, not novelty.

### Targeted search for the WP32-specific identity

Focused searches for combinations of

- prescribed second-order quantum-state curvature/Hessian;
- state-specific Stinespring implementation;
- minimum dilation generator variance;
- second-order purification cost;
- local quantum-state `2`-jets;
- energy-conserving prescribed curvature

did **not** locate a theorem matching

`inf V_impl=(1/2)Tr C`

for a prescribed feasible rank-changing **target kernel Hessian contraction**, together with an exactly energy-conserving state-specific construction and the spectral endpoint-action identity

`V_min=A_ex/(hbar nu)`.

This negative search result is not priority certification.

## 14. Hostile verdict

### Mathematical correctness

**PASS** for WP32 under its stated assumptions.

### Scope corrections required

1. WP31 is superseded and must not be cited as the canonical theorem.
2. `H_E=0` is only a special case; arbitrary spectator curvature may require nonzero but nonnegative compensation energies.
3. The theorem prescribes the **metric-contracted target kernel Hessian**, not the complete mixed second-derivative tensor.
4. Finite-information regularity remains essential:
   - trace-class stationary baseline;
   - Hilbert--Schmidt right-relative tangents;
   - positive trace-class prescribed kernel curvature.
5. `V_impl` is a state-weighted quadratic coupling/control cost, not thermodynamic work.
6. Generic covariant Stinespring dilation, Bures/QFI horizontal geometry, and PSD second-order tangent mathematics are prior art.

### Significance

The post-R3 program now answers three major hostile criticisms in a controlled setting:

- **kinematic vs dynamical:** exact minimum implementation-coupling theorem;
- **finite-dimensionality:** separable infinite-dimensional extension;
- **exact resonance:** quantitative WP25/WP27 residual laws.

The remaining physical limitation is chiefly that the cost is still a local unitary coupling/action measure rather than a full noisy thermodynamic implementation cost.

## 15. Publication recommendation after audit

The WP21--WP32 chain is now large and conceptually coherent enough to stand on its own:

1. endpoint Hessian as exact implementation coupling;
2. first-order horizontal minimum;
3. prescribed nonminimal kernel-2-jet minimum;
4. exact energy-conserving construction;
5. approximate-gap robustness;
6. infinite-dimensional completion.

**Default recommendation: keep the current R3 manuscript frozen and develop a separate follow-up paper centered on the dynamical implementation theorem.**

An R4 that imports the whole chain would likely dilute the two-regime paper's narrative and substantially increase referee surface area. If R4 is used at all, it should add at most one concise dynamical corollary, not the complete WP21--WP32 program.

## 16. Next work

1. synchronize all landing documents from WP31 to canonical WP32/WP33 status;
2. create a follow-up-paper theorem stack and significance gate before drafting prose;
3. perform one additional targeted literature search around local channel geometry / second-order Stinespring interpolation;
4. if theorem work continues, prioritize noisy/CPTP implementation cost or approximate-exchange dynamical cost rather than more edge-case completion.