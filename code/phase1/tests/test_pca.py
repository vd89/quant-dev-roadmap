"""Tests for pca. These pass once the stubs are implemented."""

import numpy as np

from src import pca


def test_explained_variance_ratio_sums_to_one():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(300, 4))
    result = pca.pca(X, n_components=4)
    assert np.isclose(result["explained_variance_ratio"].sum(), 1.0, atol=1e-6)


def test_first_component_captures_dominant_direction():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(400, 1))
    # Variance concentrated along the first axis.
    X = np.hstack([5.0 * base, 0.1 * rng.normal(size=(400, 1))])
    result = pca.pca(X, n_components=2)
    ratio = result["explained_variance_ratio"]
    assert ratio[0] > 0.9
    assert result["projection"].shape == (400, 2)


def test_components_are_orthonormal():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(200, 3))
    comps = pca.pca(X, n_components=3)["components"]
    gram = comps @ comps.T
    assert np.allclose(gram, np.eye(3), atol=1e-6)
