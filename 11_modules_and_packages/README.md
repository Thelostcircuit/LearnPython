# Lesson 11 — Modules and Packages

## A module is just a `.py` file

Any Python file is a **module**. If `helpers.py` sits next to your script, you can import it:

```python
import helpers                  # use as helpers.slugify(...)
from helpers import slugify     # use as slugify(...)
from helpers import slugify as make_slug    # rename on import
import helpers as h             # short alias (like `import numpy as np`)
```

Importing **runs the module's top-level code once**, then caches it. Importing again (anywhere)
reuses the same module object.

Avoid `from module import *`. It dumps unknown names into your file and makes it hard to tell
where things came from.

## `if __name__ == "__main__":`

Every module has a `__name__`. It's the module's name when imported, but `"__main__"` when the
file is run directly. This lets a file be both an importable module *and* a runnable script:

```python
def main() -> None:
    print("running as a script")

if __name__ == "__main__":
    main()          # runs for `python helpers.py`, NOT for `import helpers`
```

Use this in every script you write. It's the conventional "main function".

## Packages: folders of modules

A **package** is a folder of modules, usually with an `__init__.py`:

```
geometry/
├── __init__.py      ← runs on `import geometry`; often re-exports the main names
├── shapes.py
└── units.py
```

```python
import geometry.shapes
from geometry.shapes import Circle
from geometry import Circle        # works if __init__.py re-exports it
```

Inside a package, modules can import each other with **relative imports**:

```python
# in geometry/shapes.py
from .units import cm_to_m          # . = this package
from . import units                 # the sibling module itself
```

`__init__.py` typically re-exports a clean public API:

```python
# geometry/__init__.py
from .shapes import Circle, Square
__all__ = ["Circle", "Square"]      # what `from geometry import *` gives (and documents the API)
```

A leading underscore (`_helper`) is the convention for "private, don't import this from
outside". It isn't enforced, but everyone respects it.

## Where does Python look for modules?

In order, the entries of `sys.path`:

1. The folder of the script you ran (that's why `import helpers` finds the file next to it).
2. The standard library.
3. Installed packages (in the active venv's `site-packages`).

**Don't name your files after standard modules.** A `random.py` or `json.py` in your folder will
*shadow* the real one and cause baffling errors.

## The standard library and third-party packages

Python comes "batteries included": `math`, `random`, `datetime`, `json`, `pathlib`,
`collections`, `re`, `itertools`, `csv`, `sqlite3`, `urllib`... (lesson 17 tours the best ones).

For anything else there's [PyPI](https://pypi.org). In a uv project:

```sh
uv add requests          # install + record in pyproject.toml
uv remove requests
```

## Your exercise

This lesson's exercise is a small **package** called `textkit/`. Open the files in it:

1. `textkit/cleaning.py` and `textkit/stats.py`: fill in the functions.
   `stats.py` should *reuse* a function from `cleaning.py` via a relative import.
2. `textkit/__init__.py`: re-export the functions so `from textkit import word_count` works.
3. Create a **new** module, `textkit/fun.py`, from scratch (the tests say what it needs).

Then run `uv run pytest`. The full solution is in `solution/textkit/`.

## Key takeaways

- A `.py` file is a module; a folder of them (with `__init__.py`) is a package.
- `import x` / `from x import y` / `as` aliases. Imports run the module once.
- `if __name__ == "__main__":` separates "run as script" from "imported".
- Relative imports (`from .sibling import f`) inside packages; `__init__.py` shapes the public API.
- Don't shadow standard library module names with your own files.
