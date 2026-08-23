# Roadmap — Autonomous Temporal Information Law

**Branch:** `agent/autonomous-temporal-information-law`

## Goal

Develop a rigorously scoped theory of physical resources for autonomous temporal information and close the strongest physical limitations identified by hostile review: dynamical implementation cost, exact-resonance robustness, and finite-dimensionality.

The PRX Quantum R3 manuscript is build-verified and **science-frozen** while the post-R3 theorem chain is audited. The older random-time Rev11 paper remains frozen on its parent branch.

**Current frontier: WP31.**

## Completed publication theorem arc through R3

The existing paper establishes:

1. fixed-mean-energy high-frequency local-Fisher no-go under unrestricted synthesis;
2. finite-radius spectral-survival law;
3. two-sided autonomous survival law;
4. one-sided and bilateral rank-boundary synthesis laws;
5. sharp autonomous action coefficients `hbar nu/4` and `hbar nu/2`;
6. arbitrary coherent-support mixed bridge with the piecewise `Psi_a` envelope;
7. multi-gap shared-Hessian action sum;
8. pure-boundary SLD-QFI action corollary;
9. spectator-curvature no-go separating selected temporal tangent geometry from arbitrary second-order Bures curvature.

R3 is standalone and should not be changed merely because stronger theory now exists.

## Completed post-R3 dynamical program

### WP21 — supplied implementation identity

For a smooth unitary dilation,

`Q partial_j^2 rho Q
 =2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)]`.

Hence positive endpoint action is exactly a state-weighted squared implementation coupling into empty sectors.

### WP22 — exact first-order implementation minimum

For a prescribed pure-boundary exact relational tangent,

`V_min=(1/4)Tr H_SLD`.

The minimizing generator can be chosen target-only and exactly total-energy conserving.

### WP23 — exact prescribed kernel-2-jet minimum

For prescribed feasible metric-contracted kernel curvature

`C>=C_min`,

finite-dimensional dilations obey and attain

`V_min=(1/2)Tr C`.

For a clean single-gap endpoint price,

`V_min=A_ex^(2)/(hbar nu)`.

The excess curvature is realized through an orthogonal ancilla flag sector, and the optimum is achievable within the exactly energy-conserving class.

### WP24 — independent envelope audit and classical prior art

The `Psi_a(e;p,q)` envelope was re-derived independently and brute-force validated. No defect was found.

Boundary nonregularity itself is established classical statistics and must not be presented as quantum novelty.

## Completed robustness program

### WP25 — approximate finite-radius Bohr gap

With commutator residual `R_nu=[H,A]-hbar nu A`, near-resonant tangent weight is charged by a slightly lower spectral tail and off-resonant weight by an explicit residual penalty.

### WP26 — hostile audit of WP23

The prescribed-2-jet lower bound, orthogonal-flag invisibility, exact curvature reproduction, and finite-dimensional energy-shell implementation survived a dedicated adversarial audit. The theorem prescribes the physical metric contraction of the kernel Hessian, not an arbitrary full mixed-second-derivative tensor.

### WP27 — approximate rank-boundary exchange

The rank-boundary Fisher **amplitude** splits into near-resonant endpoint terms plus explicit commutator-residual penalties. The autonomous action law approaches the exact `hbar nu/4` bilateral coefficient continuously as detuning vanishes.

Thus exact Bohr resonance is no longer an all-or-nothing hypothesis in either headline regime.

## Completed infinite-dimensional program

### WP28 — finite-radius survival

For trace-class `rho_0` on a separable Hilbert space and bounded relative tangent

`A=rho_0^(1/2)B rho_0^(1/2)`, `B` bounded,

the arbitrary-POVM/finite-copy finite-radius theorem extends exactly. The ambient Hamiltonian may have general semibounded spectral measure; the exact-gap statement is formulated by unitary covariance.

### WP29 — rank-boundary synthesis

If the right-relative support-to-kernel tangent operators are Hilbert--Schmidt,

`X rho_0^(-1/2), Y rho_0^(-1/2) in S_2`,

finite-rank support truncations and monotone positive quadratic forms yield the infinite-dimensional PSD-cone curvature law. The Minkowski information bound, clean autonomous coefficients, and SLD relation survive.

