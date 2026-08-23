# Follow-up dynamical theorem stack — minimum implementation cost of rank-changing temporal synthesis

## Status

**Provisional scope freeze for a separate follow-up manuscript.**

Do not expand the existing PRX Quantum R3 paper with the full WP21--WP32 program. The new results now form a distinct paper about **dynamical implementation cost**, not merely another extension of the two-regime resource law.

This stack should be used for the dedicated significance/prior-art gate before manuscript drafting.

## Working paper question

> Given a rank-changing local quantum state family with a prescribed first-order tangent and prescribed physically feasible second-order population in the baseline-empty sector, what is the least state-weighted dynamical coupling required to implement that local family under exact total-energy conservation?

The autonomous temporal application then asks how this minimum relates to the frequency-resolved endpoint synthesis action introduced in the R3 resource paper.

## Result 1 — exact kernel-curvature / implementation-coupling identity

For a smooth unitary dilation

`Omega(theta)=U(theta)Omega_0U(theta)^dagger`,

with reduced target state `rho(theta)=Tr_E Omega(theta)`, target support `P`, kernel `Q`, and Hermitian tangent generators `K_j`,

`boxed:
Q partial_j^2 rho(0) Q
=2 Tr_E[(Q⊗I)K_j Omega_0 K_j(Q⊗I)].`

For any positive target-kernel price `G`,

`boxed:
A_G^(2)
=(1/2)sum_j Tr[(G⊗I)K_j Omega_0 K_j].`

Interpretation: the positive kernel Hessian is not merely kinematic under a unitary realization. It is exactly the state-weighted squared implementation coupling into the baseline-empty target sector.

This should be the paper's opening theorem because it directly turns the R3 synthesis action into a dynamical object.

## Result 2 — first-order horizontal minimum as a prior-art bridge

For a pure-boundary tangent with SLD-QFI tensor `H_SLD`,

`V_min(first order)=(1/4)Tr H_SLD`.

For an exact relational tangent, the minimizing horizontal generator can be chosen to commute with the total clock--signal Hamiltonian.

This result is **not a headline novelty theorem**. Generic `QFI/4 = minimum purification/variance geometry` is prior art. Its role is to:

1. connect the new second-order problem to established Bures/Uhlmann geometry;
2. show the autonomous energy-conserving constraint does not increase the first-order minimum;
3. define the minimal curvature `C_min` that the full second-order theorem must exceed.

Keep the generic horizontal-lift derivation concise and cite prior art aggressively.

## Result 3 — central theorem: exact prescribed kernel-2-jet minimum

Let the target baseline be rank deficient and let `D_j` be pure-boundary first derivatives with finite right-relative norm. Define the minimal PSD-cone curvature

`C_min=2 sum_j QD_jP rho_0^+ P D_jQ`

in finite dimension, or the corresponding Hilbert--Schmidt trace-class form in infinite dimension.

Prescribe any positive metric-contracted target-kernel Hessian

`C>=C_min`.

Then every smooth unitary dilation realizing the prescribed local target data satisfies

`boxed:
V_impl>= (1/2)Tr C,`

where

`V_impl=sum_j Var_(Omega_0)(K_j)`.

Conversely the bound is exactly attainable.

Thus

`boxed:
V_min(C;D,rho_0)=(1/2)Tr C.`

This is the principal theorem of the follow-up paper.

The proof separates:

- the minimal horizontal tangent;
- the excess positive curvature `S=(C-C_min)/2`;
- an ancilla flag sector that is first-order invisible but supplies exactly `2S` at second order.

The theorem prescribes the **physical metric contraction of the target kernel Hessian**, not an arbitrary complete tensor of mixed second derivatives.

## Result 4 — exact total-energy-conserving realization

Assume a semibounded self-adjoint target Hamiltonian and strong stationarity/energy covariance:

- `U_t rho_0 U_t^dagger=rho_0`;
- `U_t D_j U_t^dagger=D_j`;
- `U_t C U_t^dagger=C`.

In finite dimension the optimum can be realized inside exact total-energy sectors.

In separable infinite dimension, WP32 gives the corrected universal construction:

1. diagonalize the occupied trace-class baseline jointly with the target energy;
2. decompose excess curvature into energy-adapted trace-class eigenmodes;
3. split one occupied baseline eigenstate into countably many classically incoherent ancilla-labelled copies;
4. replicate its horizontal tangent across the copies;
5. compensate arbitrary target-energy differences with nonnegative ancilla input/output energies;
6. form the global encoded state as a trace-class classical branch mixture.

Finite quadratic cost controls trace-norm `C^2` differentiability even when the global direct-sum generators are unbounded.

