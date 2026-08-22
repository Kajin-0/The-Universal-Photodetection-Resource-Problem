from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev7_prxq.tex")
dst = Path("energy_survival_temporal_fisher_rev8_prxq.tex")

text = src.read_text(encoding="utf-8")

old = (
    "The central result can be read directly from Eq.~\\eqref{eq:survival-law}: retaining phase-averaged two-quadrature temporal Fisher information at angular frequency $\\nu$ requires surviving spectral probability above an excess-frequency gap $\\nu$ from the participating lower edge.  The additive edge itself is irrelevant; the resource is excitation energy above that edge.  A uniform guarantee over all sinusoidal phases is a stronger requirement and therefore obeys the same bound."
)
new = old + (
    "  The theorem is local in the waveform-perturbation parameters: it bounds Fisher information at the uniform random-time baseline and does not by itself constitute a global finite-amplitude estimation-error or risk bound."
)

count = text.count(old)
assert count == 1, f"Expected exactly one discussion anchor, found {count}"
text = text.replace(old, new, 1)

assert "does not by itself constitute a global finite-amplitude estimation-error or risk bound" in text
assert r"\section{Controlled periodic-to-continuum survival law}" in text
assert r"\section{Nonextremal single-photon wavepacket}" in text
assert r"\documentclass[aps,prx," in text
assert r"\boxed{" not in text

dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
