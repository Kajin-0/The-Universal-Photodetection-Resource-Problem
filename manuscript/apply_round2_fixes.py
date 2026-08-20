from pathlib import Path

p = Path(__file__).with_name("event_resource_theorem_draft.tex")
text = p.read_text(encoding="utf-8")

# 1. Typographical build fix in exponential-hazard saturation formula.
text = text.replace(
    r"=rac{\Lambda}{\Omega}\tan^{-1}\left(\frac{\Omega}{\Lambda}\right)",
    r"=\frac{\Lambda}{\Omega}\tan^{-1}\left(\frac{\Omega}{\Lambda}\right)",
)

# 2. Cite standard Poisson marking/displacement theory in the exact-transfer proof.
old = (
    "Independent marking and displacement preserve the Poisson property.  "
    "At $\\theta=0$, the marked output intensity measure is $\\Phi_0\\kappa(dm)$."
)
new = (
    "Independent marking and displacement preserve the Poisson property "
    "\\cite{Kingman1993,DaleyVereJones2003}.  "
    "At $\\theta=0$, the marked output intensity measure is $\\Phi_0\\kappa(dm)$."
)
text = text.replace(old, new)

# 3. Cite harmonic-analysis source at the Wiener step.
text = text.replace(
    "Wiener’s theorem for Fourier transforms of finite measures gives",
    "Wiener’s theorem for Fourier transforms of finite measures \\cite{Katznelson2004} gives",
)

# 4. Clarify source-spectrum scope.
needle = "A scalar bandwidth is not always a natural descriptor of the source task.  Let $w(\\omega)$ be a normalized incident spectral-FI density,"
replacement = (
    "A scalar bandwidth is not always a natural descriptor of the source task.  "
    "For the present theorem we assume the incident spectral Fisher-information measure "
    "is absolutely continuous with respect to Lebesgue measure.  Let $w(\\omega)$ be its "
    "normalized spectral-FI density,"
)
text = text.replace(needle, replacement)

# 5. Clarify the gateway mark-independence condition.
needle = (
    "The first gateway waiting time $T_1\\sim\\mathrm{Exp}(\\lambda_1)$ is independent of the exit destination "
    "and of subsequent autonomous Markov dynamics.  For any accessible downstream mark $M$ and additional delay "
    "$Y_M\\ge0$,"
)
replacement = (
    "The first gateway waiting time $T_1\\sim\\mathrm{Exp}(\\lambda_1)$ is independent of the exit destination "
    "and of subsequent autonomous Markov dynamics.  In this corollary the downstream mark $M$ is assumed not to "
    "contain an independent record of the hidden gateway dwell time itself; if it does, that additional timing record "
    "must be included directly in the general marked-kernel resource accounting.  For any such accessible downstream "
    "mark $M$ and additional delay $Y_M\\ge0$,"
)
text = text.replace(needle, replacement)

# 6. Wire the self-contained rare-fast appendix into the build.
needle = "\\bibliography{references}\n\n\\end{document}"
replacement = (
    "\\appendix\n"
    "\\input{appendix_rare_fast_counterexample}\n\n"
    "\\bibliography{references}\n\n"
    "\\end{document}"
)
text = text.replace(needle, replacement)

p.write_text(text, encoding="utf-8")
print(f"Patched {p}")
