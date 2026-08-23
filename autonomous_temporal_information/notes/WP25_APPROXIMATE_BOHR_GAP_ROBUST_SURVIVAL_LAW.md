# WP25 — Leakage-corrected survival law for approximate Bohr-gap tangents

## Status

**New robustness theorem proved for finite-dimensional stationary baselines.**

This directly addresses the exact-commutator idealization identified in external review. The exact spectral-survival law is stable under detuning/off-resonant leakage: the only change is a lowered tail threshold plus an explicit residual penalty.

This is not yet the full arbitrary-coherent-support autonomous extension of WP06/WP19. The clean theorem assumes the baseline commutes with the Hamiltonian whose approximate gap is being tested.

## 1. Setup

Let `H>=E_* I` be finite dimensional and let

`[rho_0,H]=0`.

Let `A` be a trace-zero complex tangent with positive affine physical radius

`R_lin=R>0`.

Then `A=PAP` on `P=supp(rho_0)` and

`B=rho_0^{-1/2} A rho_0^{-1/2}`

obeys

`||B|| <= 2/R`

by the numerical-radius argument of WP02.

Fix a target positive angular frequency `nu>0` and define the Bohr-gap residual

`boxed:
R_nu := [H,A]-hbar nu A.`

Define its natural support-weighted squared size

`boxed:
eta_nu^2 := Tr(R_nu rho_0^+ R_nu^dagger).`

This has units of energy squared times the tangent-weighted score norm.

For `0<delta<nu`, define the spectral tail

`T(omega):=Tr[rho_0 1_{[E_*+hbar omega,infinity)}(H)].`

## 2. Matrix-element decomposition

Because `rho_0` and `H` commute, choose a joint eigenbasis

`rho_0=sum_n p_n |n><n|`,

`H=sum_n E_n |n><n|`.

On the support,

`A_mn=sqrt(p_m) B_mn sqrt(p_n)`.

The right-supported weighted tangent norm is

`J(A|rho_0)
 = Tr(A rho_0^+ A^dagger)
 = sum_(m,n) p_m |B_mn|^2.`

Partition matrix elements into

`N_delta := {(m,n): |E_m-E_n-hbar nu| < hbar delta}`

and its complement.

Write

`J=J_near+J_off`.

## 3. Near-resonant contribution is paid by a slightly lower spectral tail

For every near-resonant pair,

`E_m-E_n > hbar(nu-delta)`.

Since `E_n>=E_*`, necessarily

`E_m>=E_*+hbar(nu-delta)`.

Therefore all near-resonant range indices lie in the upper tail projector

`P_U(delta)=1_{[E_*+hbar(nu-delta),infinity)}(H)`.

Hence

`J_near
 <= sum_(m in U,n) p_m |B_mn|^2`

`= Tr[P_U rho_0 B B^dagger]`

`<= ||B||^2 Tr(P_U rho_0)`

`<= (4/R^2) T(nu-delta).`

Thus

`boxed:
J_near <= 4 T(nu-delta)/R^2.`

## 4. Off-resonant contribution is controlled by the commutator residual

The residual matrix elements are

`(R_nu)_mn=(E_m-E_n-hbar nu)A_mn`.

Therefore

`eta_nu^2
 = sum_(m,n) p_m |B_mn|^2 |E_m-E_n-hbar nu|^2.`

Every off-resonant term has

`|E_m-E_n-hbar nu| >= hbar delta`,

so

`boxed:
J_off <= eta_nu^2/(hbar^2 delta^2).`

Combining,

`boxed:
J(A|rho_0)
 <= 4 T(nu-delta)/R^2
   + eta_nu^2/(hbar^2 delta^2).`

## 5. Finite-copy arbitrary-POVM Fisher law

For any finite `N` and any collective POVM on `rho(theta)^{⊗N}`, the same weighted score argument as WP02 gives

`Tr F_N^tan/N <= J(A|rho_0)`.

The trace-zero condition on `A` removes cross-copy terms exactly.

Therefore, for every `0<delta<nu`,

`boxed:
(R^2/4) [Tr F_N^tan/N]
 <= T(nu-delta)
   + R^2 eta_nu^2/(4 hbar^2 delta^2).`

Optimizing the arbitrary window gives

