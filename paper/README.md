# Paper

One command. Not a prop firm.

```
python3 -m paper --mark --equity 100000
python3 -m paper --write --equity 100000
python3 -m paper --verdict
```

`--mark` closes open tickets at worst-side quotes on 50% of credit, 21 DTE, or short tested.

Default tape is `fixtures/spy_take.json`. `--live` is Theta SPY only. The picker does not import `thetadata`.
