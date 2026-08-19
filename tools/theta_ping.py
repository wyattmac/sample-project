#!/usr/bin/env python3
"""Ping Theta Data for the single paper underlier. Not a scanner.

  export THETADATA_API_KEY=...
  python3 tools/theta_ping.py --symbol SPY
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data.theta import PaperRootError, ping  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbol",
        default="SPY",
        help="paper root: SPY (default). XSP allowed by the pipe, not by the paper mandate.",
    )
    args = parser.parse_args(argv)
    try:
        result = ping(args.symbol)
    except PaperRootError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    except ImportError as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    print(f"vendor:              {result.vendor}")
    print(f"symbol:              {result.symbol}")
    print(f"expirations listed:  {result.expiration_count}")
    window = ", ".join(d.isoformat() for d in result.window_expirations) or "(none)"
    print(f"30-45 DTE window:    {window}")
    print(f"quote expiration:    {result.quote_expiration or '(none)'}")
    print(f"quote rows:          {result.quote_count}")
    print(f"note:                {result.note}")
    if result.vendor != "theta":
        sys.stderr.write("error: market data vendor is not theta\n")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
