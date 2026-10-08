"""Lesson 14 — solutions."""

import itertools
from collections.abc import Iterable, Iterator


def evens(limit: int) -> Iterator[int]:
    n = 0
    while n < limit:
        yield n
        n += 2


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n: int, iterable: Iterable) -> list:
    return list(itertools.islice(iterable, n))


def running_total(numbers: Iterable[int]) -> Iterator[int]:
    total = 0
    for n in numbers:
        total += n
        yield total


def chunked(items: Iterable, size: int) -> Iterator[list]:
    chunk = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def unique(items: Iterable) -> Iterator:
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def read_numbers(lines: Iterable[str]) -> Iterator[int]:
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            yield int(stripped)


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> Iterator[int]:
        n = self.start
        while n > 0:
            yield n
            n -= 1
