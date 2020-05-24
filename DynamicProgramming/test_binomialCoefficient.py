from DynamicProgramming import binomialCoefficient


def test_case1():
    assert binomialCoefficient.binomialCoefficient(5, 2) == 10


def test_case2():
    assert binomialCoefficient.binomialCoefficient(4, 2) == 6


def test_case3():
    assert binomialCoefficient.binomialCoefficient(2, 0) == 1


def test_case4():
    assert binomialCoefficient.binomialCoefficient(2, 1) == 2


def test_case5():
    assert binomialCoefficient.binomialCoefficient(50, 10) == 10272278170
