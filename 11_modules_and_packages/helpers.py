"""A plain module: just a .py file with some functions in it."""

print(f"  (helpers.py top-level code is running — its __name__ is {__name__!r})")

GREETING = "Hello"


def slugify(text: str) -> str:
    """'  Hello World ' -> 'hello-world'"""
    return "-".join(text.lower().split())


def _internal_helper() -> None:
    """The leading underscore says: private, not meant to be imported elsewhere."""


def main() -> None:
    print("helpers.py was run directly, so main() runs.")
    print(slugify("  Try Running Me Directly  "))


if __name__ == "__main__":
    main()
