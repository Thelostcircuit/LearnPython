"""Lesson 5 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def area(width: float, height: float | None = None) -> float:
    """Area of a rectangle. If height is left out, it's a square (height = width)."""
    raise NotImplementedError


def stats(numbers: list[float]) -> tuple[float, float, float]:
    """Return (smallest, largest, average) of a non-empty list — a tuple of three values."""
    raise NotImplementedError


def join_words(*words: str, sep: str = " ") -> str:
    """Join any number of words with `sep` (keyword-only, default a space).

    join_words("a", "b", "c") -> "a b c"
    join_words("a", "b", sep="-") -> "a-b"
    """
    raise NotImplementedError


def make_url(base: str, **params: str | int) -> str:
    """Build a URL with query parameters, in the order given.

    make_url("https://x.com/search", q="python", page=2) -> "https://x.com/search?q=python&page=2"
    make_url("https://x.com") -> "https://x.com"
    """
    raise NotImplementedError


def add_item(item: str, basket: list[str] | None = None) -> list[str]:
    """Add item to basket and return it. With no basket given, start a NEW empty one each call.
    (The tests check you avoided the mutable default trap!)"""
    raise NotImplementedError


def apply_n_times(func, value, n: int):
    """Call func on value n times: apply_n_times(double, 1, 3) == 8."""
    raise NotImplementedError


def sort_by_last_letter(words: list[str]) -> list[str]:
    """Return a new list sorted by each word's LAST letter. Use sorted() with a key=lambda."""
    raise NotImplementedError


def make_multiplier(factor: int):
    """Return a NEW FUNCTION that multiplies its argument by factor.

    triple = make_multiplier(3); triple(5) == 15
    Hint: define a function inside this one, and return it (without calling it!).
    """
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_area():
    assert area(3, 4) == 12
    assert area(5) == 25


def test_stats():
    assert stats([3, 1, 2]) == (1, 3, 2)
    smallest, largest, avg = stats([10])
    assert (smallest, largest, avg) == (10, 10, 10)


def test_join_words():
    assert join_words("a", "b", "c") == "a b c"
    assert join_words("a", "b", sep="-") == "a-b"
    assert join_words() == ""


def test_make_url():
    assert (
        make_url("https://x.com/search", q="python", page=2)
        == "https://x.com/search?q=python&page=2"
    )
    assert make_url("https://x.com") == "https://x.com"


def test_add_item():
    assert add_item("apple") == ["apple"]
    assert add_item("pear") == ["pear"]  # fails if the default list is shared!
    mine = ["milk"]
    assert add_item("eggs", mine) == ["milk", "eggs"]


def test_apply_n_times():
    assert apply_n_times(lambda x: x * 2, 1, 3) == 8
    assert apply_n_times(str.upper, "hi", 0) == "hi"


def test_sort_by_last_letter():
    assert sort_by_last_letter(["cab", "bad", "ace"]) == ["cab", "bad", "ace"]
    assert sort_by_last_letter(["xz", "ya", "wm"]) == ["ya", "wm", "xz"]


def test_make_multiplier():
    triple = make_multiplier(3)
    double = make_multiplier(2)
    assert triple(5) == 15
    assert double(5) == 10
