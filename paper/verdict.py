"""Session verdict: keep the rule or kill it. Not a dashboard."""

from __future__ import annotations

from pathlib import Path

from paper.journal import DEFAULT_JOURNAL, settled_paper
from paper.policy import KILL_AFTER_TICKETS


def rule_verdict(journal: Path | None = None) -> str:
    n, pnl = settled_paper(journal or DEFAULT_JOURNAL)
    lines = [
        f"Settled paper tickets: {n}",
        f"Worst-side P&L:        ${pnl:,.0f}",
        f"Kill threshold:        {KILL_AFTER_TICKETS} tickets, P&L < 0",
    ]
    if n >= KILL_AFTER_TICKETS and pnl < 0:
        lines.append("VERDICT: KILL THE RULE. Paper demoted it. Do not go live.")
    elif n >= KILL_AFTER_TICKETS and pnl >= 0:
        lines.append(
            "VERDICT: paper is not negative at N="
            f"{n}. That is not a promotion. S4 is still a human decision at tiny size."
        )
    else:
        lines.append(
            f"VERDICT: not enough settled tickets ({n}/{KILL_AFTER_TICKETS}). Keep logging."
        )
    return "\n".join(lines) + "\n"
