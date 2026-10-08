"""Lesson 6 — solutions."""


def evens(numbers: list[int]) -> list[int]:
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def second_largest(numbers: list[int]) -> int:
    distinct = sorted(set(numbers), reverse=True)  # set() removes duplicates (lesson 7)
    return distinct[1]


def median(numbers: list[float]) -> float:
    ordered = sorted(numbers)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 0:
        return (ordered[mid - 1] + ordered[mid]) / 2
    return ordered[mid]


def rotate(items: list, k: int) -> list:
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items.copy()


def dedupe(items: list) -> list:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def chunk(items: list, size: int) -> list[list]:
    chunks = []
    for start in range(0, len(items), size):
        chunks.append(items[start : start + size])
    return chunks


def flatten(nested: list[list]) -> list:
    result = []
    for inner in nested:
        result.extend(inner)
    return result


def head_and_tail(items: list) -> tuple:
    first, *rest = items
    return first, rest


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    # zip(*matrix) pairs up the first items of each row, then the second items, ...
    return [list(column) for column in zip(*matrix, strict=True)]
