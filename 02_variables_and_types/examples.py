"""Lesson 2 examples. Run with: uv run python examples.py"""

import math

# --- Variables are names --------------------------------------------------------------
x = 5
print(f"x = {x!r}, type = {type(x).__name__}")
x = "now a string"
print(f"x = {x!r}, type = {type(x).__name__}")

a, b = 1, 2
a, b = b, a  # swap
print(f"swapped: a={a}, b={b}")

MAX_USERS = 100  # a "constant" by convention
print(f"MAX_USERS = {MAX_USERS}")

# --- int: unlimited size --------------------------------------------------------------
big = 2**100
print(f"2 ** 100 = {big}")
print(f"1_000_000 = {1_000_000}, 0xff = {0xFF}, 0b1010 = {0b1010}")

# --- float ----------------------------------------------------------------------------
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # floating point is approximate!
print(f"math.isclose(0.1 + 0.2, 0.3) = {math.isclose(0.1 + 0.2, 0.3)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# --- Arithmetic -----------------------------------------------------------------------
print(f"7 / 2 = {7 / 2}")
print(f"7 // 2 = {7 // 2}")
print(f"7 % 2 = {7 % 2}")
print(f"7 ** 2 = {7**2}")
print(f"-7 // 2 = {-7 // 2}  (floors toward -infinity)")
print(f"divmod(17, 5) = {divmod(17, 5)}")
print(f"abs(-3) = {abs(-3)}, min(4, 2, 8) = {min(4, 2, 8)}, max(4, 2, 8) = {max(4, 2, 8)}")
print(f"math.sqrt(2) = {math.sqrt(2):.4f}, math.pi = {math.pi:.4f}")

count = 10
count += 5
count *= 2
print(f"count = {count}")

# --- Conversion -----------------------------------------------------------------------
print(f'int("42") + 1 = {int("42") + 1}')
print(f"int(3.99) = {int(3.99)}")
print(f'float("2.5") = {float("2.5")}')
print(f"str(42) + '!' = {str(42) + '!'}")
# print("3" + 4)  # <- uncomment: TypeError: can only concatenate str (not "int") to str

# --- bool & truthiness ----------------------------------------------------------------
for value in [0, 1, -1, 0.0, "", "hi", None, [], [0]]:
    print(f"bool({value!r:>6}) = {bool(value)}")

# --- Comparisons & logic --------------------------------------------------------------
n = 5
print(f"0 < n < 10: {0 < n < 10}")
print(f"n > 3 and n % 2 == 0: {n > 3 and n % 2 == 0}")
is_big = n > 100
print(f"not is_big: {not is_big}")

# --- None and `is` --------------------------------------------------------------------
result = None
print(f"result is None: {result is None}")

# --- isinstance -----------------------------------------------------------------------
print(f"isinstance(3, int) = {isinstance(3, int)}")
print(f"isinstance(3.0, (int, float)) = {isinstance(3.0, (int, float))}")
print(f"isinstance(True, int) = {isinstance(True, int)}  (bool is a kind of int!)")
