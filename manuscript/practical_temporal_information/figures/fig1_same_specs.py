from __future__ import annotations

import json
import math
import numpy as np
import matplotlib.pyplot as plt

from common import OUT, save, setup

STEM = "fig1_same_specs_different_information"

def locked_values():
    x_half = math.sqrt((22.0 + math.sqrt(489.0)) / 5.0)
    vals = {
        "H2_at_fc": 0.5,
        "SA_at_dc": 1.0,
        "SB_at_dc": 1.0,
        "JA_at_fc": 0.5,
        "JB_at_fc": 13.0 / 6.0,
        "JB_over_JA_at_fc": 13.0 / 3.0,
        "half_fi_x": x_half,
    }
    assert abs(x_half - 2.970297775897) < 1e-12
    return vals

def main():
    setup()
    vals = locked_values()

    u = np.linspace(0.0, 4.0, 1001)
    H2 = 1.0 / (1.0 + u**2)
    SA = np.ones_like(u)
    SB = 0.2 + 0.8 / (1.0 + 25.0 * u**2)
    JA = H2 / SA
    JB = H2 / SB

    i1 = np.argmin(np.abs(u - 1.0))
    assert abs(H2[i1] - vals["H2_at_fc"]) < 1e-15
    assert abs(SA[0] - vals["SA_at_dc"]) < 1e-15
    assert abs(SB[0] - vals["SB_at_dc"]) < 1e-15
    assert abs(JA[i1] - vals["JA_at_fc"]) < 1e-15
    assert abs(JB[i1] - vals["JB_at_fc"]) < 1e-15
    assert abs((JB[i1] / JA[i1]) - vals["JB_over_JA_at_fc"]) < 1e-15
    xh = vals["half_fi_x"]
    JB_half = (1.0 + 25.0*xh*xh) / ((1.0+xh*xh)*(1.0+5.0*xh*xh))
    assert abs(JB_half - 0.5) < 1e-12

    fig, ax = plt.subplots(1, 3, figsize=(7.2, 2.55), constrained_layout=True)

    ax[0].plot(u, H2, color="black")
    ax[0].axvline(1.0, color="0.55", lw=0.9, ls=":")
    ax[0].axhline(0.5, color="0.72", lw=0.8, ls=":")
    ax[0].set(xlim=(0, 4), ylim=(0, 1.05), xlabel=r"$f/f_c$", ylabel=r"$|H(f)|^2$")
    ax[0].set_title("(a) Identical signal response")
    ax[0].text(1.08, 0.56, r"$|H(f_c)|^2=1/2$", fontsize=7.2)

    ax[1].plot(u, SA, color="black", ls="-", label="Detector A")
    ax[1].plot(u, SB, color="0.30", ls="--", label="Detector B")
    ax[1].axvline(1.0, color="0.55", lw=0.9, ls=":")
    ax[1].set(xlim=(0, 4), ylim=(0, 1.08), xlabel=r"$f/f_c$", ylabel=r"$S_n(f)/S_0$")
    ax[1].set_title("(b) Different noise spectra")
    ax[1].legend(frameon=False, loc="upper right")
    ax[1].text(0.08, 0.86, r"$S_A(0)=S_B(0)$", fontsize=7.2)

    ax[2].plot(u, JA, color="black", ls="-", label=r"$J_A$")
    ax[2].plot(u, JB, color="0.30", ls="--", label=r"$J_B$")
    ax[2].axvline(1.0, color="0.55", lw=0.9, ls=":")
    ax[2].axvline(xh, color="0.72", lw=0.8, ls=":")
    ax[2].set(xlim=(0, 4), ylim=(0, 2.75), xlabel=r"$f/f_c$", ylabel=r"$J(f)/J(0)$")
    ax[2].set_title("(c) Different Fisher spectra")
    ax[2].legend(frameon=False, loc="upper right")
    ax[2].annotate(
        r"$J_B/J_A=13/3$",
        xy=(1.0, 13.0/6.0),
        xytext=(1.48, 1.88),
        arrowprops={"arrowstyle": "->", "lw": 0.8, "color": "0.25"},
        fontsize=7.2,
    )
    ax[2].text(xh + 0.06, 0.57, r"$2.9703\,f_c$", fontsize=7.0, rotation=90, va="bottom")

    for a in ax:
        a.tick_params(direction="out", length=3)
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    save(fig, STEM)
    plt.close(fig)
    (OUT / f"{STEM}_locked.json").write_text(json.dumps(vals, indent=2, sort_keys=True) + "\n")
    return vals

if __name__ == "__main__":
    main()
