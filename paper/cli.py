"""One command. Tape → picker → journal → verdict."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from paper.journal import (
    DEFAULT_JOURNAL,
    append_decision,
    load_operator,
    open_max_loss,
)
from paper.picker import pick
from paper.policy import SYMBOL
from paper.tape import PaperRootError, load
from paper.verdict import rule_verdict


def _print_decision(decision, snap) -> None:
    print(f"tape:     {snap.source}  as_of={snap.as_of.isoformat()}  {snap.symbol}")
    print(f"spot:     {snap.spot if snap.spot is not None else '—'}")
    print(f"iv_rank:  {snap.iv_rank if snap.iv_rank is not None else '—'} ({snap.iv_rank_source})")
    print(f"status:   {decision.status}")
    print(f"reason:   {decision.reason}")
    if decision.take:
        print(
            f"condor:   {decision.short_put:.0f}/{decision.long_put:.0f} "
            f"{decision.short_call:.0f}/{decision.long_call:.0f}  "
            f"{decision.dte}DTE  {decision.contracts} lot(s)"
        )
        print(f"credit:   ${decision.credit_usd:.2f}  (worst side, fill_source={decision.fill_source})")
        print(f"max loss: ${decision.max_loss_usd:.0f}")
        print(f"thesis:   {decision.thesis}")
    print()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Paper one SPY iron condor at worst-side quotes. No broker. No LLM."
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="pull SPY from Theta (needs THETADATA_API_KEY). Default: fixture.",
    )
    parser.add_argument("--fixture", type=Path, default=None)
    parser.add_argument("--equity", type=float, default=None)
    parser.add_argument("--journal", type=Path, default=DEFAULT_JOURNAL)
    parser.add_argument(
        "--write",
        action="store_true",
        help="append the decision to journal/tickets.csv",
    )
    parser.add_argument(
        "--verdict",
        action="store_true",
        help="print the kill-rule scorekeeper and cash excess",
    )
    args = parser.parse_args(argv)

    if args.verdict and not args.write:
        sys.stdout.write(rule_verdict(args.journal))
        tools = Path(__file__).resolve().parents[1] / "tools"
        sys.path.insert(0, str(tools))
        try:
            import excess  # noqa: WPS433

            sys.stdout.write(excess.run(args.journal))
        except Exception as e:
            sys.stdout.write(f"(excess unavailable: {e})\n")
        return 0

    op = load_operator(args.journal)
    equity = args.equity
    if equity is None:
        equity = op.equity if op else None
    if equity is None:
        sys.stderr.write(
            "error: fill journal/operator.csv equity_usd or pass --equity\n"
        )
        return 2
    if op and op.paper_underlier and op.paper_underlier != SYMBOL:
        sys.stderr.write(
            f"error: operator paper_underlier is {op.paper_underlier}; this app is {SYMBOL} only\n"
        )
        return 2
    if op and op.data_vendor and op.data_vendor != "theta":
        sys.stderr.write("error: data_vendor must be theta\n")
        return 2

    try:
        snap = load(live=args.live, fixture=args.fixture)
    except (PaperRootError, ImportError, RuntimeError, FileNotFoundError) as e:
        sys.stderr.write(f"error: {e}\n")
        return 2

    decision = pick(
        snap,
        equity=equity,
        open_max_loss=open_max_loss(args.journal),
    )
    _print_decision(decision, snap)

    if args.write:
        path = append_decision(decision, as_of=snap.as_of, journal=args.journal)
        print(f"wrote {path}")

    if args.verdict:
        sys.stdout.write(rule_verdict(args.journal))

    return 0
