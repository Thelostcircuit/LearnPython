"""Lesson 1 — solutions."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def describe(name: str, age: int) -> str:
    return f"{name} is {age} years old"


def three_decimals(x: float) -> str:
    return f"{x:.3f}"


def right_align(word: str) -> str:
    return f"|{word:>10}|"


def price_tag(item: str, price: float) -> str:
    return f"{item}: ${price:.2f}"


def big_number(n: int) -> str:
    return f"{n:,}"
