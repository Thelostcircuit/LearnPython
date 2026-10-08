"""Lesson 4 — solutions."""


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def sum_to(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def first_negative_index(numbers: list[int]) -> int:
    for i, n in enumerate(numbers):
        if n < 0:
            return i
    return -1


def grade(score: int) -> str:
    if not 0 <= score <= 100:
        return "invalid"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculator(expression: str) -> float:
    match expression.split():
        case [a, "+", b]:
            return float(a) + float(b)
        case [a, "-", b]:
            return float(a) - float(b)
        case [a, "*", b]:
            return float(a) * float(b)
        case [a, "/", b]:
            return float(a) / float(b)
        case _:
            raise ValueError("bad expression")
