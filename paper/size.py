"""Cash ≈ max loss for a defined-risk iron condor."""

from __future__ import annotations

import math

from paper.policy import BOOK_CAP, MULTIPLIER, TICKET_CAP


def max_loss_one(width: float, credit: float) -> float:
    if width <= 0:
        raise ValueError("width must be positive")
    if credit < 0:
        raise ValueError("credit cannot be negative")
    if credit >= width:
        raise ValueError(
            "credit >= width means max loss would be zero or negative; check the quote"
        )
    return (width - credit) * MULTIPLIER


def size_contracts(equity: float, width: float, credit: float) -> int:
    if equity <= 0:
        raise ValueError("equity must be positive")
    one = max_loss_one(width, credit)
    cap = equity * TICKET_CAP
    if one <= 0:
        return 0
    return math.floor(cap / one)


def book_lots_allowed(equity: float, width: float, credit: float) -> int:
    one = max_loss_one(width, credit)
    if one <= 0:
        return 0
    return math.floor(equity * BOOK_CAP / one)
