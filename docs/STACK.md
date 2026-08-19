# What we use

One choice per slot. If it is not in the **Use** column, we do not use it. Details for the data pipe are in [DATA.md](DATA.md). The build order is [START.md](START.md).

Not financial advice. Not an order.

---

## Now (S0–S3)

| Slot | Use | Do not use |
|---|---|---|
| **Options data** | **Theta Data, Options Standard (~$80/mo)** | IBKR market data, TWS, `ib_insync`, Databento, Polygon, ORATS, Yahoo, Unusual Whales, CBOE DataShop |
| **Data client** | Python package `thetadata` ≥ 1.0.9, `THETADATA_API_KEY` | Theta Terminal JAR, `127.0.0.1:25503`, streaming |
| **Paper underlier** | **SPY** | XSP until live, QQQ, IWM, single names, 0DTE, “the universe” |
| **Structure** | Defined-risk iron condor (put credit spread only if the condor cannot fit the 1% cap) | Naked shorts, wheel, calendars, crush, lotteries, ICT |
| **Fill** | Theta NBBO **bid** (sell) / **ask** (buy) | Mid, broker last, “I would have gotten filled” |
| **IV rank** | Computed later from Theta history on **SPY only**; skip the week until that exists | A website rank, IBKR HV, VIX-as-IV-rank |
| **Cash** | **`SGOV`** for idle cash, broker sweep for the margin cushion — whichever the operator sheet says wins after ~20 bps | Box spreads, T-bill ladder code, HYSA-as-a-service |
| **Broker this week** | **None.** Paper does not need an execution API | Wiring TWS, Tradier, or anything that can send an order |
| **Ledger** | `journal/*.csv` + `tools/excess.py` | Postgres, NumPyro, a “foundry,” Notion |
| **Language** | Python 3.12+ | A second language for the tape |
| **Compute** | The laptop that already exists | GPU, CUDA, a always-on box “for surfaces” |
| **LLM** | Off | Anything that can touch a quote, a ticket, or `src/live/` |

SPY rather than XSP for paper: the tape is tighter, Theta examples are SPY, and you do not need index-options approval to learn whether worst-side fills kill the condor. XSP is the live upgrade if you have index approval — cash-settled, no early assignment. Not this week.

---

## Later (S4+, only if paper survived)

| Slot | Use | Do not use |
|---|---|---|
| **Broker / execution** | **Interactive Brokers** — still the least-bad live seat: combos, cash sweep, a PM path, an API | IBKR as a *data* vendor. Do not replace Theta with TWS quotes. |
| **Theta plan** | Stay on **Standard** until a live combo actually needs a stream | Pro “to be ready.” Value as a downgrade that breaks NBBO |
| **Live underlier** | XSP if approved; otherwise keep SPY and size so assignment is survivable | SPX full-size until the account and the ops are real |
| **Orders** | Native **combo** tickets, defined risk, longs on first | Four naked legs, smart-routing theater |

If you already refuse IBKR as a *broker*, say so and we pick Tradier or tastytrade for live only. Until then the default live seat is IBKR and the default quote seat is Theta. Those are different jobs.

---

## Locked values for `journal/operator.csv`

```
data_vendor=theta
theta_plan=standard
monthly_data_budget_usd=80
paper_underlier=SPY
vehicle=SGOV
```

`broker` can be `ibkr` even while we send **zero** IBKR market-data requests. It names where cash sits, not where quotes come from.

---

## If you want a second thing

You don't. A second data vendor, a second underlier, a second structure, or a broker API this week is how the factory comes back.
