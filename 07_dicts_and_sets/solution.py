"""Lesson 7 — solutions."""


def word_counts(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert(d: dict[str, int]) -> dict[int, str]:
    result = {}
    for key, value in d.items():
        result[value] = key
    return result


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


def lookup_price(prices: dict[str, float], item: str) -> float:
    return prices.get(item, 0.0)


def total_cost(prices: dict[str, float], basket: dict[str, int]) -> float:
    total = 0.0
    for item, quantity in basket.items():
        total += prices.get(item, 0.0) * quantity
    return total


def common_letters(a: str, b: str) -> str:
    return "".join(sorted(set(a) & set(b)))


def has_duplicates(items: list) -> bool:
    return len(items) != len(set(items))


def first_repeated_char(s: str) -> str | None:
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


def merge_scores(*score_dicts: dict[str, int]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for scores in score_dicts:
        for player, score in scores.items():
            totals[player] = totals.get(player, 0) + score
    return totals
