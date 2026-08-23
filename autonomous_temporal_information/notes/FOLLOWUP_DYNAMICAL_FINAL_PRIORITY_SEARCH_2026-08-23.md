# Follow-up dynamical paper — final focused priority search, 2026-08-23

## Verdict

**No direct collision located. PROVISIONAL PASS TO MANUSCRIPT SKELETON.**

This is not priority certification. The search was designed specifically to find the WP32 theorem under terminology used by channel metrology, purification geometry, covariant dilation theory, second-order quantum-state geometry, and mathematical optimization rather than under the project's own terminology.

## Central claim searched

For a rank-changing local state model with prescribed feasible metric-contracted target-kernel Hessian `C`, determine

`inf V_impl`

over smooth unitary dilations, especially under exact energy conservation, where

`V_impl=sum_j Var(K_j)`.

WP32 gives

`inf V_impl=(1/2)Tr C`

and, for clean autonomous temporal exchange,

`V_min=A_ex/(hbar nu)`.

## Search families

Targeted searches included combinations of:

- `state-specific Stinespring second order`;
- `second-order quantum channel geometry Stinespring`;
- `prescribed density-matrix Hessian purification`;
- `fixed first derivative second derivative density matrix purification`;
- `state acceleration quantum Bures purification`;
- `minimal dilation acceleration`;
- `channel Fisher Kraus gauge minimization`;
- `channel fibre bundle quantum Fisher`;
- `second-order PSD cone quantum state`;
- `parabolic tangent density matrix`.

No exact prescribed-kernel-Hessian minimum-cost theorem was located.

## Closest first-order/channel literature

### Fujiwara and Imai, 2008

*A fibre bundle over manifolds of quantum channels and its application to quantum statistics*, J. Phys. A **41**, 255304 (2008), DOI `10.1088/1751-8113/41/25/255304`.

This introduces a fibre-bundle structure over quantum channels and expresses channel Fisher information through a geometric quantity on that bundle.

It is important prior art for Kraus/dilation gauge geometry, but it is a first-order channel-estimation result rather than a prescribed target-state second-order interpolation theorem.

### Channel-extension / purification minimization literature

Escher et al., Demkowicz-Dobrzanski et al., and related channel-extension methods express output/channel QFI through minimization over differentiable purifications or equivalent parameter-dependent Kraus gauges.

These results are close to WP22's first-order horizontal minimum and remove novelty from any generic statement that QFI is obtained by minimizing a dilation generator norm.

The follow-up must therefore foreground the independent second-order datum `C`, not the QFI tangent.

### QFI convex-roof variance

Toth--Petz and Yu establish QFI/4 as the minimum averaged variance over decompositions in the relevant unitary-estimation setting.

Again, this is first-order prior art and must be cited rather than rediscovered.

## Closest covariance/dilation literature

### Scutaru, 1979

*Some remarks on covariant completely positive linear maps on C*-algebras*, Reports on Mathematical Physics **16**, 79--87 (1979), DOI `10.1016/0034-4877(79)90040-5`.

Proves a Stinespring-type theorem for covariant completely positive maps.

### Faist, Berta, Brandao, 2021

*Thermodynamic Implementations of Quantum Processes*, Commun. Math. Phys. **384**, 1709--1750 (2021).

Their Lemma 7.2 explicitly states that a time-covariant process admits a Stinespring dilation with an energy-conserving unitary and environment Hamiltonian, citing Scutaru, Keyl--Werner, and Marvian.

Thus exact energy-conserving dilation existence is prior art. WP32's candidate distinction is the **state-specific exact minimum cost for fixed local second-order target data**.

## Closest rank-deficient/Bures literature

Carrasco and Spehner, arXiv:2606.06759 (2026), derive Bures geodesics joining non-faithful states and discuss quantum-speed-limit consequences.

This reinforces that non-faithful Bures geodesics and first-order minimal-speed geometry are not new here.

## Closest second-order cone mathematics

Bonnans, Cominetti, and Shapiro, SIAM J. Optim. **9**, 466--492 (1999), develop parabolic second-order tangent sets and second-order regularity, including semidefinite programming.

The PSD-cone feasibility condition `C>=C_min` is therefore mathematical infrastructure.

## What was not found

The search did not locate a source simultaneously giving:

1. a rank-deficient target state with specified first derivative `D`;
2. an independently prescribed feasible positive target-kernel Hessian contraction `C>=C_min`;
3. optimization over physical unitary/Stinespring dilations implementing **both** local data;
4. exact minimum state-weighted quadratic generator cost
   `V_min=(1/2)Tr C`;
5. constructive realization of arbitrary excess curvature through first-order-invisible ancilla flags;
6. exact total-energy conservation with semibounded ancilla for arbitrary stationary spectator curvature;
7. the autonomous spectral specialization
   `V_min=A_ex/(hbar nu)`.

Any future source matching this package would materially change the novelty assessment.

## Priority language lock

Allowed:

> Targeted searches did not locate an existing theorem matching the prescribed rank-changing kernel-2-jet minimum-cost identity under exact energy conservation.

Not allowed:

- “first theorem”;
- “unprecedented”;
- “unique”;
- “establishes priority”;
- “new theory of implementation cost.”

Priority remains **unverified, not certified** until publication-level literature review and peer review.

## Gate decision

The requirements in `FOLLOWUP_DYNAMICAL_SIGNIFICANCE_PRIORITY_GATE.md` are satisfied sufficiently to begin a **standalone manuscript skeleton**.

The manuscript must remain theorem-first and must make the prior-art separation visible on page 1:

- first-order purification/QFI minimization is known;
- covariant Stinespring dilation is known;
- PSD-cone second-order feasibility is known;
- the candidate contribution is the exact optimization when a nonminimal rank-changing target kernel Hessian is prescribed, together with the autonomous spectral endpoint interpretation.
