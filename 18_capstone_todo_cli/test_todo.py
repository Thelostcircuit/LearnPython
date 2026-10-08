"""Tests for the todo app. Run: uv run pytest  (or -k store / -k cli for one half)"""

import json

import pytest
from store import Task, TaskNotFound, TodoList
from todo import main

# ---- store.py ------------------------------------------------------------------------


@pytest.fixture
def three() -> TodoList:
    todos = TodoList()
    for text in ["one", "two", "three"]:
        todos.add(text)
    return todos


def test_store_task_str():
    assert str(Task("write code")) == "[ ] write code"
    assert str(Task("write code", done=True)) == "[x] write code"


def test_store_add_returns_number():
    todos = TodoList()
    assert todos.add("first") == 1
    assert todos.add("second") == 2
    assert todos.tasks[0] == Task("first")


def test_store_complete(three):
    task = three.complete(2)
    assert task.text == "two"
    assert three.tasks[1].done
    assert three.pending_count == 2


@pytest.mark.parametrize("bad_number", [0, -1, 4, 100])
def test_store_missing_task_raises(three, bad_number):
    with pytest.raises(TaskNotFound, match=f"#{bad_number}"):
        three.complete(bad_number)
    with pytest.raises(TaskNotFound):
        three.remove(bad_number)


def test_store_remove(three):
    removed = three.remove(1)
    assert removed.text == "one"
    assert [t.text for t in three.tasks] == ["two", "three"]


def test_store_clear_done(three):
    three.complete(1)
    three.complete(3)
    assert three.clear_done() == 2
    assert three.tasks == [Task("two")]


def test_store_save_and_load(tmp_path, three):
    path = tmp_path / "todos.json"
    assert TodoList.load(path) == TodoList()  # missing file → empty list
    three.complete(2)
    three.save(path)
    assert json.loads(path.read_text(encoding="utf-8"))["tasks"][1] == {
        "text": "two",
        "done": True,
    }
    assert TodoList.load(path) == three


# ---- todo.py (the command line) ------------------------------------------------------


def test_cli_full_session(tmp_path, capsys):
    path = tmp_path / "todos.json"
    assert main(["add", "buy", "milk"], path) == 0
    assert main(["add", "learn python"], path) == 0
    assert main(["done", "1"], path) == 0
    assert main(["list"], path) == 0
    out = capsys.readouterr().out
    assert "Added #1: buy milk" in out
    assert "Completed #1: buy milk" in out
    assert "1. [x] buy milk" in out
    assert "2. [ ] learn python" in out
    assert "1 of 2 remaining" in out

    assert main(["clear"], path) == 0
    assert main(["remove", "1"], path) == 0
    out = capsys.readouterr().out
    assert "Removed 1 completed task(s)" in out
    assert "Removed: learn python" in out
    assert TodoList.load(path) == TodoList()


def test_cli_missing_task_is_an_error(tmp_path, capsys):
    path = tmp_path / "todos.json"
    assert main(["done", "9"], path) == 1
    assert "error: there is no task #9" in capsys.readouterr().err


def test_cli_rejects_bad_arguments(tmp_path):
    with pytest.raises(SystemExit):  # argparse exits on invalid input
        main(["done", "abc"], tmp_path / "todos.json")
