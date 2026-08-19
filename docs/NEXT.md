# Next

The app exists. Do not build GIGAHOUSE. **Run the command.**

Not financial advice. The algorithm, in order, applied to *now*.

---

## 1. Requirements are no longer the bottleneck

`python3 -m paper` takes or passes one SPY condor. That is the product. A UI, a foundry, a second ticker, or `--live` “so we have real data” is a new, dumber requirement. Reject it.

## 2. Delete (still)

Do not start: Board UI, SSVI, agents, IBKR API, Theta Pro, XSP paper, lottery, NumPyro, recording the whole OPRA sky. If a PR does not make the journal truer or faster to falsify, it does not merge.

## 3. Simplify: fill the blanks, then stop touching code

1. Put **real** numbers in `journal/operator.csv`.
2. One `cash.csv` row (`SGOV` vs sweep). Invoice Theta if you pay it.
3. Every session:

```
python3 -m paper --equity YOUR_EQUITY
python3 -m paper --write --equity YOUR_EQUITY
python3 -m paper --verdict
```

Fixture tape is enough to prove you will actually show up. A week of silence is a bug. Passed days count.

## 4. Accelerate falsification — the only allowed next feature

After **five** `--write` rows exist, one code increment: **`--mark`**. Revalue open paper tickets from the same tape (worst side). Apply PAPER exits: 50% of credit, 21 DTE, short tested. Write `result_usd`. Then `--verdict` means something.

Not before five rows. Marking zero open tickets is theater.

Do not buy live Theta until the fixture habit is real. Then `--live` replaces the fake IV rank. Standard plan. SPY only.

## 5. Automate last

After **20 settled** worst-side tickets:

- P&L < 0 → kill the rule. Delete the repo or archive it. Do not “tune.”
- P&L ≥ 0 → still not a promotion. Optional: **one** live lot, 1% cap, combo order, broker as execution only.

IBKR API, streaming, CUDA, an LLM note-taker: last, and probably never.

---

## First-unit test (today)

If you will not run `python3 -m paper` in the next session, do not write more Python. The bottleneck is obedience, not features. That was the cold-quarter sentence in every version of this program. It is now a CLI.
