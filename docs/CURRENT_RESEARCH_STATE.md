# Current Research State

**Date:** 2026-08-20

This is the first-stop handoff summary. The repository, not chat history, is authoritative.

Read in this order before continuing:

1. `AGENTS.md`
2. this file
3. `notes/RESEARCH_LOG_ROUND5.md`
4. `notes/WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
5. `notes/WP8_UV_REGULARIZATION_RESOURCE.md`
6. `notes/WP8_EXACT_GLOBAL_DUAL_CHARACTERIZATION.md`
7. `notes/WP8_PARITY_REWEIGHT_INTERPOLATION.md`
8. `notes/WP8_GAUSSIAN_PARITY_BIFURCATION.md`
9. `notes/WP8_SLD_STAM_GLOBAL_ENERGY_THEOREM.md`
10. `notes/WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md`
11. the older WP0–WP7 derivation notes as needed.

---

# 1. Project objective

Determine the physical resources necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical record with specified sensitivity and temporal bandwidth.

The project is now best viewed as a **resource-completeness / no-go + repair program**, not a search for one simple sensitivity-bandwidth-temperature product.

---

# 2. Information metric

Use source-normalized information transfer

\[
\eta_{\mathcal I}
=F_{\rm electrical}/F_{\rm incident}^{Q}.
\]

For coherent/Poisson weak photon-flux modulation,

\[
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
\]

Use a finite source task

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)},
\]

not an unweighted all-frequency integral.

---

# 3. Classical/Markov foundation — SOLVED core machinery

For stationary finite-state Markov jump detectors,

\[
S_I(\omega)=\mathbf1^T\mathcal J^{(2)}\pi
+2\operatorname{Re}[\mathbf1^T\mathcal J^{(1)}R(\omega)\mathcal J^{(1)}\pi],
\]

\[
\chi_{Iu}(\omega)=\mathbf1^T\mathcal J_u^{(1)}\pi
+\mathbf1^T\mathcal J_0^{(1)}R(\omega)W_u\pi.
\]

Strongest classical no-go:

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}.
}
\]

A reversible three-state family keeps all displayed stationary resources finite while an absolute microscopic rate scale diverges.

**Interpretation:** an absolute light–matter/internal coupling scale is a necessary resource.

Primary note: `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`.

---

# 4. Restricted internal thermokinetic completion

For a reversible optical gateway with minimum useful throughput `f_*`, EPR budget `Sigma`, activity budget `A`, and reverse optical rate `d`, define

\[
g(z)=(1-z^{-1})\ln z,
\qquad Z_*=g^{-1}(\Sigma/f_*).
\]

Then

\[
\pi_1\ge f_*/(dZ_*),
\qquad
\lambda_1\le\Lambda_*=(\mathcal A d/f_*)Z_*.
\]

For the proper single-event class,

\[
\eta_{\mathcal I}(\omega)
\le\eta_q\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2}.
\]

**Status:** PROVED under stated Markov event-transducer assumptions.

---

# 5. Passive finite-band electromagnetic capture — WP5

For coherent-state modulation through a passive frequency-preserving frontend,

\[
F_{\rm electrical}
\le
\int\frac{d\omega}{2\pi}\tau(\omega)\mathcal J_{\rm in}(\omega).
\]

Rigorous T-operator sum rules yield, for an electrically small reciprocal detector under nearly uniform illumination,

\[
\bar\eta_{\mathcal I}(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min\left(
\omega_p^2V,
(\omega_0+\Omega_s)^2\alpha_{\rm stat}
\right)
\right].
\]

Plane-wave sideband profile variation over radius `R` costs at most

\[
C_{\rm phase}=e^{2\Omega_sR/c}.
\]

**Status:** PROVED under passive reciprocal/fixed-channel assumptions.

---

# 6. Quantum finite-hypothesis theorem — WP7/QH

For two optical hypotheses and the same initial apparatus state, define

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

A trine POVM gives an exact counterexample showing that trace-distance contraction cannot simply be differentiated into an SLD-QFI contraction theorem.

---

# 7. Coherent-state QFI transfer and hidden apparatus resource

For passive bosonic source-to-pointer transfer probability `tau`, directional SLD Stam gives

\[
\boxed{
\frac1{J_C}
\ge
\frac\tau{J_A}
+\frac{1-\tau}{J_B}.
}
\]

For coherent optical input `J_A=2`, pointer QFI `J_D`,

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
}
\]

Cross-coupling action alone is insufficient: an arbitrarily pre-squeezed pointer can approach unit QFI transfer at arbitrarily weak nonzero coupling.

Thus **pre-existing apparatus metrological resource is independently necessary**.

---

# 8. Globally tight excitation-energy repair

For arbitrary pointer state with total mean excitation `N`, define

\[
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

Then

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N)}.
}
\]

This is globally tight under the passive-linear single-effective-mode model and is saturated by squeezed vacuum + beam splitter + homodyne.

The exact inverse resource trade is

\[
N_{\min}(q,\tau)
=
\frac{(q-\tau)^2}{4q(1-q)\tau(1-\tau)}
\]

for `0<tau<q`; otherwise `N_min=0`.

At weak coupling, `N_min~q/[4(1-q)Gamma^2]`.

Primary notes:
- `WP8_SLD_STAM_GLOBAL_ENERGY_THEOREM.md`
- `WP8_EXACT_ENERGY_ACTION_TRADEOFF.md`.

---

# 9. Finite-temperature free-energy frontier — major results

Let

\[
\vartheta=\beta\hbar\omega_D,
\qquad
D_0=\beta\Delta F=D(\rho_D\Vert\tau_\vartheta).
\]

## 9.1 Exact global variational characterization

The arbitrary-state frontier

\[
J_F^{\max}(D_0)
=\sup_{\rho:D(\rho\Vert\tau)\le D_0}J_X(\rho)
\]

has exact finite-dimensional dual representation

\[
\boxed{
J_F^{\max}(D_0)
=
\sup_{L=L^\dagger}
\inf_{\lambda>0}
\lambda\left[
D_0+
\ln\operatorname{Tr}
\exp\left(
\log\tau+\frac{2i[P,L]-L^2}{\lambda}
\right)
\right].
}
\]

Any interior optimizer obeys the coupled Gibbs/SLD/resource fixed-point equations.

Primary note: `WP8_EXACT_GLOBAL_DUAL_CHARACTERIZATION.md`.

## 9.2 Gaussian global optimality is false

At `vartheta=ln2`, the even-conditioned thermal state has

\[
D=\ln(3/2),
\qquad
J_X=14/3,
\]

while every Gaussian pointer at the same free-energy budget has `J_X<3.783`.

Recent literature now also explicitly studies hot parity-projected states for displacement sensing (Grochowski, arXiv:2606.13650, 2026). Do not claim parity protection itself as novel.

## 9.3 Exact pure-parity sector frontiers

For a state supported entirely in one parity sector,

\[
J_X=4\operatorname{Tr}(\rho P^2).
\]

The constrained optimum is an exact parity-conditioned quadratic Gibbs tilt. The even-sector branch satisfies

\[
J_e^{\rm opt}(D_0)
=\frac{8D_0}{\vartheta}+O(\ln D_0)
\]

and matches the global arbitrary-state upper bound to leading relative order at large free energy.

## 9.4 Simple parity reweighting already beats Gaussian states at low cost

Reweight only the even/odd probabilities while leaving conditional parity distributions thermal:

\[
\rho_p=p\tau_e+(1-p)\tau_o.
\]

The free-energy cost is exactly binary relative entropy, and the QFI is

\[
J_{\rm pr}(p)
=
\frac{2}{1-q^2}
\left[
(2p-1)^2(1+q^2)
+2\frac{[(1-p)-pq^2]^2}{(1-p)+pq^2}
\right].
\]

At `vartheta=ln2`, this simple family crosses the entire Gaussian frontier already at

\[
D_\times=0.01222932896\ldots.
\]

Primary note: `WP8_PARITY_REWEIGHT_INTERPOLATION.md`.

## 9.5 Restricted-family Gaussian/parity bifurcation

Allow both Gaussian squeezing and independent parity reweighting. In this exact two-parameter family the Gaussian branch loses local constrained stability at

\[
\mu_c=0.7441373808\ldots,
\]

\[
D_c=0.004810238075\ldots
\]

for `vartheta=ln2`.

This is a **restricted-family** bifurcation, not the exact global onset of non-Gaussianity.

Primary note: `WP8_GAUSSIAN_PARITY_BIFURCATION.md`.

---

# 10. Critical correction: unrestricted oscillator has a UV coherence instability

The earlier statement that Gaussian pointers are exactly optimal in some finite near-equilibrium neighborhood is **REJECTED**.

For a Gaussian candidate with effective thermal factor `q=e^{-mu}`, a symmetric high-Fock adjacent coherence has exact QFI-Hessian / relative-entropy-Hessian ratio

\[
\boxed{
R_n
=
\frac{8(1-q)}{\vartheta}
\left[
 n\frac{1+q+q^2}{(1+q)(1+q^2)}
+
\frac{1+q+3q^2+q^3}
{(1+q)^2(1+q^2)}
\right].
}
\]

Hence

\[
R_n\sim\alpha n\to\infty.
\]

By combining two separated adjacent coherences, the perturbation can simultaneously satisfy

\[
\delta\langle X\rangle
=\delta\langle P\rangle
=\delta\langle X^2\rangle
=0.
\]

Therefore for **every** `D_0>0`, sufficiently high-Fock centered non-Gaussian coherence improves QFI at the same free energy.

Correct interpretation:

\[
\boxed{
\text{Gaussian is regular/asymptotically perturbatively optimal as }D_0\to0,
\text{ but never exactly optimal for any }D_0>0
}
\]

in the unrestricted ideal harmonic oscillator.

The improvement is nonperturbatively small near equilibrium, approximately `exp[-C/sqrt(D_0)]`, so the Gaussian BKM expansion remains correct to ordinary algebraic orders.

Primary notes:
- `WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
- corrected `WP8_LOCAL_GAUSSIAN_OPTIMALITY.md`.

