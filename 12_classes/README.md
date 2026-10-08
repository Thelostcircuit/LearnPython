# Lesson 12 — Classes

A **class** bundles data (attributes) with the functions that work on it (methods). It's a
blueprint; each **instance** made from it has its own data.

## Defining a class

```python
class Dog:
    species = "Canis familiaris"            # class attribute — shared by all dogs

    def __init__(self, name: str, age: int) -> None:
        self.name = name                     # instance attributes — each dog has its own
        self.age = age

    def bark(self) -> str:                   # a method
        return f"{self.name} says woof"

rex = Dog("Rex", 3)       # calls __init__
rex.bark()                # 'Rex says woof'
rex.age += 1              # attributes are just values you can read and change
```

- `__init__` sets up a new instance. It's the constructor.
- **`self`** is the instance the method was called on. `rex.bark()` is really `Dog.bark(rex)`.
  Every regular method takes `self` first.
- Class names are `CamelCase`.

## Dunder ("double underscore") methods

Special method names let your objects work with Python's built-in syntax:

| Method | Enables |
| --- | --- |
| `__repr__` | how it looks in the REPL / debugging: `Dog(name='Rex', age=3)` |
| `__str__` | `str(obj)` and `print(obj)` (falls back to `__repr__`) |
| `__eq__` | `a == b` (default: only equal to itself) |
| `__lt__` etc. | `<`, which also makes `sorted()` work |
| `__len__` | `len(obj)` |
| `__contains__` | `x in obj` |
| `__add__` | `a + b` |
| `__iter__` | `for x in obj` (lesson 14) |

Always write a `__repr__`. It makes debugging much easier.

## Properties — attributes with logic

```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:          # read like an attribute: t.fahrenheit
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:   # t.fahrenheit = 212
        self.celsius = (value - 32) * 5 / 9
```

Properties let you start with a plain attribute and add validation or calculation later, without
changing the code that uses it.

## Class methods and static methods

```python
class Date:
    def __init__(self, year: int, month: int, day: int) -> None: ...

    @classmethod
    def from_string(cls, text: str) -> "Date":     # an alternative constructor
        y, m, d = map(int, text.split("-"))
        return cls(y, m, d)

    @staticmethod
    def is_leap(year: int) -> bool:                # just a function that lives in the class
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

## Privacy by convention

Python has no `private`. A single leading underscore (`self._balance`) means "internal, please
don't touch from outside". Expose what callers should use via methods or properties.

## `@dataclass` — skip the boilerplate

For classes that are mostly data, the `dataclasses` module writes `__init__`, `__repr__`, and
`__eq__` for you:

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float = 0.0                          # default
    tags: list[str] = field(default_factory=list)   # mutable default, done safely

p = Point(1, 2)          # Point(x=1, y=2, tags=[])
p == Point(1, 2)         # True
```

Options: `@dataclass(frozen=True)` makes instances immutable (and hashable, so usable as dict
keys); `@dataclass(order=True)` adds `<` so they sort.

**Rule of thumb:** reach for `@dataclass` first. Write a plain class when you need more control.

## Key takeaways

- `class Name:` with `__init__(self, ...)` to set attributes; methods take `self`.
- Dunder methods (`__repr__`, `__eq__`, `__len__`, ...) plug into Python syntax.
- `@property` for computed/validated attributes; `@classmethod` for alternative constructors.
- `@dataclass` generates the boilerplate for data-holding classes.
