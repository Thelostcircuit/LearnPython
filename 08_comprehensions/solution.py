"""Lesson 8 — solutions."""


def squares_of_odds(numbers: list[int]) -> list[int]:
    return [n * n for n in numbers if n % 2 == 1]


def lengths(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


def unique_first_letters(words: list[str]) -> set[str]:
    return {word[0].lower() for word in words}


def sum_of_squares(n: int) -> int:
    return sum(i * i for i in range(1, n + 1))


def clip(numbers: list[int], low: int, high: int) -> list[int]:
    return [min(max(n, low), high) for n in numbers]


def long_words_upper(text: str, min_len: int) -> list[str]:
    return [word.upper() for word in text.split() if len(word) > min_len]


def multiplication_table(n: int) -> list[list[int]]:
    return [[row * col for col in range(1, n + 1)] for row in range(1, n + 1)]


def names_by_age(people: list[dict]) -> list[str]:
    return [p["name"] for p in sorted(people, key=lambda p: p["age"])]


def dot(a: list[int], b: list[int]) -> int:
    return sum(x * y for x, y in zip(a, b, strict=True))


def index_positions(items: list, target) -> list[int]:
    return [i for i, item in enumerate(items) if item == target]
