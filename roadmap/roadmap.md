# Quant Developer Roadmap

> Goal: become a hireable **quantitative developer** — strong software
> engineering, solid quantitative/math foundations, and enough finance to
> work credibly alongside quant researchers and traders.

## What a quant developer actually does

Quant developers build and maintain the software that researchers and
traders rely on: backtesting engines, data pipelines, pricing/risk
libraries, execution and order-management systems, and low-latency
infrastructure. The role is **engineering-first** with quantitative
literacy — distinct from a quant researcher (math/stats-first) and a quant
trader (markets-first).

Core pillars:
1. **Software engineering** — the primary skill. Clean, tested, performant code.
2. **Mathematics & statistics** — enough to read, implement, and reason about models.
3. **Finance domain knowledge** — instruments, market microstructure, risk.
4. **Systems & performance** — concurrency, memory, latency, data at scale.

---

## Phase 0 — Foundations setup (1–2 weeks)

Set up the environment and habits you'll use for everything that follows.

- Toolchain: Git/GitHub, a solid editor/IDE, Linux command line.
- Pick primary languages: **Python** (research/tooling) + **C++** (performance)
  — optionally Java/Rust depending on target firms.
- Establish a learning log and weekly review cadence.
- **Milestone:** this repo exists, you commit daily, and you can navigate a
  Linux shell comfortably.

## Phase 1 — Mathematics (8–12 weeks)

See [`../math/phase-1-math-plan.md`](../math/phase-1-math-plan.md) for the detailed plan.

Topics: linear algebra, calculus/multivariable, probability, statistics,
and an intro to stochastic processes.

- **Milestone:** implement from scratch — Monte Carlo estimator, linear
  regression (normal equations + gradient descent), and a simple random-walk
  simulation — with written explanations.

## Phase 2 — Programming & systems (10–14 weeks)

- **Python**: idiomatic code, NumPy/pandas, profiling, packaging, testing (pytest).
- **C++**: modern C++ (11/14/17), RAII, templates, STL, memory model, basic
  concurrency. Build a small numerical library.
- **Data structures & algorithms**: enough to clear coding interviews
  (arrays, hashing, trees, graphs, DP) — grind ~150 curated problems.
- **Systems**: processes/threads, networking basics, databases (SQL), and
  how latency/throughput trade off.
- **Milestone:** a tested C++ mini-library (e.g. matrix ops + a pricer) and
  a Python backtest harness, both on GitHub with CI.

## Phase 3 — Quant finance & data (8–10 weeks)

- Instruments: equities, futures, options; bonds at a high level.
- Pricing: time value of money, Black–Scholes intuition and implementation,
  the Greeks.
- Market microstructure: order books, matching, slippage, transaction costs.
- Data engineering: ingest/clean market data, handle time series, avoid
  look-ahead bias and survivorship bias.
- **Milestone:** a working **event-driven backtester** that prices a simple
  options strategy on historical data and reports PnL/risk honestly.

## Phase 4 — Projects & portfolio (ongoing, ~8 weeks concentrated)

Three portfolio-grade projects that each demonstrate a different strength:

1. **Backtesting engine** (systems + finance) — clean architecture, tests,
   docs, realistic cost modeling.
2. **Low-latency component** (C++/performance) — e.g. an order-book
   implementation with benchmarks.
3. **Research-to-production pipeline** (data + engineering) — ingest data,
   compute a signal, evaluate it, package it.

- **Milestone:** each project has a README, tests, benchmarks where
  relevant, and an honest write-up of limitations.

## Phase 5 — Interview prep & applications (4–8 weeks, overlapping)

- **Coding**: data structures/algorithms under time pressure (C++/Python).
- **Systems design & low-latency**: concurrency, caching, data flow.
- **Math/probability brainteasers**: expectation, conditional probability,
  Markov chains, combinatorics.
- **Finance fluency**: be able to discuss your projects and basic pricing.
- **Behavioral**: clear stories about ownership, debugging, and teamwork.
- **Milestone:** mock interviews passed, applications out to a target list
  (see [`../research/job-market.md`](../research/job-market.md)).

---

## Suggested weekly cadence

- 60% hands-on coding, 25% math/theory, 15% reading + networking.
- Ship something small every week and commit it.
- Monthly: review the job-market doc and adjust the plan.

## Guiding principles

- **Engineering is the job.** Depth in software beats shallow breadth in math.
- **Build in public.** A GitHub trail of real projects beats certificates.
- **Be honest about results.** Backtests that look too good usually have a bug.
- **Iterate the plan.** This roadmap is a living document — update it.

_Last updated: 2026-11-21_
