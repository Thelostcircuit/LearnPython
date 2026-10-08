"""Lesson 2 — solutions."""


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def average(a: int, b: int) -> float:
    return (a + b) / 2


def is_even(n: int) -> bool:
    return n % 2 == 0


def minutes_to_hours(minutes: int) -> str:
    hours, mins = divmod(minutes, 60)
    return f"{hours}h {mins}m"


def parse_and_double(s: str) -> int:
    return int(s) * 2


def swap(pair: tuple[int, str]) -> tuple[str, int]:
    first, second = pair
    return second, first


def describe_type(value: object) -> str:
    if value is None:
        return "None"
    if isinstance(value, bool):  # must come before int!
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    return "other"


def is_blank(s: str | None) -> bool:
    return not s
