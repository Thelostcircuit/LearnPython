"""Lesson 15 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`."""

# ruff: noqa: F401 — some imports are only used once you've written your code

import functools
from contextlib import contextmanager


def make_accumulator():
    """Return a function that adds its argument to a running total and returns the total.

    acc = make_accumulator(); acc(5) -> 5; acc(3) -> 8
    Hint: a closure with `nonlocal`.
    """
    raise NotImplementedError


def count_calls(func):
    """Decorator: count how many times the function is called, in `wrapper.calls`.

    Use functools.wraps. Set wrapper.calls = 0 before returning the wrapper, and add 1 per call.
    """
    raise NotImplementedError


def uppercase_result(func):
    """Decorator: call the function, then return its (string) result uppercased."""
    raise NotImplementedError


def retry(times: int):
    """Decorator WITH AN ARGUMENT: call the function; if it raises an exception, try again,
    up to `times` attempts in total. If the last attempt also fails, let the exception out."""
    raise NotImplementedError


def validate_positive(func):
    """Decorator: raise ValueError("arguments must be positive") if any positional argument
    is <= 0; otherwise call the function normally."""
    raise NotImplementedError


@contextmanager
def collecting():
    """Context manager: `with collecting() as items:` gives an empty list. When the block
    ends, print "collected N items". Must print even if the block raises."""
    raise NotImplementedError
    yield  # (keeps this a generator function until you write your own yield)


@contextmanager
def temporarily(obj, attr: str, value):
    """Set obj.<attr> to value for the duration of the block, then restore the old value —
    even if an exception happens. Hint: getattr / setattr, and try/finally."""
    raise NotImplementedError
    yield


# ---- Tests (you don't need to change anything below) ---------------------------------

import pytest  # noqa: E402 — imports usually go at the top; tests are kept out of your way


def test_make_accumulator():
    acc = make_accumulator()
    assert acc(5) == 5
    assert acc(3) == 8
    other = make_accumulator()
    assert other(1) == 1


def test_count_calls():
    @count_calls
    def hello(name):
        """Say hi."""
        return f"hi {name}"

    assert hello("a") == "hi a"
    hello("b")
    assert hello.calls == 2
    assert hello.__name__ == "hello"
    assert hello.__doc__ == "Say hi."


def test_uppercase_result():
    @uppercase_result
    def greet(name, punctuation="!"):
        return f"hello {name}{punctuation}"

    assert greet("ada") == "HELLO ADA!"
    assert greet("ada", punctuation="?") == "HELLO ADA?"


def test_retry():
    attempts = []

    @retry(times=3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ConnectionError("try again")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 3

    @retry(times=2)
    def always_fails():
        raise ConnectionError("nope")

    with pytest.raises(ConnectionError):
        always_fails()


def test_validate_positive():
    @validate_positive
    def area(w, h):
        return w * h

    assert area(2, 3) == 6
    with pytest.raises(ValueError, match="positive"):
        area(2, -1)


def test_collecting(capsys):
    with collecting() as items:
        items.append("a")
        items.append("b")
    assert items == ["a", "b"]
    assert "collected 2 items" in capsys.readouterr().out

    with pytest.raises(RuntimeError), collecting() as items:
        items.append("x")
        raise RuntimeError
    assert "collected 1 items" in capsys.readouterr().out


def test_temporarily():
    class Config:
        debug = False

    cfg = Config()
    with temporarily(cfg, "debug", True):
        assert cfg.debug is True
    assert cfg.debug is False

    with pytest.raises(KeyError), temporarily(cfg, "debug", True):
        raise KeyError
    assert cfg.debug is False
