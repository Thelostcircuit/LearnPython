"""Functions that measure text."""

from .cleaning import remove_punctuation


def word_count(text: str) -> int:
    return len(remove_punctuation(text).split())


def most_common_word(text: str) -> str:
    counts: dict[str, int] = {}
    for word in remove_punctuation(text).lower().split():
        counts[word] = counts.get(word, 0) + 1
    # max() returns the first maximum it meets, and dicts keep insertion order → first seen wins
    return max(counts, key=counts.__getitem__)
