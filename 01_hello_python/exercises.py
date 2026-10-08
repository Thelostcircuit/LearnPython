"""Lesson 1 exercises.

Replace each `raise NotImplementedError` with working code, then run `uv run pytest`.
Hint: all of these can be solved with f-strings.
"""


def greet(name: str) -> str:
    """Return a greeting like "Hello, Alice!"."""
    raise NotImplementedError


def describe(name: str, age: int) -> str:
    """Return "<name> is <age> years old", e.g. "Ada is 36 years old"."""
    raise NotImplementedError


def three_decimals(x: float) -> str:
    """Return the number with exactly 3 decimal places: 2.0 -> "2.000", 1.23456 -> "1.235"."""
    raise NotImplementedError


def right_align(word: str) -> str:
    """Right-align the word in a box 10 characters wide, between | characters.

    "python" -> "|    python|"
    """
    raise NotImplementedError


def price_tag(item: str, price: float) -> str:
    """Return e.g. "coffee: $3.50" — always 2 decimal places."""
    raise NotImplementedError


def big_number(n: int) -> str:
    """Return the number with thousands separators: 1234567 -> "1,234,567"."""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below — but do read them!) -------------
# pytest runs every function whose name starts with test_. `assert` checks a condition.


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Python") == "Hello, Python!"


def test_describe():
    assert describe("Ada", 36) == "Ada is 36 years old"


def test_three_decimals():
    assert three_decimals(2.0) == "2.000"
    assert three_decimals(1.23456) == "1.235"


def test_right_align():
    assert right_align("python") == "|    python|"


def test_price_tag():
    assert price_tag("coffee", 3.5) == "coffee: $3.50"
    assert price_tag("cake", 4) == "cake: $4.00"


def test_big_number():
    assert big_number(1234567) == "1,234,567"
    assert big_number(12) == "12"
