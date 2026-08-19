# Next

The app exists. Do not build GIGAHOUSE. **Run the loop.**

```
python3 -m paper --mark --equity YOUR_EQUITY
python3 -m paper --write --equity YOUR_EQUITY
python3 -m paper --verdict
```

`--mark` is built: open tickets revalue at the worst side and close on 50% of credit, 21 DTE, or short tested.

Not financial advice.

---

## 1. Do not add product

UI, foundry, agents, IBKR API, Theta Pro, a second ticker: reject. The requirement is already one condor and a CSV.

## 2. Fill the sheet, then show up

1. Real numbers in `journal/operator.csv`.
2. One `cash.csv` row. Theta invoice if you pay it.
3. Every session: `--mark`, then `--write`, then `--verdict`. Fixture tape is enough. A week of silence is a bug.

## 3. Accelerate by using `--mark`, not by streaming

Falsification is now a flag. Use it. Do not buy live Theta until the fixture habit is real. Then `--live` is SPY only.

## 4. Automate last

After **20 settled** worst-side tickets: negative → kill the rule. Non-negative → optional **one** live lot. Broker last. Never an LLM on the order path.

## First-unit test (today)

If you will not run the three commands in the next session, do not write more Python.
