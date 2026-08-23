# WP30 — Infinite-dimensional dynamical 2-jet cost and the energy-conservation domain boundary

## Status

**Exact unconstrained unitary-dilation implementation minimum extended to separable infinite-dimensional systems under the WP29 Hilbert--Schmidt regularity assumptions.**

**Exact energy-conserving equality is proved without additional domain work when the relevant target energy support is bounded above.**

For stationary baselines with unbounded energy support, the finite-dimensional fixed-shell purification cannot be transplanted naively without introducing an ancilla Hamiltonian unbounded below. A direct-sum unbounded-generator construction is plausible but needs a separate self-adjointness/`C^2` domain theorem. This is recorded as a genuine remaining boundary, not hand-waved away.

## 1. Setup

Let the target Hilbert space be separable.

Let `rho_0` be trace class with support `P`, kernel `Q`, and spectral decomposition

`rho_0=sum_n lambda_n |n><n|`, `lambda_n>0`.

Let `D_j`, `j=1,...,d`, be pure-boundary Hermitian first derivatives with

`P D_j P=Q D_j Q=0`.

Assume

`L_j:=Q D_j P rho_0^{-1/2}`

is Hilbert--Schmidt for every coordinate.

Define

`C_min:=2 sum_j L_j L_j^dagger`,

which is positive trace class.

Prescribe a positive trace-class target kernel Hessian contraction

`C>=C_min`.

The implementation cost for a smooth global unitary dilation with tangent generators `K_j` and global baseline `Omega_0` is

`V_impl=sum_j Var_Omega0(K_j)`.

## 2. Universal lower bound remains exact

The WP21 kernel-curvature identity is valid for bounded tangent generators and extends by quadratic-form approximation whenever the displayed variances are finite:

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

The target-support/kernel variance decomposition gives

`Var_Omega0(K_j)
 >=Tr[Omega_0 K_j(Q⊗I)K_j]`.

Summing and tracing the prescribed kernel Hessian therefore yields

`boxed:
V_impl>=(1/2)Tr C.`

This lower bound is dimension independent.

## 3. Infinite-dimensional purification construction

Use the canonical separable purification

`|Omega>=sum_n sqrt(lambda_n)|n>_T |n>_E`.

For each coordinate define the horizontal tangent vector directly by

`|chi_j^hor>
 :=sum_n [Q D_j |n>/sqrt(lambda_n)]⊗|n>_E.`

The Hilbert--Schmidt assumption is exactly the condition that this vector has finite norm:

`||chi_j^hor||^2
 =Tr(L_j L_j^dagger)<infinity`.

It is orthogonal to `Omega`, and

`Tr_E(|chi_j^hor><Omega|+h.c.)=D_j`.

Moreover

`2 sum_j Tr_E[Q|chi_j^hor><chi_j^hor|Q]
 =C_min`.

Let

`S=(C-C_min)/2>=0`.

Since `S` is positive trace class, choose a separable purification

`|eta> in Q⊗E_flag`

with

`Tr_Eflag |eta><eta|=S`.

Choose the flag ancilla orthogonal to all baseline purification flags. Then all baseline--flag and horizontal--flag partial-trace cross terms vanish.

Set, for example,

`chi_1=chi_1^hor+eta`,

`chi_j=chi_j^hor`, `j>1`.

Then the first derivatives remain exactly `D_j`, while the kernel Hessian contraction becomes exactly `C`.

The total squared tangent-vector norm is

`sum_j ||chi_j||^2
 =(1/2)Tr C_min+Tr S
 =(1/2)Tr C`.

## 4. Bounded finite-rank global generators

Although the target-only horizontal generator can be unbounded when `rho_0` has eigenvalues tending to zero, the dilation construction does **not** require that generator.

Each `chi_j` is a single finite-norm vector orthogonal to the normalized `Omega`. Therefore the rank-two global operator

`K_j=i(|chi_j><Omega|-|Omega><chi_j|)`

is bounded and Hermitian, with

`||K_j||=||chi_j||`.

It satisfies

`-iK_j|Omega>=chi_j`,

`<Omega|K_j|Omega>=0`,

and

`Var_Omega(K_j)=||chi_j||^2`.

The unitary family

`U(theta)=exp[-i sum_j theta_j K_j]`

is norm-analytic in the parameters and generates a trace-norm smooth reduced family.

Hence

`boxed:
inf_(all smooth unitary dilations) V_impl
 =(1/2)Tr C.`

This is the exact infinite-dimensional analogue of WP23 **without** an energy-conservation constraint.

## 5. Equality with the clean spectral endpoint action

If the prescribed kernel curvature lies in a clean single-gap endpoint sector with bounded price

