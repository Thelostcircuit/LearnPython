# Lesson 5 — Functions

## Defining and calling

```python
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

add(2, 3)        # 5
```

- `def name(parameters):` then an indented body.
- `return` sends a value back. A function without `return` (or with a bare `return`) returns
  `None`.
- `: int` and `-> int` are **type hints**. They're optional and not enforced at runtime, but they
  document intent and let your editor catch mistakes. Use them.

## Returning several values

Return a tuple, and unpack it at the call site:

```python
def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4])
```

## Default values

```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

greet("Ada")               # Hello, Ada!
greet("Ada", "Hi")         # Hi, Ada!
greet("Ada", greeting="Hey")  # keyword argument — clearer at the call site
```

⚠️ **Never use a mutable default** like `def f(items=[])`. The list is created once and shared
across calls (you met this bug as ruff's `B006` in lesson 0). Use `None` and create it inside.

## Positional vs keyword arguments

```python
def connect(host: str, port: int = 22, *, timeout: float = 5.0) -> None: ...
#                                       ^ everything after * is keyword-only

connect("example.com", 2222, timeout=1.0)   # ✅
connect("example.com", 2222, 1.0)           # ❌ timeout must be named
```

Keyword-only arguments stop confusing calls like `f(True, False, 3)`.
(There's also `/` for positional-only: `def f(a, b, /)`, which you'll see in the docs.)

## `*args` and `**kwargs` — any number of arguments

```python
def total(*numbers: int) -> int:        # numbers is a tuple
    return sum(numbers)

total(1, 2, 3)                          # 6

def tag(name: str, **attrs: str) -> str:   # attrs is a dict
    extras = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f"<{name} {extras}>"

tag("a", href="/", title="home")        # <a href="/" title="home">
```

The same `*` / `**` **unpack** at a call site: `total(*[1, 2, 3])`, `greet(**{"name": "Ada"})`.

## Scope

Variables assigned inside a function are **local** to it. Functions can *read* outer variables,
but assigning to one creates a new local variable unless you declare `global` (or `nonlocal` in
nested functions). Needing `global` is usually a sign to pass values in and return them instead.

## Functions are values

Functions are objects: you can store them in variables, put them in lists, pass them to other
functions:

```python
def shout(s: str) -> str:
    return s.upper()

f = shout
f("hi")                              # 'HI'
sorted(["b", "A", "c"], key=str.lower)   # pass a function as `key`
```

**`lambda`** makes a small anonymous function in one expression:

```python
double = lambda x: x * 2           # (assigning a lambda to a name is discouraged — use def)
sorted(people, key=lambda p: p["age"])  # this is where lambdas shine
```

## Docstrings

The first string in a function body documents it. `help(add)` shows it, and your editor shows
it on hover.

## Key takeaways

- `def f(a: int, b: int = 0) -> int:` defines; `return` gives a value back (default `None`).
- Defaults must be immutable; use `None` for "a new list each time".
- `*` makes following params keyword-only; `*args`/`**kwargs` collect extra arguments.
- Functions are values: pass them around, e.g. `key=` in `sorted`.
