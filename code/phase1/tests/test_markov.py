"""Tests for markov. These pass once the stubs are implemented."""

import numpy as np

from src import markov


def test_random_walk_length_and_steps():
    rng = np.random.default_rng(0)
    walk = markov.random_walk(1_000, p_up=0.5, rng=rng)
    assert walk.shape == (1_000,)
    # Every step changes position by exactly 1.
    diffs = np.diff(np.concatenate([[0], walk]))
    assert set(np.unique(diffs)).issubset({-1, 1})


def test_analytic_stationary_is_fixed_point():
    P = np.array([
        [0.1, 0.6, 0.3],
        [0.4, 0.4, 0.2],
        [0.3, 0.3, 0.4],
    ])
    pi = markov.analytic_stationary(P)
    assert np.isclose(pi.sum(), 1.0)
    assert np.all(pi >= -1e-9)
    assert np.allclose(pi @ P, pi, atol=1e-8)  # pi is stationary


def test_empirical_matches_analytic():
    rng = np.random.default_rng(0)
    P = np.array([
        [0.1, 0.6, 0.3],
        [0.4, 0.4, 0.2],
        [0.3, 0.3, 0.4],
    ])
    traj = markov.simulate_chain(P, n_steps=300_000, rng=rng)
    emp = markov.empirical_stationary(traj, n_states=3, burn_in=2_000)
    ana = markov.analytic_stationary(P)
    assert np.allclose(emp, ana, atol=0.02)
