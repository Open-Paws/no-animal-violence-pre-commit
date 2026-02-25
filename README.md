# Speciesist Language Scanner — pre-commit hook

A [pre-commit](https://pre-commit.com) hook that detects speciesist language in code and documentation, suggesting clearer, more professional alternatives.

## Installation

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Open-Paws/speciesist-language-pre-commit
    rev: v0.1.0
    hooks:
      - id: speciesist-language
```

Then run:

```bash
pre-commit install
```

## What It Detects

Phrases that normalize violence toward animals, with clearer professional alternatives:

| Phrase | Suggested Alternative |
|--------|----------------------|
| "kill two birds with one stone" | "accomplish two things at once" |
| "beat a dead horse" | "belabor the point" |
| "bring home the bacon" | "bring home the results" |
| "guinea pig" | "test subject" |
| "more than one way to skin a cat" | "more than one way to solve this" |
| "let the cat out of the bag" | "reveal the secret" |
| "open a can of worms" | "create a complicated situation" |
| "wild goose chase" | "pointless pursuit" |
| "sacred cow" | "unquestioned belief" |
| "cattle vs. pets" | "ephemeral vs. persistent" |
| "canary deployment" | "progressive rollout" |
| "monkey patch" | "runtime patch" |
| "like shooting fish in a barrel" | "extremely easy" |

## License

MIT — [Open Paws](https://openpaws.ai)
