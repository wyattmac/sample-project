#!/usr/bin/env python3
"""Tape boundary: picker must not know Theta exists."""

import inspect
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import paper.journal
import paper.picker
import paper.verdict
from paper.tape import PaperRootError, load_fixture, require_spy


class TapeBoundaryTests(unittest.TestCase):
    def test_vendor_locked(self):
        from paper.policy import MARKET_DATA_VENDOR, SYMBOL

        self.assertEqual(MARKET_DATA_VENDOR, "theta")
        self.assertEqual(SYMBOL, "SPY")
        with self.assertRaises(PaperRootError):
            require_spy("XSP")
        with self.assertRaises(PaperRootError):
            require_spy("AAPL")

    def test_core_modules_do_not_import_thetadata(self):
        for mod in (paper.picker, paper.journal, paper.verdict):
            src = inspect.getsource(mod)
            self.assertNotIn("thetadata", src)
            self.assertNotIn("ib_insync", src)
            self.assertNotIn("ibapi", src)

    def test_fixture_loads_without_api(self):
        snap = load_fixture()
        self.assertEqual(snap.symbol, "SPY")
        self.assertTrue(snap.source.startswith("fixture:"))
        self.assertGreater(len(snap.quotes), 10)


if __name__ == "__main__":
    unittest.main()
