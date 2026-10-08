"""Lesson 6 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def evens(numbers: list[int]) -> list[int]:
    """A new list of only the even numbers, in order. Use a for loop and append."""
    raise NotImplementedError


def second_largest(numbers: list[int]) -> int:
    """The second-largest DISTINCT value. [5, 1, 5, 3] -> 3. Assume there are at least two."""
    raise NotImplementedError


def median(numbers: list[float]) -> float:
    """Middle value of the sorted list; for an even count, the average of the two middle values.
    Don't change the caller's list! (Use sorted(), not .sort().)"""
    raise NotImplementedError


def rotate(items: list, k: int) -> list:
    """Rotate right by k:  rotate([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3].

    Hint: slices, and k %= len(items) so rotating by more than the length still works."""
    raise NotImplementedError


def dedupe(items: list) -> list:
    """Remove duplicates, keeping the FIRST occurrence and the original order."""
    raise NotImplementedError


def chunk(items: list, size: int) -> list[list]:
    """Split into chunks of `size`:  chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]
    Hint: range(0, len(items), size) and slicing."""
    raise NotImplementedError


def flatten(nested: list[list]) -> list:
    """[[1, 2], [3], []] -> [1, 2, 3]"""
    raise NotImplementedError


def head_and_tail(items: list) -> tuple:
    """Return (first item, list of the rest) using star-unpacking:  first, *rest = items"""
    raise NotImplementedError


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Swap rows and columns: [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]"""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_evens():
    assert evens([1, 2, 3, 4, 6]) == [2, 4, 6]
    assert evens([1, 3]) == []


def test_second_largest():
    assert second_largest([5, 1, 5, 3]) == 3
    assert second_largest([1, 2]) == 1


def test_median():
    data = [3, 1, 2]
    assert median(data) == 2
    assert data == [3, 1, 2]  # unchanged!
    assert median([4, 1, 3, 2]) == 2.5


def test_rotate():
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3], 4) == [3, 1, 2]


def test_dedupe():
    assert dedupe([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedupe(["a", "a"]) == ["a"]


def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 3) == []


def test_flatten():
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]


def test_head_and_tail():
    assert head_and_tail([1, 2, 3]) == (1, [2, 3])
    assert head_and_tail(["only"]) == ("only", [])


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
