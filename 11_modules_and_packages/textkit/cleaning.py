"""Functions that clean up text."""

import string  # noqa: F401 — you will need this


def normalize_whitespace(text: str) -> str:
    """Collapse runs of spaces/tabs/newlines into single spaces and strip the ends.

    "  hello \\n\\t world  " -> "hello world"
    """
    raise NotImplementedError


def remove_punctuation(text: str) -> str:
    """Remove every character in string.punctuation:  "Hi, there!" -> "Hi there" """
    raise NotImplementedError
