"""textkit — a tiny text-processing package. (Lesson 11 solution.)"""

from .cleaning import normalize_whitespace, remove_punctuation
from .stats import most_common_word, word_count

__all__ = ["normalize_whitespace", "remove_punctuation", "word_count", "most_common_word"]
