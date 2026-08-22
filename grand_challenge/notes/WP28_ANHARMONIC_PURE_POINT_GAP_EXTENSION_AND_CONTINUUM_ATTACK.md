# WP28 — Anharmonic pure-point gap extension and hostile audit of continuum/purification objections

**Date:** 2026-08-22

**Status:** core derivation PASS at theorem level; numerical validator pending/companion. This note is a hostile response to a new adversarial critique of Rev10. It does not weaken the existing periodic theorem. It identifies one genuine generalization: the modewise Fisher-tail mechanism does not require a globally equally spaced Hamiltonian.

## 1. Adversarial claims under review

The new critique raises four claims:

1. the factorization `A_k=rho0^(1/2) V_k rho0^(1/2)` allegedly collapses for anharmonic or continuous spectra because the manuscript starts from an equally spaced semibounded ladder;
2. the controlled periodic-to-continuum theorem allegedly requires smooth spectral measures and therefore fails for singular-continuous components;
3. zero-population sector completion in the Herglotz proof allegedly introduces unphysical "ghost" states that create artificial cross-frequency constraints;
4. the theory is local in the perturbation parameters and therefore does not by itself control global finite-amplitude estimation risk.

Preliminary verdict:

- (1) identifies a real presentation/scope vulnerability but overstates the algebraic necessity of a global ladder. A fixed-Bohr-gap extension to arbitrary semibounded pure-point generators exists.
- (2) is mathematically incorrect as stated. The lower-bin tail convergence requires no density or smoothness and covers arbitrary finite Borel measures, including atomic and singular-continuous parts. The real noncompact issue is the absence of a normalized uniform time law on `R`, which Rev10 already acknowledges.
- (3) is not a loophole. Null sectors are annihilated by `rho0^(1/2)` and have zero posterior support almost everywhere; completion changes no score or Fisher information.
- (4) is correct but already explicit in Rev10. A separate finite-amplitude trace-distance extension may be possible, but it is not needed to defend the stated Fisher theorem.

---

# 2. Fixed-Hamiltonian long-window experiment

Let `H` be a semibounded Hamiltonian with countable pure-point spectrum on the participating subspace. Write distinct participating energy values as

`E_alpha = E_* + hbar omega_alpha`, `omega_alpha >= 0`,

with no commensurability assumption.

After purification, write

`|Psi> = sum_alpha sqrt(q_alpha) |phi_alpha>`,

where `|phi_alpha>` lies in the total-generator eigenspace at `E_alpha`, `q_alpha>=0`, and `sum q_alpha=1`.

Fix an arbitrary modulation angular frequency `nu>0`. For integer `M>=1`, choose

`T_M = 2 pi M / nu`

and the normalized real-time density on `[0,T_M]`

`p_(eps,M)(t) = T_M^(-1) [1 + eps_c cos(nu t) + eps_s sin(nu t)]`.

For `sqrt(eps_c^2+eps_s^2)<=1` this is nonnegative, and because `T_M` is an integer number of modulation periods, its integral is exactly one.

Define

`rho_(eps,M) = int_0^(T_M) p_(eps,M)(t) U_t |Psi><Psi| U_t^dagger dt`.

The latent input Fisher block at the origin is exactly `(1/2) I_2` for every `M`.

For an energy difference

`Delta_(beta alpha) = omega_beta - omega_alpha`,

the baseline matrix coefficient contains

`(1/T_M) int_0^(T_M) exp[-i Delta t] dt`,

which tends to zero unless `Delta=0`. The cosine/sine tangent coefficients select `Delta=+/-nu`. Thus the long-window limiting local experiment has

`rho0 = sum_alpha q_alpha |phi_alpha><phi_alpha|`

and complex positive-gap tangent

`A_nu = sum_(alpha: omega_alpha+nu in spectrum) sqrt(q_alpha q_(alpha+nu)) |phi_(alpha+nu)><phi_alpha|`,

with zero terms omitted.

For a finite-dimensional spectrum the convergence is immediate in every matrix norm. For a countable pure-point spectrum, trace-norm convergence follows by finite-energy-sector truncation: the random-unitary averages and signed tangent averages are trace-norm contractions, while the truncated finite-dimensional problem converges termwise. Therefore the limiting statistical experiment is well defined for the purified state.

This is an ordinary-real-time long-window limit on one fixed Hamiltonian. It does not require `U_(T_M)` to be periodic or the energy spectrum to be commensurate.

