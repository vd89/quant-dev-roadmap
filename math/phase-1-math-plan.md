# Phase 1 — Mathematics Study Plan

> Goal: build the mathematical foundation a quant developer needs to **read,
> implement, and reason about** quantitative models — not to become a
> research mathematician. Depth where it pays off, pragmatism everywhere else.
>
> Duration: **8–12 weeks**, ~8–10 focused hours/week.

## Guiding approach

- **Learn by implementing.** For every concept, write code that uses it.
- **Prioritize probability & linear algebra** — they recur most in the work.
- **Keep proofs light** but understand *why* results hold enough to debug them.

---

## Module 1 — Linear Algebra (2–3 weeks)

Core of numerical computing, regression, PCA, and performance work.

Topics:
- Vectors, matrices, matrix multiplication, transpose/inverse.
- Linear systems, Gaussian elimination, LU decomposition.
- Vector spaces, rank, span, basis, orthogonality.
- Eigenvalues/eigenvectors, diagonalization.
- SVD and PCA (dimensionality reduction).
- Positive-definite matrices (covariance matrices).

Resources:
- Gilbert Strang, *Introduction to Linear Algebra* (and his MIT OCW/YouTube lectures).
- 3Blue1Brown — *Essence of Linear Algebra* (intuition).

Implement:
- Matrix class with multiply/transpose/inverse (Python, then C++ in Phase 2).
- Linear regression via the normal equations.
- PCA on a small dataset from scratch.

## Module 2 — Calculus & Multivariable (1–2 weeks)

Topics:
- Derivatives, chain rule, Taylor series.
- Integrals (enough for expectations and densities).
- Partial derivatives, gradients, Jacobians, Hessians.
- Optimization basics: gradient descent, convexity intuition.

Resources:
- MIT OCW 18.01 / 18.02 (single & multivariable calculus).
- 3Blue1Brown — *Essence of Calculus*.

Implement:
- Gradient descent to minimize a simple convex function.
- Numerical vs. analytical derivatives (finite differences).

## Module 3 — Probability (2–3 weeks)

The most important module for quant work.

Topics:
- Sample spaces, events, conditional probability, Bayes' theorem.
- Random variables: discrete & continuous; PMF/PDF/CDF.
- Key distributions: Bernoulli, Binomial, Poisson, Uniform, Normal, Exponential.
- Expectation, variance, covariance, correlation.
- Law of large numbers, central limit theorem.
- Joint/marginal/conditional distributions; independence.
- Moment generating functions (light touch).

Resources:
- Blitzstein & Hwang, *Introduction to Probability* (+ Harvard Stat 110 videos).
- *A First Course in Probability*, Sheldon Ross (problems).

Implement:
- Monte Carlo estimator for π and for an expectation.
- Simulate the CLT (sample means → normal).
- Verify Bayes' theorem numerically on a toy problem.

## Module 4 — Statistics (1–2 weeks)

Topics:
- Estimators, bias/variance, MLE.
- Confidence intervals, hypothesis testing (t-test, p-values) and their limits.
- Linear regression as a statistical model; R², residual analysis.
- Overfitting, bias–variance tradeoff, cross-validation intuition.

Resources:
- Blitzstein/Hwang (overlap), or *All of Statistics*, Wasserman (reference).

Implement:
- Regression with gradient descent AND normal equations; compare.
- A simple bootstrap for a confidence interval.

## Module 5 — Intro to Stochastic Processes (1 week, intro only)

A first exposure — deepened later, not mastered here.

Topics:
- Random walks.
- Markov chains (transition matrices, stationary distributions).
- Brownian motion (intuition) and why it underlies option pricing.

Resources:
- Any accessible intro (e.g. Ross, *Introduction to Probability Models*, early chapters).

Implement:
- Simulate a 1-D random walk and a Markov chain; estimate its stationary distribution.

---

## Phase 1 milestone (exit criteria)

You can move to Phase 2 when you have, on GitHub with short write-ups:

- [ ] A from-scratch **linear regression** (normal equations + gradient descent).
- [ ] A **Monte Carlo** estimator with an error/convergence discussion.
- [ ] A **PCA** implementation on a real small dataset.
- [ ] A **random-walk / Markov-chain** simulation with stationary-distribution estimate.
- [ ] Short notes explaining the CLT, Bayes' theorem, and eigen-decomposition
      in your own words.

## Weekly template

| Day | Focus |
|-----|-------|
| Mon–Tue | New concept (video + reading) |
| Wed–Thu | Problem sets |
| Fri | Implement in code |
| Sat | Write-up + commit |
| Sun | Review + spaced repetition |

_Last updated: 2026-11-21_
