from messy import add_tag, average, find_user, is_empty


def test_average():
    assert average([2, 4, 6]) == 4.0
    assert average([]) is None


def test_is_empty():
    assert is_empty(None)
    assert not is_empty(0)


def test_add_tag():
    assert add_tag("python", []) == ["python"]


def test_find_user():
    users = [{"name": "ada"}, {"name": "grace"}]
    assert find_user(users, "grace") == {"name": "grace"}
    assert find_user(users, "linus") is None


# BONUS: once you've read ruff's explanation of B006, uncomment this test.
# It FAILS on the original code — that's the bug the linter found.
# def test_add_tag_default_is_fresh_each_call():
#     assert add_tag("a") == ["a"]
#     assert add_tag("b") == ["b"]