---

# 11. Energy moments do not repair the UV loophole

The instability perturbations are parity odd, while `H_D` and every function `f(H_D)` are parity even. Hence

\[
\boxed{
\operatorname{Tr}[\delta\rho f(H_D)]=0.
}
\]

Thus adding mean energy, energy variance, any finite collection of energy moments, or even the complete diagonal energy distribution does not control the UV coherence.

Moreover, ordinary energetic-coherence/time-translation QFI is not sufficient in an ideal harmonic ladder: adjacent level gaps are constant while displacement matrix elements grow as `sqrt(n)`, and

\[
\delta^2J_X/\delta^2F_N\sim
2\frac{1+q+q^2}{1+q^2}n\to\infty.
\]

A coherence-/support-/matrix-element-sensitive microscopic regularizer is required.

Candidate repairs:

- finite excitation cutoff / finite Hilbert dimension;
- microscopic saturation or anharmonicity;
- bounded signal-generator matrix elements;
- bounded-strength/bandwidth state-preparation channel;
- matter sum-rule constraint for the pointer degree of freedom.

Primary note: `WP8_UV_REGULARIZATION_RESOURCE.md`.

This is conceptually parallel to the classical rare-fast-state loophole: a resource can hide in a vanishing-weight sector.

---

# 12. Exact equilibrium thermal-pointer theorem

