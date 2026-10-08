"""The geometry package.

This file runs when someone does `import geometry`. Re-exporting the main names here lets users
write `from geometry import Circle` instead of `from geometry.shapes import Circle`.
"""

from .shapes import Circle, Square
from .units import cm_to_m

__all__ = ["Circle", "Square", "cm_to_m"]