### WP30 — unrestricted infinite-dimensional dynamical cost

For prescribed positive trace-class kernel curvature `C`,

`inf_(smooth unitary dilations)V_impl=(1/2)Tr C`.

WP30 initially left exact energy conservation open for stationary states with unbounded occupied target-energy support because a **single coherent purification across all energy shells** created an apparent fourth-moment/domain obstruction.

### WP31 — exact infinite-dimensional energy-conserving cost

WP31 resolves the WP30 obstruction.

Because a stationary trace-class state is compact, its occupied support decomposes into countably many genuine target-energy eigenspaces. Instead of coherently superposing these energy shells, use a **classically mixed energy-labelled dilation**:

`rho_0=direct_sum_E rho_E`,

`Omega_0=direct_sum_E p_E |Omega_E><Omega_E|`.

Within each shell, build the WP23 optimal dilation. Since the prescribed tangent and kernel curvature commute with `H_T`, every shell implementation remains at the same target energy. The ancilla Hamiltonian can be chosen identically zero.

The global direct-sum generator may be unbounded, but finite state-weighted quadratic cost implies summable trace-norm majorants for every first and mixed second derivative. No fourth-moment condition is required.

Therefore

`boxed:
inf_(semibounded exactly energy-conserving smooth unitary dilations)
V_impl=(1/2)Tr C`

for arbitrary countable, even unbounded, occupied target-energy support.

For clean exact exchange,

`boxed: V_min=A_ex^(2)/(hbar nu)`.

This closes the dynamical implementation-cost and finite-dimensionality objections for the clean finite-information regime, subject to the explicit regularity assumptions of WP28/WP29.

## Current prior-art boundary

Do not claim novelty for:

- Bures/Uhlmann horizontal lifts or `QFI/4` purification speed;
- generic quantum speed limits/control norms;
- covariant or energy-conserving Stinespring dilation theory;
- infinite-dimensional QFI/Bures geometry;
- classical nonregular likelihood theory;
- standard operator inequalities and Schur/PSD-cone geometry;
- Page--Wootters or modes-of-asymmetry theory.

The narrow post-R3 candidate is:

> the frequency-resolved endpoint synthesis action equals the exact minimum state-weighted quadratic coupling cost required to realize a prescribed feasible rank-changing local kernel 2-jet under globally conserving relational dynamics, with controlled detuning and infinite-dimensional extensions.

Priority remains unverified.

## Current research gate

The theorem production phase should pause briefly for **WP31 audit and publication architecture**, not because there is no more theory to do but because the new results are now substantial enough to warrant a deliberate paper-level decision.

### Immediate work order

1. hostile-audit the stationary trace-class/pure-point-support lemma used by WP31;
2. hostile-audit the trace-norm dominated-convergence argument for mixed energy shells;
3. expand the WP31 validator to mixed/degenerate shell baselines and random excess curvature;
4. search specifically for state-specific prescribed-second-order-jet Stinespring implementation-cost theorems and equivalent energy-covariant constructions;
5. compare two publication architectures:
   - **R4 integration:** add only the strongest dynamical theorem + robustness/infinite-dimensional corollaries to the existing paper;
   - **follow-up paper:** keep R3 compact and make WP21–WP31 a separate dynamical/infinite-dimensional article;
6. only after that decision resume new theorem work.

### If theorem work resumes

Highest-value next targets are:

1. **noisy/CPTP implementation cost:** exact or bounded cost under nonunitary encoders/open-system channels;
2. **unbounded relative tangents:** closed quadratic-form replacement for the bounded/Hilbert--Schmidt assumptions;
3. **approximate-exchange dynamical cost:** combine WP27 residual penalties with the exact WP31 implementation variational problem;
4. Gaussian/CV specialization only after the abstract infinite-dimensional theorems are stabilized.

Do not spend effort on exhaustive formal edge-case bookkeeping unless a concrete referee or proof need demands it.

## Manuscript integrity

Every public-facing manuscript must be scientifically standalone. Never include personal repository URLs, repository names, usernames, development history, or a requirement that readers consult internal research files.

## Documentation discipline

Every material theorem, counterexample, proof repair, prior-art collision, validator, or publication-strategy change must update the dedicated note and the landing documents. The repository is authoritative.