Therefore

`boxed:
inf_(semibounded exactly energy-conserving dilations)
V_impl=(1/2)Tr C.`

This should be stated as the strongest form of the central theorem, with the functional-analysis construction largely moved to Supplemental Material.

## Result 5 — autonomous spectral endpoint specialization

For a clean exact clock--signal exchange at positive gap `nu`, the kernel endpoint price is

`G_ex=2 hbar nu Q`

on the relevant synthesized endpoint sector.

The synthesis action is

`A_ex^(2)=(1/4)Tr(G_ex C)
=(hbar nu/2)Tr C`.

Hence the central theorem becomes

`boxed:
V_min=A_ex^(2)/(hbar nu).`

This is the main physical specialization:

> the frequency-resolved spectral synthesis action equals `hbar nu` times the least state-weighted quadratic coupling required to implement the prescribed rank-changing local temporal 2-jet.

The realization can conserve total bare energy exactly. Therefore net energy change/work is not the relevant implementation resource.

## Result 6 — information consequences

At the minimal pure-boundary orbit,

`V_min=(1/4)Tr H_SLD`.

For any implementation with prescribed nonminimal curvature,

`V_impl=(1/2)Tr C >= (1/4)Tr H_SLD`.

Combining with the clean common-record resource laws gives, where applicable,

- bilateral: `V_impl >= (1/4) Tr F_N^tan/N`;
- one-sided: `V_impl >= (1/2) Tr F_N^tan/N`.

These are secondary corollaries. The paper should not be sold as a new QFI or measurement-accessibility theorem.

## Result 7 — net-work no-go

The fixed-total-energy sharp constructions satisfy

`Delta <H_tot>=0`

and can keep the entire total-energy distribution unchanged while

`V_impl>0`, `A_ex>0`, and temporal information is nonzero.

Therefore no universal implementation-cost law based only on net bare-energy change can reproduce the synthesis resource.

This is conceptually important and should appear in the main text, but it is a no-go clarification rather than a new thermodynamic resource theory.

## Result 8 — robustness to imperfect resonance

WP25/WP27 show that exact Bohr resonance is not an all-or-nothing requirement for the information-resource law. Near-resonant pieces are charged by slightly enlarged endpoint windows; off-resonant pieces are charged by weighted commutator residuals.

For this follow-up paper, keep these as **robustness corollaries**, not the main theorem, unless an exact approximate-exchange dynamical-cost theorem is derived during drafting.

## Result 9 — infinite-dimensional information laws

WP28/WP29 show that the finite-radius and pure-boundary information-resource laws themselves survive in separable infinite dimension under bounded-relative / Hilbert--Schmidt finite-information assumptions.

Use only the parts needed to make Result 4 self-contained. Do not turn the follow-up into a general treatise on infinite-dimensional metrology.

## Main-text theorem stack

Recommended main paper order:

1. implementation-coupling identity;
2. concise first-order horizontal/Bures bridge;
3. exact prescribed kernel-2-jet minimum;
4. exact energy-conserving realization;
5. autonomous spectral endpoint identity;
6. fixed-energy sharp construction / net-work no-go;
7. concise robustness and infinite-dimensional consequences.

## Supplemental Material

Move to supplement:

- full PSD-cone feasibility derivation;
- all infinite-dimensional trace-class/Hilbert--Schmidt domain details;
- countable joint energy/eigenbasis lemma;
- WP32 classical splitting and ancilla-energy compensation construction;
- direct-sum self-adjointness and trace-norm `C^2` dominated convergence;
- random validators;
- approximate-gap proof details;
- mixed orientation bookkeeping not needed by the central clean theorem.

## Explicit exclusions

Do not claim or attempt to prove in this paper unless required by a concrete referee gap:

- thermodynamic work, battery depletion, switching work, or reset cost;
- a new covariant Stinespring theorem;
- a new Bures/Uhlmann/QFI variational principle;
- a new generic quantum speed limit;
- arbitrary complete second-order derivative tensors;
- universal channel implementation for all possible input states;
- noisy/CPTP optimal implementation cost;
- unbounded-relative-tangent quadratic-form generality;
- a general resource theory of time.

## Working novelty sentence

Subject to the dedicated priority gate:

> We determine the exact minimum state-weighted quadratic coupling required to realize a prescribed feasible rank-changing kernel second-order jet of a quantum state, show that the minimum can be attained under exact total-energy conservation even in separable infinite dimension, and identify the frequency-resolved endpoint synthesis action of an autonomous temporal mode as precisely `hbar nu` times this minimum cost.

Do not strengthen this sentence without new prior-art evidence.