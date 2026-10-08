"""If `uv run python examples.py` prints a happy message, your setup works!"""

import sys
from pathlib import Path

print("🐍 Python is working!")
print()
print(f"Python version: {sys.version.split()[0]}")
print(f"Running from:   {sys.executable}")

# sys.prefix != sys.base_prefix means we're inside a virtual environment.
in_venv = sys.prefix != sys.base_prefix
print(f"In a virtual environment? {in_venv}")
if not in_venv:
    print("  → Run this with `uv run python examples.py` to use the course's .venv")

try:
    import pytest

    print(f"pytest {pytest.__version__} is available")
except ModuleNotFoundError:
    print("pytest is NOT available — run `uv sync` in the course folder")

print()
print(f"This file lives at: {Path(__file__).resolve()}")
print("Next: the ruff exercise in README.md, then on to 01_hello_python.")
