# How much to build, and what does not need a live Theta key

Two different products got named “the app.” They are not the same amount of work. This file is the size of each, and what can be written against a **recorded tape** instead of `THETADATA_API_KEY`.

Not a calendar. Subsystems and blockages. Not financial advice.

---

## Three finish lines

| Finish line | What “done” means | Size | Live Theta required? |
|---|---|---|---|
| **A. Start** | S0–S4 in [START.md](START.md): cash journal, excess number, one SPY condor on paper at worst-side quotes | Small. A handful of remaining modules on top of what is already here. | **No** for the code. **Yes, once**, if you want *real* SPY chains instead of a synthetic fixture. |
| **B. Honest terminal** | A + risk wall (H14–H23 as code), a one-symbol Board, a weekly packet from the journal, optional IBKR *execution* later | Medium. A real personal app. Still one underlier, still no factory. | **No** for almost all of it. The Theta adapter is a thin I/O boundary. |
| **C. Vision (GIGAHOUSE)** | [VISION.md](VISION.md) G0–G5: GPU SSVI, whole-sky Sensor, crush desk, Bayesian foundry, tournament, replay twin, A-ladder, Cortex, lottery book, cockpit | A **trading platform**, not a feature list. This is the thing [FLAWS.md](FLAWS.md) said is sized for a firm. | You can stub every service. You cannot *know* if scanners, SSVI residuals, or Kelly sizes are anything but tests. |

**The app we are building is A, then B if A survives.** C is not a remaining coding queue. It is a vision document. Asking “how much to get to the full version” and meaning C is how this project dies of complexity (H22).

Already in the repo: `python3 -m paper` (tape → picker → journal → verdict), fixture chains, excess, tests. Theta is `--live` only.

---

## A — the Start app (built)

| Module | Needs live Theta? | Notes |
|---|---|---|
| Fixture tape (`fixtures/spy_take.json`) | No | **Built.** Default backend. |
| IV rank on the snapshot | No | **Built.** Missing or < 50 → pass. |
| Condor picker | No | **Built.** `paper.picker`. |
| `python3 -m paper --write` | No | **Built.** Appends `journal/tickets.csv`. Refuses mid. |
| Operator / 1% / 3% caps | No | **Built.** |
| Theta live adapter | Yes | **Built** as `--live`. Off-hours often empty. |

That is the rest of “the app” as START defines it. Most of it is logic and CSV I/O. The API is one adapter.

---

## B — extra subsystems (only after A is boring)

Risk wall as functions: max loss, concurrent 3%, no naked, no second symbol, H14 lottery = 0 until someone turns it on. Packet = markdown from the journal. One-symbol Board = a table of the picker output. IBKR later = execution adapter, **not** a second quote source.

Still not: SSVI, 200 names, agents, NumPyro, a GPU.

---

## C — why “full GIGAHOUSE” is not a coding estimate

G1–G5 are each a product: surface math, a scanner plugin host, an earnings machine, a Bayesian service, a replay engine, an agent authority layer, a UI that looks like a prop morning meeting. You can generate all of that as empty services. The *work* that makes C real is years of fills, invoices, and firing scanners — and a data bill that is no longer $80.

We do not schedule C. We do not stub C “so the architecture is ready.” H22: new live behavior deletes more than it adds. A empty foundry is adding.

---

## Coding without a Theta API key

**Yes. Most of A and B.** The rule:

```
policy / risk / journal / UI
        │
   QuoteTape protocol   ← already started as ThetaLike
        │
   ┌────┴────┐
 fixture/   live
 (default)  (Theta, when THETADATA_API_KEY is set)
```

- **No key:** tests and `paper_ticket` read `tests/fixtures/`. CI never calls Theta.
- **Key present:** `tools/theta_ping.py` and a `tools/record_tape.py` (not written yet) pull SPY only and overwrite the fixture if you want the tape fresh.
- **Never:** import `thetadata` from the picker, the risk wall, or the journal. If those modules know Theta exists, the boundary leaked.

What you **cannot** do without some tape (live *or* recorded from a real day):

- Claim a fill you could have had
- Claim IV rank
- Claim a scanner found a dislocation

Synthetic fixtures are enough to write and test the code. They are not enough to pass S4. S4 needs worst-side marks from a market. Record them once, then code offline for as long as you want.

---

## Direct answers

**How much coding to the full vision?** Enough that it is the wrong target. Finish A (small, mostly offline). B is a personal terminal on the same spine. C is a firm.

**Can we code most of it without Theta?** Yes. The software is a condor picker, a journal, and a risk wall. Theta is I/O. I can write A against fixtures with no API key. A live key is only required to ping, to refresh the SPY tape, and eventually to mark paper tickets on a real session.
