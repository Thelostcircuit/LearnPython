"""Lesson 16 — solutions. A complete replacement for exercises.py.

THE BUG was in pricing.bulk_discount_percent: it checked `>= 10` before `>= 50`, so an order
of 50+ items matched the first branch and only got 5% off. The parametrized test below catches
it at quantity 50, 51 and 1000. The fix is to check the bigger tier first — see
solution_pricing.py.
"""

import pytest
from pricing import (
    bulk_discount_percent,
    discounted_line_total,
    format_price,
    line_total,
    parse_price,
)

# ---- Tests ---------------------------------------------------------------------------


def test_line_total_multiplies():
    assert line_total(250, 4) == 1000


def test_line_total_zero_quantity():
    assert line_total(999, 0) == 0


def test_line_total_negative_quantity_raises():
    with pytest.raises(ValueError, match="negative"):
        line_total(100, -1)


@pytest.mark.parametrize(
    ("quantity", "expected_percent"),
    [
        (0, 0),
        (9, 0),
        (10, 5),
        (49, 5),
        (50, 10),  # <- fails on the buggy version
        (51, 10),
        (1000, 10),
    ],
)
def test_bulk_discount_tiers(quantity, expected_percent):
    assert bulk_discount_percent(quantity) == expected_percent


def test_discounted_line_total():
    assert discounted_line_total(100, 20) == 1900
    assert discounted_line_total(100, 50) == 4500
    assert discounted_line_total(100, 1) == 100


@pytest.fixture
def prices():
    return [(1234, "$12.34"), (5, "$0.05"), (0, "$0.00"), (100, "$1.00"), (99999, "$999.99")]


def test_format_price(prices):
    for cents, text in prices:
        assert format_price(cents) == text


def test_parse_price_round_trips(prices):
    for cents, _ in prices:
        assert parse_price(format_price(cents)) == cents


def test_parse_price_without_cents():
    assert parse_price("12") == 1200
    assert parse_price(" $7 ") == 700


@pytest.mark.parametrize("bad", ["abc", "$1.2", "1.234", "", "-5", "$", "1.x5"])
def test_parse_price_rejects_garbage(bad):
    with pytest.raises(ValueError):
        parse_price(bad)
