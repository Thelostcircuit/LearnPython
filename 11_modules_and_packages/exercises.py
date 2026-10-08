"""Lesson 11 exercises — this time the code you write lives in the `textkit/` package.

1. Fill in textkit/cleaning.py and textkit/stats.py.
2. Re-export the functions from textkit/__init__.py.
3. Create a NEW file, textkit/fun.py, with a function `shout(text: str) -> str` that returns
   the text uppercased with "!" on the end, and a module-level constant `VERSION = "1.0"`.

Then run `uv run pytest`. (The imports are inside each test so one missing piece doesn't
break all the others.)
"""

# ---- Tests (you don't need to change anything below) ---------------------------------


def test_normalize_whitespace():
    from textkit.cleaning import normalize_whitespace

    assert normalize_whitespace("  hello \n\t world  ") == "hello world"


def test_remove_punctuation():
    from textkit.cleaning import remove_punctuation

    assert remove_punctuation("Hi, there! (ok?)") == "Hi there ok"


def test_word_count():
    from textkit.stats import word_count

    assert word_count("Hello, hello! How are you?") == 5
    assert word_count("") == 0


def test_most_common_word():
    from textkit.stats import most_common_word

    assert most_common_word("The cat. The hat! the END") == "the"
    assert most_common_word("b a b a") == "b"


def test_package_reexports():
    import textkit

    for name in ["normalize_whitespace", "remove_punctuation", "word_count", "most_common_word"]:
        assert hasattr(textkit, name), f"textkit/__init__.py should re-export {name}"


def test_fun_module():
    from textkit.fun import VERSION, shout

    assert shout("hi") == "HI!"
    assert VERSION == "1.0"
