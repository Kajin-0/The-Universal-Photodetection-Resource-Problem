# Research Log — Round 5

**Date:** 2026-08-20

This checkpoint records the fully quantum UPRP extension through WP9. It is intentionally redundant with dedicated notes so a replacement agent can recover the scientific state without chat history.

---

## 1. Quantum finite-hypothesis information-transfer theorem

Partition the closed dilation into optical signal `F` and complete detector/apparatus side `D`, initially

\[
\rho_{FD}^{(a)}(0)=\rho_F^{(a)}\otimes\sigma_D.
\]

Define

\[
g_{\rm int}(t)=\inf_{A_F,B_D}\|H-A_F\otimes I-I\otimes B_D\|_\infty,
\]

\[
G(t)=\hbar^{-1}\int_0^t g_{\rm int}(s)ds.
\]

Then

\[
\boxed{
D_{\rm elec}(t)/D_{\rm in}\le\min\{1,2G(t)\}.
}
\]

For equal priors this bounds the transferred Helstrom discrimination advantage. If `g_int<=E_int`, transfer fraction `r` requires `t>=r hbar/(2E_int)`.

**Status:** PROVED under the initially hypothesis-independent apparatus/product-state and unitary-dilation assumptions.

Primary note: `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`.

---

## 2. Trace-distance-to-QFI shortcut rejected

A trine qubit POVM gives an exact QC channel with trace-distance contraction `2/3` but SLD/QFI contraction coefficient `1`. For near-pure equatorial phase families,

\[
F_{\rm out}/F_{\rm in}=1/(2-s)\to1.
\]

Therefore no universal step equating or ordering QFI contraction by trace-distance contraction is valid.

**Status:** COUNTEREXAMPLE / PROVED.

The quantum project splits into:

- QH: finite hypotheses / Helstrom information;
- QF: local parameter / SLD QFI.

---

## 3. Passive-linear coherent-state QFI interaction theorem

For passive number-conserving bosonic coupling with single-particle cross block `V(t)`, define

\[
\Gamma(t)=\int_0^t\|V(s)\|_2ds.
\]

The source-to-detector transfer probability obeys

\[
\tau\le\sin^2(\min\{\Gamma,\pi/2\}).
\]

A coherent/vacuum detector pointer therefore gives

\[
F_{\rm elec}/F_{\rm in}\le\sin^2\Gamma.
\]

But this is not universal because a pre-squeezed detector pointer can transfer nearly all QFI at arbitrarily weak nonzero coupling.

Thus **initial apparatus metrological resource** is an additional necessary quantum resource.

---

## 4. Directional SLD-Stam theorem and globally tight energy repair

For one output of a passive beam splitter,

\[
\rho_C=\mathcal B_\lambda(\rho_A\otimes\rho_B),
\]

directional SLD displacement QFI obeys

\[
\boxed{
\frac1{J_C}
\ge
\frac\lambda{J_A}
+\frac{1-\lambda}{J_B}.
}
\]

This follows directly from SLD-QFI data processing, product additivity, and displacement covariance. No divergence-Fisher metric substitution is used.

For coherent input (`J_A=2`) and arbitrary detector pointer with total excitation `N`, define

\[
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

The energy theorem gives

\[
J_B\le2/\xi(N),
\]

and hence

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N)}.
}
\]

With `tau<=sin^2 Gamma`,

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\,\xi(N)}.
}
\]

A squeezed-vacuum pointer, beam splitter, and homodyne saturate the bound.

**Status:** PROVED and globally tight under the passive-linear single-collective-mode model.

Primary note: `notes/WP8_SLD_STAM_GLOBAL_ENERGY_THEOREM.md`.

---

## 5. Gaussian free-energy closure is exact only inside the Gaussian class

For harmonic thermal reference and free-energy budget `D0=beta DeltaF`, the Gibbs variational principle gives an exact Gaussian quadrature-noise frontier with a squeezed-thermal optimizer.

This yields a tight Gaussian QFI-transfer theorem and extends exactly to equal-frequency multimode Gaussian pointer manifolds by concentrating resource in one collective mode.

However, Gaussian global optimality is false.

