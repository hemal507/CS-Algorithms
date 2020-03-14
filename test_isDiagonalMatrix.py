import isDiagonalMatrix


def test_case1():
    assert isDiagonalMatrix.isDiagonalMatrix([[1, 0, 0], [0, 5, 0], [0, 0, 3]]) == True


def test_case2():
    assert isDiagonalMatrix.isDiagonalMatrix([[1, 0, 0], [0, 5, 0], [2, 0, 3]]) == False


def test_case3():
    assert isDiagonalMatrix.isDiagonalMatrix([[1, 0, 0], [0, 5, 0], [0, 1, 0]]) == False


def test_case4():
    assert isDiagonalMatrix.isDiagonalMatrix([[1, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1000]]) == True


def test_case5():
    assert isDiagonalMatrix.isDiagonalMatrix([[0, 0, 0], [0, 9, 0], [0, 0, 0]]) == True


def test_case6():
    assert isDiagonalMatrix.isDiagonalMatrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == False


def test_case7():
    assert isDiagonalMatrix.isDiagonalMatrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True


def test_case8():
    assert isDiagonalMatrix.isDiagonalMatrix([[0]]) == True
