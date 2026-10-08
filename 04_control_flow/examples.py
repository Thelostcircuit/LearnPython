"""Lesson 4 examples. Run with: uv run python examples.py"""

# --- if / elif / else -----------------------------------------------------------------
for n in [-5, 0, 5]:
    if n < 0:
        print(f"{n} is negative")
    elif n == 0:
        print(f"{n} is zero")
    else:
        print(f"{n} is positive")

# conditional expression
n = 7
kind = "even" if n % 2 == 0 else "odd"
print(f"{n} is {kind}")

# --- while ----------------------------------------------------------------------------
countdown = 3
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Liftoff! 🚀")

# --- for over a list ------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# --- range ----------------------------------------------------------------------------
print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(5, 0, -1):", list(range(5, 0, -1)))

# --- enumerate ------------------------------------------------------------------------
for i, fruit in enumerate(fruits, start=1):
    print(f"#{i}: {fruit}")

# --- break / continue -----------------------------------------------------------------
for i in range(10):
    if i % 2 == 1:
        continue  # skip odd numbers
    if i > 6:
        break  # stop entirely
    print(f"even: {i}")

# --- for ... else: "no break happened" ------------------------------------------------
for candidate in [4, 6, 9, 10]:
    if candidate % 2 == 1:
        print(f"found an odd number: {candidate}")
        break
else:
    print("no odd numbers")

# --- nested loops ---------------------------------------------------------------------
for row in range(1, 4):
    line = ""
    for col in range(1, 4):
        line += f"{row * col:4}"
    print(line)


# --- match ----------------------------------------------------------------------------
def handle(command: str) -> str:
    match command.split():
        case ["go", direction]:
            return f"going {direction}"
        case ["pick", "up", item]:
            return f"picking up {item}"
        case ["quit" | "exit"]:
            return "bye"
        case []:
            return "say something!"
        case _:
            return f"unknown command: {command!r}"


for cmd in ["go north", "pick up lamp", "exit", "", "dance wildly"]:
    print(f"{cmd!r:16} -> {handle(cmd)}")


def http_status(code: int) -> str:
    match code:
        case 200 | 201:
            return "ok"
        case 404:
            return "not found"
        case n if 500 <= n < 600:
            return "server error"
        case _:
            return "something else"


for code in [200, 404, 503, 302]:
    print(f"{code} -> {http_status(code)}")
