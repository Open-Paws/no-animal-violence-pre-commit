# No Animal Violence — pre-commit hook

A [pre-commit](https://pre-commit.com) hook that detects language normalizing violence toward animals in code and documentation, suggesting clearer, more professional alternatives.

## Installation

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/Open-Paws/no-animal-violence-pre-commit
    rev: v0.2.0
    hooks:
      - id: no-animal-violence
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
| "more than one way to skin a cat" | "more than one way to solve this" |
| "let the cat out of the bag" | "reveal the secret" |
| "open a can of worms" | "create a complicated situation" |
| "wild goose chase" | "futile search" |
| "like shooting fish in a barrel" | "trivially easy" |
| "flog a dead horse" | "belabor the point" |
| "bigger fish to fry" | "more important matters to address" |
| "guinea pig" | "test subject" |
| "hold your horses" | "wait a moment" |
| "the elephant in the room" | "the obvious issue" |
| "straight from the horse's mouth" | "directly from the source" |
| "bring home the bacon" | "bring home the results" |
| "take the bull by the horns" | "face the challenge head-on" |
| "like lambs to the slaughter" | "without resistance" |
| "no room to swing a cat" | "very cramped" |
| "red herring" | "distraction" |
| "don't be a chicken" | "don't hesitate" |
| "code/memory/resource pig" | "resource-intensive" |
| "cowboy coding/coder" | "undisciplined coding" |
| "code monkey" | "developer" |
| "cattle vs. pets" | "ephemeral vs. persistent" |
| "pet project" | "side project" |
| "canary in the coal mine" | "early warning signal" |
| "dogfooding" | "self-hosting" |
| "herding cats" | "coordinating independent contributors" |
| "fishing expedition" | "exploratory investigation" |
| "sacred cow" | "unquestioned belief" |
| "scapegoat" | "blame target" |
| "rat race" | "daily grind" |
| "dead cat bounce" | "temporary rebound" |
| "dog-eat-dog" | "ruthlessly competitive" |
| "whack-a-mole" | "recurring problem" |
| "kill the process" | "terminate the process" |
| "kill the server" | "stop the server" |
| "nuke it" | "delete completely" |
| "abort" | "cancel" |
| "master/slave" | "primary/replica" |
| "whitelist/blacklist" | "allowlist/denylist" |
| "grandfathered" | "legacy" |

## License

MIT — [Open Paws](https://openpaws.ai)
