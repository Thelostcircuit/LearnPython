"""Lesson 12 — solutions."""

import math
from dataclasses import dataclass, field


class Counter:
    def __init__(self, step: int = 1) -> None:
        self.count = 0
        self.step = step

    def tick(self) -> None:
        self.count += self.step

    def reset(self) -> None:
        self.count = 0

    def __repr__(self) -> str:
        return f"Counter(count={self.count}, step={self.step})"


class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side: float) -> "Rectangle":
        return cls(side, side)

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def is_square(self) -> bool:
        return self.width == self.height


@dataclass
class Book:
    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)

    def is_classic(self) -> bool:
        return 2026 - self.year > 50
