# How this app learns to trade

It doesn’t. Not the way people mean when they say “the AI learns.”

The **policy is written down in advance** ([PAPER.md](PAPER.md): SPY, 30–45 DTE, defined-risk condor, IV rank ≥ 50, worst-side fills). The software does not invent trades, does not fine-tune on P&L, and does not put an LLM on the order path.

What it *does* is keep score, and fire the policy if the score is bad.

Not financial advice.

---

## The loop that exists (Start)

```
rule (fixed)
  → Theta snapshot (or fixture)
    → take or pass (logged)
      → settle at worst-side marks
        → journal
          → keep the rule, or kill it
```

1. **The rule does not change during the 90 days.** No “the model widened the wings this week.” If you change the rule, you started a new sample.
2. **Every day is a row.** Taken tickets *and* passes. A skipped week because IV rank was 41 is evidence, not a hole.
3. **Fills are pessimistic on purpose.** Bid when selling, ask when buying. Learning from mids is how you teach yourself a lie.
4. **Paper can only demote.** After ~20 settled tickets, if worst-fill P&L is negative, the policy dies. Paper cannot promote itself to live. Live is a human S4 decision with tiny size. See [START.md](START.md).
5. **Backtests cannot promote.** Synthetic evidence only demotes. A beautiful historical condor study is not a reason to size up.

That is the whole school. It is slow (weeks per ticket, not ticks). It is supposed to be. A 30–45 DTE book produces tens of independent-ish outcomes a year, not thousands. There is nothing here for a neural net to chew.

---

## What does *not* learn

| Thing | Role |
|---|---|
| Live path | Dumb. Executes a config. Zero LLM bytes. |
| Theta | Tape. Quotes. Not a teacher. |
| Cortex / agents (vision only) | May annotate. May not add Board rows or raise scores. May not send orders. |
| You | The compiler. You can edit the rule. That is also how the experiment gets ruined. |

There is no reinforcement learner that “figures out” 0DTE. There is no agent PM that gets smarter at picking tickers. If you want that, you want a different repo, and [FLAWS.md](FLAWS.md) already explained why that repo is a customer with a dashboard.

---

## What the vision *would* add (not built, not the queue)

[VISION.md](VISION.md) described a second school, offline:

- **Bayesian ledger:** skeptical prior on the policy’s true edge; size off the conservative quantile; promote only if P(edge > 0) ≥ 95% *and* the old frequentist gates pass.
- **Shadow tournament:** 2–4 rule tweaks paper-settled on the same tape; a winner becomes a canary through the same door, never a live shortcut.
- **Replay twin:** the day replays; takes and passes get a dollar score.

[FLAWS.md](FLAWS.md) §5 is the catch: a personal condor book does not produce enough settled, independent tickets for those posteriors to mean anything this decade. Building NumPyro before the CSV has 20 honest rows is a shrine.

So: we do not “learn” by standing up the foundry. We learn by filling `journal/tickets.csv` until the rule has a verdict.

---

## How you will know it learned something

Not a training-loss curve. These:

- A stack of **passed** rows with reasons, not only winners.
- Worst-side P&L after 20+ tickets, not a mid-mark equity curve.
- `excess.py` still honest about the Theta invoice.
- Either the rule is **killed**, or it is **still the same rule** with a boring record.

If the software started proposing a second underlier, a shorter DTE, or a “smarter” fill, that would be the opposite of learning. That would be the factory coming back.
