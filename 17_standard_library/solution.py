"""Lesson 17 — solutions."""

import random
import re
import statistics
from collections import Counter, defaultdict, deque
from datetime import date, timedelta


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    return Counter(text.lower().split()).most_common(n)


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return sorted(groups.values(), key=lambda group: group[0])


def last_n(items: list, n: int) -> list:
    window: deque = deque(maxlen=n)
    for item in items:
        window.append(item)
    return list(window)


def days_between(start_iso: str, end_iso: str) -> int:
    return (date.fromisoformat(end_iso) - date.fromisoformat(start_iso)).days


def age_on(birth_iso: str, on_iso: str) -> int:
    birth, on = date.fromisoformat(birth_iso), date.fromisoformat(on_iso)
    had_birthday = (on.month, on.day) >= (birth.month, birth.day)
    return on.year - birth.year - (0 if had_birthday else 1)


def next_weekday(start_iso: str, weekday: int) -> str:
    start = date.fromisoformat(start_iso)
    days_ahead = (weekday - start.weekday() - 1) % 7 + 1  # always 1..7 days ahead
    return (start + timedelta(days=days_ahead)).isoformat()


def find_hashtags(text: str) -> list[str]:
    return re.findall(r"#(\w+)", text)


def is_valid_time(text: str) -> bool:
    return re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", text) is not None


def roll_dice(n: int, seed: int) -> list[int]:
    rng = random.Random(seed)
    return [rng.randint(1, 6) for _ in range(n)]


def summarize(numbers: list[float]) -> dict[str, float]:
    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "stdev": statistics.stdev(numbers),
    }
