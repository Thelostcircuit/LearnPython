"""Lesson 9 examples. Run with: uv run python examples.py"""


# --- Catching a specific exception ----------------------------------------------------
def to_int(text: str) -> int:
    try:
        return int(text)
    except ValueError:
        print(f"  {text!r} is not a number, using 0")
        return 0


print(f"to_int('42') = {to_int('42')}")
print(f"to_int('abc') = {to_int('abc')}")

# --- The exception object, several except clauses, else, finally ----------------------
for value in ["10", "0", "ten"]:
    print(f"100 / {value!r}:")
    try:
        result = 100 / int(value)
    except ZeroDivisionError:
        print("  can't divide by zero")
    except ValueError as e:
        print(f"  bad input: {e}")
    else:
        print(f"  = {result}")
    finally:
        print("  (finally always runs)")

# --- Catching several types at once ---------------------------------------------------
data = {"a": [1, 2, 3]}
for key, index in [("a", 1), ("b", 0), ("a", 10)]:
    try:
        print(f"data[{key!r}][{index}] = {data[key][index]}")
    except (KeyError, IndexError) as e:
        print(f"data[{key!r}][{index}] failed with {type(e).__name__}: {e}")

# --- EAFP vs LBYL ---------------------------------------------------------------------
settings = {"theme": "dark"}
try:
    font = settings["font"]
except KeyError:
    font = "monospace"
print(f"font (EAFP) = {font}")
print(f"font (.get) = {settings.get('font', 'monospace')}")


# --- Raising --------------------------------------------------------------------------
def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return balance - amount


try:
    withdraw(100, -5)
except ValueError as e:
    print(f"withdraw refused: {e}")


# --- Custom exceptions ----------------------------------------------------------------
class BankError(Exception):
    """Base class for everything that can go wrong in our bank."""


class InsufficientFunds(BankError):
    def __init__(self, balance: float, amount: float):
        super().__init__(f"balance is {balance}, tried to withdraw {amount}")
        self.shortfall = amount - balance


def safe_withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFunds(balance, amount)
    return balance - amount


try:
    safe_withdraw(10, 50)
except InsufficientFunds as e:
    print(f"InsufficientFunds: {e} (short by {e.shortfall})")

try:
    safe_withdraw(10, 50)
except BankError as e:  # catching the parent class also works
    print(f"caught as BankError: {type(e).__name__}")


# --- Re-raising and chaining ----------------------------------------------------------
class ConfigError(Exception):
    pass


def read_port(text: str) -> int:
    try:
        return int(text)
    except ValueError as err:
        raise ConfigError(f"port must be a number, not {text!r}") from err


try:
    read_port("eighty")
except ConfigError as e:
    print(f"ConfigError: {e}  (caused by {type(e.__cause__).__name__})")

# --- An uncaught exception ------------------------------------------------------------
# Uncomment to see a full traceback and read it bottom-up:
# read_port("eighty")
