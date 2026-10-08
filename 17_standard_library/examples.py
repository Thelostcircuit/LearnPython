"""Lesson 17 examples. Run with: uv run python examples.py"""

import math
import random
import re
import statistics
import textwrap
from collections import Counter, defaultdict, deque, namedtuple
from datetime import date, datetime, timedelta
from functools import cache, partial, reduce
from zoneinfo import ZoneInfo

# --- Counter --------------------------------------------------------------------------
letters = Counter("mississippi")
print(f"Counter: {letters}")
print(f"most common 2: {letters.most_common(2)}")
text = "the cat and the hat and the bat"
print(f"top words: {Counter(text.split()).most_common(2)}")
print(f"Counters add up: {Counter('aab') + Counter('abc')}")

# --- defaultdict ----------------------------------------------------------------------
groups = defaultdict(list)
for word in ["apple", "avocado", "banana", "blueberry", "cherry"]:
    groups[word[0]].append(word)
print(f"defaultdict: {dict(groups)}")

# --- deque ----------------------------------------------------------------------------
recent = deque(maxlen=3)
for page in ["home", "about", "blog", "contact"]:
    recent.append(page)
print(f"last 3 pages: {list(recent)}")
queue = deque(["a", "b"])
queue.appendleft("first")
print(f"popleft: {queue.popleft()}, remaining: {list(queue)}")

# --- namedtuple -----------------------------------------------------------------------
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"namedtuple: {p}, p.x = {p.x}, distance = {math.hypot(*p)}")

# --- datetime -------------------------------------------------------------------------
d = date(2026, 9, 23)
print(f"\ndate: {d}, weekday: {d.strftime('%A')}, pretty: {d.strftime('%d %B %Y')}")
print(f"in 30 days: {d + timedelta(days=30)}")
print(f"days until Christmas: {(date(2026, 12, 25) - d).days}")
print(f"parsed: {datetime.strptime('23/09/2026 14:30', '%d/%m/%Y %H:%M')}")
print(f"from ISO: {date.fromisoformat('2000-01-01')}")
meeting = datetime(2026, 9, 23, 15, 0, tzinfo=ZoneInfo("America/New_York"))
in_london = meeting.astimezone(ZoneInfo("Europe/London"))
print(f"meeting: {meeting:%H:%M %Z} in New York = {in_london:%H:%M %Z} in London")

# --- re -------------------------------------------------------------------------------
log = "Contact ada@example.com or grace@navy.mil. Call 555-1234 or 555-9876."
print(f"\nemails: {re.findall(r'[\w.]+@[\w.]+\.\w+', log)}")
print(f"phone numbers: {re.findall(r'\d{3}-\d{4}', log)}")
match = re.search(r"(\w+)@(\w+)", log)
if match:
    print(f"first email user={match.group(1)!r}, domain={match.group(2)!r}")
print(f"fullmatch '12:30': {bool(re.fullmatch(r'\d{2}:\d{2}', '12:30'))}")
print(f"collapse spaces: {re.sub(r'\s+', ' ', 'too    many     spaces')!r}")

# --- random ---------------------------------------------------------------------------
rng = random.Random(42)  # seeded: the same results every time you run this
print(f"\ndice: {[rng.randint(1, 6) for _ in range(5)]}")
print(f"choice: {rng.choice(['rock', 'paper', 'scissors'])}")
cards = list("AKQJ")
rng.shuffle(cards)
print(f"shuffled: {cards}, sample: {rng.sample(range(100), 3)}")


# --- functools ------------------------------------------------------------------------
@cache
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(f"\nfib(90) = {fib(90)}")
from_binary = partial(int, base=2)
print(f"partial(int, base=2)('1010') = {from_binary('1010')}")
print(f"reduce product: {reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])}")

# --- statistics -----------------------------------------------------------------------
scores = [70, 85, 85, 90, 100]
print(f"\nmean={statistics.mean(scores)}, median={statistics.median(scores)}")
print(f"mode={statistics.mode(scores)}")
print(f"stdev={statistics.stdev(scores):.2f}")

# --- textwrap -------------------------------------------------------------------------
long_text = (
    "Python's standard library is large, and learning what's in it saves you from "
    "reinventing wheels."
)
print("\n" + textwrap.fill(long_text, width=40))
print(textwrap.shorten(long_text, width=40, placeholder="..."))
