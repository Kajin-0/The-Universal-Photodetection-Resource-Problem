#!/usr/bin/env python3
"""Numerical validator for WP23 prescribed boundary 2-jet implementation cost.

Checks random finite-dimensional globally stationary examples with:
- one support state and a two-dimensional kernel sector per energy shell;
- random energy-preserving pure-boundary tangents D_x,D_y;
- random PSD excess kernel curvature S commuting with H_T;
- an explicit energy-adapted purification plus orthogonal ancilla flags.

The construction must satisfy
  d_j rho = D_j,
  C_Delta = prescribed kernel Laplacian,
  V_impl = Tr(C_Delta)/2,
  [K_j,H_tot]=0.
"""

from __future__ import annotations

import numpy as np


def ptr_env(op: np.ndarray, d_t: int, d_e: int) -> np.ndarray:
    arr = op.reshape(d_t, d_e, d_t, d_e)
    return np.einsum("teue->tu", arr)


def run_trial(seed: int) -> None:
    rng = np.random.default_rng(seed)
    energies = [0.0, 1.0, 2.0]
    d_t = 9
    h_t_diag = np.repeat(energies, 3)
    p_idx = [0, 3, 6]
    q_idx = [i for i in range(d_t) if i not in p_idx]

    weights = rng.random(3)
    weights /= weights.sum()

    rho = np.zeros((d_t, d_t), dtype=complex)
    rho_plus = np.zeros_like(rho)
    P = np.zeros_like(rho)
    Q = np.zeros_like(rho)
    for w, p in zip(weights, p_idx):
        rho[p, p] = w
        rho_plus[p, p] = 1.0 / w
        P[p, p] = 1.0
    for q in q_idx:
        Q[q, q] = 1.0

    tangents: list[np.ndarray] = []
    cmins: list[np.ndarray] = []
    for _ in range(2):
        D = np.zeros_like(rho)
        for shell, p in enumerate(p_idx):
            qs = [3 * shell + 1, 3 * shell + 2]
            vec = rng.normal(size=2) + 1j * rng.normal(size=2)
            for q, z in zip(qs, vec):
                D[q, p] = z
                D[p, q] = z.conjugate()
        tangents.append(D)
        K_red = Q @ D @ P
        cmins.append(2.0 * K_red @ rho_plus @ K_red.conj().T)

    c_min = cmins[0] + cmins[1]

    # Arbitrary positive excess curvature, block diagonal in target energy.
    S = np.zeros_like(rho)
    for shell in range(3):
        qs = [3 * shell + 1, 3 * shell + 2]
        X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        block = 0.1 * (X @ X.conj().T)
        S[np.ix_(qs, qs)] = block
    c_target = c_min + 2.0 * S

    # Purification ancilla: 3 baseline Schmidt flags plus one fresh flag for
    # each eigenvector in the excess-curvature purification.
    flag_data: list[tuple[int, float, np.ndarray]] = []
    for shell in range(3):
        qs = [3 * shell + 1, 3 * shell + 2]
        vals, vecs = np.linalg.eigh(S[np.ix_(qs, qs)])
        for k, val in enumerate(vals):
            if val > 1e-13:
                tv = np.zeros(d_t, dtype=complex)
                tv[qs] = vecs[:, k]
                flag_data.append((shell, float(val), tv))

    d_e = 3 + len(flag_data)
    e_star = 10.0
    h_e_diag = np.empty(d_e)
    for a, shell in enumerate(range(3)):
        h_e_diag[a] = e_star - energies[shell]
    for a, (shell, _, _) in enumerate(flag_data, start=3):
        h_e_diag[a] = e_star - energies[shell]

    dim = d_t * d_e
    omega = np.zeros(dim, dtype=complex)
    for a, (w, p) in enumerate(zip(weights, p_idx)):
        omega[p * d_e + a] = np.sqrt(w)

    eye_e = np.eye(d_e)
    chi_hor: list[np.ndarray] = []
    for D in tangents:
        C = Q @ D @ P @ rho_plus
        K_hor = 1j * (C - C.conj().T)
        chi_hor.append(-1j * np.kron(K_hor, eye_e) @ omega)

    eta = np.zeros(dim, dtype=complex)
    for a, (_, val, tv) in enumerate(flag_data, start=3):
        for t, z in enumerate(tv):
            eta[t * d_e + a] += np.sqrt(val) * z

    chi = [chi_hor[0] + eta, chi_hor[1]]

    # First derivatives.
    for j, vec in enumerate(chi):
        deriv = ptr_env(
            np.outer(vec, omega.conj()) + np.outer(omega, vec.conj()), d_t, d_e
        )
        np.testing.assert_allclose(deriv, tangents[j], rtol=2e-11, atol=2e-11)

    # Prescribed kernel Laplacian.
    c_rec = 2.0 * sum(
        Q @ ptr_env(np.outer(vec, vec.conj()), d_t, d_e) @ Q for vec in chi
    )
    np.testing.assert_allclose(c_rec, c_target, rtol=2e-11, atol=2e-11)

    # Rank-two Hermitian generators realizing the chosen tangent vectors.
    generators = [
        1j * (np.outer(vec, omega.conj()) - np.outer(omega, vec.conj()))
        for vec in chi
    ]

    v_impl = 0.0
    for K in generators:
        mean = np.vdot(omega, K @ omega)
        second = np.vdot(omega, K @ K @ omega)
        v_impl += float((second - mean * mean).real)
    np.testing.assert_allclose(v_impl, 0.5 * np.trace(c_target).real, rtol=2e-11, atol=2e-11)

    # Exact global energy conservation: all relevant vectors live in one shell.
    h_tot = np.kron(np.diag(h_t_diag), np.eye(d_e)) + np.kron(
        np.eye(d_t), np.diag(h_e_diag)
    )
    np.testing.assert_allclose(h_tot @ omega, e_star * omega, rtol=0, atol=2e-12)
    for K in generators:
        np.testing.assert_allclose(K @ h_tot - h_tot @ K, 0.0, rtol=0, atol=2e-12)


if __name__ == "__main__":
    for seed in range(20):
        run_trial(seed)
    print("WP23 prescribed-2-jet implementation-cost validator: PASS")
