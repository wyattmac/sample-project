# Cash per ticket

Defined-risk iron condor. The cash the broker ties up is **about the max loss**, not SPY notional.

Not financial advice. Typical ranges, not a quote. Run `python3 tools/ticket_cash.py` with the width and credit you actually see on Theta.

---

## The rule (this is the number)

```
cash ≈ max loss = (wing width − net credit) × 100 × contracts
```

Must satisfy:

- **per ticket** ≤ **1% of equity**
- **all open tickets** ≤ **3% of equity**

If the 1-lot max loss is bigger than 1%, you do not “size up.” You skip, or you switch to the put-spread substitute in [PAPER.md](PAPER.md). You never drop the longs to make it cheaper.

Paper trading: **$0** in the broker. Live: this cash is buying power, plus a sweep cushion so `SGOV` is not force-sold.

---

## What a 1-lot SPY condor usually looks like

30–45 DTE, ~15-delta shorts, **$5 or $10** wings, credit at the **worst side**. IV and SPY level move these around. Ballpark:

| Wings | Typical worst-side credit | **Cash / max loss, 1 lot** |
|---|---|---|
| $5 wide | ~$0.80–$1.50 | **~$350–$420** |
| $10 wide | ~$1.50–$2.50 | **~$750–$850** |

Worked example: $5 wide, $1.20 credit → `($5 − $1.20) × 100 = $380` tied up. That *is* the trade. You are not posting $60,000 of SPY.

Commissions are tens of dollars, not the story. Theta’s **$80/month** is a lab invoice, not per ticket.

---

## What that means at account size

| Equity | 1% cap (one ticket) | 3% cap (all open) | Usual live size |
|---|---|---|---|
| $50k | $500 | $1,500 | **One** $5-wide 1-lot, maybe two if credits are fat |
| $100k | $1,000 | $3,000 | One $10-wide **or** two $5-wide 1-lots |
| $250k | $2,500 | $7,500 | A few 1-lots, still not a 10-lot |

The app does not scale into 20-lots because the tape looks good. Concurrent risk is the 3% line. A cold month can use that whole budget on clustered losses — that is why the cap exists.

---

## What you do *not* need

- PDT day-trade buying power (this is a 30–45 DTE hold)
- Portfolio margin, to start
- Full SPY notional
- Extra cash “for 0DTE” — we do not trade 0DTE

Keep idle cash in `SGOV`. Keep a **margin cushion in sweep** at least as large as the 3% cap so a mark against the condor does not liquidate the ladder. On $100k that is about **$3k** sitting in sweep, not in the ticket.

```
python3 tools/ticket_cash.py --equity 100000 --width 5 --credit 1.20
```
