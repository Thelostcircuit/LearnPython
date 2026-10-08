# Lesson 14 — Iterators and Generators

## What `for` really does

```python
for x in [1, 2, 3]:
    print(x)
```

is roughly:

```python
it = iter([1, 2, 3])         # ask the list for an ITERATOR
while True:
    try:
        x = next(it)         # get the next value...
    except StopIteration:    # ...until it's exhausted
        break
    print(x)
```

- An **iterable** is anything you can loop over (list, str, dict, file, range...). It has
  `__iter__`.
- An **iterator** produces values one by one with `next()`, and remembers where it is. Once
  exhausted, it stays empty.

```python
it = iter("ab")
next(it)   # 'a'
next(it)   # 'b'
next(it)   # StopIteration
```

## Generators — the easy way to make iterators

A function containing **`yield`** is a *generator function*. Calling it doesn't run the body.
It returns a generator, which runs the body a bit at a time, pausing at each `yield`:

```python
def countdown(n: int):
    while n > 0:
        yield n        # hand out a value, then PAUSE here until the next one is requested
        n -= 1

for x in countdown(3):
    print(x)           # 3, 2, 1

list(countdown(3))     # [3, 2, 1]
```

Why is this useful?

- **Lazy**: values are produced only when needed, so memory stays tiny even for huge or infinite
  sequences.
- **Pipelines**: chain small generators into a processing pipeline where each item flows through
  one at a time.

```python
def read_lines(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

def non_blank(lines):
    for line in lines:
        if line.strip():
            yield line

for line in non_blank(read_lines("big.log")):   # never loads the whole file
    ...
```

`yield from other_iterable` yields every value from another iterable.

Infinite generators are fine, as long as the consumer stops:

```python
def naturals():
    n = 0
    while True:
        yield n
        n += 1
```

## Generator expressions (recap from lesson 8)

`(x * x for x in data)` is a one-line generator.

## `itertools` — building blocks for iteration

```python
import itertools

itertools.count(10)                      # 10, 11, 12, ... forever
itertools.islice(gen, 5)                 # first 5 items of any iterator (like slicing)
itertools.chain([1, 2], [3])             # 1, 2, 3
itertools.cycle("ab")                    # a, b, a, b, ...
itertools.takewhile(lambda x: x < 5, xs) # items until the condition fails
itertools.pairwise([1, 2, 3])            # (1, 2), (2, 3)
itertools.batched(range(7), 3)           # (0, 1, 2), (3, 4, 5), (6,)
itertools.groupby(sorted_items, key=...) # group consecutive items
itertools.product("ab", repeat=2)        # aa ab ba bb
itertools.permutations([1, 2, 3], 2); itertools.combinations([1, 2, 3], 2)
```

## Making your own class iterable

Give it an `__iter__` that's a generator. That's usually all you need:

```python
class Playlist:
    def __init__(self, songs: list[str]) -> None:
        self.songs = songs

    def __iter__(self):
        yield from self.songs
```

## Key takeaways

- `for` calls `iter()` then `next()` until `StopIteration`.
- A function with `yield` is a generator: lazy, pausable, memory-cheap.
- Chain generators into pipelines; `itertools` has ready-made pieces.
- Iterators are single-use. Loop again by calling the generator function again.
