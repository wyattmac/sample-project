# Journal

Append-only CSVs. This is the product until S4.

| File | Role |
|---|---|
| `operator.csv` | Who we are. Fill this first. |
| `cash.csv` | Snapshots of idle cash vs sweep vs SGOV. |
| `invoices.csv` | What the lab costs. Zero rows is a good state. |
| `tickets.csv` | Paper (and later live) tickets at worst-side fills. |

Run:

```
python3 tools/excess.py
```

Examples live in `journal/examples/` so the tool can demo without pretending your account is $100k.
