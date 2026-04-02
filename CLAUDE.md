# No Animal Violence — pre-commit Hook

A [pre-commit](https://pre-commit.com) hook that detects speciesist language in code and documentation, suggesting clearer professional alternatives. Part of the [No Animal Violence](https://github.com/Open-Paws) speciesist language detection suite for Open Paws.

## Quick Start

```bash
# Install the hook in any repo
pip install pre-commit

# Add to .pre-commit-config.yaml:
# repos:
#   - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
#     rev: v0.2.0
#     hooks:
#       - id: no-animal-violence

pre-commit install
pre-commit run --all-files   # test against all files
```

## Architecture

Single-file Python script with no external dependencies (just `re` and `sys`). The pre-commit framework installs it via `setup.py` and invokes the `no-animal-violence-check` console script entry point.

**Flow:** pre-commit passes staged filenames as args -> `main()` iterates files -> `check_file()` runs 65+ compiled regex patterns per line -> prints findings with alternatives -> exits non-zero if any matches found.

## Key Files

| File | Description |
|------|-------------|
| `no_animal_violence_check.py` | Core scanner — 65+ regex patterns, `check_file()` and `main()` entry point |
| `.pre-commit-hooks.yaml` | Hook definition (id, entry point, language, file types, stage) |
| `setup.py` | Package setup — registers `no-animal-violence-check` console script |
| `README.md` | Usage docs with full phrase-to-alternative mapping table |
| `LICENSE` | MIT license |

## Development Commands

```bash
# Run directly against specific files (no pre-commit needed)
python no_animal_violence_check.py file1.py file2.md

# Install locally for development
pip install -e .
no-animal-violence-check file1.py

# Test via pre-commit
pre-commit try-repo . no-animal-violence --all-files
```

## Organizational Context

**Strategic role (Lever 1 + Lever 3):** Local git enforcement — catches speciesist language before code leaves the developer's machine. The earliest possible intervention in the development workflow. Single-file Python script, no external dependencies.

**Current org priorities relevant to this repo:**
- Should be added to `open-paws-platform`'s `.pre-commit-config.yaml`. This is one of four unblocked commits from `ecosystem/integration-todos.md` §27a.
- Bootcamp integration: include hook installation in bootcamp setup instructions. Every developer completing bootcamp should have this running locally.
- Suite maintenance has **no named owner** as of 2026-04-02. The 65+ regex patterns need to stay in sync with the `no-animal-violence` canonical dictionary.
- v0.2.0 tag is the current pinned version. Consumers use `rev: v0.2.0` in `.pre-commit-config.yaml`.

**Decisions affecting this repo:**
- 2026-03-25: Every org developer should have this hook installed as standard tooling.
- 2026-04-01: Patterns in `no_animal_violence_check.py` should eventually sync from the `no-animal-violence` canonical source rather than being maintained independently. Currently duplicated — known DRY violation and drift risk.

## Related Repos

- [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) — Canonical rule dictionary (patterns currently duplicated in this script)
- [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) — GitHub Action (CI-level enforcement, complements this hook)
- [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) — reviewdog runner for PR-level inline comments

## Development Standards

### 10-Point Review Checklist (ranked by AI violation frequency)

1. **DRY** — 65+ patterns in `no_animal_violence_check.py` are duplicated from `no-animal-violence`. Any pattern change must be consistent. Primary DRY violation to fix long-term.
2. **Deep modules** — `check_file()` scans one file; `main()` orchestrates iteration. Keep them separate.
3. **Single responsibility** — Pattern matching, output formatting, and exit code logic are distinct responsibilities.
4. **Error handling** — File read errors caught per-file, not crashing the whole run. Binary files and encoding errors must be handled gracefully.
5. **Information hiding** — Compiled regex patterns are an implementation detail. Consumers see only console output format and exit code.
6. **Ubiquitous language** — "farmed animal" not "livestock," "factory farm" not "farm." Never introduce synonyms in pattern messages.
7. **Design for change** — Adding a pattern requires only one entry in the patterns list. No structural changes.
8. **Legacy velocity** — Before modifying regex patterns, run against test files to confirm no regressions.
9. **Over-patterning** — Single-file script with no external dependencies is the right architecture.
10. **Test quality** — Test with files containing known phrases (should flag) and clean code (should pass) before any release.

### Quality Gates

- **Direct test**: `python no_animal_violence_check.py test-file.py` — verify output.
- **pre-commit test**: `pre-commit try-repo . no-animal-violence --all-files`
- **Desloppify**: `desloppify scan --path .` — minimum score ≥85.
- **Two-failure rule**: After two failed fixes on the same problem, stop and restart.

### Seven Concerns — Repo-Specific Notes

1. **Testing** — Manual testing via direct invocation and `pre-commit try-repo`. No automated test suite.
2. **Security** — Reads local files. No network access, no execution of scanned content.
3. **Privacy** — Runs locally. No data leaves the machine.
4. **Cost optimization** — Zero dependencies, zero compute cost.
5. **Advocacy domain** — Pattern messages must use movement-standard language in suggestions.
6. **Accessibility** — Console output must be readable in standard terminals without color support.
7. **Emotional safety** — Messages explain the alternative without requiring engagement with graphic content.

### Structured Coding Reference

For tool-specific AI coding instructions (Claude Code rules, Cursor MDC, Copilot, Windsurf, etc.), copy the corresponding directory from `structured-coding-with-ai` into this project root.
