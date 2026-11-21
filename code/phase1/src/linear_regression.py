"""Linear regression from scratch — Phase 1 milestone.

Implement ordinary least squares two ways and confirm they agree:
  1. Closed form via the normal equations:  w = (XᵀX)⁻¹ Xᵀy
  2. Batch gradient descent on the mean squared error.

Rules of the exercise:
  - Only NumPy for array math. No scikit-learn for the fit itself.
  - Add an intercept by prepending a column of ones to X.

Write-up to produce (see milestone): explain why the normal-equations
solution minimizes the MSE, and when gradient descent is preferable
(large n/p, no matrix inverse, online updates).
"""

from __future__ import annotations

import numpy as np


def add_intercept(X: np.ndarray) -> np.ndarray:
    """Prepend a column of ones so the model can fit a bias term.

    X has shape (n_samples, n_features) -> returns (n_samples, n_features + 1).
    """
    X = np.asarray(X, dtype=float)
    # TODO: return np.hstack([ones_column, X])
    raise NotImplementedError


def fit_normal_equations(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Solve for weights with the normal equations.

    Returns a weight vector of shape (n_features + 1,) including the intercept.
    Prefer np.linalg.solve(XtX, Xty) over explicitly inverting XtX.
    """
    # TODO:
    #   Xb = add_intercept(X)
    #   solve (Xb.T @ Xb) w = Xb.T @ y
    raise NotImplementedError


def fit_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.01,
    n_iters: int = 10_000,
) -> tuple[np.ndarray, list[float]]:
    """Fit by batch gradient descent on the MSE.

    Returns (weights, loss_history). The MSE gradient w.r.t. w is:
        g = (2 / n) * Xbᵀ (Xb w - y)
    Record the loss each iteration so you can plot convergence.
    """
    # TODO:
    #   Xb = add_intercept(X); initialise w = zeros
    #   loop: predictions, error, gradient, w -= lr * gradient, append mse
    raise NotImplementedError


def predict(X: np.ndarray, w: np.ndarray) -> np.ndarray:
    """Predict targets for X given fitted weights (with intercept)."""
    # TODO: return add_intercept(X) @ w
    raise NotImplementedError


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean squared error."""
    # TODO: return float(np.mean((y_true - y_pred) ** 2))
    raise NotImplementedError


if __name__ == "__main__":
    # Smoke test on synthetic data once the functions are implemented.
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 3))
    true_w = np.array([2.0, -1.0, 0.5, 3.0])  # [intercept, w1, w2, w3]
    y = true_w[0] + X @ true_w[1:] + rng.normal(scale=0.1, size=200)

    w_ne = fit_normal_equations(X, y)
    w_gd, hist = fit_gradient_descent(X, y)
    print("normal eqs :", np.round(w_ne, 3))
    print("grad descent:", np.round(w_gd, 3))
    print("final GD loss:", hist[-1])
