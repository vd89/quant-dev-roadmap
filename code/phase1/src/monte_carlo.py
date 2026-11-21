"""Monte Carlo estimation — Phase 1 milestone.

Two estimators plus a convergence study:
  1. Estimate pi by sampling points in the unit square.
  2. Estimate E[g(X)] for X ~ Uniform or Normal.
  3. Show the error shrinks like O(1/sqrt(N)) and report a standard error.

Write-up to produce: explain why Monte Carlo error scales as 1/sqrt(N)
(independent of dimension), and how the standard error is estimated from
the sample variance.
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np


def estimate_pi(n_samples: int, rng: np.random.Generator | None = None) -> float:
    """Estimate pi by the fraction of random points falling in the unit circle.

    Sample (x, y) uniformly in [0, 1]^2; the fraction with x^2 + y^2 <= 1
    approximates pi/4.
    """
    rng = rng or np.random.default_rng()
    # TODO:
    #   draw points, count inside the quarter circle, return 4 * inside / n
    raise NotImplementedError


def mc_expectation(
    g: Callable[[np.ndarray], np.ndarray],
    sampler: Callable[[int], np.ndarray],
    n_samples: int,
) -> tuple[float, float]:
    """Estimate E[g(X)] and its standard error.

    `sampler(n)` returns n draws of X; `g` maps samples to values.
    Returns (estimate, standard_error) where
        standard_error = sample_std(g(X)) / sqrt(n).
    """
    # TODO:
    #   samples = sampler(n_samples); vals = g(samples)
    #   est = mean(vals); se = std(vals, ddof=1) / sqrt(n_samples)
    raise NotImplementedError


def convergence_study(
    n_grid: list[int] | None = None,
    rng: np.random.Generator | None = None,
) -> list[tuple[int, float]]:
    """Return [(N, abs_error_vs_pi), ...] to plot error against sample size.

    Expect the error to fall roughly like 1/sqrt(N).
    """
    rng = rng or np.random.default_rng(0)
    n_grid = n_grid or [10, 100, 1_000, 10_000, 100_000]
    # TODO: for each N, estimate pi and record abs(estimate - np.pi)
    raise NotImplementedError


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    print("pi estimate:", estimate_pi(100_000, rng))
    # E[X^2] for X ~ N(0,1) is 1.0
    est, se = mc_expectation(
        g=lambda x: x**2,
        sampler=lambda n: rng.normal(size=n),
        n_samples=100_000,
    )
    print(f"E[X^2] ~ {est:.4f} +/- {se:.4f}")
    for n, err in convergence_study(rng=rng):
        print(f"N={n:>7}  |error|={err:.5f}")
