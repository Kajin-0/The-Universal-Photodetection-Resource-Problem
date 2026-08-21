from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev2.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev3.tex")

text = SRC.read_text(encoding="utf-8")

replacements = [
    (
        r"\usepackage{hyperref}",
        r"\usepackage[hidelinks]{hyperref}",
        "hide hyperlink boxes for publication rendering",
    ),
    (
        "The exact numerical spectrum used for Fig.~\\ref{fig:typeIIspectrum} is obtained by the causal Volterra equations recorded in the repository work package WP07. Rev1 leaves the final plotting input external to avoid duplicating validated numerical assets.",
        "The exact numerical spectrum used for Fig.~\\ref{fig:typeIIspectrum} is obtained from the causal Volterra renewal equations given in the underlying derivation; the numerical values quoted in the main text are validation rather than premises of the theorem.",
        "remove internal Rev1 drafting language",
    ),
    (
        "because $\\E[D]<\\infty$. Square-root likelihood localization then passes DQM to the unbounded stopping time with score $S_{\\rm cyc}=M_D$ and information $\\lambda\\E[D]$. A final manuscript revision should attach a theorem-grade counting-process likelihood citation to this standard localization step.",
        "because $\\E[D]<\\infty$. Square-root likelihood localization then passes DQM to the unbounded stopping time with score $S_{\\rm cyc}=M_D$ and information $\\lambda\\E[D]$. This stopped counting-process likelihood and martingale-localization framework is standard; see, e.g., Refs.~\\cite{AndersenBorganGillKeiding1993,Jacobsen2006}.",
        "replace internal TODO with theorem-grade references",
    ),
]

for old, new, label in replacements:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one target for {label}, found {count}")
    text = text.replace(old, new)

required = [
    r"\usepackage[hidelinks]{hyperref}",
    r"u_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
    r"G_1(\omega)>0\qquad\text{for every }\omega\neq0",
    r"\cite{AndersenBorganGillKeiding1993,Jacobsen2006}",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev3 invariant missing: {token}")

for forbidden in ["Figure 1 placeholder", "Figure 2 placeholder", "Figure 3 placeholder", "Figure 4 placeholder"]:
    # Placeholders are intentionally retained until final figure assets are generated.
    if forbidden not in text:
        raise RuntimeError(f"Expected figure placeholder missing unexpectedly: {forbidden}")

for forbidden in ["Rev1 leaves", "A final manuscript revision should"]:
    if forbidden in text:
        raise RuntimeError(f"Internal drafting language survived Rev3: {forbidden}")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
