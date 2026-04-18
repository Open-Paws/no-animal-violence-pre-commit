# AGENTS.md — no-animal-violence-pre-commit

## Summary

A single-file Python pre-commit hook that scans staged files for speciesist language idioms and exits non-zero when any are found, blocking the commit. It implements 65+ compiled regex patterns paired with movement-standard alternative phrases. The hook is part of the Open Paws speciesist-language detection ecosystem and is also consumed as a pip-installable library by downstream MCP infrastructure (`reviewdog-no-animal-violence`, `mcp-server-nav-language`, `lbr8-mcp-constraints`). No external dependencies; pure stdlib Python.

---

## Status

**Production** (v0.2.0 tagged, actively consumed by multiple downstream integrations).

Implications of status:
- The console output format (`filepath:line_num` + matched phrase + alternative) is a **stable interface contract** — downstream tools (`reviewdog-no-animal-violence`) parse it. Do not change the output format without coordinating across the ecosystem.
- The exit codes `0` (clean) and `1` (violation found) are stable contracts. Do not add new exit codes.
- Pattern additions are low-risk. Pattern removals or regex behavior changes are medium-risk (may cause regressions in downstream tools).

---

## Key files

| File | Role |
|------|------|
| `no_animal_violence_check.py` | Core implementation: `PATTERNS` list, `COMPILED` cache, `check_file()`, `main()` |
| `.pre-commit-hooks.yaml` | Hook definition consumed by the pre-commit framework |
| `setup.py` | Package metadata; registers `no-animal-violence-check` console script entry point |
| `__init__.py` | Re-exports `PATTERNS`, `COMPILED`, `check_file`, `main` for library consumers |
| `tests/test_no_animal_violence_check.py` | 8 unit tests covering detection, clean pass, multiple matches, case insensitivity, exit codes |
| `.pre-commit-config.yaml` | Self-applies the hook to this repo (uses `files: \.(py|ts|js|md|yaml|yml)$`) |

---

## Architecture

```
pre-commit framework
    └── passes staged filenames as argv[1:]
            └── main()
                    └── check_file(filepath) for each file
                            └── iterates lines
                                    └── COMPILED regex patterns (65+, case-insensitive)
                                            └── appends (filepath, line_num, matched, alternative)
                    └── prints findings to stdout
                    └── returns 1 if any findings, 0 if clean
```

Single responsibility boundaries:
- `check_file()` — file I/O and pattern matching only; no output, no exit logic
- `main()` — orchestration, output formatting, exit code

Pattern data structure: `list[tuple[str, str]]` → compiled to `list[tuple[re.Pattern, str]]` at module load. Adding a pattern is one line in `PATTERNS`.

---

## How to test

```bash
# Unit tests
python -m pytest tests/ -v

# Manual invocation against specific files
python no_animal_violence_check.py path/to/file.py

# Full pre-commit integration test (installs the hook from the working tree)
pre-commit try-repo . no-animal-violence --all-files

# Install locally and test the console script
pip install -e .
no-animal-violence-check path/to/file.py
```

Expected results:
- A file containing `"kill two birds with one stone"` should produce exit code `1` with a finding on the correct line.
- A file containing only `x = 1 + 1` should produce exit code `0` with no output.

---

## Integration points

### Upstream (source of patterns)
- [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) — canonical pattern dictionary. Patterns in `PATTERNS` are currently a manually-maintained copy. Known DRY violation; future sync automation is planned. Any pattern addition should be coordinated with this repo.

### Downstream consumers
- [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) — GitHub Actions wrapper; runs the same scanner in CI
- [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) — pip-installs this package and pipes output through reviewdog for PR inline comments; depends on stable output format
- `mcp-server-nav-language` — MCP server (Gary hub Phase 3) implementing the same pattern set for real-time agent enforcement; runs at agent generation time as a complement to this commit-time hook
- `lbr8-mcp-constraints` — bundles 12 offline NAV patterns from this suite as MCP middleware
- `mcp-server-aha-evaluation` — uses NAV rules as Stage 1 of a two-stage content evaluation pipeline
- Audit-to-dispatch (decision #37, 2026-04-11) — NAV violations found during ecosystem audits auto-dispatch as agent fix tasks

### Org integration goals (open)
- Add hook to `open-paws-platform` `.pre-commit-config.yaml` (one of four unblocked tasks from `ecosystem/integration-todos.md` §27a)
- Include hook installation in developer bootcamp setup instructions

---

## Safe vs. risky changes

### Safe
- Adding a new `(pattern, alternative)` entry to `PATTERNS` — one-line change, automatically compiled and tested
- Improving a regex to catch more variant spellings — low risk if existing matches are preserved
- Adding test cases to `tests/test_no_animal_violence_check.py`
- Updating README or AGENTS.md

### Medium risk — verify downstream before merging
- Changing the console output format (affects `reviewdog-no-animal-violence` parser)
- Removing or weakening a regex pattern (may create blind spots in downstream tools)
- Changing the exit code behavior
- Modifying `check_file()` return structure (affects any library consumer using `__init__.py` exports)

### High risk — coordinate across the ecosystem
- Renaming or removing the `no-animal-violence-check` console script entry point
- Changing `setup.py` package name or version scheme
- Modifying `__init__.py` public API (`PATTERNS`, `COMPILED`, `check_file`, `main`)
- Bumping the Python version requirement above 3.8

---

## Known issues and TODOs

1. **Pattern duplication** — `PATTERNS` in `no_animal_violence_check.py` is a copy of the canonical dictionary in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence). Drift between the two is a known risk. Planned resolution: generate `PATTERNS` from the canonical source at release time.
2. **No automated test runner in CI** — Tests exist in `tests/` but there is no GitHub Actions workflow running `pytest` automatically. Adding a CI workflow would catch regressions before release.
3. **Version pin** — Downstream consumers pin to `rev: v0.2.0`. When releasing a new version, update the version in `setup.py`, `__init__.py`, and the recommended `rev:` in README.md, then tag.
4. **No named maintainer** — As of 2026-04-02, the suite has no named owner. Changes should be coordinated via the Open Paws context repo.

---

## Compassionate language reminder

All pattern alternatives must use movement-standard language:
- "farmed animals" not "livestock"
- "farmed birds" not "poultry"
- "slaughterhouse" not "processing facility"
- "factory farm" not "farm" or "production facility"

Never introduce euphemisms in the suggested alternatives — the point is to model clearer language, not softer framing of exploitation.
