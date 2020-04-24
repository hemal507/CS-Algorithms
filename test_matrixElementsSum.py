import matrixElementsSum


def test_case1():
    assert matrixElementsSum.matrixElementsSum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]) == 9


def test_case2():
    assert matrixElementsSum.matrixElementsSum([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]) == 9


def test_case3():
    assert matrixElementsSum.matrixElementsSum([[1, 1, 1], [2, 2, 2], [3, 3, 3]]) == 18


def test_case4():
    assert matrixElementsSum.matrixElementsSum([[0]]) == 0


def test_case5():
    assert matrixElementsSum.matrixElementsSum([[1, 0, 3], [0, 2, 1], [1, 2, 0]]) == 5


def test_case6():
    assert matrixElementsSum.matrixElementsSum([[1], [5], [0], [2]]) == 6


def test_case7():
    assert matrixElementsSum.matrixElementsSum([[1, 2, 3, 4, 5]]) == 15


def test_case8():
    assert matrixElementsSum.matrixElementsSum([[1]]) == 1
