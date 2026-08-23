# Publication theorem stack after significance and mathematical audits

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** publication architecture frozen provisionally. This is not a manuscript and does not certify priority. It records the smallest coherent theorem package that survived both the literature significance gate and the hostile mathematical audit.

## 1. Recommended paper claim

Use a narrow physical claim:

> **Autonomous temporal information has two complementary spectral-resource regimes.** For a globally stationary exact clock--signal exchange with nonzero physical affine tangent radius, robust temporal Fisher information requires pre-existing spectral survival on both sides of the exchange. At a rank-changing boundary where the affine tangent radius vanishes but an exact nonlinear family exists, temporal Fisher information instead requires positive second-order endpoint synthesis action on both sides. The clean constants are sharp in fixed-total-energy shells; arbitrary coherent support requires shorted/operator geometry; and the boundary resource obeys a sharp multi-frequency sum.

Do not advertise a new resource theory of time.

## 2. Main-text theorem stack

### Main Result 1 — baseline-energy no-go and finite-radius repair

From WP02.

Show first that fixed baseline mean energy does not bound unrestricted high-frequency local Fisher information under arbitrary state synthesis.

Introduce the physical affine tangent radius `R_lin` and prove

`(R_lin^2/4)[Tr F_N/N] <= T(nu)`

for every finite `N` and arbitrary collective POVM.

This result motivates why local Fisher alone is not the physical resource.

### Main Result 2 — autonomous dual survival

From WP03 and WP06.

For exact exchange

`[H_S,A_nu]=+hbar nu A_nu`,

`[H_C,A_nu]=-hbar nu A_nu`,

prove

`(R_lin^2/4)[Tr F_N/N] <= min{T_C(nu),T_S(nu)}`.

Emphasize that:

- the joint family may be globally stationary;
- global time-translation asymmetry need not supply the resource;
- arbitrary pre-existing coherent/history-state support is allowed after WP06;
- the clean total energetic coefficient is sharp asymptotically.

This is the finite-radius half of the paper's central dichotomy.

### Main Result 3 — rank-changing boundary synthesis law

Use only the minimum WP07/WP09 machinery needed to close the `R_lin=0` loophole.

One-sided boundary:

`Tr F_N/N <= J <= Delta T`.

Bilateral boundary:

`sqrt[Tr F_N/N] <= sqrt(J_+)+sqrt(J_-)`.

Include the exact qutrit factor-two counterexample to naive additive endpoint curvature. This establishes why the boundary resource is second order and why coherent opposite orientations combine by amplitude rather than probability.

The full WP12 allocation SDP is not needed in the main text unless required for the arbitrary-support theorem proof.

### Main Result 4 — sharp autonomous dual synthesis action

WP18 is the zero-radius autonomous completion and should be the centerpiece.

Bilateral:

`boxed: A_C^(2)+A_S^(2)>=(hbar nu/4)[Tr F_N/N]`.

One-sided:

`boxed: A_C^(2)+A_S^(2)>=(hbar nu/2)[Tr F_N/N]`.

Use the fixed-total-energy qutrit/qubit extremizers.

Stress simultaneously:

- exact global stationarity;
- zero global time-translation asymmetry;
- zero signed total-energy curvature;
- nonzero relative temporal Fisher information;
- exact positive synthesis-action saturation.

This is the clearest result not naturally summarized by standard asymmetry language.

### Main Result 5 — arbitrary coherent-support bridge

State the audited WP19 theorem, but keep the technical proof largely in the supplement.

Use canonical endpoint-role projectors

`Pi_out=supp(A A^dagger)`,

`Pi_in=supp(A^dagger A)`

and

`G_ex=2hbar nu Q(Pi_out+Pi_in)Q`.

With two-sided shorted pre-existing ceilings `a_+,a_-`, restricted synthesis prices `g_+,g_-`, and

`A_ex^(2)=(1/4)Tr(G_ex C_Delta)`,

state

`Tr F_N/N`

`<=min{Psi_(a_+)(4A_ex;g_+,g_-),`

`      Psi_(a_-)(4A_ex;g_-,g_+)}`.

This theorem shows the central finite-radius/boundary dichotomy survives arbitrary coherent support rather than only diagonal baselines.

Use the shared-kernel fixed-shell qutrit to show the resource layer can be strictly above the QFI and common-record layers:

`12 > 43/4 > 55/8`.

The exact `55/8` proof itself should probably be supplementary.

### Main Result 6 — multi-frequency boundary sum

WP20.

For one common multiparameter boundary family,

`C_Sigma>=sum_k[Z_(k,+)+Z_(k,-)]`.

