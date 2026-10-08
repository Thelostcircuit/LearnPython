"""Lesson 13 examples. Run with: uv run python examples.py"""

import math
from abc import ABC, abstractmethod
from typing import Protocol


# --- Inheritance & overriding ---------------------------------------------------------
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."

    def introduce(self) -> str:
        return f"I'm {self.name} and I say {self.speak()}"


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


for pet in [Animal("Generic"), Dog("Rex"), Cat("Tom")]:
    print(pet.introduce())

print(f"isinstance(Dog('x'), Animal): {isinstance(Dog('x'), Animal)}")
print(f"issubclass(Cat, Dog): {issubclass(Cat, Dog)}")
print(f"Dog's method resolution order: {[c.__name__ for c in Dog.__mro__]}")


# --- super() --------------------------------------------------------------------------
class ServiceDog(Dog):
    def __init__(self, name: str, job: str) -> None:
        super().__init__(name)
        self.job = job

    def introduce(self) -> str:
        return super().introduce() + f", and I work as a {self.job}"


print(ServiceDog("Buddy", "guide dog").introduce())


# --- Abstract base class --------------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    def describe(self) -> str:
        return f"{type(self).__name__} with area {self.area():.2f}"


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


for shape in [Square(2), Circle(1)]:
    print(shape.describe())

try:
    Shape()  # type: ignore[abstract]
except TypeError as e:
    print(f"Shape() fails: {e}")


# --- Duck typing ----------------------------------------------------------------------
class Rug:  # NOT a Shape subclass, but it has .area()
    def area(self) -> float:
        return 6.0


def total_area_duck(things) -> float:
    return sum(t.area() for t in things)


print(f"duck-typed total: {total_area_duck([Square(2), Rug()]):.2f}")


# --- Protocol -------------------------------------------------------------------------
class HasArea(Protocol):
    def area(self) -> float: ...


def total_area(things: list[HasArea]) -> float:
    return sum(t.area() for t in things)


print(f"protocol-typed total: {total_area([Square(1), Circle(1), Rug()]):.2f}")


# --- Composition ----------------------------------------------------------------------
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"vroom ({self.horsepower} hp)"


class Car:
    def __init__(self, model: str, engine: Engine) -> None:
        self.model = model
        self.engine = engine  # a Car HAS an Engine

    def drive(self) -> str:
        return f"{self.model}: {self.engine.start()}"


print(Car("Roadster", Engine(300)).drive())


# --- Custom exceptions use inheritance too --------------------------------------------
class AppError(Exception):
    pass


class NotFound(AppError):
    pass


try:
    raise NotFound("no such user")
except AppError as e:
    print(f"caught {type(e).__name__} via its parent AppError: {e}")