With no nonequilibrium preparation,

\[
J_\beta=2t_\beta,
\qquad
t_\beta=\tanh(\beta\hbar\omega_D/2).
\]

The passive-linear optimum is

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
=
\frac{\tau t_\beta}{1-\tau+\tau t_\beta}.
}
\]

With `tau<=sin^2 Gamma`, this is an exact restricted temperature–interaction-action–information theorem.

---

# 13. Finite-band quantum composition — WP9

For pointer QFI cap `J_D`, define

\[
f_J(\tau)=\frac{\tau J_D}{2(1-\tau)+\tau J_D}.
\]

Its curvature changes sign at `J_D=2`.

- `J_D>=2`: concave; uniform spectral coupling is optimal under scalar average/pointwise transfer constraints.
- `J_D<=2`: convex; bang-bang spectral concentration is optimal.

For pointwise target fraction `q`, the required optical transfer is

\[
\boxed{
\tau_q(J_D)=
\frac{2q}{J_D(1-q)+2q}.
}
\]

Thus both the microscopic interaction-action cap and WP5 finite-band EM capture resource must support `tau>=tau_q` throughout the task band.

Primary notes:
- `WP9_FINITE_BAND_QUANTUM_SPECTRAL_COMPOSITION.md`
- `WP9_POINTWISE_RESOURCE_COMPLETE_BOUND.md`.

---

# 14. Novelty constraints — current

Do **not** claim novelty for:

- generic detector sensitivity-speed/gain-bandwidth tradeoffs;
- general quantum photodetector frameworks;
- generic TUR/KUR/finite-frequency response bounds;
- squeezing/non-Gaussian-enhanced displacement sensing;
- parity-protected hot displacement sensing;
- thermodynamic usefulness of metrological coherence;
- energetic coherence as a resource distinct from work/free energy;
- LDOS/power-bandwidth bounds;
- T-operator sum rules;
- Maxwell-constrained communication capacity.

Important adjacent work includes:

- Young–Sarovar–Léonard photodetector theory;
- Hasegawa/Dechant/Liu-Gu/Vu et al. uncertainty/response bounds;
- Schwarzhans et al. detector thermodynamics;
- Shim et al. and Zhang–Monticone–Miller optical sum-rule bounds;
- Amaolo et al. Maxwell-constrained Shannon capacity;
- Narasimhachar et al. continuous-variable thermodynamic sensing resources;
- Marvian energetic-coherence/QFI cost;
- Grochowski & Filip non-Gaussian force-sensing states;
- Grochowski, `To Cool, or Not to Cool? Displacement Sensing with Hot Quantum States`, arXiv:2606.13650 (2026).

The surviving candidate contribution is the **photodetection-specific resource-completeness chain**:

1. stationary thermodynamic observables do not bound absolute Markov speed;
2. absolute microscopic coupling is necessary;
3. coupling alone does not bound coherent-state QFI transfer if the apparatus is preloaded;
4. free energy/energy population resources alone do not uniformly regularize an infinite-dimensional pointer because UV coherence can hide in vanishing-weight sectors;
5. once optical capture, coupling, apparatus preparation/support, and internal conversion resources are all specified, finite information-bandwidth bounds become possible.

Novelty remains provisional pending theorem-level audit.

---

# 15. Highest-priority next work

1. **UV-regularized quantum completion:** move WP8 to a finite-level / finite-excitation-support detector class and derive an explicit bound showing how the cutoff enters `J_D` and information bandwidth.
2. Test whether a microscopic matter sum rule can replace an ad hoc hard cutoff by bounding the high-level pointer matrix elements.
3. Preserve the unrestricted harmonic-oscillator UV result as a no-go theorem.
4. Continue the exact finite-budget free-energy/QFI dual analysis, but do not confuse the ideal oscillator frontier with a physically complete detector model.
5. Update `AGENTS.md` and research log after the next theorem.