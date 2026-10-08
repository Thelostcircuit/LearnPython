"""Lesson 9 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def safe_int(text: str, default: int = 0) -> int:
    """int(text), or `default` if it can't be parsed."""
    raise NotImplementedError


def safe_divide(a: float, b: float) -> float | None:
    """a / b, or None if b is zero. Use try/except ZeroDivisionError."""
    raise NotImplementedError


def get_nested(data: dict, *keys):
    """Follow keys into nested dicts; return None if any key is missing.

    get_nested({"a": {"b": 1}}, "a", "b") -> 1
    get_nested({"a": {"b": 1}}, "a", "x") -> None
    """
    raise NotImplementedError


def parse_ages(lines: list[str]) -> tuple[list[int], list[str]]:
    """Parse each line as an int age. Return (the ages that parsed, the lines that didn't).

    ["30", "abc", "7"] -> ([30, 7], ["abc"])
    """
    raise NotImplementedError


def set_volume(level: int) -> int:
    """Return level if it's between 0 and 10 inclusive.
    Otherwise raise ValueError with the message "volume must be 0-10, got <level>"."""
    raise NotImplementedError


class OutOfStock(Exception):
    """Raised when there isn't enough of an item."""


class Inventory:
    """(Classes are lesson 12 — here you only need to fill in the two method bodies.)"""

    def __init__(self) -> None:
        self.stock: dict[str, int] = {}

    def add(self, item: str, quantity: int) -> None:
        """Add quantity to the item's stock (starting from 0 if it's new)."""
        raise NotImplementedError

    def remove(self, item: str, quantity: int) -> None:
        """Take quantity away. If there isn't enough (or the item is unknown), raise
        OutOfStock(f"only <have> <item> left") and leave the stock unchanged."""
        raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_safe_int():
    assert safe_int("42") == 42
    assert safe_int("nope") == 0
    assert safe_int("nope", default=-1) == -1


def test_safe_divide():
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(1, 0) is None


def test_get_nested():
    data = {"a": {"b": {"c": 1}}}
    assert get_nested(data, "a", "b", "c") == 1
    assert get_nested(data, "a", "x") is None
    assert get_nested(data) == data


def test_parse_ages():
    assert parse_ages(["30", "abc", "7", ""]) == ([30, 7], ["abc", ""])


def test_set_volume():
    assert set_volume(5) == 5
    with pytest.raises(ValueError, match="volume must be 0-10, got 11"):
        set_volume(11)
    with pytest.raises(ValueError):
        set_volume(-1)


def test_inventory():
    inv = Inventory()
    inv.add("apple", 5)
    inv.add("apple", 2)
    inv.remove("apple", 3)
    assert inv.stock == {"apple": 4}
    with pytest.raises(OutOfStock, match="only 4 apple left"):
        inv.remove("apple", 10)
    assert inv.stock == {"apple": 4}  # unchanged after the failed removal
    with pytest.raises(OutOfStock):
        inv.remove("pear", 1)
