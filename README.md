# Learn Python 🐍

A hands-on Python course split into 19 lessons (0–18). Each lesson is a folder with:

| File | What it is |
| --- | --- |
| `README.md` | **The lesson.** Read this first. |
| `examples.py` | Runnable examples of everything in the lesson. Read it, run it, change it. |
| `exercises.py` | **Your turn.** Functions that `raise NotImplementedError` for you to fill in, with tests at the bottom. |
| `solution.py` | A worked answer for the exercises. Don't peek until you've tried! |

## Setup (one time)

**Start with [`00_setup`](00_setup/README.md).** It walks through installing `uv` (which
brings Python with it), the course tools (pytest, ruff), and editor support on **Arch Linux,
Debian / Ubuntu, macOS, or Windows**, and includes a checker script. From the course folder:

```sh
uv sync
00_setup/check_setup.sh                                          # Linux / macOS
powershell -ExecutionPolicy Bypass -File 00_setup\check_setup.ps1  # Windows
```

## How to work through a lesson

```sh
cd 01_hello_python
uv run python examples.py   # run the examples
uv run pytest               # run the exercise tests — they fail until you solve them
```

1. Read `README.md`.
2. Read `examples.py`, then run it. Change things and see what happens. Break it on purpose and
   read the error — Python's tracebacks tell you the file, line, and what went wrong.
3. Open `exercises.py`. Replace each `raise NotImplementedError` with real code.
4. Run `uv run pytest` until everything passes. Useful variations:
   - `uv run pytest -k greet` runs only tests whose name contains "greet"
   - `uv run pytest -x` stops at the first failure
   - `uv run pytest -v` lists each test by name
5. Compare with `solution.py`. There is usually more than one good answer.

> Run `uv run pytest` from **inside a lesson folder**. Every lesson has a file called
> `exercises.py`, so running all lessons at once from the top level makes them clash.

`uv run` finds the course's `pyproject.toml` in the parent folder automatically, so it works from
any lesson folder.

## Lessons

| # | Folder | Topics |
| --- | --- | --- |
| 0 | `00_setup` | uv, virtual environments, pytest, ruff, editor support (Linux, macOS, Windows) |
| 1 | `01_hello_python` | `print`, f-strings, the REPL, comments, `input` |
| 2 | `02_variables_and_types` | Names, `int`/`float`/`bool`/`None`, conversion, arithmetic, dynamic typing |
| 3 | `03_strings` | Indexing, slicing, methods, formatting, immutability |
| 4 | `04_control_flow` | `if`/`elif`, `while`, `for`, `range`, `break`/`continue`, `match` |
| 5 | `05_functions` | `def`, defaults, `*args`/`**kwargs`, keyword-only args, scope, type hints |
| 6 | `06_lists_and_tuples` | Lists, methods, slicing, sorting, tuples, unpacking, mutability |
| 7 | `07_dicts_and_sets` | Dictionaries, iteration, `get`/`setdefault`, sets & set maths |
| 8 | `08_comprehensions` | List/dict/set comprehensions, generator expressions, `enumerate`, `zip`, `sorted(key=...)` |
| 9 | `09_exceptions` | `try`/`except`/`else`/`finally`, `raise`, custom exceptions |
| 10 | `10_files_and_json` | `pathlib`, reading & writing files, `with`, JSON, CSV |
| 11 | `11_modules_and_packages` | `import`, packages, `__name__ == "__main__"`, splitting code into files |
| 12 | `12_classes` | Classes, `__init__`, methods, properties, dunder methods, `@dataclass` |
| 13 | `13_inheritance_and_protocols` | Inheritance, `super()`, abstract classes, duck typing, `Protocol` |
| 14 | `14_iterators_and_generators` | The iterator protocol, `yield`, lazy pipelines, `itertools` |
| 15 | `15_decorators_and_context_managers` | Functions as values, closures, decorators, `with` & `contextmanager` |
| 16 | `16_testing` | pytest in depth: fixtures, `parametrize`, `raises`, `tmp_path` |
| 17 | `17_standard_library` | `collections`, `datetime`, `re`, `random`, `itertools`, `functools` |
| 18 | `18_capstone_todo_cli` | Build a command-line todo app using everything so far |

## When you get stuck

- **Read the traceback from the bottom up.** The last line says what went wrong; the lines above
  show where.
- Try it in the REPL: run `python3` and experiment line by line. `help(str.split)` or `dir(obj)`
  work there too.
- The official [Python Tutorial](https://docs.python.org/3/tutorial/) follows a similar order
  and is an excellent companion.
- The [standard library docs](https://docs.python.org/3/library/) are worth browsing. Python
  comes with a lot built in.

## Found a bug?

If a test looks wrong, an explanation is unclear, or an exercise can't be solved as written, open
an issue: https://github.com/Thelostcircuit/LearnPython/issues

## License

Code (examples, exercises, tests, solutions, setup scripts) is [MIT](LICENSE). The lesson text
is [CC BY 4.0](LICENSE-CONTENT): reuse and adapt it freely, just credit the source.
