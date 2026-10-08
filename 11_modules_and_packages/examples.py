"""Lesson 11 examples. Run with: uv run python examples.py

Also try:  uv run python helpers.py   (see the difference __name__ makes)
"""

import sys

print("importing helpers for the first time:")
import helpers  # noqa: E402 — imported here on purpose, to show the print happening

print("importing it again (nothing printed — modules are cached):")
import helpers as h  # noqa: E402

print(f"helpers is h? {helpers is h}")
print(f"helpers.slugify: {helpers.slugify('  Modules Are Files ')!r}")
print(f"helpers.GREETING: {h.GREETING!r}")
print(f"helpers.__name__ when imported: {helpers.__name__!r}")
print(f"this file's __name__: {__name__!r}")

# --- from ... import ... --------------------------------------------------------------
from helpers import slugify as make_slug  # noqa: E402

print(f"make_slug: {make_slug('Aliased Import')!r}")

# --- A package ------------------------------------------------------------------------
import geometry  # noqa: E402
from geometry import Circle, Square  # noqa: E402  (re-exported by geometry/__init__.py)
from geometry.units import CM_PER_M  # noqa: E402  (straight from the submodule)

print(f"\ngeometry package lives at: {geometry.__file__}")
print(f"geometry's public API (__all__): {geometry.__all__}")
print(f"Circle(50cm).area_m2() = {Circle(50).area_m2():.4f}")
print(f"Square(200cm).area_m2() = {Square(200).area_m2():.1f}")
print(f"CM_PER_M = {CM_PER_M}, geometry.cm_to_m(250) = {geometry.cm_to_m(250)}")

# --- Where Python looks ---------------------------------------------------------------
print("\nfirst entries of sys.path:")
for entry in sys.path[:3]:
    print(f"  {entry}")

# --- The standard library is just more modules ----------------------------------------
import math  # noqa: E402
import random  # noqa: E402

print(f"\nmath lives at: {math.__name__} (built in), random lives at: {random.__file__}")