`boxed:
(R^2/4) [Tr F_N^tan/N]
 <= inf_(0<delta<nu)
    {T(nu-delta)+R^2 eta_nu^2/(4 hbar^2 delta^2)}.`

This is the leakage-corrected robust survival law.

## 6. Exact-gap limit

If

`[H,A]=hbar nu A`,

then `eta_nu=0`. The bound becomes

`(R^2/4)Tr F_N/N <= T(nu-delta)`

for every `delta>0`. Letting `delta downarrow 0` and using continuity from above of the spectral measure yields

`boxed:
(R^2/4)Tr F_N/N <= T(nu),`

recovering WP02 exactly.

## 7. Relative RMS-detuning form

When `J>0`, define the tangent-weighted RMS frequency mismatch

`sigma_nu^2 := eta_nu^2/(hbar^2 J).`

Then

`J_off <= (sigma_nu^2/delta^2)J`.

For any `delta>sigma_nu`,

`J <= 4T(nu-delta)/R^2 + (sigma_nu^2/delta^2)J`,

so

`boxed:
(R^2/4)J
 <= T(nu-delta)/(1-sigma_nu^2/delta^2).`

Consequently

`boxed:
(R^2/4)Tr F_N/N
 <= T(nu-delta)/(1-sigma_nu^2/delta^2).`

This form makes the physical tradeoff transparent: a mode with small RMS detuning behaves like an exact gap after broadening the required spectral support by `delta`, at a multiplicative leakage penalty.

## 8. Locally stationary autonomous dual form

Suppose now

`[rho_0,H_S]=[rho_0,H_C]=0`

and the intended relational tangent is approximately

`[H_S,A] ~= +hbar nu A`,

`[H_C,A] ~= -hbar nu A`.

Define

`R_S=[H_S,A]-hbar nu A`,

and apply the positive-gap theorem to `A^dagger` on the clock side,

`R_C^+=[H_C,A^dagger]-hbar nu A^dagger`.

Let

`eta_S^2=Tr(R_S rho_0^+ R_S^dagger)`,

`eta_C^2=Tr(R_C^+ rho_0^+ R_C^{+dagger})`.

Then, allowing independent windows `delta_S,delta_C`,

`boxed:
(R^2/4)Tr F_N/N
 <= min{
 T_S(nu-delta_S)+R^2 eta_S^2/(4hbar^2 delta_S^2),
 T_C(nu-delta_C)+R^2 eta_C^2/(4hbar^2 delta_C^2)
 }.`

Thus the two-sided autonomous survival principle is quantitatively stable to off-resonant leakage for locally energy-stationary baselines.

The arbitrary coherent/history-state analogue, where `rho_0` need not commute with `H_C` or `H_S` separately, remains open.

## 9. Interpretation

The exact commutator is not a brittle all-or-nothing assumption.

A tangent can be decomposed operationally into:

1. near-resonant matrix elements, which must terminate in the spectral tail above `hbar(nu-delta)`;
2. off-resonant leakage, whose total weighted strength is bounded by the commutator residual divided by the detuning window.

This gives a controlled theorem for anharmonicity, imperfect resonance, and weak off-resonant coupling at the level of the encoded tangent.

It does **not** yet model decoherence during encoding. Parameter-independent noise after encoding is harmless for the necessary-resource direction by Fisher/QFI data processing, but noisy generator dynamics requires separate treatment.

## 10. Sharpness and limitations

- The exact-gap limit recovers the sharp WP02 coefficient.
- The leakage penalty is Chebyshev/Markov-type in the tangent-weighted detuning distribution and is generally not expected to be sharp for a detailed spectral line shape.
- The theorem is currently finite dimensional.
- Separate local stationarity is required for the simple autonomous dual form.
- The zero-radius synthesis/action regime under approximate gap structure remains open.

## 11. Immediate next work

1. Add a random finite-dimensional validator of the near/off decomposition and optimized bound.
2. Search prior art for approximate eigenoperator/Bohr-mode perturbation bounds in resource theory of asymmetry and open quantum systems.
3. Determine whether the same residual method extends to the zero-radius endpoint-action theorem.
4. Compare the value of an approximate-gap extension against an infinite-dimensional theorem as the next publication-significance move.
