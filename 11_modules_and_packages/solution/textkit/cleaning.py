"""Functions that clean up text."""

import string


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def remove_punctuation(text: str) -> str:
    return "".join(ch for ch in text if ch not in string.punctuation)
