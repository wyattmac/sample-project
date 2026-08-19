"""Fixed paper policy. Not a model. Do not edit these to 'learn'."""

from __future__ import annotations

SYMBOL = "SPY"
MIN_DTE = 30
MAX_DTE = 45
SHORT_DELTA = 0.15
WING_WIDTHS = (5.0, 10.0)  # dollars, tried in order until 1% cap fits
IV_RANK_MIN = 50.0
TICKET_CAP = 0.01
BOOK_CAP = 0.03
MULTIPLIER = 100
KILL_AFTER_TICKETS = 20
STRUCTURE = "iron_condor"
FILL_SOURCE = "worst"
MARKET_DATA_VENDOR = "theta"
