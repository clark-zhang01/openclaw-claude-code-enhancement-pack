from __future__ import annotations

import unittest

from src.compat import compatibility_summary


class CompatibilityTest(unittest.TestCase):
    def test_compatibility_summary_mentions_openclaw(self) -> None:
        summary = compatibility_summary("manifest.json")
        self.assertIn("OpenClaw", summary)


if __name__ == "__main__":
    unittest.main()
