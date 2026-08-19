#!/usr/bin/env python3
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import ticket_cash  # noqa: E402


class TicketCashTests(unittest.TestCase):
    def test_five_wide_typical(self):
        s = ticket_cash.size(100_000, 5, 1.20)
        self.assertEqual(s["max_loss_1lot"], 380)
        self.assertEqual(s["contracts"], 2)  # 1% of 100k = 1000; 1000/380 = 2
        self.assertEqual(s["cash_this_ticket"], 760)
        self.assertIn("2 lot(s)", ticket_cash.render(s))

    def test_over_cap_is_skip(self):
        s = ticket_cash.size(50_000, 10, 1.00)
        self.assertEqual(s["max_loss_1lot"], 900)
        self.assertEqual(s["contracts"], 0)
        self.assertIn("Skip", ticket_cash.render(s))

    def test_rejects_credit_wider_than_wings(self):
        with self.assertRaises(ValueError):
            ticket_cash.max_loss_one(5, 5)


if __name__ == "__main__":
    unittest.main()
