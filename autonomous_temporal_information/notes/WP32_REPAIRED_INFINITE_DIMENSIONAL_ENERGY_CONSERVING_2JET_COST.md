# WP32 — Repaired exact infinite-dimensional energy-conserving prescribed-2-jet cost

## Status

**Corrected exact theorem proved.**

WP31 found the right mechanism—replace one coherent purification across infinitely many energies by a trace-class classical mixture—but its shell-normalization proof had a hidden restriction. It implicitly assumed that every nonzero block of the prescribed kernel curvature `C` lies in a target-energy shell already occupied by `rho_0`, because it formed `c_E=C_E/p_E`.

That assumption is not implied by `C>=C_min` and `[C,H_T]=0`. Arbitrary positive spectator curvature may lie in an otherwise unoccupied target-energy shell. A zero-energy ancilla cannot generate such curvature while conserving total energy.

The theorem conclusion nevertheless survives. The correct construction uses a **joint eigenbasis of `rho_0` and `H_T`, classical splitting of baseline eigenstate weights, and nonnegative ancilla energy compensation for spectator curvature**.

The resulting exact optimum remains

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

No fourth-moment condition is required.

## 1. Setup

Let `H_T` be self-adjoint and semibounded on a separable target Hilbert space.

Let `rho_0>=0` be trace class with strong stationarity

`U_t rho_0 U_t^dagger=rho_0`, `U_t=exp(-iH_T t/hbar)`.

Let `P=supp(rho_0)`, `Q=I-P`.

Let `D_j`, `j=1,...,d`, be Hermitian pure-boundary first derivatives satisfying

`P D_j P=Q D_j Q=0`

and strong energy covariance

`U_t D_j U_t^dagger=D_j`.

Assume

`L_j=Q D_j P rho_0^(-1/2)`

is Hilbert--Schmidt for every `j`.

Define

`C_min=2 sum_j L_j L_j^dagger`.

Prescribe a positive trace-class target-kernel Hessian contraction

`C>=C_min`

which strongly commutes with `H_T`.

Let

`S=(C-C_min)/2>=0`.

The implementation cost is

`V_impl=sum_j Var_(Omega_0)(K_j)`

for a smooth global unitary dilation with target reduction `rho_0`, first derivatives `D_j`, and target-kernel Hessian contraction `C`.

## 2. Joint energy/eigenvalue decomposition of the stationary trace-class baseline

Because `rho_0` is positive trace class, it is compact. Each nonzero eigenspace of `rho_0` has finite dimension.

Strong stationarity means every such eigenspace is invariant under the strongly continuous unitary group `U_t`. Restricted to a finite-dimensional invariant subspace, `U_t` is a finite-dimensional unitary representation of `R` and therefore has an orthonormal basis of characters `exp(-iE t/hbar)`.

Thus the support of `rho_0` has a countable orthonormal basis of simultaneous eigenvectors

`rho_0 |n> = lambda_n |n>`,

`H_T |n> = E_n |n>`,

with `lambda_n>0` and `sum_n lambda_n=1`.

This argument avoids any ambiguous unbounded-operator commutator statement: strong stationarity under the unitary group is enough.

## 3. Horizontal tangent columns

For each occupied support eigenvector define the normalized support-to-kernel tangent vector

`|h_(j,n)> := Q D_j |n> / lambda_n`.

Because `D_j` commutes with the target time evolution, every nonzero component of `h_(j,n)` has the **same target energy `E_n`** as `|n>`.

The Hilbert--Schmidt assumption gives

`sum_n lambda_n ||h_(j,n)||^2
 =sum_n ||Q D_j|n>||^2/lambda_n
 =Tr(L_j L_j^dagger)<infinity.`

Moreover

`Q D_j P=sum_n lambda_n |h_(j,n)><n|`.

Therefore a classical mixture of pure baseline branches can reproduce the complete first derivative without coherently purifying different support eigenvectors.

## 4. Spectral decomposition of the excess curvature

`S` is positive trace class and strongly commutes with `H_T`. The same compactness/invariance argument gives a countable spectral decomposition

`S=sum_r s_r |q_r><q_r|`,

`s_r>0`, `sum_r s_r=Tr S<infinity`,

with genuine target-energy eigenvectors

`H_T |q_r>=F_r |q_r>`.

The energies `F_r` need **not** occur in the support of `rho_0`.

This is the case omitted by WP31.

## 5. Classical splitting of one occupied baseline eigenstate

Choose any support eigenvector `|n_*>` with eigenvalue `lambda_*>0` and target energy `E_*`.

If `S=0`, no splitting is needed. Assume `S!=0`.

Choose arbitrary positive weights `w_r>0` satisfying

`sum_r w_r=lambda_*`.

