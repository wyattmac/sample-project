#!/usr/bin/env python3
import unittest
from datetime import date, timedelta
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data.theta import (  # noqa: E402
    MARKET_DATA_VENDOR,
    PAPER_ROOTS,
    PaperRootError,
    Quote,
    expirations_in_dte_window,
    list_expirations,
    paper_root,
    ping,
    snapshot_quotes,
)


class FakeFrame:
    def __init__(self, rows: list[dict]):
        self._rows = rows
        self.columns = list(rows[0].keys()) if rows else []

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, key):
        return [row[key] for row in self._rows]


class FakeTheta:
    def __init__(self, fail_quotes: bool = False):
        self.fail_quotes = fail_quotes
        today = date(2026, 8, 19)
        self.expirations = FakeFrame(
            [
                {"symbol": "SPY", "expiration": today + timedelta(days=d)}
                for d in (7, 37, 90)
            ]
        )
        self.quotes = FakeFrame(
            [
                {
                    "symbol": "SPY",
                    "expiration": today + timedelta(days=37),
                    "strike": 630.0,
                    "right": "P",
                    "bid": 4.10,
                    "ask": 4.30,
                    "timestamp": "2026-08-19T15:00:00",
                },
                {
                    "symbol": "SPY",
                    "expiration": today + timedelta(days=37),
                    "strike": 670.0,
                    "right": "C",
                    "bid": 3.80,
                    "ask": 4.00,
                    "timestamp": "2026-08-19T15:00:00",
                },
            ]
        )

    def option_list_expirations(self, symbol: str):
        return self.expirations

    def option_snapshot_quote(self, symbol, expiration, **kwargs):
        if self.fail_quotes:
            raise RuntimeError("empty snapshot cache")
        return self.quotes


class ThetaPipeTests(unittest.TestCase):
    def test_vendor_is_theta_not_ibkr(self):
        self.assertEqual(MARKET_DATA_VENDOR, "theta")
        self.assertEqual(PAPER_ROOTS, frozenset({"SPY", "XSP"}))
        from data.theta import DEFAULT_PAPER_ROOT

        self.assertEqual(DEFAULT_PAPER_ROOT, "SPY")

    def test_rejects_universe_creep(self):
        with self.assertRaises(PaperRootError):
            paper_root("AAPL")
        with self.assertRaises(PaperRootError):
            ping("QQQ", client=FakeTheta())

    def test_dte_window_picks_the_paper_expiry(self):
        as_of = date(2026, 8, 19)
        exps = [as_of + timedelta(days=d) for d in (7, 37, 90)]
        window = expirations_in_dte_window(exps, as_of=as_of)
        self.assertEqual(window, [as_of + timedelta(days=37)])

    def test_quotes_use_bid_as_worst_sell(self):
        q = Quote("SPY", date(2026, 9, 25), 630.0, "P", bid=4.10, ask=4.30)
        self.assertEqual(q.worst_sell, 4.10)
        self.assertEqual(q.worst_buy, 4.30)

    def test_ping_ok_on_fake_client(self):
        result = ping("spy", client=FakeTheta(), as_of=date(2026, 8, 19))
        self.assertEqual(result.vendor, "theta")
        self.assertEqual(result.symbol, "SPY")
        self.assertEqual(result.expiration_count, 3)
        self.assertEqual(result.quote_count, 2)
        self.assertEqual(result.note, "ok")

    def test_ping_survives_closed_market(self):
        result = ping(
            "SPY",
            client=FakeTheta(fail_quotes=True),
            as_of=date(2026, 8, 19),
        )
        self.assertEqual(result.quote_count, 0)
        self.assertIn("empty snapshot cache", result.note)

    def test_list_and_snapshot_round_trip(self):
        client = FakeTheta()
        exps = list_expirations(client, "SPY")
        self.assertEqual(len(exps), 3)
        quotes = snapshot_quotes(client, "SPY", exps[1])
        self.assertEqual(len(quotes), 2)
        self.assertEqual(quotes[0].worst_sell, 4.10)


if __name__ == "__main__":
    unittest.main()
