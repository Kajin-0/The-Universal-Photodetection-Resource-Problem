# Rev8 surgical referee repairs

Source: hostile Rev7 re-review supplied 2026-08-20.

Only three changes are authorized for Rev8:

1. Rare-fast Appendix A: require fixed positive parameters to satisfy `acp >= bqs`, and show exactly that `f_R-r_R = R(acp-bqs)/(RD+E) >= 0` for every `R>0`. This places the family inside the main thermodynamic section's assumed `f>=r` sector without changing the counterexample's scaling.
2. Timing-resource hierarchy: state explicitly that `R_2`, `B_FI`, and the hazard resource belong to the absolutely continuous square-integrable finite-area branch, while atomic or more singular timing measures are governed first by the Wiener residue result and need not have finite Fisher spectral area.
3. Thermodynamic activity: define stationary one-way activity as total directed stationary jump traffic, `A_tot = sum_x pi_x sum_{y != x} W_{yx}`, with each directed jump counted once, fixing the factor-of-two convention.

Do not broaden the theorem class or add new foundational results in this revision.