Primary notes:
- `notes/WP8_FREE_ENERGY_GAUSSIAN_CLOSURE.md`
- `notes/WP8_MULTIMODE_FREE_ENERGY_EXTENSION.md`

---

## 6. Exact analytic non-Gaussian parity counterexample

At

\[
\beta\hbar\omega=\ln2,
\]

condition the thermal state on even Fock parity:

\[
\rho_e
=\sum_{k\ge0}\frac34 4^{-k}|2k\rangle\langle2k|.
\]

Exactly,

\[
D(\rho_e\Vert\tau)=\ln(3/2),
\qquad
\langle N\rangle=2/3,
\qquad
J_X(\rho_e)=14/3.
\]

The Gaussian free-energy theorem evaluated at one explicit admissible dual point proves every Gaussian pointer at the same budget has

\[
J_X^{\rm Gaussian}<3.783.
\]

Thus Gaussian free-energy optimality is strictly false.

Mechanism: `P` flips parity. Entropy stored within one parity sector does not incur the usual mixed-state QFI penalty.

**Status:** PROVED analytic counterexample.

Primary note: `notes/WP8_NON_GAUSSIAN_PARITY_COUNTEREXAMPLE.md`.

---

## 7. Exact even-parity sector frontier

For any state supported entirely in even parity,

\[
\boxed{J_X(\rho)=4\operatorname{Tr}(\rho P^2).}
\]

The free-energy constrained QFI problem therefore becomes a linear relative-entropy optimization. Its exact optimizer is

\[
\rho_s
\propto
\Pi_e\exp[\log\tau+sP^2]\Pi_e.
\]

Let

\[
\vartheta=\beta\hbar\omega,
\qquad
\mu=\sqrt{\vartheta(\vartheta-2s)}.
\]

Then

\[
Z_e(s)
=(1-e^{-\vartheta})
\frac{e^{(\vartheta-\mu)/2}}
{1-e^{-2\mu}},
\]

\[
m(s)=\frac{\vartheta}{\mu}
\left[\frac12+\frac{2}{e^{2\mu}-1}\right],
\]

\[
J_e(s)=4m(s),
\qquad
D_e(s)=s m(s)-\ln Z_e(s).
\]

This is the exact optimum over all even-supported states.

At large free energy,

\[
\boxed{
J_e^{\rm opt}(D_0)
=\frac{8D_0}{\vartheta}+O(\ln D_0).
}
\]

**Status:** PROVED exact parity-sector frontier.

Primary note: `notes/WP8_EXACT_PARITY_SECTOR_FRONTIER.md`.

---

## 8. Global arbitrary-state free-energy upper bound

For any one-mode state of mean excitation `N`,

\[
S(\rho)\le g(N).
\]

Hence

\[
D_0\ge
\vartheta N-g(N)-\ln(1-e^{-\vartheta}).
\]

Let `N_+(D0,vartheta)` be the largest root of equality. Then `N<=N_+`, so

\[
\boxed{
J_F^{\max}(D_0,\vartheta)
\le\frac2{\xi(N_+)}.
}
\]

Therefore arbitrary pointer states satisfy

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N_+)}.
}
\]

Finite nonequilibrium free energy is therefore sufficient to close the hidden apparatus-resource loophole even though the exact finite-budget frontier is not known.

At large `D0`,

\[
J_F^{\max}
\le\frac{8D_0}{\vartheta}+O(\ln D_0).
\]

Since the exact even-sector construction has the same leading form, it is asymptotically globally optimal to leading relative order.

**Status:** PROVED global upper bound and asymptotic global optimality.

Primary note: `notes/WP8_GLOBAL_FREE_ENERGY_UPPER_BOUND.md`.

---

## 9. Gaussian states are locally optimal near equilibrium

At the faithful thermal state,

\[
L_\beta=2tX,
\qquad t=\tanh(\vartheta/2).
\]

The QFI first variation is generated by

\[
K_\beta=4t-4t^2X^2.
\]

Because relative entropy has the BKM metric as its Hessian, the steepest QFI-ascent direction under an infinitesimal free-energy budget is

\[
\rho_\lambda\propto\exp[\log\tau+\lambda K_\beta],
\]

which is Gaussian.

Thus

