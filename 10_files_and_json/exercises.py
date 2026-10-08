"""Lesson 10 exercises. Replace each `raise NotImplementedError`, then run `uv run pytest`.

The tests use pytest's `tmp_path` — a fresh temporary folder per test — so nothing is written
into your lesson folder.
"""

import json
from pathlib import Path


def count_lines(path: Path) -> int:
    """How many lines are in the file?"""
    raise NotImplementedError


def write_lines(path: Path, lines: list[str]) -> None:
    """Write each string on its own line (each ending with a newline)."""
    raise NotImplementedError


def append_line(path: Path, line: str) -> None:
    """Add one line to the end of the file (create the file if it doesn't exist)."""
    raise NotImplementedError


def longest_line(path: Path) -> str:
    """The longest line in the file, without its trailing newline. "" for an empty file."""
    raise NotImplementedError


def find_files(folder: Path, suffix: str) -> list[str]:
    """Names of the files directly inside `folder` ending with `suffix` (e.g. ".py"), sorted."""
    raise NotImplementedError


def save_json(path: Path, data: dict) -> None:
    """Save data as pretty JSON (indent=2)."""
    raise NotImplementedError


def load_json(path: Path) -> dict:
    """Load a JSON file. If the file doesn't exist, return an empty dict instead."""
    raise NotImplementedError


def increment_counter(path: Path, name: str) -> int:
    """Keep named counters in a JSON file: load it (empty if missing), add 1 to counter `name`
    (starting from 0), save it, and return the new value. Reuse load_json and save_json!"""
    raise NotImplementedError


# ---- Tests (you don't need to change anything below) ---------------------------------


def test_count_lines(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("one\ntwo\nthree\n", encoding="utf-8")
    assert count_lines(f) == 3


def test_write_lines(tmp_path):
    f = tmp_path / "out.txt"
    write_lines(f, ["alpha", "beta"])
    assert f.read_text(encoding="utf-8") == "alpha\nbeta\n"


def test_append_line(tmp_path):
    f = tmp_path / "log.txt"
    append_line(f, "first")
    append_line(f, "second")
    assert f.read_text(encoding="utf-8") == "first\nsecond\n"


def test_longest_line(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("short\nthe longest one\nmid\n", encoding="utf-8")
    assert longest_line(f) == "the longest one"
    empty = tmp_path / "empty.txt"
    empty.write_text("", encoding="utf-8")
    assert longest_line(empty) == ""


def test_find_files(tmp_path):
    for name in ["b.py", "a.py", "notes.md"]:
        (tmp_path / name).write_text("", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "c.py").write_text("", encoding="utf-8")
    assert find_files(tmp_path, ".py") == ["a.py", "b.py"]


def test_json_round_trip(tmp_path):
    f = tmp_path / "data.json"
    data = {"name": "Ada", "langs": ["python"], "active": True, "boss": None}
    save_json(f, data)
    assert '\n  "name": "Ada"' in f.read_text(encoding="utf-8")  # pretty-printed
    assert load_json(f) == data
    assert load_json(tmp_path / "missing.json") == {}
    assert json.loads(f.read_text(encoding="utf-8")) == data


def test_increment_counter(tmp_path):
    f = tmp_path / "counters.json"
    assert increment_counter(f, "visits") == 1
    assert increment_counter(f, "visits") == 2
    assert increment_counter(f, "errors") == 1
    assert load_json(f) == {"visits": 2, "errors": 1}
