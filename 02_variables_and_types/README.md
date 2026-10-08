# Lesson 2 — Variables and Types

## Variables are names

```python
x = 5
x = "now a string"     # fine — the NAME x now points at a different value
```

A variable in Python is a **name attached to a value**. There's no declaration and no fixed type.
The *value* has a type, not the name. This is called **dynamic typing**.

Naming rules: letters, digits, underscores; can't start with a digit; case-sensitive. Convention
is `snake_case` for variables and functions, `UPPER_CASE` for constants (Python doesn't enforce
constants; the capitals are a promise not to change it).

```python
MAX_USERS = 100
user_count = 3
a, b = 1, 2          # assign several at once
a, b = b, a          # swap!
```

## The basic types

| Type | Examples | Notes |
| --- | --- | --- |
| `int` | `42`, `-7`, `1_000_000`, `0xff`, `0b1010` | **Unlimited size** — `2 ** 1000` just works |
| `float` | `3.14`, `1e-3`, `float("inf")` | 64-bit; `0.1 + 0.2 == 0.30000000000000004` |
| `bool` | `True`, `False` | Capitalised! |
| `str` | `"hi"`, `'hi'` | Text (lesson 3) |
| `NoneType` | `None` | "No value" — like null elsewhere |

`type(x)` tells you the type; `isinstance(x, int)` checks it.

## Arithmetic

```python
7 + 2    # 9
7 - 2    # 5
7 * 2    # 14
7 / 2    # 3.5    — / ALWAYS gives a float
7 // 2   # 3      — floor division
7 % 2    # 1      — remainder (modulo)
7 ** 2   # 49     — power
-7 // 2  # -4     — floors toward negative infinity, not toward zero!

x += 1   # also -=, *=, /=, //=, %=, **=   (there is no x++)
```

Handy built-ins: `abs(-3)`, `round(3.14159, 2)`, `min(1, 2)`, `max(1, 2)`, `divmod(7, 2)` → `(3, 1)`.
More in the `math` module: `import math; math.sqrt(2); math.pi; math.floor(2.7)`.

## Converting between types

```python
int("42")       # 42
int(3.99)       # 3        — truncates toward zero
float("3.5")    # 3.5
str(42)         # "42"
bool(0)         # False
int("abc")      # ❌ ValueError (lesson 9 shows how to handle this)
```

Python won't silently mix strings and numbers: `"3" + 4` is a `TypeError`. You must convert.

## Truthiness

In an `if`, **every** value counts as true or false:

- **Falsy:** `False`, `None`, `0`, `0.0`, `""`, and empty collections (`[]`, `{}`, `()`, `set()`)
- **Truthy:** everything else

```python
name = ""
if not name:
    print("name is empty")
```

## Comparisons and logic

`==`, `!=`, `<`, `<=`, `>`, `>=`. They can be chained: `0 < x < 10`.
Logic uses words: `and`, `or`, `not`.

`is` checks whether two names refer to the **same object**. Use it only for `None`:
`if x is None:`. For everything else, compare values with `==`.

## Type hints (a preview)

You can *annotate* types. Python itself ignores them when running, but your editor
(basedpyright) and humans use them:

```python
age: int = 36
def double(n: int) -> int:
    return n * 2
```

The exercises use hints throughout. You'll learn more about them in lesson 5.

## Key takeaways

- Variables are names; values have types. `type()` and `isinstance()` inspect them.
- `/` always gives a float; `//` floors; `%` is remainder; `**` is power.
- Convert explicitly with `int()`, `float()`, `str()`. No silent mixing.
- Empty/zero/`None` values are falsy. Use `is None` to check for `None`.