With positive spectral cost `G`,

`sum_k gamma_k Tr F_(N,k)/N <=4A_(G,Sigma)^(2)`.

For clean bilateral exchanges,

`boxed: A_(G,Sigma)^(2)`

`>=sum_k(hbar nu_k/4)Tr F_(N,k)/N`.

Use the fixed-total-energy star shell and one discrete Fourier measurement to show **simultaneous sharpness of every mode and the entire weighted sum**.

This is the natural final theorem: the resource principle becomes a spectrum rather than a single-frequency inequality.

## 3. What should NOT be central in the main paper

### WP04 / WP05

The exact hard/mean-energy retention and sine-chain results are strong but belong to a different finite-amplitude structured-retention story. Including them would make the current paper too broad. Cite them only if they supply motivation or place them in a separate future manuscript.

### WP08

Useful as a precursor to WP20 but can be compressed to a lemma or supplement.

### WP10

Clean mixed commuting-support bridge is a special case of WP19. Supplement or omit from main theorem numbering.

### WP11--WP14

These are important technical infrastructure:

- shorting constants;
- shared curvature allocation;
- positive spectral action;
- inverse-curvature principal angle.

Use only the pieces needed to prove WP19. Full operator-allocation development belongs in the supplement unless referees demand it.

### WP15 / WP16

These prove that resource, QFI, and accessible Fisher are genuinely different layers and are valuable evidence against conflation. However, a long measurement-optimization section risks obscuring the physical resource theorem.

Recommendation:

- main text: show the hierarchy `12 > 43/4 > 55/8` in one concise figure/example;
- supplement: exact `55/8` witness and generic rank-one-kernel accessibility theorem.

### WP17

No-go bookkeeping only. Do not include except possibly as an internal record.

## 4. Suggested paper structure

1. **Introduction** — why detector/clock temporal information needs a physical resource law; distinguish from standard QFI/asymmetry statements.
2. **Mean-energy no-go** — fixed mean energy cannot bound arbitrary synthesized local Fisher.
3. **Physical tangent robustness** — WP02 theorem.
4. **Autonomous relative time** — WP03/WP06 dual survival.
5. **Rank-changing boundary** — WP07/WP09 second-order synthesis.
6. **Autonomous synthesis action** — WP18, sharp fixed-shell extremizers.
7. **Arbitrary coherent support** — concise WP19 theorem and qutrit hierarchy.
8. **Spectral sum law** — WP20 and simultaneous Fourier saturation.
9. **Relation to prior art** — shared asymmetry, energetic coherence/QFI, WAY, waveform Holevo, protocol-energy constraints.
10. **Discussion** — kinematic endpoint-incidence action versus dynamical implementation energy; open continuum/dynamical questions.

Supplement:

- full finite-copy weighted-score proofs;
- PSD-cone curvature derivation;
- WP11--WP14 shorted/allocation machinery;
- full WP19 benchmark reconstruction;
- WP15/WP16 accessibility proofs;
- validators / symbolic checks.

## 5. Recommended title directions

Avoid grandiose titles such as `A resource theory of time`.

Better candidates:

- **Spectral resource laws for autonomous temporal information**
- **Pre-existing survival and synthesis action constrain relational temporal information**
- **Resource bounds for rank-changing temporal information in energy-conserving quantum systems**
- **Two spectral-resource regimes for autonomous temporal information**

The second or fourth title best captures the actual theorem story.

## 6. Required prior-art positioning in the manuscript

Explicitly distinguish the theorem from:

- Marvian--Spekkens modes of asymmetry;
- Carmo--Soares-Pinto shared asymmetry/Page--Wootters resource;
- Marvian QFI energetic-coherence formation cost;
- Tajima--Shiraishi--Saito conservation-law coherence cost;
- quantitative WAY/reference-frame bounds;
- Safranek rank-changing QFI/Bures geometry;
- Gardner et al. waveform Holevo bounds;
- Chen--Yang protocol-level energy-constrained metrology;
- fixed-number relative-phase and multiphase measurements.

The paper should say explicitly that its synthesis action is a **kinematic state-family resource**, not a complete implementation-energy accounting.

## 7. Publication gate status

- Literature significance gate: **PROVISIONAL PASS**.
- Hostile mathematical gate: **PASS after minor corrections**.
- Priority: **UNVERIFIED**.
- Manuscript theorem stack: **FROZEN PROVISIONALLY**.

The next action may be manuscript formation. Do not add further abstract work packages unless manuscript drafting exposes a concrete missing theorem or defect.
