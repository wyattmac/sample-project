# GIGAHOUSE

**Start here:** [docs/NEXT.md](docs/NEXT.md) — run the command. Do not add a factory.

```
python3 -m paper --mark --equity 100000
python3 -m paper --write --equity 100000
python3 -m paper --verdict
python3 -m unittest discover -s tests -q
```

Theta is optional (`--live`). Interactive Brokers is not a quote source. The rule does not learn. See [docs/REBUILD.md](docs/REBUILD.md).

## Docs

| Doc | What it is |
|---|---|
| [docs/NEXT.md](docs/NEXT.md) | **What to do now.** Run the command. `--mark` only after five rows. Automate last. |
| [docs/STACK.md](docs/STACK.md) | What we use |
| [docs/PAPER.md](docs/PAPER.md) | The condor rule |
| [docs/SIZE.md](docs/SIZE.md) | Cash per ticket |
| [docs/LEARN.md](docs/LEARN.md) | Scorekeeper, not a model |
| [docs/REBUILD.md](docs/REBUILD.md) | Why this is the app |
| [docs/FLAWS.md](docs/FLAWS.md) | Why the factory is oversized |

## License

MIT.
