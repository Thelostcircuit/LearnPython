# Lesson 0 — Setting Up Your Computer for Python

This lesson gets your computer ready to write Python. It takes about 10 minutes. Instructions
are given for **Arch Linux** (and Arch-based distros like CachyOS, EndeavourOS, Manjaro),
**Debian / Ubuntu** (and derivatives like Mint and Pop!_OS), **macOS**, and **Windows**. Pick
your system in each step. At the end, the setup checker should report all green.

## What you'll install

| Thing | What it is |
| --- | --- |
| **uv** | Fast all-in-one Python tool: virtual environments, packages, running tools, and installing Python itself. It's the only thing you install by hand. |
| **Python 3.12+** | The interpreter that runs your code. uv downloads a copy for the course automatically if your system doesn't have a new enough one. |
| **pytest** and **ruff** | The course tools: pytest runs tests, ruff lints and formats. uv installs them into the course's own environment. |
| An **editor** set up for Python | VS Code, Neovim, PyCharm, Zed, or anything with LSP support. |

> Throughout the course, **"the course folder"** means the `LearnPython` folder you unzipped or
> cloned (the one containing this `00_setup` folder). Commands like `cd 00_setup` are run from
> there.

## The one rule: don't install packages into the system Python

On Linux and macOS, the system's Python belongs to the operating system: its own tools depend on
it. If you try `pip install something` globally on Arch, Debian 12+, Ubuntu 23.04+, or with
Homebrew's Python, you'll get an `externally-managed-environment` error. That error is
protecting you. On Windows nothing stops you, but it causes the same mess later.

Instead, every project gets its own **virtual environment** (a `.venv/` folder): a private copy
of Python with its own packages. `uv` creates and manages it for you.

