"""Random walks & Markov chains — Phase 1 milestone.

Implement:
  1. A 1-D random walk simulation.
  2. A finite Markov chain: simulate trajectories and estimate the
     stationary distribution two ways —
       (a) empirically, from long-run state frequencies, and
       (b) analytically, as the left eigenvector of P with eigenvalue 1.
  Confirm the two agree.

Write-up to produce: explain what a stationary distribution is, the
condition P^T pi = pi, and why an irreducible aperiodic chain converges
to it regardless of the start state.
"""

from __future__ import annotations

import numpy as np


def random_walk(n_steps: int, p_up: float = 0.5,
                rng: np.random.Generator | None = None) -> np.ndarray:
    """Simulate a 1-D random walk; return the position after each step.

    Each step is +1 with probability p_up, else -1. Output length n_steps
    (the cumulative position), starting from 0.
    """
    rng = rng or np.random.default_rng()
    # TODO: steps = where(rng.random(n_steps) < p_up, +1, -1); return cumsum
    raise NotImplementedError


def simulate_chain(P: np.ndarray, n_steps: int, start: int = 0,
                   rng: np.random.Generator | None = None) -> np.ndarray:
    """Simulate a Markov chain with transition matrix P.

    P[i, j] = probability of moving from state i to state j (rows sum to 1).
    Returns an array of visited state indices of length n_steps.
    """
    rng = rng or np.random.default_rng()
    P = np.asarray(P, dtype=float)
    # TODO:
    #   state = start; for each step sample next state from P[state]
    #   (np.searchsorted on the row's cumulative sum is a clean way)
    raise NotImplementedError


def empirical_stationary(states: np.ndarray, n_states: int,
                         burn_in: int = 0) -> np.ndarray:
    """Estimate the stationary distribution from visit frequencies.

    Drop the first `burn_in` states, then count how often each state appears.
    """
    # TODO: counts = np.bincount(states[burn_in:], minlength=n_states); normalise
    raise NotImplementedError


def analytic_stationary(P: np.ndarray) -> np.ndarray:
    """Stationary distribution as the normalized left eigenvector of P.

    Solve pi P = pi  <=>  P^T pi = pi, i.e. the eigenvector of P^T for
    eigenvalue 1. Take the real part, make it non-negative, and normalize
    to sum to 1.
    """
    # TODO:
    #   vals, vecs = np.linalg.eig(P.T)
    #   pick the eigenvector whose eigenvalue is closest to 1
    #   normalise so it sums to 1
    raise NotImplementedError


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    P = np.array([
        [0.1, 0.6, 0.3],
        [0.4, 0.4, 0.2],
        [0.3, 0.3, 0.4],
    ])
    traj = simulate_chain(P, n_steps=200_000, rng=rng)
    emp = empirical_stationary(traj, n_states=3, burn_in=1_000)
    ana = analytic_stationary(P)
    print("empirical :", np.round(emp, 3))
    print("analytic  :", np.round(ana, 3))
