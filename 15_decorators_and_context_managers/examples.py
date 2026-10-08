"""Lesson 15 examples. Run with: uv run python examples.py"""

import functools
import io
import time
from contextlib import contextmanager, redirect_stdout, suppress
from pathlib import Path


# --- Closures -------------------------------------------------------------------------
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = make_counter()
print(f"counter: {c()}, {c()}, {c()}")
other = make_counter()
print(f"a separate counter starts fresh: {other()}")


# --- A simple decorator ---------------------------------------------------------------
def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  -> calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"  <- {func.__name__} returned {result!r}")
        return result

    return wrapper


@announce
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


add(2, 3)
print(f"wraps kept the name and docstring: {add.__name__!r}, {add.__doc__!r}")


# --- A timing decorator ---------------------------------------------------------------
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"  {func.__name__} took {time.perf_counter() - start:.4f}s")

    return wrapper


@timed
def slow_sum(n: int) -> int:
    return sum(range(n))


print(f"slow_sum = {slow_sum(2_000_000):,}")


# --- A decorator with arguments -------------------------------------------------------
def repeat(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def cheer() -> None:
    print("  hip hip hooray!")


cheer()


# --- functools.cache ------------------------------------------------------------------
@functools.cache
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


start = time.perf_counter()
print(f"fib(200) = {fib(200)}  in {time.perf_counter() - start:.4f}s thanks to caching")


# --- A registry decorator (how web frameworks map routes) -----------------------------
handlers = {}


def command(name: str):
    def decorator(func):
        handlers[name] = func
        return func  # return the original, unwrapped

    return decorator


@command("greet")
def greet_cmd() -> str:
    return "hello!"


@command("bye")
def bye_cmd() -> str:
    return "see you!"


for name in ["greet", "bye"]:
    print(f"handlers[{name!r}]() -> {handlers[name]()}")


# --- Context managers with @contextmanager --------------------------------------------
@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"  {label}: {time.perf_counter() - start:.3f}s")


with timer("sleeping"):
    time.sleep(0.05)


@contextmanager
def indented_log(title: str):
    print(f"begin {title}")
    lines: list[str] = []
    try:
        yield lines  # becomes the `as` variable
    finally:
        for line in lines:
            print(f"    {line}")
        print(f"end {title}")


with indented_log("shopping") as log:
    log.append("milk")
    log.append("bread")

# cleanup runs even when the block raises:
try:
    with indented_log("risky") as log:
        log.append("about to fail")
        raise RuntimeError("boom")
except RuntimeError as e:
    print(f"caught {e!r} after cleanup")


# --- A class-based context manager ----------------------------------------------------
class Overrides:
    """Temporarily override some settings, then put the old values back."""

    def __init__(self, settings: dict, **overrides) -> None:
        self.settings = settings
        self.overrides = overrides
        self.saved: dict = {}

    def __enter__(self) -> dict:
        self.saved = dict(self.settings)
        self.settings.update(self.overrides)
        return self.settings

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.settings.clear()
        self.settings.update(self.saved)
        return False  # don't swallow exceptions


settings = {"debug": False, "level": 1}
with Overrides(settings, debug=True) as s:
    print(f"inside: {s}")
print(f"after: {settings}")

# --- Standard library helpers ---------------------------------------------------------
with suppress(FileNotFoundError):
    Path("definitely-not-here.txt").read_text()
print("suppress() swallowed the FileNotFoundError")

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("this goes into the buffer, not the terminal")
print(f"captured: {buffer.getvalue()!r}")
