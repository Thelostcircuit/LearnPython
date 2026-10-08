"""Lesson 8 examples. Run with: uv run python examples.py"""

import sys

nums = list(range(10))

# --- Loop vs comprehension ------------------------------------------------------------
squares_loop = []
for n in nums:
    if n % 2 == 0:
        squares_loop.append(n * n)
squares = [n * n for n in nums if n % 2 == 0]
print(f"loop: {squares_loop}")
print(f"comp: {squares}")

# --- The four kinds -------------------------------------------------------------------
words = ["apple", "banana", "cherry", "date"]
print(f"list: {[w.upper() for w in words]}")
print(f"set:  {sorted({len(w) for w in words})}")
lengths = {w: len(w) for w in words}
print(f"dict: {lengths}")
gen = (len(w) for w in words)
print(f"generator object: {gen}")
print(f"...consumed by sum(): {sum(gen)}")

# --- if/else choosing the value -------------------------------------------------------
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
print(f"labels: {labels}")

# --- Nested ---------------------------------------------------------------------------
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"pairs: {pairs}")
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [item for row in matrix for item in row]
print(f"flat: {flat}")
grid = [[0] * 3 for _ in range(2)]
print(f"grid: {grid}")

# --- Generator expressions are lazy ---------------------------------------------------
as_list = [n * n for n in range(100_000)]
as_gen = (n * n for n in range(100_000))
print(f"list uses {sys.getsizeof(as_list):,} bytes, generator uses {sys.getsizeof(as_gen)} bytes")
print(f"sum of squares below 100,000: {sum(n * n for n in range(100_000)):,}")

lines = ["code", "# comment", "more code"]
print(f"any comment lines? {any(line.startswith('#') for line in lines)}")
print(f"all lowercase? {all(line == line.lower() for line in lines)}")

# --- Friends: enumerate, zip, sorted, max with key ------------------------------------
names = ["ada", "grace", "linus"]
ages = [36, 85, 21]
print(f"numbered: {[f'{i}. {n}' for i, n in enumerate(names, start=1)]}")
print(f"zipped: {list(zip(names, ages, strict=True))}")
print(f"as dict: {dict(zip(names, ages, strict=True))}")

people = [{"name": n, "age": a} for n, a in zip(names, ages, strict=True)]
print(f"oldest: {max(people, key=lambda p: p['age'])['name']}")
print(f"by age: {[p['name'] for p in sorted(people, key=lambda p: p['age'])]}")
by_name = {p["name"]: p for p in people}
print(f"lookup grace: {by_name['grace']}")

# --- map / filter (older style) -------------------------------------------------------
print(f"map:    {list(map(str.upper, names))}")
print(f"filter: {list(filter(lambda n: n > 30, ages))}")
print(f"same with comprehensions: {[n.upper() for n in names]}, {[a for a in ages if a > 30]}")
