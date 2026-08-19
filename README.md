# GIGAHOUSE

A paper SPY iron condor. Engineering plan, not financial advice.

```
python3 -m paper --equity 100000          # dry-run off a fixture (no API key)
python3 -m paper --write --equity 100000  # append journal/tickets.csv
python3 -m paper --verdict                # kill-rule + cash excess
python3 -m unittest discover -s tests -q
```

Theta is optional (`--live`). Interactive Brokers is not a quote source. The rule does not learn. See [docs/REBUILD.md](docs/REBUILD.md).

## Docs

| Doc | What it is |
|---|---|
| [docs/START.md](docs/START.md) | Build path |
| [docs/STACK.md](docs/STACK.md) | What we use |
| [docs/PAPER.md](docs/PAPER.md) | The condor rule |
| [docs/SIZE.md](docs/SIZE.md) | Cash per ticket |
| [docs/LEARN.md](docs/LEARN.md) | Scorekeeper, not a model |
| [docs/REBUILD.md](docs/REBUILD.md) | Why this is the app |
| [docs/FLAWS.md](docs/FLAWS.md) | Why the factory is oversized |

## License

MIT.
