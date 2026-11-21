# Phase 1 — Math Milestone Starter Code

Starter stubs for the four [Phase 1 milestones](../../math/phase-1-math-plan.md).
Each module has `TODO` markers and a `raise NotImplementedError` where you
write the implementation. Tests are already written — make them pass.

## Layout

```
code/phase1/
├── src/
│   ├── linear_regression.py   # normal equations + gradient descent
│   ├── monte_carlo.py         # pi estimate, E[g(X)], convergence study
│   ├── pca.py                 # PCA via covariance eigen-decomposition
│   └── markov.py              # random walk + stationary distribution
└── tests/                     # pytest suite (red until you implement)
```

## Setup

```bash
cd code/phase1
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Workflow

1. Pick a module (start with `linear_regression.py`).
2. Implement each function where it says `TODO` / `NotImplementedError`.
3. Run its tests until green:

```bash
pytest tests/test_linear_regression.py -v
```

4. Run the module directly to see the smoke test:

```bash
python -m src.linear_regression
```

5. Write the short explanation called for in each module's docstring, then
   commit.

## Milestone checklist

- [ ] `linear_regression` — normal equations and gradient descent agree
- [ ] `monte_carlo` — pi estimate + convergence (error ~ 1/sqrt(N)) + standard error
- [ ] `pca` — explained-variance ratios, orthonormal components
- [ ] `markov` — empirical stationary distribution matches the analytic one
- [ ] Written notes: CLT, Bayes, eigen-decomposition, stationary distributions

Run the whole suite with `pytest -v` from this directory.
