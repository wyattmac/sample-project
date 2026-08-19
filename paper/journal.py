"""Append-only CSV journal. The product."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Optional

from paper.picker import Decision

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JOURNAL = REPO_ROOT / "journal"

TICKET_FIELDS = [
    "date",
    "status",
    "underlier",
    "structure",
    "dte",
    "expiration",
    "iv_rank",
    "iv_rank_source",
    "width",
    "contracts",
    "short_put",
    "long_put",
    "short_call",
    "long_call",
    "max_loss_usd",
    "credit_usd",
    "fill_source",
    "thesis",
    "result_usd",
    "notes",
]


def _blank(v) -> str:
    if v is None:
        return ""
    return str(v)


@dataclass(frozen=True)
class Operator:
    equity: float
    paper_underlier: str
    data_vendor: str
    theta_plan: str


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def load_operator(journal: Path | None = None) -> Optional[Operator]:
    path = (journal or DEFAULT_JOURNAL) / "operator.csv"
    for row in _rows(path):
        raw = (row.get("equity_usd") or "").strip()
        if not raw:
            continue
        return Operator(
            equity=float(raw),
            paper_underlier=(row.get("paper_underlier") or "SPY").strip().upper() or "SPY",
            data_vendor=(row.get("data_vendor") or "").strip().lower(),
            theta_plan=(row.get("theta_plan") or "").strip().lower(),
        )
    return None


def open_max_loss(journal: Path | None = None) -> float:
    path = (journal or DEFAULT_JOURNAL) / "tickets.csv"
    total = 0.0
    for row in _rows(path):
        if (row.get("status") or "").strip().lower() != "paper":
            continue
        if (row.get("result_usd") or "").strip() != "":
            continue
        raw = (row.get("max_loss_usd") or "").strip()
        if raw:
            total += float(raw)
    return total


def settled_paper(journal: Path | None = None) -> tuple[int, float]:
    path = (journal or DEFAULT_JOURNAL) / "tickets.csv"
    n = 0
    pnl = 0.0
    for row in _rows(path):
        if (row.get("status") or "").strip().lower() != "paper":
            continue
        raw = (row.get("result_usd") or "").strip()
        if raw == "":
            continue
        n += 1
        pnl += float(raw)
    return n, pnl


def write_tickets(rows: list[dict], journal: Path | None = None) -> Path:
    path = (journal or DEFAULT_JOURNAL) / "tickets.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TICKET_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") or "" for k in TICKET_FIELDS})
    return path


def load_tickets(journal: Path | None = None) -> list[dict]:
    return _rows((journal or DEFAULT_JOURNAL) / "tickets.csv")


def append_decision(
    decision: Decision,
    *,
    as_of: date,
    journal: Path | None = None,
    notes: str = "",
) -> Path:
    path = (journal or DEFAULT_JOURNAL) / "tickets.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists() or path.stat().st_size == 0
    fill = decision.fill_source if decision.take else ""
    if decision.take and fill != "worst":
        raise ValueError("refusing to write a take that is not fill_source=worst")
    row = {
        "date": as_of.isoformat(),
        "status": decision.status,
        "underlier": decision.underlier,
        "structure": decision.structure if decision.take else "",
        "dte": _blank(decision.dte),
        "expiration": _blank(decision.expiration),
        "iv_rank": _blank(decision.iv_rank),
        "iv_rank_source": decision.iv_rank_source,
        "width": _blank(decision.width if decision.take else None),
        "contracts": _blank(decision.contracts if decision.take else None),
        "short_put": _blank(decision.short_put if decision.take else None),
        "long_put": _blank(decision.long_put if decision.take else None),
        "short_call": _blank(decision.short_call if decision.take else None),
        "long_call": _blank(decision.long_call if decision.take else None),
        "max_loss_usd": _blank(decision.max_loss_usd if decision.take else None),
        "credit_usd": _blank(decision.credit_usd if decision.take else None),
        "fill_source": fill,
        "thesis": decision.thesis or decision.reason,
        "result_usd": "",
        "notes": notes or decision.reason,
    }
    with path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TICKET_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(row)
    return path