`G_ex=2hbar nu Q`

on that curvature, then

`A_ex=(1/4)Tr(G_ex C)
     =(hbar nu/2)Tr C`.

Therefore

`boxed:
V_min=A_ex/(hbar nu)`

for the unconstrained infinite-dimensional unitary-dilation problem.

Thus the kinematic/dynamical equality itself is not finite-dimensional.

## 6. Exact energy conservation with bounded target-energy support

Now assume a self-adjoint semibounded target Hamiltonian `H_T` and

`[rho_0,H_T]=0`,

`[D_j,H_T]=0`,

`[C,H_T]=0`.

Because `rho_0` is compact, each nonzero eigenspace of `rho_0` is finite dimensional and invariant under `H_T`; therefore its basis can be chosen from genuine normalizable energy eigenvectors.

Assume additionally that every target energy appearing in the support of `rho_0`, the horizontal tangent ranges, and `C` is bounded above by some finite `E_max`.

Choose `E_*>E_max` and assign each baseline/flag ancilla associated with target energy `E` the energy

`E_*-E>=0`.

The ancilla Hamiltonian is then semibounded. Baseline purification vectors, horizontal tangent vectors, and excess-curvature flags all lie in the single global energy shell `E_*`.

The bounded rank-two generators above therefore commute exactly with

`H_tot=H_T+H_E`.

Consequently

`boxed:
inf_(semibounded energy-conserving dilations) V_impl
 =(1/2)Tr C`

under the bounded-energy-support hypothesis.

## 7. Why unbounded stationary energy support is nontrivial

If the target support contains arbitrarily large energies, the finite-dimensional fixed-shell trick would assign ancilla energies

`E_*-E`

that tend to `-infinity` for any fixed `E_*`.

That produces an ancilla Hamiltonian unbounded below and is not an acceptable semibounded physical energy model.

A different construction can keep the ancilla semibounded by allowing different total-energy shells. For example, a copy-energy ancilla assigns the same nonnegative energy `E` to a flag paired with a target state of energy `E`.

However, the global generator must then be a direct sum over infinitely many energy shells. The shellwise coupling strengths can diverge as the baseline eigenvalues tend to zero even while the **state-weighted variance** remains finite. The resulting generator may be unbounded.

To claim a fully energy-conserving theorem one must prove:

1. the direct-sum generator is self-adjoint on a dense domain;
2. the baseline purification lies in the domain required for the first and second state derivatives;
3. `exp(-i theta K)` produces the prescribed trace-norm `C^2` reduced family;
4. the total-energy commutator vanishes in the appropriate strong sense.

Hilbert--Schmidt first-order cost alone does not automatically imply all of these higher-domain properties.

Therefore **no unrestricted unbounded-energy-support energy-conserving equality is claimed yet**.

## 8. Potential sufficient strengthening

A natural stronger regularity condition is a shellwise fourth-moment bound ensuring the purification lies in `Dom(K_j^2)`.

In an energy-adapted decomposition let `Omega_E` and `chi_{j,E}` be the baseline and tangent components in one energy shell. A sufficient condition for the obvious shellwise rank-two generator is

`sum_E ||chi_{j,E}||^4 / ||Omega_E||^2 < infinity`.

This is stronger than finite variance

`sum_E ||chi_{j,E}||^2<infinity`.

Under such a condition the direct-sum construction should give the required second derivative. This remains to be written as a formal theorem.

## 9. Significance

WP30 sharpens the scope of the finite-dimensional criticism:

- the exact minimum **dilation coupling cost** and endpoint-action equality extend to separable infinite-dimensional systems under finite-information regularity;
- what remains genuinely difficult is imposing **semibounded exact energy conservation** when the stationary state occupies infinitely many unbounded energy shells.

This is a domain/physical-Hamiltonian issue, not a failure of the resource geometry itself.

## 10. Prior-art boundary

Infinite-dimensional Bures/QFI, SLD forms, unbounded logarithmic derivatives, and purification geometry are established subjects. Do not claim novelty for them.

The recent infinite-dimensional QFI literature explicitly treats trace-class state models and potentially unbounded SLDs. Likewise Bures metrics have operator-algebraic extensions.

The candidate contribution remains only the specific endpoint-action / prescribed-kernel-curvature implementation identity.

## 11. Next work

1. Decide whether the shellwise fourth-moment condition is close to necessary or merely convenient.
2. Prove the energy-conserving direct-sum theorem under an explicit sufficient domain condition.
3. Audit infinite-dimensional QFI/Bures sources before any publication claim.
4. Keep thermodynamic work/reset costs separate from generator-variance implementation cost.
