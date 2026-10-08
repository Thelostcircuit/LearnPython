# Lesson 10 — Files, Paths, and JSON

## Paths with `pathlib`

`pathlib.Path` is the modern way to work with file paths. It's cross-platform and much nicer than
string concatenation:

```python
from pathlib import Path

home = Path.home()                    # /home/you
notes = home / "notes" / "todo.txt"   # join with /
notes.name        # 'todo.txt'
notes.stem        # 'todo'
notes.suffix      # '.txt'
notes.parent      # /home/you/notes
notes.exists(); notes.is_file(); notes.is_dir()
Path.cwd()                            # the current working directory
Path(__file__).parent                 # the folder THIS script is in — very useful
```

Listing files:

```python
for p in Path(".").iterdir():         # everything in a folder
for p in Path(".").glob("*.py"):      # matching a pattern
for p in Path(".").rglob("*.md"):     # recursively
```

Creating and deleting: `path.mkdir(parents=True, exist_ok=True)`, `path.unlink()` (delete a
file), `path.rename(new)`.

## Reading and writing — the quick way

```python
text = path.read_text(encoding="utf-8")
path.write_text("hello\n", encoding="utf-8")     # creates or OVERWRITES
```

Always pass `encoding="utf-8"`. Otherwise Python uses the system default, which varies between
machines.

## `open` and `with` — for more control

```python
with open(path, "w", encoding="utf-8") as f:
    f.write("line 1\n")
    f.write("line 2\n")
# the file is closed automatically when the `with` block ends — even if an error happens

with open(path, encoding="utf-8") as f:     # "r" (read) is the default mode
    for line in f:                          # reads one line at a time — fine for huge files
        print(line.rstrip("\n"))
```

Modes: `"r"` read, `"w"` write (truncates!), `"a"` append, `"x"` create (fails if it exists).
Add `"b"` for binary data (`"rb"`, `"wb"`), e.g. images.

`with` is a **context manager**: it guarantees cleanup. Lesson 15 shows how to write your own.

## JSON — structured data as text

JSON maps almost directly onto Python types: objects ↔ `dict`, arrays ↔ `list`, strings, numbers,
`true`/`false` ↔ `True`/`False`, `null` ↔ `None`.

```python
import json

data = {"name": "Ada", "langs": ["python", "rust"], "active": True}

text = json.dumps(data, indent=2)          # dict → JSON string
back = json.loads(text)                    # JSON string → dict

path.write_text(json.dumps(data, indent=2), encoding="utf-8")   # save
loaded = json.loads(path.read_text(encoding="utf-8"))           # load
```

(There's also `json.dump(data, f)` / `json.load(f)` for open file objects.)

Only basic types can be converted. A `set` or your own class needs converting first.

## CSV — spreadsheets as text

```python
import csv

with open("people.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Ada", "age": 36})

with open("people.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):        # each row is a dict of STRINGS
        print(row["name"], int(row["age"]))
```

## Handling missing files

```python
try:
    config = json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    config = {}          # first run — no file yet
```

## Key takeaways

- `Path` objects: join with `/`, inspect with `.name`/`.suffix`/`.exists()`, list with `.glob()`.
- `read_text`/`write_text` for quick jobs; `with open(...) as f:` for line-by-line or appending.
- Always `encoding="utf-8"`.
- `json.dumps`/`json.loads` convert between Python data and JSON text; `csv.DictReader`/`DictWriter`
  for CSV.
