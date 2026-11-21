"""PCA from scratch — Phase 1 milestone.

Implement principal component analysis via the eigen-decomposition of the
covariance matrix (or, as a stretch, via the SVD of the centered data).

Steps:
  1. Center the data (subtract the column means).
  2. Form the covariance matrix C = (1/(n-1)) Xc^T Xc.
  3. Eigen-decompose C; sort eigenpairs by descending eigenvalue.
  4. Project onto the top-k eigenvectors.

Write-up to produce: explain why the top eigenvectors of the covariance
matrix are the directions of maximum variance, and what the eigenvalues
say about explained variance.
"""

from __future__ import annotations

import numpy as np


def center(X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (X_centered, column_means)."""
    X = np.asarray(X, dtype=float)
    # TODO: means = X.mean(axis=0); return X - means, means
    raise NotImplementedError


def covariance_matrix(X_centered: np.ndarray) -> np.ndarray:
    """Covariance matrix of already-centered data, shape (n_features, n_features)."""
    # TODO: n = X_centered.shape[0]; return (X_centered.T @ X_centered) / (n - 1)
    raise NotImplementedError


def pca(X: np.ndarray, n_components: int) -> dict:
    """Fit PCA and return components, explained variance, and the projection.

    Returns a dict with keys:
        'components'            -> (n_components, n_features) top eigenvectors (rows)
        'explained_variance'    -> (n_components,) eigenvalues, descending
        'explained_variance_ratio' -> fraction of total variance per component
        'mean'                  -> feature means used for centering
        'projection'            -> (n_samples, n_components) transformed data
    Use np.linalg.eigh (covariance is symmetric) and remember eigh returns
    eigenvalues in ASCENDING order — reverse them.
    """
    # TODO:
    #   Xc, mean = center(X)
    #   C = covariance_matrix(Xc)
    #   eigvals, eigvecs = np.linalg.eigh(C); sort descending
    #   pick top-k; projection = Xc @ components.T
    raise NotImplementedError


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    # Correlated 2-D data stretched along one direction.
    base = rng.normal(size=(300, 1))
    X = np.hstack([base, 0.5 * base + 0.1 * rng.normal(size=(300, 1))])
    result = pca(X, n_components=2)
    print("explained variance ratio:", np.round(result["explained_variance_ratio"], 3))
