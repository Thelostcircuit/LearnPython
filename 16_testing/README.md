# Lesson 16 — Testing with pytest

You've been *running* tests all course. Now you'll write them.

## A test is a function that asserts

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 2) == 4
```

pytest finds files named `test_*.py` (this course also collects `exercises.py`), runs every
function starting with `test_`, and reports which ones raised. A plain `assert` is all you need.
When it fails, pytest shows you both sides of the comparison.

## Organising: Arrange, Act, Assert

```python
def test_withdraw_reduces_balance():
    account = Account(100)        # Arrange — set up
    account.withdraw(30)          # Act — do the thing
    assert account.balance == 70  # Assert — check the result
```

Name tests after the **behaviour** they check. When `test_withdraw_more_than_balance_raises`
fails, you know what broke without reading it.

## Testing exceptions

```python
import pytest

def test_withdraw_too_much():
    with pytest.raises(ValueError, match="insufficient"):
        Account(10).withdraw(50)
```

## Floats

`0.1 + 0.2 == 0.3` is `False`. Use `pytest.approx`:

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

## `@pytest.mark.parametrize` — one test, many cases

```python
@pytest.mark.parametrize(("text", "expected"), [
    ("racecar", True),
    ("hello", False),
    ("", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
```

Each row runs, and is reported, as its own test.

## Fixtures — reusable setup

A fixture is a function whose return value pytest passes to any test that names it as a
parameter:

```python
@pytest.fixture
def account():
    return Account(100)

def test_deposit(account):          # pytest calls account() and passes the result in
    account.deposit(50)
    assert account.balance == 150
```

Each test gets a **fresh** fixture value. Fixtures can `yield` instead of `return` to run cleanup
afterwards. Put shared fixtures in a `conftest.py` file and every test in that folder can use them.

### Built-in fixtures worth knowing

| Fixture | Gives you |
| --- | --- |
| `tmp_path` | a fresh temporary folder (a `Path`) |
| `capsys` | captured `print` output: `capsys.readouterr().out` |
| `monkeypatch` | temporarily replace attributes, env vars, dict items: undone after the test |

## Running tests

```sh
uv run pytest                   # everything in this folder
uv run pytest -v                # list each test
uv run pytest -k withdraw       # only tests with "withdraw" in the name
uv run pytest -x                # stop at first failure
uv run pytest --lf              # re-run only the tests that failed last time
uv run pytest -s                # show print() output
```

## What to test

- The **normal case**, then the **edges**: empty input, zero, one item, negative numbers,
  maximums, duplicates, invalid input.
- One behaviour per test.
- When you find a bug: **write a test that fails because of it first**, then fix the code. The test
  keeps the bug from coming back.

## Your exercise

`pricing.py` contains finished code. **Your job is to write the tests** in `exercises.py`. One
function has a **bug**. Your tests should find it! Then fix the bug in `pricing.py`.

Run `uv run python examples.py` for a guided tour of `test_examples.py`, which shows every feature
above in action.

## Key takeaways

- Tests are `test_*` functions with plain `assert`s.
- `pytest.raises`, `pytest.approx`, `@pytest.mark.parametrize`, fixtures (`tmp_path`, `capsys`,
  `monkeypatch`).
- Test edges, one behaviour per test, and write the failing test before fixing a bug.
