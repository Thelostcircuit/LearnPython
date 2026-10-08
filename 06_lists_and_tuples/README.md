# Lesson 6 — Lists and Tuples

## Lists — ordered, changeable collections

```python
nums = [3, 1, 4]
mixed = [1, "two", 3.0, None]    # can mix types (usually you won't)
empty = []

nums[0]        # 3
nums[-1]       # 4
nums[1:]       # [1, 4]        — slicing works just like strings
len(nums)      # 3
4 in nums      # True
```

Unlike strings, lists are **mutable**. You can change them in place:

```python
nums[0] = 10
nums.append(5)          # add to end               [10, 1, 4, 5]
nums.insert(0, 99)      # insert at index          [99, 10, 1, 4, 5]
nums.extend([6, 7])     # add several              [..., 6, 7]
nums.remove(99)         # remove first matching VALUE
last = nums.pop()       # remove & return last item (or nums.pop(i) for index i)
del nums[0]             # delete by index
nums.index(4)           # position of a value (ValueError if missing)
nums.count(4)           # how many times it appears
nums.clear()            # empty it
```

## Sorting

```python
nums.sort()                  # sorts IN PLACE, returns None
nums.sort(reverse=True)
new = sorted(nums)           # returns a NEW sorted list, original untouched
words.sort(key=len)          # sort by a computed key
nums.reverse()               # in place; or reversed(nums) / nums[::-1] for a copy
```

A classic mistake: `nums = nums.sort()` makes `nums` into `None`. `sort()` changes the list and
returns nothing.

## Names point to objects, and copying

```python
a = [1, 2, 3]
b = a          # b is the SAME list, not a copy!
b.append(4)
print(a)       # [1, 2, 3, 4]  ← surprise

c = a.copy()   # or list(a), or a[:] — a new list (a "shallow" copy)
```

This is the most important thing to understand about Python data: **assignment never copies**.
It attaches another name to the same object. `a is b` tells you if two names share one object.

Nested lists need `copy.deepcopy()` to copy all the inner lists too.

## Useful built-ins on lists

`sum`, `min`, `max`, `len`, `sorted`, `reversed`, `any` (is anything truthy?), `all` (is
everything truthy?), `enumerate`, `zip`:

```python
names = ["ada", "grace"]
ages = [36, 85]
for name, age in zip(names, ages):
    print(name, age)
```

## Tuples — ordered, **unchangeable** collections

```python
point = (3, 4)
single = (5,)          # the comma makes it a tuple — (5) is just 5 in brackets
x, y = point           # unpacking
point[0]               # 3
point[0] = 1           # ❌ TypeError — tuples are immutable
```

Use a **tuple** for a fixed group of related values (a coordinate, a record, a function returning
two things). Use a **list** for a variable-length collection of similar things.

Tuples can be dictionary keys and set members (lesson 7); lists can't.

## Unpacking

```python
first, second = [1, 2]
first, *rest = [1, 2, 3, 4]          # first=1, rest=[2, 3, 4]
*init, last = [1, 2, 3, 4]           # init=[1, 2, 3], last=4
for name, age in [("ada", 36), ("grace", 85)]:
    ...
```

## Key takeaways

- Lists are mutable: `append`, `insert`, `pop`, `remove`, `sort`...
- `sort()` changes in place and returns `None`; `sorted()` returns a new list.
- Assignment shares the object; use `.copy()` to get an independent list.
- Tuples are immutable fixed groups; unpack them with `a, b = pair` and `first, *rest = items`.
