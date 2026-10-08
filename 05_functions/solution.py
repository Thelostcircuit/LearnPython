"""Lesson 5 — solutions."""


def area(width: float, height: float | None = None) -> float:
    if height is None:
        height = width
    return width * height


def stats(numbers: list[float]) -> tuple[float, float, float]:
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def join_words(*words: str, sep: str = " ") -> str:
    return sep.join(words)


def make_url(base: str, **params: str | int) -> str:
    if not params:
        return base
    query = "&".join(f"{key}={value}" for key, value in params.items())
    return f"{base}?{query}"


def add_item(item: str, basket: list[str] | None = None) -> list[str]:
    if basket is None:
        basket = []
    basket.append(item)
    return basket


def apply_n_times(func, value, n: int):
    for _ in range(n):
        value = func(value)
    return value


def sort_by_last_letter(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: word[-1])


def make_multiplier(factor: int):
    def multiply(x: int) -> int:
        return x * factor  # `factor` is remembered from the outer call (a "closure")

    return multiply
