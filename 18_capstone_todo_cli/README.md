# Lesson 18 — Capstone: a Todo CLI

Time to put it all together. You'll finish a small command-line todo app that saves tasks to a
JSON file:

```sh
$ uv run python todo.py add "Learn generators"
Added #1: Learn generators
$ uv run python todo.py add "Build something cool"
Added #2: Build something cool
$ uv run python todo.py done 1
Completed #1: Learn generators
$ uv run python todo.py list
1. [x] Learn generators
2. [ ] Build something cool
1 of 2 remaining
$ uv run python todo.py remove 1
Removed: Learn generators
$ uv run python todo.py clear
Removed 0 completed task(s)
$ uv run python todo.py --help
```

Tasks are saved in `todos.json` in the folder you run it from.

## What it uses

| Concept | Where |
| --- | --- |
| `@dataclass` | `Task` in `store.py` |
| Classes, methods, properties | `TodoList` in `store.py` |
| Custom exceptions | `TaskNotFound` in `store.py` |
| Lists, comprehensions, `sum`/`any` | throughout `TodoList` |
| `pathlib` + `json`, handling a missing file | `TodoList.load` / `save` |
| `argparse` subcommands | `build_parser` in `todo.py` (complete — read it!) |
| `match` | `run` in `todo.py` |
| `if __name__ == "__main__"`, exit codes | bottom of `todo.py` |
| pytest: `tmp_path`, `capsys`, `raises` | `test_todo.py` |

## Layout

```
store.py      — Task + TodoList: the logic and saving/loading   (TODOs)
todo.py       — command-line interface                          (some TODOs in run())
test_todo.py  — tests for both                                  (complete)
solution/     — a complete working version
```

## Steps

After each step, run `uv run pytest` and watch more tests pass.

1. **Read `todo.py` first**, especially `build_parser()`, to see how `argparse` turns
   `todo.py done 3` into `args.command == "done"` and `args.number == 3`.
2. **`store.py`**: fill in the `Task` and `TodoList` methods. `uv run pytest -k store` runs just
   those tests.
3. **`todo.py`**: `add` and `list` in `run()` are done as examples. Write `done`, `remove` and
   `clear` the same way.
4. **Try it for real.**

Stuck? Compare with the matching file in `solution/`. To try the reference version, run
`uv run python solution/todo.py list`.

## Stretch goals

- `edit <n> <new text>` command.
- Priorities: `add --priority high "..."`, and sort `list` by priority.
- `list --pending` / `list --done` filters.
- Due dates stored as ISO strings, with `list` highlighting overdue tasks (`datetime.date`).
- Colours: try the `rich` package (`uv add rich`). It makes tables easy too.
- Store the file in your home folder: `Path.home() / ".todos.json"`.
- Use `sqlite3` instead of JSON.
- Rewrite the CLI with `typer` (`uv add typer`), which builds on type hints.
- Package it so `todo` works as a real command: look up `[project.scripts]` in `pyproject.toml`
  and `uv tool install .`

## What next, after this course?

- The official [Python Tutorial](https://docs.python.org/3/tutorial/) fills in the corners.
- *Fluent Python* (Luciano Ramalho) is the best book for going from "can write Python" to
  "writes idiomatic Python".
- Build something you actually want: automate a chore, a web app (`fastapi` or `flask`), a data
  notebook (`jupyter` + `pandas` / `polars`), a game (`pygame`), or scripts for your own notes.
- [Advent of Code](https://adventofcode.com) puzzles are great practice.
