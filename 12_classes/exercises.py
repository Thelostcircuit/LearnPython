"""Lesson 12 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""

# ruff: noqa: F401 — some imports are only used once you've written your code

from dataclasses import dataclass


class Counter:
    """Counts up by `step` each time tick() is called."""

    def __init__(self, step: int = 1) -> None:
        """Start at count 0."""
        raise NotImplementedError

    def tick(self) -> None:
        raise NotImplementedError

    def reset(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        """Counter(count=3, step=1)"""
        raise NotImplementedError


class BankAccount:
    def __init__(self, owner: str) -> None:
        """Store owner, and a balance of 0 in `self._balance`."""
        raise NotImplementedError

    @property
    def balance(self) -> int:
        """Read-only view of the balance."""
        raise NotImplementedError

    def deposit(self, amount: int) -> None:
        """Add amount. Raise ValueError if amount <= 0."""
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        """Subtract amount. Raise ValueError if amount <= 0 OR greater than the balance."""
        raise NotImplementedError


class Vector:
    """A 2D vector that supports +, *, ==, abs() and a nice repr."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Vector(1, 2)"""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __add__(self, other: "Vector") -> "Vector":
        raise NotImplementedError

    def __mul__(self, scalar: float) -> "Vector":
        """Vector(1, 2) * 3 == Vector(3, 6)"""
        raise NotImplementedError

    def __abs__(self) -> float:
        """Length: sqrt(x² + y²).  abs(Vector(3, 4)) == 5"""
        raise NotImplementedError


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @classmethod
    def square(cls, side: float) -> "Rectangle":
        """Alternative constructor: a Rectangle with equal sides."""
        raise NotImplementedError

    @property
    def area(self) -> float:
        raise NotImplementedError

    @property
    def is_square(self) -> bool:
        raise NotImplementedError


# Turn this into a dataclass: add the @dataclass decorator and the fields
# `title: str`, `author: str`, `year: int`, and `tags: list[str]` defaulting to an empty list
# (use field(default_factory=list) — you'll need to import `field` too).
# Then implement the `is_classic` method.
class Book:
    def is_classic(self) -> bool:
        """True if the book is more than 50 years old in 2026."""
        raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_counter():
    c = Counter(step=5)
    c.tick()
    c.tick()
    assert c.count == 10
    assert repr(c) == "Counter(count=10, step=5)"
    c.reset()
    assert c.count == 0
    assert Counter().step == 1


def test_bank_account():
    acct = BankAccount("ada")
    assert acct.owner == "ada"
    acct.deposit(100)
    acct.withdraw(30)
    assert acct.balance == 70
    with pytest.raises(ValueError):
        acct.withdraw(1000)
    with pytest.raises(ValueError):
        acct.deposit(-5)
    with pytest.raises(AttributeError):
        acct.balance = 5  # type: ignore[misc]  # read-only property


def test_vector():
    v = Vector(1, 2)
    assert repr(v) == "Vector(1, 2)"
    assert v + Vector(3, 4) == Vector(4, 6)
    assert v * 3 == Vector(3, 6)
    assert abs(Vector(3, 4)) == 5
    assert v != Vector(2, 1)


def test_rectangle():
    r = Rectangle(2, 3)
    assert r.area == 6
    assert not r.is_square
    s = Rectangle.square(4)
    assert isinstance(s, Rectangle)
    assert s.area == 16
    assert s.is_square


def test_book_dataclass():
    b = Book("Dune", "Frank Herbert", 1965)  # type: ignore[call-arg]
    assert b == Book("Dune", "Frank Herbert", 1965)  # type: ignore[call-arg]
    assert b.tags == []
    assert "Book(title='Dune'" in repr(b)
    assert b.is_classic()
    assert not Book("New", "Someone", 2020).is_classic()  # type: ignore[call-arg]
    other = Book("A", "B", 2000)  # type: ignore[call-arg]
    other.tags.append("x")
    assert b.tags == []  # each book gets its own list