For example, after enumerating the nonzero eigenvalues of `S`, one may take a normalized geometric sequence.

Replace the single global baseline branch of weight `lambda_*` by countably many **classically incoherent copies**

`w_r |n_*,a_r><n_*,a_r|`,

where the ancilla input states `|a_r>` are mutually orthogonal.

For every other support eigenvector `n!=n_*`, retain one branch of weight `lambda_n` with its own orthogonal ancilla label.

Tracing out the ancilla still gives exactly `rho_0`.

## 6. Ancilla energy compensation for arbitrary spectator energies

Give the ancilla a self-adjoint nonnegative Hamiltonian.

For every excess eigenvector `|q_r>` of target energy `F_r`, choose a nonnegative input ancilla energy `a_r` and a nonnegative output ancilla energy `b_r` satisfying

`E_* + a_r = F_r + b_r`.

A universal choice is

`a_r=max(0,F_r-E_*)`,

`b_r=max(0,E_*-F_r)`.

Use mutually orthogonal ancilla states even when some energies coincide.

Thus a baseline branch `|n_*,a_r>` and its excess flag `|q_r,b_r>` have exactly the same total energy.

The horizontal tangent attached to that baseline copy uses the **same input ancilla state `|a_r>`**, so it also has total energy `E_*+a_r` because its target energy remains `E_*`.

For every unsplit support branch `|n,a_n>`, choose any nonnegative ancilla input energy and use the same ancilla state for its horizontal tangent. Its target energy remains `E_n`.

Hence every branch generator constructed below acts inside one exact eigenspace of

`H_tot=H_T tensor I + I tensor H_E`.

No ancilla energy is negative, even if the target and spectator energies are unbounded above.

## 7. Branch tangent vectors

For an unsplit branch `n!=n_*`, define

`|chi_(j,n)>=|h_(j,n)> tensor |a_n>`.

For the split branch `n_*`, copy `r`, define horizontal pieces

`|chi_(j,*,r)^hor>=|h_(j,n_*)> tensor |a_r>`.

Assign all excess curvature to coordinate `j=1` without loss of generality for the prescribed metric contraction. Define the excess flag amplitude

`|eta_r>=sqrt(s_r/w_r) |q_r> tensor |b_r>`.

The input and output ancilla flags are chosen orthogonal, so

`Tr_E(|eta_r><n_*,a_r|)=0`

and

`Tr_E(|eta_r><chi_(j,*,r)^hor|)=0`.

Set

`chi_(1,*,r)=chi_(1,*,r)^hor+eta_r`,

`chi_(j,*,r)=chi_(j,*,r)^hor`, `j>1`.

Every component of `chi_(j,*,r)` has the same total energy as its baseline branch.

## 8. Branch generators and exact energy conservation

For each pure global baseline branch `|Omega_alpha>` and its tangent vector `|chi_(j,alpha)>`, define

`K_(j,alpha)=i(|chi_(j,alpha)><Omega_alpha|-|Omega_alpha><chi_(j,alpha)|)`.

Because `chi_(j,alpha)` is orthogonal to `Omega_alpha`, this is bounded Hermitian on the branch subspace and

`Var_(Omega_alpha)(K_(j,alpha))=||chi_(j,alpha)||^2`.

Because both vectors lie in the same exact total-energy eigenspace,

`[K_(j,alpha),H_tot]=0`.

Take the orthogonal direct sum over all branches:

`K_j=direct_sum_alpha K_(j,alpha)`.

The direct-sum operator may be unbounded, but it is self-adjoint on the standard direct-sum domain because every block is bounded self-adjoint.

For a parameter vector `theta`, define the unitary blockwise by

`U(theta)=direct_sum_alpha exp[-i sum_j theta_j K_(j,alpha)]`.

Every block is total-energy preserving, hence

`[U(theta),H_tot]=0`

strongly for all `theta`.

## 9. Exact first derivatives

Let the global baseline density operator be the classical branch mixture

`Omega_0=sum_alpha w_alpha |Omega_alpha><Omega_alpha|`.

For an unsplit support eigenstate `n`, its branch contributes

`lambda_n (|h_(j,n)><n|+h.c.)`.

For the split state `n_*`, every copy uses the same normalized horizontal tangent `h_(j,n_*)`, so the sum of its branch contributions is

`sum_r w_r (|h_(j,n_*)><n_*|+h.c.)
 =lambda_* (|h_(j,n_*)><n_*|+h.c.).`

The excess flags are first-order invisible after partial trace because their ancilla labels are orthogonal to the baseline input labels.

Summing all branches gives

`partial_j rho(0)=D_j`

exactly.

## 10. Exact prescribed kernel curvature

The horizontal branch contributions give

