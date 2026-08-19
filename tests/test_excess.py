#!/usr/bin/env python3
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import excess  # noqa: E402


class ExcessTests(unittest.TestCase):
    def test_demo_journal_invoices_eat_the_edge(self):
        text = excess.run(ROOT / "journal" / "examples")
        self.assertIn("Vehicle vs SGOV", text)
        self.assertIn("VERDICT: invoices eat the cash edge", text)
        self.assertIn("fill_source worst=1", text)
        self.assertNotIn("INVALID for S4", text)

    def test_empty_live_journal_does_not_crash(self):
        text = excess.run(ROOT / "journal")
        self.assertIn("no complete snapshot", text)
        self.assertIn("Invoices: none", text)

    def test_sgov_equals_vehicle_is_a_settings_page(self):
        snap = excess.CashSnapshot(
            as_of=excess.date(2026, 8, 19),
            equity=100_000,
            unencumbered=40_000,
            vehicle="SGOV",
            vehicle_apy=5.18,
            sweep_apy=4.70,
            sgov_apy=5.18,
        )
        invoices = excess.Invoices(0, 0.0, None, None, {})
        tickets = excess.Tickets(0, 0, 0, 0, 0, 0, 0.0, 0)
        text = excess.render(snap, invoices, tickets)
        self.assertIn("Certainty is a settings page", text)
        self.assertIn("S1 is done. Do not build G0", text)
        self.assertIn("$0 / yr", text)  # vs SGOV
        self.assertIn("$192 / yr", text)  # 40000 * 0.48%

    def test_mid_fills_invalidate_s4(self):
        tickets = excess.summarize_tickets(
            [
                {
                    "status": "paper",
                    "fill_source": "mid",
                    "result_usd": "100",
                }
            ]
        )
        text = excess.render(None, excess.Invoices(0, 0.0, None, None, {}), tickets)
        self.assertIn("INVALID for S4", text)
        self.assertEqual(tickets.mid_fills, 1)


if __name__ == "__main__":
    unittest.main()
