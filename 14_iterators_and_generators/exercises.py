"""Lesson 14 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`.

Most of these should be GENERATOR functions: use `yield`, not `return [...]`.
"""

import itertools
from collections.abc import Iterable, Iterator


def evens(limit: int) -> Iterator[int]:
    """Yield 0, 2, 4, ... up to (not including) limit."""
    raise NotImplementedError


def fibonacci() -> Iterator[int]:
    """Yield Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, ..."""
    raise NotImplementedError


def take(n: int, iterable: Iterable) -> list:
    """The first n items as a list. Works on infinite generators. Hint: itertools.islice"""
    raise NotImplementedError


def running_total(numbers: Iterable[int]) -> Iterator[int]:
    """[1, 2, 3] -> 1, 3, 6"""
    raise NotImplementedError


def chunked(items: Iterable, size: int) -> Iterator[list]:
    """Yield lists of `size` items (the last may be shorter). Must work on ANY iterable,
    including generators — so no slicing! Collect items into a list and yield when it's full."""
    raise NotImplementedError


def unique(items: Iterable) -> Iterator:
    """Yield each item the first time it's seen, lazily (works on infinite input)."""
    raise NotImplementedError


def read_numbers(lines: Iterable[str]) -> Iterator[int]:
    """Pipeline step: skip blank lines and lines starting with "#", yield the rest as ints."""
    raise NotImplementedError


class Countdown:
    """An iterable: `for n in Countdown(3)` gives 3, 2, 1. Looping twice works both times."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> Iterator[int]:
        raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import types  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_evens_is_a_generator():
    assert isinstance(evens(10), types.GeneratorType)
    assert list(evens(10)) == [0, 2, 4, 6, 8]


def test_fibonacci_and_take():
    assert take(10, fibonacci()) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert take(3, "abcdef") == ["a", "b", "c"]


def test_running_total():
    assert list(running_total([1, 2, 3, 4])) == [1, 3, 6, 10]


def test_chunked():
    assert list(chunked(range(7), 3)) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(chunked(iter([]), 2)) == []
    assert take(2, chunked(itertools.count(), 2)) == [[0, 1], [2, 3]]  # infinite input


def test_unique():
    assert list(unique([3, 1, 3, 2, 1])) == [3, 1, 2]
    assert take(2, unique(itertools.cycle("aab"))) == ["a", "b"]


def test_read_numbers():
    lines = ["# header", "10", "", "  ", "20", "#note", "5"]
    assert sum(read_numbers(lines)) == 35


def test_countdown():
    c = Countdown(3)
    assert list(c) == [3, 2, 1]
    assert list(c) == [3, 2, 1]  # works a second time
