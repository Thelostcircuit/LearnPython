# This code WORKS (test_messy.py passes) but it's badly formatted and has classic mistakes.
# 1. Run `uv run ruff format messy.py` and see how the formatting changes.
# 2. Run `uv run ruff check messy.py` and fix each problem it reports, by hand.
# Don't worry about understanding every line yet — the lessons cover all of it.
import sys
import os
from typing import List,Optional

def average(numbers:List[int])->Optional[float]:
    if len(numbers)==0: return None
    total=0
    for i in range(len(numbers)): total=total+numbers[i]
    return total/len(numbers)

def is_empty(value):
    if value == None:
        return True
    else:
        return False

def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

def find_user(users, name):
    for user in users:
        if user["name"] == name:
            result = user
            return user
    return None
