#!/usr/bin/env python3
"""Cash tied up by one defined-risk iron condor.

  python3 tools/ticket_cash.py --equity 100000 --width 5 --credit 1.20

max loss = (width - credit) * 100 * contracts, capped at 1% of equity.
"""

from __future__ import annotations

import argparse
import math
import sys


MULTIPLIER = 100
TICKET_CAP = 0.01
BOOK_CAP = 0.03


def max_loss_one(width: float, credit: float) -> float:
    if width <= 0:
        raise ValueError("width must be positive")
    if credit < 0:
        raise ValueError("credit cannot be negative")
    if credit >= width:
        raise ValueError("credit >= width means max loss would be zero or negative; check the quote")
    return (width - credit) * MULTIPLIER


def size(equity: float, width: float, credit: float) -> dict:
    if equity <= 0:
        raise ValueError("equity must be positive")
    one = max_loss_one(width, credit)
    ticket_cap = equity * TICKET_CAP
    book_cap = equity * BOOK_CAP
    n = math.floor(ticket_cap / one) if one > 0 else 0
    return {
        "equity": equity,
        "width": width,
        "credit": credit,
        "max_loss_1lot": one,
        "ticket_cap": ticket_cap,
        "book_cap": book_cap,
        "contracts": n,
        "cash_this_ticket": n * one,
        "open_lots": math.floor(book_cap / one) if one > 0 else 0,
    }


def _money(n: float) -> str:
    return f"${n:,.0f}"


def render(s: dict) -> str:
    lines = [
        "Defined-risk iron condor — cash ≈ max loss",
        f"  Equity:                 {_money(s['equity'])}",
        f"  Wings:                  ${s['width']:.2f} wide",
        f"  Net credit (1 lot):     ${s['credit']:.2f}",
        f"  Max loss, 1 lot:        {_money(s['max_loss_1lot'])}",
        f"  1% ticket cap:          {_money(s['ticket_cap'])}",
        f"  3% book cap:            {_money(s['book_cap'])}",
        "",
    ]
    if s["contracts"] < 1:
        lines.append(
            f"  VERDICT: 1-lot max loss exceeds 1% cap. Skip, or narrower wings / put-spread substitute."
        )
    else:
        lines.append(
            f"  VERDICT: {s['contracts']} lot(s) this ticket "
            f"({_money(s['cash_this_ticket'])} cash). "
            f"Book cap allows {s['open_lots']} such lots open in total."
        )
    lines.append("  Sweep cushion: keep ~3% of equity unencumbered so SGOV is not force-sold.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--equity", type=float, required=True)
    p.add_argument("--width", type=float, required=True, help="wing width in dollars, e.g. 5")
    p.add_argument("--credit", type=float, required=True, help="net credit per 1-lot, worst side")
    args = p.parse_args(argv)
    try:
        sys.stdout.write(render(size(args.equity, args.width, args.credit)))
    except ValueError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
