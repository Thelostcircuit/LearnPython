"""Lesson 7 examples. Run with: uv run python examples.py"""

# --- Dict basics ----------------------------------------------------------------------
ages = {"ada": 36, "grace": 85}
print(f"ages = {ages}")
print(f"ages['ada'] = {ages['ada']}")
ages["linus"] = 21
ages["ada"] = 37  # overwrite
del ages["grace"]
print(f"after changes: {ages}")
print(f"'ada' in ages: {'ada' in ages}, 36 in ages: {36 in ages}  (in checks keys)")
# print(ages["nobody"])  # <- uncomment: KeyError

# --- Safe access ----------------------------------------------------------------------
print(f"get missing: {ages.get('bob')}, with default: {ages.get('bob', 0)}")
ages.setdefault("bob", 50)
ages.setdefault("ada", 999)  # already there, so unchanged
print(f"after setdefault: {ages}")
print(f"pop: {ages.pop('bob')}, pop missing with default: {ages.pop('zed', None)}")

# --- Looping --------------------------------------------------------------------------
for name, age in ages.items():
    print(f"  {name} is {age}")
print(f"keys: {list(ages)}, values: {list(ages.values())}")

# --- Counting -------------------------------------------------------------------------
text = "the cat sat on the mat the end"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(f"counts: {counts}")
most_common = max(counts, key=counts.get)
print(f"most common word: {most_common!r}")

# --- Grouping -------------------------------------------------------------------------
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
by_letter = {}
for w in words:
    by_letter.setdefault(w[0], []).append(w)
print(f"grouped: {by_letter}")

# --- Merging --------------------------------------------------------------------------
defaults = {"theme": "light", "font_size": 12}
overrides = {"theme": "dark"}
settings = defaults | overrides
print(f"merged settings: {settings}")

# --- Nested data ----------------------------------------------------------------------
user = {"name": "ada", "langs": ["python", "rust"], "address": {"city": "London"}}
print(f"{user['name']} lives in {user['address']['city']} and knows {', '.join(user['langs'])}")

# --- Tuples as keys -------------------------------------------------------------------
distances = {("london", "paris"): 344, ("paris", "berlin"): 878}
print(f"london -> paris: {distances[('london', 'paris')]} km")

# --- Sets -----------------------------------------------------------------------------
paint_pots = ["red", "green", "red", "blue"]
colors = set(paint_pots)
print(f"colors = {colors}  (duplicates removed, order not guaranteed)")
colors.add("yellow")
colors.discard("pink")  # no error
print(f"'red' in colors: {'red' in colors}")

empty_dict = {}
empty_set = set()
print(f"type({{}}) = {type(empty_dict).__name__}, type(set()) = {type(empty_set).__name__}")

a = {1, 2, 3}
b = {2, 3, 4}
print(f"a | b = {a | b}")
print(f"a & b = {a & b}")
print(f"a - b = {a - b}")
print(f"a ^ b = {a ^ b}")
print(f"{{1, 2}} <= a: {({1, 2}) <= a}")

python_devs = {"ada", "grace", "guido"}
rust_devs = {"grace", "graydon"}
print(f"knows both: {python_devs & rust_devs}")
print(f"knows only python: {sorted(python_devs - rust_devs)}")

print(f"unique letters in 'mississippi': {sorted(set('mississippi'))}")
