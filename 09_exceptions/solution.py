"""Lesson 9 — solutions."""


def safe_int(text: str, default: int = 0) -> int:
    try:
        return int(text)
    except ValueError:
        return default


def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


def get_nested(data: dict, *keys):
    current = data
    try:
        for key in keys:
            current = current[key]
    except (KeyError, TypeError):  # TypeError: tried to index into a non-dict
        return None
    return current


def parse_ages(lines: list[str]) -> tuple[list[int], list[str]]:
    ages: list[int] = []
    bad: list[str] = []
    for line in lines:
        try:
            ages.append(int(line))
        except ValueError:
            bad.append(line)
    return ages, bad


def set_volume(level: int) -> int:
    if not 0 <= level <= 10:
        raise ValueError(f"volume must be 0-10, got {level}")
    return level


class OutOfStock(Exception):
    """Raised when there isn't enough of an item."""


class Inventory:
    def __init__(self) -> None:
        self.stock: dict[str, int] = {}

    def add(self, item: str, quantity: int) -> None:
        self.stock[item] = self.stock.get(item, 0) + quantity

    def remove(self, item: str, quantity: int) -> None:
        have = self.stock.get(item, 0)
        if quantity > have:
            raise OutOfStock(f"only {have} {item} left")
        self.stock[item] = have - quantity
