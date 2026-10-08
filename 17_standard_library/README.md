# Lesson 17 — A Tour of the Standard Library

Python's motto is "batteries included". Before installing a package or writing something
yourself, check whether the standard library already does it. Here are the modules you'll reach
for most.

## `collections` — better containers

```python
from collections import Counter, defaultdict, deque, namedtuple

Counter("mississippi")                  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
Counter(words).most_common(3)           # the 3 most frequent, as (item, count) pairs

groups = defaultdict(list)              # missing keys start as list()
groups["a"].append("apple")             # no setdefault needed

recent = deque(maxlen=3)                # a list-like queue; old items fall off the front
recent.append(1); recent.appendleft(0); recent.popleft()

Point = namedtuple("Point", ["x", "y"]) # a lightweight immutable record (or use a dataclass)
```

## `datetime` — dates and times

```python
from datetime import date, datetime, timedelta

today = date.today()
d = date.fromisoformat("2026-09-23")
d + timedelta(days=30)                  # date arithmetic
(date(2026, 12, 25) - d).days           # days between
d.strftime("%A %d %B %Y")               # 'Wednesday 23 September 2026'
datetime.now().isoformat(timespec="seconds")
datetime.strptime("23/09/2026", "%d/%m/%Y")   # parse a custom format
```

Time zones: `from zoneinfo import ZoneInfo; datetime.now(ZoneInfo("America/New_York"))`.

## `re` — regular expressions

Patterns for searching and validating text. Always use raw strings (`r"..."`):

```python
import re

re.findall(r"\d+", "a1b22c333")                 # ['1', '22', '333']
re.search(r"(\w+)@(\w+)\.com", text)            # first match or None; .group(1) etc.
re.fullmatch(r"\d{3}-\d{4}", "555-1234")        # does the WHOLE string match?
re.sub(r"\s+", " ", "too    many   spaces")     # replace
```

| Pattern | Matches |
| --- | --- |
| `\d` `\w` `\s` | digit, word char (letter/digit/_), whitespace |
| `.` | any character |
| `*` `+` `?` `{2,4}` | 0+, 1+, 0 or 1, 2 to 4 of the previous |
| `[abc]` `[^abc]` `[a-z]` | one of / none of / range |
| `^` `$` | start / end |
| `( )` | capture group |

Regexes are powerful but hard to read. Use string methods when they're enough.

## `random`

```python
import random
random.randint(1, 6)            # dice roll, inclusive
random.choice(["a", "b"])
random.shuffle(items)           # in place
random.sample(range(100), 5)    # 5 unique picks
rng = random.Random(42)         # a seeded generator: same "random" results every run (great for tests)
```

(For passwords or tokens use `secrets`, not `random`.)

## `functools`

```python
from functools import cache, partial, reduce

@cache                                  # memoise (lesson 15)
def fib(n): ...

int_from_binary = partial(int, base=2)  # pre-fill some arguments
int_from_binary("1010")                 # 10

reduce(lambda acc, x: acc * x, [1, 2, 3, 4])   # 24 — fold a list into one value
```

## And more worth knowing

| Module | For |
| --- | --- |
| `statistics` | `mean`, `median`, `mode`, `stdev` |
| `math` | `sqrt`, `ceil`, `floor`, `gcd`, `isclose`, `inf`, `pi` |
| `itertools` | lesson 14 |
| `pathlib`, `json`, `csv` | lesson 10 |
| `textwrap` | `wrap`, `fill`, `dedent`, `shorten` |
| `string` | `ascii_letters`, `digits`, `punctuation` |
| `sys` / `os` | `sys.argv`, `sys.exit`, `os.environ` |
| `subprocess` | run other programs |
| `shutil` | copy/move/delete folders |
| `sqlite3` | a full SQL database in a file |
| `argparse` | command-line interfaces (lesson 18) |
| `logging` | proper logging instead of `print` |
| `urllib.request` / `http.server` | basic HTTP (most people use `httpx`/`requests` from PyPI) |
| `unittest.mock` | fake objects for tests |

## Key takeaways

- `Counter` for counting, `defaultdict` for grouping, `deque` for queues and "last N".
- `datetime`/`timedelta` for dates; `re` for patterns; `random.Random(seed)` for repeatable
  randomness.
- Check the standard library before writing it yourself.
