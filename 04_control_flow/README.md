# Lesson 4 — Control Flow

## Indentation is syntax

Python groups code into **blocks** by indentation (4 spaces), after a line ending in `:`.
There are no braces:

```python
if temperature > 30:
    print("hot")          # inside the if
    print("drink water")  # still inside
print("done")             # outside — runs either way
```

Mixing up indentation is an `IndentationError`. Your editor and `ruff format` keep it consistent.

## `if` / `elif` / `else`

```python
if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")
```

**Conditional expression** (Python's ternary):

```python
kind = "even" if n % 2 == 0 else "odd"
```

## `while` — repeat while a condition holds

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

## `for` — loop over anything iterable

```python
for fruit in ["apple", "banana"]:
    print(fruit)

for i in range(5):          # 0 1 2 3 4
for i in range(1, 6):       # 1 2 3 4 5
for i in range(0, 10, 2):   # 0 2 4 6 8
for i in range(5, 0, -1):   # 5 4 3 2 1

for i, fruit in enumerate(["apple", "banana"]):    # index AND value
    print(i, fruit)
```

`for` in Python is a "for each" loop. Loop over the items directly rather than over indexes
whenever you can.

## `break`, `continue`, and `else` on loops

```python
for n in numbers:
    if n < 0:
        continue      # skip to the next item
    if n > 100:
        break         # leave the loop entirely
    print(n)
else:
    print("finished without a break")   # runs only if the loop wasn't broken out of
```

(`for ... else` is unusual. It reads as "if no break", and it's handy for searches.)

## `match` — structural pattern matching (Python 3.10+)

A powerful `switch`:

```python
match command.split():
    case ["go", direction]:
        print(f"going {direction}")
    case ["pick", "up", item]:
        print(f"picking up {item}")
    case ["quit" | "exit"]:
        print("bye")
    case _:
        print("unknown command")
```

Patterns can match literal values, sequences, alternatives (`|`), capture variables, and add
guards: `case n if n > 100:`.

## `pass`

A block can't be empty. `pass` is a do-nothing placeholder:

```python
if something:
    pass   # TODO
```

## Key takeaways

- Indentation defines blocks; `:` starts one.
- `if`/`elif`/`else`; `x if cond else y` for small choices.
- `for item in collection` is the main loop; `range()` for counting; `enumerate()` for indexes.
- `break` leaves, `continue` skips; `match` for matching shapes of data.
