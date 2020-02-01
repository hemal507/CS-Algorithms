import fractionDivision


def test_case1():
    assert fractionDivision.fractionDivision([2, 3], [5, 6]) == [4, 5]


def test_case2():
    assert fractionDivision.fractionDivision([9, 4], [3, 4]) == [3, 1]
