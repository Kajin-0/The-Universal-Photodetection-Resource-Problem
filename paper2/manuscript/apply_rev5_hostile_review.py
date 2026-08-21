from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev4.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev5.tex")

text = SRC.read_text(encoding="utf-8")

replacements = [
    (
        "For a parameter-independent autonomous detector channel driven by the source family above, there exists an even measurable function",
        "For a parameter-independent autonomous detector channel driven by the source family above, the Fisher bilinear form initially defined on $C_c^\\infty(\\R)$ extends uniquely and continuously to $L^2(\\R)$, and there exists an even measurable function",
        "clarify L2 extension versus physical tangent class",
    ),
    (
        "The independent-event timing law of the first paper is recovered as a special case. Here we instead ask what the spectrum does when high-flux history dependence is essential.",
        "The autonomous independent-event marked-delay channel is recovered as the special case $G(\\omega)=\\int |H_m(\\omega)|^2\\,\\kappa(dm)$, where $H_m$ is the characteristic function of the mark-conditioned registration delay and $\\kappa$ is the capture measure over accessible marks. Here we instead ask what the spectrum does when high-flux history dependence is essential.",
        "make independent-event recovery self-contained",
    ),
    (
        "The exact numerical spectrum used for Fig.~\\ref{fig:typeIIspectrum} is obtained from the causal Volterra renewal equations given in the underlying derivation; the numerical values quoted in the main text are validation rather than premises of the theorem.",
        r"""For numerical evaluation at the saturation point $\lambda=\tau=1$, let $k_0(d)$ be the baseline next-registration density and $k_1(d)$ its first-order complex-mode derivative. With
\begin{equation}
 h_\omega(v)=e^{i\omega v}-\frac{e^{i\omega v}-1}{i\omega},
\end{equation}
the causal Volterra equations are
\begin{equation}
 k_0(d)=e^{-d}\mathbf1_{\{d>1\}}
 +\int_0^{\min(1,d)} e^{-v}k_0(d-v)\,dv,
\label{eq:volterraK0}
\end{equation}
and
\begin{align}
 k_1(d)=&\ e^{-d}h_\omega(d)\mathbf1_{\{d>1\}}\\
 &+\int_0^{\min(1,d)}e^{-v}
 \left[h_\omega(v)k_0(d-v)+e^{i\omega v}k_1(d-v)\right]dv.
\label{eq:volterraK1}
\end{align}
The exact complete-record multiplier is then
\begin{equation}
 G_1(\omega)=e^{-1}\int_1^\infty\frac{|k_1(d)|^2}{k_0(d)}\,dd.
\label{eq:volterraG}
\end{equation}
We solved Eqs.~\eqref{eq:volterraK0}--\eqref{eq:volterraG} by causal trapezoidal quadrature. At $\omega\tau=\pi$, step sizes $h=0.005$ and $0.0025$ give $0.52783253$ and $0.52798759$, respectively; first-order Richardson extrapolation gives $0.52814265$, above the rigorous bound $0.51697536$. The numerical spectrum is validation rather than a premise of Theorem~\ref{thm:spectralEscape}.""",
        "make Figure 2 numerical method self-contained",
    ),
    (
        "Equation~\\eqref{eq:ordRate}, the sublinear boundary term, and a standard split on $Y\\le\\delta L$ versus $Y>\\delta L$ yield Eq.~\\eqref{eq:windowEquality}.",
        "By data processing from the future Poisson source, $I_{\\rm ord}(s)\\le\\lambda s$ for every $s$. Equation~\\eqref{eq:ordRate}, this linear bound, the sublinear boundary term, and a split on $Y\\le\\delta L$ versus $Y>\\delta L$ therefore yield Eq.~\\eqref{eq:windowEquality} by first taking $L\\to\\infty$ and then $\\delta\\downarrow0$.",
        "state the domination used in stationary-window limit",
    ),
    (
        "The repository contains independent Volterra numerical assets for the complete static FI values quoted in Sec.~\\ref{sec:noGo}. Those numbers are validation rather than a premise of Theorem~\\ref{thm:varianceNoGo}.",
        "Independent Volterra evaluation gives the complete static FI values quoted in Sec.~\\ref{sec:noGo}; those numbers are validation rather than a premise of Theorem~\\ref{thm:varianceNoGo}.",
        "remove repository-internal drafting language",
    ),
]

for old, new, label in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one target for {label}, found {count}")
    text = text.replace(old, new)

required = [
    r"extends uniquely and continuously to $L^2(\R)$",
    r"G(\omega)=\int |H_m(\omega)|^2\,\kappa(dm)",
    r"\label{eq:volterraK0}",
    r"\label{eq:volterraK1}",
    r"\label{eq:volterraG}",
    r"I_{\rm ord}(s)\le\lambda s",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev5 invariant missing: {token}")

for forbidden in [
    "first paper",
    "The repository contains",
    "underlying derivation",
    "placeholder",
    "TODO",
    "TBD",
]:
    if forbidden in text:
        raise RuntimeError(f"Drafting residue survived Rev5: {forbidden}")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
