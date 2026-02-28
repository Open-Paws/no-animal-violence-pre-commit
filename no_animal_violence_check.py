# AUTO-GENERATED from project-compassionate-code. Do not edit directly.
"""Pre-commit hook for detecting language that normalizes violence toward animals."""

import re
import sys


PATTERNS = [
    (r"kill\s+two\s+birds\s+with\s+one\s+stone", "accomplish two things at once"),
    (r"beat(ing)?\s+a\s+dead\s+horse", "belabor the point"),
    (r"more\s+than\s+one\s+way\s+to\s+skin\s+a\s+cat", "more than one way to solve this"),
    (r"let\s+the\s+cat\s+out\s+of\s+the\s+bag", "reveal the secret"),
    (r"open(ing)?\s+a\s+can\s+of\s+worms", "create a complicated situation"),
    (r"wild\s+goose\s+chase", "futile search"),
    (r"like\s+shooting\s+fish\s+in\s+a\s+barrel", "trivially easy"),
    (r"flog(ging)?\s+a\s+dead\s+horse", "belabor the point"),
    (r"bigger\s+fish\s+to\s+fry", "more important matters to address"),
    (r"guinea\s+pig", "test subject"),
    (r"hold\s+your\s+horses", "wait a moment"),
    (r"the\s+elephant\s+in\s+the\s+room", "the obvious issue"),
    (r"straight\s+from\s+the\s+horse'?s\s+mouth", "directly from the source"),
    (r"bring(ing)?\s+home\s+the\s+bacon", "bring home the results"),
    (r"take?(ing|ook)?\s+the\s+bull\s+by\s+the\s+horns", "face the challenge head-on"),
    (r"like\s+lambs?\s+to\s+(the\s+)?slaughter", "without resistance"),
    (r"no\s+room\s+to\s+swing\s+a\s+cat", "very cramped"),
    (r"red\s+herring", "distraction"),
    (r"don'?t\s+be\s+a\s+chicken", "don't hesitate"),
    (r"(code|memory|resource)\s+pig", "resource-intensive"),
    (r"cowboy\s+cod(ing|er)", "undisciplined coding"),
    (r"code\s+monkeys?", "developer"),
    (r"cattle\s+(vs?\.?|versus)\s+pets?", "ephemeral vs. persistent"),
    (r"pet\s+project", "side project"),
    (r"canary\s+in\s+(a|the)\s+coal\s+mine", "early warning signal"),
    (r"dog\s?food(ing)?", "self-hosting"),
    (r"herding\s+cats", "coordinating independent contributors"),
    (r"fishing\s+expedition", "exploratory investigation"),
    (r"sacred\s+cows?", "unquestioned belief"),
    (r"scapegoat(ed|ing|s)?", "blame target"),
    (r"rat\s+race", "daily grind"),
    (r"dead[\s_-]?cat[\s_-]?bounce", "temporary rebound"),
    (r"dog[\s-]eat[\s-]dog", "ruthlessly competitive"),
    (r"whack[\s-]a[\s-]mole", "recurring problem"),
    (r"kill\s+(the\s+)?process", "terminate the process"),
    (r"kill\s+(the\s+)?server", "stop the server"),
    (r"nuke\s+(it|the|this|that|everything)", "delete completely"),
    (r"abort(ed|ing)?", "cancel"),
    (r"(master|slave)", "primary/replica"),
    (r"(white|black)list", "allowlist/denylist"),
    (r"grandfather(ed|ing)?", "legacy"),
]

COMPILED = [(re.compile(pattern, re.IGNORECASE), alt) for pattern, alt in PATTERNS]


def check_file(filepath):
    """Check a single file for animal violence language. Returns list of findings."""
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
        print("Animal violence language detected:\n")
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
