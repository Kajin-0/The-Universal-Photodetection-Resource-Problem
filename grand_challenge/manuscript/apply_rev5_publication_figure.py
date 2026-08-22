from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev4.tex")
dst = Path("energy_survival_temporal_fisher_rev5.tex")

text = src.read_text(encoding="utf-8")


def replace_once(old: str, new: str):
    global text
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old[:120]!r}"
    text = text.replace(old, new, 1)


# Publication-only visual dependencies and nonintrusive hyperlink rendering.
replace_once(
    r"\usepackage{hyperref}" + "\n",
    r"\usepackage{hyperref}" + "\n"
    r"\usepackage{graphicx}" + "\n"
    r"\usepackage{tikz}" + "\n"
    r"\usetikzlibrary{arrows.meta,positioning}" + "\n"
    r"\hypersetup{hidelinks}" + "\n",
)

# Add one conceptual figure after the Introduction's explicit source-class
# boundary.  It visualizes the parameter-entry point, arbitrary downstream
# parameter-independent processing, the operational theorem, and the excluded
# arbitrary waveform-synthesis class.
anchor = (
    "We also state the boundary of the theorem explicitly.  If the unknown waveform is allowed to modify the quantum state through a parameter-dependent control map rather than only through a random translation distribution, baseline mean energy is insufficient: infinitesimal high-frequency coherent sidebands can enter the state tangent at first order while their added mean energy is second order.  Any theorem for that broader class must account for the encoding/control resource itself.\n\n"
)
assert anchor in text, "Expected end-of-Introduction scope paragraph not found"

figure = r"""\begin{figure*}[t]
\centering
\resizebox{0.98\textwidth}{!}{\input{figure1_operational_architecture_body.tex}}
\caption{Operational architecture and theorem scope.  The temporal parameter enters through the latent random-time distribution of a fixed excitation.  All subsequent source-to-field dynamics, overlap, detector memory, ancillas, and final measurement are parameter independent and can be absorbed into $\Gamma$, so the accessible record obeys the energy-tail Fisher bound.  Arbitrary parameter-dependent waveform-state synthesis is a different resource class.}
\label{fig:architecture}
\end{figure*}

"""
text = text.replace(anchor, anchor + figure, 1)

# Rev5 is publication engineering only.
assert r"\input{figure1_operational_architecture_body.tex}" in text
assert r"\hypersetup{hidelinks}" in text
assert r"\boxed{" not in text

dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
