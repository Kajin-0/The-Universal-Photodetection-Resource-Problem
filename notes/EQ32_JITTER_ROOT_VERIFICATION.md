# Eq. 32 Jitter-Root Verification

**Date:** 2026-08-20

## Trigger

An external review of `manuscript/event_resource_theorem_rev6.tex` reported a possible numerical mismatch when solving the quadratic used in Eq. 32 of the exact fixed-mean/fixed-variance jitter no-go construction.

## Result

**VERIFIED — no manuscript correction is required.**

The variance written in the manuscript is

\[
V_{\epsilon,n}(x)
=\frac{2(1-\epsilon)}{n^2}+2\epsilon x^2
-\left[\frac{1-\epsilon}{n}+\epsilon x\right]^2.
\]

Expanding gives

\[
\epsilon(2-\epsilon)x^2
-\frac{2\epsilon(1-\epsilon)}{n}x
+\frac{1-\epsilon^2}{n^2}
-\sigma^2=0.
\]

The positive quadratic root is

\[
x
=\frac{\epsilon(1-\epsilon)/n
+\sqrt{\epsilon(2-\epsilon)\sigma^2-2\epsilon(1-\epsilon)/n^2}}
{\epsilon(2-\epsilon)}.
\]

Factoring `sqrt(epsilon)/n` from the square root and simplifying yields exactly the manuscript form

\[
\boxed{
x_{\epsilon,n}
=\frac{
\sqrt{(2-\epsilon)n^2\sigma^2-2(1-\epsilon)}
+\sqrt\epsilon(1-\epsilon)
}{
\sqrt\epsilon\,n(2-\epsilon)
}.}
\]

Direct substitution returns `V_{epsilon,n}(x_{epsilon,n}) = sigma^2` identically. Independent numerical substitution across representative `epsilon` values also agrees to machine precision.

## Publication consequence

The external-review concern is resolved as a reviewer-side algebra/numerical mismatch rather than a defect in Rev6. The qualitative and exact fixed-mean/fixed-variance no-go theorem remain unchanged.