| Instead of... | Use |
| --- | --- |
| `pip install requests` | `uv add requests` (adds to `pyproject.toml` and installs into `.venv`) |
| `python script.py` | `uv run python script.py` (runs inside the project's `.venv`) |
| `pytest` | `uv run pytest` |
| installing a CLI tool globally | `uv tool install <tool>` (each tool gets its own isolated env) |

## Step 1 — Install uv

<details open>
<summary><b>Arch Linux / CachyOS</b></summary>

```sh
sudo pacman -S uv
```

Arch already ships a current Python (`/usr/bin/python3`), and uv will use it.

</details>

<details>
<summary><b>Debian / Ubuntu</b></summary>

Use the official installer. (Debian and Ubuntu don't package uv, or package an old one.)

```sh
sudo apt update
sudo apt install curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

It installs `uv` into `~/.local/bin` and adds that folder to your PATH. **Open a new terminal**
afterwards so the change takes effect.

If your system Python is older than 3.12 (Debian 12 ships 3.11, Ubuntu 22.04 ships 3.10),
that's fine: uv downloads its own Python for the course in Step 2. Leave the system one alone.

</details>

<details>
<summary><b>macOS</b></summary>

With [Homebrew](https://brew.sh):

```sh
brew install uv
```

Or without Homebrew, use the official installer, then **open a new terminal**:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

macOS's built-in `python3` is either missing or an old copy tied to Apple's developer tools.
You don't need it: uv downloads its own Python for the course in Step 2.

</details>

<details>
<summary><b>Windows</b></summary>

Open **PowerShell** and run:

```powershell
winget install --id=astral-sh.uv -e
```

No `winget`? Use the official installer instead:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Close PowerShell and open a new window** afterwards so it picks up the new PATH. You don't need
to install Python from python.org or the Microsoft Store: uv downloads its own Python for the
course in Step 2.

</details>

Check it worked:

```sh
uv --version
```

## Step 2 — Install the course tools

The course's `pyproject.toml` (in the course folder) lists pytest and ruff as dev tools. One
command creates `.venv/` and installs them. If your computer doesn't have Python 3.12 or newer,
uv downloads one first:

```sh
cd LearnPython        # the course folder, wherever you put it
uv sync
```

Try them:

```sh
uv run python --version
uv run pytest --version
uv run ruff --version
```

`uv run` looks upward from the current folder for `pyproject.toml`, so it works from inside any
lesson folder too.

> **Optional: activating the venv.** If you'd rather type `python` and `pytest` directly,
> activate the environment from the course folder:
>
> | Shell | Command |
> | --- | --- |
> | bash / zsh (Linux, macOS) | `source .venv/bin/activate` |
> | fish | `source .venv/bin/activate.fish` |
> | PowerShell (Windows) | `.venv\Scripts\Activate.ps1` |
>
> Your prompt changes to show `(learnpython)`, and `deactivate` undoes it. The lessons use
> `uv run` so they work either way.

## Step 3 — Meet the REPL

The REPL (Read-Eval-Print Loop) is an interactive Python prompt. It's great for quick
experiments. From the course folder:

```sh
uv run python
```

```python
>>> 2 ** 100
1267650600228229401496703205376
>>> "hello".upper()
'HELLO'
>>> help(str.split)     # built-in docs; press q to leave
>>> exit()              # or Ctrl+D (Ctrl+Z then Enter on Windows)
```

Python 3.13+'s REPL has colours, multi-line editing, and history (↑). Keep one open in a spare
terminal while you learn.

## Step 4 — Put uv's tool folder on your PATH

`uv tool install <tool>` puts tools in `~/.local/bin` (`%USERPROFILE%\.local\bin` on Windows).
You won't need this for the course itself, but you will the first time you install a Python CLI
tool, e.g. `uv tool install httpie`.

If you installed uv with the official installer (Debian / Ubuntu, macOS without Homebrew,
Windows), it already did this. Otherwise, run this once, then open a new terminal:

```sh
uv tool update-shell
```

It works for bash, zsh and PowerShell. For **fish**, run this instead:

```fish
mkdir -p ~/.local/bin
fish_add_path ~/.local/bin
```

The `mkdir` matters: `fish_add_path` silently skips folders that don't exist. fish remembers the
path permanently.

## Step 5 — Set up your editor

Pick one. **VS Code** is the easiest place to start if you don't already have a favourite.

<details open>
<summary><b>VS Code</b> (all systems)</summary>

1. Install it:
   - Arch: `sudo pacman -S code`
   - Debian / Ubuntu: download the `.deb` from <https://code.visualstudio.com>, then
     `sudo apt install ./code_*.deb`
   - macOS: `brew install --cask visual-studio-code`, or download it from the website
   - Windows: `winget install Microsoft.VisualStudioCode`
2. Open the Extensions panel (`Ctrl+Shift+X`, or `Cmd+Shift+X` on macOS) and install
   **Python** (by Microsoft) and **Ruff** (by Astral).
3. Open the course folder with *File → Open Folder…*. VS Code should find `.venv` by itself. If
   it asks which interpreter to use, pick the one in `.venv`. (Or open the Command Palette with
   `Ctrl+Shift+P` / `Cmd+Shift+P` → *Python: Select Interpreter*.)
4. Open `00_setup/messy.py`. You should see ruff's warnings underlined.

Useful keys: `F12` goes to definition, hovering shows types and docs, `Ctrl+.` (`Cmd+.`) shows
quick fixes, and `Shift+Alt+F` (`Shift+Option+F`) formats the file.

</details>

<details>
<summary><b>Neovim with LazyVim</b></summary>

LazyVim has a ready-made Python bundle. Its default language server (pyright) needs Node.js. If
you don't have Node installed, tell it to use **basedpyright** instead, which comes with
everything it needs:

1. Open `~/.config/nvim/lua/config/options.lua` and add this line at the bottom:

   ```lua
   vim.g.lazyvim_python_lsp = "basedpyright"
   ```

2. Open Neovim, type `:LazyExtras`, move to **`lang.python`**, press `x` to enable it.
3. Quit and reopen Neovim. Mason downloads basedpyright and ruff. `:Mason` shows progress.
4. From the course folder, open `nvim 00_setup/messy.py`. You should see ruff's warnings as
   diagnostics, and hovering (`K`) over a name shows its type.

Useful keys (`<leader>` is Space):

| Keys | Does |
| --- | --- |
| `K` | Hover: type & docs of the thing under the cursor |
| `gd` | Go to definition (works on standard library code too) |
| `<leader>ca` | Code actions: quick fixes, e.g. "remove unused import" |
| `<leader>cr` | Rename a symbol everywhere |
| `]d` / `[d` | Jump to next / previous problem |
| `<leader>cf` | Format the file (ruff format) |

</details>

<details>
<summary><b>Other editors</b></summary>

- **PyCharm** (JetBrains): a full Python IDE with a free edition. Open the course folder and
  point it at the existing `.venv` interpreter when it asks.
- **Zed**: Python support is built in. Install it from <https://zed.dev> (Arch:
  `sudo pacman -S zed`; macOS: `brew install --cask zed`).
- **Kate** (Linux): its LSP client supports Python. Install a server for it with
  `uv tool install basedpyright` (after Step 4), then enable *Settings → Configure Kate →
  Plugins → LSP Client*.

</details>

The course's `pyproject.toml` already points basedpyright/pyright at `.venv`, so editors can find
pytest etc., and sets strictness to "standard" so it doesn't bury you in warnings while you learn.

## Step 6 — Check everything

From the course folder, run the checker. It only looks, and never installs or changes anything.

**Linux / macOS:**

```sh
00_setup/check_setup.sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy Bypass -File 00_setup\check_setup.ps1
```

Then run the examples:

```sh
cd 00_setup
uv run python examples.py
```

## Exercise — meet `ruff`

`messy.py` has code that *works* (its tests in `test_messy.py` pass) but is badly formatted and
has several classic mistakes. Ruff is Python's linter **and** formatter:

1. `uv run pytest` — passes. The code is "correct"... for now.
2. `uv run ruff format messy.py` — reformats to the standard style. Look at the file again.
3. `uv run ruff check messy.py` — lists problems, each with a rule code (like `F401`). Look any
   code up with `uv run ruff rule F401`.
4. Fix each one **by hand**. Reading the explanation is the point. (`ruff check --fix` can
   auto-fix some, but not yet!)
5. You're done when `ruff check` says `All checks passed!` and `uv run pytest` still passes.

One of the warnings (`B006`) points at a **real bug** that the tests don't catch yet. Read its
explanation carefully. It's one of Python's most famous gotchas.

Compare with `solution.py` afterwards.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `uv: command not found` / `uv is not recognized` | Open a new terminal. Still missing? Re-run the Step 1 installer for your system |
| `error: externally-managed-environment` | You ran `pip install` outside a venv. Use `uv add` / `uv run` instead |
| `ModuleNotFoundError: No module named 'pytest'` | You ran `python`/`pytest` directly without the venv. Use `uv run pytest`, or run `uv sync` first |
| `No pyproject.toml found` / `No project found` | You're outside the course folder. `cd` into it (or into a lesson folder inside it) |
| `Activate.ps1 cannot be loaded because running scripts is disabled` (Windows) | Run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. Or skip activating and use `uv run` |
| `python` opens the Microsoft Store (Windows) | Use `uv run python`. To stop it, turn off the *python.exe* entries under *Settings → Apps → Advanced app settings → App execution aliases* |
| `command not found` after `uv tool install` | Step 4 (PATH), then open a new terminal |
| `./check_setup.sh: Permission denied` | `bash 00_setup/check_setup.sh` |
| Editor shows no Python diagnostics | Open the **course folder** (not a single file) and make sure it's using the `.venv` interpreter. In Neovim, `:LspInfo` shows attached servers and `:Mason` shows installs |
| Editor says it can't find imports (e.g. `pytest`) | Run `uv sync` so `.venv/` exists, then restart the editor |

## Key takeaways

- Never `pip install` into the system Python. Each project gets a `.venv`, managed by `uv`.
- `uv sync` installs a project's dependencies (and Python itself, if needed); `uv run <cmd>`
  runs things inside its `.venv`.
- `ruff format` formats, `ruff check` lints. `pytest` runs tests.
