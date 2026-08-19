# Paper

One command. Not a prop firm.

```
python3 -m paper --equity 100000
python3 -m paper --write --equity 100000
python3 -m paper --verdict
python3 -m paper --live --equity 100000
```

Default tape is `fixtures/spy_take.json` (no API key). `--live` is Theta SPY only.

The picker does not import `thetadata`. Fills are worst-side. Paper can only demote.
