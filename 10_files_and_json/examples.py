"""Lesson 10 examples. Run with: uv run python examples.py

Everything is written inside a temporary folder that's deleted at the end, so this script
leaves no files behind.
"""

import csv
import json
import tempfile
from pathlib import Path

# --- Paths ----------------------------------------------------------------------------
here = Path(__file__).parent
print(f"this script's folder: {here}")
print(f"home: {Path.home()}")
example = Path.home() / "notes" / "todo.txt"
print(f"{example} -> name={example.name!r}, stem={example.stem!r}, suffix={example.suffix!r}")
print(f"parent: {example.parent}, exists? {example.exists()}")
print(f"python files next to this script: {sorted(p.name for p in here.glob('*.py'))}")

with tempfile.TemporaryDirectory() as tmp:
    workdir = Path(tmp)
    print(f"\nworking in temporary folder {workdir}")

    # --- write_text / read_text -------------------------------------------------------
    hello = workdir / "hello.txt"
    hello.write_text("Hello, file!\nSecond line\n", encoding="utf-8")
    print(f"read_text: {hello.read_text(encoding='utf-8')!r}")

    # --- open() with `with` -----------------------------------------------------------
    log = workdir / "log.txt"
    with open(log, "w", encoding="utf-8") as f:
        for i in range(3):
            f.write(f"entry {i}\n")
    with open(log, "a", encoding="utf-8") as f:  # append
        f.write("appended entry\n")
    with open(log, encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(f"  line {number}: {line.rstrip()}")

    # --- Folders ----------------------------------------------------------------------
    nested = workdir / "a" / "b" / "c"
    nested.mkdir(parents=True, exist_ok=True)
    (nested / "deep.txt").write_text("deep!", encoding="utf-8")
    txt_files = sorted(p.relative_to(workdir).as_posix() for p in workdir.rglob("*.txt"))
    print(f"all .txt files: {txt_files}")

    # --- JSON -------------------------------------------------------------------------
    data = {"name": "Ada", "langs": ["python", "rust"], "active": True, "manager": None}
    text = json.dumps(data, indent=2)
    print(f"as JSON:\n{text}")
    settings_file = workdir / "settings.json"
    settings_file.write_text(text, encoding="utf-8")
    loaded = json.loads(settings_file.read_text(encoding="utf-8"))
    print(f"loaded back equal? {loaded == data}; langs = {loaded['langs']}")

    # --- Handling a missing file ------------------------------------------------------
    missing = workdir / "nope.json"
    try:
        config = json.loads(missing.read_text(encoding="utf-8"))
    except FileNotFoundError:
        config = {}
        print(f"{missing.name} doesn't exist yet — starting with {config}")

    # --- CSV --------------------------------------------------------------------------
    people_csv = workdir / "people.csv"
    with open(people_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Ada", "age": 36})
        writer.writerow({"name": "Grace", "age": 85})
    print(f"CSV file contents:\n{people_csv.read_text(encoding='utf-8')}")
    with open(people_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print(f"  {row['name']} will be {int(row['age']) + 1} next year")

print("\ntemporary folder deleted")
