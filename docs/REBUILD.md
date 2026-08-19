# If the algorithm ran on *this* repo

GIGAHOUSE was the first Elon pass: delete the seven-desk org chart, keep a factory metaphor. That was analogical thinking with better branding.

A second pass would run the same five steps on **what we actually have** — a pile of vision docs and a CSV journal — and delete the factory too.

The production algorithm, in order. Not financial advice. Not a personality impression.

---

## 1. Make the requirements less dumb

The requirement is not “a personal prop firm in a box.” That is a costume.

The less-dumb requirement:

> One command, one underlier, one rule. Each session: take a defined-risk SPY condor at the worst quote, or pass. Write the row. After enough rows, keep the rule or delete the repo. Excess versus the cash you would have held, after the Theta invoice, is the only dashboard.

If we had never seen Jane Street, Tesla, or a cockpit UI, we would still need that. We would not need Cortex, a Radar, or a foundry.

---

## 2. Delete

Default yes:

| Delete | Why |
|---|---|
| GIGAHOUSE / three factories / Starship | Org chart with rockets. The Start app is one condor. |
| Whole-sky Sensor, SSVI, GEX | Quote garbage at retail. $80 Standard is a SPY tape, not OPRA-as-a-service. |
| Bayesian ledger, Kelly, shadows, replay twin | N is too small. A shrine. |
| Agents, A-ladder, weekly packet theater | An LLM cannot be the intern with the launch button, so it should not be the intern with a career either. |
| Lottery book | 1% convexity is how the interesting brain stays in the project. Failure mode. |
| Box lending, Carry “factory” | `SGOV` is a settings page. |
| Broker API this year | Paper first. An order path is automation (step 5). |
| Half of `docs/` | A repo with more constitution than code is a blog. Keep START, PAPER, STACK, FLAWS, this file. The rest is archive. |

The best part is no part. The best factory is no factory.

---

## 3. Simplify (only after delete)

The rebuilt app is four functions:

1. **Tape** — SPY chain, bid/ask (Theta live *or* last recorded fixture).
2. **Picker** — 30–45 DTE, ~15Δ, defined-risk, 1% cap. Worst-side credit. Or `pass`.
3. **Journal** — append one row. No second database.
4. **Verdict** — `excess.py` + ticket P&L. Kill the rule if the sample says so.

One CLI:

```
python3 -m paper --equity 100000
python3 -m paper --write --equity 100000
python3 -m paper --verdict
```

This exists. Default tape is a fixture. `--live` is Theta SPY. No UI.

---

## 4. Accelerate cycle time

Not “stream every OPRA quote.” Not 0DTE.

Faster *falsification*:

- Mark open paper tickets every session from the same snapshot, not when someone remembers.
- Passed days are first-class (already in PAPER.md). A week of silence is a bug.
- Twenty settled worst-side tickets is a verdict, not a “wait for the foundry.”
- If Theta’s $80/month is slower to justify than recording a tape once a week, record the tape. The invoice is part of cycle time.

A feedback loop slower than the 30-day hold is decoration. A feedback loop faster than the hold (tick replay, CUDA) is theater.

---

## 5. Automate — last

Live broker routing is last. CUDA is last. An agent that writes the daily note is last, and probably never.

The Autopilot rule still holds, smaller: **the picker is not a neural net.** It is a config. If you want a net, it proposes offline and the 1%/3% caps dispose. If the cap code is down, nothing papers. Fail-static.

Do not automate `SGOV`. That is a buy.

---

## First-unit economics (the actual Elon question)

Before writing G1:

- Theta Standard ≈ $80/month
- A 1-lot $5-wide SPY condor ties up ~$350–$420 ([SIZE.md](SIZE.md))
- Sweep-vs-SGOV on idle cash is tens of bps

If the lab bill exceeds anything the condor can honestly earn, **the first unit does not work.** He would cancel Pro, cancel the universe scan, cancel the UI, and either keep Standard as a SPY tape or freeze a fixture and stop paying until the picker exists.

Vertical integration here is not “own OPRA.” It is **own the row**: quote → rule → journal → kill. The pipe you do not own is the exchange. Pretending otherwise is how you buy Databento.

---

## What he would ship, in order

1. `python3 -m paper` against a fixture (no API key). Tests. Already half-started.
2. Same command against Theta SPY only. Ping already exists.
3. Nightly mark + `excess.py` on a cron. No dashboard.
4. Stop. Read twenty tickets. Delete the repo or keep the rule.
5. *Then* a broker combo order, size 1 lot, 1% cap in code.

He would not rebuild GIGAHOUSE. He would treat GIGAHOUSE as the requirements document that failed step 1.

---

## One line

Be the customer. One condor. One CSV. Kill the rule or kill the project. Everything else is a rendering bug.
