"""A small pricing module — the code under test for lesson 16.

All money is handled in integer CENTS to avoid floating-point surprises.
One of these functions has a bug. Write tests in exercises.py to find it!
"""


def line_total(price_cents: int, quantity: int) -> int:
    """Price times quantity. Raises ValueError if quantity is negative."""
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    return price_cents * quantity


def bulk_discount_percent(quantity: int) -> int:
    """Discount tiers: 50 or more items → 10% off; 10 or more → 5% off; otherwise 0."""
    if quantity >= 10:
        return 5
    elif quantity >= 50:
        return 10
    return 0


def discounted_line_total(price_cents: int, quantity: int) -> int:
    """line_total with the bulk discount applied (rounded down to whole cents)."""
    total = line_total(price_cents, quantity)
    return total * (100 - bulk_discount_percent(quantity)) // 100


def format_price(cents: int) -> str:
    """1234 -> "$12.34",  5 -> "$0.05" """
    return f"${cents // 100}.{cents % 100:02}"


def parse_price(text: str) -> int:
    """ "$12.34" -> 1234,  "12" -> 1200.  Raises ValueError for anything unparseable."""
    cleaned = text.strip().removeprefix("$")
    dollars, _, cents = cleaned.partition(".")
    if not dollars.isdigit() or (cents and (not cents.isdigit() or len(cents) != 2)):
        raise ValueError(f"not a price: {text!r}")
    return int(dollars) * 100 + int(cents or 0)
