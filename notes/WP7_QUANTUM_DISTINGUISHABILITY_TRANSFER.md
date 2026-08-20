# WP7 — Quantum distinguishability-transfer theorem and QFI obstruction

**Date:** 2026-08-19

## Scope

This work package asks whether the classical/semiclassical UPRP resource theorem can be extended to arbitrary coherent quantum detector dynamics without quotienting out useful unitary pointer motion.

The first result is a fully quantum finite-hypothesis information-transfer bound. The second result is an exact obstruction showing why that trace-distance theorem cannot simply be differentiated into an SLD/QFI theorem.

---

# 1. Bipartite measurement model

Partition the full Hilbert space into

- `F`: optical signal degrees of freedom carrying the encoded hypothesis;
- `D`: the entire detector/apparatus side, including any internal environment, amplification chain, pointer, or ancilla that is initially independent of the optical hypothesis.

Let the two optical hypotheses be `rho_F^(0)` and `rho_F^(1)`. Let the detector start in the same state `sigma_D` under both hypotheses:

\[
\rho_{FD}^{(a)}(0)=\rho_F^{(a)}\otimes\sigma_D,
\qquad a\in\{0,1\}.
\]

The closed dilation evolves under a possibly time-dependent Hamiltonian `H(t)` on `F tensor D`.

Define the input trace distance

\[
D_{\rm in}
=\frac12\|\rho_F^{(0)}-\rho_F^{(1)}\|_1.
\]

After the interaction, define the reduced detector states

\[
\rho_D^{(a)}(t)=\operatorname{Tr}_F\rho_{FD}^{(a)}(t),
\]

and

\[
D_D(t)=\frac12\|\rho_D^{(0)}(t)-\rho_D^{(1)}(t)\|_1.
\]

---

# 2. Decomposition-invariant interaction resource

Purely field-local and detector-local Hamiltonians cannot transfer hypothesis information across the `F|D` partition. Therefore define the instantaneous nonlocal interaction seminorm

\[
\boxed{
 g_{\rm int}(t)
 =
 \inf_{A_F,B_D}
 \left\|
 H(t)-A_F\otimes I_D-I_F\otimes B_D
 \right\|_\infty .
}
\]

The infimum removes arbitrary local Hamiltonian pieces. A global scalar is already absorbed into either local term.

Define the dimensionless accumulated interaction action

\[
\boxed{
G(t)=\frac1\hbar\int_0^t g_{\rm int}(s)\,ds.
}
\]

This resource is not a restatement of detector bandwidth. It is an operator-level strength of the cross-partition coupling.

---

# 3. Quantum distinguishability-transfer theorem

Let

\[
\Delta(t)=\rho_{FD}^{(0)}(t)-\rho_{FD}^{(1)}(t).
\]

At all times the global unitary evolution preserves

\[
\|\Delta(t)\|_1=\|\Delta(0)\|_1=2D_{\rm in}.
\]

For arbitrary local `A_F(t),B_D(t)`, define

\[
K(t)=H(t)-A_F\otimes I-I\otimes B_D.
\]

The field-local commutator vanishes after partial trace. The detector-local term generates the same local unitary on both reduced detector states and therefore cannot increase their trace distance. In the corresponding detector-local frame,

\[
\frac{d}{dt}\Delta_D(t)
=-\frac{i}{\hbar}\operatorname{Tr}_F[K(t),\Delta(t)].
\]

Using trace-norm contractivity under partial trace and

\[
\|[K,X]\|_1\le2\|K\|_\infty\|X\|_1,
\]

we obtain

\[
\frac{d^+}{dt}D_D(t)
\le
\frac{2}{\hbar}\|K(t)\|_\infty D_{\rm in}.
\]

Taking the infimum over local decompositions gives

\[
\frac{d^+}{dt}D_D(t)
\le
\frac{2}{\hbar}g_{\rm int}(t)D_{\rm in}.
\]

Since `D_D(0)=0`, integration gives

\[
\boxed{
D_D(t)
\le
2G(t)D_{\rm in}.
}
\]

Ordinary data processing also gives `D_D(t)<=D_in`. Therefore

\[
\boxed{
\frac{D_D(t)}{D_{\rm in}}
\le
\alpha_H(t)
\equiv
\min\{1,2G(t)\}.
}
\]

