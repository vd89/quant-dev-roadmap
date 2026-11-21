"""Tests for monte_carlo. These pass once the stubs are implemented."""

import numpy as np

from src import monte_carlo as mc


def test_estimate_pi_close():
    rng = np.random.default_rng(0)
    est = mc.estimate_pi(200_000, rng)
    assert abs(est - np.pi) < 0.05


def test_mc_expectation_normal_second_moment():
    rng = np.random.default_rng(0)
    est, se = mc.mc_expectation(
        g=lambda x: x**2,
        sampler=lambda n: rng.normal(size=n),
        n_samples=200_000,
    )
    assert abs(est - 1.0) < 0.05  # E[X^2] = 1 for N(0,1)
    assert se > 0


def test_convergence_error_decreases():
    rng = np.random.default_rng(0)
    results = mc.convergence_study(n_grid=[100, 100_000], rng=rng)
    err_small_n = results[0][1]
    err_large_n = results[-1][1]
    assert err_large_n < err_small_n
