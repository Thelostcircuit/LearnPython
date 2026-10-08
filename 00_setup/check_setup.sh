#!/usr/bin/env bash
# Checks that this machine is ready for the LearnPython course. Safe to run any time:
# it only looks, it never installs or changes anything.
# (Windows: use check_setup.ps1 instead.)

course_dir="$(cd "$(dirname "$0")/.." && pwd)"
venv="$course_dir/.venv"
green=$'\e[32m'; red=$'\e[31m'; yellow=$'\e[33m'; reset=$'\e[0m'
problems=0

ok()   { echo "  ${green}✔${reset} $1"; }
bad()  { echo "  ${red}✘${reset} $1"; echo "      → $2"; problems=$((problems + 1)); }
warn() { echo "  ${yellow}!${reset} $1"; echo "      → $2"; }

# Which install command to suggest.
fix_uv="curl -LsSf https://astral.sh/uv/install.sh | sh   (Step 1), then open a new terminal"
if [ "$(uname -s)" = Darwin ]; then
    command -v brew >/dev/null && fix_uv="brew install uv   (Step 1)"
elif [ -r /etc/os-release ]; then
    . /etc/os-release
    case " $ID $ID_LIKE " in
        *" arch "*) fix_uv="sudo pacman -S uv   (Step 1)" ;;
    esac
fi

echo "Required"

if command -v uv >/dev/null; then
    ok "$(uv --version)"
else
    bad "uv not installed" "$fix_uv"
fi

if [ -x "$venv/bin/python" ]; then
    if "$venv/bin/python" -c 'import sys; sys.exit(sys.version_info < (3, 12))'; then
        ok "course virtual environment: $("$venv/bin/python" --version)"
    else
        bad "course virtual environment uses $("$venv/bin/python" --version) (need 3.12+)" \
            "cd $course_dir && rm -rf .venv && uv sync   (Step 2)"
    fi
else
    bad "course virtual environment missing" "cd $course_dir && uv sync   (Step 2)"
fi

if [ -x "$venv/bin/pytest" ]; then
    ok "$("$venv/bin/pytest" --version 2>&1 | head -1)"
else
    bad "pytest not installed in the course venv" "cd $course_dir && uv sync   (Step 2)"
fi

if [ -x "$venv/bin/ruff" ]; then
    ok "$("$venv/bin/ruff" --version)"
else
    bad "ruff not installed in the course venv" "cd $course_dir && uv sync   (Step 2)"
fi

echo
echo "Recommended"

case ":$PATH:" in
    *":$HOME/.local/bin:"*) ok "~/.local/bin is on PATH" ;;
    *) warn "~/.local/bin is not on PATH (only matters for 'uv tool install' tools)" \
            "uv tool update-shell   (fish: mkdir -p ~/.local/bin; fish_add_path ~/.local/bin)   (Step 4), then open a new terminal" ;;
esac

nvim_opts="$HOME/.config/nvim/lua/config/options.lua"
lazy_json="$HOME/.config/nvim/lazyvim.json"
if [ -f "$lazy_json" ]; then
    if grep -q 'lazyvim_python_lsp.*basedpyright' "$nvim_opts" 2>/dev/null || command -v node >/dev/null; then
        ok "Neovim can run a Python language server"
    else
        warn "LazyVim would use pyright, which needs Node.js (not installed)" \
             "add  vim.g.lazyvim_python_lsp = \"basedpyright\"  to $nvim_opts   (Step 5)"
    fi
    if grep -q 'lang.python' "$lazy_json"; then
        ok "LazyVim Python extra enabled"
    else
        warn "LazyVim Python extra not enabled" "in nvim: :LazyExtras → lang.python → x   (Step 5)"
    fi
fi

echo
if [ "$problems" -eq 0 ]; then
    echo "${green}All required pieces are installed. Try: cd 00_setup && uv run python examples.py${reset}"
else
    echo "${red}$problems required piece(s) missing — follow the → hints above, then run this again.${reset}"
    exit 1
fi
