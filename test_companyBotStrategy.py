import companyBotStrategy


def test_case1():
    assert companyBotStrategy.companyBotStrategy([[3, 1], [6, 1], [4, 1], [5, 1]]) == 4.5


def test_case2():
    assert companyBotStrategy.companyBotStrategy([[4, 1], [4, -1], [0, 0], [6, 1]]) == 5


def test_case3():
    assert companyBotStrategy.companyBotStrategy([[4, -1], [0, 0], [5, -1]]) == 0


def test_case4():
    assert companyBotStrategy.companyBotStrategy([[3, 1], [6, 1], [4, -1], [5, 1]]) == 4.666666666666667
