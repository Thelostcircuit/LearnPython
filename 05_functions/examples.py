"""Lesson 5 examples. Run with: uv run python examples.py"""


# --- Basics ---------------------------------------------------------------------------
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


print(f"add(2, 3) = {add(2, 3)}")


def say_hi() -> None:
    print("hi!")


result = say_hi()
print(f"a function with no return gives back: {result}")


# --- Returning several values ---------------------------------------------------------
def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


lo, hi = min_max([3, 1, 4, 1, 5])
print(f"min={lo}, max={hi}")


# --- Defaults and keyword arguments ---------------------------------------------------
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


print(greet("Ada"))
print(greet("Ada", "Hi"))
print(greet(greeting="Hey", name="Grace"))  # keywords can go in any order


# --- The mutable default trap, and the fix --------------------------------------------
def append_bad(item: int, items: list[int] = []) -> list[int]:  # noqa: B006 (on purpose!)
    items.append(item)
    return items


def append_good(item: int, items: list[int] | None = None) -> list[int]:
    if items is None:
        items = []
    items.append(item)
    return items


print(f"bad:  {append_bad(1)} then {append_bad(2)}   <- the same list, shared!")
print(f"good: {append_good(1)} then {append_good(2)}")


# --- Keyword-only arguments -----------------------------------------------------------
def connect(host: str, port: int = 22, *, timeout: float = 5.0) -> str:
    return f"connecting to {host}:{port} (timeout {timeout}s)"


print(connect("example.com", 2222, timeout=1.0))
# print(connect("example.com", 2222, 1.0))  # <- uncomment: TypeError


# --- *args and **kwargs ---------------------------------------------------------------
def total(*numbers: int) -> int:
    print(f"  numbers is a {type(numbers).__name__}: {numbers}")
    return sum(numbers)


print(f"total(1, 2, 3) = {total(1, 2, 3)}")
nums = [4, 5, 6]
print(f"total(*nums) = {total(*nums)}")


def tag(name: str, **attrs: str) -> str:
    extras = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f"<{name} {extras}>"


print(tag("a", href="/", title="home"))
options = {"src": "cat.png", "alt": "a cat"}
print(tag("img", **options))

# --- Scope ----------------------------------------------------------------------------
counter = 0


def local_only() -> None:
    counter = 100  # a NEW local variable; the global one is untouched
    print(f"  inside: counter = {counter}")


local_only()
print(f"outside: counter = {counter}")


# --- Functions are values -------------------------------------------------------------
def shout(s: str) -> str:
    return s.upper() + "!"


def whisper(s: str) -> str:
    return s.lower() + "..."


for style in [shout, whisper]:
    print(f"{style.__name__}: {style('Hello')}")


def apply_twice(f, x):
    return f(f(x))


print(f"apply_twice(shout, 'hey') = {apply_twice(shout, 'hey')}")

words = ["banana", "Apple", "cherry"]
print(f"sorted: {sorted(words)}")
print(f"sorted, ignoring case: {sorted(words, key=str.lower)}")
print(f"sorted by length: {sorted(words, key=len)}")

people = [{"name": "Ada", "age": 36}, {"name": "Grace", "age": 85}, {"name": "Linus", "age": 21}]
youngest_first = sorted(people, key=lambda p: p["age"])
print(f"youngest first: {[p['name'] for p in youngest_first]}")

# --- Docstrings -----------------------------------------------------------------------
print(f"add's docstring: {add.__doc__!r}")
