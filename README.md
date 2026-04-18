[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/Open-Paws/no-animal-violence-pre-commit/releases)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Last Commit](https://img.shields.io/github/last-commit/Open-Paws/no-animal-violence-pre-commit)](https://github.com/Open-Paws/no-animal-violence-pre-commit/commits/main)

# no-animal-violence-pre-commit

A [pre-commit](https://pre-commit.com) hook that scans staged files for language that normalizes harm to animals — idioms, industry euphemisms, and tech jargon — and suggests clearer alternatives. It runs locally before any code leaves the developer's machine, making it the earliest enforcement point in the development workflow. No external dependencies; patterns compile at import time.

> [!NOTE]
> This project is part of the [Open Paws](https://openpaws.ai) ecosystem — AI infrastructure for the animal liberation movement. [Explore the full platform →](https://github.com/Open-Paws)

## Usage

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: v0.2.0
    hooks:
      - id: no-animal-violence
        files: \.(py|ts|js|md|yaml|yml)$   # recommended: limit to text files
        exclude: ^tests/fixtures/           # optional: skip known-bad fixtures
```

## Quickstart

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```
2. Add the hook config above to `.pre-commit-config.yaml` in your repository root.
3. Install the hooks:
   ```bash
   pre-commit install
   ```
4. Run against all existing files (recommended on first install):
   ```bash
   pre-commit run no-animal-violence --all-files
   ```
5. From this point on, the hook runs automatically on every `git commit`.

**Run without installing** (one-shot scan):
```bash
pre-commit try-repo https://github.com/Open-Paws/no-animal-violence-pre-commit no-animal-violence --all-files
```

## Features

### What it checks

The hook scans each staged file line-by-line against 65+ compiled regular expressions (case-insensitive) covering three categories:

- **Animal idioms in code and prose** — `kill two birds with one stone`, `guinea pig`, `cattle vs. pets`, `herding cats`, `canary in the coal mine`, and 30+ others
- **Industry euphemisms for exploitation** — `livestock` → farmed animals, `processing plant` → slaughterhouse, `humane slaughter`, `spent hens`, `depopulation`, and others
- **Tech jargon with harmful roots** — `master/slave` → primary/replica, `whitelist/blacklist` → allowlist/denylist, `cowboy coding`, `code monkey`, `dogfooding`

On any match the hook prints the file path, line number, matched phrase, and suggested alternative, then exits non-zero to block the commit:

```
Animal violence language detected:

  src/utils.py:14
    Found:   "kill two birds with one stone"
    Suggest: "accomplish two things at once"

  docs/architecture.md:37
    Found:   "cattle vs. pets"
    Suggest: "ephemeral vs. persistent"

2 instance(s) found. Consider using the suggested alternatives.
```

Fix the flagged phrases, re-stage, and commit again.

### Configuration options

All filtering uses standard pre-commit arguments — no environment variables or config files are required:

| Option | Example | Effect |
|--------|---------|--------|
| `files` | `\.(py|ts|js|md)$` | Limit to specific extensions |
| `exclude` | `^tests/fixtures/` | Skip paths matching the pattern |
| `stages` | `[pre-commit, manual]` | Control when the hook runs |

All patterns are built in. There is no external config file to maintain.

### Running as a standalone script

The scanner can also be invoked directly, outside of pre-commit:

```bash
pip install git+https://github.com/Open-Paws/no-animal-violence-pre-commit.git

no-animal-violence-check src/utils.py docs/README.md
```

Exit code `0` = clean. Exit code `1` = one or more violations found.

## Documentation

- [Canonical pattern dictionary](https://github.com/Open-Paws/no-animal-violence) — authoritative source for all 65+ patterns and rationale
- [pre-commit documentation](https://pre-commit.com/docs) — general hook configuration reference
- [`.pre-commit-hooks.yaml`](.pre-commit-hooks.yaml) — hook manifest for this repo

### Ecosystem

This hook is one layer in a multi-tool detection suite. Each tool targets a different enforcement point:

| Tool | Enforcement point |
|------|-------------------|
| **no-animal-violence-pre-commit** ← you are here | Local git commit |
| [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) | GitHub Actions CI |
| [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) | PR inline annotations |
| [eslint-plugin-no-animal-violence](https://github.com/Open-Paws/eslint-plugin-no-animal-violence) | JS/TS editor + lint |
| [vale-no-animal-violence](https://github.com/Open-Paws/vale-no-animal-violence) | Prose / docs |
| [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) | VS Code extension |
| [danger-plugin-no-animal-violence](https://github.com/Open-Paws/danger-plugin-no-animal-violence) | Danger.js PR checks |

## Architecture

<details>
<summary>Implementation details</summary>

The hook is a single Python file (`no_animal_violence_check.py`) with no runtime dependencies beyond the standard library.

**Pattern structure:** Each entry in `PATTERNS` is a `(regex_string, alternative_string)` tuple. All patterns are compiled once at module load time into `COMPILED` using `re.IGNORECASE`.

**Execution flow:**
1. `pre-commit` calls the `no-animal-violence-check` console script with a list of staged filenames as arguments.
2. `main()` iterates over each filename and calls `check_file()`.
3. `check_file()` opens the file in UTF-8 mode (with error replacement for binary content), iterates line-by-line, and runs all compiled regexes via `finditer`.
4. Findings are collected as `(filepath, line_number, matched_text, alternative)` tuples.
5. If any findings exist, they are printed to stdout and the process exits with code `1`, blocking the commit.

**Pattern source:** Patterns are auto-generated from [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code) and derived from the [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) canonical dictionary. The pattern list in this repo is currently maintained as a copy (a known DRY limitation tracked for future resolution). Pattern changes must be applied consistently in both repos until automatic sync is implemented.

**Python requirement:** 3.8+. The hook is registered in `.pre-commit-hooks.yaml` with `language: python` and `types: [text]`.

</details>

## Contributing

Contributions are welcome — especially new patterns. The most useful additions are phrases that appear in real codebases and have clear, professionally neutral alternatives.

1. Fork the repository and create a feature branch.
2. Patterns live in the `PATTERNS` list in `no_animal_violence_check.py`. Each entry is a `(regex, alternative)` tuple.
3. Run the test suite:
   ```bash
   python -m pytest tests/
   ```
4. Verify the hook end-to-end:
   ```bash
   pre-commit try-repo . no-animal-violence --all-files
   ```
5. Open a parallel PR in [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) if adding a new phrase to the canonical dictionary.
6. Use movement-standard language in alternatives: "farmed animals" not "livestock", "slaughterhouse" not "processing facility".

---

<!-- TODO: add adoption/usage numbers once available from GitHub dependency graph or package download stats -->

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Open Paws.

## Acknowledgments

Pattern dictionary maintained by the Open Paws community. This hook is auto-generated from [project-compassionate-code](https://github.com/Open-Paws/project-compassionate-code), which submits animal-friendly PRs to open-source repositories at scale.

---

[Donate](https://openpaws.ai/donate) · [Discord](https://discord.gg/openpaws) · [openpaws.ai](https://openpaws.ai) · [Volunteer](https://openpaws.ai/volunteer)

---

<!-- Metadata
tech_stack: Python, pre-commit
project_status: production
difficulty: beginner
skill_tags: pre-commit, language-linting, speciesist-language, advocacy-tooling, python
related_repos: no-animal-violence, no-animal-violence-action, reviewdog-no-animal-violence, eslint-plugin-no-animal-violence, vale-no-animal-violence, vscode-no-animal-violence, danger-plugin-no-animal-violence, project-compassionate-code
-->
