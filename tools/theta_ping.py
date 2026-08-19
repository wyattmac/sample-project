#!/usr/bin/env python3
"""Ping Theta for SPY. Prefer: python3 -m paper --live"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from paper.tape import PaperRootError, load_theta, require_spy  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbol", default="SPY")
    args = parser.parse_args(argv)
    try:
        require_spy(args.symbol)
        snap = load_theta(args.symbol)
    except (PaperRootError, ImportError, RuntimeError) as e:
        sys.stderr.write(f"error: {e}\n")
        return 2
    print(f"vendor:              theta")
    print(f"symbol:              {snap.symbol}")
    print(f"source:              {snap.source}")
    print(f"quote rows:          {len(snap.quotes)}")
    window = ", ".join(d.isoformat() for d in snap.window_expirations()) or "(none)"
    print(f"30-45 DTE window:    {window}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
