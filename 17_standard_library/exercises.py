"""Lesson 17 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`.

Each one is short IF you use the right standard-library tool (named in the docstring).
"""

# ruff: noqa: F401 — some imports are only used once you've written your code

import random
import re
import statistics
from collections import Counter, defaultdict, deque
from datetime import date, timedelta


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """The n most common lowercase words with their counts.  (Counter.most_common)"""
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other (same letters, different order).

    Key each word by "".join(sorted(word)) in a defaultdict(list).
    Return the groups (each in original order), sorted by their first word.
    ["listen", "google", "silent", "enlist"] -> [["google"], ["listen", "silent", "enlist"]]
    """
    raise NotImplementedError


def last_n(items: list, n: int) -> list:
    """The last n items, processing items one at a time.  (deque with maxlen)"""
    raise NotImplementedError


def days_between(start_iso: str, end_iso: str) -> int:
    """Days from start to end, dates given as "YYYY-MM-DD".  (date.fromisoformat)"""
    raise NotImplementedError


def age_on(birth_iso: str, on_iso: str) -> int:
    """Whole years old on a given date. Careful: the birthday may not have happened yet that year.
    Hint: compare (month, day) tuples."""
    raise NotImplementedError


def next_weekday(start_iso: str, weekday: int) -> str:
    """The next date AFTER start that falls on `weekday` (0=Monday ... 6=Sunday), as ISO.
    2026-09-23 is a Wednesday, so next_weekday("2026-09-23", 4) -> "2026-09-25" (Friday).
    (timedelta, date.weekday())"""
    raise NotImplementedError


def find_hashtags(text: str) -> list[str]:
    """All #hashtags (without the #), in order.  (re.findall with r"#(\\w+)")"""
    raise NotImplementedError


def is_valid_time(text: str) -> bool:
    """True for a 24-hour "HH:MM" time from 00:00 to 23:59.  (re.fullmatch)
    Hint: hours are [01]\\d or 2[0-3]; minutes are [0-5]\\d"""
    raise NotImplementedError


def roll_dice(n: int, seed: int) -> list[int]:
    """n dice rolls (1-6) from random.Random(seed): the same seed always gives the same rolls."""
    raise NotImplementedError


def summarize(numbers: list[float]) -> dict[str, float]:
    """{"mean": ..., "median": ..., "stdev": ...}  (statistics)"""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_top_words():
    assert top_words("The cat and the hat and THE bat", 2) == [("the", 3), ("and", 2)]


def test_group_anagrams():
    words = ["listen", "google", "silent", "enlist", "banana"]
    assert group_anagrams(words) == [["banana"], ["google"], ["listen", "silent", "enlist"]]


def test_last_n():
    assert last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert last_n([1], 3) == [1]


def test_days_between():
    assert days_between("2026-09-23", "2026-12-25") == 93
    assert days_between("2024-02-28", "2024-03-01") == 2  # leap year!


def test_age_on():
    assert age_on("2000-06-15", "2026-06-14") == 25
    assert age_on("2000-06-15", "2026-06-15") == 26


def test_next_weekday():
    assert next_weekday("2026-09-23", 4) == "2026-09-25"
    assert next_weekday("2026-09-23", 2) == "2026-09-30"  # a whole week later, not the same day


def test_find_hashtags():
    assert find_hashtags("Learning #python and #rust_lang today! #100DaysOfCode") == [
        "python",
        "rust_lang",
        "100DaysOfCode",
    ]


@pytest.mark.parametrize(
    ("text", "ok"),
    [
        ("00:00", True),
        ("23:59", True),
        ("09:30", True),
        ("24:00", False),
        ("12:60", False),
        ("9:30", False),
        ("12:30pm", False),
    ],
)
def test_is_valid_time(text, ok):
    assert is_valid_time(text) == ok


def test_roll_dice():
    rolls = roll_dice(100, seed=7)
    assert len(rolls) == 100
    assert set(rolls) <= {1, 2, 3, 4, 5, 6}
    assert rolls == roll_dice(100, seed=7)
    assert rolls != roll_dice(100, seed=8)


def test_summarize():
    result = summarize([2, 4, 4, 4, 5, 5, 7, 9])
    assert result["mean"] == 5
    assert result["median"] == 4.5
    assert result["stdev"] == pytest.approx(2.138, abs=0.001)
