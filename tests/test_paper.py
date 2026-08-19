#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from paper.journal import append_decision, open_max_loss, settled_paper
from paper.picker import pick
from paper.size import max_loss_one, size_contracts
from paper.tape import PaperRootError, load_fixture, require_spy
from paper.verdict import rule_verdict


ROOT = Path(__file__).resolve().parents[1]
TAKE = ROOT / "fixtures" / "spy_take.json"
PASS_IV = ROOT / "fixtures" / "spy_pass_iv.json"


class RebuildTests(unittest.TestCase):
    def test_tape_rejects_universe(self):
        with self.assertRaises(PaperRootError):
            require_spy("AAPL")

    def test_take_on_high_iv_rank(self):
        snap = load_fixture(TAKE)
        d = pick(snap, equity=100_000)
        self.assertTrue(d.take)
        self.assertEqual(d.fill_source, "worst")
        self.assertEqual(d.dte, 37)
        self.assertGreater(d.credit_usd, 0)
        self.assertLessEqual(d.max_loss_usd, 1000)  # 1% of 100k
        self.assertGreaterEqual(d.contracts, 1)
        self.assertEqual(d.short_put, 565.0)
        self.assertEqual(d.long_put, 560.0)

    def test_pass_on_low_iv_rank(self):
        snap = load_fixture(PASS_IV)
        d = pick(snap, equity=100_000)
        self.assertFalse(d.take)
        self.assertIn("IV rank", d.reason)

    def test_pass_when_one_lot_blows_the_cap(self):
        snap = load_fixture(TAKE)
        d = pick(snap, equity=200)  # 1% = $2
        self.assertFalse(d.take)
        self.assertIn("1%", d.reason)

    def test_pass_when_book_cap_exhausted(self):
        snap = load_fixture(TAKE)
        d = pick(snap, equity=100_000, open_max_loss=3000)
        self.assertFalse(d.take)
        self.assertIn("3%", d.reason)

    def test_write_refuses_mid(self):
        snap = load_fixture(TAKE)
        d = pick(snap, equity=100_000)
        bad = d.__class__(**{**d.__dict__, "fill_source": "mid"})
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                append_decision(bad, as_of=snap.as_of, journal=Path(tmp))

    def test_journal_round_trip_and_kill_rule(self):
        snap = load_fixture(TAKE)
        take = pick(snap, equity=100_000)
        passed = pick(load_fixture(PASS_IV), equity=100_000)
        with tempfile.TemporaryDirectory() as tmp:
            j = Path(tmp)
            append_decision(take, as_of=snap.as_of, journal=j)
            append_decision(passed, as_of=snap.as_of, journal=j)
            self.assertGreater(open_max_loss(j), 0)
            n, pnl = settled_paper(j)
            self.assertEqual(n, 0)
            # settle 20 losers
            import csv
            from paper.journal import TICKET_FIELDS

            p = j / "tickets.csv"
            # rewrite with 20 settled losers
            with p.open("w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=TICKET_FIELDS)
                w.writeheader()
                for i in range(20):
                    w.writerow(
                        {
                            "date": "2026-01-01",
                            "status": "paper",
                            "underlier": "SPY",
                            "structure": "iron_condor",
                            "dte": "37",
                            "iv_rank": "62",
                            "iv_rank_source": "fixture",
                            "max_loss_usd": "400",
                            "credit_usd": "120",
                            "fill_source": "worst",
                            "thesis": "test",
                            "result_usd": "-50",
                            "notes": "",
                        }
                    )
            text = rule_verdict(j)
            self.assertIn("KILL THE RULE", text)

    def test_cli_dry_run(self):
        from io import StringIO
        from unittest.mock import patch
        from paper.cli import main

        buf = StringIO()
        with patch("sys.stdout", buf):
            rc = main(["--fixture", str(TAKE), "--equity", "100000"])
        self.assertEqual(rc, 0)
        self.assertIn("fill_source=worst", buf.getvalue())

    def test_mark_leaves_open_on_same_tape(self):
        from paper.mark import mark_open

        snap = load_fixture(TAKE)
        take = pick(snap, equity=100_000)
        with tempfile.TemporaryDirectory() as tmp:
            j = Path(tmp)
            append_decision(take, as_of=snap.as_of, journal=j)
            reports = mark_open(snap, j)
            self.assertEqual(len(reports), 1)
            self.assertEqual(reports[0].action, "open")
            n, _ = settled_paper(j)
            self.assertEqual(n, 0)

    def test_mark_closes_at_21_dte(self):
        from paper.mark import mark_open

        snap = load_fixture(TAKE)
        take = pick(snap, equity=100_000)
        later = load_fixture(ROOT / "fixtures" / "spy_dte21.json")
        with tempfile.TemporaryDirectory() as tmp:
            j = Path(tmp)
            append_decision(take, as_of=snap.as_of, journal=j)
            reports = mark_open(later, j)
            self.assertEqual(reports[0].action, "closed")
            self.assertIn("DTE", reports[0].reason)
            n, _ = settled_paper(j)
            self.assertEqual(n, 1)

    def test_mark_closes_when_short_tested(self):
        from paper.mark import mark_open

        snap = load_fixture(TAKE)
        take = pick(snap, equity=100_000)
        tested = load_fixture(ROOT / "fixtures" / "spy_tested.json")
        with tempfile.TemporaryDirectory() as tmp:
            j = Path(tmp)
            append_decision(take, as_of=snap.as_of, journal=j)
            reports = mark_open(tested, j)
            self.assertEqual(reports[0].action, "closed")
            self.assertIn("tested", reports[0].reason)

    def test_cli_mark_with_no_opens(self):
        from io import StringIO
        from unittest.mock import patch
        from paper.cli import main

        buf = StringIO()
        with tempfile.TemporaryDirectory() as tmp:
            from paper.journal import TICKET_FIELDS
            import csv

            p = Path(tmp) / "tickets.csv"
            with p.open("w", newline="") as f:
                csv.DictWriter(f, fieldnames=TICKET_FIELDS).writeheader()
            with patch("sys.stdout", buf):
                rc = main(["--mark", "--fixture", str(TAKE), "--journal", tmp])
        self.assertEqual(rc, 0)
        self.assertIn("no open paper tickets", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
