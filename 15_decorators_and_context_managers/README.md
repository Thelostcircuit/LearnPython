# Lesson 15 — Decorators and Context Managers

Both of these wrap code in *before/after* behaviour. Decorators wrap **functions**; context
managers wrap **blocks** (`with`).

## Step 1: functions are values (recap)

```python
def shout(s): return s.upper()
f = shout            # no parentheses: the function itself, not a call
f("hi")              # 'HI'
```

## Step 2: closures — functions that remember

A function defined inside another can use the outer function's variables, even after the outer
function has returned:

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count      # we want to MODIFY the outer variable, not make a new local
        count += 1
        return count
    return increment

c = make_counter()
c(); c(); c()        # 1, 2, 3
```

## Step 3: a decorator is a function that wraps a function

```python
import functools

def announce(func):
    @functools.wraps(func)                 # keep func's name and docstring on the wrapper
    def wrapper(*args, **kwargs):          # accept any arguments...
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)     # ...and pass them straight through
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b
```

`@announce` above `def add` is exactly the same as writing `add = announce(add)` afterwards. Now
every call to `add` goes through `wrapper`.

Common uses: timing, logging, caching, retrying, checking permissions, registering handlers
(web frameworks use `@app.get("/")`).

### Decorators with arguments

Add one more layer: a function that *returns* a decorator:

```python
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello(): print("hello")
```

### Built-in decorators you'll use

`@property`, `@classmethod`, `@staticmethod` (lesson 12), `@dataclass`, and
`@functools.cache` / `@functools.lru_cache(maxsize=...)`, which remember results of previous
calls:

```python
@functools.cache
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
fib(100)   # instant, instead of taking longer than the age of the universe
```

## Context managers — `with`

```python
with open("f.txt", encoding="utf-8") as f:
    data = f.read()
# f is closed here, guaranteed — even if an exception happened inside the block
```

A context manager runs setup code on entry, and cleanup code on exit, **no matter what**.

### Writing one with `@contextmanager`

The easiest way is a generator with a single `yield`:

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label: str):
    start = time.perf_counter()        # setup — runs on entering `with`
    try:
        yield                          # the with-block runs here
    finally:
        elapsed = time.perf_counter() - start     # cleanup — ALWAYS runs
        print(f"{label}: {elapsed:.3f}s")

with timer("sleeping"):
    time.sleep(0.1)
```

Whatever you `yield` becomes the `as` variable: `yield resource` → `with thing() as resource:`.

### As a class

The underlying protocol is two methods: `__enter__` (setup; its return value is the `as`
variable) and `__exit__(self, exc_type, exc, tb)` (cleanup; return `True` to swallow an
exception).

### Handy ones from the standard library

- `contextlib.suppress(FileNotFoundError)`: ignore specific exceptions in a block
- `tempfile.TemporaryDirectory()`: a folder that deletes itself
- `contextlib.redirect_stdout(buffer)`: capture prints

## Key takeaways

- A decorator takes a function and returns a wrapped version. `@dec` is `f = dec(f)`.
- Use `*args, **kwargs` to pass arguments through, and `functools.wraps` to keep the name/docs.
- `@functools.cache` memoises expensive pure functions.
- Context managers guarantee cleanup; write them with `@contextmanager` + `try`/`yield`/`finally`.
