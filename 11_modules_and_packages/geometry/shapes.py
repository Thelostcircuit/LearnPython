"""Shapes. (Classes are covered in lesson 12 — here, just notice the relative import.)"""

import math

from .units import cm_to_m  # relative import: `units` is a sibling module in this package


class Circle:
    def __init__(self, radius_cm: float) -> None:
        self.radius_cm = radius_cm

    def area_m2(self) -> float:
        return math.pi * cm_to_m(self.radius_cm) ** 2


class Square:
    def __init__(self, side_cm: float) -> None:
        self.side_cm = side_cm

    def area_m2(self) -> float:
        return cm_to_m(self.side_cm) ** 2
