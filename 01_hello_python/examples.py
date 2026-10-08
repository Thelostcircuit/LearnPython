"""Lesson 1 examples. Run with: uv run python examples.py"""

# The classic.
print("Hello, world!")

# --- print ----------------------------------------------------------------------------
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("no newline here... ", end="")
print("so this continues the same line.")
print()  # blank line

# --- f-strings ------------------------------------------------------------------------
name = "Ada"
age = 36
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")
print(f"{name=}, {age=}")  # debugging shorthand: shows the name AND value

# --- format specs ---------------------------------------------------------------------
pi = 3.14159265
print(f"pi to 2 places: {pi:.2f}")
print(f"right  [{42:>6}]")
print(f"left   [{42:<6}]")
print(f"centre [{42:^6}]")
print(f"zeros  [{42:06}]")
print(f"big number: {1234567:,}")
print(f"percent: {0.256:.1%}")
print(f"hex {255:x}, binary {5:b}")

# To print a literal brace in an f-string, double it.
print(f"Braces look like {{this}}, and the value is {age}")

# --- quotes ---------------------------------------------------------------------------
# (`fmt: skip` stops `ruff format` from switching these to double quotes)
print('single quotes')  # fmt: skip
print("double quotes")
print("it's easy to put one kind inside the other")
print("""triple quotes
span multiple lines""")

# --- building a string without printing it --------------------------------------------
message = f"{name} says hi"
print(message)


# --- docstrings -----------------------------------------------------------------------
def greet():
    """Say hello. This text is the function's docstring."""
    print("hello from greet()")


greet()
print(greet.__doc__)

# --- input ----------------------------------------------------------------------------
# Uncomment to try it (the program will wait for you to type):
# your_name = input("What's your name? ")
# print(f"Nice to meet you, {your_name}!")
