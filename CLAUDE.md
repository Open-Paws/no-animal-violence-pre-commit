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
