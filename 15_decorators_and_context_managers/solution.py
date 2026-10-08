"""Lesson 15 — solutions."""

import functools
from contextlib import contextmanager


def make_accumulator():
    total = 0

    def add(amount):
        nonlocal total
        total += amount
        return total

    return add


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def uppercase_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def retry(times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise  # out of attempts: re-raise the last error

        return wrapper

    return decorator


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg <= 0 for arg in args):
            raise ValueError("arguments must be positive")
        return func(*args, **kwargs)

    return wrapper


@contextmanager
def collecting():
    items: list = []
    try:
        yield items
    finally:
        print(f"collected {len(items)} items")


@contextmanager
def temporarily(obj, attr: str, value):
    old = getattr(obj, attr)
    setattr(obj, attr, value)
    try:
        yield
    finally:
        setattr(obj, attr, old)
