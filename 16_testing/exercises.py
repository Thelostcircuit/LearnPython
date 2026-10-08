"""Lesson 16 exercises — this time YOU write the tests.

The code under test is in pricing.py (already written). Replace each
`raise NotImplementedError` below with a real test. One function in pricing.py has a BUG:
a good test will catch it. When it does, fix the bug in pricing.py and watch the test pass.

Run just these tests with:  uv run pytest exercises.py -v
"""

# ruff: noqa: F401 — some imports are only used once you've written your code

import pytest
from pricing import (
    bulk_discount_percent,
    discounted_line_total,
    format_price,
    line_total,
    parse_price,
)

# ---- Tests (this whole section is yours to write) ------------------------------------


def test_line_total_multiplies():
    # e.g. 250 cents x 4 = 1000
    raise NotImplementedError


def test_line_total_zero_quantity():
    raise NotImplementedError


def test_line_total_negative_quantity_raises():
    # use: with pytest.raises(ValueError): ...
    raise NotImplementedError


# Replace this single test with a @pytest.mark.parametrize test covering the discount tiers.
# Think about the EDGES: 0, 9, 10, 49, 50, 51, 1000. What should each give?
def test_bulk_discount_tiers():
    raise NotImplementedError


def test_discounted_line_total():
    # 20 items at 100 cents: 2000 total, 5% off -> 1900
    raise NotImplementedError


@pytest.fixture
def prices():
    """Write a fixture returning a list of (cents, formatted) pairs to reuse below,
    e.g. [(1234, "$12.34"), (5, "$0.05"), ...]"""
    raise NotImplementedError


def test_format_price(prices):
    raise NotImplementedError


def test_parse_price_round_trips(prices):
    # parse_price(format_price(x)) should give back x — check it for every pair
    raise NotImplementedError


def test_parse_price_without_cents():
    raise NotImplementedError


def test_parse_price_rejects_garbage():
    # try several bad inputs: "abc", "$1.2", "1.234", "", "-5"
    raise NotImplementedError
