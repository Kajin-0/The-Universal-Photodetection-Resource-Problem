from __future__ import annotations

from pathlib import Path
import matplotlib as mpl
mpl.use("Agg")

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "generated"

def setup():
    OUT.mkdir(parents=True, exist_ok=True)
    mpl.rcParams.update({
        "font.family": "DejaVu Serif",
        "font.size": 8.5,
        "axes.titlesize": 9.0,
        "axes.labelsize": 8.5,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.2,
        "lines.linewidth": 1.5,
        "axes.linewidth": 0.8,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

def save(fig, stem: str):
    pdf = OUT / f"{stem}.pdf"
    png = OUT / f"{stem}.png"
    pdf_meta = {
        "Title": stem,
        "Author": "Paper-4 deterministic figure generator",
        "Creator": "matplotlib",
        "CreationDate": None,
        "ModDate": None,
    }
    fig.savefig(pdf, bbox_inches="tight", metadata=pdf_meta)
    fig.savefig(
        png,
        dpi=300,
        bbox_inches="tight",
        metadata={"Software": "matplotlib", "Title": stem},
    )
    return pdf, png
