"""Tests for no_animal_violence_check pre-commit hook."""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from no_animal_violence_check import check_file, main


class TestCheckFile(unittest.TestCase):
    def _write_temp(self, content: str) -> str:
        fd, path = tempfile.mkstemp(suffix=".py")
        with os.fdopen(fd, "w") as f:
            f.write(content)
        return path

    def test_detects_known_idiom(self):
        path = self._write_temp("# kill two birds with one stone\n")
        try:
            findings = check_file(path)
            self.assertEqual(len(findings), 1)
            filepath, line_num, matched, alternative, reason = findings[0]
            self.assertEqual(line_num, 1)
            self.assertIn("accomplish two things at once", alternative)
        finally:
            os.unlink(path)

    def test_clean_file_returns_no_findings(self):
        path = self._write_temp("x = 1 + 1\n")
        try:
            self.assertEqual(check_file(path), [])
        finally:
            os.unlink(path)

    def test_multiple_matches_on_same_line(self):
        path = self._write_temp("livestock and poultry\n")
        try:
            findings = check_file(path)
            self.assertEqual(len(findings), 2)
        finally:
            os.unlink(path)

    def test_unreadable_file_returns_empty(self):
        findings = check_file("/nonexistent/path/file.py")
        self.assertEqual(findings, [])

    def test_case_insensitive_match(self):
        path = self._write_temp("Guinea Pig experiment\n")
        try:
            findings = check_file(path)
            self.assertTrue(len(findings) >= 1)
        finally:
            os.unlink(path)

    def test_main_no_args_returns_zero(self):
        sys.argv = ["no-animal-violence-check"]
        self.assertEqual(main(), 0)

    def test_main_with_clean_file_returns_zero(self):
        path = self._write_temp("result = 42\n")
        try:
            sys.argv = ["no-animal-violence-check", path]
            self.assertEqual(main(), 0)
        finally:
            os.unlink(path)

    def test_main_with_flagged_file_returns_one(self):
        path = self._write_temp("# beat a dead horse\n")
        try:
            sys.argv = ["no-animal-violence-check", path]
            self.assertEqual(main(), 1)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
