# Research Log — Round 5

**Date:** 2026-08-19

## Purpose

Durable checkpoint after WP6. This round starts the fully quantum UPRP extension and records an exact obstruction that prevents an invalid shortcut from trace-distance transfer to QFI transfer.

---

## 1. Quantum finite-hypothesis information-transfer theorem

Partition the full closed dilation into optical signal `F` and the complete detector/apparatus side `D`. The apparatus starts in the same state under both optical hypotheses:

\[
\rho_{FD}^{(a)}(0)=\rho_F^{(a)}\otimes\sigma_D.
\]

Define the nonlocal interaction seminorm

\[
g_{\rm int}(t)=\inf_{A_F,B_D}\|H(t)-A_F\otimes I-I\otimes B_D\|_\infty,
\]

and accumulated interaction action

\[
G(t)=\hbar^{-1}\int_0^t g_{\rm int}(s)ds.
\]

Using unitary conservation of global trace distance, the fact that local Hamiltonians cannot transfer hypothesis information across the partition, partial-trace contractivity, and the commutator trace-norm inequality gives

\[
\boxed{
D_{\rm elec}(t)/D_{\rm in}\le\min\{1,2G(t)\}.
}
\]

For equal priors this bounds the transferred Helstrom discrimination advantage. If `g_int<=E_int`, transfer fraction `r` requires

\[
\boxed{t\ge r\hbar/(2E_{\rm int}).}
\]

This theorem includes coherent pointer rotations and arbitrary non-Markovian internal detector dynamics provided those degrees of freedom are included in `D`.

**Status:** PROVED under the initially hypothesis-independent apparatus/product-state assumption and unitary dilation.

Primary derivation: `notes/WP7_QUANTUM_DISTINGUISHABILITY_TRANSFER.md`.

---

## 2. Trace-distance-to-QFI shortcut rejected

A generic trace-distance contraction coefficient cannot be used as the same upper bound on SLD/QFI contraction.

Exact counterexample: qubit trine POVM

\[
F_k=\frac13(I+\mathbf n_k\cdot\boldsymbol\sigma),
\quad \theta_k=0,2\pi/3,4\pi/3.
\]

The resulting QC channel has trace-distance contraction coefficient

\[
\boxed{\eta_{\rm Tr}=2/3.}
\]

For equatorial states

\[
\rho_{s,\phi}=\tfrac12[I+s(\cos\phi\sigma_x+\sin\phi\sigma_y)],
\]

phase encoding at `phi=0` gives

\[
F_{\rm in}=s^2,
\qquad
F_{\rm out}=\frac{s^2}{2-s},
\]

so

\[
\boxed{F_{\rm out}/F_{\rm in}=1/(2-s)\to1\quad(s\to1^-).}
\]

Therefore

\[
\boxed{\eta_{\rm SLD}=1\;\text{while}\;\eta_{\rm Tr}=2/3.}
\]

This explicitly falsifies any proposed universal step `QFI contraction <= trace contraction` or `<= trace contraction^2`.

**Status:** COUNTEREXAMPLE / PROVED analytically.

Literature consistency: Hiai–Ruskai contraction-coefficient theory already establishes that quantum trace and monotone-Riemannian contraction coefficients do not obey the simple classical ordering needed for such a shortcut. The trine calculation gives a compact project-specific unit test.

---

## 3. Quantum project split

The quantum extension must now be treated as two separate problems.

### QH — finite hypotheses / Helstrom information

Solved at the interaction-action level:

\[
\eta_H(t)=D_{\rm elec}/D_{\rm in}\le\min\{1,2G(t)\}.
\]

### QF — local parameter / SLD-QFI information

Open. Requires a separate argument.

The most physically relevant next source class is coherent-state displacement/sideband modulation, matching WP0/WP5, rather than an optimization over arbitrary quantum states near rank-deficient boundaries.

Candidate routes:

1. direct SLD/Bures contraction coefficient bound for the induced field-to-electrical QC channel;
2. prove a hypothesis-independent replacer/no-click component and use a strong data-processing inequality;
3. direct channel-QFI differential bound from `H_int`;
4. source regularity/finite-energy/mode restrictions if no state-independent bound exists.

---

## 4. Doeblin/replacer route status

Quantum Doeblin coefficients are relevant because replacer decompositions yield strong contraction bounds for many information measures. However, bounded small interaction action by itself does **not yet** imply a useful positive replacer fraction for an arbitrary unitary field-detector interaction. This must be proved or disproved before use.

A photodetector-specific event/no-click architecture may provide a natural hypothesis-independent branch and therefore a stronger route than a fully arbitrary quantum channel.

**Status:** OPEN.

---

## 5. Current overall hierarchy

Classical/semiclassical UPRP currently has:

1. source-normalized finite information task;
2. Markov thermodynamic no-go: stationary EPR/activity/detailed balance do not set absolute speed;
3. missing absolute microscopic coupling scale;
4. rigorous passive finite-band optical capture bound from T-operator sum rules;
5. plane-wave finite-footprint robustness;
6. restricted composite optical + thermokinetic theorem.

Quantum UPRP now adds:

7. finite-hypothesis interaction-action transfer theorem;
8. proof that local-QFI transfer is a genuinely distinct gate.

---

## 6. Immediate next action

Work on QF for coherent optical displacement states. First test whether an event/no-click detector channel has a rigorous theta-independent replacer component. If yes, derive its classical FI/QFI contraction exactly. If no, construct an explicit coherent-state counterexample and identify the missing output/source regularity resource.

Only after QF is resolved should the quantum result be composed with WP5/WP6 and evaluated for publication-level novelty.
