# D2 hostile theorem-language audit

## Verdict

**PASS after one substantive implementation-class clarification and three presentation repairs.**

The central coefficient and the repaired energy-conserving construction are unchanged.

## Audited theorem

For a rank-deficient baseline `rho0`, pure-boundary derivatives `D_j`, and a prescribed positive trace-class physical-metric kernel Hessian contraction

`C = Q sum_j partial_j^2 rho(0) Q`

satisfying the PSD-cone feasibility condition

`C >= C_min`,

the manuscript claims

`V_min = (1/2) Tr C`.

Under strong stationarity/covariance of `rho0`, `D_j`, and `C` with respect to a semibounded target Hamiltonian, the same minimum is attainable by an exactly total-energy-conserving dilation with a semibounded ancilla Hamiltonian, including in separable infinite dimension with unbounded occupied target energies and with excess curvature in target-energy shells empty at baseline.

For the clean autonomous temporal endpoint price,

`A_ex^(2)=hbar nu V_min`.

## Issue found and repaired

### Infinite-dimensional implementation topology

The D1 text used the shorthand “smooth unitary dilation” together with `partial_j U(0)=-iK_j` everywhere. That is harmless for bounded generators but is too strong/ambiguous for the repaired infinite-dimensional energy-conserving construction, whose global generator is an unbounded direct sum.

D2 now defines the actual implementation class used by the proof:

- each `K_j` is self-adjoint on the baseline domain;
- the baseline has finite generator second moment `Tr(Omega0 K_j^2)<infinity`;
- the implemented reduced state family is trace-norm `C^2` at the origin;
- for bounded generators the usual operator expansion is used;
- for unbounded generators the kernel identity is obtained by state-weighted quadratic-form/spectral truncation, while the constructive direct-sum family is differentiated branchwise with trace-norm dominated convergence.

The energy-conserving theorem now states explicitly that the blockwise unitary is strongly continuous and that the claimed smoothness is statewise in trace norm on the finite-cost baseline.

This aligns the theorem statement with the actual WP32/WP33 proof and removes a functional-analysis ambiguity without weakening the result.

## Central lower bound audit

For a supplied implementation,

`Q partial_j^2 rho Q = 2 Tr_E[(Q tensor I) K_j Omega0 K_j (Q tensor I)]`.

The baseline is supported in `P tensor E`. Therefore

`Var_Omega0(K_j)`

splits into a nonnegative support-block variance plus the `P -> Q` transition norm. Summing gives

`V_impl >= (1/2) Tr C`.

No energy covariance is needed for this lower bound.

## Attainability audit

Write

`S=(C-C_min)/2 >=0`.

The horizontal tangent realization costs `(1/2)Tr C_min`. An orthogonal ancillary flag purifying `S`:

- contributes zero reduced first derivative;
- has zero horizontal cross term after partial trace;
- contributes exactly `2S` to the kernel Hessian contraction;
- adds exactly `Tr S` to the generator variance.

Hence the total cost is exactly

`(1/2)Tr C_min + Tr S = (1/2)Tr C`.

This is the nonminimal second-order step that is not contained in the generic first-order Bures/QFI horizontal-lift identity.

## Infinite-dimensional energy-conservation audit

The manuscript uses the repaired construction, not the superseded same-shell normalization shortcut.

Strong stationarity of a trace-class baseline implies that each nonzero eigenspace of the compact state is finite dimensional and invariant under the target time-translation group. Thus the occupied support has a countable joint state/energy eigenbasis even when the ambient Hamiltonian has continuous spectrum elsewhere.

Stationary positive trace-class excess curvature also has a countable energy-adapted eigenmode decomposition. These curvature modes may occur at target energies with zero baseline population.

For each such mode the proof:

1. splits one occupied baseline eigenstate into classically incoherent ancilla-labelled copies;
2. chooses nonnegative ancilla input/output energies `a_r,b_r` satisfying `E_*+a_r=F_r+b_r`;
3. places the flag transition and replicated horizontal transition inside one total-energy eigenspace;
4. takes the orthogonal direct sum over branches.

The branchwise generators are bounded; the global generator may be unbounded. Finite quadratic cost gives summable first-derivative majorants and, by Cauchy--Schwarz, summable mixed-second-derivative majorants. Dominated convergence therefore yields trace-norm `C^2` state evolution. No fourth-moment assumption is required.

The proof also allows branch weights to be selected so that the baseline ancilla has finite mean energy when desired.

## Scope locks that remain mandatory

The paper does **not** claim:

- a thermodynamic work minimum;
- a total protocol-energy minimum;
- a new generic Bures/Uhlmann or QFI purification theorem;
- a new generic channel-QFI/Kraus-gauge theorem;
- a new covariant Stinespring theorem;
- a solution for an arbitrary full tensor of mixed second derivatives;
- a generic noisy-CPTP encoder optimum;
- novelty of boundary nonregularity itself.

The optimized second-order datum is the **physical-metric contraction of the target kernel Hessian**.

## Presentation repairs

D2 also removes the three D1 build warnings identified in the first green build:

1. the overfull central-theorem assumption paragraph was shortened and split;
2. the long infinite-dimensional supplement section title was shortened;
3. the math-bearing `C^2` bookmark title was replaced by a text-only section title.

The D2 GitHub Actions build and visual render inspection show clean theorem pages and no targeted layout/bookmark regression.

## Publication implication

The theorem stack is stable enough for publication-style abstract/introduction work. Do not add another theorem merely to increase scope. Any next mathematical work should be triggered by a concrete referee/prior-art collision or by a real gap exposed during manuscript compression.