**Status: PROVED** under the stated initially product/same-apparatus-state assumption and a unitary dilation of the full detector side.

---

# 4. Electrical-readout corollary

Any electrical record is generated from the detector side by a measurement / quantum-to-classical channel `M`. Trace distance is contractive, so if `p_0(y|t),p_1(y|t)` are the resulting classical output distributions,

\[
D_{\rm elec}(t)
\equiv
\frac12\sum_y|p_0(y|t)-p_1(y|t)|
\le D_D(t).
\]

Hence

\[
\boxed{
\frac{D_{\rm elec}(t)}{D_{\rm in}}
\le
\min\{1,2G(t)\}.
}
\]

For equal priors, the optimal binary discrimination success probabilities satisfy

\[
P_{\rm succ}^{\rm opt}=\frac12(1+D).
\]

Thus the useful electrical discrimination advantage obeys

\[
\boxed{
P_{\rm succ,elec}^{\rm opt}(t)-\frac12
\le
\alpha_H(t)
\left(P_{\rm succ,in}^{\rm opt}-\frac12\right).
}
\]

This is a direct quantum resource-to-information-transfer speed limit. It includes coherent pointer rotations, arbitrary non-Markovian internal detector dynamics, and arbitrary downstream measurements because all detector-side dynamics are included on the `D` side of the partition.

---

# 5. Constant-coupling corollary

If

\[
g_{\rm int}(t)\le E_{\rm int},
\]

then

\[
D_{\rm elec}(t)/D_{\rm in}
\le
\min\left\{1,\frac{2E_{\rm int}t}{\hbar}\right\}.
\]

To transfer a fraction `r` of the input binary distinguishability into the electrical record, a necessary condition is

\[
\boxed{
t\ge\frac{r\hbar}{2E_{\rm int}}.
}
\]

This is not claimed tight. The factor-of-two/operator-norm commutator estimate is a robust universal ceiling, not an optimized speed limit.

---

# 6. Why this does NOT automatically imply a QFI theorem

The project information metric for infinitesimal modulation is SLD quantum Fisher information. It is tempting to differentiate the trace-distance theorem and infer a QFI contraction bound. That step is invalid in general.

Hiai and Ruskai, *Contraction coefficients for noisy quantum channels*, J. Math. Phys. 57 (2016), show that contraction coefficients for trace distance and monotone Riemannian metrics are genuinely different in the quantum case. The SLD/QFI metric is the minimal/Bures metric corresponding to

\[
\kappa_{\min}(x)=\frac{2}{1+x}.
\]

Generic trace-distance contraction does not furnish the required upper bound on the SLD contraction coefficient.

The obstruction can be made completely explicit with a quantum-to-classical channel.

---

# 7. Exact trine-POVM counterexample

Consider the rank-one trine POVM on a qubit,

\[
F_k=\frac13(I+\mathbf n_k\cdot\boldsymbol\sigma),
\qquad
\theta_k=0,\frac{2\pi}{3},\frac{4\pi}{3},
\]

where

\[
\mathbf n_k=(\cos\theta_k,\sin\theta_k,0).
\]

It defines a quantum-to-classical channel

\[
\Phi(\rho)=\sum_k\operatorname{Tr}(F_k\rho)|k\rangle\langle k|.
\]

## 7.1 Trace-distance contraction

For a traceless qubit Hermitian operator `A=a dot sigma`,

\[
\|A\|_1=2|\mathbf a|,
\]

and

\[
\Phi(A)_k=\frac23\mathbf n_k\cdot\mathbf a.
\]

Therefore

\[
\frac{\|\Phi(A)\|_1}{\|A\|_1}
=
\frac13\sum_{k=1}^3|\mathbf n_k\cdot\hat{\mathbf a}|.
\]

The maximum occurs when `a` is aligned with one trine arm, giving projections `1,-1/2,-1/2`. Hence

\[
\boxed{
\eta_{\rm Tr}(\Phi)=\frac23.
}
\]

## 7.2 Local SLD/QFI contraction

Take the equatorial state family

\[
\rho_{s,\phi}
=\frac12\left[I+s(\cos\phi\,\sigma_x+\sin\phi\,\sigma_y)\right],
\qquad 0<s<1.
\]

For the phase parameter `phi`, the input SLD QFI is

\[
\boxed{F_{\rm in}=s^2.}
\]

