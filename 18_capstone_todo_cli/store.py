"""The todo list itself, and saving/loading it as JSON.

Task NUMBERS shown to the user start at 1, but list INDEXES start at 0 — be careful!

The JSON file looks like:
    {"tasks": [{"text": "buy milk", "done": false}, {"text": "learn python", "done": true}]}
"""

# ruff: noqa: F401 — some imports are only used once you've written your code

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path


class TaskNotFound(Exception):
    """Raised when the user refers to a task number that doesn't exist."""

    def __init__(self, number: int) -> None:
        super().__init__(f"there is no task #{number}")
        self.number = number


@dataclass
class Task:
    text: str
    done: bool = False

    def __str__(self) -> str:
        """ "[x] text" when done, "[ ] text" when not."""
        raise NotImplementedError


@dataclass
class TodoList:
    tasks: list[Task] = field(default_factory=list)

    def add(self, text: str) -> int:
        """Add a new (not done) task and return its number (1-based)."""
        raise NotImplementedError

    def _index(self, number: int) -> int:
        """Convert a 1-based task number to a list index, or raise TaskNotFound(number).
        (A helper for the next three methods. Watch out for number 0 and negatives!)"""
        raise NotImplementedError

    def complete(self, number: int) -> Task:
        """Mark task `number` as done and return it."""
        raise NotImplementedError

    def remove(self, number: int) -> Task:
        """Remove task `number` and return it."""
        raise NotImplementedError

    def clear_done(self) -> int:
        """Remove every completed task; return how many were removed.
        Hint: rebuild self.tasks with a list comprehension."""
        raise NotImplementedError

    @property
    def pending_count(self) -> int:
        """How many tasks are not done yet."""
        raise NotImplementedError

    def save(self, path: Path) -> None:
        """Write {"tasks": [...]} as pretty JSON. Hint: dataclasses.asdict(task) gives a dict."""
        raise NotImplementedError

    @classmethod
    def load(cls, path: Path) -> "TodoList":
        """Read the file back into a TodoList. A missing file means an empty list, not an error.
        Hint: Task(**task_dict) builds a Task from a dict."""
        raise NotImplementedError