---

# 3. Arbitrary-Bohr-gap factorization theorem

For fixed `nu>0`, define

`V_nu = sum_(alpha: q_alpha q_(alpha+nu)>0) |phi_(alpha+nu)><phi_alpha|`.

Because `omega -> omega+nu` is one-to-one, the domain and range vectors are orthonormal sets; hence `V_nu` is a partial isometry.

Then exactly

`A_nu = rho0^(1/2) V_nu rho0^(1/2)`.

Define paired masses

`D_nu = Tr(rho0 V_nu^dagger V_nu)`,

`U_nu = Tr(rho0 V_nu V_nu^dagger)`.

Every range energy satisfies `omega>=nu`, because its paired lower energy is nonnegative. Hence

`U_nu <= S(nu) := sum_(alpha: omega_alpha>=nu) q_alpha`.

The Hilbert--Schmidt Cauchy--Schwarz proof of the finite-copy theorem is otherwise unchanged. For the limiting gap-resolved experiment, every finite `N` and every joint POVM therefore obey

`Tr F_N^(nu)/N <= min(D_nu,U_nu) <= S(nu)`.

This includes arbitrary finite-copy entangled collective measurements on the limiting experiment.

### Consequence

The global equally spaced decomposition in Rev10 is sufficient for the exact compact-periodic formulation, but it is **not the essential algebraic hypothesis of the modewise tail bound**. The essential structure is a semibounded generator plus an exact spectral translation by the requested Bohr gap.

If an anharmonic finite or pure-point system has no pair separated by `hbar nu`, then `A_nu=0` and the asymptotic local Fisher retention at that exact modulation frequency vanishes. Anharmonicity can therefore strengthen the gap restriction rather than invalidate it.

---

# 4. Common-measurement Herglotz structure for an anharmonic spectrum

Fix the same base `nu`. Partition the pure-point spectrum into residue classes modulo `nu`: two frequencies belong to the same class when their difference is an integer multiple of `nu`.

Each nonempty class is a subset of an integer chain bounded below. Relabel its lowest occupied integer as `n=0` and append zero-population placeholders at missing integers and above the occupied set. On the direct sum of all completed residue chains define the isometry

`V = direct_sum_c sum_(n>=0) |c,n+1><c,n|`.

The physical baseline `rho0` has zero weight on every appended vector. For each integer `m>=1`,

`A_(m nu) = rho0^(1/2) V^m rho0^(1/2)`

is exactly the true `m nu` Bohr-gap tangent: endpoints separated by `m nu` contribute whether or not intermediate energies are physically occupied.

Therefore the Rev10 posterior-state/Herglotz argument applies verbatim to one fixed one-copy POVM across the harmonics `m nu`:

`R_M(m nu) = int cos(m theta) J_M(dtheta)`.

Thus the Toeplitz matrices of the retention sequence are positive semidefinite even for a globally anharmonic pure-point Hamiltonian.

The energy-tail block argument is now naturally continuous in energy. With

`S(x)=Pr(Omega>=x)`

and

`Ebar+/hbar = int_0^infinity S(x) dx`,

monotonicity gives

`Ebar+/hbar >= nu sum_(m=1)^M S(m nu) >= nu sum_(m=1)^M R_M(m nu)`.

Combining with the Herglotz angle propagation yields the same high-retention law

`Ebar+ >= hbar nu A(q)`, `q=R_M(nu)`,

and hence the same inverse-square-root divergence as `q->1`.

Thus the fixed-one-copy common-measurement near-lossless law also does not fundamentally require a globally harmonic Hamiltonian; it requires evaluation on the exact multiples of one chosen gap in the long-window dephased experiment.

The complete extremizer classification remains more specialized: Rev10's geometric-mixture/Hausdorff equivalence is still claimed only for the full contiguous single-chain pure-sector model.

---

# 5. Why zero-population completion is not a loophole

Let

`tau(B)=rho0^(1/2) M(B) rho0^(1/2)`.

If `|g>` is any appended zero-population vector, then `rho0^(1/2)|g>=0`, so

`tau(B)|g>=0`

for every measurable outcome set `B`.

For the posterior Radon--Nikodym density `tau(dy)=X_y p(dy)`, positivity and

`int X_y p(dy)=rho0`

