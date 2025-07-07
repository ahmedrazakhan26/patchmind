# PatchMind

PatchMind is a modular Python-based framework that monitors a local Git repository for changes and suggests automated patches. It is designed for developers who want lightweight tooling to keep their codebase clean and up to date.

## Why PatchMind?

Keeping track of every small change in a project can be tedious. PatchMind exists to analyze repository updates, evaluate their significance, and propose patch suggestions automatically. This helps maintainers stay focused on what matters while benefiting from quick feedback about potential improvements.

## How It Works

1. **Monitor**: Watch a local Git repository for file additions, deletions, and modifications.
2. **Evaluate**: Determine the impact of these changes and identify areas that could use patches.
3. **Suggest**: Provide patch suggestions through a simple command-line interface.

```
[Repository] -> [PatchEngine] -> [Patch Suggestions]
```

## Running the CLI

PatchMind ships with a command-line interface. After installing the dependencies, run:

```bash
python -m cli.main --changes
```

This prints a summary of added, modified, and deleted files in the current repository. Without `--changes` the CLI currently performs no action.

## PatchEngine

`PatchEngine` powers the change detection in PatchMind. It scans a Git project and categorizes file additions, modifications, and deletions. The results are returned as a simple dataclass:

```python
from core.patch_engine import PatchEngine

engine = PatchEngine()
changes = engine.detect_changes()
print(changes.added)
```

## Contributing

Contributions are welcome! Fork the repository, create a feature branch, and open a pull request with your changes. Please ensure any new functionality includes appropriate tests.
