"""Lesson 13 — solutions."""

from abc import ABC, abstractmethod
from typing import Protocol


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def annual_pay(self) -> float:
        return self.salary

    def describe(self) -> str:
        return f"{self.name} earns {self.annual_pay():.2f}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_pay(self) -> float:
        return super().annual_pay() + self.bonus


class Notifier(ABC):
    def __init__(self) -> None:
        self.sent: list[str] = []

    @abstractmethod
    def format(self, message: str) -> str: ...

    def send(self, message: str) -> None:
        self.sent.append(self.format(message))


class EmailNotifier(Notifier):
    def format(self, message: str) -> str:
        return f"EMAIL: {message}"


class SmsNotifier(Notifier):
    def format(self, message: str) -> str:
        return message[:10]


class Priced(Protocol):
    def price(self) -> float: ...


class Coffee:
    PRICES = {"small": 2.0, "medium": 2.5, "large": 3.0}

    def __init__(self, size: str) -> None:
        self.size = size

    def price(self) -> float:
        return self.PRICES[self.size]


class Cake:
    def __init__(self, slices: int) -> None:
        self.slices = slices

    def price(self) -> float:
        return 3.5 * self.slices


def order_total(items: list[Priced]) -> float:
    return sum(item.price() for item in items)
