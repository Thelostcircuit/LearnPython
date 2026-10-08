"""Lesson 13 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""

from abc import ABC, abstractmethod
from typing import Protocol

# --------------------------------------------------------------------------------------
# 1. An employee hierarchy


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def annual_pay(self) -> float:
        """Just the salary."""
        raise NotImplementedError

    def describe(self) -> str:
        """e.g. "Ada earns 50000.00" — uses annual_pay(), so subclasses change it for free."""
        raise NotImplementedError


class Manager(Employee):
    """A Manager also has a `bonus`, and their annual pay is salary + bonus.

    Write __init__(self, name, salary, bonus) — call super().__init__ for name and salary —
    and override annual_pay(). Don't override describe()!
    """


# --------------------------------------------------------------------------------------
# 2. An abstract base class


class Notifier(ABC):
    def __init__(self) -> None:
        self.sent: list[str] = []

    @abstractmethod
    def format(self, message: str) -> str: ...

    def send(self, message: str) -> None:
        """Format the message and append it to self.sent."""
        raise NotImplementedError


class EmailNotifier(Notifier):
    """format() returns "EMAIL: <message>". Implement it."""


class SmsNotifier(Notifier):
    """format() returns the message cut to its first 10 characters. Implement it."""


# --------------------------------------------------------------------------------------
# 3. Protocols and duck typing


class Priced(Protocol):
    def price(self) -> float: ...


class Coffee:
    def __init__(self, size: str) -> None:
        self.size = size

    def price(self) -> float:
        """small: 2.0, medium: 2.5, large: 3.0"""
        raise NotImplementedError


class Cake:
    def __init__(self, slices: int) -> None:
        self.slices = slices

    def price(self) -> float:
        """3.5 per slice"""
        raise NotImplementedError


def order_total(items: list[Priced]) -> float:
    """Sum of item prices. Coffee and Cake don't share a parent class — only a method."""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_employee():
    e = Employee("Ada", 50000)
    assert e.annual_pay() == 50000
    assert e.describe() == "Ada earns 50000.00"


def test_manager():
    m = Manager("Grace", 80000, 10000)  # type: ignore[call-arg]
    assert isinstance(m, Employee)
    assert m.name == "Grace"
    assert m.bonus == 10000  # type: ignore[attr-defined]
    assert m.annual_pay() == 90000
    assert m.describe() == "Grace earns 90000.00"
    assert "describe" not in Manager.__dict__, "describe should be inherited, not overridden"


def test_notifier_is_abstract():
    with pytest.raises(TypeError):
        Notifier()  # type: ignore[abstract]


def test_notifiers():
    email, sms = EmailNotifier(), SmsNotifier()
    for n in (email, sms):
        n.send("Your package has arrived")
    assert email.sent == ["EMAIL: Your package has arrived"]
    assert sms.sent == ["Your packa"]


def test_order_total():
    assert order_total([Coffee("large"), Cake(2), Coffee("small")]) == 12.0
    assert order_total([]) == 0
