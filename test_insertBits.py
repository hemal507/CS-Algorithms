import insertBits


def test_case1():
    assert insertBits.insertBits(1024, 1, 6, 17) == 1058


def test_case2():
    assert insertBits.insertBits(11, 1, 2, 2) == 13


def test_case3():
    assert insertBits.insertBits(1, 3, 4, 3) == 25


def test_case4():
    assert insertBits.insertBits(15, 0, 0, 1) == 15


def test_case5():
    assert insertBits.insertBits(15, 3, 3, 0) == 7


def test_case6():
    assert insertBits.insertBits(2147483647, 0, 30, 0) == 0
