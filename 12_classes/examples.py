"""Lesson 12 examples. Run with: uv run python examples.py"""

from dataclasses import dataclass, field


# --- A basic class --------------------------------------------------------------------
class Dog:
    species = "Canis familiaris"  # class attribute (shared)

    def __init__(self, name: str, age: int) -> None:
        self.name = name  # instance attributes (per dog)
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof"

    def birthday(self) -> None:
        self.age += 1

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, age={self.age})"


rex = Dog("Rex", 3)
fido = Dog("Fido", 7)
print(rex.bark())
rex.birthday()
print(f"{rex!r}, {fido!r}")
print(f"both share species: {rex.species} / {Dog.species}")
print(f"rex.bark() is Dog.bark(rex): {rex.bark() == Dog.bark(rex)}")


# --- Dunder methods -------------------------------------------------------------------
class Money:
    def __init__(self, cents: int) -> None:
        self.cents = cents

    def __repr__(self) -> str:
        return f"Money({self.cents})"

    def __str__(self) -> str:
        return f"${self.cents // 100}.{self.cents % 100:02}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and self.cents == other.cents

    def __lt__(self, other: "Money") -> bool:
        return self.cents < other.cents

    def __add__(self, other: "Money") -> "Money":
        return Money(self.cents + other.cents)


a, b = Money(1250), Money(399)
print(f"str: {a}, repr: {a!r}")
print(f"a + b = {a + b}")
print(f"a == Money(1250): {a == Money(1250)}, a < b: {a < b}")
print(f"sorted: {sorted([a, b, Money(5)])}")


class Playlist:
    def __init__(self, *songs: str) -> None:
        self._songs = list(songs)  # leading underscore: internal

    def __len__(self) -> int:
        return len(self._songs)

    def __contains__(self, song: str) -> bool:
        return song in self._songs


mix = Playlist("Intro", "Groove", "Outro")
print(f"len(mix) = {len(mix)}, 'Groove' in mix: {'Groove' in mix}")


# --- Properties -----------------------------------------------------------------------
class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5 / 9


t = Temperature(100)
print(f"{t.celsius}C = {t.fahrenheit}F")
t.fahrenheit = 32
print(f"after setting 32F: {t.celsius}C")


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = 0

    @property
    def balance(self) -> int:  # read-only: there's no setter
        return self._balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount


acct = Account("ada")
acct.deposit(50)
print(f"balance = {acct.balance}")
try:
    acct.balance = 1_000_000  # type: ignore[misc]
except AttributeError as e:
    print(f"can't set balance directly: {e}")


# --- classmethod & staticmethod -------------------------------------------------------
class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, text: str) -> "Date":
        year, month, day = (int(part) for part in text.split("-"))
        return cls(year, month, day)

    @staticmethod
    def is_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"


print(f"Date.from_string('2026-09-23') = {Date.from_string('2026-09-23')}")
print(f"Date.is_leap(2024) = {Date.is_leap(2024)}, 1900: {Date.is_leap(1900)}")


# --- dataclasses ----------------------------------------------------------------------
@dataclass
class Point:
    x: float
    y: float = 0.0
    tags: list[str] = field(default_factory=list)

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


p = Point(3, 4)
print(f"{p}, distance = {p.distance_to_origin()}")
print(f"Point(3, 4) == Point(3, 4): {Point(3, 4) == Point(3, 4)}")


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int


versions = [Version(1, 10), Version(1, 2), Version(0, 9)]
print(f"sorted versions: {sorted(versions)}")
releases = {Version(1, 0): "stable"}
print(f"frozen, so usable as a dict key: {releases}")
try:
    versions[0].major = 2  # type: ignore[misc]
except AttributeError as e:
    print(f"frozen dataclass: {type(e).__name__}")
