#!/usr/bin/python3
import importlib.machinery
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = importlib.machinery.SourceFileLoader(
    "ansible_temple", str(ROOT / "ansible-temple")
).load_module()


class CatalogTest(unittest.TestCase):
    def test_manifest_keeps_only_playbooks_that_exist(self):
        catalog = PROGRAM.load_catalog(ROOT / "tests" / "fixture")
        self.assertEqual([item["id"] for item in catalog], ["redis", "freqtrade"])
        freqtrade = catalog[1]
        self.assertEqual(freqtrade["playbook"], "playbooks/freqtrade/main.yml")
        self.assertEqual(PROGRAM.option_key(freqtrade["options"][0]), "freqtrade_port")

    def test_boolean_and_number_encoding(self):
        options = [
            {"key": "port", "type": "number"},
            {"key": "dry", "type": "boolean"},
        ]
        encoded = PROGRAM.encode(options, ["6379", "oui"])
        self.assertEqual(encoded, {"port": 6379, "dry": True})


if __name__ == "__main__":
    unittest.main()
