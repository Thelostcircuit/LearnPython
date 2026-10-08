"""Lesson 16 examples. Run with: uv run python examples.py

This lesson's real examples are TESTS, in test_examples.py. This script runs them for you
with pytest's verbose output, so you can see each one by name. Then read test_examples.py.
"""

import subprocess
import sys

print("Running: pytest test_examples.py -v\n")
result = subprocess.run([sys.executable, "-m", "pytest", "test_examples.py", "-v"], check=False)

print("\nNow open test_examples.py and read how each of those tests works.")
print("Try: uv run pytest test_examples.py -k parametrize -v")
sys.exit(result.returncode)
