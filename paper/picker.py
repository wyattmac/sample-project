"""Pick a defined-risk SPY iron condor or pass. No learning."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from paper.policy import (
    BOOK_CAP,
    FILL_SOURCE,
    IV_RANK_MIN,
    SHORT_DELTA,
    STRUCTURE,
    SYMBOL,
    WING_WIDTHS,
)
from paper.size import max_loss_one, size_contracts
from paper.tape import Contract, Snapshot


@dataclass(frozen=True)
class Decision:
    status: str  # paper | passed
    reason: str
    underlier: str = SYMBOL
    structure: str = STRUCTURE
    dte: Optional[int] = None
    expiration: Optional[str] = None
    iv_rank: Optional[float] = None
    iv_rank_source: str = ""
    short_put: Optional[float] = None
    long_put: Optional[float] = None
    short_call: Optional[float] = None
    long_call: Optional[float] = None
    width: Optional[float] = None
    credit_usd: Optional[float] = None
    max_loss_usd: Optional[float] = None
    contracts: int = 0
    fill_source: str = FILL_SOURCE
    thesis: str = ""

    @property
    def take(self) -> bool:
        return self.status == "paper"


def _closest_delta(chain: list[Contract], right: str, target: float) -> Optional[Contract]:
    candidates = [c for c in chain if c.right == right and c.delta is not None]
    if not candidates:
        return None
    return min(candidates, key=lambda c: abs(float(c.delta) - target))


def _at_strike(chain: list[Contract], right: str, strike: float) -> Optional[Contract]:
    hits = [c for c in chain if c.right == right and abs(c.strike - strike) < 1e-6]
    return hits[0] if hits else None


def pick(
    snap: Snapshot,
    *,
    equity: float,
    open_max_loss: float = 0.0,
) -> Decision:
    if snap.symbol != SYMBOL:
        return Decision(status="passed", reason=f"underlier {snap.symbol} is not {SYMBOL}")

    iv_rank = snap.iv_rank
    source = snap.iv_rank_source
    if iv_rank is None:
        return Decision(
            status="passed",
            reason="IV rank missing; skip the week rather than borrow a website rank",
            iv_rank_source=source,
        )
    if iv_rank < IV_RANK_MIN:
        return Decision(
            status="passed",
            reason=f"IV rank {iv_rank:.0f} < {IV_RANK_MIN:.0f}",
            iv_rank=iv_rank,
            iv_rank_source=source,
        )

    window = snap.window_expirations()
    if not window:
        return Decision(
            status="passed",
            reason="no expiration in 30–45 DTE",
            iv_rank=iv_rank,
            iv_rank_source=source,
        )
    expiration = min(window, key=lambda e: abs(snap.dte(e) - 37))
    dte = snap.dte(expiration)
    chain = snap.chain(expiration)
    if not chain:
        return Decision(
            status="passed",
            reason="empty chain on the window expiry",
            dte=dte,
            expiration=expiration.isoformat(),
            iv_rank=iv_rank,
            iv_rank_source=source,
        )

    short_put = _closest_delta(chain, "P", -SHORT_DELTA)
    short_call = _closest_delta(chain, "C", SHORT_DELTA)
    if short_put is None or short_call is None:
        return Decision(
            status="passed",
            reason="no 15-delta shorts (tape needs delta)",
            dte=dte,
            expiration=expiration.isoformat(),
            iv_rank=iv_rank,
            iv_rank_source=source,
        )

    best: Optional[Decision] = None
    last_reason = "no wing width fit the 1% cap"
    for width in WING_WIDTHS:
        long_put = _at_strike(chain, "P", short_put.strike - width)
        long_call = _at_strike(chain, "C", short_call.strike + width)
        if long_put is None or long_call is None:
            last_reason = f"${width:.0f} wings missing on the chain"
            continue
        credit = (
            short_put.worst_sell
            + short_call.worst_sell
            - long_put.worst_buy
            - long_call.worst_buy
        )
        if credit <= 0:
            last_reason = f"${width:.0f} wings: worst-side credit {credit:.2f} ≤ 0"
            continue
        try:
            one = max_loss_one(width, credit)
        except ValueError as e:
            last_reason = str(e)
            continue
        n = size_contracts(equity, width, credit)
        ticket_loss = n * one
        if n < 1:
            last_reason = (
                f"${width:.0f} wings: 1-lot max loss ${one:.0f} exceeds 1% of equity"
            )
            continue
        if open_max_loss + ticket_loss > equity * BOOK_CAP + 1e-6:
            last_reason = "concurrent max loss would exceed 3% of equity"
            continue
        thesis = (
            f"SPY {dte}DTE IC {short_put.strike:.0f}/{long_put.strike:.0f} "
            f"{short_call.strike:.0f}/{long_call.strike:.0f} "
            f"IVR {iv_rank:.0f}; worst-side credit ${credit:.2f}; {n} lot(s)"
        )
        best = Decision(
            status="paper",
            reason="take",
            dte=dte,
            expiration=expiration.isoformat(),
            iv_rank=iv_rank,
            iv_rank_source=source,
            short_put=short_put.strike,
            long_put=long_put.strike,
            short_call=short_call.strike,
            long_call=long_call.strike,
            width=width,
            credit_usd=round(credit * 100 * n, 2),
            max_loss_usd=round(ticket_loss, 2),
            contracts=n,
            thesis=thesis,
        )
        break
    if best is None:
        return Decision(
            status="passed",
            reason=last_reason,
            dte=dte,
            expiration=expiration.isoformat(),
            iv_rank=iv_rank,
            iv_rank_source=source,
        )
    return best
