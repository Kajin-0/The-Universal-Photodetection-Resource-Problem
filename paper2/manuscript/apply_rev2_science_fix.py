from pathlib import Path

SRC = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev1.tex")
DST = Path(__file__).with_name("fisher_spectra_memory_photodetectors_rev2.tex")

text = SRC.read_text(encoding="utf-8")

old = r"""\begin{equation}
\nu_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)\,dt,
\qquad
W_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)\frac{R(t)}{m}\,dt.
\label{eq:usWs}
\end{equation}"""
new = r"""\begin{equation}
u_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)\,dt,
\qquad
W_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)\frac{R(t)}{m}\,dt.
\label{eq:usWs}
\end{equation}"""
# The replacement above intentionally uses the ordinary Latin symbol u_s,
# not the Greek command \nu_s.  Keep the source target exact so this fails
# loudly if Rev1 changes.
new = new.replace(r"\nu_s", "u_s", 1)

count = text.count(old)
if count != 1:
    raise RuntimeError(f"Expected exactly one u_s notation target, found {count}")

text = text.replace(old, new)

# Guard the core notation introduced by WP27.  These assertions make the
# generator fail loudly if later edits accidentally remove the distinction.
required = [
    r"\newcommand{\GDC}{\mathcal G_{\rm DC}}",
    r"\newcommand{\Gcyc}{\mathcal G_{\rm cyc}}",
    r"\GDC=\Gcyc=\frac{r}{\lambda}I_D",
    r"G_1(\omega)>0\qquad\text{for every }\omega\neq0",
]
for token in required:
    if token not in text:
        raise RuntimeError(f"Required Rev2 invariant missing: {token}")

# Ensure the notation repair really occurred rather than silently replacing
# the target with itself.
if r"\nu_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)" in text:
    raise RuntimeError("Rev2 notation repair failed: Greek \\nu_s still present")
if r"u_s=\int_0^\infty e^{-st}U_{\lambda_*}(t)" not in text:
    raise RuntimeError("Rev2 notation repair failed: Latin u_s not present")

DST.write_text(text, encoding="utf-8")
print(f"Wrote {DST.name}")
