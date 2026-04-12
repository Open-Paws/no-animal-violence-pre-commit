"""no-animal-violence-pre-commit: pre-commit hook for speciesist language."""

from no_animal_violence_check import COMPILED, PATTERNS, check_file, main

__version__ = "0.2.0"
__all__ = ["check_file", "main", "PATTERNS", "COMPILED"]
