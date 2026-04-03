from __future__ import annotations

import json
from pathlib import Path
import unittest


class ManifestTest(unittest.TestCase):
    def test_manifest_exists_and_has_core_fields(self) -> None:
        manifest = Path("manifest.json")
        self.assertTrue(manifest.exists())
        data = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual(data["id"], "openclaw-claude-code")
        self.assertEqual(data["name"], "OpenClaw Claude Code Enhancement Pack")
        self.assertIn("prompt-engineering", data["capabilities"])


if __name__ == "__main__":
    unittest.main()
