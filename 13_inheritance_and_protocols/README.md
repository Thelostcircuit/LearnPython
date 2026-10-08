# Lesson 13 — Inheritance, Abstract Classes, and Protocols

## Inheritance

A class can **inherit** from another, getting all its attributes and methods, then add or
change ("override") some:

```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def introduce(self) -> str:
        return f"I'm {self.name} and I say {self.speak()}"

class Dog(Animal):                 # Dog IS-AN Animal
    def speak(self) -> str:        # override
        return "woof"

Dog("Rex").introduce()             # "I'm Rex and I say woof" — introduce() calls Dog's speak()
isinstance(Dog("Rex"), Animal)     # True
```

## `super()` — call the parent's version

```python
class ServiceDog(Dog):
    def __init__(self, name: str, job: str) -> None:
        super().__init__(name)     # let Animal set up `name`
        self.job = job

    def introduce(self) -> str:
        return super().introduce() + f", and I work as a {self.job}"
```

## Abstract base classes — "subclasses MUST implement this"

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    def describe(self) -> str:             # regular methods can use the abstract ones
        return f"{type(self).__name__} with area {self.area():.2f}"

Shape()           # ❌ TypeError: can't instantiate abstract class
class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side
    def area(self) -> float:
        return self.side ** 2
```

## Duck typing — "if it quacks like a duck..."

Python mostly doesn't care about an object's class, only whether it has the methods you call:

```python
def total_area(shapes) -> float:
    return sum(s.area() for s in shapes)   # works for ANYTHING with an .area() method
```

That's why `len()` works on lists, strings, dicts, and your own classes with `__len__`. They don't
share a parent class, just a method.

## Protocols — duck typing your editor can check

`typing.Protocol` describes "anything with these methods", **without** requiring inheritance:

```python
from typing import Protocol

class HasArea(Protocol):
    def area(self) -> float: ...

def total_area(shapes: list[HasArea]) -> float:
    return sum(s.area() for s in shapes)
```

Any class with a matching `area()` fits `HasArea` automatically. basedpyright checks it for you.
Protocols are often a better fit than inheritance for "things that can do X".

## Composition over inheritance

Inheritance means "IS-A". For "HAS-A", store an object as an attribute instead:

```python
class Car:
    def __init__(self) -> None:
        self.engine = Engine()     # a Car HAS an Engine; it isn't one
```

Deep inheritance trees get hard to follow. Prefer shallow hierarchies, composition, and protocols.
Reach for inheritance when there is a genuine "is a kind of" relationship and shared behaviour.

## Key takeaways

- `class Child(Parent):` inherits; override methods by redefining them; `super()` calls the parent.
- `ABC` + `@abstractmethod` force subclasses to implement methods.
- Duck typing: what matters is what an object can *do*. `Protocol` makes that checkable.
- Prefer composition ("has a") unless it's truly "is a".
