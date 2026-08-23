# M2R1 post-rewrite hostile consistency audit

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

## Verdict

**STATEMENT-LEVEL PASS.**

No new theorem defect, coefficient error, dimensional inconsistency, or hidden measurement assumption was found after rewriting the audited M2R1 main and supplement. The remaining unclosed gate is mechanical LaTeX/BibTeX compilation because this session cannot retrieve push-triggered Actions results or materialize the repository into the local runtime.

Priority remains unverified, not certified.

## Audited canonical pair

- `autonomous_temporal_resource_law_m2r1.tex`
- `autonomous_temporal_resource_law_supplement_m2r1.tex`

with proof modules:

- `proofs/finite_radius_survival_proofs.tex`
- `proofs/boundary_and_autonomous_action_proofs.tex`
- `proofs/noncommuting_mixed_bridge_proof_r1.tex`
- `proofs/multigap_action_sum_proof_r1.tex`
- `proofs/shared_kernel_qutrit_benchmark.tex`
- `proofs/wp15_exact_common_record_qutrit.tex`

## Checks passed

### Finite-radius layer

- The single-system `min{D_nu,U_nu}` theorem is stated under a stationary baseline, matching the clean WP02 proof.
- The autonomous dual-survival theorem separately invokes the arbitrary-coherent-baseline WP06 extension, so separate local stationarity is not accidentally reintroduced.
- Independent-copy weighted norms scale exactly by `N`; no separable-readout assumption enters.
- `R_lin^2 Tr F` is dimensionless under the fixed quadrature normalization.

### Rank-changing layer

- One-sided boundary theorem uses `Tr F_N/N <= J <= Delta T` with the audited coefficient.
- Bilateral score amplitudes combine by Minkowski rather than false scalar additivity.
- Clean autonomous action coefficients remain exactly
  - bilateral: `hbar nu/4`,
  - one-sided: `hbar nu/2`.
- The one-sided fixed-shell ket uses the convention-consistent `x-i y` sign.

### Mixed arbitrary-support layer

- Canonical cost remains
  `G_ex=2 hbar nu Q(Pi_out+Pi_in)Q`.
- Bilateral `Psi` reduction is used only when both synthesized orientations are nonzero and positively priced.
- Plus-only, minus-only, and no-synthesis cases are derived directly from the measurement-side master inequality rather than by assigning eigenvalues to absent ranges.
- A zero shorting constant means that local scalar survival branch is unavailable; it is not represented by division by zero or by an infinite value inside `Psi`.
- A nonzero synthesized direction with `g=0` is explicitly outside finite scalar action-only control for that chosen `G`.
- If no internal scalar branch is available, the scalar mixed reduction is vacuous while the underlying operator/measurement inequalities remain valid.

### Multi-gap layer

- Operator-valued PSD curvature is summed before scalar pricing, preventing per-mode double charging.
- Effective bilateral price is harmonic only for positively priced nonzero orientations.
- A cost-null information-bearing direction receives `gamma_k=0`; no positive control is claimed from that `G`.
- The theorem refers to Fisher blocks of one fixed common record and does not assert simultaneous optimality in general.
- The fixed-shell Fourier extremizer independently proves simultaneous saturation in the clean mode-separated model.
- Parameter-space trace uses the fixed direct-sum Euclidean metric of the cosine/sine quadratures; arbitrary anisotropic reparameterization invariance is not claimed.

### Qutrit hierarchy

The supplement is self-contained and preserves

`12 > 43/4 > 55/8`

for physical resource, SLD-QFI trace, and exact one-copy common-record Fisher supremum.

The canonical qutrit endpoint-incidence calculation remains

`G_ex/(hbar nu)=diag(2,4,2)`,

`g_+=g_-=13 hbar nu/4`,

`4 A_ex=247 hbar nu/16`,

and the scalar resource envelope gives exactly `12`.

## Dimensional audit

Under dimensionless mode coordinates (or, more generally, coordinates carrying a fixed amplitude unit):

- `F`: inverse-coordinate-squared;
- `R_lin^2 F`: dimensionless;
- `Delta T`: inverse-coordinate-squared;
- `g`, `hbar nu`: energy;
- `A^(2)`: energy times inverse-coordinate-squared;
- every displayed action/Fisher inequality is dimensionally homogeneous.

## Publication consequence

No additional theorem work is justified by the current manuscript audit. The correct next phase is publication positioning and prose compression:

1. identify the strongest defensible target journal based on current scope and comparable literature;
2. compress the abstract and introduction around the two-regime theorem rather than the full WP history;
3. preserve the narrow priority claim and explicit distinction from shared asymmetry, QFI resource theory, WAY/coherence costs, waveform Holevo bounds, and protocol-level energy constraints;
4. keep the mixed shorted-operator machinery and the `55/8` witness primarily in the supplement.

Do not start WP21 unless a later referee-style manuscript review exposes a genuine mathematical hole.
