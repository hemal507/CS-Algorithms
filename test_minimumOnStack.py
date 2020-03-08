import minimumOnStack


def test_case1():
    assert minimumOnStack.minimumOnStack(
        ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]) == [10, 5, 5, 5, 10]


def test_case2():
    assert minimumOnStack.minimumOnStack(
        ["push 10", "min", "pop", "push 3", "min", "push 5", "pop", "push 3", "min", "pop"]) == [10, 3, 3]


def test_case3():
    assert minimumOnStack.minimumOnStack(["push 10"]) == []


def test_case4():
    assert minimumOnStack.minimumOnStack(["push 10", "pop"]) == []
