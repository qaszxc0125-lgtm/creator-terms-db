#!/usr/bin/env python3
"""Unit tests for official-source monitor error classification."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_sources", ROOT / "scripts" / "check_sources.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class ClassifyStatusTests(unittest.TestCase):
    def test_broken_url_statuses(self):
        self.assertEqual(MODULE.classify_status(404), "likely_broken_url")
        self.assertEqual(MODULE.classify_status(410), "likely_broken_url")

    def test_access_restrictions_are_not_broken_urls(self):
        for status in (401, 403, 407, 429):
            with self.subTest(status=status):
                self.assertEqual(MODULE.classify_status(status), "blocked_or_rate_limited")

    def test_server_errors_are_retryable(self):
        for status in (500, 502, 503, 599):
            with self.subTest(status=status):
                self.assertEqual(MODULE.classify_status(status), "server_error_retry")

    def test_other_http_errors_are_reviewed(self):
        self.assertEqual(MODULE.classify_status(400), "http_error_review")

    def test_success(self):
        self.assertEqual(MODULE.classify_status(200), "ok")

if __name__ == "__main__":
    unittest.main()
