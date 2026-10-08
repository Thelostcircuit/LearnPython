"""Examples of pytest features. Run: uv run pytest test_examples.py -v"""

import json
import os

import pytest


# Code under test (normally this would live in its own module and be imported) --------
class Account:
    def __init__(self, balance: float = 0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def greet(name: str) -> None:
    print(f"Hello, {name}!")


# Plain asserts -----------------------------------------------------------------------
def test_withdraw_reduces_balance():
    account = Account(100)  # Arrange
    account.withdraw(30)  # Act
    assert account.balance == 70  # Assert


# Exceptions --------------------------------------------------------------------------
def test_withdraw_more_than_balance_raises():
    with pytest.raises(ValueError, match="insufficient"):
        Account(10).withdraw(50)


# Floats ------------------------------------------------------------------------------
def test_float_arithmetic_needs_approx():
    assert 0.1 + 0.2 != 0.3
    assert 0.1 + 0.2 == pytest.approx(0.3)  # noqa: SIM300 — reads naturally this way


# Parametrize -------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome_parametrize(text, expected):
    assert is_palindrome(text) == expected


# Fixtures ----------------------------------------------------------------------------
@pytest.fixture
def account():
    """A fresh Account with 100 in it, for every test that asks for `account`."""
    return Account(100)


def test_deposit_with_fixture(account):
    account.deposit(50)
    assert account.balance == 150


def test_fixture_is_fresh_each_time(account):
    assert account.balance == 100  # unaffected by the previous test's deposit


@pytest.fixture
def sample_file(tmp_path):
    """Fixtures can use other fixtures, and yield to run cleanup afterwards."""
    path = tmp_path / "data.json"
    path.write_text(json.dumps({"users": ["ada", "grace"]}), encoding="utf-8")
    yield path
    # anything here runs after the test (tmp_path cleans itself up anyway)


def test_reads_json_with_tmp_path(sample_file):
    data = json.loads(sample_file.read_text(encoding="utf-8"))
    assert data["users"] == ["ada", "grace"]


# capsys: capture printed output ------------------------------------------------------
def test_greet_prints(capsys):
    greet("Ada")
    assert capsys.readouterr().out == "Hello, Ada!\n"


# monkeypatch: temporarily replace things ---------------------------------------------
def app_mode() -> str:
    return os.environ.get("APP_MODE", "production")


def test_monkeypatch_env(monkeypatch):
    monkeypatch.setenv("APP_MODE", "testing")  # undone automatically after this test
    assert app_mode() == "testing"


def test_monkeypatch_replaces_a_function(monkeypatch):
    monkeypatch.setattr(json, "dumps", lambda obj: "<fake json>")
    assert json.dumps({"a": 1}) == "<fake json>"


# Marks -------------------------------------------------------------------------------
@pytest.mark.skip(reason="demonstrates skipping")
def test_skipped():
    raise AssertionError("never runs")


@pytest.mark.xfail(reason="known bug: demonstrates an expected failure")
def test_expected_failure():
    assert Account(0).balance == 1
