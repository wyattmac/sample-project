#!/usr/bin/env python3
"""Shim: canonical math lives in paper.size."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper.size import book_lots_allowed, max_loss_one, size_contracts  # noqa: E402
from paper.policy import BOOK_CAP, TICKET_CAP  # noqa: E402


def _money(n: float) -> str:
    return f"${n:,.0f}"


def size(equity: float, width: float, credit: float) -> dict:
    one = max_loss_one(width, credit)
    n = size_contracts(equity, width, credit)
    return {
        "equity": equity,
        "width": width,
        "credit": credit,
        "max_loss_1lot": one,
        "ticket_cap": equity * TICKET_CAP,
        "book_cap": equity * BOOK_CAP,
        "contracts": n,
        "cash_this_ticket": n * one,
        "open_lots": book_lots_allowed(equity, width, credit),
    }


def render(equity: float, width: float, credit: float) -> str:
    one = max_loss_one(width, credit)
    n = size_contracts(equity, width, credit)
    ticket_cap = equity * TICKET_CAP
    book_cap = equity * BOOK_CAP
    lines = [
        "Defined-risk iron condor — cash ≈ max loss",
        f"  Equity:                 {_money(equity)}",
        f"  Wings:                  ${width:.2f} wide",
        f"  Net credit (1 lot):     ${credit:.2f}",
        f"  Max loss, 1 lot:        {_money(one)}",
        f"  1% ticket cap:          {_money(ticket_cap)}",
        f"  3% book cap:            {_money(book_cap)}",
        "",
    ]
    if n < 1:
        lines.append(
            "  VERDICT: 1-lot max loss exceeds 1% cap. Skip, or narrower wings / put-spread substitute."
        )
    else:
        lines.append(
            f"  VERDICT: {n} lot(s) this ticket "
            f"({_money(n * one)} cash). "
            f"Book cap allows {book_lots_allowed(equity, width, credit)} such lots open in total."
        )
    lines.append("  Sweep cushion: keep ~3% of equity unencumbered so SGOV is not force-sold.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--equity", type=float, required=True)
    p.add_argument("--width", type=float, required=True)
    p.add_argument("--credit", type=float, required=True)
    args = p.parse_args(argv)
    try:
        sys.stdout.write(render(args.equity, args.width, args.credit))
    except ValueError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
