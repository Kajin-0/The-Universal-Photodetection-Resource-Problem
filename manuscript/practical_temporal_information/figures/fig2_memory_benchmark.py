from __future__ import annotations

import json
import numpy as np
import matplotlib.pyplot as plt

from common import OUT, save, setup

STEM = "fig2_same_saturation_different_timestamps"

def moments(x, w):
    mean = float(np.sum(x*w))
    var = float(np.sum((x-mean)**2*w))
    return mean, var

def locked_values():
    xA = np.array([0.5, 1.5])
    wA = np.array([0.5, 0.5])
    xB = np.array([0.25, 1.0, 1.75])
    wB = np.array([2/9, 5/9, 2/9])
    mA, vA = moments(xA, wA)
    mB, vB = moments(xB, wB)
    assert abs(mA-1.0) < 1e-15 and abs(mB-1.0) < 1e-15
    assert abs(vA-0.25) < 1e-15 and abs(vB-0.25) < 1e-15
    vals = {
        "mean_A": mA,
        "mean_B": mB,
        "variance_A": vA,
        "variance_B": vB,
        "cv_A": np.sqrt(vA)/mA,
        "cv_B": np.sqrt(vB)/mB,
        "g2_A_at_0p75m": 0.7274957073,
        "g2_B_at_0p75m": 0.3188717529,
        "g2_ratio_A_over_B": 0.7274957073/0.3188717529,
        "P_short_A": 0.0,
        "P_short_B": 0.024502903710,
        "GZ_A": 0.0,
        "GZ_B": 0.00443520488427,
    }
    assert abs(vals["cv_A"] - 0.5) < 1e-15
    assert abs(vals["cv_B"] - 0.5) < 1e-15
    return vals, xA, wA, xB, wB

def main():
    setup()
    vals, xA, wA, xB, wB = locked_values()

    fig, ax = plt.subplots(2, 2, figsize=(7.2, 5.0), constrained_layout=True)

    a = ax[0, 0]
    for x, w in zip(xA, wA):
        a.vlines(x-0.025, 0, w, color="black", lw=2.0)
        a.plot(x-0.025, w, "o", color="black", ms=4)
    for x, w in zip(xB, wB):
        a.vlines(x+0.025, 0, w, color="0.38", lw=1.7, linestyles="--")
        a.plot(x+0.025, w, "s", mfc="white", mec="0.30", ms=4)
    a.plot([], [], "o-", color="black", label="Law A")
    a.plot([], [], "s--", color="0.38", mfc="white", label="Law B")
    a.set(xlim=(0, 2.0), ylim=(0, 0.64), xlabel=r"Recovery $T/m$", ylabel="Probability")
    a.set_title("(a) Matched recovery moments")
    a.legend(frameon=False, loc="upper right")
    a.text(0.05, 0.58, r"$\mathbb{E}[T/m]=1,\ \mathrm{Var}(T/m)=1/4$", fontsize=7.2)

    a = ax[0, 1]
    rho = np.linspace(0, 3.0, 600)
    rm = rho*np.exp(-rho)
    a.plot(rho, rm, color="black", ls="-", label="Law A")
    a.plot(rho, rm, color="0.38", ls="--", label="Law B")
    a.axvline(1.0, color="0.60", ls=":", lw=0.9)
    a.set(xlim=(0, 3), ylim=(0, 0.40), xlabel=r"$\rho=\lambda m$", ylabel=r"$r\,m$")
    a.set_title("(b) Exactly identical saturation")
    a.legend(frameon=False, loc="upper right")
    a.text(1.05, 0.34, r"$r m=\rho e^{-\rho}$", fontsize=7.2)

    a = ax[1, 0]
    g = [vals["g2_A_at_0p75m"], vals["g2_B_at_0p75m"]]
    a.bar([0, 1], g, width=0.55, color=["0.15", "0.75"], edgecolor="black")
    a.set_xticks([0, 1], ["Law A", "Law B"])
    a.set(ylim=(0, 0.82), ylabel=r"$g^{(2)}(0.75m)$")
    a.set_title("(c) Timestamp correlation separates them")
    a.text(0.5, 0.77, f"A/B = {vals['g2_ratio_A_over_B']:.2f}", ha="center", fontsize=7.4)
    for i, y in enumerate(g):
        a.text(i, y+0.025, f"{y:.3f}", ha="center", fontsize=7.2)

    a = ax[1, 1]
    G = [vals["GZ_A"], vals["GZ_B"]]
    a.bar([0, 1], G, width=0.55, color=["0.15", "0.75"], edgecolor="black")
    a.set_xticks([0, 1], ["Law A", "Law B"])
    a.set(ylim=(0, 0.0052), ylabel=r"$G_Z$")
    a.set_title("(d) One-bit interval FI witness")
    a.text(0, 0.00018, "0", ha="center", fontsize=7.2)
    a.text(1, G[1]+0.00016, rf"${G[1]:.4g}$", ha="center", fontsize=7.2)
    a.text(
        0.5, 0.00465,
        r"$Z=\mathbf{1}\{D\leq0.4m\}$" + "\n" +
        rf"$P_A=0,\quad P_B={vals['P_short_B']:.4f}$",
        ha="center", va="top", fontsize=7.1
    )

    for a in ax.flat:
        a.tick_params(direction="out", length=3)
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    fig.suptitle("Frozen companion benchmark: identical saturation, different timestamp information",
                 fontsize=9.2)
    save(fig, STEM)
    plt.close(fig)
    (OUT / f"{STEM}_locked.json").write_text(json.dumps(vals, indent=2, sort_keys=True) + "\n")
    return vals

if __name__ == "__main__":
    main()
