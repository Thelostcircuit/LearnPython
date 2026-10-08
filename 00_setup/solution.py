# Lesson 0 — solution: messy.py after `ruff format` and fixing every `ruff check` problem.
# (F401 = unused import, I001 = unsorted imports: the unused `sys` and `os` are just deleted.)


# UP035 / UP006 / UP045 — modern syntax: list[int] instead of typing.List[int], and X | None
# instead of Optional[X]. No import from `typing` needed any more.
def average(numbers: list[int]) -> float | None:
    # (`ruff format` already split the one-line `if ...: return None`, which ruff calls E701)
    if len(numbers) == 0:
        return None
    # (the loop is fine for ruff, but `sum(numbers)` is the Pythonic way — see lesson 8)
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def is_empty(value) -> bool:
    # E711 — compare to None with `is`, not `==`
    # SIM103 — `if cond: return True else: return False` is just `return cond`
    return value is None


# B006 — a mutable default argument is created ONCE, when the function is defined, and then
# shared by every call. So add_tag("a") then add_tag("b") returned ["a", "b"]!
# The standard fix is a None default, and a fresh list inside the function.
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


def find_user(users: list[dict], name: str) -> dict | None:
    for user in users:
        if user["name"] == name:
            return user  # F841 — `result` was assigned but never used
    return None
