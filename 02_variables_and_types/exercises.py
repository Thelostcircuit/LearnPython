"""Lesson 2 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def celsius_to_fahrenheit(c: float) -> float:
    """F = C * 9/5 + 32"""
    raise NotImplementedError


def average(a: int, b: int) -> float:
    """The average of two numbers.  average(1, 2) == 1.5"""
    raise NotImplementedError


def is_even(n: int) -> bool:
    """True if n is even. Hint: %"""
    raise NotImplementedError


def minutes_to_hours(minutes: int) -> str:
    """Convert minutes to "Hh Mm":  135 -> "2h 15m",  45 -> "0h 45m".  Hint: // and %, or divmod."""
    raise NotImplementedError


def parse_and_double(s: str) -> int:
    """Convert the string to an int and double it:  "21" -> 42"""
    raise NotImplementedError


def swap(pair: tuple[int, str]) -> tuple[str, int]:
    """Swap the two values:  (1, "a") -> ("a", 1)"""
    raise NotImplementedError


def describe_type(value: object) -> str:
    """Return "int", "float", "str", "bool", or "None" for the given value, else "other".

    Careful: isinstance(True, int) is True, so check bool BEFORE int!
    """
    raise NotImplementedError


def is_blank(s: str | None) -> bool:
    """True if s is None or an empty string. Use truthiness — this fits on one line."""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40


def test_average():
    assert average(1, 2) == 1.5
    assert average(10, 20) == 15


def test_is_even():
    assert is_even(4)
    assert not is_even(7)
    assert is_even(0)


def test_minutes_to_hours():
    assert minutes_to_hours(135) == "2h 15m"
    assert minutes_to_hours(45) == "0h 45m"
    assert minutes_to_hours(60) == "1h 0m"


def test_parse_and_double():
    assert parse_and_double("21") == 42
    assert parse_and_double("-5") == -10


def test_swap():
    assert swap((1, "a")) == ("a", 1)


def test_describe_type():
    assert describe_type(3) == "int"
    assert describe_type(3.0) == "float"
    assert describe_type("3") == "str"
    assert describe_type(True) == "bool"
    assert describe_type(None) == "None"
    assert describe_type([3]) == "other"


def test_is_blank():
    assert is_blank(None)
    assert is_blank("")
    assert not is_blank("x")
