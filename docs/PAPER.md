# Paper policy — one structure, 90 days

The only Surface policy allowed before S4 in [START.md](START.md). If you want a second rule, you are not following the start.

Not financial advice. Paper only. No live orders from this document.

---

## Edge, in one paragraph

Equity-index implied vol is usually rich versus the vol that realizes over the next month. Selling a **defined-risk** 30–45 DTE condor or credit spread on **SPY or XSP** when IV rank is high is a crowded, well-documented way to rent that premium with a known max loss. It fails in clusters when vol jumps and stays jumped. We are not discovering this. We are asking whether *our fills and our hands* survive it on paper at the **worst side of the quote**.

If you cannot live with that paragraph, do not add clauses. Pick a different life.

---

## Universe

- **One** underlier: **`SPY`**. Write it in `journal/operator.csv` (`paper_underlier=SPY`).
- XSP is the live upgrade (cash-settled, no early assignment) after S4, if you have index approval. Not a second paper book.
- No single names. No earnings. No 0DTE. No FOMC/CPI overlays. Those are other policies.

## Structure (pick one, write it down, do not switch mid-window)

**Default: iron condor, defined risk.**

- DTE at entry: 30–45
- Short strikes: ~15-delta (call and put)
- Long strikes: next width that caps max loss at ≤ **1% of equity** per ticket. Cash tied up ≈ that max loss. Typical 1-lot SPY: **~$350–$850** depending on $5 vs $10 wings. See [SIZE.md](SIZE.md).
- No naked shorts. Longs on before or with the shorts. Always.

**Allowed substitute:** a single credit put spread, same DTE and delta, same max-loss cap — if the condor's call side is too wide to fit the 1% cap. Still defined risk.

## Entry (all must be true)

1. DTE in window.
2. IV rank ≥ 50 on that underlier, computed from **Theta** history on that same root (log `iv_rank_source=theta`). If you cannot compute rank yet, skip the week (`status=passed`) — do not borrow IV rank from a broker or a website.
3. Concurrent paper max-loss (this ticket + open paper tickets) ≤ **3% of equity**.
4. You can trade the package as a combo, not four naked legs "to be more efficient."

## Exit (first hit wins)

- 50% of credit received (using **worst-side** marks, not mid), or
- 21 DTE, or
- Short strike tested, or
- Paper "day loss" on this policy ≥ 1% of equity (stop adding, flatten paper)

No adding width. No rolling into more risk. No "managing" that turns a defined-risk ticket into a story.

## Fills (the whole point)

| Leg | Log this price |
|---|---|
| You sell | **bid** |
| You buy | **ask** |
| Combo credit | the credit you would get lifting/hitting the **combo** worst side, not the sum of mids |

`fill_source` must be `worst`. Bid/ask come from Theta `option_snapshot_quote`, not from Interactive Brokers. Rows with `mid` are invalid for S4. Delete them or mark `status=void`.

Combo NBBO is often not in the snapshot. Until we have a combo quote, **do not invent one by summing four mids.** Summing four *worst* sides is allowed and conservative (it overstates friction). Log that in `notes`.

## What to write on every `tickets.csv` row

See `journal/tickets.csv` headers. Minimum: date, status=`paper`, underlier, structure, dte, iv_rank, max_loss_usd, credit_usd, fill_source=`worst`, thesis (one sentence), result if settled.

Passed days count. Log `status=passed` with why (IV rank too low, cap hit, no combo quote). The Radar was going to journal passes. So do we. In a CSV.

## Kill the policy early

Any of:

- After 20 settled paper tickets, worst-fill P&L is negative and you are not curious in a useful way
- You broke the rules (mid fills, second underlier, live "just to see")
- You want to add crush, lotteries, or a scanner

Paper can demote. It cannot promote to live by itself. See START.md S4.
