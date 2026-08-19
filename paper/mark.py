"""Mark open paper tickets against the current tape. Worst side. No broker."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

from paper.journal import load_tickets, write_tickets
from paper.policy import EXIT_DTE, FILL_SOURCE, MULTIPLIER, PROFIT_FRACTION
from paper.tape import Contract, Snapshot


@dataclass(frozen=True)
class MarkReport:
    date: str
    action: str  # closed | open | skipped
    reason: str
    pnl_usd: Optional[float] = None
    close_usd: Optional[float] = None


def _f(row: dict, key: str) -> Optional[float]:
    raw = (row.get(key) or "").strip()
    if raw == "":
        return None
    return float(raw)


def _leg(chain: list[Contract], right: str, strike: float) -> Optional[Contract]:
    hits = [c for c in chain if c.right == right and abs(c.strike - strike) < 1e-6]
    return hits[0] if hits else None


def _close_debit(sp: Contract, lp: Contract, sc: Contract, lc: Contract) -> float:
    """Debit to flatten: buy shorts at ask, sell longs at bid."""
    return sp.ask + sc.ask - lp.bid - lc.bid


def mark_ticket(row: dict, snap: Snapshot) -> tuple[dict, MarkReport]:
    status = (row.get("status") or "").strip().lower()
    if status != "paper" or (row.get("result_usd") or "").strip() != "":
        return row, MarkReport(row.get("date") or "", "skipped", "not an open paper ticket")

    exp_raw = (row.get("expiration") or "").strip()
    sp_k, lp_k = _f(row, "short_put"), _f(row, "long_put")
    sc_k, lc_k = _f(row, "short_call"), _f(row, "long_call")
    credit = _f(row, "credit_usd")
    n = _f(row, "contracts")
    if not exp_raw or None in (sp_k, lp_k, sc_k, lc_k, credit, n) or n <= 0:
        return row, MarkReport(row.get("date") or "", "skipped", "missing legs; cannot mark")

    expiration = date.fromisoformat(exp_raw)
    dte = (expiration - snap.as_of).days
    chain = snap.chain(expiration)
    sp, lp = _leg(chain, "P", sp_k), _leg(chain, "P", lp_k)
    sc, lc = _leg(chain, "C", sc_k), _leg(chain, "C", lc_k)
    if None in (sp, lp, sc, lc):
        return row, MarkReport(row.get("date") or "", "skipped", "leg missing on this tape")

    debit = _close_debit(sp, lp, sc, lc)
    close_usd = debit * MULTIPLIER * n
    pnl = credit - close_usd

    reason = None
    if pnl >= PROFIT_FRACTION * credit - 1e-6:
        reason = f"50% of credit (pnl ${pnl:.0f} vs credit ${credit:.0f})"
    elif dte <= EXIT_DTE:
        reason = f"{dte} DTE <= {EXIT_DTE} exit"
    elif snap.spot is not None and (snap.spot <= sp_k or snap.spot >= sc_k):
        reason = f"short tested (spot {snap.spot:.2f})"

    updated = dict(row)
    updated["dte"] = str(dte)
    if reason:
        updated["result_usd"] = f"{pnl:.2f}"
        updated["fill_source"] = FILL_SOURCE
        updated["notes"] = f"closed: {reason}"
        return updated, MarkReport(row.get("date") or "", "closed", reason, pnl, close_usd)
    return updated, MarkReport(
        row.get("date") or "",
        "open",
        f"unrealized ${pnl:.0f}; {dte} DTE left",
        pnl,
        close_usd,
    )


def mark_open(snap: Snapshot, journal: Path | None = None) -> list[MarkReport]:
    rows = load_tickets(journal)
    out: list[dict] = []
    reports: list[MarkReport] = []
    changed = False
    for row in rows:
        new_row, report = mark_ticket(row, snap)
        out.append(new_row)
        if (row.get("status") or "").strip().lower() == "paper" and (
            row.get("result_usd") or ""
        ).strip() == "":
            reports.append(report)
            if report.action == "closed":
                changed = True
            elif new_row.get("dte") != row.get("dte"):
                changed = True
    if changed or reports:
        write_tickets(out, journal)
    return reports
