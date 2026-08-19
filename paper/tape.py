"""Quote tape. Fixture by default. Theta is an adapter, not the picker."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Optional

from paper.policy import MARKET_DATA_VENDOR, MAX_DTE, MIN_DTE, SYMBOL

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = REPO_ROOT / "fixtures" / "spy_take.json"


class PaperRootError(ValueError):
    pass


def require_spy(symbol: str) -> str:
    root = symbol.strip().upper()
    if root != SYMBOL:
        raise PaperRootError(
            f"paper tape is {SYMBOL} only, not {root!r}. One underlier. Not the sky."
        )
    return root


def _as_date(item: Any) -> date:
    if isinstance(item, datetime):
        return item.date()
    if isinstance(item, date):
        return item
    return date.fromisoformat(str(item)[:10])


@dataclass(frozen=True)
class Contract:
    expiration: date
    strike: float
    right: str
    bid: float
    ask: float
    delta: Optional[float] = None
    iv: Optional[float] = None

    @property
    def worst_sell(self) -> float:
        return self.bid

    @property
    def worst_buy(self) -> float:
        return self.ask

    def tradable(self) -> bool:
        return self.bid > 0 and self.ask >= self.bid


@dataclass(frozen=True)
class Snapshot:
    as_of: date
    symbol: str
    spot: Optional[float]
    iv_rank: Optional[float]
    iv_rank_source: str
    quotes: tuple[Contract, ...]
    source: str

    def dte(self, expiration: date) -> int:
        return (expiration - self.as_of).days

    def window_expirations(self) -> list[date]:
        found = sorted({q.expiration for q in self.quotes})
        return [exp for exp in found if MIN_DTE <= self.dte(exp) <= MAX_DTE]

    def chain(self, expiration: date) -> list[Contract]:
        return [q for q in self.quotes if q.expiration == expiration and q.tradable()]


def load_fixture(path: Path | None = None) -> Snapshot:
    fixture = path or DEFAULT_FIXTURE
    raw = json.loads(fixture.read_text())
    symbol = require_spy(raw["symbol"])
    quotes = []
    for row in raw["quotes"]:
        quotes.append(
            Contract(
                expiration=_as_date(row["expiration"]),
                strike=float(row["strike"]),
                right=str(row["right"]).upper()[:1],
                bid=float(row["bid"]),
                ask=float(row["ask"]),
                delta=None if row.get("delta") is None else float(row["delta"]),
                iv=None if row.get("iv") is None else float(row["iv"]),
            )
        )
    iv_rank = raw.get("iv_rank")
    return Snapshot(
        as_of=_as_date(raw["as_of"]),
        symbol=symbol,
        spot=None if raw.get("spot") is None else float(raw["spot"]),
        iv_rank=None if iv_rank is None else float(iv_rank),
        iv_rank_source=str(raw.get("iv_rank_source") or "fixture"),
        quotes=tuple(quotes),
        source=f"fixture:{fixture.name}",
    )


def _column(frame: Any, *names: str) -> list:
    cols = getattr(frame, "columns", None)
    if cols is not None:
        available = [str(c) for c in list(cols)]
        for name in names:
            if name in available:
                return list(frame[name])
    if isinstance(frame, list) and frame and isinstance(frame[0], dict):
        for name in names:
            if name in frame[0]:
                return [row[name] for row in frame]
    raise KeyError(f"could not find columns {names} on Theta response")


def load_theta(symbol: str = SYMBOL) -> Snapshot:
    """Live Theta snapshot for SPY. Requires THETADATA_API_KEY and thetadata."""
    root = require_spy(symbol)
    try:
        from thetadata import ThetaClient
    except ImportError as e:
        raise ImportError(
            "thetadata is not installed. pip install thetadata. Or omit --live and use the fixture."
        ) from e
    if not os.environ.get("THETADATA_API_KEY") and not Path("creds.txt").exists():
        raise RuntimeError(
            "no THETADATA_API_KEY (and no creds.txt). Use the fixture or export the key."
        )
    client = ThetaClient()
    today = date.today()
    try:
        exp_frame = client.option_list_expirations(symbol=root)
        expirations = sorted({_as_date(x) for x in _column(exp_frame, "expiration")})
    except Exception as e:
        raise RuntimeError(f"Theta expirations failed: {e}") from e
    window = [e for e in expirations if MIN_DTE <= (e - today).days <= MAX_DTE]
    if not window:
        return Snapshot(
            as_of=today,
            symbol=root,
            spot=None,
            iv_rank=None,
            iv_rank_source="theta",
            quotes=(),
            source="theta",
        )
    target = min(window, key=lambda e: abs((e - today).days - 37))
    quotes: list[Contract] = []
    greeks_by_key: dict[tuple, float] = {}
    try:
        greeks = client.option_snapshot_greeks_all(
            symbol=root,
            expiration=target,
            strike="*",
            right="both",
        )
        n = len(greeks)
        for i in range(n):
            exp = _as_date(_column(greeks, "expiration")[i])
            strike = float(_column(greeks, "strike")[i])
            right = str(_column(greeks, "right")[i]).upper()[:1]
            try:
                delta = float(_column(greeks, "delta")[i])
            except (KeyError, TypeError, ValueError):
                continue
            greeks_by_key[(exp, strike, right)] = delta
    except Exception:
        greeks_by_key = {}
    try:
        frame = client.option_snapshot_quote(
            symbol=root,
            expiration=target,
            strike="*",
            right="both",
            max_dte=MAX_DTE,
        )
        n = len(frame)
        for i in range(n):
            exp = _as_date(_column(frame, "expiration")[i])
            strike = float(_column(frame, "strike")[i])
            right = str(_column(frame, "right")[i]).upper()[:1]
            quotes.append(
                Contract(
                    expiration=exp,
                    strike=strike,
                    right=right,
                    bid=float(_column(frame, "bid")[i]),
                    ask=float(_column(frame, "ask")[i]),
                    delta=greeks_by_key.get((exp, strike, right)),
                )
            )
    except Exception as e:
        raise RuntimeError(
            f"Theta quote snapshot failed ({type(e).__name__}: {e}). "
            "Off-hours cache is often empty. Use the fixture."
        ) from e
    return Snapshot(
        as_of=today,
        symbol=root,
        spot=None,
        iv_rank=None,
        iv_rank_source="theta",
        quotes=tuple(quotes),
        source="theta",
    )


def load(*, live: bool = False, fixture: Path | None = None) -> Snapshot:
    if live:
        return load_theta(SYMBOL)
    return load_fixture(fixture)
