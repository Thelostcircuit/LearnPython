"""Lesson 3 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def reverse(s: str) -> str:
    """Reverse a string.  "hello" -> "olleh"  (one slice!)"""
    raise NotImplementedError


def initials(full_name: str) -> str:
    """Uppercase initials:  "ada lovelace" -> "AL".  Hint: split(), then take word[0]."""
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """True if s reads the same backwards, ignoring case and anything that isn't a letter.

    "A man, a plan, a canal: Panama" -> True
    Hint: build a new string of only lowercase letters (ch.isalpha()), then compare to its reverse.
    """
    raise NotImplementedError


def count_vowels(s: str) -> int:
    """Count a, e, i, o, u (either case)."""
    raise NotImplementedError


def slugify(title: str) -> str:
    """Make a URL slug: strip, lowercase, words joined with "-".

    "  Hello World From Python  " -> "hello-world-from-python"
    """
    raise NotImplementedError


def mask_card(number: str) -> str:
    """Hide all but the last 4 digits with *:  "1234567812345678" -> "************5678"."""
    raise NotImplementedError


def file_extension(filename: str) -> str:
    """Return the extension without the dot, lowercased, or "" if there isn't one.

    "photo.JPG" -> "jpg",  "archive.tar.gz" -> "gz",  "README" -> ""
    Hint: rpartition(".") or rfind(".")
    """
    raise NotImplementedError


def caesar(text: str, shift: int) -> str:
    """Shift each lowercase letter forward by `shift` places, wrapping z -> a. Leave others alone.

    caesar("abc xyz", 3) -> "def abc"
    Hint: ord(ch) - ord("a") gives 0-25; % 26 wraps; chr(...) turns it back.
    """
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""


def test_initials():
    assert initials("ada lovelace") == "AL"
    assert initials("Grace Brewster Hopper") == "GBH"


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("python")


def test_count_vowels():
    assert count_vowels("Programming in PYTHON") == 5
    assert count_vowels("rhythm") == 0


def test_slugify():
    assert slugify("  Hello World From Python  ") == "hello-world-from-python"
    assert slugify("one") == "one"


def test_mask_card():
    assert mask_card("1234567812345678") == "************5678"
    assert mask_card("1234") == "1234"


def test_file_extension():
    assert file_extension("photo.JPG") == "jpg"
    assert file_extension("archive.tar.gz") == "gz"
    assert file_extension("README") == ""


def test_caesar():
    assert caesar("abc xyz", 3) == "def abc"
    assert caesar("hello, world!", 13) == "uryyb, jbeyq!"
