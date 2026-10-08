# Lesson 9 — Exceptions

When something goes wrong, Python **raises an exception**. If nothing catches it, the program
stops and prints a **traceback**:

```
Traceback (most recent call last):
  File "example.py", line 3, in <module>
    total = int(user_input) + 1
            ^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'abc'
```

Read it **bottom-up**: the last line is *what* happened (`ValueError` plus a message), and the
lines above are *where*, most recent call last.

## Common built-in exceptions

| Exception | Typical cause |
| --- | --- |
| `ValueError` | Right type, bad value: `int("abc")` |
| `TypeError` | Wrong type: `"a" + 1` |
| `KeyError` | Missing dict key |
| `IndexError` | List index out of range |
| `AttributeError` | `None.upper()`: the object doesn't have that attribute |
| `ZeroDivisionError` | `1 / 0` |
| `FileNotFoundError` | Opening a file that isn't there |
| `NameError` | Using a variable that doesn't exist (often a typo) |

## Catching exceptions: `try` / `except`

```python
try:
    age = int(text)
except ValueError:
    print("that's not a number")
    age = 0
```

The full form:

```python
try:
    f = open(path)
except FileNotFoundError as e:       # `as e` gives you the exception object
    print(f"missing: {e}")
except (PermissionError, IsADirectoryError):   # several types at once
    print("can't read it")
else:
    print("runs only if NO exception happened")
finally:
    print("ALWAYS runs — cleanup goes here")
```

Guidelines:

- **Catch specific exceptions.** A bare `except:` or `except Exception:` also hides your typos and
  bugs.
- Keep the `try` block small: just the line that can fail.
- Don't catch an exception if you can't do anything sensible about it. Let it propagate to a place
  that can.

## "Easier to ask forgiveness than permission"

Python style often *tries* the operation and handles failure (EAFP), rather than checking
everything first (LBYL, "look before you leap"):

```python
# LBYL                                  # EAFP — often cleaner and avoids race conditions
if key in d:                            try:
    value = d[key]                          value = d[key]
else:                                   except KeyError:
    value = default                         value = default
```

(For this exact case, `d.get(key, default)` is best. Use whichever reads most clearly.)

## Raising exceptions

```python
def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return balance - amount
```

Inside an `except` block, a bare `raise` re-raises the current exception (e.g. after logging it).

## Custom exceptions

Subclass `Exception` (classes are lesson 12, but this part is simple):

```python
class InsufficientFunds(Exception):
    """Raised when a withdrawal is bigger than the balance."""

raise InsufficientFunds("balance is 10, tried to withdraw 50")
```

Custom exceptions let callers catch *your* specific problem without catching everything else.
Callers can also catch a parent class: `except Exception` would catch `InsufficientFunds`.

**Chaining**: `raise ConfigError("bad port") from err` keeps the original error in the traceback.

## Key takeaways

- Read tracebacks bottom-up.
- `try`/`except SpecificError` to handle; `else` for success-only code; `finally` for cleanup.
- `raise ValueError("clear message")` when your function gets bad input.
- Define custom exception classes for errors your callers might want to handle specifically.
