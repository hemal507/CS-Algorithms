import arrayPacking


def test_case1():
    assert arrayPacking.arrayPacking([24, 85, 0]) == 21784


def test_case2():
    assert arrayPacking.arrayPacking([23, 45, 39]) == 2567447


def test_case3():
    assert arrayPacking.arrayPacking([1, 2, 4, 8]) == 134480385


def test_case4():
    assert arrayPacking.arrayPacking([5]) == 5


def test_case5():
    assert arrayPacking.arrayPacking([187, 99, 42, 43]) == 724198331
