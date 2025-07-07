"""Tests for PatchEngine."""

import unittest

from core.patch_engine import PatchEngine


class TestPatchEngine(unittest.TestCase):
    """Ensure PatchEngine initializes correctly."""

    def test_initialization(self) -> None:
        engine = PatchEngine()
        self.assertIsInstance(engine, PatchEngine)


if __name__ == "__main__":
    unittest.main()
