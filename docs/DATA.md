# Data pipe — Theta, not the broker

Options market data comes from **[Theta Data](https://www.thetadata.net/)**. Interactive Brokers (and every other broker) is **not** a quote source, not a greeks source, not a history source.

Fills in the journal are Theta NBBO, marked at the **worst side**. Broker prints, when they exist later, are for execution recon — they do not replace the quote we used to decide.

Engineering plan, not financial advice.

---

## What we buy

Retail Theta **Options** plans ([pricing](https://thetadata.net/pricing), individual use, cancel anytime):

| Plan | List (monthly) | What it is for **this** repo |
|---|---|---|
| Value — $40 | 1-minute intervals, 4y history | Not enough. We need NBBO bid/ask for worst-side paper fills. |
| **Standard — $80** | Chain snapshots, tick, every OPRA NBBO quote, 8y | **Default for S3 paper.** One underlier. Not the sky. |
| Pro — $160 | Root snapshots, stream every option trade, 12y | Frozen until S4 live. Do not subscribe "to be ready." |

Plus OPRA. Theta's own [fee guide](https://www.thetadata.net/articles/2026-05-29-opra-fee-guide-for-options-market-data): non-professional is about **$1.25**/user/month (Theta pays it on the retail page). Professional is about **$31.50**. Non-display (algos, risk systems, "the house") starts around **$2,000**/month per category and is a commercial license. If you are actually running a prop desk as a business, you are not on the $80 page. Do not pretend otherwise.

Log the invoice in `journal/invoices.csv` the day it hits the card. `tools/excess.py` will tell you if Theta ate the cash edge. It probably did. That is allowed only because you chose a lab cost. It is not "Certainty funding the Sensor."

---

## How we talk to it

**Python library, no Terminal required.**

```
pip install thetadata
export THETADATA_API_KEY="..."
python3 tools/theta_ping.py --symbol SPY
```

- Package: [`thetadata`](https://pypi.org/project/thetadata/) ≥ 1.0.9, Python 3.12+
- Auth: `THETADATA_API_KEY` (or `.env` in the repo root — never commit it)
- Client: `ThetaClient()` from `thetadata` — HTTPS + gRPC, returns a dataframe
- We do **not** run `ThetaTerminalv3.jar` and we do **not** scrape `http://127.0.0.1:25503` unless streaming is later forced by a live seat. Paper does not need a JAR.

Allowed roots until S4: **`SPY` or `XSP`**, the one in `journal/operator.csv`. A request for any other symbol is a bug. The ping tool will refuse it.

Allowed calls until S4:

- `option_list_expirations(symbol=root)`
- `option_snapshot_quote(...)` for **one** expiration in the 30–45 DTE window, `strike_range` capped (not `expiration=*`, not the whole chain of every expiry)
- later: enough history on **that same root** to compute IV rank — still not the universe

Forbidden:

- IBKR market data, `ib_insync` quotes, TWS hist, broker greeks
- Databento, Polygon, Orats, Yahoo "as a backup"
- Whole-sky snapshots, GEX maps, every-root scans
- Streaming every OPRA quote (that is Pro, and it is a Sensor)

---

## Operator fields

In `journal/operator.csv`:

- `data_vendor` = `theta` (no other value is valid)
- `theta_plan` = `standard` until S4 says otherwise
- `monthly_data_budget_usd` = what you actually pay Theta + OPRA (likely **80**, not 0)

The old START gate "data budget $0 means no Sensor" still holds for a *Sensor*. Theta for **one paper underlier** is a quote tape, not a Sensor. Do not "while we're paying Standard, pull 200 names." That is how $80 becomes a foundry.

---

## License landmine

The vision says "personal proprietary trading firm." Theta's $40/$80/$160 page is **individual / non-professional**. Automating quotes into a trading system, running it as a business, or redistributing data can push you into professional, non-display, or commercial. Read their commercial page before you put "the house" on a server. This repo assumes personal paper use of Standard. If that assumption is wrong, stop and fix the license before you write more code.
