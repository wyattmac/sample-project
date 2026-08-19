# Journal

Append-only CSVs. This is the product until S4.

| File | Role |
|---|---|
| `operator.csv` | Who we are. Fill this first. |
| `cash.csv` | Snapshots of idle cash vs sweep vs SGOV. |
| `invoices.csv` | What Theta (and anything else) costs. Log the $80. |
| `tickets.csv` | Paper (and later live) tickets at worst-side fills. |

`data_vendor` is `theta`. Quotes never come from Interactive Brokers.

Run:

```
python3 tools/excess.py
python3 tools/theta_ping.py --symbol SPY
```

Examples live in `journal/examples/` so the tool can demo without pretending your account is $100k.
