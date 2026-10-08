"""Lesson 14 examples. Run with: uv run python examples.py"""

import itertools

# --- iter() and next() by hand --------------------------------------------------------
it = iter("abc")
print(f"next: {next(it)}, {next(it)}, {next(it)}")
print(f"next with a default when exhausted: {next(it, 'DONE')}")


# --- A generator function -------------------------------------------------------------
def countdown(n: int):
    print("  (countdown started)")
    while n > 0:
        yield n
        n -= 1
    print("  (countdown finished)")


gen = countdown(3)
print(f"calling countdown(3) gives: {gen}  — nothing has run yet")
for x in gen:
    print(f"  got {x}")
print(f"the generator is now used up: {list(gen)}")


# --- Lazy: only computes what's asked for ---------------------------------------------
def squares():
    n = 0
    while True:  # infinite!
        print(f"    computing {n}²")
        yield n * n
        n += 1


print(f"first 3 squares: {list(itertools.islice(squares(), 3))}")


# --- A pipeline of generators ---------------------------------------------------------
log_lines = [
    "INFO start",
    "",
    "ERROR disk full",
    "INFO retry",
    "ERROR disk still full",
    "   ",
]


def non_blank(lines):
    for line in lines:
        if line.strip():
            yield line


def errors_only(lines):
    for line in lines:
        if line.startswith("ERROR"):
            yield line.removeprefix("ERROR ")


def numbered(items):
    for i, item in enumerate(items, start=1):
        yield f"{i}: {item}"


for entry in numbered(errors_only(non_blank(log_lines))):
    print(f"  {entry}")


# --- yield from -----------------------------------------------------------------------
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # recursion + yield from
        else:
            yield item


print(f"flatten: {list(flatten([1, [2, [3, [4]]], 5]))}")


# --- An iterable class ----------------------------------------------------------------
class Playlist:
    def __init__(self, *songs: str) -> None:
        self.songs = list(songs)

    def __iter__(self):
        yield from self.songs


mix = Playlist("Intro", "Groove", "Outro")
print(f"songs: {[song.upper() for song in mix]}")
print(f"and again (a fresh iterator each time): {list(mix)}")

# --- itertools tour -------------------------------------------------------------------
print(f"count + islice: {list(itertools.islice(itertools.count(10, 5), 4))}")
print(f"chain: {list(itertools.chain([1, 2], 'ab', range(3)))}")
print(f"cycle: {list(itertools.islice(itertools.cycle('RGB'), 7))}")
print(f"takewhile: {list(itertools.takewhile(lambda x: x < 10, [1, 5, 12, 3]))}")
print(f"pairwise: {list(itertools.pairwise([1, 4, 9, 16]))}")
print(f"batched: {list(itertools.batched(range(7), 3))}")
print(f"product: {[''.join(p) for p in itertools.product('ab', repeat=2)]}")
print(f"combinations: {list(itertools.combinations('ABC', 2))}")
print(f"permutations: {len(list(itertools.permutations(range(4))))} orderings of 4 items")

words = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
for letter, group in itertools.groupby(words, key=lambda w: w[0]):
    print(f"  groupby {letter}: {list(group)}")
