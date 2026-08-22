from pathlib import Path

path = Path("energy_survival_temporal_fisher_rev7_prxq.tex")
text = path.read_text(encoding="utf-8")


def replace_once(old: str, new: str):
    global text
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old!r}"
    text = text.replace(old, new, 1)


# The first Rev7 full build exposed only two overfull lines.  Shorten the
# theorem heading and opening example prose; no equation or claim changes.
replace_once(
    r"\begin{corollary}[Area and first-moment energy corollaries]",
    r"\begin{corollary}[Energy corollaries]",
)
replace_once(
    "The equality family is mathematically extremal, so it is useful to check that the survival ceiling is also informative for a nonextremal photon wavepacket.  Single-photon time--frequency variables and quantum-limited arrival-time measurements are standard quantum-optical settings~\\cite{FabreKellerMilman2022,FolgeEtAl2026}.",
    "As a nonextremal check, consider a single-photon wavepacket.  Single-photon time--frequency variables and quantum-limited arrival-time measurements are established quantum-optical settings~\\cite{FabreKellerMilman2022,FolgeEtAl2026}.",
)

# Make the phase convention behind the Hellinger-affinity timing formula
# explicit: this concrete photon is transform-limited with zero spectral phase.
replace_once(
    "Consider a Gaussian spectral density centered one Gaussian width above the active edge and truncated only by semiboundedness,",
    "Take a transform-limited photon with zero spectral phase, $\\psi(\\Omega)=\\sqrt{q_\\sigma(\\Omega)}$, and Gaussian spectral density centered one Gaussian width above the active edge and truncated only by semiboundedness,",
)

assert r"\begin{corollary}[Energy corollaries]" in text
assert "As a nonextremal check" in text
assert "transform-limited photon with zero spectral phase" in text
path.write_text(text, encoding="utf-8")
print(f"Repaired {path}")
