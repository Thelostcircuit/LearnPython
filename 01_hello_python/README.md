# Lesson 1 — Hello, Python

## Running Python

There are two ways to run Python code:

1. **A script**: put code in a `.py` file and run it: `uv run python examples.py`
2. **The REPL**: type `python3` and enter code line by line. Each expression's value is printed
   straight away. Perfect for experiments.

Python runs a script **top to bottom**, one line at a time. There's no `main` function required
(though you'll see a common pattern for one in lesson 11).

## Your first program

```python
print("Hello, world!")
```

- `print` is a built-in **function**. You call it with parentheses.
- Text in quotes is a **string**. `'single'` and `"double"` quotes are the same thing.
- No semicolons, no braces. Python uses **indentation** (4 spaces) to group code, as you'll see
  in lesson 4.

## `print` in more detail

```python
print("a", "b", "c")            # a b c        — separated by spaces
print("a", "b", sep="-")        # a-b
print("no newline", end="")     # stays on the same line
print()                         # just a blank line
```

## f-strings — putting values into text

Put an `f` before the quotes, and anything in `{braces}` is evaluated:

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")        # Ada is 36 years old
print(f"Next year: {age + 1}")             # any expression works
print(f"{name=}")                          # name='Ada'   — handy for debugging!
```

Format specs go after a colon:

```python
pi = 3.14159
print(f"{pi:.2f}")        # 3.14        — 2 decimal places
print(f"[{42:>5}]")       # [   42]     — right-align, width 5
print(f"[{42:<5}]")       # [42   ]     — left-align
print(f"[{42:^5}]")       # [ 42  ]     — centre
print(f"[{42:05}]")       # [00042]     — zero-pad
print(f"{1234567:,}")     # 1,234,567   — thousands separator
print(f"{0.256:.1%}")     # 25.6%       — percentage
```

## Comments and docstrings

```python
# A comment runs to the end of the line.

def greet():
    """A docstring: the first string in a function documents it. help(greet) shows it."""
```

## `input` — reading from the keyboard

```python
name = input("What's your name? ")   # always returns a string
print(f"Hi, {name}!")
```

(The examples file skips `input` so it can run unattended. Try it in the REPL!)

## Key takeaways

- `uv run python file.py` runs a script; `python3` opens the REPL.
- `print(...)` prints; `f"...{value}..."` builds strings with values inside.
- `{value:.2f}`, `{value:>5}`, `{value:,}` control formatting.
- `#` for comments, `"""docstrings"""` to document functions.
