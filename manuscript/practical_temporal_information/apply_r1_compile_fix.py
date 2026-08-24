from pathlib import Path

ROOT = Path(__file__).resolve().parent
src = ROOT / "operational_temporal_information_draft.tex"
out = ROOT / "operational_temporal_information_r1.tex"

text = src.read_text(encoding="utf-8")

old_lead = (
    "A practical theory should distinguish failure of a detector reduction from failure of a resource inequality. "
    "Table~\\ref{tab:falsification} summarizes that hierarchy."
)
new_lead = (
    "A practical theory should distinguish failure of a detector reduction from failure of a resource inequality. "
    "The tests below summarize that hierarchy."
)

start_marker = "\\begin{table*}[t]"
end_marker = "\\end{table*}"

if text.count(old_lead) != 1:
    raise SystemExit("Expected exactly one falsification-table lead sentence")
if text.count(start_marker) != 1 or text.count(end_marker) != 1:
    raise SystemExit("Expected exactly one falsification table")

replacement = r"""\noindent\textbf{Linear Gaussian detector.}
Measure $\mathcal R(f)$, $S_n(f)$, and the empirical likelihood/Fisher information. The prediction is $F_{xx}/T=F_{yy}/T=|\mathcal R|^2/S_n$. A significant failure is Level I evidence for non-Gaussianity, nonstationarity, parameter-dependent covariance, calibration error, or nonlinear response.

\medskip\noindent\textbf{Poisson timestamps with jitter.}
Measure $\lambda_0$, the jitter distribution, and the timestamp Fisher information. The prediction is $\Tr F/T=\lambda_0|\Phi_J|^2$. A significant failure is Level I evidence for a non-Poisson source, correlated or state-dependent jitter, dead time, afterpulsing, or likelihood mismatch.

\medskip\noindent\textbf{Type-II memory benchmark.}
Measure the rate curve together with interval or higher-order timestamp statistics. The companion result predicts that the same $r(\lambda)$ need not imply the same timestamp Fisher information, and deterministic recovery is singular at $\lambda m=1$. A failure first tests the specified recovery model; only after reproducing the companion assumptions would it challenge the companion theorem.

\medskip\noindent\textbf{Finite sideband seed.}
Measure $p$, $\kappa$, $R_{\rm lin}$, and the phase-sensitive Fisher information. The prediction is $(R_{\rm lin}^2/4)\Tr F\le p$. A violation is Level II only after independently verifying the selected-mode state model, support, radius, and parameter normalization.

\medskip\noindent\textbf{Empty sideband boundary.}
Measure $\Delta P_s(0)$ and the phase-sensitive Fisher information. The prediction is $\Tr F\le\Delta P_s(0)$. A violation is Level II under independently verified boundary-state assumptions.

\medskip\noindent\textbf{Ideal phase modulation.}
Measure $\Delta P_\pm(0)$ and the Fisher information. The ideal equality is $\Tr F=[\sqrt{\Delta P_+}+\sqrt{\Delta P_-}]^2=4$. Failure is Level III evidence against the ideal modulator/analyzer model unless the underlying inequality itself is exceeded under verified assumptions.

\medskip\noindent\textbf{Resonant exchange benchmark.}
Independently calibrate $gt$ and the endpoint curvature $C$. The ideal equality is $V_{\rm impl}=\tfrac12\Tr C=8(gt)^2$. Failure of equality is Level III; a sub-bound value under verified theorem assumptions would challenge the companion lower bound."""

start = text.index(start_marker)
end = text.index(end_marker, start) + len(end_marker)
text = text.replace(old_lead, new_lead)
text = text[:start] + replacement + text[end:]

out.write_text(text, encoding="utf-8")
print(f"Generated {out.name}: replaced the REVTeX-incompatible falsification table with conservative paragraph blocks")