\[
J_F^{\max}(D_0)
=J_\beta+
\sqrt{2\mathcal V_{\rm KM}(K_\beta)D_0}
+O(D_0),
\]

and squeezed-thermal Gaussian states attain the leading expansion.

Combined with the finite-budget parity counterexample, this proves a **Gaussian-to-non-Gaussian resource crossover** for the explicit temperature example.

**Status:** PROVED asymptotic local Gaussian optimality.

Primary note: `notes/WP8_LOCAL_GAUSSIAN_OPTIMALITY.md`.

---

## 10. Exact equilibrium thermal-pointer theorem

For an apparatus with no nonequilibrium preparation resource,

\[
J_\beta=2\tanh(\beta\hbar\omega_D/2).
\]

Under passive transfer probability `tau`, the exact optimum is

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
=
\frac{\tau t_\beta}{1-\tau+\tau t_\beta},
\qquad
t_\beta=\tanh(\beta\hbar\omega_D/2).
}
\]

With `tau<=sin^2 Gamma`,

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{t_\beta\sin^2\Gamma}
{\cos^2\Gamma+t_\beta\sin^2\Gamma}.
}
\]

**Status:** PROVED and saturable in the passive-linear single-effective-mode model.

Primary note: `notes/WP8_EXACT_THERMAL_POINTER_THEOREM.md`.

---

## 11. WP9 finite-band spectral composition

Let WP5 supply

\[
\bar\tau\le B_{\rm opt}(\Omega_s)
\]

and WP7 supply the pointwise cap

\[
\tau(\omega)\le\tau_{\max}=\sin^2\Gamma_{\max}.
\]

For a frequency-independent pointer-QFI cap `J_D`, define

\[
f_J(\tau)=\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
\]

Its curvature changes sign at `J_D=2`:

- `J_D<2`: convex; optimal spectral allocation is bang-bang/concentrated;
- `J_D>2`: concave; optimal spectral allocation is uniform;
- `J_D=2`: linear.

Exact flat-band compositions:

For `J_D>=2`,

\[
\boxed{
\bar\eta\le
f_J(\min\{B_{\rm opt},\tau_{\max}\}).
}
\]

For `J_D<=2`,

\[
\boxed{
\bar\eta\le
f_J(\tau_{\max})
\min\{1,B_{\rm opt}/\tau_{\max}\}.
}
\]

For an equilibrium thermal pointer this gives an explicit finite-band electromagnetic + temperature + interaction-action ceiling.

**Status:** PROVED exact scalar spectral-resource optimization under the passive-linear narrow-band assumptions.

Primary note: `notes/WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md`.

---

## 12. Literature/novelty corrections

Generic non-Gaussian displacement-sensing advantage and sparse/`N`-spaced Fock-support probes are already known. In particular, Grochowski & Filip, *Optimal Phase-Insensitive Force Sensing with Non-Gaussian States*, PRL 135, 230802 (2025), finds `N`-spaced states approaching force-sensing bounds.

Therefore do **not** claim novelty for parity/sparse Fock support as a generic metrological idea.

The potentially distinct contribution is the **finite-temperature nonequilibrium-free-energy resource frontier for a detector apparatus** and its integration into the photodetection resource-completeness/no-go/completion structure.

Also relevant: Marvian, PRL 129, 190502 (2022), gives an operational thermodynamic interpretation of QFI as a coherence-preparation cost for time-translation asymmetry. It does not immediately solve directional phase-space displacement QFI relative to a harmonic thermal reference, but it is a mandatory comparison.

---

## 13. Current sharp open problem

The exact arbitrary-state finite-budget frontier

\[
J_F^{\max}(D_0,\vartheta)
=\sup_{\rho:D(\rho\Vert\tau_\vartheta)\le D_0}J_X(\rho)
\]

remains unknown at intermediate `D0`.

What is known rigorously:

- small `D0`: Gaussian globally optimal to leading order;
- finite `D0`: explicit non-Gaussian parity state can beat every Gaussian;
- large `D0`: exact even-parity exponential family is asymptotically globally optimal;
- all `D0`: rigorous arbitrary-state upper bound via maximum entropy + energy-QFI theorem.

The next analytic target is the finite-budget **two-parity interpolation**, or an exact dual variational characterization tight enough to close the remaining gap.
