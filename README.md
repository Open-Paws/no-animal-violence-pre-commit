# No Animal Violence — pre-commit hook

> **Status: 🟢 Production** | Part of the [Open Paws](https://openpaws.ai) speciesist-language detection ecosystem

A [pre-commit](https://pre-commit.com) hook that detects language normalizing harm to animals in code and documentation, suggesting clearer professional alternatives. This is the **earliest enforcement point** in the development workflow — violations are caught locally before any code leaves the developer's machine.

---

## Ecosystem

This hook is one layer in a multi-tool detection suite:

| Tool | Enforcement point |
|------|-------------------|
| **no-animal-violence-pre-commit** ← you are here | Local git commit |
| [no-animal-violence-action](https://github.com/Open-Paws/no-animal-violence-action) | GitHub Actions CI |
| [reviewdog-no-animal-violence](https://github.com/Open-Paws/reviewdog-no-animal-violence) | PR inline annotations |
| [eslint-plugin-no-animal-violence](https://github.com/Open-Paws/eslint-plugin-no-animal-violence) | JS/TS editor + lint |
| [vale-no-animal-violence](https://github.com/Open-Paws/vale-no-animal-violence) | Prose / docs |
| [vscode-no-animal-violence](https://github.com/Open-Paws/vscode-no-animal-violence) | VS Code extension |

Canonical pattern dictionary: [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) (65+ patterns, source of truth for the entire ecosystem).

---

## Installation

### Minimal setup

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: v0.2.0
    hooks:
      - id: no-animal-violence
```

Then install and run:

```bash
pre-commit install
pre-commit run --all-files   # scan everything on first install
```

### Limit to specific file types (recommended)

```yaml
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: v0.2.0
    hooks:
      - id: no-animal-violence
        files: \.(py|ts|js|md|yaml|yml)$
```

### Run manually without installing

```bash
pip install pre-commit
pre-commit try-repo https://github.com/Open-Paws/no-animal-violence-pre-commit no-animal-violence --all-files
```

---

## Hooks

### `no-animal-violence`

| Property | Value |
|----------|-------|
| Language | Python (no external dependencies) |
| Entry point | `no-animal-violence-check` console script |
| File types | All text files (or filtered by `files:` pattern) |
| Stage | `pre-commit` |
| Exit code | `0` = clean, `1` = violations found |

The hook scans each staged file line-by-line against 65+ compiled regular expressions. On any match it prints the file path, line number, matched phrase, and the suggested alternative, then exits non-zero to block the commit.

---

## Example output

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

Fix the flagged phrases and re-stage to proceed with the commit.

---

## Phrase reference

The hook detects all of the following (case-insensitive):

| Phrase | Suggested alternative |
|--------|-----------------------|
| kill two birds with one stone | accomplish two things at once |
| beat a dead horse | belabor the point |
| more than one way to skin a cat | more than one way to solve this |
| let the cat out of the bag | reveal the secret |
| open a can of worms | create a complicated situation |
| wild goose chase | futile search |
| like shooting fish in a barrel | trivially easy |
| flog a dead horse | belabor the point |
| bigger fish to fry | more important matters to address |
| guinea pig | test subject |
| hold your horses | wait a moment |
| the elephant in the room | the obvious issue |
| straight from the horse's mouth | directly from the source |
| bring home the bacon | bring home the results |
| take the bull by the horns | face the challenge head-on |
| like lambs to the slaughter | without resistance |
| no room to swing a cat | very cramped |
| red herring | distraction |
| curiosity killed the cat | curiosity backfired |
| like a chicken with its head cut off | in a panic |
| your goose is cooked | you're in trouble |
| throwing someone to the wolves | abandon to criticism |
| hook, line, and sinker | completely |
| clip someone's wings | restrict someone's freedom |
| straw that broke the camel's back | the tipping point |
| bird in the hand worth two in the bush | a sure thing beats a possibility |
| eating crow | admit being wrong |
| fighting like cats and dogs | constantly argue |
| take the bait | fall for it |
| don't count your chickens | don't assume success prematurely |
| livestock | farmed animals |
| poultry | farmed birds |
| gestation crates | pregnancy cage |
| depopulation | mass killing |
| processing plant/facility | slaughterhouse |
| farrowing crates | birthing cage |
| battery cages | small wire cage |
| spent hens | discarded hen |
| humane slaughter / humane killing | slaughter |
| broilers | chicken raised for meat |
| don't be a chicken | don't hesitate |
| code/memory/resource pig | resource-intensive |
| cowboy coding/coder | undisciplined coding |
| code monkey | developer |
| badgering | pestering |
| ferreting out | uncover |
| cattle vs. pets | ephemeral vs. persistent |
| pet project | side project |
| canary in the coal mine | early warning signal |
| dogfooding | self-hosting |
| herding cats | coordinating independent contributors |
| fishing expedition | exploratory investigation |
| sacred cow | unquestioned belief |
| scapegoat | blame target |
| rat race | daily grind |
| dead cat bounce | temporary rebound |
| dog-eat-dog | ruthlessly competitive |
| whack-a-mole | recurring problem |
| cash cow | profit center |
| sacrificial lamb | expendable person |
| sitting duck | easy target |
| open season | free-for-all |
| put out to pasture | retire |
| dead duck | lost cause |
| kill the process | terminate the process |
| kill the server | stop the server |
| nuke it | delete completely |
| abort | cancel |
| cull | remove |
| master/slave | primary/replica |
| whitelist/blacklist | allowlist/denylist |
| grandfathered | legacy |

For the authoritative pattern list and rationale, see the [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) canonical dictionary.

---

## Configuration options

The hook accepts standard pre-commit filtering arguments in your config:

```yaml
- id: no-animal-violence
  files: \.(py|ts|js|md|yaml|yml)$   # limit to specific extensions
  exclude: ^tests/fixtures/           # exclude paths
  args: []                            # no additional CLI args supported
```

No environment variables or config files are required. All patterns are built in.

---

## Running directly (without pre-commit)

The scanner can be invoked as a standalone script:

```bash
# Install
pip install git+https://github.com/Open-Paws/no-animal-violence-pre-commit.git

# Run against files
no-animal-violence-check src/utils.py docs/README.md

# Or via Python directly
python no_animal_violence_check.py src/utils.py
```

Exit code `0` = no violations. Exit code `1` = one or more violations found.

---

## Relationship to the canonical pattern dictionary

The patterns in `no_animal_violence_check.py` are derived from the [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) canonical dictionary. Currently they are maintained as a copy in this repository (known DRY limitation — tracked for future resolution). Until automatic sync is implemented, any pattern changes must be applied consistently in both repos.

The same 65+ pattern set is also enforced at agent-generation time by `mcp-server-nav-language` in the Gary MCP hub, providing end-to-end coverage from developer commit through to AI agent output.

---

## Contributing

1. Fork the repository and create a feature branch.
2. Patterns live in the `PATTERNS` list in `no_animal_violence_check.py`. Each entry is a `(regex, alternative)` tuple.
3. Run the test suite before opening a pull request:
   ```bash
   python -m pytest tests/
   ```
4. Verify the hook works end-to-end:
   ```bash
   pre-commit try-repo . no-animal-violence --all-files
   ```
5. Check that new patterns align with the [no-animal-violence](https://github.com/Open-Paws/no-animal-violence) canonical dictionary — open a parallel PR there if adding new phrases.
6. Keep alternatives in movement-standard language: "farmed animals" not "livestock", "slaughterhouse" not "processing facility".

---

MIT License — [Open Paws](https://openpaws.ai)
