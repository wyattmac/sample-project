# Where we start

Not the Radar. Not the foundry. Not Cortex. Not seven desks renamed as three factories.

**We start with a spreadsheet of cash, invoices, and paper tickets — then we stop until those numbers are boring.**

`VISION.md` is the ambition. `FLAWS.md` is why the ambition is oversized. `STACK.md` is what we use. `SCOPE.md` is how much we actually build. This file is the build path. If a PR cannot point to a step here, it does not merge.

Engineering plan, not financial advice. Nothing here is an order.

---

## The order (do not skip, do not reorder)

| Step | What | Done when | Not done when |
|---|---|---|---|
| **S0** | Fill the operator sheet | `journal/operator.csv` has real numbers, not blanks | You are still guessing account size, sweep APY, or options level |
| **S1** | Park idle cash | Unencumbered cash is in `SGOV` (or the broker vehicle that *beats* `SGOV` after friction) and `python3 tools/excess.py` runs against your journal | You wrote a Carry "factory." You opened a box. You bought data to "pay for itself later." |
| **S2** | Journal, for real | Every invoice and every paper ticket has a row. Excess is computed against **sweep you already had**, not against zero | A Bayesian service. A second CSV "for the foundry." |
| **S3** | One paper policy | [PAPER.md](PAPER.md) followed for **90 calendar days**, fills marked at the **worst side of the quote**, no live orders | A second policy. A scanner. A crush overlay. ICT. Lottery tickets. |
| **S4** | Read the number | Trailing excess after invoices is clearly positive, *or* you admit it is not and you do not scale | You start live because the paper book "looks good" at the mid |

Live trading is not a step on this list. It is a decision *after* S4, with size so small that a full max-loss month is a rounding error on equity. If that sentence feels unsatisfying, that is the point.

---

## S0 — Operator sheet (this week, before code)

Copy the headers in `journal/operator.csv` and fill them. The program does not get to assume six figures, portfolio margin, or a free OPRA firehose.

Required fields:

- broker
- equity (USD)
- unencumbered cash (USD)
- current sweep APY (%)
- current `SGOV` (or equivalent) APY (%)
- options approval level
- PDT status
- portfolio margin: yes/no
- `data_vendor` (must be `theta` — see [DATA.md](DATA.md))
- `theta_plan` (`standard` for paper NBBO; not Value; not Pro until S4)
- monthly data budget you will actually pay Theta + OPRA (likely **80**, not 0)
- hours per week you will actually give this (default: be honest)
- `paper_underlier` (`SPY` — see [STACK.md](STACK.md); XSP is a live upgrade, not a paper fork)

**Data pipe is Theta. Not Interactive Brokers.** IBKR (or any broker) may hold the account later. It does not supply quotes, greeks, or history. Paper fills are Theta NBBO, worst side.

**Gate:** Theta Standard is a quote tape for **one** underlier, not a license to scan 200 names. `tools/theta_ping.py` will refuse anything except SPY/XSP.

**Gate:** if monthly data budget is $0, you do not have Theta, so you do not have paper quotes. Skip S3 or pay the invoice and log it. Coverage is a function of cash. That was B7. We mean it now.

**Gate:** if sweep APY is within ~20 bps of `SGOV`, S1 is "leave it" or a one-ticket `SGOV` buy — not a laddering engine.

**Gate:** if equity is below the broker's portfolio-margin line, boxes do not exist. Do not spec them.

---

## S1 — Certainty as a settings page

One afternoon:

1. Put unencumbered cash in `SGOV` / `BIL` / the broker's T-bill vehicle — whichever the operator sheet says wins after spread and tax lots.
2. Turn on the best sweep for cash that must stay cash (margin cushion).
3. Log a `journal/cash.csv` row.
4. Run `python3 tools/excess.py`.

That is the whole Carry desk. If this is not earning more than it costs, nothing downstream is allowed to spend.