The trine output probabilities are

\[
p_k(\phi)=\frac13[1+s\cos(\phi-\theta_k)].
\]

At `phi=0`,

\[
\partial_\phi p_1=0,
\]

and the other two outcomes have equal/opposite derivatives. Direct substitution gives

\[
F_{\rm out}
=\frac{s^2}{2-s}.
\]

Therefore

\[
\boxed{
\frac{F_{\rm out}}{F_{\rm in}}
=\frac{1}{2-s}.
}
\]

As the input approaches a pure equatorial state,

\[
\boxed{
\lim_{s\to1^-}
\frac{F_{\rm out}}{F_{\rm in}}
=1.
}
\]

Thus

\[
\boxed{
\eta_{\rm SLD}(\Phi)=1
\quad\text{while}\quad
\eta_{\rm Tr}(\Phi)=\frac23.
}
\]

This is an exact analytic counterexample to any claim that a trace-distance contraction coefficient by itself upper-bounds SLD/QFI contraction by the same coefficient (or by its square).

**Status: PROVED.**

---

# 8. Consequence for UPRP

The quantum project must now be split into two logically distinct branches.

## Branch QH — finite-hypothesis / Helstrom information

The interaction-action theorem is already rigorous:

\[
\boxed{
\eta_H(t)
\equiv
D_{\rm elec}/D_{\rm in}
\le
\min\{1,2G(t)\}.
}
\]

This is architecture-independent once the `F|D` partition and initial-independence condition are specified.

## Branch QF — infinitesimal/QFI information

A separate resource inequality is required. It cannot be obtained merely by differentiating the trace-distance result.

Candidate routes:

1. bound the **SLD/Bures contraction coefficient** of the induced field-to-electrical QC channel directly from interaction resources;
2. establish a quantum Doeblin/replacer component generated by finite interaction action, then use a strong data-processing inequality for Fisher information;
3. impose a physically justified source regularity condition (e.g. bounded away from rank deficiency / finite energy and mode constraints) and derive a QFI bound under that restricted class;
4. work directly with the optical coherent-state displacement family, where the source family is fixed and physically regular, instead of maximizing over arbitrary quantum states;
5. derive a channel-QFI bound from the interaction Hamiltonian without passing through trace distance.

The trine counterexample shows that a fully state-independent SLD contraction theorem is more delicate than the finite-hypothesis theorem, especially near rank-deficient input families.

---

# 9. Relation to existing literature / novelty caution

Relevant prior work includes:

- Hiai & Ruskai, *Contraction coefficients for noisy quantum channels*, J. Math. Phys. 57, 015211 (2016), DOI `10.1063/1.4936215`: contraction coefficients for trace distance, monotone metrics, Bures/SLD geometry, and QC/CQ channels.
- Matsushita & Hofmann, *Uncertainty limits of the information exchange between a quantum system and an external meter*, Phys. Rev. A 104, 012219 (2021): measurement sensitivity expressed through distinguishability of meter states and quantum coherence/backaction.
- Bravyi, *Upper bounds on entangling rates of bipartite Hamiltonians*, Phys. Rev. A 76, 052319 (2007): interaction-norm bounds on entanglement generation.
- modern quantum speed-limit and channel-contraction literature, including quantum Doeblin coefficients (2026).

The generic ideas “interaction strength limits information transfer,” “meter distinguishability depends on coupling,” and “quantum channels contract distinguishability” are therefore not novel.

The possible UPRP contribution is the **photodetection-specific composition** with the already derived finite-band optical capture and thermokinetic results, plus the explicit separation between finite-hypothesis and local-QFI information-transfer limits.

No publication-level novelty claim is made for the interaction-action theorem until a dedicated citation-chain audit is complete.

---

# 10. Next action

Highest-priority quantum task:

1. specialize the field input to physically relevant coherent-state sideband/displacement families used in WP0/WP5;
2. derive the induced detector/electrical QFI directly under bounded `g_int` rather than using trace distance;
3. test whether a Doeblin/replacer decomposition or channel-QFI bound gives `F_out/F_in <= f(G)` with `f(G)->0` as `G->0`;
4. if no state-independent bound exists, identify the minimal source regularity/resource needed;
5. only then compose the result with the WP5 electromagnetic finite-band theorem and WP3/WP4 thermokinetic theorem.
