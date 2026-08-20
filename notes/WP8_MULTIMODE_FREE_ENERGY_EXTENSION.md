# WP8 — Multimode free-energy extension

**Date:** 2026-08-19

## Result

The single-mode finite-temperature free-energy noise frontier extends **exactly and without a mode-count penalty** to any number of degenerate-frequency harmonic detector pointer modes when the signal couples through a normalized collective mode.

---

# 1. Degenerate harmonic apparatus

Let the detector apparatus contain `m` bosonic pointer modes of the same frequency `omega_D`:

\[
H_D
=\frac{\hbar\omega_D}{2}
\sum_{j=1}^m(X_j^2+P_j^2).
\]

At inverse temperature `beta`, the thermal reference is

\[
\tau_\beta^{(m)}
=\tau_{\beta,1}^{\otimes m}.
\]

Define

\[
a=\beta\hbar\omega_D/2,
\qquad
D_0=\beta\Delta F_\beta.
\]

Let `c` be any normalized collective bosonic mode obtained by a passive unitary mixing of the detector modes. Its quadrature is denoted `X_c`.

Because all frequencies are equal, the apparatus Hamiltonian is invariant under every passive mode rotation:

\[
U_{\rm pass}H_DU_{\rm pass}^\dagger=H_D.
\]

The thermal reference is therefore invariant as well.

There exists a passive rotation carrying `c` to mode 1, so the optimization of `Var(X_c)` at fixed relative entropy/free energy is unitarily equivalent to the optimization of `Var(X_1)`.

---

# 2. Direct Gibbs-variational proof

Apply the relative-entropy variational inequality with

\[
K=-sX_c^2,
\qquad s>0.
\]

After a passive rotation taking `X_c -> X_1`,

\[
\beta H_D+sX_c^2
\sim
(a+s)X_1^2+aP_1^2
+
a\sum_{j=2}^m(X_j^2+P_j^2).
\]

The orthogonal `m-1` thermal modes factor out of the partition-function ratio exactly. Hence

\[
\frac{Z_s^{(m)}}{Z_0^{(m)}}
=
\frac{\sinh a}
{\sinh\sqrt{a(a+s)}},
\]

identical to the one-mode ratio.

Therefore every centered apparatus state satisfying

\[
D(\rho_D\|\tau_\beta^{(m)})\le D_0
\]
obeys, for every normalized collective quadrature,

\[
\boxed{
\operatorname{Var}(X_c)
\ge
v_F(D_0,a),
}
\]

where

\[
v_F(D_0,a)
=
\sup_{s>0}
\frac{
\ln[\sinh\sqrt{a(a+s)}/\sinh a]-D_0
}{s}.
\]

**Status:** PROVED for arbitrary apparatus states at the level of the quadrature second-moment/noise floor.

---

# 3. Saturating state

The bound is saturated by

\[
\boxed{
\rho_{\rm opt}
=
\rho_{s,c}\otimes
\tau_\beta^{\otimes(m-1)},
}
\]

in a collective-mode basis, where

\[
\rho_{s,c}
\propto
\exp[-(a+s)X_c^2-aP_c^2]
\]

is the same squeezed thermal optimizer as in the one-mode problem.

Thus the optimal strategy is:

> concentrate all nonequilibrium preparation resource into the single collective pointer mode actually used by the optical coupling; leave every orthogonal mode thermal.

There is no advantage, for minimizing the coupled quadrature noise, to spreading the same total free-energy budget across degenerate orthogonal pointer modes.

---

# 4. Tight multimode Gaussian QFI theorem

For coherent optical displacement encoding and arbitrary passive coupling into the detector mode manifold, let `tau` denote the total source displacement-transfer probability into the detector subspace.

Detector-local passive processing may rotate the transferred displacement into the optimally prepared collective mode without changing the degenerate apparatus Hamiltonian/free-energy budget.

For a Gaussian detector apparatus, the minimum achievable noise in that coupled collective direction is exactly `v_F(D_0,a)`. Therefore

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+2(1-\tau)v_F(D_0,a)}.
}
\]

With the passive coupling-action bound

\[
\tau\le\sin^2\Gamma,
\]

we obtain

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+2\cos^2\Gamma v_F(D_0,a)}.
}
\]

This is the same functional form as the single-mode theorem and is tight within the degenerate multimode Gaussian class.

**Status:** PROVED and saturable.

---

# 5. No mode-number factor

A naive resource count might suggest that `m` pointer modes improve sensitivity by an extensive factor. They do not under a **fixed total free-energy preparation budget** and a single normalized signal displacement direction.

The reason is geometric: only one collective quadrature is conjugate to the transferred displacement parameter. All orthogonal directions carry no local signal QFI unless additional independent signal modes/parameters are supplied.

Thus

\[
\boxed{
\text{single encoded displacement parameter}
+\text{fixed total }\Delta F
\Rightarrow
\text{no multiplicative }m\text{ advantage}.
}
\]

Parallel independent optical signal channels are a different resource problem and must be counted explicitly on the source side.

---

# 6. Unequal-frequency apparatus

If detector modes have unequal frequencies,

\[
H_D=\sum_j\frac{\hbar\omega_j}{2}(X_j^2+P_j^2),
\]

passive rotations no longer leave the Hamiltonian/thermal reference invariant. The exact scalar reduction above then fails.

For a specified normalized collective quadrature `X_c`, the Gibbs variational theorem still gives

\[
\boxed{
\operatorname{Var}(X_c)
\ge
\sup_{s>0}
\frac{
\ln[Z_0/Z_s(c)]-D_0
}{s},
}
\]

where

\[
Z_s(c)
=\operatorname{Tr}
\exp[-\beta H_D-sX_c^2].
\]

For a quadratic `H_D`, `Z_s(c)` is computable from the symplectic spectrum of the tilted quadratic form. The saturating state is again Gaussian:

\[
\rho_{s,c}\propto e^{-\beta H_D-sX_c^2}.
\]

A channel-independent theorem for unequal mode frequencies therefore requires the detector Hamiltonian/spectrum itself as a resource. It cannot in general be reduced to total free energy alone without losing physical information.

**Status:** general variational form PROVED; closed-form arbitrary-spectrum optimization OPEN.

---

# 7. Consequence for resource completeness

The preparation resource is not merely a scalar amount of free energy in complete abstraction. Its usefulness depends on the detector Hamiltonian that converts free energy into pointer sharpness.

A fully general quantum theorem should therefore treat

\[
\boxed{(H_D,T,\Delta F_D)}
\]

as the apparatus-preparation resource specification, rather than `Delta F_D` alone.

For a degenerate harmonic pointer manifold, this specification collapses to the compact pair `(omega_D, DeltaF)` and the exact frontier `v_F(beta DeltaF, beta hbar omega_D/2)`.

---

# 8. Next steps

1. Use the degenerate multimode theorem as the clean quantum photodetector pointer model in the first publication-level composite result.
2. Keep the unequal-frequency variational expression as the mathematically general extension.
3. Investigate whether non-Gaussian states can outperform the Gaussian SLD-QFI frontier at fixed `(H_D,T,DeltaF)`; the divergence-Fisher Stam route has been rejected for this purpose.
4. Formulate the optical-capture + coupling/preparation composition for coherent temporal modes without conflating interaction time with modulation bandwidth.
