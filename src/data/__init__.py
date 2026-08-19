"""Data plane. Options quotes come from Theta, never from a broker."""

from .theta import (
    MARKET_DATA_VENDOR,
    PAPER_ROOTS,
    PaperRootError,
    PingResult,
    Quote,
    connect,
    paper_root,
    ping,
    snapshot_quotes,
)

__all__ = [
    "MARKET_DATA_VENDOR",
    "PAPER_ROOTS",
    "PaperRootError",
    "PingResult",
    "Quote",
    "connect",
    "paper_root",
    "ping",
    "snapshot_quotes",
]
