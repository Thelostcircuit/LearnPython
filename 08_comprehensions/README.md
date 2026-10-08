# Lesson 8 — Comprehensions and Friends

You've written many loops like this:

```python
squares = []
for n in range(10):
    if n % 2 == 0:
        squares.append(n * n)
```

A **comprehension** says the same in one readable line:

```python
squares = [n * n for n in range(10) if n % 2 == 0]
#          ^ what  ^ for each...     ^ optional filter
```

## The four kinds

```python
[x * 2 for x in items]                 # list
{x % 3 for x in items}                 # set
{word: len(word) for word in words}    # dict
(x * 2 for x in items)                 # generator expression — lazy, see below
```

With an `if ... else` **choosing the value** (note: it goes *before* the `for`):

```python
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
```

Nested loops read left to right, like the equivalent `for` statements:

```python
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
flat = [item for row in matrix for item in row]
```

**Readability rule:** if a comprehension doesn't fit comfortably on one or two lines, or needs
more than one `if`, write a normal loop instead.

## Generator expressions — lazy comprehensions

Parentheses instead of brackets produce values **one at a time, on demand**, without building a
list in memory:

```python
total = sum(n * n for n in range(1_000_000))   # no million-item list created
any(line.startswith("#") for line in lines)     # stops at the first match
```

When a generator is the only argument, the extra brackets can be dropped, like the `sum(...)`
above. Lesson 14 goes deeper into generators.

## Built-ins that pair well with comprehensions

| Built-in | Does |
| --- | --- |
| `enumerate(items, start=0)` | `(index, item)` pairs |
| `zip(a, b)` | pairs items from several iterables (stops at the shortest; `strict=True` to require equal length) |
| `sorted(items, key=..., reverse=...)` | new sorted list |
| `reversed(items)` | iterate backwards |
| `sum`, `min`, `max` (also with `key=`) | aggregate |
| `any`, `all` | "is any/every item truthy?" |
| `map(f, items)`, `filter(f, items)` | older style; comprehensions are usually clearer |

```python
oldest = max(people, key=lambda p: p["age"])
by_name = {p["name"]: p for p in people}           # index a list by a field
dict(zip(names, ages))                              # two lists → dict
```

## Key takeaways

- `[expr for x in items if cond]` replaces the build-a-list loop.
- Set `{...}` and dict `{k: v ...}` comprehensions work the same way.
- `(... for ...)` is lazy; perfect inside `sum`, `any`, `all`, `max`.
- Keep them short. A plain loop is better than a clever, unreadable comprehension.
