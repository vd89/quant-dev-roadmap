"""Tests for linear_regression. These pass once the stubs are implemented."""

import numpy as np
import pytest

from src import linear_regression as lr


@pytest.fixture
def data():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(500, 3))
    true_w = np.array([2.0, -1.0, 0.5, 3.0])  # intercept + 3 weights
    y = true_w[0] + X @ true_w[1:] + rng.normal(scale=0.05, size=500)
    return X, y, true_w


def test_add_intercept_shape():
    X = np.ones((4, 2))
    Xb = lr.add_intercept(X)
    assert Xb.shape == (4, 3)
    assert np.allclose(Xb[:, 0], 1.0)


def test_normal_equations_recovers_weights(data):
    X, y, true_w = data
    w = lr.fit_normal_equations(X, y)
    assert np.allclose(w, true_w, atol=0.05)


def test_gradient_descent_matches_normal_equations(data):
    X, y, _ = data
    w_ne = lr.fit_normal_equations(X, y)
    w_gd, hist = lr.fit_gradient_descent(X, y, lr=0.05, n_iters=20_000)
    assert np.allclose(w_gd, w_ne, atol=0.02)
    assert hist[-1] < hist[0]  # loss decreased
