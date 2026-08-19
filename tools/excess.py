#!/usr/bin/env python3
"""Excess over the cash you would have held anyway.

Prints vehicle yield versus SGOV and versus the sweep you already had,
then subtracts invoices. Paper ticket P&L is shown separately and is
never treated as funding.

  python3 tools/excess.py
  python3 tools/excess.py --journal journal/examples
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Optional


def _f(row: dict, key: str) -> Optional[float]:
    raw = (row.get(key) or "").strip()
    if raw == "":
        return None
    return float(raw)


def _d(row: dict, key: str = "date") -> Optional[date]:
    raw = (row.get(key) or "").strip()
    if raw == "":
        return None
    return datetime.strptime(raw, "%Y-%m-%d").date()


def _money(n: float) -> str:
    sign = "-" if n < 0 else ""
    return f"{sign}${abs(n):,.0f}"


def _pct(n: float) -> str:
    return f"{n:.2f}%"


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"missing {path}")
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


@dataclass
class CashSnapshot:
    as_of: date
    equity: float
    unencumbered: float
    vehicle: str
    vehicle_apy: float
    sweep_apy: float
    sgov_apy: float


def latest_cash(rows: list[dict]) -> Optional[CashSnapshot]:
    parsed: list[CashSnapshot] = []
    for row in rows:
        as_of = _d(row)
        if as_of is None:
            continue
        unencumbered = _f(row, "unencumbered_cash_usd")
        vehicle_apy = _f(row, "vehicle_apy_pct")
        sweep_apy = _f(row, "sweep_apy_pct")
        sgov_apy = _f(row, "sgov_apy_pct")
        equity = _f(row, "equity_usd")
        vehicle = (row.get("vehicle") or "").strip() or "?"
        if None in (unencumbered, vehicle_apy, sweep_apy, sgov_apy, equity):
            continue
        parsed.append(
            CashSnapshot(
                as_of=as_of,
                equity=equity,
                unencumbered=unencumbered,
                vehicle=vehicle,
                vehicle_apy=vehicle_apy,
                sweep_apy=sweep_apy,
                sgov_apy=sgov_apy,
            )
        )
    if not parsed:
        return None
    parsed.sort(key=lambda s: s.as_of)
    return parsed[-1]


@dataclass
class Invoices:
    count: int
    total: float
    first: Optional[date]
    last: Optional[date]
    by_category: dict[str, float]

    @property
    def span_days(self) -> Optional[int]:
        if self.first is None or self.last is None:
            return None
        return (self.last - self.first).days + 1

    def annualized(self) -> Optional[float]:
        span = self.span_days
        if span is None or span <= 0 or self.count == 0:
            return None
        if span < 28:
            return None
        return self.total * (365.0 / span)


def summarize_invoices(rows: list[dict]) -> Invoices:
    dates: list[date] = []
    total = 0.0
    by_cat: dict[str, float] = {}
    n = 0
    for row in rows:
        amount = _f(row, "amount_usd")
        if amount is None:
            continue
        n += 1
        total += amount
        cat = (row.get("category") or "uncategorized").strip() or "uncategorized"
        by_cat[cat] = by_cat.get(cat, 0.0) + amount
        as_of = _d(row)
        if as_of is not None:
            dates.append(as_of)
    return Invoices(
        count=n,
        total=total,
        first=min(dates) if dates else None,
        last=max(dates) if dates else None,
        by_category=by_cat,
    )


@dataclass
class Tickets:
    paper: int
    passed: int
    live: int
    void_or_other: int
    mid_fills: int
    worst_fills: int
    paper_result: float
    paper_result_n: int


def summarize_tickets(rows: list[dict]) -> Tickets:
    t = Tickets(0, 0, 0, 0, 0, 0, 0.0, 0)
    for row in rows:
        status = (row.get("status") or "").strip().lower()
        if status == "paper":
            t.paper += 1
        elif status == "passed":
            t.passed += 1
        elif status == "live":
            t.live += 1
        elif status:
            t.void_or_other += 1
        else:
            continue
        fill = (row.get("fill_source") or "").strip().lower()
        if fill == "mid":
            t.mid_fills += 1
        elif fill == "worst":
            t.worst_fills += 1
        if status == "paper":
            result = _f(row, "result_usd")
            if result is not None:
                t.paper_result += result
                t.paper_result_n += 1
    return t


def render(cash: Optional[CashSnapshot], invoices: Invoices, tickets: Tickets) -> str:
    lines: list[str] = []
    lines.append("GIGAHOUSE excess — cash you would have held anyway")
    lines.append("")

    if cash is None:
        lines.append("Cash: no complete snapshot in cash.csv")
        lines.append("      Need date, equity, unencumbered cash, vehicle APY, sweep APY, SGOV APY.")
        vs_sgov = 0.0
        vs_sweep = 0.0
    else:
        vs_sgov = cash.unencumbered * (cash.vehicle_apy - cash.sgov_apy) / 100.0
        vs_sweep = cash.unencumbered * (cash.vehicle_apy - cash.sweep_apy) / 100.0
        lines.append(f"Cash snapshot (latest): {cash.as_of.isoformat()}")
        lines.append(f"  Equity:                   {_money(cash.equity)}")
        lines.append(f"  Unencumbered cash:        {_money(cash.unencumbered)}")
        lines.append(f"  Vehicle:                  {cash.vehicle} @ {_pct(cash.vehicle_apy)}")
        lines.append(f"  Sweep (already had):      {_pct(cash.sweep_apy)}")
        lines.append(f"  SGOV (benchmark):         {_pct(cash.sgov_apy)}")
        lines.append("")
        lines.append("  Annualized, this cash level, before invoices:")
        lines.append(f"    Vehicle vs SGOV:        {_money(vs_sgov)} / yr")
        lines.append(f"    Vehicle vs sweep:       {_money(vs_sweep)} / yr")
        if abs(cash.vehicle_apy - cash.sgov_apy) < 0.05:
            lines.append("    (Vehicle ≈ SGOV. Certainty is a settings page, not an engine.)")

    lines.append("")
    if invoices.count == 0:
        lines.append("Invoices: none. This is the correct state until a data bill is forced.")
        invoice_yr = 0.0
        invoice_note = "none"
    else:
        lines.append(
            f"Invoices: {invoices.count} row(s), "
            f"{_money(invoices.total)} raw"
            + (
                f" ({invoices.first} → {invoices.last})"
                if invoices.first and invoices.last
                else ""
            )
        )
        for cat, amt in sorted(invoices.by_category.items()):
            lines.append(f"    {cat}: {_money(amt)}")
        annualized = invoices.annualized()
        if annualized is None:
            invoice_yr = invoices.total * 12.0
            invoice_note = "naive ×12 from a short window — not a measurement"
            lines.append(
                f"  Window < 28 days. Naive annualization: {_money(invoice_yr)} / yr ({invoice_note})."
            )
        else:
            invoice_yr = annualized
            invoice_note = f"annualized from {invoices.span_days} days"
            lines.append(f"  Annualized:               {_money(invoice_yr)} / yr ({invoice_note})")

    lines.append("")
    lines.append("Net (the number):")
    net_sgov = vs_sgov - invoice_yr
    net_sweep = vs_sweep - invoice_yr
    lines.append(f"  vs SGOV, after invoices:  {_money(net_sgov)} / yr")
    lines.append(f"  vs sweep, after invoices: {_money(net_sweep)} / yr")
    if cash is not None and invoice_yr > 0 and net_sweep < 0:
        lines.append("  VERDICT: invoices eat the cash edge. Do not buy more pipe.")
    elif cash is not None and abs(vs_sgov) < 1 and invoices.count == 0:
        lines.append("  VERDICT: parked at SGOV, no lab costs. S1 is done. Do not build G0.")
    elif cash is not None and net_sweep > 0:
        lines.append("  VERDICT: small positive vs sweep after costs. Still not a factory.")
    else:
        lines.append("  VERDICT: fill operator.csv and cash.csv before arguing with the vision.")

    lines.append("")
    lines.append("Paper tickets (not funding):")
    lines.append(f"  paper={tickets.paper}  passed={tickets.passed}  live={tickets.live}")
    lines.append(f"  fill_source worst={tickets.worst_fills}  mid={tickets.mid_fills}")
    if tickets.mid_fills:
        lines.append("  INVALID for S4: mid fills present. Mid is a lie.")
    if tickets.live:
        lines.append("  LIVE rows exist. Live is not a start step. See docs/START.md S4.")
    if tickets.paper_result_n:
        lines.append(
            f"  Settled paper P&L ({tickets.paper_result_n} tickets): "
            f"{_money(tickets.paper_result)}  — synthetic; cannot promote."
        )
    lines.append("")
    return "\n".join(lines)


def run(journal: Path) -> str:
    cash = latest_cash(read_csv(journal / "cash.csv"))
    invoices = summarize_invoices(read_csv(journal / "invoices.csv"))
    tickets = summarize_tickets(read_csv(journal / "tickets.csv"))
    return render(cash, invoices, tickets)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--journal",
        type=Path,
        default=Path("journal"),
        help="directory with cash.csv, invoices.csv, tickets.csv",
    )
    args = parser.parse_args(argv)
    try:
        sys.stdout.write(run(args.journal))
    except FileNotFoundError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    except ValueError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
