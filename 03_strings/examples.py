"""Lesson 3 examples. Run with: uv run python examples.py"""

s = "Python"

# --- Indexing & slicing ---------------------------------------------------------------
print(f"s = {s!r}, len = {len(s)}")
print(f"s[0] = {s[0]!r}, s[-1] = {s[-1]!r}")
print(f"s[1:4] = {s[1:4]!r}, s[:2] = {s[:2]!r}, s[2:] = {s[2:]!r}")
print(f"s[::2] = {s[::2]!r}, s[::-1] = {s[::-1]!r}")
print(f"s[100:] = {s[100:]!r}  (slices never raise)")
# print(s[100])  # <- uncomment: IndexError

# --- Immutability ---------------------------------------------------------------------
# s[0] = "J"  # <- uncomment: TypeError
jython = "J" + s[1:]
print(f"new string: {jython!r}, original unchanged: {s!r}")

# --- Combining ------------------------------------------------------------------------
print("ab" + "cd", "ab" * 3, "-".join(["2026", "09", "23"]))
print(f"'yth' in s: {'yth' in s}")

# --- Methods --------------------------------------------------------------------------
text = "  Hello, World!  "
print(f"strip: {text.strip()!r}")
print(f"upper: {text.strip().upper()!r}  lower: {text.strip().lower()!r}")
print(f"title: {'the quick brown fox'.title()!r}")
csv_line = "a,b,c"
print(f"split(','): {csv_line.split(',')}")
spaced = "  lots   of   space  "
print(f"split(): {spaced.split()}")
print(f"replace: {'2026-09-23'.replace('-', '/')!r}")
print(f"startswith/endswith: {'notes.txt'.startswith('notes')}, {'notes.txt'.endswith('.md')}")
print(f"find: {'hello'.find('l')}, find missing: {'hello'.find('z')}")
print(f"count: {'banana'.count('a')}")
print(f"isdigit: {'2026'.isdigit()}, isalpha: {'abc'.isalpha()}, {'abc1'.isalpha()}")
print(f"removesuffix: {'report.pdf'.removesuffix('.pdf')!r}")
print(f"zfill: {'7'.zfill(3)!r}, center: {'hi'.center(8, '*')!r}")
print(f"partition: {'key=value'.partition('=')}")

# Methods chain nicely because each returns a string:
messy = "  MiXeD case INPUT  "
print(f"chained: {messy.strip().lower().replace(' ', '_')!r}")

# --- Looping --------------------------------------------------------------------------
vowels = 0
for ch in "programming":
    if ch in "aeiou":
        vowels += 1
print(f"'programming' has {vowels} vowels")

# --- Escapes & raw strings ------------------------------------------------------------
print("tab:\tafter tab\nnew line, and a backslash: \\")
print(r"raw: C:\new\folder  (the \n stays as-is)")

# --- Unicode --------------------------------------------------------------------------
snake = "héllo 🐍"
print(f"{snake!r} has {len(snake)} characters")
print(f"ord('A') = {ord('A')}, chr(97) = {chr(97)!r}")

# --- Multi-line strings ---------------------------------------------------------------
poem = """Roses are red,
Python is neat."""
for i, line in enumerate(poem.splitlines(), start=1):
    print(f"line {i}: {line}")
