"""Lesson 10 — solutions."""

import json
from pathlib import Path


def count_lines(path: Path) -> int:
    with open(path, encoding="utf-8") as f:
        return sum(1 for _ in f)


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("".join(line + "\n" for line in lines), encoding="utf-8")


def append_line(path: Path, line: str) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def longest_line(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    return max(lines, key=len, default="")


def find_files(folder: Path, suffix: str) -> list[str]:
    return sorted(p.name for p in folder.iterdir() if p.is_file() and p.suffix == suffix)


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def increment_counter(path: Path, name: str) -> int:
    counters = load_json(path)
    counters[name] = counters.get(name, 0) + 1
    save_json(path, counters)
    return counters[name]
