# Research Roadmap

**Updated:** 2026-08-22

`main` is the repository landing/index branch.

**Active scientific branch:** `agent/temporal-information-resource-law`

Paper 1 Rev11 and Paper 2 Rev7 are frozen.

Grand Challenge science checkpoint: **WP24**.

- Rev4: frozen science content.
- Rev5: frozen publication content.
- Rev6: current PRX Quantum style package.

## Theorem state

For exact periodic random-time encoding with sector probabilities `q_n`, any finite-copy joint POVM obeys

`Tr F_N^(k)<=N min(D_k,U_k)<=N T_k`,

`T_k=sum_(m>=k)q_m`,

and hence `sum_(k>=1)R_N(k)<=nbar`.

Controlled large-period limits obey

`R(nu)<=P(Omega>=nu)`,

`int_R R(nu)dnu<=2Ebar^+/hbar`,

`Ebar^+>=hbar nu R(nu)=h f R(2pi f)`.

WP23 gives the independent-event source-to-field embedding; WP14 gives the arbitrary-waveform no-go. The separately optimized QFI envelope remains secondary.

## Priority

The candidate contribution is the operational classical-Fisher tail/survival theorem and its energy/source-to-record consequences. Generic `U(1)` modes, phase estimation, general quantum-information bounds, random-unitary estimation, waveform QFI, Hardy--Hilbert analysis, and generic Poisson/CPTP machinery are prior art.

**Priority remains unverified, not certified.**

## Manuscript / journal gate

Working title: **A Sharp Energy-Survival Law for Temporal Fisher Information**.

Rev5 passed complete local publication preflight. Rev6 changes only REVTeX style `pra -> prx` and remains seven pages with no local target-style page-flow regression. Dedicated CI is configured to compile Rev6.

**First target:** PRX Quantum — Research Article.

**Preferred fallback:** Physical Review A — Regular Article.

PRL is a stretch only after a separate Letter rewrite.

## Current work order — human submission completion

No new theorem or autonomous polish work by default.

1. Human author personally verifies the AI-assisted science/manuscript sufficiently to make a truthful APS disclosure.
2. Supply final author name/order, affiliation(s), contact email, optional ORCID(s), funding/conflict/submission-history facts.
3. Decide preprint/e-print status.
4. Select a stable repository/archive citation for Data Availability.
5. Decide optional referee recommendations/exclusions.
6. Confirm PRX Quantum APC coverage/institutional agreement.
7. Generate the final administrative Rev6 submission package.
8. Run one final build/checksum/visual pass.
9. Submit to PRX Quantum.

If PRX Quantum declines on selectivity rather than correctness, prefer APS transfer to PRA rather than broadening claims.

## Documentation policy

Detailed derivations and manuscript generation live on `agent/temporal-information-resource-law`; `main` must always show the current target/status.