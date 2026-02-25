"""Pre-commit hook for detecting speciesist language."""

import re
import sys


PATTERNS = [
    (r"kill two birds with one stone", "accomplish two things at once"),
    (r"beat(?:ing)? a dead horse", "belabor the point"),
    (r"bring(?:ing)? home the bacon", "bring home the results"),
    (r"guinea pig", "test subject"),
    (r"more than one way to skin a cat", "more than one way to solve this"),
    (r"let(?:ting)? the cat out of the bag", "reveal the secret"),
    (r"open(?:ing|ed)? a can of worms", "create a complicated situation"),
    (r"wild goose chase", "pointless pursuit"),
    (r"sacred cows?", "unquestioned belief"),
    (r"cattle vs\.? pets", "ephemeral vs. persistent"),
    (r"canary deployment|canary release", "progressive rollout"),
    (r"monkey[- ]?patch", "runtime patch"),
    (r"like shooting fish in a barrel", "extremely easy"),
]

COMPILED = [(re.compile(pattern, re.IGNORECASE), alt) for pattern, alt in PATTERNS]


def check_file(filepath):
    """Check a single file for speciesist language. Returns list of findings."""
    findings = []
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            for line_num, line in enumerate(f, start=1):
                for regex, alternative in COMPILED:
                    for match in regex.finditer(line):
                        findings.append(
                            (filepath, line_num, match.group(), alternative)
                        )
    except (OSError, IOError):
        # Skip files that can't be read
        pass
    return findings


def main():
    """Entry point. Accepts filenames as arguments (provided by pre-commit)."""
    filenames = sys.argv[1:]
    if not filenames:
        return 0

    all_findings = []
    for filename in filenames:
        all_findings.extend(check_file(filename))

    if all_findings:
        print("Speciesist language detected:\n")
        for filepath, line_num, matched, alternative in all_findings:
            print(f"  {filepath}:{line_num}")
            print(f"    Found:   \"{matched}\"")
            print(f"    Suggest: \"{alternative}\"\n")
        print(
            f"{len(all_findings)} instance(s) found. "
            "Consider using the suggested alternatives."
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
