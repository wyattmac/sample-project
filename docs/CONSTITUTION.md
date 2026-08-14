# The Czar's Constitution

Unappealable. Enforced in code. Agents do not get a vote. Persuasive agents especially do not get a vote.

v5/v6 articles **H1–H13** remain absolute and are not restated here: interlocks per book, asymmetric autonomy (H12 tokens), sweeps, falsification budgets, equity governor, fail-static, dead-men, defined risk, no naked shorts. If an article below conflicts with H1–H13, H1–H13 wins.

v7 articles **H14–H18** are inherited. v8 adds **H19–H23**.

---

## H14 — Convexity cap

Lottery / Convexity factory risk ≤ **1% of equity per month**.

- Calendar-replenished only.
- Funded only from program equity **above high-water**.
- **No intra-month re-up path exists in code.**
- Spent is spent. Chasing is a compile error.

## H15 — Factory drawdown budgets

Each factory carries a hard drawdown budget (default **3% of program equity**).

- Certainty factory is exempt.
- Breach → factory flat + demoted one interlock level + packet inquest.

## H16 — Concentration

- No factory above **35%** of program risk (Certainty exempt).
- No single underlying above **20%** across all factories combined.
- Portfolio Greeks (H5) net across factories. The Czar is the sole netting authority.

## H17 — Tier funding order

The stack rule in code. Speculative-tier budgets shrink first and automatically in drawdown. Certainty is the lung. No path exists to refill Convexity from a losing Surface month.

## H18 — Cortex authority bounds

A-ladder state is enforced at the API layer.

- A0 annotates. Cannot affect decisions.
- A1 annotations enter scoring with a **measured, capped** weight.
- A2 veto is a tracked position. Veto alpha is published. Negative veto alpha fires the veto.
- A3 proposes tickets and DSL promotions through the **full gauntlet only**.

No Cortex output reaches the actuator by any path that skips the gauntlet. Property-tested. Adversarial fixtures where a 'persuasive' output attempts every known shortcut. A shortcut is Sev-0.

## H19 — Sensor stale is dead

If surface-fit or Board age exceeds the SLA (default: **3× snapshot interval**), actuators freeze.

A stale Sensor is not degraded mode. It is a dead man. Fail-static. Compute is a risk input.

## H20 — Kill-by-date

Every scanner, policy head, Cortex role, and model seat carries an expiry.

If the skeptical posterior has not cleared its promotion threshold by N settled decisions (configured per class), it is fired automatically. No evergreen hypotheses. No museum.

## H21 — Single throat to choke

One Czar process. One journal. One posterior service. One actuator.

Dual-writes and "temporary" side channels are Sev-0. If you cannot point to the process that said no, you do not have a Czar.

## H22 — Complexity budget

`src/live/` has a hard line-count and dependency ceiling, enforced in CI.

New live behavior must **delete more than it adds**, or it does not merge. The dominant risk of v7 was complexity. The mitigation is a compiler error.

## H23 — No part that does not earn

A factory, scanner, or role whose conservative posterior is below zero after its kill-by-date does not get a stay of execution because the story is good.

Stories are cheap. Posteriors are not.

---

## Kill criteria at every altitude

```
ticket (defined risk)
  → day (H2)
    → factory (H15)
      → tier (H17)
        → program (falsification budget)
```

The maximum tuition of every layer — including Starship — is computable in advance. That is the entire difference between a casino patron and a casino owner.

## Autonomy (asymmetric, unchanged)

- Every **increase** in capital or authority needs the Board's token.
- Every **decrease** already happened by the time you read about it.

## Live path (unchanged, non-negotiable)

Zero LLM bytes in `src/live/`. CI greps. The neural net proposes. The safety computer disposes. If the Czar is down, the house does not trade.
