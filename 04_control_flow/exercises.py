"""Lesson 4 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""


def fizzbuzz(n: int) -> str:
    """ "Fizz" if divisible by 3, "Buzz" if by 5, "FizzBuzz" if both, else the number as a str."""
    raise NotImplementedError


def sum_to(n: int) -> int:
    """Sum 1 + 2 + ... + n using a for loop and range.  sum_to(4) == 10"""
    raise NotImplementedError


def factorial(n: int) -> int:
    """n! = n * (n-1) * ... * 1, and 0! == 1."""
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """True if n is prime. 0 and 1 are not prime."""
    raise NotImplementedError


def collatz_steps(n: int) -> int:
    """Steps to reach 1: if even, n //= 2; if odd, n = 3n + 1.  collatz_steps(6) == 8

    Use a while loop.
    """
    raise NotImplementedError


def fib(n: int) -> int:
    """The nth Fibonacci number: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2). Use a loop.

    Hint: a, b = b, a + b
    """
    raise NotImplementedError


def first_negative_index(numbers: list[int]) -> int:
    """Index of the first negative number, or -1 if there isn't one. Use enumerate + return."""
    raise NotImplementedError


def grade(score: int) -> str:
    """90+ -> "A", 80+ -> "B", 70+ -> "C", 60+ -> "D", below -> "F".
    Anything outside 0-100 -> "invalid"."""
    raise NotImplementedError


def calculator(expression: str) -> float:
    """Evaluate "<number> <op> <number>" where op is + - * /.  "3 * 4" -> 12.0

    Use `match` on expression.split(). Raise ValueError("bad expression") for anything else.
    Hint:  case [a, "+", b]:  return float(a) + float(b)
    """
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_fizzbuzz():
    assert [fizzbuzz(n) for n in [1, 3, 5, 15, 16]] == ["1", "Fizz", "Buzz", "FizzBuzz", "16"]


def test_sum_to():
    assert sum_to(0) == 0
    assert sum_to(4) == 10
    assert sum_to(100) == 5050


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(20) == 2432902008176640000


def test_is_prime():
    assert [n for n in range(30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_collatz_steps():
    assert collatz_steps(1) == 0
    assert collatz_steps(6) == 8
    assert collatz_steps(27) == 111


def test_fib():
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib(100) == 354224848179261915075


def test_first_negative_index():
    assert first_negative_index([3, 1, -2, -5]) == 2
    assert first_negative_index([1, 2]) == -1


def test_grade():
    assert [grade(s) for s in [95, 85, 75, 65, 10]] == ["A", "B", "C", "D", "F"]
    assert grade(101) == "invalid"
    assert grade(-1) == "invalid"


def test_calculator():
    assert calculator("3 * 4") == 12
    assert calculator("10 / 4") == 2.5
    assert calculator("1.5 + 1") == 2.5
    assert calculator("7 - 10") == -3
    with pytest.raises(ValueError):
        calculator("3 ^ 4")
