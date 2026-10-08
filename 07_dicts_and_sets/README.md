# Lesson 7 — Dictionaries and Sets

## Dictionaries — key → value lookup

```python
ages = {"ada": 36, "grace": 85}
ages["ada"]            # 36
ages["linus"] = 21     # add or overwrite
del ages["grace"]      # remove
"ada" in ages          # True   — checks KEYS
len(ages)              # 2
```

- Keys must be **immutable** (hashable): strings, numbers, tuples. Not lists.
- Dicts **remember insertion order**.
- Looking up a missing key with `[]` raises `KeyError`.

## Safe access

```python
ages.get("bob")              # None instead of KeyError
ages.get("bob", 0)           # or a default of your choice
ages.setdefault("bob", 0)    # insert the default if missing, then return the value
ages.pop("bob", None)        # remove & return (with a default so it can't fail)
```

## Looping

```python
for name in ages:                   # keys
for age in ages.values():           # values
for name, age in ages.items():      # both — the most common
```

Don't add or remove keys *while* looping over a dict. Loop over `list(ages)` if you need to.

## Common patterns

**Counting:**

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

**Grouping:**

```python
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
```

(Lesson 17 shows `collections.Counter` and `defaultdict`, which do these even more neatly.)

**Merging:** `merged = defaults | overrides` (right side wins), or `d.update(other)` in place.

**Nested data** (like JSON):

```python
user = {"name": "ada", "langs": ["python", "rust"], "address": {"city": "London"}}
user["address"]["city"]      # 'London'
```

## Sets — unique, unordered values

```python
colors = {"red", "green", "red"}   # {'red', 'green'} — duplicates vanish
empty = set()                      # NOT {} — that's an empty dict!
colors.add("blue")
colors.discard("pink")             # remove if present (no error)
"red" in colors                    # True — and very fast, even for huge sets
unique = set(some_list)            # quick de-duplication (order is lost)
```

Set maths:

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b     # {1, 2, 3, 4}   union
a & b     # {2, 3}         intersection
a - b     # {1}            difference
a ^ b     # {1, 4}         in one or the other, not both
a <= b    # False          subset?
```

**Performance tip:** `x in some_list` checks every item; `x in some_set` or `x in some_dict` is
near-instant. If you look things up a lot, use a set or dict.

## Key takeaways

- Dicts map keys to values: `d[k]`, `d.get(k, default)`, `d.items()` for looping.
- `get`/`setdefault` make counting and grouping easy.
- Sets hold unique values with fast `in` checks and set maths (`| & - ^`).
- `{}` is an empty dict; `set()` is an empty set.
