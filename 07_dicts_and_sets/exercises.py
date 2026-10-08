"""Lesson 7 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def word_counts(text: str) -> dict[str, int]:
    """Count each word (split on whitespace, lowercased)."""
    raise NotImplementedError


def invert(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values:  {"a": 1, "b": 2} -> {1: "a", 2: "b"}"""
    raise NotImplementedError


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """{length: [words of that length, in original order]}"""
    raise NotImplementedError


def lookup_price(prices: dict[str, float], item: str) -> float:
    """The item's price, or 0.0 if it isn't in the dict. One line with .get()."""
    raise NotImplementedError


def total_cost(prices: dict[str, float], basket: dict[str, int]) -> float:
    """basket maps item -> quantity. Sum price * quantity. Items with no known price cost 0."""
    raise NotImplementedError


def common_letters(a: str, b: str) -> str:
    """Letters that appear in BOTH words, sorted, as one string:  ("hello", "world") -> "lo" """
    raise NotImplementedError


def has_duplicates(items: list) -> bool:
    """True if any value appears more than once. Hint: compare len(items) to len(set(items))."""
    raise NotImplementedError


def first_repeated_char(s: str) -> str | None:
    """The first character that has already been seen earlier, or None.
    "abcbad" -> "b".   Use a set of seen characters."""
    raise NotImplementedError


def merge_scores(*score_dicts: dict[str, int]) -> dict[str, int]:
    """Add up scores per player across any number of dicts.
    merge_scores({"ada": 3}, {"ada": 2, "bob": 1}) -> {"ada": 5, "bob": 1}"""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_word_counts():
    assert word_counts("The cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}


def test_invert():
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_group_by_length():
    assert group_by_length(["hi", "yo", "hey", "a"]) == {2: ["hi", "yo"], 3: ["hey"], 1: ["a"]}


def test_lookup_price():
    prices = {"apple": 0.5}
    assert lookup_price(prices, "apple") == 0.5
    assert lookup_price(prices, "caviar") == 0.0


def test_total_cost():
    prices = {"apple": 0.5, "bread": 2.0}
    assert total_cost(prices, {"apple": 4, "bread": 1, "mystery": 3}) == 4.0


def test_common_letters():
    assert common_letters("hello", "world") == "lo"
    assert common_letters("abc", "xyz") == ""


def test_has_duplicates():
    assert has_duplicates([1, 2, 1])
    assert not has_duplicates([1, 2, 3])


def test_first_repeated_char():
    assert first_repeated_char("abcbad") == "b"
    assert first_repeated_char("abc") is None


def test_merge_scores():
    assert merge_scores({"ada": 3}, {"ada": 2, "bob": 1}) == {"ada": 5, "bob": 1}
    assert merge_scores() == {}
