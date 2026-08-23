# WP07 / WP18 sine-coordinate convention erratum

**Date:** 2026-08-23

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** harmless coordinate-sign correction; no theorem, Fisher-information, curvature, action, or sharpness coefficient changes.

The branch convention is

`D_c=(A+A^dagger)/2`,

`D_s=(A-A^dagger)/(2i)`.

For

`A=2c|1><0|`,

this gives

`D_s=-ic|1><0|+ic|0><1|`.

Therefore an exact pure-state family whose `y` derivative is **exactly** `D_s` is

`|psi(x,y)>=sqrt(1-c^2(x^2+y^2))|0>+c(x-i y)|1>`.

The original WP07 illustrative ket was written with `x+i y`. That family realizes the same tangent plane but with the sine coordinate reversed:

`partial_y rho(0)=-D_s`.

Equivalently, it is the convention-consistent family after the reparameterization `y -> -y`.

Consequences:

- `R_lin=0` is unchanged;
- `T_U=c^2(x^2+y^2)` is unchanged;
- `Delta T_U=4c^2` is unchanged;
- `J=4c^2` is unchanged;
- the attainable two-quadrature Fisher trace is unchanged;
- every WP07 inequality and sharp coefficient is unchanged.

The same convention mismatch was independently found and already corrected in the audited WP18 one-sided extremizer. The new autonomous-temporal manuscript uses the convention-consistent `x-i y` form whenever an exact family is stated.

This erratum should be read together with

- `WP07_NONLINEAR_ZERO_RADIUS_CURVATURE_AND_FINITE_AMPLITUDE_LAW.md`;
- `WP18_AUTONOMOUS_DUAL_SYNTHESIS_ACTION_LAW.md`;
- `HOSTILE_MATHEMATICAL_AUDIT_WP18_WP20.md`.