imply `X_y|g>=0` for `p`-almost every `y`: the nonnegative function `<g|X_y|g>` integrates to zero, and positivity then forces the entire row/column to vanish.

Consequently every score

`Tr(V^m X_y)`

receives contributions only from physically populated endpoint sectors. Missing intermediate sectors merely provide an algebraic dilation allowing all exact `m nu` maps to be represented as powers of one isometry. They cannot create Fisher information.

The Herglotz representation is an equality representation of the actual retention sequence, not a looser bound obtained by granting population to fictitious states.

---

# 6. Singular-continuous spectral measures do not break Theorem 2

Rev10's controlled continuum theorem starts with an **arbitrary probability measure** `mu` on `[0,infinity)` with finite first moment. It does not assume a density.

For lower bins

`q_n^(delta)=mu([n delta,(n+1)delta))`,

one has exactly

`T_k^(delta)=mu([k delta,infinity))`.

With `k_delta=floor(nu/delta)`, for every `epsilon>0` and sufficiently small `delta`,

`nu-epsilon <= k_delta delta <= nu`,

so

`mu([nu,infinity)) <= mu([k_delta delta,infinity)) <= mu([nu-epsilon,infinity))`.

Continuity from above of a finite measure gives convergence to the closed tail as `epsilon downarrow 0`. This argument is valid for:

- absolutely continuous measures;
- pure-point/atomic measures;
- singular-continuous measures;
- arbitrary mixtures of these.

No smoothness under nested refinement is used.

The genuine continuum hypothesis is elsewhere: a chosen sequence of periodic **physical measurement schemes** must have retention values converging (or one states the corresponding limsup result). This is deliberately a controlled-limit statement because a normalized uniform time distribution on the noncompact group `R` does not exist.

A useful manuscript clarification is therefore: *spectral-measure regularity is not assumed; the controlled hypothesis concerns the physical detector/source limit, not smoothness of `mu`.*

The adversarial claim that singular-continuous spectra are frequent in structured open-system baths is also too broad. Standard structured-bath models are usually expressed through continuous spectral densities and/or discrete oscillator-mode sums; singular-continuous spectra occur in more special quasiperiodic/disordered/fractal spectral problems. This physical side claim is not needed for the mathematical rebuttal.

---

# 7. Local Fisher scope

The critique that the theorem is local is correct but not a newly exposed defect. Rev10 explicitly states that it bounds Fisher information at the uniform/random-time baseline and is not a global finite-amplitude estimation-risk theorem.

Because the sinusoidal random-time family is affine in `(eps_c,eps_s)`, there is a separate possible global distinguishability bound. For perturbation amplitude `a=sqrt(eps_c^2+eps_s^2)`,

`rho_eps-rho0 = a D_phi`

with

`D_phi=(e^(-i phi)A+e^(i phi)A^dagger)/2`.

Therefore

`||D_phi||_1 <= ||A||_1`

and, in the pure-sector model,

`||A||_1 = sum_pairs sqrt(q_lower q_upper) <= sqrt(D U) <= sqrt(T)`.

Thus every downstream parameter-independent measurement/channel obeys the finite-amplitude trace-distance ceiling

`(1/2)||rho_eps-rho0||_1 <= (a/2) sqrt(D U) <= (a/2) sqrt(T)`.

This gives a global binary-discrimination/total-variation consequence, but it has a square-root tail coefficient and is conceptually different from the local Fisher theorem. It should be developed only if it materially improves the manuscript rather than added defensively.

---

# 8. Research decision

The strongest adversarial point should not be answered merely by defensive wording. The arbitrary-pure-point gap extension is a genuine theorem-level strengthening and directly removes the claim that anharmonicity destroys the proof engine.

Recommended next gate:

1. numerically validate the long-window convergence and arbitrary-gap FI coefficient on deliberately incommensurate spectra;
2. targeted priority search for a prior arbitrary-POVM Fisher-tail theorem formulated at exact Bohr gaps of an anharmonic semibounded Hamiltonian;
3. if both pass, replace the peripheral separately optimized SLD-QFI section in the manuscript with a compact fixed-Hamiltonian pure-point extension, keeping page count approximately unchanged;
4. add one sentence to the continuum theorem stating explicitly that no absolute-continuity/smoothness assumption on `mu` is made;
5. add one sentence to the Herglotz proof explaining null-sector completion invariance.

Do not broaden the complete-extremizer theorem beyond its proven contiguous-chain scope.