`2 sum_j sum_n lambda_n |h_(j,n)><h_(j,n)|
 =C_min.`

For excess mode `r`, the split baseline copy contributes

`2 w_r |eta_r><eta_r|`

after partial trace, and therefore

`2 w_r (s_r/w_r)|q_r><q_r|
 =2 s_r |q_r><q_r|.`

Summing over `r` gives `2S=C-C_min`.

All horizontal--excess partial-trace cross terms vanish by ancilla orthogonality.

Hence

`boxed:
Q sum_j partial_j^2 rho(0) Q=C`

exactly.

Again, the theorem prescribes the physical metric contraction of the kernel Hessian, not an arbitrary full mixed-second-derivative tensor.

## 11. Exact implementation cost

The horizontal cost is

`sum_j sum_n lambda_n ||h_(j,n)||^2
 =(1/2)Tr C_min.`

Classical splitting of `lambda_*` does not change it because `sum_r w_r=lambda_*`.

The excess cost is

`sum_r w_r ||eta_r||^2
 =sum_r s_r
 =Tr S
 =(1/2)Tr(C-C_min).`

Therefore

`boxed:
V_impl=(1/2)Tr C.`

The dimension-independent WP21/WP30 lower bound gives

`V_impl>=(1/2)Tr C`

for every smooth unitary dilation realizing the prescribed curvature.

Thus the construction is optimal:

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C.`

## 12. Trace-norm C^2 regularity needs only quadratic cost

The global baseline is a trace-class classical mixture, not one coherent vector.

For branch state `omega_alpha=|Omega_alpha><Omega_alpha|`,

`||[K_(j,alpha),omega_alpha]||_1<=2||K_(j,alpha)||`,

`||[K_(j,alpha),[K_(k,alpha),omega_alpha]]||_1
 <=4||K_(j,alpha)|| ||K_(k,alpha)||`.

The state-weighted quadratic sums are finite because

`sum_alpha w_alpha sum_j ||K_(j,alpha)||^2=V_impl=(1/2)Tr C<infinity.`

Hence first-derivative trace-norm majorants are summable by Cauchy--Schwarz, and all mixed second-derivative majorants are summable by Cauchy--Schwarz.

Termwise differentiation of the trace-class branch series is therefore justified by dominated convergence. The global and reduced families are trace-norm `C^2` at the origin.

No fourth moment is required.

## 13. Clean exact-exchange endpoint action

If the prescribed curvature is the clean single-gap endpoint curvature with

`G_ex=2 hbar nu Q`

on the relevant target kernel, then

`A_ex^(2)=(1/4)Tr(G_ex C)=(hbar nu/2)Tr C`.

Therefore

`boxed:
V_min=A_ex^(2)/(hbar nu).`

This holds for separable infinite-dimensional targets, unbounded occupied baseline energy support, and arbitrary additional stationary spectator curvature, including curvature in target-energy shells unoccupied at baseline.

## 14. What WP31 got wrong and what survives

### Defect

WP31 formed `c_E=C_E/p_E` shell by shell. This omitted the possibility `C_E!=0` with `p_E=0`.

Its claim that a zero-energy ancilla suffices for arbitrary prescribed `C` was therefore too strong.

### Surviving idea

The central insight was correct: use a **classical trace-class mixture** rather than one coherent purification across infinitely many energies. That is what removes the fourth-moment/domain obstruction.

### Corrected statement

A semibounded ancilla still suffices universally, but its branch input/output energies may need to compensate target-energy differences for excess spectator curvature. `H_E=0` is sufficient only in the special case where every implemented transition remains within the same target-energy shell.

## 15. Prior-art boundary

Energy-conserving and time-covariant Stinespring dilations are established prior art. Generic direct-sum self-adjointness, trace-class dominated convergence, Bures/Uhlmann geometry, and infinite-dimensional QFI are established mathematics.

Do not claim novelty for those ingredients.

The narrow candidate result remains:

> for a stationary rank-changing relational state family with a prescribed feasible metric-contracted target-kernel Hessian, the exact minimum state-weighted quadratic coupling cost over semibounded exactly energy-conserving dilations equals one half of the target kernel-curvature trace; in the clean single-gap geometry this equals the endpoint synthesis action divided by `hbar nu`.

Priority remains unverified.

## 16. Immediate audit work

1. build a validator with mixed/degenerate occupied energy sectors and excess curvature in **unoccupied** target-energy shells;
2. verify the branch-energy compensation and exact cost numerically under random PSD excess curvature;
3. audit the strong-stationarity -> countable joint energy/eigenbasis lemma;
4. search state-specific second-order energy-conserving Stinespring/purification literature;
5. update landing documents so WP31 is treated as a superseded intermediate proof and WP32 is canonical.