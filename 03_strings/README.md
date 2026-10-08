# Lesson 3 — Strings

Strings (`str`) are **sequences of characters**, and they're **immutable**: you can't change a
string in place. Every "change" makes a new string.

## Indexing and slicing

```python
s = "Python"
s[0]      # 'P'         — first
s[-1]     # 'n'         — last (negative counts from the end)
s[1:4]    # 'yth'       — from index 1 up to (not including) 4
s[:2]     # 'Py'        — from the start
s[2:]     # 'thon'      — to the end
s[::2]    # 'Pto'       — every 2nd character
s[::-1]   # 'nohtyP'    — reversed!
len(s)    # 6
```

Slices never raise errors for out-of-range values: `s[100:]` is just `''`. A single index out of
range (`s[100]`) raises `IndexError`.

```python
s[0] = "J"          # ❌ TypeError: strings are immutable
s = "J" + s[1:]     # ✅ make a new string instead
```

## Combining

```python
"ab" + "cd"             # 'abcd'
"ab" * 3                # 'ababab'
"-".join(["a", "b"])    # 'a-b'       — join a list of strings with a separator
"py" in "python"        # True        — substring check
```

## The most useful methods

Methods are called with a dot, and always **return a new string**:

| Method | Example | Result |
| --- | --- | --- |
| `upper`, `lower`, `title`, `capitalize` | `"hi there".title()` | `'Hi There'` |
| `strip`, `lstrip`, `rstrip` | `"  hi  ".strip()` | `'hi'` |
| `split` | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `split()` (no argument) | `" a  b ".split()` | `['a', 'b']` — any whitespace |
| `replace` | `"aXbX".replace("X", "-")` | `'a-b-'` |
| `startswith`, `endswith` | `"file.py".endswith(".py")` | `True` |
| `find`, `index` | `"hello".find("l")` | `2` (`find` gives -1 if missing; `index` raises) |
| `count` | `"banana".count("a")` | `3` |
| `isdigit`, `isalpha`, `isalnum`, `isspace`, `isupper` | `"42".isdigit()` | `True` |
| `removeprefix`, `removesuffix` | `"file.py".removesuffix(".py")` | `'file'` |
| `center`, `ljust`, `rjust`, `zfill` | `"7".zfill(3)` | `'007'` |
| `splitlines` | `"a\nb".splitlines()` | `['a', 'b']` |

Explore more in the REPL: `dir(str)` lists them all, `help(str.partition)` explains one.

## Looping over a string

```python
for ch in "hi!":
    print(ch)
```

## Escapes and raw strings

```python
"line 1\nline 2"     # \n newline, \t tab, \\ backslash, \" quote
r"C:\new\folder"     # raw string: backslashes are literal (handy for regexes and paths)
```

## Characters and Unicode

Python strings are full Unicode: `"🐍"` is one character, `len("héllo") == 5`.
`ord("A")` → `65`, `chr(65)` → `'A'`.

## Key takeaways

- Index with `s[i]`, slice with `s[start:stop:step]`; `s[::-1]` reverses.
- Strings are immutable. Methods return new strings.
- `split` and `join` convert between strings and lists. `in` checks for substrings.
- f-strings (lesson 1) are the go-to way to build strings.