No box-spread module. No sweep optimizer. No GPU.

---

## S2 — The journal is the product

Three files, append-only, in `journal/`:

| File | What it proves |
|---|---|
| `operator.csv` | Who we are, in numbers |
| `cash.csv` | What idle cash is doing versus `SGOV` and versus sweep |
| `invoices.csv` | What the lab costs |
| `tickets.csv` | What we did or would have done, **at a fill we could have had** |

`tools/excess.py` reads those files and prints the only number the cockpit was supposed to be:

**vehicle yield − SGOV yield − invoices**

and the harsher twin:

**vehicle yield − sweep you already had − invoices**

If the second number is negative, GIGAHOUSE is a consumer of your life. The tool will say so. Do not argue with it.

---

## S3 — One paper policy, 90 days

Mandate: [docs/PAPER.md](PAPER.md).

- One underlying family: **SPY or XSP**, not both to start.
- One structure: **defined-risk short vol** (iron condor or credit spread). Not crush, not calendars, not lotteries, not ICT.
- Entry/exit rules fit on one page. If you need "and also," you are collecting scanners. Stop.
- **Credit is logged at the bid** (you are selling). Debits at the ask. Mid is a lie. Mark `fill_source=worst`.
- Max loss per ticket ≤ 1% of equity. Concurrent paper risk ≤ 3% of equity. Same shape as H15, even on paper, so the muscle memory exists before the money does.
- Quotes from Theta (`option_snapshot_quote` on that one root). Not TWS, not IBKR hist, not mid.
- No live broker API. No LLM in anything that could be mistaken for an order.

Ninety days of this is a small number of tickets. That is fine. That is the sample-size lesson arriving on time instead of as a NumPyro shrine.

---

## S4 — Only then, look at live

Live is allowed to be *considered* when all of these are true:

1. S0–S3 complete (90 days of paper, not 90 days of planning).
2. You have run `excess.py` **with the Theta invoice logged**. If net vs sweep is negative, you are funding a lab. Do not "fix" that by omitting the invoice or by scanning 200 names "since we're paying." Live is still not implied.
3. Paper tickets used `fill_source=worst`, not mid.
4. You can state the edge in one paragraph without "and also."
5. First live size: one ticket, max loss you would not notice. Not a factory allocation.

If paper lost at honest fills, you do not "go live smaller." You stop. Synthetic evidence only demotes. Paper is synthetic. It can kill the policy. It cannot birth a desk.

---

## Frozen until S4 (a compiler error in English)

Do not start:

- Surface engine / SSVI / GPU fits
- Whole-sky scanner fleet / Best Options Board / `expiration=*` on every root
- Interactive Brokers (or any broker) as a market-data source
- Event crush pipeline
- Flow / GEX / vanna feeds
- Bayesian ledger, Kelly sizer, shadow tournament, replay twin
- A-ladder, agent PMs, vector memory
- Lottery / Convexity book
- Box lending
- Any LLM in `src/live/` (there is no `src/live/` yet; do not create it to put an LLM in it)
- A second paper policy

v8's G0–G5 nodes are **not** the start. They are what we might earn the right to build if S4 is boringly positive. Curiosity will want G1 this week. That is the failure mode `FLAWS.md` named. This file is the counterweight.

---

## This week's work (the only queue)

1. Fill `journal/operator.csv` (`data_vendor=theta`, `theta_plan=standard`, `paper_underlier=SPY`, real equity).
2. Park cash or log why sweep already wins. Add a `cash.csv` row. Log the Theta invoice if you pay it.
3. Dry-run the app (no API key):

```
python3 -m paper --equity 100000
python3 -m paper --write --equity 100000
python3 -m paper --verdict
```

4. Optional: `python3 -m paper --live --equity 100000` with `THETADATA_API_KEY` — SPY only.
5. One real paper row per session at worst-side fills. Not five. Not a backtest. Not a second symbol.

That is the start.
