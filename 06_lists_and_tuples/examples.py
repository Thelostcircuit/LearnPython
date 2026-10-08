"""Lesson 6 examples. Run with: uv run python examples.py"""

import copy

# --- Creating and reading -------------------------------------------------------------
nums = [3, 1, 4, 1, 5]
print(f"nums = {nums}, len = {len(nums)}")
print(f"nums[0] = {nums[0]}, nums[-1] = {nums[-1]}, nums[1:3] = {nums[1:3]}")
print(f"4 in nums: {4 in nums}")

# --- Changing in place ----------------------------------------------------------------
nums[0] = 10
nums.append(9)
nums.insert(0, 99)
nums.extend([2, 6])
print(f"after changes: {nums}")
nums.remove(99)
last = nums.pop()
print(f"removed 99, popped {last}: {nums}")
print(f"index of 4: {nums.index(4)}, count of 1: {nums.count(1)}")

# --- Sorting --------------------------------------------------------------------------
scores = [70, 95, 82, 61]
ranked = sorted(scores, reverse=True)
print(f"sorted copy: {ranked}, original: {scores}")
scores.sort()
print(f"sorted in place: {scores}")
print(f"what sort() returns: {scores.sort()}")  # None!

words = ["banana", "fig", "cherry", "kiwi"]
print(f"by length: {sorted(words, key=len)}")

# --- Assignment shares, copy copies ---------------------------------------------------
a = [1, 2, 3]
b = a
b.append(4)
print(f"a = {a}  (changed through b!)   a is b: {a is b}")
c = a.copy()
c.append(5)
print(f"a = {a}, c = {c}   a is c: {a is c}")

grid = [[0, 0], [0, 0]]
shallow = grid.copy()
deep = copy.deepcopy(grid)
grid[0][0] = 1
print(f"shallow copy sees inner change: {shallow}; deep copy doesn't: {deep}")

# The classic grid mistake:
bad_grid = [[0] * 3] * 3  # three references to ONE inner list
bad_grid[0][0] = 1
print(f"bad_grid: {bad_grid}")
good_grid = [[0] * 3 for _ in range(3)]  # a list comprehension (lesson 8)
good_grid[0][0] = 1
print(f"good_grid: {good_grid}")

# --- Built-ins ------------------------------------------------------------------------
values = [4, 8, 15, 16, 23, 42]
print(f"sum={sum(values)}, min={min(values)}, max={max(values)}")
print(f"any > 40: {any(v > 40 for v in values)}, all even: {all(v % 2 == 0 for v in values)}")

names = ["ada", "grace", "linus"]
ages = [36, 85, 21]
for name, age in zip(names, ages, strict=True):  # strict: lengths must match
    print(f"  {name} is {age}")

for i, name in enumerate(names):
    print(f"  #{i} {name}")

# --- Tuples ---------------------------------------------------------------------------
point = (3, 4)
x, y = point
print(f"point = {point}, x = {x}, y = {y}")
single = (5,)
not_a_tuple = 5
print(f"type((5,)) = {type(single).__name__}, type((5)) = {type(not_a_tuple).__name__}")
# point[0] = 1  # <- uncomment: TypeError

# --- Unpacking ------------------------------------------------------------------------
first, *rest = [1, 2, 3, 4]
*init, last = [1, 2, 3, 4]
print(f"first={first}, rest={rest}; init={init}, last={last}")

records = [("ada", 36), ("grace", 85)]
for name, age in records:
    print(f"  {name}: {age}")

# --- Lists of lists -------------------------------------------------------------------
matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    print("  " + " ".join(f"{n:3}" for n in row))
print(f"matrix[1][2] = {matrix[1][2]}")
