from __future__ import annotations

import json
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from common import OUT, save, setup

STEM = "fig3_support_survival_synthesis_crossover"

def rlin(p):
    return math.sqrt(p*(1.0-p)) / (1.0-2.0*p)

def locked_values():
    vals = {
        "Rlin_p0p15": rlin(0.15),
        "Rlin_p0p05": rlin(0.05),
        "Rlin_p0p01": rlin(0.01),
        "boundary_curvature": 4.0,
    }
    assert abs(vals["Rlin_p0p15"] - 0.510102030610) < 1e-12
    assert abs(vals["Rlin_p0p05"] - 0.242161052419) < 1e-12
    assert abs(vals["Rlin_p0p01"] - 0.101529330317) < 1e-12
    return vals

def main():
    setup()
    vals = locked_values()

    fig, ax = plt.subplots(2, 2, figsize=(7.2, 5.3), constrained_layout=True)

    a = ax[0, 0]
    a.set_xlim(-0.2, 2.2)
    a.set_ylim(-0.05, 1.05)
    a.bar([0, 1], [0.85, 0.15], width=0.55, color=["0.18", "0.72"], edgecolor="black")
    a.text(0, 0.89, r"$1-p$", ha="center", fontsize=7.5)
    a.text(1, 0.19, r"$p>0$", ha="center", fontsize=7.5)
    a.text(1.72, 0.58, r"$p\rightarrow0^+$", ha="center", fontsize=8.0)
    a.annotate("", xy=(1.95, 0.18), xytext=(1.48, 0.18),
               arrowprops={"arrowstyle":"->","lw":1.0,"color":"0.2"})
    a.plot([2.0], [0.0], marker="o", mfc="white", mec="black", ms=6)
    a.text(2.0, 0.08, "empty sideband", ha="center", fontsize=7.0)
    a.set_xticks([0, 1], [r"carrier $|c\rangle$", r"sideband $|s\rangle$"])
    a.set_yticks([])
    a.set_title("(a) Pre-existing support to boundary")
    for s in ["left","right","top"]:
        a.spines[s].set_visible(False)

    a = ax[0, 1]
    a.set_aspect("equal")
    a.set_xlim(-0.60, 0.60)
    a.set_ylim(-0.60, 0.60)
    radii = [(0.15, vals["Rlin_p0p15"], "0.20", "-"),
             (0.05, vals["Rlin_p0p05"], "0.45", "--"),
             (0.01, vals["Rlin_p0p01"], "0.68", ":")]
    for p, R, col, ls in radii:
        a.add_patch(Circle((0,0), R, fill=False, ec=col, lw=1.6, ls=ls,
                           label=rf"$p={p:.2f}$, $R_{{\rm lin}}={R:.3f}$"))
    a.plot(0,0,"ko",ms=2.8)
    a.axhline(0, color="0.85", lw=0.6)
    a.axvline(0, color="0.85", lw=0.6)
    a.set(xlabel=r"$x$", ylabel=r"$y$")
    a.set_title("(b) Affine physical radius collapses")
    a.legend(frameon=False, loc="lower left", bbox_to_anchor=(-0.04, -0.02), fontsize=6.8)
    a.text(0.28, 0.47, r"$R_{\rm lin}\to0$", fontsize=7.5)

    a = ax[1, 0]
    p = np.linspace(1e-4, 0.24, 800)
    y = 4.0*(1.0-2.0*p)**2/(1.0-p)
    a.plot(p, y, color="black")
    a.axhline(4.0, color="0.50", ls="--", lw=1.0,
              label=r"$\Delta P_s(0)=4$")
    a.plot([0], [4], marker="o", mfc="white", mec="black", ms=5, clip_on=False)
    a.set(xlim=(0, 0.24), ylim=(1.1, 4.18), xlabel=r"sideband seed $p$",
          ylabel=r"$4p/R_{\rm lin}^2$")
    a.set_title("(c) Survival resource approaches synthesis curvature")
    a.legend(frameon=False, loc="lower left")
    a.annotate(r"$p\to0^+$", xy=(0.005, 3.96), xytext=(0.065, 3.45),
               arrowprops={"arrowstyle":"->","lw":0.8,"color":"0.25"}, fontsize=7.2)

    a = ax[1, 1]
    a.set_xlim(0, 1)
    a.set_ylim(0, 1)
    a.axis("off")
    box_kw = dict(boxstyle="round,pad=0.02,rounding_size=0.01", fc="white", ec="0.25", lw=0.9)
    boxes = [
        (0.05, 0.68, 0.42, 0.22, "Baseline + tangent\ntomography", r"$R_{\rm lin}$"),
        (0.53, 0.68, 0.42, 0.22, "Zero-seed quadratic\npopulation fit", r"$\Delta P_s(0)$"),
        (0.29, 0.15, 0.42, 0.22, "Phase-sensitive\nlikelihood", r"$\mathrm{Tr}\,F$"),
    ]
    for x, y0, w, h, title, out in boxes:
        a.add_patch(FancyBboxPatch((x,y0),w,h, **box_kw))
        a.text(x+w/2, y0+h*0.63, title, ha="center", va="center", fontsize=7.0)
        a.text(x+w/2, y0+h*0.22, out, ha="center", va="center", fontsize=8.0)
    a.annotate("", xy=(0.50,0.40), xytext=(0.26,0.66),
               arrowprops={"arrowstyle":"->","lw":0.8,"color":"0.35"})
    a.annotate("", xy=(0.50,0.40), xytext=(0.74,0.66),
               arrowprops={"arrowstyle":"->","lw":0.8,"color":"0.35"})
    a.text(0.50, 0.44, "independent comparison", ha="center", fontsize=7.0)
    a.set_title("(d) Noncircular falsification protocol")

    for a in ax.flat[:3]:
        a.tick_params(direction="out", length=3)
        a.spines["top"].set_visible(False)
        a.spines["right"].set_visible(False)

    fig.suptitle(r"Visualization path $a_p=1-p,\ \sigma_p=0,\ q=\kappa=1$; theorem permits stationary inert spectators",
                 fontsize=9.0)
    save(fig, STEM)
    plt.close(fig)
    (OUT / f"{STEM}_locked.json").write_text(json.dumps(vals, indent=2, sort_keys=True) + "\n")
    return vals

if __name__ == "__main__":
    main()
