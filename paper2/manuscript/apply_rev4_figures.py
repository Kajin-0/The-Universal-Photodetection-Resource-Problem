from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev3.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev4.tex")

text = SRC.read_text(encoding="utf-8")

pkg_old = r"\usepackage{graphicx}"
pkg_new = """\\usepackage{graphicx}
\\usepackage{tikz}
\\usepackage{pgfplots}
\\pgfplotsset{compat=1.18}
\\usetikzlibrary{patterns}"""
if text.count(pkg_old) != 1:
    raise RuntimeError("Expected exactly one graphicx package line")
text = text.replace(pkg_old, pkg_new)

figures = [
    (
        r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.88\linewidth}{\centering
\vspace{1.0cm}
\textbf{Figure 1 placeholder.} Poisson input trajectory $\rightarrow$ autonomous detector with hidden memory $\rightarrow$ complete accessible record. Contrast a scalar saturation curve $r(\lambda)$ with the complete local Fisher spectrum $G(\omega)$.
\vspace{1.0cm}}}
\caption{Conceptual distinction between a scalar high-flux response summary and the complete local temporal information-transfer object.}
\label{fig:concept}
\end{figure}""",
        r"\input{figure1_channel_schematic}",
        "Figure 1",
    ),
    (
        r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.88\linewidth}{\centering
\vspace{1.0cm}
\textbf{Figure 2 placeholder.} Plot exact numerical $G_1(\omega)$ and rigorous lower bound $L_1(\omega\tau)$ versus $\omega\tau$; show static zero, the point $\pi$, and horizontal asymptote $1/e$.
\vspace{1.0cm}}}
\caption{Deterministic Type-II information spectrum at the classical paralysis maximum. The detector is statically Fisher-blind but retains information at every nonzero frequency.}
\label{fig:typeIIspectrum}
\end{figure}""",
        r"\input{figure2_typeii_spectrum}",
        "Figure 2",
    ),
    (
        r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.88\linewidth}{\centering
\vspace{1.0cm}
\textbf{Figure 3 placeholder.} Upper panel: identical saturation curve $r(\lambda)=\lambda e^{-\lambda m}$ for deterministic and random recovery. Lower panel: static information retention at $\lambda m=1$, showing deterministic $0$ and exponential recovery $\simeq0.06916$.
\vspace{1.0cm}}}
\caption{Equal conventional saturation curves do not imply equal information transfer.}
\label{fig:sameCurve}
\end{figure}""",
        r"\input{figure3_saturation_static_fi}",
        "Figure 3",
    ),
    (
        r"""\begin{figure}[t]
\centering
\fbox{\parbox{0.88\linewidth}{\centering
\vspace{1.0cm}
\textbf{Figure 4 placeholder.} Stem plots for recovery laws A and B with the same mean and variance, plus a compact annotation showing zero versus positive FI for the common event $D\le2/5$.
\vspace{1.0cm}}}
\caption{An exact mean--variance matched counterexample to finite-summary resource completeness.}
\label{fig:varianceNoGo}
\end{figure}""",
        r"\input{figure4_variance_counterexample}",
        "Figure 4",
    ),
]

# Raw strings above contain a single LaTeX backslash despite JSON escaping.
for old, new, label in figures:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} placeholder, found {count}")
    text = text.replace(old, new)

required = [
    r"\usepackage{pgfplots}",
    r"\input{figure1_channel_schematic}",
    r"\input{figure2_typeii_spectrum}",
    r"\input{figure3_saturation_static_fi}",
    r"\input{figure4_variance_counterexample}",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev4 invariant missing: {token}")

# Guard against the prior generator bug that emitted a LaTeX line-break command
# before input rather than the input command itself.
if r"\\input{figure" in text:
    raise RuntimeError("Rev4 generator emitted double-backslash figure input")
if "placeholder" in text:
    raise RuntimeError("A figure placeholder survived Rev4")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
