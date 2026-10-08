"""Lesson 8 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`.

Challenge: solve each one with a single comprehension or generator expression!
"""


def squares_of_odds(numbers: list[int]) -> list[int]:
    """[1, 2, 3] -> [1, 9]"""
    raise NotImplementedError


def lengths(words: list[str]) -> dict[str, int]:
    """{word: len(word)}"""
    raise NotImplementedError


def unique_first_letters(words: list[str]) -> set[str]:
    """Set of lowercase first letters."""
    raise NotImplementedError


def sum_of_squares(n: int) -> int:
    """1² + 2² + ... + n², using a generator expression inside sum()."""
    raise NotImplementedError


def clip(numbers: list[int], low: int, high: int) -> list[int]:
    """Clamp each number into [low, high]:  clip([-5, 3, 99], 0, 10) -> [0, 3, 10]"""
    raise NotImplementedError


def long_words_upper(text: str, min_len: int) -> list[str]:
    """Words longer than min_len, uppercased, in order."""
    raise NotImplementedError


def multiplication_table(n: int) -> list[list[int]]:
    """n x n table:  multiplication_table(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]"""
    raise NotImplementedError


def names_by_age(people: list[dict]) -> list[str]:
    """Names sorted by age (youngest first). Each person is {"name": ..., "age": ...}."""
    raise NotImplementedError


def dot(a: list[int], b: list[int]) -> int:
    """Sum of a[i] * b[i].  Use zip."""
    raise NotImplementedError


def index_positions(items: list, target) -> list[int]:
    """Every index where `target` appears:  index_positions("banana", "a") -> [1, 3, 5]"""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_squares_of_odds():
    assert squares_of_odds([1, 2, 3, 4, 5]) == [1, 9, 25]


def test_lengths():
    assert lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}


def test_unique_first_letters():
    assert unique_first_letters(["Apple", "avocado", "Banana"]) == {"a", "b"}


def test_sum_of_squares():
    assert sum_of_squares(3) == 14
    assert sum_of_squares(0) == 0


def test_clip():
    assert clip([-5, 3, 99], 0, 10) == [0, 3, 10]


def test_long_words_upper():
    assert long_words_upper("the quick brown fox", 3) == ["QUICK", "BROWN"]


def test_multiplication_table():
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


def test_names_by_age():
    people = [{"name": "ada", "age": 36}, {"name": "linus", "age": 21}]
    assert names_by_age(people) == ["linus", "ada"]


def test_dot():
    assert dot([1, 2, 3], [4, 5, 6]) == 32


def test_index_positions():
    assert index_positions(list("banana"), "a") == [1, 3, 5]
    assert index_positions([1, 2], 9) == []
