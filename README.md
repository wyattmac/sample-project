# GIGAHOUSE

A personal options system. Engineering plan, not financial advice. No system is profitable by declaration.

**Start here:** [docs/START.md](docs/START.md). **What we use:** [docs/STACK.md](docs/STACK.md).

```
python3 tools/excess.py
python3 tools/theta_ping.py --symbol SPY
python3 tests/test_excess.py tests/test_theta.py
```

Options data is **Theta Data**, not Interactive Brokers. See [docs/DATA.md](docs/DATA.md).

The only number that matters: **vehicle yield − sweep you already had − invoices.**

## Docs

| Doc | What it is |
|---|---|
| [docs/START.md](docs/START.md) | **Where we start.** Operator sheet → park cash → journal → 90 days of one paper policy. |
| [docs/STACK.md](docs/STACK.md) | **What we use.** One choice per slot. Theta Standard, SPY, SGOV, CSV. IBKR is not data. |
| [docs/SCOPE.md](docs/SCOPE.md) | **How much to build.** Start vs vision. Most of the app is fixture-tape; Theta is one adapter. |
| [docs/DATA.md](docs/DATA.md) | **Theta Data is the pipe.** IBKR is not a quote source. Standard plan, one underlier. |
| [docs/SIZE.md](docs/SIZE.md) | **Cash per ticket.** Defined-risk condor: about $350–$850 a lot, capped at 1% of equity. |
| [docs/LEARN.md](docs/LEARN.md) | **How it learns.** It doesn’t train a model. It keeps score and can only fire the rule. |
| [docs/FLAWS.md](docs/FLAWS.md) | Red team. Why the factory is oversized. |
| [docs/VISION.md](docs/VISION.md) | v8 — GIGAHOUSE. Ambition. Not the build queue. |
| [docs/ALGORITHM.md](docs/ALGORITHM.md) | Five-step production algorithm. |
| [docs/CONSTITUTION.md](docs/CONSTITUTION.md) | H14–H23. |

Defined risk always. No naked shorts. No LLM in a live path. Synthetic evidence only demotes. The Czar is you.

## License

MIT. The plan is not a product, not a solicitation, and not advice.
