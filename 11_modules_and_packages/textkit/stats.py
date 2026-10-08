"""Functions that measure text.

TODO: import remove_punctuation from the sibling `cleaning` module with a RELATIVE import,
and use it in both functions below so "Hello, hello!" counts as two words "hello".
"""


def word_count(text: str) -> int:
    """Number of words, ignoring punctuation."""
    raise NotImplementedError


def most_common_word(text: str) -> str:
    """The most frequent word, lowercased, ignoring punctuation. Ties: the one seen first."""
    raise NotImplementedError
