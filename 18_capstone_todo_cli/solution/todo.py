"""A command-line todo app.  Try:  uv run python todo.py --help"""

import argparse
import sys
from pathlib import Path

from store import TaskNotFound, TodoList

TODO_FILE = Path("todos.json")


def build_parser() -> argparse.ArgumentParser:
    """Describe the command line. (Complete — read it to see how argparse works.)"""
    parser = argparse.ArgumentParser(prog="todo", description="A tiny todo list.")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="add a task")
    add.add_argument("text", nargs="+", help="what needs doing")  # nargs="+": one or more words

    commands.add_parser("list", help="show all tasks")

    done = commands.add_parser("done", help="mark a task as done")
    done.add_argument("number", type=int, help="the task number shown by `list`")

    remove = commands.add_parser("remove", help="delete a task")
    remove.add_argument("number", type=int)

    commands.add_parser("clear", help="delete all completed tasks")
    return parser


def run(args: argparse.Namespace, todos: TodoList) -> None:
    """Carry out one command."""
    match args.command:
        case "add":
            text = " ".join(args.text)
            number = todos.add(text)
            print(f"Added #{number}: {text}")
        case "list":
            if not todos.tasks:
                print("Nothing to do! 🎉")
                return
            for number, task in enumerate(todos.tasks, start=1):
                print(f"{number}. {task}")
            print(f"{todos.pending_count} of {len(todos.tasks)} remaining")
        case "done":
            task = todos.complete(args.number)
            print(f"Completed #{args.number}: {task.text}")
        case "remove":
            task = todos.remove(args.number)
            print(f"Removed: {task.text}")
        case "clear":
            removed = todos.clear_done()
            print(f"Removed {removed} completed task(s)")


def main(argv: list[str] | None = None, path: Path = TODO_FILE) -> int:
    """Parse arguments, load, run, save. Returns the exit code (0 = success).

    `argv` and `path` are parameters so the tests can call main() directly with fake
    arguments and a temporary file.
    """
    args = build_parser().parse_args(argv)
    todos = TodoList.load(path)
    try:
        run(args, todos)
    except TaskNotFound as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    todos.save(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
