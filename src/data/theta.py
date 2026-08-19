# Market data is Theta Data. Brokers are not quote sources.
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Optional, Protocol

MARKET_DATA_VENDOR = "theta"
PAPER_ROOTS = frozenset({"SPY", "XSP"})
DEFAULT_MIN_DTE = 30
DEFAULT_MAX_DTE = 45
DEFAULT_STRIKE_RANGE = 8  # 8 above + 8 below + ATM ≈ 17 strikes, not the wing farm


class ThetaLike(Protocol):
    def option_list_expirations(self, symbol: str) -> Any: ...

    def option_snapshot_quote(
        self,
        symbol: str,
        expiration: date,
        strike: str = "*",
        right: str = "both",
        max_dte: Optional[int] = None,
        strike_range: Optional[int] = None,
    ) -> Any: ...


class PaperRootError(ValueError):
    pass


def paper_root(symbol: str) -> str:
    root = symbol.strip().upper()
    if root not in PAPER_ROOTS:
        raise PaperRootError(
            f"Theta paper pipe may only request {sorted(PAPER_ROOTS)}, not {root!r}. "
            "One underlier. Not the sky."
        )
    return root


def connect(client: Optional[ThetaLike] = None) -> ThetaLike:
    if client is not None:
        return client
    try:
        from thetadata import ThetaClient
    except ImportError as e:
        raise ImportError(
            "thetadata is not installed. pip install thetadata "
            "(Python 3.12+, package >= 1.0.9). "
            "Do not install ib_insync for quotes."
        ) from e
    return ThetaClient()


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


def _as_date(item: Any) -> date:
    if isinstance(item, datetime):
        return item.date()
    if isinstance(item, date):
        return item
    return date.fromisoformat(str(item)[:10])


def list_expirations(client: ThetaLike, symbol: str) -> list[date]:
    root = paper_root(symbol)
    frame = client.option_list_expirations(symbol=root)
    raw = _column(frame, "expiration")
    return sorted({_as_date(item) for item in raw})


def expirations_in_dte_window(
    expirations: list[date],
    *,
    as_of: Optional[date] = None,
    min_dte: int = DEFAULT_MIN_DTE,
    max_dte: int = DEFAULT_MAX_DTE,
) -> list[date]:
    today = as_of or date.today()
    picked: list[date] = []
    for exp in expirations:
        dte = (exp - today).days
        if min_dte <= dte <= max_dte:
            picked.append(exp)
    return picked


@dataclass(frozen=True)
class Quote:
    symbol: str
    expiration: date
    strike: float
    right: str
    bid: float
    ask: float
    timestamp: Optional[str] = None

    @property
    def worst_sell(self) -> float:
        """Price you get when you sell this contract."""
        return self.bid

    @property
    def worst_buy(self) -> float:
        """Price you pay when you buy this contract."""
        return self.ask


def snapshot_quotes(
    client: ThetaLike,
    symbol: str,
    expiration: date,
    *,
    strike_range: int = DEFAULT_STRIKE_RANGE,
    max_dte: int = DEFAULT_MAX_DTE,
) -> list[Quote]:
    root = paper_root(symbol)
    frame = client.option_snapshot_quote(
        symbol=root,
        expiration=expiration,
        strike="*",
        right="both",
        max_dte=max_dte,
        strike_range=strike_range,
    )
    n = len(frame)
    symbols = _column(frame, "symbol")
    exps = _column(frame, "expiration")
    strikes = _column(frame, "strike")
    rights = _column(frame, "right")
    bids = _column(frame, "bid")
    asks = _column(frame, "ask")
    try:
        stamps = _column(frame, "timestamp")
    except KeyError:
        stamps = [None] * n
    quotes: list[Quote] = []
    for i in range(n):
        exp = exps[i]
        exp = _as_date(exp)
        quotes.append(
            Quote(
                symbol=str(symbols[i]),
                expiration=exp,
                strike=float(strikes[i]),
                right=str(rights[i]).upper()[:1],
                bid=float(bids[i]),
                ask=float(asks[i]),
                timestamp=None if stamps[i] is None else str(stamps[i]),
            )
        )
    return quotes


@dataclass(frozen=True)
class PingResult:
    vendor: str
    symbol: str
    expiration_count: int
    window_expirations: list[date]
    quote_count: int
    quote_expiration: Optional[date]
    note: str


def ping(
    symbol: str = "SPY",
    *,
    client: Optional[ThetaLike] = None,
    as_of: Optional[date] = None,
) -> PingResult:
    root = paper_root(symbol)
    pipe = connect(client)
    expirations = list_expirations(pipe, root)
    window = expirations_in_dte_window(expirations, as_of=as_of)
    if not window:
        return PingResult(
            vendor=MARKET_DATA_VENDOR,
            symbol=root,
            expiration_count=len(expirations),
            window_expirations=[],
            quote_count=0,
            quote_expiration=None,
            note="no expiration in 30–45 DTE window",
        )
    target = window[0]
    try:
        quotes = snapshot_quotes(pipe, root, target)
    except Exception as exc:  # market closed → empty snapshot cache
        return PingResult(
            vendor=MARKET_DATA_VENDOR,
            symbol=root,
            expiration_count=len(expirations),
            window_expirations=window,
            quote_count=0,
            quote_expiration=target,
            note=f"quote snapshot empty or failed ({type(exc).__name__}: {exc}). "
            "Theta resets the snapshot cache at midnight ET; this is normal off-hours.",
        )
    return PingResult(
        vendor=MARKET_DATA_VENDOR,
        symbol=root,
        expiration_count=len(expirations),
        window_expirations=window,
        quote_count=len(quotes),
        quote_expiration=target,
        note="ok" if quotes else "zero rows — likely off-hours snapshot cache",
    )
